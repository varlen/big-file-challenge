# Big File Challenge

How to process a big file with little memory? Here's a solution using Python.

Originally from [here](https://twitter.com/zanfranceschi/status/1532505851658784768). Full text also [here](https://dev.to/zanfranceschi/desafio-processar-arquivos-grandes-com-restricao-de-memoria-2ie)

Thanks [@zanfranceschi](https://twitter.com/zanfranceschi/)!

---

### Explanation

The key concept here is: It is not possible to load the entire file on memory. You must understand the behavior of the language or tooling you are using to parse the file to ensure that only a small part of the file is using memory at a given time.

When opening a file, Python will not bring its contents into memory automatically. Instead, it will keep a reference to the file in disk that can be used to fetch the file contents.This is necessary to work with large files.

But there's a catch: one common pratice in Python is to access the file contents using ```file.readlines()```. This approach is not valid for this challenge and won't work.

The reason is that the ```.readlines()``` method returns a list, therefore loading the entire file into memory during its execution.

The ```.readline()``` method, however, read a single line each time its called, until it reaches EOF, returning a falsey value.

That's exactly what's needed for this challenge. ```.readline()``` allows us to lazily read the file, keeping the memory consumption low.

This solution also uses a ```defaultdict```, which is a dictionary structure that returns a default value when a key is not found, removing the need to check if a key exists explicitly.

It also uses the ```:=``` operator, allowing to check a condition and attribute a value in the same line.

---

### How to run

Build image with:
```
docker build . -t challengebigfile
```

Then run with:
```
docker run --memory="20m" challengebigfile
```
