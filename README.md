# djavue

creator: [tonylampada](https://github.com/tonylampada)

based on: [evolutio/djavue](https://github.com/evolutio/djavue)

## `backend` set-up

### `pyenv`

you should have installed `pyenv`, so you can manage multiple python versions.  
> you can get the version used in this project, by checking the **file**:  
>
> `.python-version`
>
> at the root project folder.

if you don't have `pyenv` already installed, check this [guide](https://github.com/pyenv/pyenv#installation)

### `virtualenv`

```bash
pyenv which virtualenv
```

> if you get a response like:
>
> ```bash
> pyenv: virtualenv: command not found
> ```
>
> you should run:
> >
> > ```bash
> > pip install virtualenv
> > ```
> >
> if everything is ok, just follow.

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## `frontend` set-up

TODO

## `docker` set-up

TODO
