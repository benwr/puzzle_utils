DEC = "0123456789"
CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
BASE64 = CAPS + ALPHA + DEC + '+/'
FUCKED64 = DEC + CAPS + ALPHA + '+/'
FUCKED65 = ALPHA + CAPS + DEC + '+/'
FUCKED66 = '+/' + CAPS + ALPHA + DEC
FUCKED67 = DEC + ALPHA + CAPS + '+/'
HEX = DEC + ALPHA[:6]
ASCII = (' ' * 33 + '!"#$%&\'()*+,-./' + DEC + ':;<=>?@' +
         CAPS + "[\\]^_`" + ALPHA + "{|}~ ")

EN_CHAR_FREQS = [82, 15, 28, 43, 127, 22, 20, 61, 70, 2, 8, 40, 24,
                 67, 75, 19, 1, 60, 63, 91, 28, 10, 23, 2, 20, 1]


def from_base(s, base=16, alphabet=HEX):
    indices = {}
    for i, a in enumerate(alphabet):
        indices[a] = i

    strlen = len(s)
    acc = 0
    for i, c in enumerate(s):
        acc += base ** (strlen - i - 1) * indices[c]
    return acc


def to_base(i, base=16, alphabet=HEX, minwidth=1):
    result = []
    neg = i < 0
    if neg:
        i = -i

    while i > 0 or len(result) < minwidth:
        result.append(alphabet[i % base])
        i = i // base

    if neg:
        result.append("-")

    return ''.join(reversed(result))


def convert_base(s, base_a, alpha_a, base_b, alpha_b):
    val = from_base(s, base=base_a, alphabet=alpha_a)
    return to_base(val, base=base_b, alphabet=alpha_b)


def rot_n(s, shift=13, base=26, alphabet=ALPHA, negate=False):
    indices = {}
    for i, a in enumerate(alphabet):
        indices[a] = i

    result = []
    for c in s:
        if negate:
            result.append(alphabet[
                (base - indices[c] + shift) % base] if c in indices else c)
        else:
            result.append(alphabet[
                (indices[c] + shift) % base] if c in indices else c)

    return ''.join(result)


def freqs(s):
    d = {}
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1

    return d
