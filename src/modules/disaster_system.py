from dataclasses import dataclass 

LEVEL_BENCANA = {'KRITIS': 1, 'SEDANG': 2, 'RINGAN': 3} 
JENIS_BANTUAN = ['MAKANAN', 'AIR', 'OBAT', 'SELIMUT', 'TENDA'] 
  
@dataclass 
class Lokasi: 
    kode: str 
    nama: str 
    level: int 
    populasi: int 
    status: int = 0 
  
@dataclass 
class Bantuan: 
    bantuan_id: int 
    jenis: str 
    jumlah: int 
    asal: str 
    tujuan: str 
    prioritas: int 