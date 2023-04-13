# Protocolo HTTP

## Conteúdo
- [O que é o protocolo HTTP?](#o-que-é-o-protocolo-http)
- [Como o protocolo HTTP funciona?](#como-o-protocolo-http-funciona)
- [Métodos HTTP](#métodos-http)
- [URLs](#urls)
- [Cabeçalhos HTTP](#cabeçalhos-http)
- [HTTPS](#https)
- [REST](#rest)
- [Instruções de aplicação](#instruções)

## O que é o protocolo HTTP?

## Como o protocolo HTTP funciona?


## Métodos HTTP
...

## URLs
...

## Cabeçalhos HTTP
...

## HTTPS

O HTTPS (HTTP Secure) é usado para garantir a segurança da comunicação HTTP. Ele usa criptografia SSL/TLS para proteger a comunicação entre clientes e servidores da web.

## REST


## Instruções

### Servidor Web

Nesta aplicação, será colocado em prática os fundamentos da programação de sockets para conexões TCP em Python: 
1. Criar um soquete, vinculá-lo a um endereço e porta específicos, bem como enviar e receber um pacote HTTP; 
2. Noções básicas do formato de cabeçalho HTTP;
3. Desenvolvimento de um servidor Web que lida com uma solicitação HTTP por vez.
4. O servidor web deve aceitar e analisar uma solicitação HTTP, obtenha o arquivo solicitado do sistema de arquivos do servidor, criando uma resposta HTTP mensagem que consiste no arquivo solicitado precedido por linhas de cabeçalho e, em seguida, enviar a resposta diretamente para
o cliente. 
Se o arquivo solicitado não estiver presente no servidor, o servidor deverá enviar uma mensagem de volta para o cliente HTTP "404 Not Found".

### Executando o servidor

1. É necessário um arquivo HTML(por exemplo, HelloWorls.html), e ele deve estar no mesmo diretório que o arquivo do servidor.
2. Execute o programa do servidor.
3. Abra um navegador e forneça a URL correspondente ao endereço de IP (por exemplo, http://127.0.0.1:8081/HelloWorld.html).
4. Observe que, o IP utilizado neste exemplo, é determinado a partir do host que esta executando o servidor, e juntamente com a porta, podem ser alterados.
5. Será obtido uma resposta no navegador, caso o arquivo esteja no diretório, e a porta corresponder ao preenchido no código do servidor.
5. Em seguida, tente obter um arquivo que não esteja presente no servidor. Deverá receber uma mensagem “404 Not Found”.

### Notas adicionais

1. Para desenvolver o servidor, foi utilizado a linguagem de programação Python
2. Para escrita dos códigos foi utilizado o VScode
