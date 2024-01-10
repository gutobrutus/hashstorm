# **HashStorm**

## 1. Introdução

Aplicação CLI em Python para realizar o decode de hashes, baseado em um ataque de força bruta a partir de uma wordlist.

### Licença

[GPLv3](LICENSE)

## 2. Instalação

```shell
pip install hashstorm
```
**Checando a versão**:
```shell
hashstorm -v
```
ou
```shell
hashstorm --version
```
### 2.1. Pré-requisitos:
1. Python 3.10 ou superior
2. Pip

## 3. Exemplos de uso

1. Texto em claro teve aplicação de md5 -> base64 -> sha1. Tem-se o hash sha1, tentativa através da wordlist, voltar e chegar no texto em claro:
```shell
hashstorm wordlist/storm-wordlist.txt md5,base64,sha1
```
2. Texto em claro teve aplicação de md5 -> sha512. Tem-se o hash sha512, tentativa através da wordlist, voltar e chegar no texto em claro:
```shell
hashstorm wordlist/storm-wordlist.txt md5,sha512
```
3. Texto em claro teve aplicação de sha256 -> md5 -> base64 -> sha1. Tem-se o hash sha512, tentativa através da wordlist, voltar e chegar no texto em claro:
```shell
hashstorm wordlist/storm-wordlist.txt sha256,md5,base64,sha1
```
4. Consultando o help:
```shell
hashstorm -h
```
ou
```shell
hashstorm --help
```
