def format_number(s):
    new_s = ''
    for c in s:
        if c.isdigit() or c in (',', '.'):
            if c == ',':
                new_s += '.'
            else:
                new_s += c
    return new_s