extensions = {
    "py":"python",
    "c":"C",
    "cpp":"C++",
    "java":"Java",
    "js":"Javascript",
    "php":"php",
    "html":"html",
}

filename = input("Input the Filename: ").strip()
if '.' in filename:
    e = filename[filename.index('.')+1:]
    if e in extensions:
        print("The extension of the file is: '"+extensions[e]+"'")
    else:
        print("Extension Not Known")
else:
    print("Invalid Filename")