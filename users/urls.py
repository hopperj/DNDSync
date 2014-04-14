from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',

                       url( r'^login.html$',
                            'user_login',
                            name='users_login'),

                       url( r'^registration.html$',
                            'user_registration',
                            name='users_registration'),

                       url( r'^logout.html$',
                            'user_logout',
                            name='users_logout'),

                       url( r'^$',
                            'index',
                            name='users_index'),

)
