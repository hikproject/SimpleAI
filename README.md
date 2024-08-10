# Persiapan Proyek Django SimpleAI

Jika Anda ingin menggunakan proyek SimpleAI ikuti langkah-langkah berikut:

1. Clone Repositori
   ```
   git clone [URL_REPOSITORI_SIMPLEAI]
   cd SimpleAI
   ```

2. Buat dan Aktifkan Virtual Environment
   ```
   python -m venv myenv
   source myenv/bin/activate  # Untuk Linux/macOS
   myenv\Scripts\activate     # Untuk Windows
   ```

3. Instal Dependensi
   ```
   pip install -r requirements.txt
   ```

4. Konfigurasi API Key
   - Buka file `SimpleAI/views.py`
   - Cari baris `genai.configure(api_key='[your api key]')`
   - Ganti `[your api key]` dengan API key Gemini Anda

5. Jalankan Migrasi
   ```
   python manage.py migrate
   ```

6. Jalankan Server Pengembangan
   ```
   python manage.py runserver
   ```

Sekarang Anda siap menggunakan SimpleAI! Buka browser dan akses `http://localhost:8000` untuk mulai berinteraksi dengan AI.

Catatan: 
- Pastikan untuk selalu menarik (pull) perubahan terbaru dari repositori sebelum mulai bekerja.
- SimpleAI menggunakan model Gemini dari Google. Pastikan Anda memiliki akses dan API key yang valid.


