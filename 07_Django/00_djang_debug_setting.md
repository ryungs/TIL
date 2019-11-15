# djang_debug_setting

```bash
`$ pip instll django-debug-toolbar`
```



```python 
INSTALLED_APPS = [
 ...
 'debug_toolbar'
]
MIDDLEWARE = [
 ...
 'debug_toolbar.middleware.DebugToolbarMiddleware',
]
master urls.py
if settings.DEBUG:
   import debug_toolbar

   urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
   ] + urlpatterns
```

