# Desafios

## Crawlers

### Parte 1

O script presente no arquivo 'crawlers/Python/src/script.py' soluciona a parte 1, devendo ser executado por linha de comando:
```Shell
python script.py [threads]
```

O uso pode ser notado de acordo com a tabela:

| Campo       | Obrigatório   | Descrição                               | Valor mínimo de upvotes
| ---         | ---           | ---                                     | ---
| threads     | sim           | nomes de threads a serem vasculhadas    | 5000

Exemplo:
```Shell
python script.py cats dogs
```

resultado examplo:
```json
URL: https://www.reddit.com/r/cats
STATUS: 200
REASON: OK

URL: https://www.reddit.com/r/dogs
STATUS: 200
REASON: OK

[
    {
        "cats": [
            {
                "commentaries_link": "https://www.reddit.com/r/cats/comments/9nitmu/my_first_rescue_i_guess_im_gonna_be_a_catdad/",
                "subreddit": "cats",
                "subthread_link": "https://www.reddit.com/r/cats/search?q=flair_name%253A%2522Cat%2520Picture%2522&restrict_sr=1",
                "title": "My first rescue I guess I'm gonna be a catdad...",
                "upvotes": "7.8k"
            }
        ]
    },
    {
        "dogs": []
    }
]
```

### Parte 2