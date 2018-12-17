from PIL import Image
import argparse


def get_char(gray, use_html):
    # chars = ['@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', ' ']
    # chars = ['@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', ' ']
    # chars = "$ @ B % 8 & W M # * o a h k b d p q w m Z O 0 Q L C J U Y X z c v u n x r j f t / \ | ( ) 1 { } [ ] ? - + ~ < > i ! l I ; : , \" ^ ` ' .".split()
    chars = ['#', '=', '-', ' ']
    # chars.append(' ')
    # chars = [i for i in "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "]
    # chars = ['@', '#', 'k', 'i', '.']
    # if use_html:
    #     chars.append('&nbsp;')
    # else:
    #     chars.append(' ')
    idx = int((gray / 255) * (len(chars) - 1))
    return chars[idx]


def main():
    parser = argparse.ArgumentParser(description='convert image to ascii art')
    parser.add_argument('--input', '-i', required=True, type=str)
    parser.add_argument('--output', '-o', required=True, type=str)
    parser.add_argument('--scale', '-s', type=int, default=1)
    parser.add_argument('--html', action='store_true')
    args = parser.parse_args()

    img = Image.open(args.input)
    pix = img.load()
    (width, height) = img.size

    rows = []
    for y in range(0, height, args.scale):
        row = []
        for x in range(0, width, args.scale):
            (r, g, b, a) = pix[x, y]
            # gray = r * 0.3 + g * 0.59 + b * 0.11
            gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
            if a == 0:
                gray = 255
            row.append(get_char(gray, args.html))
            if args.html:
                continue
            row.append(get_char(gray, args.html))
            row.append(get_char(gray, args.html))
        # if args.html:
        #     row.append('<br>')
        # else:
        #     row.append('\n\r')
        row.append('\n\r')
        rows.append(row)

    if args.html:
        with open('template.html') as template:
            lines = template.readlines()
            line = ''
            for row in rows:
                for char in row:
                    line += char
            lines[21] = line
            rows = lines

    with open(args.output, 'w') as output_file:
        for row in rows:
            for char in row:
                output_file.write(char)


if __name__ == "__main__":
    main()
