
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Business, Neighbourhood
from .forms import ProfileForm, PostForm
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request, neighbourhood_id):
    posts = Post.objects.filter(neighbourhood= neighbourhood_id).all()
    print(posts)
    return render(request, 'home.html', {"posts": posts})

def single_photo(request, post_id):
    photo = Post.objects.get(id=post_id)
    return render(request, 'image-details.html', {'photo': photo})

def neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html', {'neighbourhoods':neighbourhoods})

def businesses(request):
    businesses = Business.get_businesses() 
    return render(request, 'business.html', {"businesses": businesses})

@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    profiles = Profile.objects.filter(user=current_user).count()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            if profiles == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
            else:
                record = Profile.objects.filter(user=current_user)
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form})

@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Post.objects.filter(user=request.profile.id).all()

    except:

        title = f'{current_user.username}'

        pics = Post.objects.filter(user=request.profile.id).all()


    return render(request, 'profile.html', {"title": title, "current_user": current_user, "pics": pics})


def search_results(request):
    # businesses
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get("businesses")
        searched_businesses = Business.search_by_neighbourhood(search_term)
        message = f"{search_term}"

        return render(request, 'search-results.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search-results.html',{"message":message})

@login_required(login_url='/accounts/login')
def create_post(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    posts = Post.objects.filter(user=current_user).count()

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid:

            if posts == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(home)
            else:
                record = Post.objects.filter(user=current_user)
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(home)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {"form": form})