import pyrebase

config = {
    "apiKey": "AIzaSyDGPSm4Lbdkmk4AXReop1xj6l_ogYquaYU",
    "authDomain": "python-picup.firebaseapp.com",
    "databaseURL": "https://python-picup.firebaseio.com",
    "projectId": "python-picup",
    "storageBucket": "python-picup.appspot.com",
    "messagingSenderId": "465785417019",
    "appId": "1:465785417019:web:d72db391bfeb3c85e75b1e",
    "measurementId": "G-3ZHGQ5GWTF"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "images/Upload.jpg"
path_local_up = "Internet/Firebase/my_image.jpg"
storage.child(path_on_cloud).put(path_local_up)

path_local_down = "Internet/Firebase/Download.jpg"
storage.child(path_on_cloud).download(path_local_down)
