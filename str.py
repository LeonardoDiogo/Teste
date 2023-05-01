string = "exemplo de string"  # string a ser invertida
string_invertida = ""  # inicializa a string invertida

for i in range(len(string)-1, -1, -1):  # percorre a string de trás para frente
    string_invertida += string[i]  # adiciona cada caracter na nova string

print(string_invertida)  # imprime a string invertida

"""Explicação do código:

Na primeira linha, é definida a string a ser invertida;
Em seguida, é inicializada a string que receberá os caracteres da string original, mas invertidos;
O laço for percorre a string original de trás para frente, ou seja, começando pelo último caractere e indo até o primeiro;
Dentro do laço, a cada iteração, o caractere atual é adicionado na nova string;
Por fim, a nova string invertida é impressa na tela."""
