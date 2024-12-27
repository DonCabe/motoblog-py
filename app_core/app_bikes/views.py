from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

# Lista de publicaciones
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app_bikes/post_list.html', {'posts': posts})

# Funcionalidad de "like"
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_list') # Redirige a la lista de publicaciones

# Botón de contacto (redirige a WhatsApp)
def contacto(request):
    whatsapp_url = "https://wa.me/1234567890?text=¡Hola! Estoy interesado en esta motocicleta." # El número de teléfono es un ejemplo
    return redirect(whatsapp_url)

