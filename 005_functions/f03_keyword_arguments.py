def nepali_book(title, author, year):
    return f"'{title}' by {author}, published in {year}"


# Using keyword arguments in any order
print(nepali_book(author="Laxmi Prasad Devkota", title="Muna Madan", year=1936))
print(nepali_book(year=1999, title="Palpasa Café", author="Narayan Wagle"))
print(nepali_book(title="Shirishko Phool", year=1965, author="Parijat"))

# Note: Keyword arguments make function calls more readable
# and less prone to errors from argument order mistakes
