from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Books, Article
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404


# Create groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Assign permissions to the Editors group
can_edit = Permission.objects.get(codename='can_edit')
can_create = Permission.objects.get(codename='can_create')
editors_group.permissions.add(can_edit, can_create)

# Assign permissions to the Viewers group
can_view = Permission.objects.get(codename='can_view')
viewers_group.permissions.add(can_view)

# Assign permissions to the Admins group (e.g., all permissions)
admins_group.permissions.set(Permission.objects.all())

@permission_required('yourapp.can_view', raise_exception=True)
def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

@permission_required('yourapp.can_create', raise_exception=True)
def article_create_view(request):
    # Code to handle article creation
    return render(request, 'article_form.html')

@permission_required('yourapp.can_edit', raise_exception=True)
def article_edit_view(request, pk):
    # Code to handle article editing
    return render(request, 'article_form.html')

@permission_required('yourapp.can_delete', raise_exception=True)
def article_delete_view(request, pk):
    # Code to handle article deletion
    return render(request, 'article_confirm_delete.html')
