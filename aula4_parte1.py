# ----------- Funções em Python -----------
# Funções ajudam a:
# 1. Tornar o código mais organizado e limpo
# 2. Reaproveitar trechos de código
# 3. Executar ações somente quando necessário

def boas_vindas(usuario):
    """Exibe mensagem de boas-vindas para o usuário logado."""
    print(f"Seja bem-vindo {usuario}, tenha um excelente dia!!!")

def pague_pessoas():
    """Exibe mensagem alertando sobre pagamentos pendentes."""
    print("Pague as pessoas!!!")

def dados_invalidos():
    """Exibe mensagem para login inválido."""
    print("Dados inconsistentes, tente novamente!!!")

# Solicitando credenciais do usuário
login = input("Digite o seu e-mail: ")

try:
    senha = int(input("Digite a sua senha: "))
except ValueError:
    print("Erro: A senha deve ser um número inteiro.")
    senha = None  # Definir como None para evitar verificação incorreta

# Verificando credenciais apenas se a senha foi inserida corretamente
if senha is not None:
    if login == "joaodascouves@gmail.com" and senha == 123:
        boas_vindas(login)
    elif login == "fernandadopix@gmail.com" and senha == 321:
        pague_pessoas()
    else:
        dados_invalidos()

# ----------- Conversão de Tipos em Python -----------

# Tuplas são imutáveis, mas podemos convertê-las para listas, modificar os dados e converter de volta.

dados_sigilosos = ("João",)  # Tupla com um único elemento precisa da vírgula

def conversao_list(dados):
    """Converte uma tupla para lista para permitir modificações."""
    return list(dados)

# Convertendo tupla para lista
dados_sigilosos = conversao_list(dados_sigilosos)

# Adicionando novo dado
dados_sigilosos.append("João das Couves")

def conversao_tuple(dados):
    """Converte uma lista de volta para tupla."""
    return tuple(dados)

# Convertendo lista para tupla novamente
dados_sigilosos = conversao_tuple(dados_sigilosos)

# Exibindo dados sigilosos (agora uma tupla novamente)
print("\nDados sigilosos:", dados_sigilosos)

# ----------- Dicionários em Python -----------

# Dicionário armazena dados organizados como chave:valor
nomes_clientes = {
    'cliente_rj': 'Ruan',
    'cliente_sp': "Maria Eduarda",
    'cliente_am': 'Ítalo',
    'cliente_rs': 'Amandah',
    'cliente_ac': 'Felipe',
    'cliente_pe': 'Alexandre',
    'cliente_ce': ["Agleice"],  # Lista para permitir múltiplos nomes
    'cliente_ma': 'Luan',
    'cliente_pi': 'Luciana',
    'cliente_mg': 'Mônica'
}

# Adicionando um novo nome ao cliente do Ceará
nomes_clientes['cliente_ce'].append("Enzo")

# Exibindo dicionário atualizado
print("\nLista de clientes atualizada:")
print(nomes_clientes)

# Adicionando um novo cliente
nomes_clientes.update({'cliente_df': 'Lucas'})

# Exibir dicionário atualizado novamente
print("\nLista de clientes com nova adição:")
print(nomes_clientes)

# Exibir apenas os valores (nomes dos clientes)
print("\nLista de clientes por estado:")
for clientes in nomes_clientes.values():
    print(clientes)
