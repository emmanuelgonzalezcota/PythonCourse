# Demonstrating the lstrip() method

print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))

page = "pythoninstitute.org"
pager = page.lstrip("p.org")
print(pager)

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)
