from django.urls import include, path
from api import views

# StoreCreateView

urlpatterns = [
    path('user-detail/<int:pk>/', views.UserDetailUpdateDestroy.as_view(), name='user_get'),
    path('users/', views.UserList.as_view(), name='users'),
    path('sent-user/', views.SentMessageUserList.as_view({'get': 'list'}), name='sent_user_list'),

    # Message
    path('messages/', views.MessageList.as_view(), name='messages'),
    path('inbox-messages-list/', views.InboxMessageList.as_view({'get': 'list'}), name='inbox_messages_list'),
    path('sent-messages-list/', views.SentMessageList.as_view({'get': 'list'}), name='sent_messages_list'),
    path('message-detail/<int:pk>/', views.MessageDetailDestroy.as_view(), name='message_get'),

    path('', views.home, name="home"),
]