from out import OpenCC

cc = OpenCC.opencc_open("out/s2t.json")
text = "测试"
result = OpenCC.opencc_convert_utf8(cc, text, len(text.encode("utf-8")))
OpenCC.opencc_close(cc)

print("{0} --> {1}".format(text, result))
