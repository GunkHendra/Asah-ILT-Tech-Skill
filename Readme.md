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

---

# Eksplorasi Unsupervised Learning: Teknik dan Penerapan Praktis by Ivan Andrianto
Unsupervised learning adalah metode machine learning di mana model belajar dari data yang tidak memiliki label. Tujuannya adalah untuk menemukan pola, struktur, atau hubungan tersembunyi dalam data tanpa bantuan supervisi manusia.  
  
## Jenis-jenis Unsupervised Learning
- Clustering (bagi berdasarkan kemiripan)
- Sistem Rekomendasi (memprediksi preferensi pengguna)
- Association (menemukan relasi menarik)
- Deteksi Anomali (mendeteksi data yang tidak sesuai pola)
- Dimensionality Reduction (mengurangi jumlah fitur/data)

### Algoritma Clustering
Mengelompokan contoh-contoh yang tidak berlabel ke dalam cluster berdasarkan pola yang mirip/sama.
    
Jenis-jenis clustering algorithm:
- Centroid-based clustering
- Density-based clustering
- Distribution-based clustering
- Hierarchical clustering
  
#### Algoritma K-means
- Secara acak memilih K cluster centroid
- Menetapkan setiap titik ke centroid terdekat untuk mendapatkan K cluster awal
- Menghitung ulang posisi centroid berdasarkan rata-rata titik pada masing-masing cluster
- Mengulangi proses penetapan titik ke centroid terdekat dan perhitungan ulang centroid hingga posisi centroid tidak berubah (konvergen) atau jumlah iterasi maksimum tercapai
- Hasil akhir adalah pembagian data ke dalam K cluster berdasarkan kemiripan  
  
Cost function pada algoritma K-means:  
Fungsi ini menghitung rata-rata dari jarak kuadrat antara setiap titik data dengan centroid dari cluster tempat titik tersebut berada.
    
Bagaimana memilih jumlah cluster?
Kita bisa menggunakan elbow method.
- Inertia dihitung dengan menjumlahkan jarak kuadrat.
- Elbow method adalah salah satu metode paling populer untuk menentukan nilai optimal dari k.
- Dalam metode ini, kita memilih nilai k pada titik di mana terjadi penurunan inertia yang tajam dan signifikan.  
  
Hands-on:  
https://colab.research.google.com/drive/1siquTlH3xSfTAlhqoj1L3JmVKj18EHSz?usp=sharing
  
### Sistem Rekomendasi
Dalam konteks machine learning, pengembangan sistem rekomendasi dapat melibatkan supervised learning dan/atau unsupervised learning.  
  
#### Jenis-jenis sistem rekomendasi
- Content-based filtering  
Sistem rekomendasi yang menyarankan item berdasarkan kemiripan karakteristik atau fitur dengan item yang pernah disukai atau dikonsumsi oleh pengguna. Contohnya, jika pengguna suka film bergenre aksi, maka sistem akan merekomendasikan film lain dengan genre serupa.
- Collaborative filtering  
Sistem rekomendasi yang menyarankan item berdasarkan pola perilaku dan preferensi pengguna lain yang mirip. Contohnya, jika pengguna A dan B memiliki riwayat menonton film yang mirip, maka film yang disukai oleh A tapi belum ditonton oleh B dapat direkomendasikan ke B.
    
Pada dasarnya, sistem rekomendasi ini menghitung kemiripan/similarity.  
  
Bagaimana cara menghitung similarity?  
- Cosine similarity
- Euclidian similarity

Hands-on:  
https://colab.research.google.com/drive/1bmvef4L9req3DY-I4QiHmUSaPJ_qInZo?usp=sharing