import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import chardet

# Deteksi encoding file
file_path = 'data_grup_cleaned.csv'
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(f"Detected encoding: {result}")

# Baca file dengan encoding yang terdeteksi
data = pd.read_csv(file_path, on_bad_lines='skip', encoding=result['encoding'])

# Fungsi untuk memparsing baris data
def parse_message(row):
    pattern = r"(\d{8}\d{2}\.\d{2})(.*?)\s(.+)"
    match = re.match(pattern, row)
    if match:
        return match.groups()
    return None, None, None

# Terapkan parsing pada kolom pertama data
data_cleaned = data.iloc[:, 0].dropna().apply(parse_message)
parsed_data = pd.DataFrame(data_cleaned.tolist(), columns=["Timestamp", "Sender", "Message"])

# Validasi hasil parsing
if parsed_data.empty or parsed_data["Message"].isnull().all():
    print("Error: Tidak ada pesan yang valid setelah parsing.")
    print("Pastikan data sesuai dengan pola yang diharapkan.")
    exit()

print("Sample Messages:")
print(parsed_data["Message"].head())
print("Total Messages:", len(parsed_data["Message"]))
print("Non-empty Messages:", parsed_data["Message"].notnull().sum())

# Step 1: Preprocessing - Konversi pesan menjadi representasi numerik menggunakan TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=500)  # Batasi fitur pada 500 kata teratas
X = vectorizer.fit_transform(parsed_data["Message"])

# Step 2: Fungsi untuk melakukan clustering dan menganalisis hasilnya
def perform_clustering(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)
    
    # Top keywords per cluster
    top_keywords = []
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()
    for i in range(n_clusters):
        top_keywords.append([terms[ind] for ind in order_centroids[i, :3]])  # Top 3 words per cluster
    
    return clusters, top_keywords

# Lakukan clustering untuk 3, 4, dan 5 cluster
results = {}
for n in [3, 4, 5]:
    clusters, keywords = perform_clustering(X, n_clusters=n)
    parsed_data[f"Cluster_{n}"] = clusters  # Tambahkan label cluster ke dataframe
    results[n] = keywords

# Menampilkan beberapa baris dari dataframe yang sudah diberi label cluster
print("\n=== Parsed Data with Clustering ===")
print(parsed_data.head())

# Menampilkan top keywords untuk setiap cluster
print("\n=== Top Keywords per Cluster ===")
for n_clusters, keywords in results.items():
    print(f"\nNumber of Clusters: {n_clusters}")
    for i, words in enumerate(keywords):
        print(f"Cluster {i}: {', '.join(words)}")
