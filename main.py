import requests

url = "https://talentern.telkomuniversity.ac.id/kegiatan-saya/logbook/create-logbook-daily/code dari alamat" #Mencari Code dari alamat
activities = [
      {
        "_token": "Cari Token nya Terlebih Dahulu", #Tutorial ada di Deskripsi
        "date": "2025-04-21", #sesuaikan dengan tanggal yang ing diinputkan
        "emoticon": "5",
        "activity": "Sesuaikan berdasarkan kegiatan yang dilakukan pada tanggal tersebut."
    },
    {
        "_token": "Cari Token nya Terlebih Dahulu", #Tutorial ada di Deskripsi
        "date": "2025-04-22", #sesuaikan dengan tanggal yang ing diinputkan
        "emoticon": "5",
        "activity": "Sesuaikan berdasarkan kegiatan yang dilakukan pada tanggal tersebut."
    },
    {
        "_token": "Cari Token nya Terlebih Dahulu", #Tutorial ada di Deskripsi
        "date": "2025-04-23", #sesuaikan dengan tanggal yang ing diinputkan
        "emoticon": "5",
        "activity": "Sesuaikan berdasarkan kegiatan yang dilakukan pada tanggal tersebut."
    },
    {
        "_token": "Cari Token nya Terlebih Dahulu", #Tutorial ada di Deskripsi
        "date": "2025-04-24", #sesuaikan dengan tanggal yang ing diinputkan
        "emoticon": "5",
        "activity": "Sesuaikan berdasarkan kegiatan yang dilakukan pada tanggal tersebut."
    },
    {
        "_token": "Cari Token nya Terlebih Dahulu", #Tutorial ada di Deskripsi
        "date": "2025-04-25", #sesuaikan dengan tanggal yang ing diinputkan
        "emoticon": "5",
        "activity": "Sesuaikan berdasarkan kegiatan yang dilakukan pada tanggal tersebut."
    }
]
cookies = {
    "talentern_session": "Cari Cookie nya Terlebih Dahulu", #Tutorial ada di Deskripsi
}

for activity in activities:
    response = requests.post(url, data=activity, cookies=cookies)
    print(f"{activity['date']}: {response.status_code} - {response.text[:100]}")