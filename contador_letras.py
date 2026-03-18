def main():
    print("--- 📝 Contador de Letras ---")
    
    # Solicitamos el nombre al usuario
    nombre = input("Por favor, ingresa tu nombre: ").strip()
    
    if not nombre:
        print("⚠️ ¡Vaya! Parece que no ingresaste nada.")
        return

    # Calculamos la longitud (podemos usar len(nombre) para todo el texto, 
    # o nombre.replace(' ', '') para contar solo las letras reales)
    numero_letras = len(nombre.replace(" ", ""))
    
    print(f"\n✨ ¡Hola, {nombre}!")
    print(f"📊 Tu nombre tiene un total de {numero_letras} letras (sin contar espacios).")
    print("¡Que tengas un excelente día! 🚀")

if __name__ == "__main__":
    main()
