def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Solicitar a entrada do usuário
consumo_mensal = float(input("Digite seu consumo médio mensal de dados em GB: "))
plano_recomendado = recomendar_plano(consumo_mensal)

# Exibir o plano recomendado
print(plano_recomendado)