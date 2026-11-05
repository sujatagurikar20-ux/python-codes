s = "Hello Python"
print("Original String", s)
print("Length", len(s))
print("Uppercase", s.upper())
print("Lowercase", s.lower())
print("Character at index 6:", s[6])
print("Position of Python:", s.find("Python"))
print("Slice:", s[6:])
print("Replace:", s.replace("Python", "Universe"))
print(s)
print("Contains Python:", "Python" in s)
print("Concatenation:", s + "Programming")
s2 = "   Hello world   "
print("Trim", s2.strip())
