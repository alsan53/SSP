- git config --global user.name "Nama Baru"
- git config --global user.email "emailbaru@example.com"

Ganti Email pada Git Lokal (untuk Commit)
Jika kamu sudah pernah melakukan commit sebelumnya, pastikan email dan nama Git lokal kamu juga diperbarui agar sesuai dengan identitas baru.

- git init

Inisialisasi Git Lokal.
Jika belum pernah diinisiasi.

- git add .

Tambahkan Semua File ke Git

- git remote add origin https://github.com/alsan53/SSP.git 

jika belum ada origin

- git remote set-url origin https://github.com/alsan53/SSP.git 

Ubah URL Remote Origin (Jika Mau Ganti Repo Tujuan)

- git branch -M main

Memindahkan / mengganti nama branch ke nama baru , sekaligus menghapus histori branch lama jika ada konflik .
Jika branch main sudah ada, maka akan di-replace.

- git pull origin main (Jika ada commit yang sudah ada)

Ada commit yang sudah diupload ke repo GitHub sebelumnya (misal dari komputer lain atau dengan nama branch yang sama).
Kamu mencoba push ke branch main yang tidak bisa langsung ditimpa karena ada perbedaan histori commit.

- git push -u origin main

Menghubungkan branch lokal dengan remote branch di GitHub
Setelah ini, kamu bisa menggunakan git push atau git pull tanpa harus menyebut origin main setiap kali.

- git push --force -u origin main

Memaksa Git untuk menimpa isi repo remote sesuai dengan apa yang ada di komputer kamu.
Bisa menghilangkan commit yang ada di remote jika tidak ada di lokal.
