#!/usr/bin/python3

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

