from django.urls import path
from masters import views

urlpatterns = [
    path('', views.ContractList.as_view(), name='home'),
    # path('about/', views.about, name='about'),
    # path('photos/', views.show_photos, name='all_photos'),
    #   path('contact/', views.contact, name='contact'),
    #   path('login/', views.login, name='login'),
    #   path('post/<slug:post_slug>/', views.show_post, name='post'),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # path('category/<slug:cat_slug>/', views.show_category, name='category'),
    #   path('category/<slug:cat_slug>/', views.MastersCategory.as_view(), name='category'),
    # path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.show_tag_postlist, name='tag'),
    #   path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),

]
