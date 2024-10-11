# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44
pages = 100
strs = 50
symbols = 25
one_symbs = 4
volume_of_symbols = symbols * one_symbs #объем символов в строке в байтах
volume_of_strs = volume_of_symbols * strs #объем одной странички в байтах
volume_of_pages = volume_of_strs * pages #объем одной книги в байтах
volume_of_pages_mb = volume_of_pages / 1024 / 1024 #объем криги в Мб
number_of_books = inf_volume // volume_of_pages_mb
print("Количество книг, помещающихся на дискету:", int(number_of_books))
