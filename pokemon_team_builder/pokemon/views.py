from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

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
  context = {
      
  }
  return HttpResponse(template.render(context, request))

def main_redirect(request):
  return redirect('/home/')

 
# login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
     
    # Render the login page template (GET request)
    return render(request, 'login.html')

def login_redirect(request):
    return redirect('/login/')
 
# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')


@login_required
def logout_page(request):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect('/login/') # Redirect to the login page upon pass

@login_required
def teams(request):
  myteams = Team.objects.filter(owner=request.user)
  template = loader.get_template('teams.html')
  context = {
      'myteams': myteams
  }
  return HttpResponse(template.render(context, request))

def teams_details(request, id):
  myteam = Team.objects.get(id=id)
  template = loader.get_template('teams_details.html')
  context = {
      'myteam': myteam
  }
  return HttpResponse(template.render(context, request))

def create_team(request):
  if request.method == 'POST':
      form = TeamForm(request.POST)
      if form.is_valid():
          team = form.save(commit=False)
          team.owner = request.user
          print(request.POST)
          team.save()
          
          return redirect('/teams/details/' + str(team.id))
  else:
      form = TeamForm()
      print(request.POST)
      context = {
          'form': form
      }
  template = loader.get_template('create_team.html')
 
  return HttpResponse(template.render(context, request))

def update_team(request, id):
  myteam = get_object_or_404(Team, id=id, owner=request.user)
  if request.method == 'POST':
      form = TeamForm(request.POST, instance=myteam)
      if form.is_valid():
          form.save()
          return redirect(f'/teams/details/{id}')
  else:
      form = TeamForm(instance=myteam)
      print(form.instance.name)
      print(form.instance.pokemon1)
      print(form.instance.ability1)
      print(form.instance.move1_1)
      print(form.instance.move1_2)
      print(form.instance.move1_3)
      print(form.instance.move1_4)
      print(form.instance.pokemon2)
      print(form.instance.ability2)
      print(form.instance.move2_1)
      print(form.instance.move2_2)
      print(form.instance.move2_3)
      print(form.instance.move2_4)
      print(form.instance.pokemon3)
      print(form.instance.ability3)
      print(form.instance.move3_1)
      print(form.instance.move3_2)
      print(form.instance.move3_3)
      print(form.instance.move3_4)
      print(form.instance.pokemon4)
      print(form.instance.ability4)
      print(form.instance.move4_1)
      print(form.instance.move4_2)
      print(form.instance.move4_3)
      print(form.instance.move4_4)
      print(form.instance.pokemon5)
      print(form.instance.ability5)
      print(form.instance.move5_1)
      print(form.instance.move5_2)
      print(form.instance.move5_3)
      print(form.instance.move5_4)
      print(form.instance.pokemon6)
      print(form.instance.ability6)
      print(form.instance.move6_1)
      print(form.instance.move6_2)
      print(form.instance.move6_3)
      print(form.instance.move6_4)
      context = {
          'form': form
      }
  template = loader.get_template('update_team.html')
 
  return HttpResponse(template.render(context, request))

def delete_team(request, id):
  myteam = get_object_or_404(Team, id=id, owner=request.user)
  if request.method == 'POST':
      myteam.delete()
      return redirect('teams')
  return redirect('teams')

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))