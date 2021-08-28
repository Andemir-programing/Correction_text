import enchant

dictionary = enchant.Dict('en_US')
print(dictionary.check('driver'))

print(dictionary.check('draiver'))

print(dictionary.suggest(u'draiver'))

import difflib

woi = 'draiver'
sim = dict()

dictionary = enchant.Dict('en_US')
suggestions = set(dictionary.suggest(woi))

for word in suggestions:
    measure = difflib.SequenceMatcher(None, woi, word).ratio()
    sim[measure] = word

print('Coerrect word is:', sim[max(sim.keys())])

from enchant.checker import SpellChecker

checker = SpellChecker('en_US')
checker.set_text('I have got a new kar and it is ameizing.')
print([i.word for i in checker])

from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter

checker_with_filters = SpellChecker('en_US', filters=[EmailFilter])
checker_with_filters.set_text('Hi! My neim is John and thiz is my email: johnnyhatesjazz@gmail.com.')
print([i.word for i in checker_with_filters])
