from django.conf.urls import url

from . import views

app_name = 'images'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/delete/(\d+)/$', views.delete_images, name='delete_images'),

    url(r'^api/image/opened/(\d+)/$', views.image_opened, name='image_opened'),
    url(r'^api/image/closed/(\d+)/$', views.image_closed, name='image_closed'),

    url(r'^image/setfree/(\d+)/$', views.set_free, name='setfree_imageset'),
    url(r'^image/upload/(\d+)/$', views.upload_image, name='upload_image'),
    url(r'^image/(\d+)/$', views.view_image, name='view_image'),
    url(r'^image/view_thumbnail(\d+)/$', views.view_thumbnail, name='view_thumbnail'),
    url(r'^image/(\d+_files/\d+/\d+_\d+.(?:png|jpeg))/$', views.view_image_tile, name='view_image_tile'),
    url(r'^api/image/verify/$', views.api_verify_image, name='verify_image'),

    url(r'^api/image/plugins/$', views.image_plugins, name='plugins'),


    url(r'^api/image/navigator_overlay_status/$', views.navigator_overlay_status, name='navigator_overlay_status'),
    url(r'^image/(\d+_navigator_overlay/\d+/\d+_\d+.(?:png|jpeg))/$',
        views.view_image_navigator_overlay_tile, name='view_image_navigator_overlay_tile'),

    url(r'^api/image/statistics/$', views.image_statistics, name='image_statistics'),
    url(r'^imagelist/(\d+)/$', views.list_images, name='list_images'),
    url(r'^imageset/(\d+)/label-upload/$', views.label_upload, name='label_upload'),
    url(r'^imageset/create/$', views.create_imageset, name='create_imageset'),
    url(r'^imageset/(\d+)/delete/$', views.delete_imageset, name='delete_imageset'),
    url(r'^imageset/(\d+)/pin/$', views.toggle_pin_imageset, name='pin_imageset'),
    url(r'^imageset/(\d+)/edit/$', views.edit_imageset, name='edit_imageset'),
    url(r'^imageset/(\d+)/$', views.view_imageset, name='view_imageset'),
    url(r'^imageset/(\d+)/download/$', views.download_imageset_zip, name='download_imageset'),
    url(r'^imageset/explore/$', views.explore_imageset, name='explore_imageset'),
    url(r'^imageset/exact_dl_script.py$', views.dl_script, name='dl_script'),
    url(r'^api/imageset/load/$', views.load_image_set, name='load_image_set'),
    url(r'^api/imageset/tag/add/$', views.tag_image_set, name='tag_image_set'),
    url(r'^api/imageset/tag/delete/$', views.remove_image_set_tag, name='remove_image_set_tag'),
    url(r'^api/imageset/tag/autocomplete/$', views.autocomplete_image_set_tag, name='autocomplete_image_set_tag'),

    url(r'^api/imageset/product/add/$', views.product_image_set, name='product_image_set'),
    url(r'^api/imageset/product/delete/$', views.remove_image_set_product, name='remove_image_set_product'),

]