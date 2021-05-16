import numpy as np

def quantize(x, n, form): # função para realizar a quantização
    X = x.reshape((-1,1))

    N = 2**n # quantidade de níveis de quantização
    A = 1.0 # valor de pico do intervalo de medição
    R = 2*A/N # resolução do quantizador

    if form == 'midrise':
        S = np.linspace(-A + R/2, A - R/2, N) # níveis de quantização mid-rise
    elif form == 'midtread':
        S = np.linspace(-A, A-R, N) # níveis de quantização mid-tread
    else:
        raise ValueError("Digite midrise ou midtread")

    dists = abs(X-S)
    nearestIndex = dists.argmin(axis=1)
    quantized = S.flat[nearestIndex]
    return  quantized.reshape(x.shape)