# OCR-WKWK


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

Ada beberapa tahapan yang dilakukan program ini untuk mengenali karakter pada plat nomor kendaraan. berikut diagram nya

* Python - HTML enhanced for web apps!
* Opencv python - awesome web-based text editor


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


