from django.db.models.deletion import PROTECT
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.views import*
from django.db import models

# Create your models here.
banco=[
    [0, "BANRURAL"],
    [1, "GYT CONTINENTAL"],
    [2, "BANCO INDUSTRIAL"],
    [3, "INTERBANCO"],
    [4, "BAC CREDOMATIC"],
    [5, "BANCO DE ANTIGUA"],
    [6, "VIVIBANCO"],
]    
class Vendedor(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=75)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    fechaingre = models.DateField()
    telefono = models.CharField(max_length=10)
    porcentaj2 = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.CharField(max_length=20)
    foto = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo
    
class Departamento(models.Model):
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)
    iniciales = models.CharField(max_length=10)
    
    def __str__(self):
        return self.codigo
    
class Rutas(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=15)
    distancia = models.DecimalField(max_digits=11, decimal_places=0)
    depto = models.DecimalField(max_digits=11, decimal_places=0)
    deptodesti = models.DecimalField(max_digits=11, decimal_places=0)
    placa = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre

class Municipios(models.Model):
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    depto = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)
    ruta = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    lugar = models.CharField(max_length=3)
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=70)
    #email = models.CharField(max_length=50)
    #web = models.CharField(max_length=50)
    nit = models.CharField(max_length=15)
    municipio = models.CharField(max_length=50)
    depto = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    #ctacontabl = models.CharField(max_length=15)
    #transporte = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=10)
    #pequenocon = models.BooleanField()
    limitecred = models.DecimalField(max_digits=10, decimal_places=2)
    rutadestin = models.CharField(max_length=30)
    ruta = models.CharField(max_length=30)
    fechacrea = models.DateField()
    observa = models.TextField()
    
    def __str__(self):
        return self.codigo
    
class Pilotos(models.Model):
    ruta = models.CharField(max_length=10)
    descripcio = models.CharField(max_length=75)
    responsabl = models.CharField(max_length=75)
    
    def __str__(self):
        return self.ruta

class Ingreso_guias(models.Model):
    idfactura = models.DecimalField(max_digits=11, decimal_places=0)
    idrecolect = models.DecimalField(max_digits=11, decimal_places=0)
    serie = models.CharField(max_length=10)
    factura = models.DecimalField(max_digits=11, decimal_places=0)
    codigo = models.CharField(max_length=16)
    cotizacion = models.DecimalField(max_digits=11, decimal_places=0)
    formapago = models.CharField(max_length=20)
    cheque = models.DecimalField(max_digits=16, decimal_places=0)
    banco = models.DecimalField(max_digits=5, decimal_places=0)
    fechapago = models.DateField()
    fecha = models.DateField()
    descuento = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    totenvia = models.DecimalField(max_digits=12, decimal_places=2)
    totrecibe = models.DecimalField(max_digits=12, decimal_places=2)
    dereceta = models.BooleanField()
    estado = models.CharField(max_length=1)
    codigoclie = models.DecimalField(max_digits=11, decimal_places=0)
    cliente = models.CharField(max_length=15)
    preciounit = models.DecimalField(max_digits=12, decimal_places=2)
    unidades = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.CharField(max_length=20)
    recibo = models.DecimalField(max_digits=11, decimal_places=0)
    tipofactur = models.CharField(max_length=30)
    diascredit = models.CharField(max_length=10)
    concepto = models.CharField(max_length=200)
    tipoinvent = models.CharField(max_length=30)
    lote = models.DecimalField(max_digits=16, decimal_places=0)
    ruta = models.CharField(max_length=20)
    manifiesto = models.DecimalField(max_digits=16, decimal_places=0)
    destinatar = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    origen = models.CharField(max_length=5)
    destino = models.CharField(max_length=5)
    codedestin = models.DecimalField(max_digits=11, decimal_places=0)
    cerrado = models.BooleanField()
    rutaingres = models.CharField(max_length=30)
    usuario = models.CharField(max_length=15)
    quienrecib = models.CharField(max_length=75)
    dpirecibe = models.CharField(max_length=15)
    fecharecib = models.DateField()
    municipio = models.CharField(max_length=50)
    observa = models.CharField(max_length=250)
    nomenvia = models.CharField(max_length=100)
    direnvia = models.CharField(max_length=100)
    telenvia = models.CharField(max_length=100)
    entraguate = models.BooleanField()
    f1 = models.DateField()
    saleguate = models.BooleanField()
    f2 = models.DateField()
    entradepto = models.BooleanField()
    f3 = models.DateField()
    saledepto = models.BooleanField()
    f4 = models.DateField()
    fasefin = models.BooleanField()
    f5 = models.DateField()
    responsabl = models.CharField(max_length=30)
    rutaresp = models.CharField(max_length=10)
    responsab2 = models.CharField(max_length=30)
    tcontraent = models.DecimalField(max_digits=12, decimal_places=2)
    codeconten = models.CharField(max_length=10)
    
    def __str__(self):
        return self.No_guia
    
class Ingreso_bodega(models.Model):
    bodega=models.CharField(max_length=50, verbose_name="Nombre de Bodega")
    fecha=models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Fecha ingreso Bodega")
    ruta=models.ForeignKey(Rutas, verbose_name="Ruta Entrega", on_delete=models.PROTECT)
    piloto=models.ForeignKey(Pilotos, on_delete=models.PROTECT, verbose_name="Piloto de ruta")
    auxliar=models.CharField(max_length=50, verbose_name="Auxiliar de ruta")
    personalrecibe=models.CharField(max_length=50, verbose_name="Personal Que Recibe")
    noguia= models.CharField(verbose_name="Numero de guia", max_length=6)
    guiamadre=models.IntegerField(verbose_name="Ultima guia madre escaneada")
    guiahija=models.CharField(max_length=50, verbose_name="Ultima guia Hija escaneada")
    piezas = models.IntegerField(verbose_name="Total Piezas")
    guias = models.IntegerField(verbose_name="Total Guias")
    
    def __str__(self):
        return self.bodega
    
class Boletadeposito(models.Model):
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)
    boleta = models.CharField(max_length=15)
    boleta2 = models.CharField(max_length=15)
    boleta3 = models.CharField(max_length=15)
    boleta4 = models.CharField(max_length=15)
    fgenera = models.DateField(verbose_name='Fechar Generada')
    origen = models.CharField(max_length=15)
    destino = models.CharField(max_length=15)
    frecibido = models.DateField(verbose_name='Fecha Ingreso')
    noguias = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Total guias')
    nopiezas = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Total piezas')
    noguiasrec = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Guias recibidas')
    xcobrar = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total por cobrar')
    contado = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total contado')
    credito = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total credito')
    prepago = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total prepago')
    contraentr = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Total contraentrega')
    fdeposito = models.DateField(verbose_name='Fecha depositado')
    banco = models.IntegerField(choices=banco, verbose_name='Banco')
    estatus = models.CharField(max_length=20)
    observa = models.CharField(max_length=250)
    ruta = models.CharField(max_length=15)
    totalbole1 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole2 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole3 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole4 = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.boleta
    
    