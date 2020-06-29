def encoding(s1):
    print("Encoding")
    table = {}
    for i in range(0, 256):
        table[str(chr(i))] = i
    p = str(s1[0])
    c = ""
    code = 256
    output_code = []
    for i in range(0, len(s1)):
        if i != len(s1) - 1:
            c += s1[i+1]
        if p+c in table.keys():
            p = p+c
        else:
            print(p, "\t", table[p], "\t", p+c, "\t", code)
            output_code.append(table[p])
            table[p+c] = code
            code += 1
            p = c
        c = ""
    print(p, "\t", table[p])
    output_code.append(table[p])
    return output_code
 
 
def decoding(op):
    print("\nDecoding")
    table = {}
    for i in range(0, 256):
        table[i] = str(chr(i))
    old = op[0]
    s = table[old]
    c = str(s[0])
    print(s, end="")
    count = 256
    for i in range(0,len(op)-1):
        n = op[i+1]
        if n not in table.keys():
            s = table[old]
            s = s+c
        else:
            s = table[n]
        print(s, end="")
        c = str(s[0])
        table[count] = table[old] + c
        count += 1
        old = n
 
 
if __name__ == "__main__":
    s = "WYS*WYGWYS*WYSWYSG"
    output_code = encoding(s)
    print("Output Codes are: ", end="")
    for i in range(0, len(output_code)):
        print(output_code[i], end=" ")
    print()
    decoding(output_code)
