# OCR-WKWK
<p align="center">
  <br>
  <img width="450" src="https://raw.githubusercontent.com/muhammadrofiq/OCRWKWK/master/src/img/B3974EGX.jpg">
  <br>
</p>


OCR-WKWK Merupakan project untuk mengenali karakter pada nomor kendaraan Indonesia (wkwk land), program ini dibuat menggunakan bahasa pemrograman python dengan metode KNN dan Haar Cascade. Untuk hasil yang lebih baik anda dapat membuat model haar anda sendiri, dan/atau anda dapat melakukan training kembali model KNN yang telah kami buat. 

  - Kami memberikan model haar cascade dalam bentuk XML yang dihasilkan melalui process pelatihan yang cukup lama
  - Model KNN yang kami berikan hanya model sederhana yang kami latih menggunakan beberapa tipe font plat nomor. 

# The Features!
  - main.py, merupakan program inti untuk mendeteksi karakter pada platnomor
  - Single-cap, pengguna dapat melakukan capturing image menggunakan camera laptop kemudian image tersebut dieksekusi menggunakan main.py
  - Program ini dapat terkoneksi ke arduino 


untuk saat ini program koneksi ke arduino sedang tidak diaktifkan.



### Tech

project ini menggunakan beberapa teknologi, yaitu:

* Python 
* Opencv python 

### Diagram

Ada beberapa tahapan yang dilakukan program ini untuk mengenali karakter pada plat nomor kendaraan.
![alt text](https://github.com/muhammadrofiq/OCRWKWK/blob/master/misc/Alur%20OCR.JPG?raw=true)

* Image input yang diproses akan disegmentasi atau diambil bagian **platnomornya saja** menggunakan model harcascade yang telah dibuat
* Setelah gambar terfokus pada bagian platnomor saja dilakukanlah **praprocessing**, dengan memaksimalkan kontras dan penghalusan citra dengan gaussian blur.
* Langkah selanjutnya adalah mendeteksi karakter yang terdapat pada plat nomor kendaraan. program ini mendeteksi **seluruh kontur** pada citra.
* Kontur yang telah didapatkan akan di **filter** dengan menyaring kontur yang benar benar memiliki **karakteristik seperti huruf dan angka** kemudian mengelompokannya sesuai dengan kemiripan ukuran dengan karakter lain.

Berikut ini merupakandiagram dari fungsi automation gate.
![alt text](https://github.com/muhammadrofiq/OCRWKWK/blob/master/misc/Alur%20Gate%20Automization.JPG?raw=true)

Jika anda ingin mengkoneksikan project ini ke arduino, berikut skema arduino yang di perlu di buat.
![alt text](https://github.com/muhammadrofiq/OCRWKWK/blob/master/misc/Skema%20arduino.png?raw=true)
### Installation


Install Opencv python mengikuti petunjuk ini:
[installation guide](https://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/)
Clone atau download project OCR-WKWK dan extract.
Masuk kedalam directory src dan jalankan program single-cap.py
```sh
$ cd src
$ workon cv
$ python single-cap.py
```

### Notes
Program ini dibuat diatas sistem operasi linux, sehingga ada kemungkinan beberapa fungsi ada yang tidak berjalan pada sistem operasi lain. 

License
----

Ga ada.


