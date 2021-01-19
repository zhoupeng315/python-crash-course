import pizza

pizza.make_pizza(16, 'peperoni')
pizza.make_pizza(12, 'mushroom', 'green peper', 'extra cheese')

from pizza import make_pizza as mp

mp(16, 'peperoni')
mp(12, 'mushroom', 'green peper', 'extra cheese')