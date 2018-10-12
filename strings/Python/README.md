# Desafios

## Strings

O script presente no arquivo 'src/script.py' soluciona tanto a parte 1 como a 2, tendo que foi contruido em uma estrutura de linha de comando:
```Shell
python src/script.py [source] [--limit/-n] [--justified] [--write] [--help/-h]
```
O uso pode ser notado de acordo com a tabela:\

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
python src/script.py quote.txt --lines 40 --write
```

### Parte 2
Para obter o resultado semelhante ao exemplificado em output_parte2.txt:
```
python src/script.py quote.txt --lines 40 --justified --write
```

##### OBS: Para obter um resultado idêntico (mesmo conteúdo):
substitua o nome do arquivo pelo do exemplo:
```Shell
python src/script.py example.txt --lines 40 [--justified] --write
```