# smol trie py
it's a smol (28 lines) pure python trie / prefix tree implementation


### example


```
>>> t = {} # use a regular dict
>>> add(t, 'muri')
>>> add(t, 'muda')
>>> add(t, 'mura')
>>> print(*items(at(t, 'mu')))
muri mura muda
```
