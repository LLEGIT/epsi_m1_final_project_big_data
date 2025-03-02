from minio import Minio
import os

# Configuration de MinIO
minio_client = Minio(
    "localhost:9000",  # Adresse de ton serveur MinIO
    access_key="admin",  # Clé d'accès
    secret_key="password",  # Clé secrète
    secure=False  # Si tu utilises HTTP (non sécurisé) ; si HTTPS, mets secure=True
)

# Le nom du bucket
bucket_name = "warehouse"

# Vérifier si le bucket existe, sinon le créer
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' créé.")
else:
    print(f"Bucket '{bucket_name}' existe déjà.")

# Répertoire local avec les fichiers à télécharger
local_directory = "C:/Users/anais/OneDrive/Bureau/daniel/epsi_m1_final_project_big_data/data"

# Parcours tous les fichiers dans le répertoire local
for filename in os.listdir(local_directory):
    local_file_path = os.path.join(local_directory, filename)

    # Vérifie que c'est un fichier (et pas un répertoire)
    if os.path.isfile(local_file_path):
        # Télécharger le fichier dans le bucket 'warehouse'
        print(f"Uploading {filename} to {bucket_name}...")
        minio_client.fput_object(bucket_name, filename, local_file_path)

print("Tous les fichiers ont été téléchargés.")