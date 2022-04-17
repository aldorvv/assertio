# Assertio

Pseudo-functional Python api testing framework.

## Installation

`pip install assertio`

## Basic Usage

Assertio consists on create requests on a chain way, you can organize
this requests within a Runner class in order to define test cases.

You can find below an example using the [Pokemon API](https://pokeapi.co)

```python
# main.py
from assertio import Request, Runner


class MyRunner(Runner):

    def test_get_pikachu(self):
        Request()\
            .to("/pokemon/pikachu")\
            .with_method("GET")\
            .perform()\
            .assert_http_ok()\
            .assert_response_field("name")\
            .equals("pikachu")

MyRunner().start()

```

This will run all the defined methods within `MyRunner` as long as they start
with `test`.

Wait, where should I add my API URL? 
Well you can export an enviromnent variable for that!

```bash
$ export ASSERTIO_BASE_URL=https://pokeapi.co/api/v2
```

Once this environment variable is setup let's start the test!

```bash
$ python main.py
```

Should do the trick!


But that's not it!

Assertio has many assertions defined and is flexible enough to let you define
your custom assertions and preconditions.

You can chain as many assertions and preconditions as you want, just remember
to keep it simple, if your request chain is 15 lines long, maybe it's time
to consider to split it in smaller tests.

Anyway, let's take a look to a more complex example using a POST to a custom
API.

Remember to change the `ASSERTIO_BASE_URL` environment variable

```bash
$ export ASSERTIO_BASE_URL=http://my-books-api-domain/api/v1
```

And let's try to add a new resource.

```python

# main.py
from assertio import Request, Runner

DEFAULT_HEADERS = {"Content-Type": "application/json"}
BOOK_PAYLOAD = {
    "id": 144,
    "title": "The Divine Comedy", 
    "author": {
        "id": 12,
        "name": "Dante Alighieri",
        "nationality": "Italian"
    }, 
    "year": 1472
}

class MyRunner(Runner):

    def test_create_book(self):
        Request()\
            .to("/books/")\
            .with_method("POST")\
            .with_headers(DEFAULT_HEADERS)\
            .with_body(BOOK_PAYLOAD)\
            .perform()\
            .assert_http_created()\
            .assert_response_field("author.nationality")\
            .equals("Italian")

MyRunner().start()
```

All the tests must start with `test`! 
Otherwise `start()` method will not run it

