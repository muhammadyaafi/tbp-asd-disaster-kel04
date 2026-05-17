import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'src')
    )
)

import time
import random
import numpy as np

from data_structures.stack import Stack
from data_structures.priority_queue import PriorityQueueBantuan
from data_structures.bst import BSTLokasi
from data_structures.graph import GraphRute

from modules.disaster_system import Lokasi, Bantuan
from modules.algoritma_dijkstra import dijkstra_logistik


# =========================================================
# KONFIGURASI UKURAN DATA
# =========================================================

DATASET_SIZES = {
    100: 100,
    1000: 1000,
    10000: 10000
}

random.seed(47)
np.random.seed(47)


# =========================================================
# UTILITAS TIMER
# =========================================================

def ukur_waktu(func, *args, repeat=1):
    """
    Mengukur runtime fungsi.
    Return dalam satuan detik.
    """

    start = time.perf_counter()

    for _ in range(repeat):
        func(*args)

    end = time.perf_counter()

    return (end - start) / repeat


# =========================================================
# GENERATOR DATA
# =========================================================

def generate_lokasi(n):

    lokasi_list = []

    for i in range(n):

        lokasi = Lokasi(
            kode=f"L{i:05d}",
            nama=f"Lokasi-{i}",
            level=random.randint(1, 3),
            populasi=random.randint(100, 10000)
        )

        lokasi_list.append(lokasi)

    return lokasi_list


def generate_bantuan(n):

    bantuan_list = []

    jenis_list = [
        "MAKANAN",
        "AIR",
        "OBAT",
        "SELIMUT",
        "TENDA"
    ]

    for i in range(n):

        bantuan = Bantuan(
            bantuan_id=i,
            jenis=random.choice(jenis_list),
            jumlah=random.randint(1, 100),
            asal="DEPOT_0",
            tujuan=f"L{random.randint(0, n-1):05d}",
            prioritas=random.randint(1, 3)
        )

        bantuan_list.append(bantuan)

    return bantuan_list


def generate_graph(n):

    graph = GraphRute()

    # tambah node
    for i in range(n):
        graph.tambah_node(f"L{i:05d}")

    # graph sederhana terhubung
    for i in range(n - 1):

        u = f"L{i:05d}"
        v = f"L{i+1:05d}"

        jarak = random.randint(1, 50)
        kapasitas = random.randint(1, 10)

        graph.tambah_rute(u, v, jarak, kapasitas)

    # tambah edge random
    extra_edges = n // 2

    for _ in range(extra_edges):

        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)

        if a != b:

            u = f"L{a:05d}"
            v = f"L{b:05d}"

            jarak = random.randint(1, 50)
            kapasitas = random.randint(1, 10)

            graph.tambah_rute(u, v, jarak, kapasitas)

    return graph


# =========================================================
# BENCHMARK STACK
# =========================================================

def benchmark_stack(n):

    stack = Stack()

    data = list(range(n))

    # PUSH
    t_push = ukur_waktu(
        lambda: [stack.push(x) for x in data]
    )

    # POP
    t_pop = ukur_waktu(
        lambda: [stack.pop() for _ in range(n)]
    )

    return t_push, t_pop


# =========================================================
# BENCHMARK PRIORITY QUEUE
# =========================================================

def benchmark_priority_queue(n):

    pq = PriorityQueueBantuan()

    bantuan_list = generate_bantuan(n)

    # ENQUEUE
    t_enqueue = ukur_waktu(
        lambda: [pq.enqueue(b) for b in bantuan_list]
    )

    # DEQUEUE
    t_dequeue = ukur_waktu(
        lambda: [pq.dequeue() for _ in range(n)]
    )

    return t_enqueue, t_dequeue


# =========================================================
# BENCHMARK BST
# =========================================================

def benchmark_bst(n):

    bst = BSTLokasi()

    lokasi_list = generate_lokasi(n)

    # ACAK DATA
    random.shuffle(lokasi_list)

    # INSERT
    t_insert = ukur_waktu(
        lambda: [bst.insert(lok) for lok in lokasi_list]
    )

    # SEARCH
    random_codes = [
        lokasi_list[random.randint(0, n - 1)].kode
        for _ in range(min(100, n))
    ]

    t_search = ukur_waktu(
        lambda: [bst.search(code) for code in random_codes]
    )

    return t_insert, t_search

# =========================================================
# BENCHMARK BFS
# =========================================================

def benchmark_bfs(n):

    graph = generate_graph(n)

    # BFS
    t_bfs = ukur_waktu(
        lambda: graph.bfs_akses("L00000")
    )

    return t_bfs

# =========================================================
# BENCHMARK GRAPH + DIJKSTRA
# =========================================================

def benchmark_graph_dijkstra(n):

    graph = generate_graph(n)

    # DIJKSTRA
    t_dijkstra = ukur_waktu(
        lambda: dijkstra_logistik(
            graph,
            "L00000"
        )
    )

    return t_dijkstra


# =========================================================
# CETAK HASIL
# =========================================================

def print_header():

    print("=" * 80)
    print("BENCHMARK DISASTER RESPONSE LOGISTICS SYSTEM")
    print("=" * 80)


def print_table_header():

    print(
        f"{'UKURAN':<10}"
        f"{'STACK PUSH':<15}"
        f"{'STACK POP':<15}"
        f"{'PQ ENQ':<15}"
        f"{'PQ DEQ':<15}"
        f"{'BST INS':<15}"
        f"{'BST SRC':<15}"
        f"{'BFS:<15'}"
        f"{'DIJKSTRA':<15}"
    )


def print_result_row(
    label,
    push,
    pop,
    enq,
    deq,
    bst_ins,
    bst_src,
    bfs,
    dijkstra
):

    print(
        f"{label:<10}"
        f"{push:<15.6f}"
        f"{pop:<15.6f}"
        f"{enq:<15.6f}"
        f"{deq:<15.6f}"
        f"{bst_ins:<15.6f}"
        f"{bst_src:<15.6f}"
        f"{bfs:<15.6f}"
        f"{dijkstra:<15.6f}"
    )


# =========================================================
# MAIN BENCHMARK
# =========================================================

def main():

    print_header()

    print_table_header()

    for label, n in DATASET_SIZES.items():

        # STACK
        push_time, pop_time = benchmark_stack(n)

        # PRIORITY QUEUE
        enq_time, deq_time = benchmark_priority_queue(n)

        # BST
        bst_insert_time, bst_search_time = benchmark_bst(n)

        #BFS
        bfs_time = benchmark_bfs(n)

        # DIJKSTRA
        dijkstra_time = benchmark_graph_dijkstra(n)

        # CETAK
        print_result_row(
            label,
            push_time,
            pop_time,
            enq_time,
            deq_time,
            bst_insert_time,
            bst_search_time,
            bfs_time,
            dijkstra_time
        )

    print("=" * 80)
    print("Satuan runtime = detik")
    print("=" * 80)


if __name__ == "__main__":
    main()