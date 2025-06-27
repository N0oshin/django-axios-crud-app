from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, index_view
from django.urls import path

router = DefaultRouter()
router.register(r"items", ItemViewSet)  # r'items' makes the endpoint /items/

urlpatterns = router.urls + [
    path("app/", index_view, name="index"),  # http://127.0.0.1:8000/api/app/
]


"""
DRF auto-creates routes like:
- GET /items/ → list all items
- POST /items/ → create new item
- GET /items/{id}/ → retrieve a specific item
- PUT /items/{id}/ → update
- DELETE /items/{id}/ → delete

"""

# from django.urls import path
# from .views import ItemsView

# urlpatterns = [
#     path("items/", ItemsView.as_view(), name="items"),
# ]
