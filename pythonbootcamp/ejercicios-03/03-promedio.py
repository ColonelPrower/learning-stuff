"""
Calcular promedio
"""

def promedio(*nums):
    resultado = 0
    if not nums:
        return 0
    
    for n in nums:
        resultado += n
    print(f"el promedio es: {resultado/len(nums)}")
    # return sum(nums)/len(nums) solucion mamona

promedio(1,2,3,4,5)
promedio()
promedio(10,10,5,8,7,9,5)
