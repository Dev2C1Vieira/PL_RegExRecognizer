# Comando padrão quando apenas "make" é executado
.DEFAULT_GOAL := reconhecer_palavra

# Comando para reconhecer uma palavra
reconhecer_palavra:
	python leitura_automato.py afd.json
	python geracao_grafo.py afd.json

# python reconhecimento_palavra.py

# Comando para limpar arquivos gerados
clean:
	rm -f automato.png