x=input("Zadaj mi číslo s viac ako jednou cifrou: ")
y=input("Zadaj mi číslo s viac ako jednou cifrou: ")
z=len(x)-1
f=len(y)-1
c=x[z]
v=y[f]
n=int(v+c)
if len(x) < 2 or len(y) <2:
	print("Podmienka nebola splnená")
elif n%2==0:
	print("Súčet posledných dvoch cifier čísel je párny")
else:
	print("Súčet posledných dvoch čísel nie je párny")
