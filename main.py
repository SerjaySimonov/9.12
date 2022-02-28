listeven=[ ]
listodd=[ ]
listpos=[ ]
listneg=[ ]
listtens=[ ]
listhundreds=[ ]

N = int(input("Cik veseļu skaitļu: "))
for x in range(N):
  x = int(input("Ievadi tos: "))
  if x%2==0:
    listeven.append(x)
  if x%2!=0:
    listodd.append(x)
  if x>0:
    listpos.append(x)
  if x<0:
    listneg.append(x)
  if 10<=x<100:
    listtens.append(x)
  if x>=100:
    listhundreds.append(x)
if len(listeven)>len(listodd):
  print("Vairāk ir pāra skaitļu")
else:
  print("Vairāk ir nepāra skaitļu")
if len(listpos)>len(listneg):
  print("Vairāk ir pozitīvo skaitļu")
else:
  print("Vairāk ir negatīvo skaitļu")
if len(listtens)>len(listhundreds):
  print("Vairāk ir divciparu skaitļu")
else:
  print("Vairāk ir trisciparu skaitļu")