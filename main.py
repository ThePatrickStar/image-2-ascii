from PIL import Image
import argparse


def get_char(gray):
    # chars = ['@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', ' ']
    chars = ['@', '#', 'k', 'i', '.', ' ']
    idx = int(((255.0 - gray) / 255) * (len(chars) - 1))
    return chars[idx]


def main():
    parser = argparse.ArgumentParser(description='convert image to ascii art')
    parser.add_argument('--input', '-i', required=True, type=str)
    parser.add_argument('--output', '-o', required=True, type=str)
    parser.add_argument('--scale', '-s', type=int, default=1)
    args = parser.parse_args()

    img = Image.open(args.input)
    pix = img.load()
    (width, height) = img.size

    rows = []
    for y in range(0, height, args.scale):
        row = []
        for x in range(0, width, args.scale):
            (r, g, b, a) = pix[x, y]
            gray = r * 0.3 + g * 0.59 + b * 0.11
            if a == 0:
                gray = 0.0
            row.append(get_char(gray))
            row.append(get_char(gray))
            row.append(get_char(gray))
        row.append('\n\r')
        rows.append(row)

    with open(args.output, 'w') as output_file:
        for row in rows:
            for char in row:
                output_file.write(char)


if __name__ == "__main__":
    main()
