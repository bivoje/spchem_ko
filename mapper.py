#!/usr/bin/python3

import importlib
pureomoa = importlib.import_module("pureo-moa")
pureosseugi = pureomoa.pureosseugi
import sys

# unicode code points in order they are arranged in
# normal/medium/large/tiny/tooltip.png
raw_mapping_list = [
  list(range(0x0020, 0x0080)), # 1: _ ! " ... 3: } ~ _ # Basic Latin
  list(range(0x00A0, 0x0100)), # 4: _ ¡ ¢ ... 6: ý þ ÿ # Latin 1 Suppliment
  list(range(0x0100, 0x0180)), # 7: Ā ā Ă ...10: Ž ž ſ # Latin Extended A
  list(range(0x01F0, 0x0200)), #11: ǰ Ǳ ǲ ...11: ǽ Ǿ ǿ # Latin Extended B
  list(range(0x0384, 0x03D0)), #11: ΄ ΅ Ά ...13: ύ ώ Ϗ # Greek and Coptic
  list(range(0x0400, 0x0460)), #14: Ѐ Ё Ђ ...16: ѝ ў џ # Cyrillic
  list(range(0x0490, 0x04A0)), #17: Ґ ґ Ғ ...17: ҝ Ҟ ҟ # Cyrillic
  list(range(0x1EF0, 0x1EFA)), #18: Ự ự Ỳ ...18: ỷ Ỹ ỹ # Latin Extended Additional
  list(range(0x20A0, 0x20B0)), #18: ₠ ₡ ₢ ...18: ₭ ₮ ₯ # Currency Symbols
  list(range(0x2080, 0x208C)), #19: ₀ ₁ ₂ ...19: ₉ ₊ ₋ # Superscripts and Subscripts
]

#mapping_alpha = list(map(chr,range(0x00C0, 0x00C0+33)))
#mapping_jamo = 'ㅁ ㅎ ㅊ ㅜ ㄷ ㄹ ㅠ ㅗ ㅑ ㅓ ㅏ ㅣ ㅡ ㅇ ㅐ ㅂ ㅔ ㄱ ㄴ ㅅ ㅕ ㅍ ㅈ ㅌ ㅛ ㅋ ㄸ ㅒ ㅖ ㅃ ㄲ ㅆ ㅉ'.split()
mapping_alpha = list(map(chr,range(0x0120, 0x0120+33)))
mapping_jamo = 'ㄸ ㅒ ㅖ ㄲ ㅃ ㅆ ㅉ ㅁ ㅂ ㅏ ㄷ ㅊ ㄱ ㅇ ㄹ ㅎ ㅑ ㅓ ㅠ ㅅ ㄴ ㅣ ㅗ ㅔ ㅐ ㅡ ㅈ ㅜ ㅕ ㅍ ㅌ ㅛ ㅋ'.split()

shadowed = set()

for line in sys.stdin.readlines():
  buff = ""
  for ch in pureosseugi(line):
    if ch in mapping_alpha:
      shadowed.add(ch)
      buff += chr(ord(ch)+0x40 if ch == 0x00C0 else ord(ch)+0x20)
    elif ch in mapping_jamo:
      idx = mapping_jamo.index(ch)
      buff += mapping_alpha[idx]
    else:
      buff += ch
  print(buff, end='')

print(shadowed, file=sys.stderr)
