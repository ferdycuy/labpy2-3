## labpy2-3

# PENGGUNAAN PYCHARM

-  ### *Disini saya akan menjelaskan dahulu cara menggunakan pychram,karena saya akan menggunakan apk Pycharm*
- pertama yang pasti buka pycharm
- kemudian pilih menu file -  new project,seperti gambar dibawah ini

![Screenshot (41)](https://user-images.githubusercontent.com/115714443/200235931-6a59b232-85f8-48f3-97ca-947a2a333c7f.png)

- kemudian Buat 2 buah folder,karena untuk membedakan pratikum2 dan pratikum3
- lalu buat klik menu file - new file kemudian pilih file python,sepert gambar dibawah ini

![Screenshot (42)](https://user-images.githubusercontent.com/115714443/200236375-50c51382-5988-4053-a166-19430024a19d.png)

![Screenshot (43)](https://user-images.githubusercontent.com/115714443/200236965-1108f357-a6bd-4baa-88af-8d5c90cdb358.png)
##### *ini contoh file kosong yang akan kita isi codingan nantinya*


- langkah diatas akan kita gunakan terus untuk menyelesaiakan persoalan-persoalan dibawah ini.

## Tugas Pratikum 2

#### alur algoritma 

- soal:

  program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
  tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
  
- flowchart

![flowchart latihan1](https://user-images.githubusercontent.com/115714443/200234287-2f8b3741-012e-4786-bb26-952b2a01b764.jpg)

 - Kita akan mencoba untuk memasukan coding di Pycharm tadi
 - Sebelumnya buat file dulu yaa,sudah saya jelaskan di atas langkah- langkahnya
 - Berikut untuk codinganya

   Kalian bisa memasukan code dibawah ini
   
```   e = int(input('Masukkan nilai e: '))
f = int(input('Masukkan nilai f: '))
g = int(input('Masukkan nilai g: '))

if e > f and e > g:
  print('e yang terbesar')
elif f > e and f > g:
  print('f yang terbesar')
else:
  print('g yang terbesar') 
  ```
 
- setelah sudah memasukkan code diatas,kemudian run
- Maka hasilnya akan seperti gambar dibawah ini

![Screenshot (37)](https://user-images.githubusercontent.com/115714443/200238266-7eb667a2-d505-4c3f-9b6f-f04119c63b0a.png)

## Tugas Pratikum 3

### Latihan 1

#### alur algoritma latihan 1

- Soal :

  1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
  2. nilai n diisi pada saat runtime
  3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
  4. gunakan fungsi random() yang dapat diimport terlebih dahulu

- Flowchart

![flowchart latihan1](https://user-images.githubusercontent.com/115714443/200326355-694ff69a-fbcc-488e-9243-2c69b4b4569d.png)

- Sebelumnya buat file dulu yaa,sudah saya jelaskan di atas langkah- langkahnya
- Kita akan mencoba untuk memasukan coding di file yang kita buat tadi di apk Pycharm
- Berikut untuk codinganya

  Kalian bisa memasukan code dibawah ini!
  ```
  print("*******latihan1*******")

print ("masukkan nilai N: 5 ")
import random
jumlah = 5
a = 0
for x in range (jumlah) :
    i = random.uniform(.0,.5)
    a+=1
    print('data ke :',a,a,'==>', i)

print("***** Selesai ******")
```
- setelah sudah memasukkan code diatas,kemudian run
- Maka hasilnya akan seperti gambar dibawah ini

![Screenshot (37)](https://user-images.githubusercontent.com/115714443/200327587-bed9a1d3-704f-4baa-b348-cee8a2df94dd.png)
##### *jika hasilnya seperti itu artinya sukses*

### Latihan 2

#### alur algoritma latihan 2

- Soal :

   Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.
Masukkan angka 0 untuk berhenti.

- Flowchart

![flowchart latihan2](https://user-images.githubusercontent.com/115714443/200328138-5551a2f1-4974-48ec-b8f5-71136dfe7dbc.png)

- Buat file baru lagi
- Seperti latihan 1,kita akan memasukan coding di file yang kita buat tadi di apk pycharm ya
- Berikut untuk codinganya

  Kalian masukan code dibawah ini!
```
max=0
while True:
    a=int(input('Masukkan Bilangan = '))
    if max < a:
        max = a
    if a==0:
     break
print('Bilangan Terbesarnya Adalah',max)
```

- setelah sudah memasukkan code diatas,kemudian run
- Maka hasilnya akan seperti gambar dibawah ini

![Screenshot (38)](https://user-images.githubusercontent.com/115714443/200328749-7534bbee-31f7-428c-8f15-4592e6859885.png)

### Progam1

#### alur algoritma progam 1

- soal :

   Buat program sederhana dengan perulangan: program1.py
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.

- Flowchart

![flowchart progam1](https://user-images.githubusercontent.com/115714443/200328958-276c8ce4-a1ba-4ac2-b404-64191f3ef96a.png)

- Buat file baru lagi
- Seperti latihan 1 dan 2,kita akan memasukan coding di file yang kita buat tadi di apk pycharm ya
- Berikut untuk codinganya

  Kalian masukan code dibawah ini!
  ```
  a = 100000000
for x in range (1, 9):
    if(x>=1 and x<=2):
         b=a*0
         print ('Laba bulan ke-',x,' :', b)
    if(x>=3 and x<=4):
        c=a*0.1
        print ('Laba bulan ke-',x, ' :', c)
    if(x>=5 and x<=7) :
        d=a*0.5
        print ('Laba bulan ke-',x, ' :', d)
    if (x==8) :
        e=a*0.3
        print ('Laba bulan ke-',x, ' :', e)
total = b+b+c+c+d+d+d+e
print ('\nTotal : ', total)
```
- setelah sudah memasukkan code diatas,kemudian run
- Maka hasilnya akan seperti gambar dibawah ini

![Screenshot (39)](https://user-images.githubusercontent.com/115714443/200329395-9482ea0e-4563-4388-9226-29e3687a410f.png)

![Screenshot (40)](https://user-images.githubusercontent.com/115714443/200329417-13f2a908-baa7-4c1e-9fea-6d98f5eb74eb.png)

### Selesaii,Selamat mencoba. *Terima kasi*




