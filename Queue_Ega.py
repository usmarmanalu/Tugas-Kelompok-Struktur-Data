from datetime import timedelta, datetime
from tim

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def antrian():
    endtime = datetime.now() + timedelta(seconds = 2)
    tanda='n'
    pasien = Queue()
    antrean = Queue ()
    inputan = int(input('Masukan berapa orang yang ingin antri ='))
    for i in range(inputan):
        nama = input('Masukan nama pasien ke %i = '%(i+1))
        pasien.enqueue(nama)
        antrean.enqueue(nama)

    print("Estimasi Jam Pelayanan Pasien")
    while not pasien.isEmpty():
        if not pasien.isEmpty():
            if tanda=='n':
                print(pasien.dequeue(),'akan dilayani pada:', datetime.now())

            else :
                print(pasien.dequeue(),'akan dilayani pada:', endtime)
                endtime = endtime + timedelta(seconds = 2)

    tanda='n'
    print("==========================Antrian=================================")
    while not antrean.isEmpty():
        if not antrean.isEmpty():
            if tanda==0:
                print(antrean.dequeue(),'sedang dilayani')

        else:
            sleep(2)
            print(antrean.dequeue(),'sedang dilayani')

    if antrean.isEmpty():
            print('====================Antrean kosong========================')
            antrian()
antrian()