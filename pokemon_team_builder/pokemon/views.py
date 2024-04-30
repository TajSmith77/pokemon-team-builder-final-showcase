from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Pokemon, Type, Ability, Move

def pokemon(request):
    mypokemon = Pokemon.objects.all().prefetch_related('types', 'moves', 'abilities')
    all_types = Type.objects.all()
    all_abilities = Ability.objects.all()
    all_moves = Move.objects.all()

    #Filtering
    filter_visible = request.GET.get('filter_visible', False)
    pokedex_number_query = request.GET.get('pokedex_number')
    if pokedex_number_query:
        mypokemon = mypokemon.filter(id=pokedex_number_query)

    name_query = request.GET.get('poke_name')
    if name_query:
        name_query = name_query.strip().lower()
        mypokemon = mypokemon.filter(name__istartswith=name_query)

    type_query = request.GET.get('type')
    if type_query:
        mypokemon = mypokemon.filter(types__id=type_query)

    ability_query = request.GET.get('ability')
    if ability_query:
        mypokemon = mypokemon.filter(abilities__id=ability_query)

    move_query = request.GET.get('move')
    if move_query:
        mypokemon = mypokemon.filter(moves__id=move_query)

    hp_query = request.GET.get('min_hp')
    if hp_query:
        mypokemon = mypokemon.filter(hp__gte=hp_query)

    attack_query = request.GET.get('min_attack')
    if attack_query:
        mypokemon = mypokemon.filter(attack__gte=attack_query)

    defense_query = request.GET.get('min_defense')
    if defense_query:
        mypokemon = mypokemon.filter(defense__gte=defense_query)

    special_attack_query = request.GET.get('min_special_attack')
    if special_attack_query:
        mypokemon = mypokemon.filter(special_attack__gte=special_attack_query)

    special_defense_query = request.GET.get('min_special_defense')
    if special_defense_query:
        mypokemon = mypokemon.filter(special_defense__gte=special_defense_query)

    speed_query = request.GET.get('min_speed')
    if speed_query:
        mypokemon = mypokemon.filter(speed__gte=speed_query)

    #Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by:
        sort_by = sort_by.strip()
        if sort_by == 'name':
            mypokemon = mypokemon.order_by('name')
        if sort_by == 'id':
            mypokemon = mypokemon.order_by('id')

    #Pagination
    per_page = int(request.GET.get('per_page', 50))
    paginator = Paginator(mypokemon, per_page)
    page_number = request.GET.get('page')
    poke_page = paginator.get_page(page_number)
    template = loader.get_template('all_pokemon.html')
    context = {
        'mypokemon': mypokemon,
        'poke_page': poke_page,
        'per_page': per_page,
        'name_query': name_query,
        'pokedex_number_query': pokedex_number_query,
        'type_query': type_query,
        'ability_query': ability_query,
        'move_query': move_query,
        'hp_query': hp_query,
        'attack_query': attack_query,
        'defense_query': defense_query,
        'special_attack_query': special_attack_query,
        'special_defense_query': special_defense_query,
        'speed_query': speed_query,
        'sort_by': sort_by,
        'all_types': all_types,
        'all_abilities': all_abilities,
        'all_moves': all_moves,
        'filter_visible': filter_visible
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mypokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('poke_details.html')
    context = {
        'mypokemon': mypokemon
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))