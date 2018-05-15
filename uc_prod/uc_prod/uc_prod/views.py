"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from uc_prod import app

import urllib   
import re


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/news.md")
    html=responce.read().decode('utf-8')
    html=str.split(html,"\n")
    #list=[]
    #for x in html:
    #    zz=re.sub("(^[0-9].+?\s)",r"<b>\1</b>  ",x)
    #    list.append(zz);
    #for li in zz:
    #    print(li)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        list=html
    )

@app.route('/news')
def news():
    """Renders the contact page."""
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/news.md")
    html=responce.read().decode('utf-8')
    html=str.split(html,"\n")
    return render_template(
        'news.html',
        title='Новости',
        year=datetime.now().year,
        message='Информация о выпуске новой продукции и обновлениях продуктов.',
        html=html
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contacts.html',
        title='Контакты',
        year=datetime.now().year,
        message='Информация о контактах.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/gsm_module')


def gsm_module():
    """Renders the gsm module page."""
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D1%81%D0%B1%D0%BE%D1%80%D0%B0-%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%87%D0%B8-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8-%D0%BF%D0%BE-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%83-gsm.md")
    html=responce.read().decode('utf-8')
    sstr="](http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/";
    replaced = re.sub(r'\]\(/', sstr, html)
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%9F%D1%80%D0%BE%D1%88%D0%B8%D0%B2%D0%BA%D0%B0-GSM-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8F.md")
    html1=responce.read().decode('utf-8')
    replaced1 = re.sub(r'\]\(/', sstr, html1)
    return render_template(
        'products/gsm-module.html',
        title='Модуль сбора и передачи информации по каналу GSM',
        year=datetime.now().year,
        page=replaced,
        page1=replaced1
        #message='Your application description page.'
    )

@app.route('/usi')

def usi_module():
    """Renders the usi module page."""
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%A3%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8-%D1%81%D0%B1%D0%BE%D1%80%D0%B0-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8-%D0%A3%D0%A3%D0%A1%D0%98-16.md")
    html=responce.read().decode('utf-8')
    sstr="](http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/";
    replaced = re.sub(r'\]\(/', sstr, html)
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%9F%D1%80%D0%BE%D1%88%D0%B8%D0%B2%D0%BA%D0%B0-%D0%A3%D0%A3%D0%A1%D0%98-16.md")
    html1=responce.read().decode('utf-8')
    replaced1 = re.sub(r'\]\(/', sstr, html1)
    return render_template(
        'products/usi.html',
        title='Устройство управления и сбора информации УУСИ 16',
        year=datetime.now().year,
        page=replaced,
        page1=replaced1
        #message='Your application description page.'
    )

@app.route('/config')

def config_module():
    """Renders the usi module page."""
    responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%9A%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D1%8F.md")
    html=responce.read().decode('utf-8')
    sstr="](http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/";
    replaced = re.sub(r'\]\(/', sstr, html)
    #responce=urllib.request.urlopen("http://gitlab.vitebsk.energo.net/uc_oes1/ztp-flash/wikis/%D0%9F%D1%80%D0%BE%D1%88%D0%B8%D0%B2%D0%BA%D0%B0-%D0%A3%D0%A3%D0%A1%D0%98-16.md")
    #html1=responce.read().decode('utf-8')
    #replaced1 = re.sub(r'\]\(/', sstr, html1)
    return render_template(
        'products/config.html',
        title='Программа конфигурации контроллеров',
        year=datetime.now().year,
        page=replaced,
        #page1=replaced1
        #message='Your application description page.'
    )