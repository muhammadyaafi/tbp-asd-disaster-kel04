import numpy as np, time, random 

from data_structures.bst import BSTLokasi
from data_structures.graph import GraphRute
from data_structures.stack import Stack
from data_structures.priority_queue import PriorityQueueBantuan

from modules.disaster_system import Bantuan
from modules.generate_peta import generate_peta_bencana
from modules.algoritma_dijkstra import dijkstra_logistik
from modules.reconstruct_path import reconstruct_path

np.random.seed(47) 
random.seed(47) 

LEVEL_BENCANA = {'KRITIS': 1, 'SEDANG': 2, 'RINGAN': 3} 
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA'] 

def main(): 
    bst_lokasi = BSTLokasi() 
    graph = GraphRute() 
    antrian_bantuan = PriorityQueueBantuan() 
    log_kirim = Stack() 
    bantuan_counter = 0 
    
    lokasi_list, edges = generate_peta_bencana(35, 3, seed=47) 
    for lok in lokasi_list: 
        bst_lokasi.insert(lok) 
        graph.tambah_node(lok.kode) 
    for u, v, j, k in edges: 
        graph.tambah_rute(u, v, j, k) 
    
    print('Disaster Response Logistics System | Ketik BANTUAN untuk daftar perintah') 
    # TODO: implementasikan loop CLI 
    # Perintah: KIRIM <depot> <lokasi> <jenis> <jumlah> 
    # PROSES_BANTUAN, RUTE_OPTIMAL <depot> <tujuan> 
    # UPDATE_LEVEL <kode> <level>, TIDAK_TERJANGKAU <depot> 
    # LOG_PENGIRIMAN, LAPORAN_BENCANA, KELUAR 
    while True:

        cmd = input("\n>> ").strip()

        if not cmd:
            continue

        parts = cmd.split()

        perintah = parts[0].upper()

        # ==================================================
        # KIRIM
        # ==================================================

        if perintah == "KIRIM":

            if len(parts) != 5:
                print("Format salah!")
                continue

            depot = parts[1]
            tujuan = parts[2]
            if depot not in graph._adj:
                print("Depot tidak ditemukan!")
                continue
            if tujuan not in graph._adj:
                print("Lokasi tidak ditemukan!")
                continue
            lokasi = bst_lokasi.search(tujuan)
            jenis = parts[3].upper()
            if jenis not in JENIS_BANTUAN:
                print("Jenis bantuan tidak valid!")
                print(f"Bantuan yang Tersedia: {JENIS_BANTUAN}")
                continue
            try:
                jumlah = int(parts[4])
            except ValueError:
                print("Jumlah harus angka!")
                continue

            bantuan_counter += 1

            bantuan = Bantuan(
                bantuan_id=bantuan_counter,
                jenis=jenis,
                jumlah=jumlah,
                asal=depot,
                tujuan=tujuan,
                prioritas=lokasi.level
            )

            antrian_bantuan.enqueue(bantuan)

            print(f"Bantuan masuk antrian prioritas.")
            antrian_bantuan.tampilkan_antrian()

        # ==================================================
        # PROSES_BANTUAN
        # ==================================================

        elif perintah == "PROSES_BANTUAN":

            bantuan = antrian_bantuan.dequeue()

            if bantuan is None:
                print("Antrian kosong!")
                continue

            print("\nBantuan diproses:")
            print(
                f"Mengirim {bantuan.jumlah} "
                f"{bantuan.jenis} "
                f"dari {bantuan.asal} "
                f"ke {bantuan.tujuan}"
            )
            print("\nAntrian tersisa:")
            antrian_bantuan.tampilkan_antrian()

            # simpan ke log stack
            log_kirim.push(bantuan)

        # ==================================================
        # RUTE_OPTIMAL
        # ==================================================

        elif perintah == "RUTE_OPTIMAL":

            if len(parts) != 3:
                print("Format salah!")
                continue

            depot = parts[1]
            tujuan = parts[2]

            if depot not in graph._adj:
                print("Depot tidak ditemukan!")
                continue
            if tujuan not in graph._adj:
                print("Lokasi tidak ditemukan!")
                continue
            dist, parent = dijkstra_logistik(graph, depot)

            if dist[tujuan] == float('inf'):
                print("Lokasi tidak terjangkau!")
                continue

            path = reconstruct_path(parent, tujuan)

            print("\nRute Optimal:")
            print(" -> ".join(path))

            print(f"Total jarak: {dist[tujuan]} km")

        # ==================================================
        # UPDATE_LEVEL
        # ==================================================

        elif perintah == "UPDATE_LEVEL":

            if len(parts) != 3:
                print("Format salah!")
                continue
            
            kode = parts[1]
            lokasi = bst_lokasi.search(kode)
            if lokasi is None:
                print("Lokasi tidak ditemukan!")
                continue
            level_baru = int(parts[2])
            if level_baru not in [1, 2, 3]:
                print("Level harus 1-3!")
                continue

            level_lama = lokasi.level

            bst_lokasi.update_level(kode, level_baru)

            # ubah angka level menjadi teks
            nama_level = {v: k for k, v in LEVEL_BENCANA.items()}

            print("Level berhasil diperbarui.")
            print(
                f"{kode} : "
                f"{nama_level[level_lama]} -> "
                f"{nama_level[level_baru]}"
            )

        # ==================================================
        # TIDAK_TERJANGKAU
        # ==================================================

        elif perintah == "TIDAK_TERJANGKAU":

            if len(parts) != 2:
                print("Format salah!")
                continue

            depot = parts[1]

            visited = graph.bfs_akses(depot)

            semua = set(graph._adj.keys())

            tidak_terjangkau = semua - visited

            print("\nLokasi tidak terjangkau:")

            if not tidak_terjangkau:
                print("Tidak ada")
            else:
                for x in sorted(tidak_terjangkau):
                    print(x)

        # ==================================================
        # LOG_PENGIRIMAN
        # ==================================================

        elif perintah == "LOG_PENGIRIMAN":

            logs = log_kirim.to_list()
            logs.reverse()  # membalik urutan keterangan pengiriman

            if not logs:
                print("Log kosong!")
                continue

            print("\nRiwayat Pengiriman:")

            for nomor, item in enumerate(logs, start=1):

                print(
                    f"{nomor} : "
                    f"{item.jumlah} {item.jenis} "
                    f"dari {item.asal} ke {item.tujuan}"
                )

        # ==================================================
        # LAPORAN_BENCANA
        # ==================================================

        elif perintah == "LAPORAN_BENCANA":

            data = bst_lokasi.inorder()

            print("\nDaftar Lokasi:")

            for lok in data:

                print(
                    f"{lok.kode} | "
                    f"{lok.nama} | "
                    f"Level:{lok.level} | "
                    f"Populasi:{lok.populasi}"
                )

        # ==================================================
        # KELUAR
        # ==================================================

        elif perintah == "KELUAR":

            print("Program selesai.")
            break

        # ==================================================
        # BANTUAN
        # ==================================================

        elif perintah == "BANTUAN":
            print("\nPerintah:")
            print("KIRIM <depot> <lokasi> <jenis> <jumlah>")
            print("PROSES_BANTUAN")
            print("RUTE_OPTIMAL <depot> <tujuan>")
            print("UPDATE_LEVEL <kode> <level>")
            print("TIDAK_TERJANGKAU <depot>")
            print("LOG_PENGIRIMAN")
            print("LAPORAN_BENCANA")
            print("KELUAR")

        # ==================================================
        # COMMAND TIDAK DIKENAL
        # ==================================================

        else:
            print("Perintah tidak dikenali!")
            print("\nPerintah yang tersedia:")
            print("KIRIM <depot> <lokasi> <jenis> <jumlah>")
            print("PROSES_BANTUAN")
            print("RUTE_OPTIMAL <depot> <tujuan>")
            print("UPDATE_LEVEL <kode> <level>")
            print("TIDAK_TERJANGKAU <depot>")
            print("LOG_PENGIRIMAN")
            print("LAPORAN_BENCANA")
            print("KELUAR")

if __name__ == '__main__': 
    main()