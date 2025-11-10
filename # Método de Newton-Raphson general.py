# Método de Newton-Raphson general
# Autor: Luis Enrique Lira Aguila, Juan Gerardo Lara Leos 
# Este programa permite ingresar cualquier ecuación f(x)=0 sin modificar el código

import sympy as sp

# ⿡ Definir la variable simbólica
x = sp.Symbol('x')

# ⿢ Ingresar la ecuación como texto
ecuacion = input("Ingresa la función f(x) = ")
f = sp.sympify(ecuacion)  # Convierte el texto a expresión simbólica

# ⿣ Derivar automáticamente
f_prime = sp.diff(f, x)

# ⿤ Pedir parámetros numéricos
x0 = float(input("Ingresa el valor inicial x0: "))
tolerancia = float(input("Ingresa la tolerancia (ej. 0.0001): "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

# ⿥ Convertir las funciones simbólicas a funciones numéricas
f_eval = sp.lambdify(x, f, "math")
f_prime_eval = sp.lambdify(x, f_prime, "math")

# ⿦ Iterar el método
print("\nIter\t x_n\t\t f(x_n)\t\t Error")
for i in range(max_iter):
    fx = f_eval(x0)
    fpx = f_prime_eval(x0)

    if fpx == 0:
        print("❌ Error: la derivada es cero. No se puede continuar.")
        break

    x1 = x0 - fx / fpx
    error = abs(x1 - x0)

    print(f"{i+1}\t {x1:.6f}\t {fx:.6f}\t {error:.6f}")

    if error < tolerancia:
        print("\n✅ Raíz aproximada encontrada:")
        print(f"x ≈ {x1:.6f}")
        break

    x0 = x1
else:
    print("\n⚠ No se alcanzó la convergencia después de las iteraciones dadas.")