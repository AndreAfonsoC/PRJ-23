# PRJ-23


# Passos para Configurar Git e Colaborar no Projeto

### 1. **Instalar o Git**
- Baixar e instalar o Git: [Download do Git](https://git-scm.com/downloads)

### 2. **Configurar o Git**
- No terminal, configurar o nome de usuário e e-mail:
  ```bash
  git config --global user.name "Seu nome"
  git config --global user.email "email@example.com"
  ```

### 3. **Clonar o Repositório do GitHub**
- Para baixar o projeto, rodar o comando:
  ```bash
  git clone https://github.com/AndreAfonsoC/PRJ-23
  ```

### 4. **Criar uma Branch Própria**
- Sempre trabalhar em uma branch separada. Após clonar o repositório, criar uma branch:
  ```bash
  git checkout -b nome-da-branch
  ```
Exemplo:
  ```bash
  git checkout -b confeti
  ```
Nesse caso, eu irei modificar tudo nessa parte antes de subir para a versão oficial do grupo (que seria a branch main)

### 5. **Fazer Alterações**
- Modificar os arquivos necessários. Depois de fazer as mudanças, adicionar os arquivos:
  ```bash
  git add .
  ```
- Fazer o commit das mudanças:
  ```bash
  git commit -m "Descrição das alterações"
  ```
Descreva cada alteração de maneira clara.
Contraexemplo: "mudança médico 1"
Exemplo bom: "mudança nas dimensões da asa do hermes"

### 6. **Puxar Atualizações do Repositório (git pull) (não faça sempre)**
Cuidado com esse passo! Só fazê-lo caso você tenha criado uma função nova, que não havia ainda no projeto!
Se você estiver modificando, por exemplo, a design_tools_hermes.py e fizer pull ele vai sumir suas modificações

- Antes de enviar as mudanças para o GitHub, garantir que estão com a versão mais recente do projeto:
  ```bash
  git pull origin main
  ```

### 7. **Enviar a Branch para o GitHub (git push)**
- Para enviar as mudanças para o GitHub:
  ```bash
  git push origin nome-da-branch
  ```

### 8. **Criar um Pull Request**
- No GitHub, abrir um *Pull Request* para revisão antes de integrar as mudanças na `main`.

## Obs.:
Tem uma janela no vs-code chamada "source control".
Ela pode ser acessada via atalho: "ctrl+shift+g <solta> g <aperta g novamente>".
Por meio dela é possível fazer commits e dar push na sua branch.

La embaixo (barra azul na parte de baixo do vs code) você vê qual branch está.
É possível mudar de branch clicando-se na janela com o nome da sua branch atual.
Além disso, clicando nessa janela você consegue criar novas branchs.

