# AES-128 (CTR) & RSA-OAEP

Trabalho final do curso de segurança computacional da Universidade de Brasília

Rodrigo Mamédio Arrelaro & Eduardo Xavier

# Módulo I - Cifração com RSA(OAEP) e AES-128(CTR)

A chave 'K' utilizada pelo AES-128 é cifrada utilizando o RSA, após as duas tuplas geradas, sendo elas chave pública e privada, respectivamente. É calculado o SHA-3 do texto plano antes do processo de cifração realizado com AES.
Após a cifração realizada, o arquivo "texto.txt" é lido e transferido para ser realizada a cifração utilizando o AES-128 (CTR), tendo a saída no próprio "texto.txt".

# Módulo II - Parsing e Assinatura
cancelado

# Módulo III - Verificador
É realizada a comparação das hashes com a mensagem decifrada e, caso verdadeiro, a mensagem é printada para o usuário, bem como a confirmação do sucesso da operação.
