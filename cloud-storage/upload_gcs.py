from google.cloud import storage
import argparse

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"Archivo {source_file_name} subido a {destination_blob_name}."
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subir un archivo a Google Cloud Storage.")
    parser.add_argument("bucket_name", help="Nombre del bucket de GCS.")
    parser.add_argument("source_file_name", help="Ruta del archivo local a subir.")
    parser.add_argument("destination_blob_name", help="Nombre del blob en GCS.")

    args = parser.parse_args()

    upload_blob(args.bucket_name, args.source_file_name, args.destination_blob_name)