#Notificador del clima

ciudad = input("Introduce la ciudad:")
temperatura = int(input("Introduce la temperatura registrada en el termómetro: "))
print("Consultando el estado del clima en", ciudad)
    


if temperatura > 30:
    print("En", ciudad, "hace mucho calor")
elif temperatura > 20:
    print("En", ciudad, "hace un clima agradable")
else:
    print("En", ciudad, "hace frío")
    