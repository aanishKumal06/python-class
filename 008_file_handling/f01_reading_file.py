try:
    # Open the file named 'sample_file.txt' in read mode ('r')
    f = open("sample_file.txt", "r")
    content = f.read()
    print(content)

    # Move the file cursor back to the beginning of the file (position 0)
    f.seek(0)
    read_another_time = f.read()
    print(read_another_time)
    f.close()
except Exception as e:
    print(f"An unexpected error occurred: {e.__class__.__name__} {e}")
