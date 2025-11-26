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

# Game Changer: NLP dan Generative AI by Zanuar Ekaputra Rus'an

## Apa yang akan dilakukan di sesi ILT kali ini:

- Menjelaskan Konsep dari Natual Language Processing
- Mengidentifikasi Berbagai Jenis Arsitektur NLP
- Menelaah konsep-konsep dari Generative AI

## Mari Berbicara dengan Komputer dalam NLP

### Bagaimana Komputer dapat Memahami Kita?

Jadi di antara manusia dan komputer, ada yang namanya interaksi. Interaksi ini bisa berupa input dan output.

### Apa itu NLP?

NLP adalah cabang dari AI yang memberikan mesin kemampuan untuk membaca, memproses, dan mengambil makna dari bahasa manusia.

### Bagaimana Alur NLP?

#### Teks Dibersihkan sebelum Diproses (Preprocessing)

- Case folding
- Special character removal (angka, tanda baca, simbol, atau karakter khusus lainnya)
- Stopwords removal
- Stemming or Lemmatization

#### Tokenization dan Pembentukan Vocabulary

Tokenization adalah proses memecah teks menjadi bagian-bagian kecil seperti kata atau sub-kata (token), yang kemudian digunakan untuk membentuk daftar kata (vocabulary) yang dikenali oleh sistem.

#### Tambah OOV Token untuk Kata yang Tidak Dikenal

OOV (Out-of-Vocabulary) token ditambahkan untuk menggantikan kata yang tidak ada dalam vocabulary, agar model tetap dapat memproses teks meskipun terdapat kata baru atau asing.

#### Padding

Padding digunakan untuk menyesuaikan semua data dalam satu urutan. Padding akan menyamakan panjang urutan token agar bisa diproses oleh model.

#### Word Embeddings

Word embeddings adalah jenis representasi kata yang memungkinkan kata-kata dengan makna serupa memiliki representasi yang mirip.

## Berbagai Jenis Algoritma NLP

### Keterbatasan Model ANN Dasar

Dalam permasalahan berurutan, urutan nilai sangat penting. Untuk menangani hal ini, model perlu menggunakan pengalaman sebelumnya untuk memproses nilai input berikutnya. Model ANN dasar tidak mampu melakukan hal ini.

### Sequence Prediction

Sequence prediction adalah jenis tugas machine learning yang melibatkan pemrosesan data berurutan untuk memprediksi elemen berikutnya atau menghasilkan urutan baru.  
Contohnya dalam NLP adalah memprediksi kata berikutnya dalam kalimat atau menerjemahkan teks dari satu bahasa ke bahasa lain.  
Tugas seperti ini memerlukan model yang mampu mengingat konteks, sehingga muncullah model seperti RNN dan LSTM.

### Arsitektur Model RNN

Algoritma RNN adalah jenis algoritma deep learning yang dirancang untuk memproses data urutan.  
Kekurangan pada model RNN:  
RNN tidak pernah benar-benar berhasil menangani urutan data yang panjang, seperti paragraf yang panjang. Ketika sampai di akhir paragraf, model ini cenderung lupa apa yang terjadi di awal.

### LSTM Network

LSTM adalah jenis khusus dari RNN yang mampu mempelajari long-term dependencies. LSTM memiliki memoti jangka panjang yang disebut "cell state". LSTM menggunakan tiga "gerbang" utama untuk mengontrol aliran informasi:

- Forget gate -> menentukan informasi apa yang perlu dibuang dari memori.
- Input gate -> menentukan informasi baru apa yang akan disimpan.
- Output gate -> menentukan informasi apa yang akan dikeluarkan ke langkah berikutnya.

### Gated Recurrent Unit (GRU)

GRU adalah jenis unit dalam RNN yang dikembangkan untuk memodelkan long-range dependencies pada data urutan dengan cara yang lebih efisien. GRU menggunakan dua gerbang utama:

- Reset Gate
- Update Gate

## Bonjour, Generative AI

### Apa itu Generative AI

Generative AI adalah jenis kecerdasan buatan yang mampu menciptakan konten baru seperti teks, gambar, musik, atau kode berdasarkan pola dari data yang telah dipelajari.

#### Discriminative Model

Discriminative model berfokus pada membedakan atau mengklasifikasikan data berdasarkan fitur yang ada.
Model ini belajar dari hubungan antara input dan label untuk menentukan kategori atau hasil yang benar.
Contohnya seperti logistic regression atau support vector machine (SVM) yang digunakan untuk klasifikasi.

#### Generative Model

Generative model berfokus pada mempelajari distribusi data untuk dapat menghasilkan data baru yang mirip dengan data asli.
Model ini tidak hanya mengenali perbedaan antar kelas, tetapi juga memahami bagaimana data tersebut terbentuk.
Contohnya adalah Variational Autoencoder (VAE), GAN (Generative Adversarial Network), dan GPT (Generative Pretrained Transformer).

### Kelebihan dan Kekurangan

Kelebihan:

- Time efficient
- Personalization
- Creative potential
- Versatility
- Innovation

###

Kekurangan:

- Copyright risk
- High computation cost
- Ethical concerns
- Inaccuracy
- Data-driven

### Pertimbangan Etika dalam Generative AI

- Mengidentifikasi dan mengurangi bias dalam modal AI
- Menjaga privasi dan perlindungan data dalam aplikasi AI
- Hak kekayaan
- Tranparansi dan keterjelasan
- Standar global

## Segala Hal tentang Generative AI

### Sentence predictions

- RNN
- LSTM
- GRU

### Transformers

Paper: Attention Is All You Need
Transformer adalah arsitektur model deep learning yang dirancang untuk memproses data berurutan seperti teks, namun tanpa menggunakan urutan langkah seperti RNN atau LSTM.
Model ini menggunakan mekanisme yang disebut self-attention, yang memungkinkan model memahami hubungan antar kata dalam satu kalimat secara bersamaan, bukan satu per satu.

### LLM

#### Bagaimana Cara Kerjanya?

LLM dilatih menggunakan kombinasi berbagai teknik, dengan deep learning dan dataset berukuran besar sebagai komponen utamanya. Yang paling penting: data itu krusial. LLM sangat rakus data dan membutuhkan sejumlah besar data teks untuk pelatihan yang efektif.

#### Limitasi LLM

- Mereka tidak mengetahui data spesifik domain tertentu
- Mereka tidak memiliki informasi secara real-time
- Mereka sering mengasumsikan bahwa isi prompt adalah benar
- Mereka tidak memiliki kemampuan untuk menanyakan informasi konteks

#### Teknik Optimasi

Optimasi LLM dilakukan dengan menerapkan teknik-teknik yang dapat meningkatkan kinerja dan kemampuan adaptasi terhadap tugas spesifik.

#### Prompt Engineering

Prompt engineering adalah proses merancang dan menyempurnakan masukan (prompt) untuk mengarahkan LLM dalam menghasilkan keluaran yang sesuai.

### RAG

RAG (Retrieval-Augmented Generation) adalah pendekatan dalam AI di mana sebuah model mengambil informasi yang relevan dari database atau dokumen untuk meningkatkan dan menghasilkan respons yang lebih akurat serta konstektual.

### Fine-tuning

Fine-tuning adalah proses menyesuaikan model yang sudah dilatih sebelumnya (pretrained model) dengan data baru yang lebih spesifik agar hasilnya lebih sesuai dengan kebutuhan tertentu.
Dengan cara ini, model tidak perlu dilatih dari awal, sehingga menghemat waktu dan sumber daya, namun tetap mampu beradaptasi dengan konteks atau domain baru.

---

# TensorFlow di Dunia Nyata: Model Deployment by Kimberley Blessinda

## Pengenalan terhadap Machine Learning Deployment

Model Deployment adalah tahap terakhir dalam pengembangan model AI. Kita akan lebih berhubungan dengan software engineer pada tahap ini.

- Project Planning & Setup  
  Tentukan permalasahan yang dikerjakan, tetapkan kebutuhan dan tujuan, serta tentukan cara alokasi sumber daya
- Data Collection & Labeling  
  Kumpulkan dan atur data (seperti gambar, teks, data tabular, dll), serta lakukan anotasi ground truth
- Model Training & Debugging  
  Implementasi model baseline dengan cepat, menemukan dan mereproduksi metode state-of-the-art untuk domain permasalahan, dan sebagainya
- Deployment & Monitoring  
  Tempatkan model ke production, tulis perangkat lunak yang dibutuhkan agar model dapat berjalan dan menghasilkan prediksi

### Fase Deployment Model Machine Learning

- Deployment
- Evaluation
- Monitoring
- Management

### Berbagai Tantangan Model Deployment

- Sensitif terhadap semantics, jumlah, dan kelengkapan data yang masuk
- Penurunan performa seiring waktu
- Dan lainnya

### Opsi Model Deployment

- Centralize model di server
- Distribute model di perangkat pengguna

### Model Inference Options

- Batch Prediction
- Real Time Prediction

### Opsi Bentuk Model Deployment

- TensorFlow Serving
- TensorFlow Lite
- TensorFlow.js
- Other Language Bindings

## Model Deployment TensorFlow.js

### Apa itu TensorFlow.js

Open-source JS library untuk melatih dan deploying model machine learning di client's browser atau server Node.js

### Tahapan Umum Penggunaan TensorFlow.js

- Build a model
- Save model
- Convert
- Deploy

Hands-on:
https://colab.research.google.com/drive/1ggM9VmC3y9O9t7uaq2hJF8cz5VvM9qxu#scrollTo=b_Qph3FDOYZx

## Model Deployment: ~~TensorFlow~~ Lite LiteRT

### Apa itu LiteRT?

Open-source deep learning framework untuk menjalankan model TensorFlow langsung di perangkat (on-device)

### Tantangan Model On-Device

Harus menangani beragam jenis perangkat dan tidak memiliki akses ke data sebenarnya. Perlu ada keseimbangan anatara:

- Efisiensi daya
- Inference latency
- Akurasi dan

### Tahapan Umum Penggunaan TensorFlow Lite

- Build a model
- Save model
- Convert
- Deploy

Hands-on:
https://colab.research.google.com/drive/1LF7fG8onq0afuKKRkNxl-rrhPLQ3bYG4#scrollTo=2HGjyQGTI7nz

## Model Deployment: TensorFlow Serving

### Apa itu TensorFlow Serving?

Sistem serving yang flexible dan memiliki performa tinggi untuk model machine learning, yang dirancang khusus untuk production environments

### Tahapan Umum Penggunaan TensorFlow Serving

- Membuat dan train model
- Simpan model
- Build & run a docker image
- Mengirim permintaan prediksi

#### Apa itu Container? Docker?

Container adalah unit standar perangkat uank yang membungkus kode dan semua dependensinya sehingga aplikasi dapat dijalankan secara portabel

##### Bagaimana Membuat Docker Container?

Docker File -> Build -> Docker Image -> Run -> Docker Container

### Apa itu Federated Learning?

Memungkinkan setiap klien melatih modelnya sendiri secara mandiri menggunakan datanya sendiri pada perangkat

### Apa itu TensorFlow Datasets

Kumpulan dataset yang siap digunakan, baik dengan TensorFlow yang siap digunakan, baik dengan TensorFlow maupun framework machine learning Python lainnya

---
