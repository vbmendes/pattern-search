import os
import timeit
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

sys.path.append(ROOT_DIR)


def fixture(name):
    return os.path.join(ROOT_DIR, 'tests', 'fixtures', name)

setup = """

import json
from pattern_search.nary_search_tree import Tree
from pattern_search.pattern_search_dict import PatternSearchDict

def search_in_list(l, p):
    return [c for c in l if c['nome_cidade'].startswith(p)]

def search_in_tree(t, p):
    return t.search(p)

def search_in_native(t, p):
    return t[p]
"""

le_arquivo = """
with file('%s', 'r') as f:
    l = json.loads(f.read()[:-2])
""" % fixture('cidades.json')

monta_arvore = """
t = Tree()
for c in l:
    t.push(c['nome_cidade'], c)
"""

monta_arvore_nativo = """
nt = PatternSearchDict(lambda obj: obj['nome'])
for c in l:
    nt.push(c)
"""


ts = timeit.Timer(setup)
ta = timeit.Timer(le_arquivo, setup=setup)
tm = timeit.Timer(monta_arvore, setup=setup + le_arquivo)
tmn = timeit.Timer(monta_arvore_nativo, setup=setup + le_arquivo)
#til = timeit.Timer("search_in_list(l, 'Nat')", setup=setup+le_arquivo)
tit = timeit.Timer("search_in_tree(t, 'Nat')", setup=setup + le_arquivo + monta_arvore)
titn = timeit.Timer("search_in_native(nt, 'Nat')", setup=setup + le_arquivo + monta_arvore_nativo)

count = int(sys.argv[1])

print 'setup\t\t\t\t\t\t%s' % ts.timeit(1)
print 'read fixtures\t\t\t\t\t%s' % ta.timeit(1)
print 'create nary_search_tree\t\t\t\t%s' % tm.timeit(1)
print 'create pattern_search_dict\t\t\t%s' % tmn.timeit(1)
#print '%d le lista\t\t%s' % (count, til.timeit(count))
print '%d searchs in nary_search_tree\t\t%s' % (count, tit.timeit(count))
print '%d search in pattern_search_dict\t\t%s' % (count, titn.timeit(count))
