<h1 align="center">TSKSW</h1>
<h3 align="center">Tampilkan Semua Kata Sandi Wifi</h3>
<blockquote align="center">
Peringatan: Penggunaan program ini tanpa izin adalah ilegal dan melanggar privasi. Pembuat program (Rofidoang03) tidak bertanggung jawab atas penggunaan yang salah. Pastikan Anda memiliki izin resmi sebelum menggunakan program ini.</blockquote>
<p align="center"><a href="hdhdhd">:open_book: Tentang</a> • <a href="">📋Persyaratan</a> • <a href="">:gear: Cara menginstal</a> • <a href =""> 🏃🏻 Cara menjalankan</a></p>
<h2>Tentang </h2>
<p>TSKSW adalah program python3 yang dikembangkan oleh Rofidoang03, program ini bertujuan untuk menampilkan semua kata sandi dari jaringan Wi-Fi yang tersimpan pada sistem</code>. Dengan menggunakan modul os untuk berinteraksi dengan sistem operasi, subprocess untuk menjalankan perintah shell, dan colorama untuk memberikan warna pada output, program ini memulai dengan membersihkan layar dan menetapkan judul program. Selanjutnya, perintah <code>netsh wlan show profiles</code> digunakan untuk menampilkan semua profil Wi-Fi, dan data yang diperoleh diproses untuk mendapatkan nama semua profil Wi-Fi. Proses berlanjut dengan menggunakan perintah <code>netsh wlan show profiles [nama_profil] key=clear</code> untuk mendapatkan kata sandi dari setiap profil Wi-Fi. Informasi Wi-Fi beserta kata sandi disimpan dalam list <code>data_wifi</code>, yang kemudian ditampilkan dalam format tabel dengan <code>nomor, nama jaringan Wi-Fi, dan kata sandi</code>. Output dihiasi dengan warna untuk memperjelas informasi.</p>
<h2>Persyaratan 📋</h2>
<ul>
    <li>Sistem Operasi: Windows 10 atau yang lebih baru.</li>
    <li>Python 3</li>
    <li>Git</li>
    <li>Modul Colorama</li>
</ul>
<h2>Cara Menginstal ⚙️</h2>
<ol>
    <li>Buka Command Prompt (CMD).</li>
    <li>Salin perintah di bawah ini</li>
<pre>
git clone https://github.com/rofidoang03/TSKSW.git && cd TSKSW && pip3 install -r requirements.txt
</pre>
    </li>
    <li>Tempelkan perintah yang telah disalin ke CMD, lalu tekan [Enter].</li>
    <li>Tunggu beberapa saat sampai proses instalasi selesai.</li>
</ol>
<h2>Cara Menjalankan 🏃🏻</h2>
<p>Buka Command Prompt (CMD) dan ketikkan perintah:</p>
<pre>
python3 main.py
</pre>
