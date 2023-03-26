whitespace = " \t\n\r\v\f"
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_extended = "¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýÿ"
ascii_letters = ascii_lowercase + ascii_uppercase
digits = "0123456789"
hexdigits = digits + "abcdef" + "ABCDEF"
octdigits = "01234567"
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace + ascii_extended
pools = [whitespace, ascii_lowercase, ascii_uppercase, ascii_extended, digits]

related_extended = [
    "Aa@4ÀÁÂÃÄÅÆàáâãäå",
    "BbÞß6Þ",
    "Cc¢çÇ",
    "Dd6Ð£",
    "Ee3§èéêë&",
    "Ff£#=",
    "Gg&¶",
    "Hhµ%",
    "Iil|!¦ìíîïÌÍÎÏ1",
    "Jj¶?¿",
    "Kk¥;",
    "LlI\/1",
    "Mmn",
    "Nnmñ",
    "Oo8ðòóôõöø©@ÒÓÔÕÖØ0",
    "PpqÞþ¶9",
    "Qq¶9",
    "Rr+£",
    "Ss5§2",
    "TtlI",
    "UuÙÚÛÜùúûüµ",
    "Vvw^¥<>",
    "Wwv",
    "Xx*×",
    "Yy¥ýÿÝ",
    "Zzs2",
]


related = [
    "Aa@4ÀÁÂÃàáâã",
    "Bb6",
    "CcçÇ",
    "Dd6Cc",
    "Ee3èéêë&",
    "Ff£#",
    "Gg&",
    "Hh%",
    "Iil|!ìíîÌÍÎ1",
    "Jj?",
    "Kk;",
    "LlI\/1",
    "Mmn",
    "Nnmñ",
    "OoòóôõÒÓÔÕ0",
    "Ppq9",
    "Qq9",
    "Rr+",
    "Ss52",
    "TtlI",
    "UuÙÚÛùúû",
    "Vvw^<>",
    "Wwv",
    "Xx*×",
    "YyýÝ",
    "Zzs2",
]
