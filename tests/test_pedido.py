import pytest
from src.pedido import calcular_total_pedido


# =========================================================
# TESTE 1 - SUCESSO
# =========================================================

# Nome descritivo:
# Deve calcular corretamente o total do pedido quando
# o valor mínimo for atingido

# Cenário testado:
# Verifica se a função retorna corretamente a soma
# dos itens quando o valor mínimo é respeitado.

# Dados de entrada:
# itens = [{"preco": 10}, {"preco": 20}]
# valor_minimo = 15

# Resultado esperado:
# Retornar 30


def test_deve_calcular_total_quando_valor_minimo_atingido():

    # Arrange
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15

    # Act
    resultado = calcular_total_pedido(itens, valor_minimo)

    # Assert
    assert resultado == 30


# =========================================================
# TESTE 2 - SUCESSO
# =========================================================

# Nome descritivo:
# Deve aceitar pedido quando total for igual ao valor mínimo

# Cenário testado:
# Verifica se pedidos exatamente no valor mínimo
# são considerados válidos.

# Dados de entrada:
# itens = [{"preco": 25}]
# valor_minimo = 25

# Resultado esperado:
# Retornar 25


def test_deve_aceitar_pedido_com_valor_igual_ao_minimo():

    # Arrange
    itens = [{"preco": 25}]
    valor_minimo = 25

    # Act
    resultado = calcular_total_pedido(itens, valor_minimo)

    # Assert
    assert resultado == 25


# =========================================================
# TESTE 3 - ERRO
# =========================================================

# Nome descritivo:
# Deve gerar erro quando pedido não atingir valor mínimo

# Cenário testado:
# Verifica se a função impede pedidos abaixo do valor mínimo.

# Dados de entrada:
# itens = [{"preco": 5}, {"preco": 5}]
# valor_minimo = 20

# Resultado esperado:
# Gerar ValueError


def test_deve_gerar_erro_quando_valor_minimo_nao_atingido():

    # Arrange
    itens = [{"preco": 5}, {"preco": 5}]
    valor_minimo = 20

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)