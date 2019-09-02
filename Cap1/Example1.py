# -*- coding: latin-1 -*-

"""
Examples by: LeTurtleBoy
GitHub: https://github.com/LeTurtleBoy

Examples of implementation of chapter 1 of Fluent Python:
    use of special python methods "__methodname__"

Ejemplos de implementación del capitulo 1 de Fluent Python:
    uso de los metodos especiales de python "__methodname__"
"""

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split() # 'spades diamonds clubs hearts'
    
    """
    Creamos la clase y con su constructor inicializamos las variables necesarias
    que dan sentido a la case, en este ejemplo se construlle una baraja francesa 
    y se agregan todos los valores posibles en un mazo de cartas.

    We create the class and with its constructor we initialize the necessary variables
    that give meaning to the case, in this example a French deck is built
    and all the possible values ??are added in a deck of cards.
    """

    def __init__(self): 
        
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]

    """
    implementación del metodo __len__, con este uso podemos saber que nuestra clase tiene un tamaño,
    para cada definición es diferente, en este caso la longitud logica de una baraja de naipes es la cantidad
    de cartas que posee, por ende se "sobrecarga" el metodo indicando que cuando se use el metodo len(), tendremos
    un resultado logico en nuestra clase.

    
    implementation of the __len__ method, with this use we can know that our class has a size,
    for each definition is different, in this case the logical length of a deck of cards is the amount
    of letters that he owns, therefore the method is "overloaded" indicating that when the len () method is used, 
    we will have a logical result in our class.
    """
    def __len__(self):
        return len(self._cards)

    """
    implementación del metodo __getitem__, con este uso podemos obtener un elemento de nuestra clase,
    en el contexto del ejemplo lo logico es obtener una de las cartas de la bara y por ende debemos
    retornar una carta segun su posición.

    
    implementation of the __getitem__ method, with this use we can obtain an element of our class,
    in the context of the example the logical thing is to obtain one of the cards of the bara and therefore we must
    return a letter according to your position.
    """

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck() # Creamos un objeto baraja, Create a deck object

"""
Podemos imprimir un elemento dentro de la baraja por su posición asi como una lista iterable de elementos.

we can print an element of the deck using his position, and also can get a list of elements in a pythonic way.
"""

print(deck[0]) #  imprimimos la primer carta del mazo, print fisrt card of the deck
print(deck[0::13]) #  imprimimos la primer carta de cada pinta mazo, print the first card of every color in the deck
