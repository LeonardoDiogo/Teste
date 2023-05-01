distancia_rp_franca = 100  # km
velocidade_carro = 110  # km/h
velocidade_caminhao = 80  # km/h
tempo_pedagio = 5 / 60  # 5 minutos em horas

tempo_carro = distancia_rp_franca / velocidade_carro
tempo_caminhao = (distancia_rp_franca /
                  velocidade_caminhao) + 2 * tempo_pedagio

x = (velocidade_carro * tempo_caminhao * distancia_rp_franca) / \
    (velocidade_carro + velocidade_caminhao)

distancia_carro_rp = distancia_rp_franca - x
distancia_caminhao_rp = x

if distancia_caminhao_rp < distancia_carro_rp:
    print("O caminhão está mais próximo de Ribeirão Preto")
else:
    print("O carro está mais próximo de Ribeirão Preto")
