DEC = "0123456789"
CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
BASE64 = CAPS + ALPHA + DEC + '+/'
HEX = DEC + ALPHA[:6]
ASCII = (' ' * 33 + '!"#$%&\'()*+,-./' + DEC + ':;<=>?@' +
         CAPS + "[\\]^_`" + ALPHA + "{|}~ ")

EN_CHAR_FREQS = [82, 15, 28, 43, 127, 22, 20, 61, 70, 2, 8, 40, 24,
                 67, 75, 19, 1, 60, 63, 91, 28, 10, 23, 2, 20, 1]


def from_base(s, base=16, alphabet=HEX):
    """Interpret `s` as representing a value in the specified base/alphabet.

    (basically a slightly fancier version of `int(s, base)`)

    s: The string to read. Must contain only characters in `alphabet`.
    alphabet: The character set to assume `s` is using. There can be more
         than `base` characters in `alphabet`; only the first `base` characters
         are used. Defaults to the HEX character ordering ('01234567890abcdef').
         Other alphabets are available: ASCII, BASE64, ALPHA, CAPS
    base: The base in which the string should be interpreted. Defaults
         to 16 for hex interpretation.

    Returns a python integer.
    """
    indices = {}
    for i, a in enumerate(alphabet):
        indices[a] = i

    strlen = len(s)
    acc = 0
    for i, c in enumerate(s):
        acc += base ** (strlen - i - 1) * indices[c]
    return acc


def to_base(i, base=16, alphabet=HEX, minwidth=1):
    """Stringify an integer using digits from a given alphabet.

    i: The integer to interpret.
    base: The base to use. Must be no larger than the `len(alphabet)`.
    alphabet: A string of digits to use to encode the alphabet. Defaults to
         the hexadecimal characters ('0123456789abcdef').
    minwidth: If the output would be shorter than this width,
         it will be padded with the zero character until it is this long.
         Defaults to 1, which will cause an input of `0` to be shown as
         the zero character. If it were 0, `0` would be shown as the empty
         string.

    Returns a python string.
    """
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
    """Do from_base, and then do to_base with the result."""
    val = from_base(s, base=base_a, alphabet=alpha_a)
    return to_base(val, base=base_b, alphabet=alpha_b)


def rot_n(s, shift=13, base=26, alphabet=ALPHA, negate=False):
    """Caesar cipher.
    
    s: The string to shift.
    shift: The (integer) direction to shift through the alphabet.
         Defaults to 13.
    base: The base to shift through
    alphabet: The characterset to shift through. If a character
         is not in this alphabet, it will be left alone in the
         result. Defaults to *ONLY LOWERCASE* characters. A
         more principled way to handle this would be to accept
         a list of alphabets as the argument (to allow lower
         and upper case to be shifted separately, or for
         other weird ciphers)
    negate: I needed this once but probably never will again.
    """
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
