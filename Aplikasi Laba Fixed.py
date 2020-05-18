import sys
from PyQt5 import QtWidgets,QtCore,QtGui
app = QtWidgets.QApplication([])
winma1 = QtWidgets.QMainWindow()
mawin1 = QtWidgets.QWidget()
def sebelum():
    def hash():
        try:
            satu = int(lenei[0].text())
            dua = int(lenei[1].text())
            tiga = int(lenei[2].text())
            empat = int(lenei[3].text())
            if satu < 0 or dua < 0 or tiga <= 0 or empat < 0:
                raise AssertionError
        except ValueError:
            silha.setText("Masukkan Harus Berisikan Angka!!")
            pulsi.setText("Silahkan Coba Lagi!")
        except AssertionError:
            silha.setText("Masukkan Tidak Boleh Terlalu Kecil")
            pulsi.setText("Silahkan Coba Lagi!")
        else:
            resu = dua * satu * tiga
            slap = resu-empat
            if resu > empat:
                lmao = f"Mendapatkan Untung Sebesar Rp.{slap},00"
            elif resu < empat:
                lick = empat-resu
                lmao = f"Mengalami Rugi Sebesar Rp.{lick},00"
            else:
                lmao = "Tidak Mengalami Untung / Rugi"
            silha.setText(f"Hasil Kotor Sebesar Rp.{resu},00 dalam {tiga} hari")
            pulsi.setText(f"Maka Anda {lmao}")
    winma.close()
    viba = QtWidgets.QVBoxLayout()
    heba = QtWidgets.QHBoxLayout()
    firm = QtWidgets.QFormLayout()
    lab1c = QtWidgets.QLabel("Perencanaan Usaha Untuk Masa Depan!")
    lab1c.setAlignment(QtCore.Qt.AlignCenter)
    lenei = []
    for i in range(4):
        i = QtWidgets.QLineEdit()
        lenei.append(i)
    lenei[0].setClearButtonEnabled(True)
    lenei[1].setClearButtonEnabled(True)
    lenei[2].setClearButtonEnabled(True)
    lenei[3].setClearButtonEnabled(True)
    lenei[3].returnPressed.connect(hash)
    pusha = QtWidgets.QPushButton("Hitung")
    pusha.clicked.connect(hash)
    pusho = QtWidgets.QPushButton("Kembali")
    pusho.clicked.connect(utama)
    pic = QtGui.QPixmap("ashiap.png")
    pic = pic.scaledToWidth(250)
    pix = QtWidgets.QLabel()
    pix.setPixmap(pic)
    silha = QtWidgets.QLabel("")
    silha.setContentsMargins(0, 20, 0, 0)
    pulsi = QtWidgets.QLabel("")
    pulsi.setContentsMargins(0, 0, 0, 20)
    firm.addRow(QtWidgets.QLabel("Harga Per Unit (Rp.)"), lenei[0])
    firm.addRow(QtWidgets.QLabel("Banyaknya Unit Per Hari"), lenei[1])
    firm.addRow(QtWidgets.QLabel("Lama Waktu Usaha (Hari)"), lenei[2])
    firm.addRow(QtWidgets.QLabel("Total Modal Keseluruhan (Rp.)"), lenei[3])
    firm.addRow(pusho, pusha)
    firm.addRow(silha)
    firm.addRow(pulsi)
    viba.addWidget(lab1c)
    viba.addLayout(firm)
    heba.addWidget(pix)
    heba.addLayout(viba)
    mawin1.setLayout(heba)
    winma1.setCentralWidget(mawin1)
    winma1.show()
winma2 = QtWidgets.QMainWindow()
mawin2 = QtWidgets.QWidget()
def sesudah():
    def hitung():
        try:
            satu = int(ledit[0].text())
            dua = int(ledit[1].text())
            tiga = int(ledit[2].text())
            if satu < 0 or dua < 0 or tiga <= 0 :
                raise AssertionError
        except ValueError:
            hasil.setText("Masukkan Harus Berisikan Angka!!")
            kesi.setText("Silahkan Coba Lagi!")
        except AssertionError:
            hasil.setText("Masukkan Tidak Boleh Negatif!!")
            kesi.setText("Silahkan Coba Lagi!")
        else:
            resu = (dua-satu)*tiga
            lmao = ""
            if dua>satu :
                lmao = "Mendapatkan Laba"
            elif dua<satu :
                lmao = "Mengalami Kerugian"
            else:
                lmao = "Tidak Mendapatkan Apa-Apa"
            hasil.setText(f"Hasil Bersih Sebesar Rp.{resu},00 dalam {tiga} hari")
            kesi.setText(f"Maka Anda {lmao}")
    winma.close()
    frm = QtWidgets.QFormLayout()
    labi = QtWidgets.QLabel("Perhitungan Setelah Usaha")
    labi.setAlignment(QtCore.Qt.AlignCenter)
    pusi = QtWidgets.QPushButton("Hitung")
    puse = QtWidgets.QPushButton("Kembali")
    pusi.clicked.connect(hitung)
    puse.clicked.connect(utama)
    pic = QtGui.QPixmap("ashiap.png")
    pic = pic.scaledToWidth(250)
    pix = QtWidgets.QLabel()
    pix.setPixmap(pic)
    hasil = QtWidgets.QLabel("")
    hasil.setContentsMargins(0,30,0,0)
    kesi = QtWidgets.QLabel("")
    kesi.setContentsMargins(0,0,0,30)
    ledit = []
    for i in range(3):
        i = QtWidgets.QLineEdit()
        ledit.append(i)
    ledit[0].setClearButtonEnabled(True)
    ledit[1].setClearButtonEnabled(True)
    ledit[2].setClearButtonEnabled(True)
    ledit[2].returnPressed.connect(hitung)
    hbo = QtWidgets.QHBoxLayout()
    frm.addRow(QtWidgets.QLabel("Total Seluruh Modal (Rp.)"), ledit[0])
    frm.addRow(QtWidgets.QLabel("Total Seluruh Hasil (Rp.)"), ledit[1])
    frm.addRow(QtWidgets.QLabel("Lama Waktu Usaha (Hari)"), ledit[2])
    frm.addRow(puse,pusi)
    frm.addRow(hasil)
    frm.addRow(kesi)
    vbo = QtWidgets.QVBoxLayout()
    vbo.addWidget(labi)
    vbo.addLayout(frm)
    hbo.addWidget(pix)
    hbo.addLayout(vbo)
    mawin2.setLayout(hbo)
    winma2.setCentralWidget(mawin2)
    winma2.show()
winma = QtWidgets.QMainWindow()
mawin = QtWidgets.QWidget()
def utama():
    winma1.close()
    winma2.close()
    grid1 = QtWidgets.QGridLayout()
    herb = QtWidgets.QHBoxLayout()
    herb.setContentsMargins(0,0,0,100)
    labtop = QtWidgets.QLabel("Pilih Perhitungan Sebelum atau Sesudah Berwirausaha!")
    labtop.setContentsMargins(0,30,0,0)
    push1 = QtWidgets.QPushButton("Sebelum")
    push2 = QtWidgets.QPushButton("Sesudah")
    push1.clicked.connect(sebelum)
    push2.clicked.connect(sesudah)
    pic = QtGui.QPixmap("ashiap.png")
    pic = pic.scaledToWidth(250)
    pix = QtWidgets.QLabel()
    pix.setPixmap(pic)
    herb.addWidget(push1)
    herb.addWidget(push2)
    hebo = QtWidgets.QHBoxLayout()
    grid1.addWidget(labtop,0,0)
    grid1.addLayout(herb,1,0)
    hebo.addWidget(pix)
    hebo.addLayout(grid1)
    mawin.setLayout(hebo)
    winma.setCentralWidget(mawin)
    winma.show()
winma.setWindowTitle("Aplikasi Laba")
winma1.setWindowTitle("Hitung Masa Depan")
winma2.setWindowTitle("Mengenang Masa Lalu")
ikon = QtGui.QIcon("ashiap.png")
winma.setWindowIcon(ikon)
winma1.setWindowIcon(ikon)
winma2.setWindowIcon(ikon)
if __name__ == '__main__':
    utama()
sys.exit(app.exec_())