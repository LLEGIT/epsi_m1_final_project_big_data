from minio import Minio
import pandas as pd
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
# Nom du fichier à récupérer depuis MinIO
object_name = "crimes-et-delits-enregistres-par-les-services-de-gendarmerie-et-de-police-depuis-2012.xlsx"
# Chemin local pour enregistrer le fichier téléchargé
download_path = f"./data/{object_name}"

# Télécharger le fichier depuis MinIO
try:
    minio_client.fget_object(bucket_name, object_name, download_path)
    print(f"Fichier {object_name} téléchargé avec succès.")
except Exception as e:
    print(f"Erreur lors du téléchargement : {e}")
    exit()

# Vérifier si le fichier existe
if os.path.exists(download_path):
    # Lire le fichier Excel depuis la feuille "Services PN 2012" en ignorant les 3 premières lignes
    df = pd.read_excel(download_path, sheet_name="Services PN 2012", skiprows=3, engine='openpyxl')
    
    # Afficher les premières lignes
    print("Aperçu des données :")
    print(df.head())
else:
    print(f"Le fichier {download_path} n'existe pas.")
