from math import trunc
import emoji

n = float(input('digite um numero: '))
print(f'o numero {n} tem a parte inteira {trunc(n)}')
print(emoji.emojize(':alien:', use_aliases=True))
