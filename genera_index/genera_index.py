#!/usr/bin/env python3

#import sys
from csv import reader



def print_header():
    print(f"""<!DOCTYPE html>
    <html lang="en">
    
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Vendemos todo por mudanza</title>
        <link rel="stylesheet" href="style.css" />
      </head>
    
      <body>
    
        <header class="site-header">
          <h1>¡¡¡ Nos mudamos y vendemos TODO !!!</h1>
          <h3><i>Contacto: beranor@gmail.com</i></h3>
        </header>
    
        <ul class="menu">
          <li><a href="#airelibre">Aire Libre</a></li>
          <li><a href="#cocina">Cocina</a></li>
          <li><a href="#hogar">Hogar</a></li>
          <li><a href="#juegos">Juegos</a></li>
          <li><a href="#peluches">Peluches</a></li>
          <li><a href="#libros">Libros</a></li>
          <li><a href="#muebles">Muebles</a></li>
          <li><a href="#rodados">Rodados</a></li>
          <li><a href="#tecnologia">Tecnología</a></li>
        </ul>""")


def print_section(sect):

    csvfile = f"csv/{sect}.csv"
    if sect == 'airelibre':
        title = 'Aire Libre'
    else:
        title = sect.capitalize()

    print(f"""
    <div class="container">
      <h2 id="{sect}" class="heading-text">{title}</h2>
      <ul class="image-gallery">""")

    with open(csvfile, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                img = row[0]
                desc = row[1]
                price = row[2]
                sold = row[3]
                len_sold = len(sold)
                len_img = len(img)
                if img and price and sold != "SI":
                    print_item(img, desc, price)

    print(f"""      </ul>
    </div>
    """)


def print_item(img, desc, price):
    print(f"""
        <li>
          <img src="{img}" alt="">
          <div class="overlay">
            <span>{desc}<br>
            Precio: <b>$ {price}</b></span>
          </div>
        </li>""")


def print_footer():
    print(f"""  </body>
</html>""")




# BEGIN

sections = [ "airelibre", "cocina", "hogar", "juegos", "peluches", "libros", "muebles", "rodados", "tecnologia" ]


print_header()

for section in sections:
    print_section(section)

print_footer()




