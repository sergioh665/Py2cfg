
# Preparação do ambiente...  

## Na sua máquina: 

# Instalando WSL
```bash
wsl --install SE DER ERRO, TENTE => wsl --install -d Ubuntu
```

# Atualizar listas de pacotes

```bash
sudo apt update
```
# Instalar pacotes e ferramentas

```bash
sudo apt install python3 python3-pip python3-venv graphviz
```
# Mudar para diretório de destino

```bash
cd /mnt/c/Users/seu_usuario/Desktop/pasta_destino
```

# Criar ambiente virtual

```bash
python3 -m venv venv
```

# Ativar ambiente virtual

```bash
source venv/bin/activate
```

# Instalar pacotes

```bash
pip install graphviz py2cfg
```


## Código para criar .svg

```bash
from py2cfg import CFGBuilder 
# Construa o CFG a partir do arquivo Python de teste
cfg = CFGBuilder().build_from_file('arquivo', 'seu_arquivo.py')
# Gere a visualização do CFG e salve como SVG
cfg.build_visual('arquivo-fib', 'svg')
```
