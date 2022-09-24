def multiply(a: float, b:float) -> dict:
    resultado = a*b
    response = {'resultado': resultado,
                'operador 1': a,
                'operador 2': b}

    return response

def divide(a: float, b: float, resto: bool) -> dict:
    if resto is True:
        resultado =  a%b
    if resto is False:
        resultado = a/b    
    response = {'resultado': resultado,
                'divisão com resto?': resto,
                'operador 1': a,
                'operador 2': b}

    return response

def sum(a: float, b:float) -> dict:
    resultado = a+b
    response = {'resultado': resultado,
                'operador 1': a,
                'operador 2': b}

    return response

def subtract(a: float, b:float) -> dict:
    resultado = a-b
    response = {'resultado': resultado,
                'operador 1': a,
                'operador 2': b}

    return response
