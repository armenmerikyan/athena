"""los URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from store import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView 


urlpatterns = [  
    path('', views.marketcap_async, name='index'), 
    path('verify_signature/', views.verify_signature, name='verify_signature'),    
    path('game_create/', views.game_create, name='game_create'),  
    path('game_next/', views.game_next, name='game_next'),  
    path('all_games/', views.all_games, name='all_games'), 
    path('game/<str:game_id>/', views.view_game, name='view_game'), 
    path('api/add-handle/', views.add_social_media_handle, name='api_add_handle'),
    path('toggle_handle/<int:handle_id>/', views.toggle_handle_status, name='toggle_handle_status'),
    path('add-token-marketing/', views.TokenMarketingContentCreateView.as_view(), name='add_token_marketing'),
    path('login/', views.login_view, name='login'),
    path('forward-to-x/', views.forward_to_x, name='forward_to_x'),
    path('tweets/', views.tweet_list, name='tweet_list'),  # URL for listing tweets
    path('add/', views.create_tweet, name='tweet_add'),  # URL for creating a new tweet
    path('delete_tweet/', views.delete_tweet_by_content, name='delete_tweet_by_content'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='tweet_delete'),  # URL for deleting a tweet
    path('api/create-tweet/', views.create_tweet_api, name='create_tweet_api'),
    path('api/twitter-status/', views.save_twitter_status, name='save_twitter_status'),
    path('api/twitter-status/view/', views.list_twitter_status, name='list_twitter_status'),  # API view
    path('twitter-status/', views.view_twitter_status, name='view_twitter_status'),  # HTML view
    path('delete-status/<int:status_id>/', views.delete_status, name='delete_status'),
    path('api/token/', views.ObtainAuthToken.as_view(), name='token_obtain'),
    path('status/<str:status_id>/', views.twitter_status_detail, name='twitter_status_detail'),
    path('status/<str:status_id>/process/', views.processed_status, name='toggle_processed_status'),
    path('api/user-query/', views.create_user_query, name='create_user_query'), 
    path('api/user-query/<int:query_id>/', views.get_user_query, name='get_user_query'),
    path('user-queries/', views.user_queries_view, name='user_queries_view'),
    path('accounts/login/', views.login_view, name='login'),
    path('api/convo-log/', views.create_convo_log, name='create_convo_log'),
    path('convo_log/<int:pk>/', views.convo_log_detail, name='convo_log_detail'),
    path('api/conversation-topics/', views.create_conversation_topic, name='create_conversation_topic'),
    path('topics/', views.conversation_topics, name='conversation_topics'),  # URL to view topics
    path('topics/<int:pk>/delete/', views.delete_conversation_topic, name='conversation_topic_delete'),
    path('convo_log/delete/<int:id>/', views.delete_convo_log, name='delete_convo_log'),
    path('about-us/', views.about_us, name='about_us'),
    path('upvote/<int:log_id>/', views.upvote_convo_log, name='upvote_convo_log'),
    
    path('verify_signature_game/', views.verify_signature_game, name='verify_signature_game'),
    path('verify_signature/', views.verify_signature, name='verify_signature'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    
    path('marketcap_async/', views.marketcap_async, name='marketcap_async'),
    path('marketcap_json/', views.marketcap_json, name='marketcap_json'),
    path('create_token/', views.create_token, name='create_token'),
    path('get_count/', views.get_count, name='get_count'),  
    
    path('token/<str:mint>/', views.token_detail, name='token_detail'),  
    path('tweets/', views.tweet_list, name='tweet_list'),  # URL for listing tweets
    path('add/', views.create_tweet, name='tweet_add'),  # URL for creating a new tweet
    path('toggle-scam-filter/', views.toggle_scam_filter, name='toggle_scam_filter'),
    path('marketcap_async_search/', views.marketcap_async_search, name='marketcap_async_search'), 


    path('save_room/', views.save_room_view, name='save_room'),
    path('rooms/', views.room_list_view, name='room_list'),  # URL for listing rooms
    path('api/save_room/', views.save_room, name='save_room'),

    path('memories/', views.memory_list, name='memory-list'),  # This will render the HTML page

    path('memory/', views.MemoryView.as_view(), name='create_memory'),
    path('memory/<int:memory_id>/', views.MemoryView.as_view(), name='memory_detail'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
