import xlrd
import xlwt
import pandas
import random




dosya = pandas.read_excel("C:\\Users\Hp\Desktop\\odevlermakine\\shuffle\\Diabetes.xls", header = None)
satir_sayisi, sutun_sayisi = dosya.shape[:2]
karisik_dosya = xlwt.Workbook()
karisik_sayfa = karisik_dosya.add_sheet("Sheet1")
liste = []
sayac = 0
while(True):
    satir_numarasi = random.randint(0, satir_sayisi - 1)
    if satir_numarasi not in liste:
        liste.append(satir_numarasi)
        satir = karisik_sayfa.row(satir_numarasi)
        for sutun in range(sutun_sayisi):
            satir.write(sutun, dosya[sutun][sayac])
        sayac += 1
    if sayac == satir_sayisi:
        break
karisik_dosya.save("C:\\Users\Hp\Desktop\\odevlermakine\\shuffle\\Diabetes_calisma.xls")
    