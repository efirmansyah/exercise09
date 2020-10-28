class Segitiga:
    def __init__(self, alas=None, tinggi=None, sisiA=None, sisiB=None, sisiC=None):
        self.alas = alas
        self.tinggi = tinggi
        self.sisiA = sisiA
        self.sisiB = sisiB
        self.sisiC = sisiC
    
    def luasSegitiga(self):
        print(0.5 * self.alas * self.tinggi)

    def kelilingSegitiga(self):
        print(self.sisiA + self.sisiB + self.sisiC)
        
inputAlas= float(input("Masukkan alas:"))
inputTinggi= float(input("Masukkan tinggi:"))

luas = Segitiga(inputAlas,inputTinggi)
luas.luasSegitiga()

keliling= Segitiga(sisiA=10, sisiB= 20, sisiC= 30)

keliling.kelilingSegitiga()

#print("Hasilnya adalah:", {luas.luasSegitiga()})


class savedata:
    def __init__(self):
        self.record = []

    def save(self, nama, jabatan):
        self.record.append({"Nama": nama, "Jabatan": jabatan})
        
    def getData(self):
        return self.record

listdata = savedata()
listdata.save("Asep", "Gubernur")
listdata.save("Dadang", "Bupati")
print(listdata.getData())






    











    


