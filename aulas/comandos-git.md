# Git — Guia Rápido

## Verificar o estado do projeto

Mostra arquivos modificados, não rastreados e a branch atual.

```bash
git status
````

---

## Ver quais branches existem

```bash
git branch
```

Ver também as branches remotas:

```bash
git branch -a
```

---

## Baixar atualizações do GitHub

Se você **não tem alterações locais**:

```bash
git pull origin main
```

ou

```bash
git pull origin master
```

dependendo do nome da branch principal.

---

## Salvar alterações temporariamente (stash)

Guardar modificações sem criar commit:

```bash
git stash
```

Listar stashes salvos:

```bash
git stash list
```

Restaurar o último stash:

```bash
git stash pop
```

Fluxo comum para atualizar o projeto sem perder trabalho:

```bash
git stash
git pull origin main
git stash pop
```

---

## Salvar alterações definitivamente (commit)

Adicionar todos os arquivos modificados:

```bash
git add .
```

Criar um commit:

```bash
git commit -m "Descrição das alterações"
```

---

## Enviar alterações para o GitHub

```bash
git push origin main
```

ou

```bash
git push origin master
```

---

## Fluxo mais comum do dia a dia

```bash
git status
git add .
git commit -m "Implementa nova funcionalidade"
git push origin main
```

---

## Clonar um repositório

```bash
git clone URL_DO_REPOSITORIO
```

Exemplo:

```bash
git clone https://github.com/usuario/projeto.git
```

---

## Trocar de branch

```bash
git checkout nome-da-branch
```

ou (mais recente):

```bash
git switch nome-da-branch
```

---

## Criar uma nova branch

```bash
git checkout -b nova-branch
```

ou

```bash
git switch -c nova-branch
```

---

## Ver histórico de commits

```bash
git log
```

Versão resumida:

```bash
git log --oneline
```

---

## Descartar alterações locais

Descartar mudanças em arquivos rastreados:

```bash
git restore .
```

---

## Forçar o projeto local a ficar igual ao GitHub

 Apaga todas as alterações locais não salvas.

```bash
git fetch origin
git reset --hard origin/main
```

---

## Configuração inicial (uma única vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Ver configurações:

```bash
git config --list
```

