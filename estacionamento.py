
print(''' ____________________________
         | Estacionamento Do Tio Chico|
         |____________________________|
''')
numerodevagas = int(input("Número de vagas: "))
clientesesperados= int(input("Número de clientes: "))
    
carros = []
for _ in range(clientesesperados):
    vaga = int(input("Vaga a ser ocupada: "))
    if vaga not in carros:
        carros.append(vaga)
    
    atendidos = len(carros)
    print(f"Clientes atendidos: {atendidos}")



