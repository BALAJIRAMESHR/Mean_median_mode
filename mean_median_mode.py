rahul=[10,0,100,20,50]
ajay=[40,30,40,30,40]

s=len(rahul)
rahul.sort()
total=sum(rahul)
mean1=total/s
print("mean1",mean1)
s2=len(ajay)
ajay.sort()
total=sum(ajay)
mean2=total/s
print("mean1",mean2)
print('------------------------------------------------')

if s%2!=0:
    print("median",rahul[s//2])
else:
    q=rahul[(s//2)-1]+rahul[s//2]
    print("meadian",q//2)

if s2%2!=0:
    print("median",ajay[s2//2])
else:
    q=ajay[(s2//2)-1]+ajay[s2//2]
    print("meadian",q//2)

print('------------------------------------------------')

mode1=0
for i in rahul:
    c1=rahul.count(i)
    if c1 > mode1:
        mode1=c1
        c3=i
        
if mode1==1:
    print("Mode of first player is =0")
else:
    print("mode",c3)
print('------------------------------------------------')
mode2=0
for f in ajay:
    c2=ajay.count(f)
    if c2 > mode1:
        mode1=c2
        c4=i
        
if mode2==1:
    print("Mode of first player is =0")
else:
    print("mode",c4)
print('------------------------------------------------')

variance1=0
sum1=0
for i in rahul:
    sum1=sum1+(i-mean1)**2

sd=(sum1/s)**0.5
print("sd",sd)
variance1=sd**2
print("variance1",variance1)
print('------------------------------------------------')


variance2=0
sum2=0
for j in ajay:
    sum2=sum2+(j-mean2)**2

sd2=(sum2/s2)**0.5
print("sd",sd2)
variance2=sd2**2
print("variance2",variance2)



from matplotlib import pyplot as pyplot
pyplot.hist([rahul,ajay])
pyplot.show
