import datetime
from django import forms
from datetime import datetime

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class ExamenesFilterForm(forms.Form):
    anio_academico = forms.ChoiceField(
        label="Año Académico",
        choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
        required=False,
    )

    propuesta_ids = forms.MultipleChoiceField(
        label="Carreras",
        choices=[
            # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
            ('33', 'Ingeniería Electromecánica'),
            ('28', 'Ingeniería Civil'),
            ('21', 'Ingeniería en Sistemas de Información'),
            ('5', 'Licenciatura en Organización Industrial'),
            # Agrega más carreras según sea necesario
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


class EgresadosFilterForm(forms.Form):
    anio = forms.ChoiceField(
        label="Año",
        choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
        required=False,
    )

    propuesta_ids = forms.MultipleChoiceField(
        label="Carreras",
        choices=[
            # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
            ('33', 'Ingeniería Electromecánica'),
            ('28', 'Ingeniería Civil'),
            ('21', 'Ingeniería en Sistemas de Información'),
            ('5', 'Licenciatura en Organización Industrial'),
            # Agrega más carreras según sea necesario
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


class CursadasFilterForm(forms.Form):
            anio = forms.ChoiceField(
            label="Año",
            choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
            required=False,
         )

            propuesta_ids = forms.MultipleChoiceField(
            label="Carreras",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('33', 'Ingeniería Electromecánica'),
                ('28', 'Ingeniería Civil'),
                ('21', 'Ingeniería en Sistemas de Información'),
                ('5', 'Licenciatura en Organización Industrial'),
                # Agrega más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
    )

class ResultadoCursaFilterForm(forms.Form):
            anio = forms.ChoiceField(
            label="Año",
            choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
            required=False,
         )

            propuesta_ids = forms.MultipleChoiceField(
            label="Carreras",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('33', 'Ingeniería Electromecánica'),
                ('28', 'Ingeniería Civil'),
                ('21', 'Ingeniería en Sistemas de Información'),
                ('5', 'Licenciatura en Organización Industrial'),
                ('31', 'Tecnicatura Univ. en Adm.y Gestión en Inst.de Educación Sup.'),
                ('32', 'Tecnicatura Univ. en Higiene y Seguridad en el Trabajo'),
                ('12', 'Tecnicatura Univ. en Procedimientos y Tecnolog. Ambientales'),
                ('2', 'Tecnicatura Universitaria en Administración'),
                ('1', 'Tecnicatura Universitaria en Bromatología y Medio Ambiente'),
                ('3', 'Tecnicatura Universitaria en Diseño Industrial'),
                ('8', 'Tecnicatura Universitaria en Mantenimiento Industrial'),
                ('9', 'Tecnicatura Universitaria en Mecatrónica'),
                ('7', 'Tecnicatura Universitaria en Programación'),
                ('40', 'Tecnicatura Universitaria en Programación (EaD)'),
                # Agrega más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
    )

class IngresantesFilterForm(forms.Form):
            anio = forms.ChoiceField(
            label="Año",
            choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
            required=False,
         )

            propuesta_ids = forms.MultipleChoiceField(
            label="Carreras",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('33', 'Ingeniería Electromecánica'),
                ('28', 'Ingeniería Civil'),
                ('21', 'Ingeniería en Sistemas de Información'),
                ('5',  'Licenciatura en Organización Industrial'),
                # Agregar más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
    )

class DocentesFilterForm(forms.Form):
            anio = forms.ChoiceField(
            label="Año",
            choices=[('', '------')] + [(str(year), str(year)) for year in range(2025, 2014,-1)], # Añade opción vacía
            required=False,
         )

            propuesta_ids = forms.MultipleChoiceField(
            label="Carreras",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('33', 'Ingeniería Electromecánica'),
                ('28', 'Ingeniería Civil'),
                ('21', 'Ingeniería en Sistemas de Información'),
                ('5', 'Licenciatura en Organización Industrial'),
                # Agrega más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
        )
            dptos_ids = forms.MultipleChoiceField(
            label="Dptos",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('2', 'Ingenieria Civil'),
                ('3', 'Ingenieria Electromecanica'),
                ('6', 'Licenciatura en Organizacion Industrial'),
                ('8', 'Ingenieria en Sistemas de Informacion'),
                ('10', 'Materias Basicas'),
                # Agrega más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
        )

class EgresadosxAnioFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # ¡IMPORTANTE: llamar al __init__ del padre primero!

        current_year = datetime.now().year
        # Año de inicio del rango (ej. si current_year es 2025, entonces 2025 - 19 = 2006)
        start_year_for_range = current_year - 19
        # Año de fin del rango (ej. si current_year es 2025, entonces 2025 - 4 = 2021)
        end_year_for_range = current_year - 4

        # Generar las opciones en orden descendente (del más reciente al más antiguo)
        # range(inicio_inclusivo, fin_exclusivo, paso)
        # Queremos del 2021 (end_year_for_range) hasta el 2006 (start_year_for_range)
        # Por eso el fin es (start_year_for_range - 1)
        year_choices = [(str(year), str(year)) for year in range(end_year_for_range, start_year_for_range - 1, -1)]

        # Añadir la opción vacía al principio
        self.fields['anio'] = forms.ChoiceField(
            label="Año",
            choices=[('', '------')] + year_choices,
            required=False,
        )

    propuesta_ids = forms.MultipleChoiceField(
            label="Carreras",
                choices=[
                # No hay opción vacía para MultipleChoiceField, ya que no se selecciona nada por defecto
                ('33', 'Ingeniería Electromecánica'),
                ('28', 'Ingeniería Civil'),
                ('21', 'Ingeniería en Sistemas de Información'),
                ('5', 'Licenciatura en Organización Industrial'),
                ('31', 'Tecnicatura Univ. en Adm.y Gestión en Inst.de Educación Sup.'),
                ('32', 'Tecnicatura Univ. en Higiene y Seguridad en el Trabajo'),
                ('12', 'Tecnicatura Univ. en Procedimientos y Tecnolog. Ambientales'),
                ('2', 'Tecnicatura Universitaria en Administración'),
                ('1', 'Tecnicatura Universitaria en Bromatología y Medio Ambiente'),
                ('3', 'Tecnicatura Universitaria en Diseño Industrial'),
                ('8', 'Tecnicatura Universitaria en Mantenimiento Industrial'),
                ('9', 'Tecnicatura Universitaria en Mecatrónica'),
                ('7', 'Tecnicatura Universitaria en Programación'),
                ('40', 'Tecnicatura Universitaria en Programación (EaD)'),
                # Agrega más carreras según sea necesario
                ],
                required=False,
            widget=forms.CheckboxSelectMultiple
    )