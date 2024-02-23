# Vashist CTF 2024

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
