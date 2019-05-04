adict = {}
adict["a"] = "@"
adict["b"] = "8"
adict["c"] = "("
adict["d"] = "|)"
adict["e"] = "3"
adict["f"] = "#"
adict["g"] = "6"
adict["h"] = "[-]"
adict["i"] = "|"
adict["j"] = "_|"
adict["k"] = "|<"
adict["l"] = "1"
adict["m"] = "[]\/[]"
adict["n"] = "[]\[]"
adict["o"] = "0"
adict["p"] = "|D"
adict["q"] = "(,)"
adict["r"] = "|Z"
adict["s"] = "$"
adict["t"] = "']['"
adict["u"] = "|_|"
adict["v"] = "\/"
adict["w"] = "\/\/"
adict["x"] = "}{"
adict["y"] = "`/"
adict["z"] = "2"

i = input()
o = []
for C in i:
    c = C.lower()
    if c in adict:
        o.append(adict[c])
    else:
        o.append(c)
print("".join(o))