## Strings

O script presente no arquivo 'strings/Python/src/script.py' soluciona tanto a parte 1 como a 2, tendo que foi contruido em uma estrutura de linha de comando:
```Shell
python script.py [source] [--limit/-n] [--justified] [--write] [--help/-h]
```
O uso pode ser notado de acordo com a tabela:

| Campo       | Obrigatório   | Descrição
| ---         | ---           | ---   
| source      | sim           | O arquivo de origem
| --limit/-n  | sim           | O limit de caracteres por linha
| --justified | não           | Justifica o conteúdo da saída
| --write     | não           | Escreve em um arquivo a saída (omitindo do terminal)
| --help/-h   | não           | Escreve no terminal um texto de ajuda

### Parte 1
Para obter o resultado semelahnte ao exemplificado em output_parte1.txt:
```Shell
python script.py quote.txt --limit 40 --write
```

### Parte 2
Para obter o resultado semelhante ao exemplificado em output_parte2.txt:
```
python script.py quote.txt --limit 40 --justified --write
```

##### OBS: Para obter um resultado idêntico (mesmo conteúdo):
substitua o nome do arquivo pelo do exemplo:
```Shell
python script.py example.txt --limit 40 [--justified] --write
```

OBS: Não foi utilizado o formato 'nome;nome' por dois motivos principais:
1. quando usado em linha de comando ';' inicia um novo comando, sendo que python script.py cats;dogs inicia o script para 'cats' e tenta iniciar um comando 'dogs'.
2. reddit aceita threads com ';' ficando impossibilitado de se obter as postagens para estes tópicos caso se use ';' como separador.