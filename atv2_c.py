import math

angulo = int(input('Infome um angulo:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(' seno do angulo {}º é {:.2f},\n Cossenho: {:.2f},\n Tangente: {:.2f}.'.format(angulo, seno, cos, tan))
