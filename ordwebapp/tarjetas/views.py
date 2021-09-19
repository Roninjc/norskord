"""views to generate vocabulary game"""
import random
import csv
from django.shortcuts import render
from tarjetas.models import Ordforrad


def index(request):
    """"view of the choose game page"""
    return render(request, 'tarjetas/index.html')

def cards(request):
    """view to generate the cards game"""
    selected_word_type = request.session.get('selected_word_type')
    selected_level = request.session.get('selected_level')
    if selected_word_type == 'adjective':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        if selected_level == 'low':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'medium':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'high':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        else:
            rows = table.count()
            wid = random.randint(0, rows -1)
            queryset = table[wid]
    elif selected_word_type == 'noun':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        if selected_level == 'low':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'medium':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'high':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        else:
            rows = table.count()
            wid = random.randint(0, rows -1)
            queryset = table[wid]
    elif selected_word_type == 'verb':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        if selected_level == 'low':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'medium':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'high':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        else:
            rows = table.count()
            wid = random.randint(0, rows -1)
            queryset = table[wid]
    else:
        table = Ordforrad.objects.all()
        if selected_level == 'low':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'medium':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        elif selected_level == 'high':
            table_dif = table.filter(lvl_usage=selected_level)
            rows = table_dif.coun()
            wid = random.randint(0, rows -1)
            queryset = table_dif[wid]
        else:
            rows = table.count()
            wid = random.randint(0, rows -1)
            queryset = table[wid]

    word = queryset.norwegian
    translation = queryset.english
    context = {'word': word, 'translation': translation}

    return render(request, 'tarjetas/cards.html', context)

def sidedown(request):
    """view to generate the sidedown game"""
    selected_word_type = request.session.get('selected_word_type')
    if selected_word_type == 'adjective':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    elif selected_word_type == 'noun':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    elif selected_word_type == 'verb':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    else:
        table = Ordforrad.objects.all()
        rows = table.count()
        wid = random.randint(0, rows - 1)
        queryset = table[wid]

    word = queryset.norwegian
    translation = queryset.english
    context = {'word': word, 'translation': translation}

    return render(request, 'tarjetas/sidedown.html', context)

def writit(request):
    """view to generate the sidedown game"""
    selected_word_type = request.session.get('selected_word_type')
    if selected_word_type == 'adjective':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    elif selected_word_type == 'noun':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    elif selected_word_type == 'verb':
        table = Ordforrad.objects.filter(word_class=selected_word_type)
        rows = table.count()
        wid = random.randint(0, rows -1)
        queryset = table[wid]
    else:
        table = Ordforrad.objects.all()
        rows = table.count()
        wid = random.randint(0, rows - 1)
        queryset = table[wid]

    word = queryset.norwegian
    translation = queryset.english
    context = {'word': word, 'translation': translation}

    return render(request, 'tarjetas/writit.html', context)

def populate(request):
    """función para llenar el modelo Ordforrad
    def load(x):
        with open('C:/Users/jesus/Desktop/nouns_list.csv') as file_csv:
            reader = csv.reader(file_csv, delimiter=';', quotechar=';')
            nouns_list = []
            for row in reader:
                nouns_list.append(row)
        r_nouns = len(nouns_list)
        for nouns_fields in nouns_list:
            nouns = Ordforrad.objects.create(
                norwegian=nouns_fields[0],
                english=nouns_fields[1],
                word_class=nouns_fields[2],
                lvl_usage=nouns_fields[3],
                usage_fr=nouns_fields[4],
                usage_permll=nouns_fields[5],
            )
            nouns.save()"""

    def load_nouns():
        with open('C:/Users/jesus/Desktop/nouns_list.csv') as file_csv_csv:
            reader = csv.reader(file_csv_csv, delimiter=';', quotechar=';')
            nouns_list = []
            for row in reader:
                nouns_list.append(row)
        r_nouns = len(nouns_list)
        for nouns_fields in nouns_list:
            nouns = Ordforrad.objects.create(
                norwegian=nouns_fields[0],
                english=nouns_fields[1],
                word_class=nouns_fields[2],
                lvl_usage=nouns_fields[3],
                usage_fr=nouns_fields[4],
                usage_permll=nouns_fields[5],
            )
            nouns.save()
        context.setdefault('r_nouns', r_nouns)
        return context

    def load_verbs():
        with open('C:/Users/jesus/Desktop/verbs_list.csv') as file_csv:
            reader = csv.reader(file_csv, delimiter=';', quotechar=';')
            verbs_list = []
            for row in reader:
                verbs_list.append(row)
        r_verbs = len(verbs_list)
        for verbs_fields in verbs_list:
            verbs = Ordforrad.objects.create(
                norwegian=verbs_fields[0],
                english=verbs_fields[1],
                word_class=verbs_fields[2],
                lvl_usage=verbs_fields[3],
                usage_fr=verbs_fields[4],
                usage_permll=verbs_fields[5],
            )
            verbs.save()
        context.setdefault('r_verbs', r_verbs)
        return context

    def load_adj():
        with open('C:/Users/jesus/Desktop/adj_list.csv') as file_csv:
            reader = csv.reader(file_csv, delimiter=';', quotechar=';')
            adj_list = []
            for row in reader:
                adj_list.append(row)
        r_adj = len(adj_list)
        for adj_fields in adj_list:
            adj = Ordforrad.objects.create(
                norwegian=adj_fields[0],
                english=adj_fields[1],
                word_class=adj_fields[2],
                lvl_usage=adj_fields[3],
                usage_fr=adj_fields[4],
                usage_permll=adj_fields[5],
            )
            adj.save()
        context.setdefault('r_adj', r_adj)
        return context

    Ordforrad.objects.all().delete()
    context = {}

    load_nouns()
    load_verbs()
    load_adj()

    count = Ordforrad.objects.all().count()
    context.setdefault('count', count)
    return render(request, 'tarjetas/populate.html', context)
