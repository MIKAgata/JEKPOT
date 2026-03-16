def tampilkan_ascii(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            ascii_art = f.read()
            print(ascii_art)
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


tampilkan_ascii("banner.txt")