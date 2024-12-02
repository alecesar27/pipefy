from django.urls import path
from .views import home, login, signup, logout, list_pipes, create_pipe, update_pipe, create_phase, create_card, read_cards,read_card_details, delete_card,update_card_title,delete_pipe

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('create-pipe/<int:organization_id>/', create_pipe, name='create_pipe'),
    path('update-pipe/<int:pipe_id>', update_pipe, name='update_pipe'),
    path('create-phase/', create_phase, name='create_phase'),
    path('create-card/<int:pipe_id>/', create_card, name='create_card'),
    path('cards/<int:pipe_id>/', read_cards, name='read_cards'),
    path('card-details/<int:pipe_id>/<int:id_card>/', read_card_details, name='read_card_details'),
    path('update-card-title/<int:card_id>', update_card_title, name='update_card_title'),
    path('delete-card/<int:card_id>/', delete_card, name='delete_card'),
    path('delete-pipe/<int:pipe_id>/', delete_pipe, name='delete_pipe'),
    path('list-pipes/', list_pipes, name='list_pipes'),
]