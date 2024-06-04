from django.shortcuts import render, get_object_or_404, redirect
from goods.models import Aproduct, Products, Comment, Favorite
from .forms import ProductSearchForm, CommentForm
from django.contrib.auth.decorators import login_required


def productsView(request):
    products_list = Products.objects.all()
    context = {
        'title': 'Products - catalog',
        'products': products_list,
    }
    return render(request, 'goods/products.html', context)

def product_detail_view(request, slug):
    product = get_object_or_404(Aproduct, slug=slug)
    comments = product.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()
    return render(request, 'goods/product.html', {'product': product, 'comments': comments, 'form': form})

@login_required
def add_comment(request, slug):
    product = get_object_or_404(Aproduct, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()
    return render(request, 'goods/product.html', {'product': product, 'form': form})


def search_view(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Aproduct.objects.filter(title__icontains=query) | Aproduct.objects.filter(description__icontains=query)
    return render(request, 'goods/search_results.html', {'query': query, 'results': results})



@login_required
def add_to_favorite(request, product_slug):
    product = get_object_or_404(Aproduct, slug=product_slug)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('products')

@login_required
def remove_from_favorite(request, product_slug):
    product = get_object_or_404(Aproduct, slug=product_slug)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return redirect('products')


@login_required
def favorite_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'goods/favorite_page.html', {'favorites': favorites})
