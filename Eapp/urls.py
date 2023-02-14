from django.urls import path
from Eapp import views
urlpatterns=[
    path('',views.indexpg,name='indexpg'),
    path('homepg/',views.homepg,name='homepg'),
    path('notepg/', views.notepg, name='notepg'),
    path('notedbpg/',views.notedbpg,name='notedbpg'),
    path('displaynote/',views.displaynote,name='displaynote'),
    path('editnote/<int:dataid>/',views.editnote,name='editnote'),
    path('updatenote/<int:dataid>/',views.updatenote,name='updatenote'),
    path('delnote/<int:dataid>/',views.delnote,name='delnote'),
    path('aboutpg/',views.aboutpg,name='aboutpg'),
    path('regpg/', views.regpg, name='regpg'),
    path('regpagedb/',views.regpagedb,name='regpagedb'),
    path('logpg/',views.logpg,name='logpg'),
    path('logpgdb/',views.logpgdb,name='logpgdb'),
    path('profilepg/',views.profilepg,name='profilepg'),
    path('editprofile/<int:dataid>/',views.editprofile,name='editprofile'),
    path('updateprofile/<int:dataid>/',views.updateprofile,name='updateprofile'),
    path('delprofile/<int:dataid>/',views.delprofile,name='delprofile'),
    path('userlogout/',views.userlogout,name='userlogout')



]