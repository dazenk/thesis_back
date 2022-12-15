import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# guarda las credenciales necesarias para acceder a firebase y traer las puntuaciones de los test para manipularlas
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
