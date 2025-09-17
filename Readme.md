# Memahami Dasar-Dasar Pemrograman Python by Ananda Fitri Karimah
## Hello, Python
Apa itu Python?  
Python adalah bahasa yang dinamis dan diinterpretasikan (dijalankan melalui bytecode).    

Cara install python bisa lewat website officialnya, atau menggunakan Anaconda. Dan di Anaconda kita bisa membuat virtual environment.    

Kenapa sih harus buat virtual environment?  
Untuk menghindari dependensi hell, dan agar tidak tabrakan antar versi python.    

Kode bisa dicek di folder Code ILT 1  
<a href="https://colab.research.google.com/drive/1-KrKC947ldqzAIPQUWdsJSBY45Yrb8bF?usp=sharing#scrollTo=lqot9q8IYTjE">Google Collab Link</a>

---

# Pengenalan Supervised Learning: Konsep dan Penerapannya by I Nyoman Yoga Saputra
## Hello Machine Learning
Machine learning adalah cabang dari AI, yaitu sebuah kemampuan ketika komputer dapat belajar dari data tanpa perlu diprogram secara eksplisit.
    
## Jenis - Jenis Machine Learning
- Supervised Learning  
Machine learning yang belajarnya sudah ada target.
- Unsupervised Learning  
Machine learning yang belajarnya tanpa target, sehingga ia harus membuat target/cluster itu sendiri.
- Reinforcement Learning  
Machine learning yang belajar secara berkelanjutan.
  
## Jenis - Jenis Supervised Learning
Kasus umum penggunaan supervised learning adalah:
- Model Regression (regresi) memprediksi nilai numerik dari banyak kemungkinan angka.
- Model Classification (klasifikasi) memprediksi kemungkinan suatu data termasuk ke dalam suatu kategori.
  
Epoch: 1 kali pengulangan pelatihan

### Regression Model
- Linear Regression
- Polynomial Regression
- Support Vector Regression
- Decision Tree Regression
- Dan masih banyak lagi  
  
Hasil prediksi dari model regresi sering kali berbeda dengan nilai sebenarnya. Untuk mengevaluasi model kita, ada yang namanya Cost Function/Loss Function.
  
Matrik Evaluasi untuk Regression
- MAE - Mean Absolute Error
- MSE - Mean Squared Error
  
Hands-on:
https://colab.research.google.com/drive/1vz89B1nx8mG-dMwpEl8G3xItUlxQUyEJ?usp=sharing
  
### Classification Model
- Logistic Regression
- Decision Tree
- Support Vector Machine
- KNN
- Dan masih banyak lagi
  
Binary classification mengklasifikasikan suatu data menjadi salah satu dari 2 kelas/kategori.  
Multiclass classification mengklasifikasikan suatu data menjadi salah satu dari banyak kelas (>2 kelas).  
Multilabel classification mengklasifikasikan suatu data menjadi lebih dari satu kelas.
  
- Logistic Regression
Meskipun ada regression di namanya, logistic regression ini digunakan untuk melakukan klasifikasi. Kenapa? Pada logistic regression kita menggunakan fungsi sigmoid, yang dimana itu adalah fungsi matematika yang mengambil nilai sembarang dan memetakannya menjadi angka 0 atau 1, jadi seperti mengklasifikasikannya menjadi 0 atau 1.
  
Matrik Evaluasi untuk Classification
- Accuracy: perbandingan antara prediksi yang benar dengan total seluruh prediksi yang dilakukan 
- Precision: perbandingan antara prediksi yang benar dari suatu kelas dengan total prediksi untuk kelas tersebut
- Recall: perbandingan antara prediksi yang benar dari suatu kelas dengan total data kelas yang ada sebenarnya
- F1-score: harmonis antara precision dan recall
  
Hands-on:
https://colab.research.google.com/drive/1dqkwLgN2ArWePNVDZX_8nR1NWZVPu0-l?usp=sharing

