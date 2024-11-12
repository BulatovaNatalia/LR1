# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44  # размер дискеты в Мб
pages_per_book = 100  # количество страниц в книге
lines_per_page = 50   # количество строк на странице
chars_per_line = 25   # количество символов в строке
size_per_char_bytes = 4  # размер одного символа в байтах

# Переводим размер дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Расчет общего количества символов в книге
total_chars_per_book = pages_per_book * lines_per_page * chars_per_line

# Расчет объема одной книги в байтах
book_size_bytes = total_chars_per_book * size_per_char_bytes

# Количество книг, помещающихся на дискету
number_of_books = disk_size_bytes / book_size_bytes
number_of_books = round (number_of_books)
print("Количество книг, помещающихся на дискету:", number_of_books)
