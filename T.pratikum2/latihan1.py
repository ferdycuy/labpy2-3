e = int(input('Masukkan nilai e: '))
f = int(input('Masukkan nilai f: '))
g = int(input('Masukkan nilai g: '))

if e > f and e > g:
  print('e yang terbesar')
elif f > e and f > g:
  print('f yang terbesar')
else:
  print('g yang terbesar')