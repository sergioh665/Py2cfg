from py2cfg import CFGBuilder # type: ignore

# Construa o CFG a partir do arquivo Python de teste
cfg = CFGBuilder().build_from_file('arquivo', 'fib.py')

# Gere a visualização do CFG e salve como SVG
cfg.build_visual('arquivo-fib', 'svg')