from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText
from smtplib import SMTP
from PIL import Image, ImageTk

def calcular_presupuesto():
    
    ancho = ancho_ent.get()
    alto = alto_ent.get()
    hojas = hojas_ent.get()
    vidrio = vidrio_ent.get()

    antiruidos = 4 * hojas * 10.4
    escuadras = 4 * 227
    goma_amortiguadora = 4 * hojas * 6
    ruedas = 2 * hojas * 153
    burlete = (2 * ancho + 2 * alto * hojas) * 89.5
    felpa = (ancho * 4 + (alto * 5 if hojas == 3 else alto * 3 * hojas)) * 44.88
    tornillos = 32 * 8.75
    parker = 4 * hojas * 25.75
    marco = (2 * ancho + 2 * alto) * 0.84 * 4000
    travesano = ancho * 2 * 0.417 * 4000
    central = (alto * (4 if hojas == 3 else hojas)) * 0.419 * 4000
    lateral = (alto * (2 if hojas == 3 else hojas)) * 0.468 * 4000
    
    vidrio_3mm = hojas * alto * 4600 if vidrio == 3 else 0
    vidrio_4mm = hojas * alto * 4800 if vidrio == 4 else 0

    desperdicio = (antiruidos + escuadras + goma_amortiguadora + ruedas + burlete + felpa + tornillos + parker +
                   marco + travesano + central + lateral + vidrio_3mm + vidrio_4mm) * 0.05
    ganancia = (antiruidos + escuadras + goma_amortiguadora + ruedas + burlete + felpa + tornillos + parker +
                marco + travesano + central + lateral + vidrio_3mm + vidrio_4mm + desperdicio) * 0.4
    total = antiruidos + escuadras + goma_amortiguadora + ruedas + burlete + felpa + tornillos + parker + marco + \
            travesano + central + lateral + vidrio_3mm + vidrio_4mm + desperdicio + ganancia

    
    presupuesto = f'''
    NOMBRE: {nombre_entry.get()}
    MAIL: {mail_entry.get()}
    TELEFONO: {telefono_entry.get()}

    MATERIALES        | CANTIDAD | PRECIO VENTA
    ----------------- | -------- | -------------
    Antiruidos        |    4     | ${antiruidos:.2f}
    Escuadras         |    4     | ${escuadras:.2f}
    Parte J           |    4     | ${goma_amortiguadora:.2f}
    Ruedas            |    2     | ${ruedas:.2f}
    Burlete           |    1     | ${burlete:.2f}
    Felpa             |    1     | ${felpa:.2f}
    Tornillos         |    1     | ${tornillos:.2f}
    Parker            |    4     | ${parker:.2f}
    Marco             |    1     | ${marco:.2f}
    Travesaño         |    2     | ${travesano:.2f}
    Central           |    {4 if vidrio == 3 else vidrio}     | ${central:.2f}
    Lateral           |    {2 if vidrio == 3 else vidrio}     | ${lateral:.2f}
    Vidrio            |    {vidrio}     | ${vidrio_3mm if vidrio == 3 else vidrio_4mm:.2f}

    ----------------- | -------- | -------------
    TOTAL             |          | ${total:.2f}
    '''

   
    messagebox.showinfo("Presupuesto", presupuesto)

    enviar_correo(presupuesto)
    
    ventana.mainloop()



def enviar_correo(presupuesto):

    mensaje = (f"Presupuesto\n\n{presupuesto}")
    
    remitente = "UnSoloUso5151@gmail.com"
    destinatario = "UnSoloUso5151@gmail.com"
    
    mensaje_correo = MIMEText(mensaje)
    mensaje_correo["From"] = remitente
    mensaje_correo["To"] = destinatario
    mensaje_correo["Subject"] = "Prueba de envio de mail"
    
    servidor = SMTP("smtp.gmail.com", 587)
    servidor.ehlo()
    servidor.starttls()
    
    servidor.login("UnSoloUso5151@gmail.com", "kjquduioootukkao")
    
    servidor.sendmail(remitente, destinatario, mensaje_correo.as_string())
    
    servidor.quit()


ventana = Tk()
ventana.title("Calculadora de Precios de Ventanas")
ventana.geometry("1000x600")
ventana.resizable(False, False)
ventana.iconbitmap("imagenes/logo.ico")

ancho_ent = DoubleVar(master=ventana,name="anch")
alto_ent = DoubleVar(master=ventana,name="alt")
hojas_ent = IntVar(master=ventana,name="hoj")
vidrio_ent = IntVar(master=ventana,name="vid")

Label(ventana, text="Nombre:").pack()
nombre_entry = Entry(ventana)
nombre_entry.pack()

Label(ventana, text="Mail:").pack()
mail_entry = Entry(ventana)
mail_entry.pack()

Label(ventana, text="Teléfono:").pack()
telefono_entry = Entry(ventana)
telefono_entry.pack()

anch = Label(ventana, text="Ancho de la ventana (metros):").pack()
ancho_entry = Entry(ventana,textvariable=ancho_ent)
ancho_entry.pack()

alt = Label(ventana, text="Alto de la ventana (metros):").pack()
alto_entry = Entry(ventana,textvariable=alto_ent)
alto_entry.pack()

hoj = Label(ventana, text="Cantidad de hojas:").pack()
hojas_entry = Entry(ventana,textvariable=hojas_ent)
hojas_entry.pack()

vid = Label(ventana, text="Vidrio (3mm o 4mm):").pack()
vidrio_entry = Entry(ventana,textvariable=vidrio_ent)
vidrio_entry.pack()

Label(ventana, text="Imagen de referencia: 2 hojas").place(x=0,y=0)
Label(ventana, text="Imagen de referencia: 2 hojas 1 fija").place(x=0,y=100)
Label(ventana, text="Imagen de referencia: 2 cuartos").place(x=0,y=200)
Label(ventana, text="Imagen de referencia: 3 hojas").place(x=0,y=300)
Label(ventana, text="Imagen de referencia: 4 hojas").place(x=0,y=400)

image_1 = Image.open("imagenes/pngwing2h.png")
image_1 = image_1.resize((50, 50))
image_2 = Image.open("imagenes/pngwing2_1.png")
image_2 = image_2.resize((50, 50))
image_3 = Image.open("imagenes/pngwing2c.png")
image_3 = image_3.resize((50, 50))
image_4 = Image.open("imagenes/pngwing3h.png")
image_4 = image_4.resize((50, 50))
image_5 = Image.open("imagenes/pngwing4h.png")
image_5 = image_5.resize((50, 50))

photo_1 = ImageTk.PhotoImage(image_1)
photo_2 = ImageTk.PhotoImage(image_2)
photo_3 = ImageTk.PhotoImage(image_3)
photo_4 = ImageTk.PhotoImage(image_4)
photo_5 = ImageTk.PhotoImage(image_5)

image_label_1 = Label(ventana, image=photo_1)
image_label_1.place(x=50,y=30)
image_label_2 = Label(ventana, image=photo_2)
image_label_2.place(x=50,y=130)
image_label_3 = Label(ventana, image=photo_3)
image_label_3.place(x=50,y=235)
image_label_4 = Label(ventana, image=photo_4)
image_label_4.place(x=50,y=330)
image_label_5 = Label(ventana, image=photo_5)
image_label_5.place(x=50,y=425)

Button(ventana, text="Calcular presupuesto", command=calcular_presupuesto).pack()


ventana.mainloop()
