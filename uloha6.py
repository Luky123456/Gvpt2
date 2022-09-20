x = input("Zadaj mi najmenšiu stranu trojuholníka: ")
y = input("Zadaj mi stredne dlhú stranu: ")
z = input("Zadaj mi najdlhšiu stranu: ")
x=int(x)
y=int(y)
z=int(z)
if x <= y <= z and (x+y)>z:
	if (x**2+y**2)==z**2:
		print("Tento trojuholník je pravouhlý")
	elif x==z==y:
		print("Tento trojuholník je rovnostranný")
	elif x==y or y==z or z==x:
		print("Tento trojuholník je rovnoramenný")
	else:
		print("Tento trojuholník je obyčajný")
else:
	print("Takýto trojuholník nemôže existovať")