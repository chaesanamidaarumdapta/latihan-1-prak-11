class student():
    "Program data Mahasiswa"
    empCount = 0
    
    def init(self, name ,nim, year):
        self.name = name
        self.nim = nim
        self.year = year
        
    def displayInput(self):
        self.name = input("Masukkan Nama mu : ")
        self.nim = input("Masukkan NIM mu : ")
        self.year = input("Masukkan Tahun Angkatan mu : ")
        student.empCount += 1
        
    def displayCount(self):
        print("Total Mahasiswa %d" % student.empCount)
        
    def displayStudent(self):
        print ("Biodata Anda :")
        print ("Nama : ", self.name)
        print ("NIM : ", self.nim)
        print ("Angkatan : ", self.year)
    
        
dataStd = student()
dataStd.displayInput()
dataStd.displayStudent()
print("Total Mahasiswa %d" % student.empCount)