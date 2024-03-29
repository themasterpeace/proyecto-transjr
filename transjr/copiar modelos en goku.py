# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bodega(models.Model):
    fecha = models.DateField()
    destinatar = models.CharField(max_length=60)
    factura = models.DecimalField(max_digits=11, decimal_places=0)
    formapago = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    totenvia = models.DecimalField(max_digits=12, decimal_places=2)
    totrecibe = models.DecimalField(max_digits=12, decimal_places=2)
    codigoclie = models.DecimalField(max_digits=11, decimal_places=0)
    preciounit = models.DecimalField(max_digits=12, decimal_places=2)
    unidades = models.DecimalField(max_digits=10, decimal_places=2)
    ruta = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bodega'


class Boletadeposito(models.Model):
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)
    boleta = models.CharField(max_length=15)
    boleta2 = models.CharField(max_length=15)
    boleta3 = models.CharField(max_length=15)
    boleta4 = models.CharField(max_length=15)
    fgenera = models.DateField()
    origen = models.CharField(max_length=15)
    destino = models.CharField(max_length=15)
    frecibido = models.DateField()
    noguias = models.DecimalField(max_digits=11, decimal_places=0)
    nopiezas = models.DecimalField(max_digits=11, decimal_places=0)
    noguiasrec = models.DecimalField(max_digits=11, decimal_places=0)
    xcobrar = models.DecimalField(max_digits=12, decimal_places=2)
    contado = models.DecimalField(max_digits=12, decimal_places=2)
    credito = models.DecimalField(max_digits=12, decimal_places=2)
    prepago = models.DecimalField(max_digits=12, decimal_places=2)
    contraentr = models.DecimalField(max_digits=12, decimal_places=2)
    fdeposito = models.DateField()
    banco = models.CharField(max_length=20)
    estatus = models.CharField(max_length=20)
    observa = models.CharField(max_length=250)
    ruta = models.CharField(max_length=15)
    totalbole1 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole2 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole3 = models.DecimalField(max_digits=12, decimal_places=2)
    totalbole4 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'boletadeposito'


class Cargacamiones(models.Model):
    escaneo = models.CharField(max_length=11)
    guiamadre = models.CharField(max_length=11)
    guiahijade = models.CharField(max_length=11)
    guiahijaca = models.CharField(max_length=11)
    totalunida = models.DecimalField(max_digits=11, decimal_places=0)
    estado = models.CharField(max_length=1)
    fecha = models.DateField()
    depto = models.CharField(max_length=20)
    rutadestin = models.CharField(max_length=30)
    responsabl = models.CharField(max_length=30)
    placa = models.CharField(max_length=10)
    recibe = models.CharField(max_length=50)
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)
    hora = models.CharField(max_length=5)
    observa = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cargacamiones'


class Clasificaproducto(models.Model):
    idclasi = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clasificaproducto'


class Clientes(models.Model):
    lugar = models.CharField(max_length=3)
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    nit = models.CharField(max_length=15)
    municipio = models.CharField(max_length=50)
    depto = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    ctacontabl = models.CharField(max_length=15)
    transporte = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=10)
    pequenocon = models.BooleanField()
    limitecred = models.DecimalField(max_digits=10, decimal_places=2)
    observa = models.TextField()
    rutadestin = models.CharField(max_length=30)
    ruta = models.CharField(max_length=30)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'clientes'


class Deptos(models.Model):
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)
    iniciales = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'deptos'


class Deptosasignadospilotos(models.Model):
    piloto = models.CharField(max_length=10)
    depto = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'deptosasignadospilotos'


class Descargacamiones(models.Model):
    escaneo = models.CharField(max_length=11)
    guiamadre = models.CharField(max_length=11)
    totalunida = models.CharField(max_length=11)
    fecha = models.DateField()
    rutaingres = models.CharField(max_length=30)
    responsabl = models.CharField(max_length=30)
    placa = models.CharField(max_length=10)
    depto = models.CharField(max_length=30)
    horaini = models.CharField(max_length=5)
    horafin = models.CharField(max_length=5)
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'descargacamiones'


class Destino(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'destino'


class Envios(models.Model):
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

    class Meta:
        managed = False
        db_table = 'envios'


class Envioshistorico(models.Model):
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

    class Meta:
        managed = False
        db_table = 'envioshistorico'


class Formapago(models.Model):
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)
    efectivo = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'formapago'


class Lugarcodigos(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'lugarcodigos'


class Manifiesto(models.Model):
    id = models.DecimalField(max_digits=11, decimal_places=0)
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)
    detalle = models.CharField(max_length=60)
    fsalida = models.DateField()
    fretorna = models.DateField()
    envio = models.DecimalField(max_digits=11, decimal_places=0)
    entregado = models.CharField(max_length=2)
    kmini = models.DecimalField(max_digits=10, decimal_places=2)
    kmfin = models.DecimalField(max_digits=10, decimal_places=2)
    consumogas = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    contado = models.DecimalField(max_digits=12, decimal_places=2)
    porcobrar = models.DecimalField(max_digits=12, decimal_places=2)
    credito = models.DecimalField(max_digits=12, decimal_places=2)
    prepago = models.DecimalField(max_digits=12, decimal_places=2)
    cerrado = models.BooleanField()
    totenvia = models.DecimalField(max_digits=12, decimal_places=2)
    totrecibe = models.DecimalField(max_digits=12, decimal_places=2)
    ruta = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'manifiesto'


class Manifiestohistorico(models.Model):
    id = models.DecimalField(max_digits=11, decimal_places=0)
    manifiesto = models.DecimalField(max_digits=11, decimal_places=0)
    detalle = models.CharField(max_length=60)
    fsalida = models.DateField()
    fretorna = models.DateField()
    envio = models.DecimalField(max_digits=11, decimal_places=0)
    entregado = models.CharField(max_length=2)
    kmini = models.DecimalField(max_digits=10, decimal_places=2)
    kmfin = models.DecimalField(max_digits=10, decimal_places=2)
    consumogas = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    contado = models.DecimalField(max_digits=12, decimal_places=2)
    porcobrar = models.DecimalField(max_digits=12, decimal_places=2)
    credito = models.DecimalField(max_digits=12, decimal_places=2)
    prepago = models.DecimalField(max_digits=12, decimal_places=2)
    cerrado = models.BooleanField()
    totenvia = models.DecimalField(max_digits=12, decimal_places=2)
    totrecibe = models.DecimalField(max_digits=12, decimal_places=2)
    ruta = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'manifiestohistorico'


class Municipio(models.Model):
    codigo = models.DecimalField(max_digits=11, decimal_places=0)
    depto = models.DecimalField(max_digits=11, decimal_places=0)
    nombre = models.CharField(max_length=50)
    ruta = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'municipio'


class Origen(models.Model):
    ruta = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'origen'


class Origenes(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'origenes'


class Producto(models.Model):
    codigo2 = models.CharField(max_length=30)
    descripcio = models.CharField(max_length=75)
    mutilidad = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.DecimalField(max_digits=10, decimal_places=2)
    costunidad = models.DecimalField(max_digits=10, decimal_places=2)
    costototal = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.DecimalField(max_digits=16, decimal_places=0)
    umedida = models.DecimalField(max_digits=11, decimal_places=0)
    proveedor = models.DecimalField(max_digits=11, decimal_places=0)
    gadmon = models.DecimalField(max_digits=10, decimal_places=2)
    clasifica = models.CharField(max_length=40)
    imagen = models.CharField(max_length=200)
    ctacontabl = models.CharField(max_length=15)
    grupo = models.CharField(max_length=3)
    tipoinvent = models.CharField(max_length=20)
    ml = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'producto'


class Productoclientesespeciales(models.Model):
    lugar = models.CharField(max_length=10)
    cliente = models.DecimalField(max_digits=11, decimal_places=0)
    producto = models.CharField(max_length=15)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'productoclientesespeciales'


class Responsables(models.Model):
    ruta = models.CharField(max_length=10)
    descripcio = models.CharField(max_length=75)
    responsabl = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'responsables'


class Rutas(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=15)
    distancia = models.DecimalField(max_digits=11, decimal_places=0)
    depto = models.DecimalField(max_digits=11, decimal_places=0)
    deptodesti = models.DecimalField(max_digits=11, decimal_places=0)
    placa = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'rutas'


class Vendedores(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=75)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    fechaingre = models.DateField()
    telefono = models.CharField(max_length=10)
    porcentaj2 = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.CharField(max_length=20)
    foto = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vendedores'
