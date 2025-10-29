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

---

# Deep Learning: Computer Vision dan Time Series by Fina Noviantika
## Neural Network
### Perbedaan Machine Learning dan Deep Learning
Di machine learning, feature extractionnya masih ada campur tangan manusia, sedangkan di deep learning, feature extraction langsung pada modelnya. Namun perbedaan utamanya adalah dari arsitekturnya, yang dimana deep learning ini berbentuk seperti sistem sarah buatan, atau artificial neural network.

### Biological Nerves vs Artificial Nerves
Di articial nerves, kita punya perceptron. Sebuah perceptron mengambil nilai input (x) dan mengkalikannya dengan bobot (w). Lalu ditambahkan bias (b) ke hasil tersebut. Ini menghasilkan net input (z).
    
Selanjutnya, net input tersebut melewati activation function (f) untuk menghasilkan output akhit (y)

### Istilah dalam Neural Network
#### Activation Function
Activation function adalah fungsi matematika yang menentukan apakah sebuah neuron dalam ANN (Artificial Neural Network) akan menghasilkan output berdasarkan inputnya. Pada perceptron, fungsi ini membantu neural network menangani pola dengan data yang tidak linier. Berikut merupakan beberapa activation function,
- ReLU
- Leaky ReLu
- Sigmoid
- Tanh
- Softmax

#### Loss Function
Loss function adalah rumus matematika yang digunakan untuk mengukur seberapa baik atau buruk performa model neural network pada data pelatihan. Bedanya sama cost function di machine learning gimana? Cost function menghitung rata rata kesalahan nilai error dari seluruh data, kalau loss function menghitung dari satu data aja.

#### Optimizer
Optimizer adalah komponen utama yang bertanggung jawab untuk mengoptimalkan atau menyesuaikan bobot dan bias pada jaringan agar mengurangi kesalahan prediksi.
- Stochastic Gradient Descent
- RMSprop
- Adam

### Definisi Deep Learning
Deep learning adalah bagian dari AI. Ini menggunakan metode yang terinspirasi dari cara kerja otak manusia. Metode-metode ini dilakukan melalui Artificial Neural Network (ANN).

### Arsitektur Deep Learning
- Input Layer (menerima input-an)
- Hidden Layer (memroses input-an)
- Output Layer (menampilkan hasil pemrosesan)

### Metode Forward Propagation dan Backpropagation
Forward propagation dan backpropagation adalah dua proses utama dalam pelatihan jaringan saraf. Forward propagation adalah tahap di mana data input diteruskan dari lapisan awal hingga lapisan output untuk menghasilkan prediksi. Sedangkan backpropagation adalah tahap pembelajaran di mana kesalahan (error) dari hasil prediksi dibandingkan dengan target sebenarnya, lalu digunakan untuk memperbarui bobot jaringan agar model menjadi lebih akurat. Singkatnya, forward propagation digunakan untuk memprediksi, sementara backpropagation digunakan untuk belajar dari kesalahan prediksi.

### Deep Learning Training Pattern
Data inputan -> diproses -> dihitung probabilitas prediksi -> evalurasi dan optimasi hasil -> diulang (epoch)

## Computer Vision
Computer vision adalah cabang dari AI yang berfokus pada bagaimana komputer dapat memperoleh, memproses, menganalisis, dan memahami informasi dari gambar atau video digital. Metode ini memungkinkan sistem mengenali objek, memahami konteks visual, dan mengambil keputusan berdasarkan data visual.

### Segment Anything Model
Segment Anything Model (SAM) adalah model computer vision yang dirancang untuk melakukan segmentasi objek dalam gambar atau video. Segmentasi di sini berarti memisahkan atau mengidentifikasi area tertentu yang berisi objek tertentu.

## Image Classification
### Convolutional Neural Network (CNN)
CNN adalah salah satu algoritma neural network yang memungkinkan kita untuk mengekstraksi representasi tingkat tinggi dari sebuah gambar. Berikut arsitektur CNN,
- Input layer: menerima data input atau masukan dari dataset
- Convolutional layer: mengekstrak fitur-fitur penting dari gambar (garis tepinya, dan sebagainya). Dari input image masuk ke convolutional layer ini akan menghasilkan gambar baru, yang disebut activation maps.
- Activation function: lapisan untuk menerapkan fungsi aktivasi
- Pooling layer: mengurangi dimensi spasial dari representasi gambar untuk mengurangi jumlah parameter dan komputasi dalam jaringan, membantu mencegah overfitting, serta mempercepat proses pelatihan. Ada 2 metode, max pooling dan average pooling.
- Fully connected layers: menggabungkan semua fitur yang sudah diekstraksi di lapisan sebelumnya untuk membuat keputusan akhir, seperti klasifikasi atau prediksi.
- Output layers: bagian terakhir, berfungsi untuk menghasilkan prediksi atau keluaran akhir dari model

Hands-on: https://colab.research.google.com/drive/1kSFQTkXiSKfZAg2-mysYym5Cq260AJ8D?usp=sharing

## Time Series (Forecasting)
### Apa itu Time Series?
Time series adalah kumpulan data yang diambil atau dicatat secara berurutan pada interval waktu yang tetap. Setiap titik data dalam time series mewakili sebuah observasi pada waktu tertentu.

### Univariate & Multivariate Time Series
- Univariate: mengobservasi satu variabel sepanjang waktu.
- Multivariate mengobservasi banyak variabel sepanjang waktu.

### Metode Pembagian Data Time Series: Sliding Windows & Expanding Windows
Sliding windows berfokus pada data terbaru, sedangkan expanding windows menangkap seluruh konteks historis.

Periode pelatihan adalah bagain dari dataset time series yang digunakan untuk melatih model, sedangkan periode validasi adalah segmen terpisah yang digunakan untuk melakukan validasi model.
  
Ini menunjukkan bagaimana sebuah model belajar mempredikasi nilai di masa depan (label Y) berdasarkan jendela input tetap (input X) dari data time series sebelumnya.

Hands-on: https://colab.research.google.com/drive/1vFf1fsPnLeBfTUXBT58yNyB4NLUITbzx?usp=sharing

---

