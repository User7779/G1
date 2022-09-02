import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

mengetik('Jangan Lupa Subscribe Channel User Eror21.. \n Selamat Menonton \n Terimakasih..')
