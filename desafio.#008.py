"""escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros."""
                           #     km hm dam m dm cm mm
medida = float(input("uma distancia em metro "))
cm = medida * 100
mm = medida * 1000
dam = medida * 10
hm = medida * 100
km = medida * 1000
print(f'A medida {medida}m a {cm:.0f}cm e {mm:.0f}mm  \n medida do {dam}dm e o {hm}hm e o {km}km')
