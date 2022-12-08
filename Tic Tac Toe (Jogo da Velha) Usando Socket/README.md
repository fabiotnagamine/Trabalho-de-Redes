# Jogo da Velha

O jogo da velha é um jogo extremamente simples e fácil aprendizado, o jogo se popularizou na Inglaterra do século 19, quando mulheres se reuniam no fim da tarde para poder conversar e bordar.

O nome jogo da velha veio do simples fato de que  mulheres idosas jogavam muito, pelo simples fatos de não conseguirem mais bordar por causa da vista, o nome jogo da velha não tem nada a ver com o original: nós e cruzes (tradução de Noughts and Crosses)

Porém sua origem é bem mais antiga datada do século 14 antes de Cristo, não se sabe ao certo sua origem, pois temos relatos várias civilizações (chineses, america pré-colombiana) 

## Descrição do Projeto
- Utilização o socket para implementação de um simples jogo da velha, podendo assim fazer a conexão entre 2 jogadores de forma simultânea
--- 
## Bibliotecas Usadas

##### Socket IO

Socket IO é uma biblioteca que permite comunicação de baixa latência , bidirecional e baseada em eventos entre um cliente e um servidor.

Ele é construído sobre o protocolo WebSocket e oferece garantias adicionais, como fallback para HTTP long-polling ou reconexão automática.

Existem várias implementações de servidor Socket IO disponíveis como Java Script, Java, Python, Golang, todas disponíveis com código no github.

E implementações de cliente na maioria dos principais idiomas JavaScript, Java, C++, Swift, Dardo, Python, .Net, Rust, Kotlin, também todas disponíveis com seu código no github.

Embora o Socket IO realmente use WebSocket para transporte quando possível, ele adiciona metadados adicionais a cada pacote. É por isso que um cliente WebSocket não poderá se conectar com sucesso a um servidor Socket IO, e um cliente Socket IO também não poderá se conectar a um servidor WebSocket simples.

O protocolo implementa no projeto para a criação do jogo é o protocolo HTTP além do protocolo TCP, no caso do TCP o servidor fica aguardando um jogador para jogar, não podemos iniciar o jogo sozinho


##### Pygame

O Pygame é um conjunto de módulos do python projetados em SDL, feita para escrever games. Permitindo a criação de jogos completos e programas multimidias na linguagem python.

O Pygame é um módulo muito portátil que roda em quase todas as plataformas e sistemas operacionais.

---

## Instalando os pacotes:
- Instalarndo os pacotes que serão utilizados para rodar o jogo:
```
pip install pygame
```

### Como Jogar?
- 1º Abra o terminal
- 2º Entre na pasta Jogo da Velha - Socket + Pygame
```
cd '.\04 Jogo da Velha - Socket + Pygame\'
```
- 3º Iniciando o servidor
```
py server.py
```

- Iniciado a conexão com o servidor, podemos agora iniciar a conexão para jogar, para conexões locais podemos utilizar o `localhost` ou podemos utilizar o endereço de loopback `127.0.0.1`
- Jogador 1
    - Iniciando o client do player 1:
    ```
    py player.py
    Entre com o IP : localhost
    Para saber o ip do host
    Terminal -> digitar ipconfig -> endereço de ipv4
    ```
    <img src = Help.png>
- Jogador 2 
    ```
     py player.py
    Entre com o IP : IP da máquina onde está hospedado o host
    ```





