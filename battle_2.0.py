a = 2
b = 3
#entèval la
x =1
y = 20

miltip_a = []
for i in range(x, y+1):
    if i % a == 0:
        miltip_a.append(i)
print(f"Miltip {a} yo se")
for num in miltip_a:
    print(f"{num}", end=", ")
print(f"--> {sum(miltip_a)}")

miltip_b = []        
for j in range(x, y+1):
    if j % b == 0:
        miltip_b.append(j)
print(f"Miltip {b} yo se")
for num in miltip_b:
    print(f"{num}", end=", ")
print(f"--> {sum(miltip_b)}")
        
miltip_a_b = []
for ab in range(x, y+1):
    if ab % a == 0 and ab % b ==0:
        miltip_a_b.append(ab)
print(f"Miltip {a} ak {b} yo se")
for num in miltip_a_b:
    print(f"{num}", end=", ")
print(f"--> {sum(miltip_a_b)}")
        
not_miltip = []
for _ab in range(x, y+1):
    if _ab % a != 0 and _ab % b != 0:
        not_miltip.append(_ab)
print(f"Ki ni Miltip {a} ni {b}  yo se")
for num in not_miltip:
    print(f"{num}", end=", ")
print(f"--> {sum(not_miltip)}")
        
    