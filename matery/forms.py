from django import forms

from matery.models import matery

class FormMatery(forms.ModelForm):

	class Meta:
		model = matery

		fields = [
			'user',
			'Nombre',
			'Orientacion1',
			'Orientacion2',
			'Orientacion3',
			'Orientacion4',
			'Orientacion5',
			'Espacial1',
			'Espacial2',
			'Espacial3',
			'Espacial4',
			'Espacial5',
			'fijacion',
			'calculo',
			'recuerdo',
			'lenguaje1',
			'lenguaje2',
			'lenguaje3',
			'lenguaje4',
			'lenguaje5',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Nombre': 'Nombre de la materia',
			'Matematicas1': '¿Que son los números naturales?',
			'Matematicas2': '¿Que son los números enteros?',
			'Matematicas3': '√432',
			'Matematicas4': '2918838/897',
			'Matematicas5': '(45/26)*(39/25)*(22/33)',
			'Matematicas6': 'x-(2x+1)=8-(3x+3)',
			'Matematicas7': '(5-3x)-(-4x+6)=(8x+11)-(3x-6)',
			'Matematicas8': 'La suma de 2 numeros es 9 y la suma de sus cuadrados 53 hallar los números',
			'Matematicas9': 'A tiene 3 años mas que B y el cuadrado de la edad de A aumentada en el cuadrado de la edad de B equivale a 317 años Hallar ambbas edades ',
			'Matematicas10': 'Un vaso tiene agua se coloca un objeto y la altura sube 10 cm si el radio del vaso es de 5 cm ¿Cual es el volumen del objeto?',
			'fijacion': 'Nombre tres palabras Peseta-Caballo-Manzana (o Balón- Bandera-Arbol) a razón de 1 por segundo. Luego se pide al paciente que las repita. Esta primera repetición otorga la puntuación. Otorgue 1 punto por cada palabra correcta, pero continúe diciéndolas hasta que el sujeto repita las 3, hasta un máximo de 6 veces',
			'calculo': '¿Si tiene 30 pesetas y me va dando de tres en tres, ¿Cuántasle van quedando?. Detenga la prueba tras 5 sustraciones. Si el sujeto no puede realizar esta prueba, pídale que deletree la palabra MUNDO al revés.? ',
			'recuerdo': 'Preguntar por las tres palabras mencionadas anteriormente',
			'Matematicas14': 'DENOMINACIÓN. \n Mostrarle un lápiz o un bolígrafo y preguntar ¿qué es esto?. Hacer lo mismo con un reloj de pulsera',
			'Matematicas15': 'REPETICIÓN. Pedirle que repita la frase: "ni sí, ni no, ni pero" (o “En un trigal había 5 perros”)',
			'Matematicas16': 'ÓRDENES. Pedirle que siga la orden: "coja un papel con la mano derecha, dóblelo por la mitad, y póngalo en el suelo"',
			'Matematicas17': 'Coje con mano d. 0-1 dobla por mitad 0-1 pone en suelo 0-1 .LECTURA. Escriba legiblemente en un papel "Cierre los ojos". Pídale que lo lea y haga lo que dice la frase ', 
			'Matematicas18': 'ESCRITURA. Que escriba una frase (con sujeto y predicado)',
			
		}
		widgets = {
			'Nombbre': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion1': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion2': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion3': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion4': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion5': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial1': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial2': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial3': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial4': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial5': forms.TextInput(attrs={'class':'form-control'}),
			'fijacion': forms.TextInput(attrs={'class':'form-control'}),
			'calculo': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje1': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje2': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje3': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje4': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje5': forms.TextInput(attrs={'class':'form-control'}),
			
		}