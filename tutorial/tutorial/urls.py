"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path(
        '',
        views.api_root
    ),
    path(
        'snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'
    ),
    path(
        'snippets/<int:pk>/',
        views.SnippetDetail.as_view(),    # 因為他這裏，只吃 function, 所以你不能給 class, 他提供一個方法去處理， class -> function
        name='snippet-detail'
    ),
    path(
        'snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'
    ),
    path(
        'users/',
        views.UserList.as_view(),
        name='user-list'
    ),
    path(
        'users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'
    )
])
'''
def as_view():

    def function(request):
        if request.method == 'GET':
            return self.retrieve(request)

        if request.method == 'DELETE':
            return self.destroy(request)

        if request.method == 'PUT':
            return self.update(request)
    return function
'''
