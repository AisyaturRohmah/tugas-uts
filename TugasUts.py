'''finalis class music'''
from time import strftime


def score_finalis():
    print ("1. regina \t = 83")
    print ("2. Agatha \t = 85")
    print ("3. cymbre \t = 65")
    print ("4. Dhinar\t = 82")
    print ("5. mahanta\t = 69")
      
score_finalis()
data = str(input('masukkan nama yg akan di cek : '))
if data == 'regina':
    lulus = 'lulus'
    print(f'dengan score 83 dinyatakan {lulus}')

if data == 'Agatha':
    lulus = 'lulus'
    print(f'dengan score 85 dinyatakan {lulus}')

if data == 'cymbre':
    tidak_lulus = 'tidak lulus'
    print(f'dengan score 65 dinyatakan {tidak_lulus}')

if data == 'Dhinar':
    lulus = 'lulus'
    print(f'dengan score 82 dinyatakan {lulus}')

if data == 'mahanta':
    tidak_lulus = 'tidak lulus'
    print(f'dengan score 69 dinyatakan {tidak_lulus}')

else:
    print('iya')





