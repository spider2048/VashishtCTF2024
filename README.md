# Vashist CTF 2024

## Challenge Ideas

See: [Ideas](/Challenges.md)

## Guidelines

### Compiling C/C++ Code

Always use the `gcc` docker image to compile programs - so that your builds will be consistent.

```bash
$ docker pull gcc
```

To run an instance of it in your folder, use:

```bash
$ docker run --rm -v $(pwd):/usr/src -v /usr/src -it gcc /bin/bash
```

After that, you can simply run:

```bash
$ g++ <args>
```

Do not optimize your code, **only** use `-Oz` because it makes your challenges harder.


### Making Web Applications

Make sure that:

* All (npm/pip) packages are up to date
* User input is **always** escaped/sanitized and in some cases has a word limit
* Every endpoint is **ratelimited**

For python apps:

* Use `poetry` Basic usage [here](https://python-poetry.org/docs/basic-usage/)
