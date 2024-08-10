from django.shortcuts import render
import google.generativeai as genai
import markdown
from django.core.cache import cache

genai.configure(api_key='[your api key]')
model = genai.GenerativeModel('gemini-1.5-flash')

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST.get('promt', '')
        
        # Ambil riwayat percakapan dari cache
        conversation_history = cache.get('conversation_history', [])
        
        # Tambahkan input pengguna ke riwayat
        conversation_history.append(f"User: {data}")
        
        # Gabungkan riwayat percakapan menjadi satu string
        full_conversation = "\n".join(conversation_history)
        
        # Kirim seluruh percakapan ke model AI
        response = model.generate_content(full_conversation)
        
        # Tambahkan respons AI ke riwayat
        conversation_history.append(f"AI: {response.text}")
        
        # Simpan riwayat percakapan yang diperbarui ke cache
        cache.set('conversation_history', conversation_history, timeout=3600)  # Simpan selama 1 jam
        
        riwayat_html = '<hr>'.join([markdown.markdown(item) for item in conversation_history])
        return render(request, 'home.html', {'hasil': markdown.markdown(response.text), 'riwayat': riwayat_html})
    
    # Jika bukan POST request, hapus cache dan tampilkan halaman kosong
    cache.delete('conversation_history')
    return render(request, 'home.html')
