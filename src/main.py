from data_structures.bst import BSTLokasi
from data_structures.graph import GraphRute
from data_structures.stack import Stack
from data_structures.priority_queue import PriorityQueueBantuan

from modules.generate_peta import generate_peta_bencana

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
    
    print('Disaster Response Logistics System  Ketik BANTUAN untuk daftar perintah') 
    # TODO: implementasikan loop CLI 
    # Perintah: KIRIM <depot> <lokasi> <jenis> <jumlah> 
    # PROSES_BANTUAN, RUTE_OPTIMAL <depot> <tujuan> 
    # UPDATE_LEVEL <kode> <level>, TIDAK_TERJANGKAU <depot> 
    # LOG_PENGIRIMAN, LAPORAN_BENCANA, KELUAR 

if __name__ == '__main__': 
    main()