from flask import Flask, render_template

app = Flask(__name__)

# Data gabungan untuk Grid Gambar (About Me & Journey)
data_profil = [
    {
        "id": "modal-about",
        "judul": "About Me",
        "gambar": "about.jpg",
        "isi_teks": "Sebagai mahasiswi Teknologi Informasi, saya telah mendedikasikan waktu saya untuk mempelajari siklus pengembangan perangkat lunak secara mendalam. Saya telah berhasil menyelesaikan beberapa proyek tugas kampus, hingga situs portofolio pribadi. Saya sangat menyukai tantangan baru dan selalu mencari peluang untuk menerapkan keterampilan saya dalam skenario dunia nyata. Saya percaya bahwa kolaborasi dan pembelajaran berkelanjutan adalah kunci dalam dunia teknologi. Saya terbuka untuk kesempatan magang dan kolaborasi proyek!"
    },
    {
        "id": "modal-kuliah",
        "judul": "Mahasiswa IT",
        "gambar": "tenis.jpg",
        "isi_teks": "Tahun 2024 - Sekarang: Saat ini saya sedang menempuh pendidikan D4 - Teknik Informatika. Di sini saya fokus mempelajari algoritma, struktur data, dan pengembangan web backend hingga frontend."
    },
    {
        "id": "modal-cv",  
        "judul": "My CV",  
        "gambar": "leg.jpg", 
        "isi_teks": "Berikut adalah Curriculum Vitae (CV) saya. Silakan klik tombol di bawah ini untuk melihat detail riwayat pendidikan, keahlian, dan pengalaman yang saya miliki.",
        "file_cv": "CV_Baru.pdf.pdf"  
    },
    {
        "id": "modal-skills",  
        "judul": "Skills & Tools", 
        "gambar": "foto.jpg", 
        "isi_teks": "Berikut adalah beberapa bahasa pemrograman dan teknologi yang saya pelajari dan gunakan dalam membangun berbagai proyek:",
        "logos": [
            {"nama": "Python", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"},
            {"nama": "HTML5", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg"},
            {"nama": "CSS3", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg"},
            {"nama": "JavaScript", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"},
            {"nama": "Tailwind", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg"},
            {"nama": "Flask", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg"},
            {"nama": "Laravel", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/laravel/laravel-original.svg"},
            {"nama": "Django", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg"},
            {"nama": "VS Code", "url": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg"},
            {"nama": "GitHub", "url": "https://cdn.simpleicons.org/github/white"}
        ]
    }
]


data_proyek = [
    {"nama": "Aplikasi Marine Ice Jaya", "deskripsi": "Aplikasi Jual Es Balok Ikan Perusahaan CV. Marine Ice Jaya.", "teknologi": "PHP, PHP MyAdmin"},
    {"nama": "Aplikasi MediCheck", "deskripsi": "Aplikasi untuk Monitoring Diet Sehat, Rekomendasi Makanan Diet Selama Seminggu Kedepan, dan Rekomendasi Lifestyle.", "teknologi": "Python (Django), SQLite"},
    {"nama": "Aplikasi MusicPlayer", "deskripsi": "Aplikasi layaknya Spotify berbasis web, disertai Fitur Sering Didengar, dll.", "teknologi": "C#, SQLite"},
    {"nama": "Aplikasi Voting-LAN", "deskripsi": "Aplikasi Vote berbasis website agar Lebih Mudah dalam Perhitungan Vote.", "teknologi": "Python (Flask), SQLite"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proyek')
def proyek():
    # Mengirim data_profil dan data_proyek ke HTML
    return render_template('proyek.html', profil=data_profil, proyek=data_proyek)

if __name__ == '__main__':
    app.run(debug=True)