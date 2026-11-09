# Membuat file suara natural (Bahasa Indonesia) untuk Asisten Frayn.
# Jalankan di laptop/PC yang terhubung internet:
#   pip install edge-tts
#   python generate_audio.py
# Hasilnya folder "audio/" -> taruh di samping asisten-frayn.html saat upload.
import asyncio, os, edge_tts

VOICE = "id-ID-GadisNeural"   # alternatif suara pria: id-ID-ArdiNeural
RATE  = "+0%"                 # contoh lebih pelan: "-8%"

CLIPS = {
 "welcome": "Halo, selamat datang! Saya adalah asisten chatbot yang dikembangkan oleh Frayn. Apakah ada yang mau ditanyakan seputar tuan saya, Frayn?",
 "bye": "Terima kasih sudah ngobrol. Sampai jumpa!",
 "bingung": "Hmm, maaf, saya cuma bisa menjawab seputar tuan saya, Frayn. Coba tanya soal nama, umur, hobi, asal, atau kuliahnya.",
 "pacar": "Hehe… aduh, kok nanyanya gitu sih. Dari dulu tuan saya menjomblo, dan sekarang belum ada cewek atau pacar.",
 "nama": "Nama lengkap tuan saya adalah Frumensius Saputra Arjon. Biasanya dia dipanggil Frayn.",
 "panggil": "Nama panggilannya Frayn.",
 "umur": "Tuan Frayn sekarang berumur 21 tahun.",
 "anak": "Tuan Frayn itu anak pertama di keluarganya.",
 "hobi": "Hobi tuan saya adalah melukis.",
 "skill": "Keahliannya di bidang ethical hacking, tingkat menengah ya. Masih terus belajar dia.",
 "sifat": "Tuan Frayn aslinya pendiam, tapi cepat akrab.",
 "asal": "Tuan Frayn berasal dari NTT, tepatnya Kabupaten Manggarai Barat.",
 "kuliah": "Sekarang tuan saya semester 3, program studi Informatika di Universitas Sarjanawiyata Tamansiswa.",
 "aku": "Saya asisten chatbot yang dikembangkan oleh Frayn. Saya di sini untuk menjawab pertanyaan seputar tuan saya.",
 "makasih": "Sama-sama! Ada lagi yang mau ditanyakan seputar tuan saya, Frayn?",
 "halo": "Halo juga! Ada yang mau ditanyakan seputar tuan saya, Frayn?",
}

async def main():
    os.makedirs("audio", exist_ok=True)
    for key, text in CLIPS.items():
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(f"audio/{key}.mp3")
        print("ok", key)

asyncio.run(main())
