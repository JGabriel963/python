def file_read_from_line(fname, nlines):
    from itertools import islice

    with open(fname, encoding="utf-8") as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_line("texto.txt", 1)
