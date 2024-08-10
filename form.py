from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import countries

countries_list = countries.countries_list

class FormSubscribe(FlaskForm):
    zoom_string = "Ao vivo pelo Zoom"
    schadule_date="Brevemente a anunciar"
    schadule_time="Das 20h as 22h (Lisboa)"
    
    
    full_name = StringField(
        'Full Name', 
        validators=[DataRequired()], 
        render_kw={
            "nome":"full_name",   
            "placeholder": "Nome completo", 
            'class':'form-control'
            }
        )
    countries = SelectField(
        'Countries', choices=[(country, f"{country} ({code})") for country, code in countries_list.items()], 
        validators=[DataRequired()], 
        render_kw={
            "nome": "countries", 
            "placeholder": "Selecione o país", 
            'class':'form-control'
            }
        )
    wtsapp = StringField(
        'WhatsApp', 
        validators=[DataRequired()], 
        render_kw={
            "nome": "wtsapp",
            "placeholder": "WhatsApp", 
            'class':'form-control'
            }
        )
    submit = SubmitField(
        'Inscreve-te já',
        render_kw={
            'class':'btn btn_firs_form btn-success'
            }
        )
