import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .models import Fruit, Vitamin


@csrf_exempt
def fruit_view(request, pk = None, *args, **kwargs):

    if request.method == "POST":
        try:
            """ data = json.loads(request.body) """
            files = request.FILES

            id = request.POST.get("id")
            name = request.POST.get("name")
            price = request.POST.get("price")
            vitamin_ids = request.POST.get("vitamins")
            image = files.get("image")

            if not id or not name or not price or not vitamin_ids or not image:
                return JsonResponse({"error": "All the fields are required"}, status = 400)

            fruit = Fruit(
                id = id,
                name = name,
                price = price,
                image = image
            )
            fruit.save(using = "default")

            # adding vitamins to the ManyToManyFields
            vitamin_ids = vitamin_ids.split(",")
            vitamins = Vitamin.objects.using('default').filter(id__in = vitamin_ids)
            fruit.vitamins.set(vitamins, through_defaults = None)
            
            data = model_to_dict(fruit)
            data['image'] = fruit.image.url
            data['vitamins'] = [{"id": v.id, "name": v.name} for v in fruit.vitamins.all()]
            return JsonResponse(data, status = 200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 400)
        
    if request.method == "GET":
        if pk:
            try:
                fruit = Fruit.objects.get(id = pk)
                data = model_to_dict(fruit)
                data['image'] = fruit.image.url
                data['vitamins'] = [{"id": v.id, "name": v.name} for v in fruit.vitamins.all()]
                return JsonResponse(data, safe = False ,status = 200)
            except Fruit.DoesNotExist:
                return JsonResponse({"error": "Fruit not found"}, status = 404)
            except Exception as e:
                return JsonResponse({"error": e}, status = 404)     
        
        try:
            fruits = Fruit.objects.all()
            data = []
            for fruit in fruits:
                fruit_data = model_to_dict(fruit)
                fruit_data['image'] = fruit.image.url
                fruit_data['vitamins'] = [{"id": v.id, "name": v.name} for v in fruit.vitamins.all()]
                data.append(fruit_data)
            return JsonResponse(data, safe = False ,status = 200)
        except Fruit.DoesNotExist:
            return JsonResponse({"error": "Fruit not found"}, status = 404)
        except Exception as e:
            return JsonResponse({"error": e}, status = 404)  

    if request.method == "PUT":
        if pk:
            try:
                data = json.loads(request.body)

                fruit = Fruit.objects.get(id = pk)

                id = data.get("id")
                name = data.get("name")
                price = data.get("price")
                vitamin_ids = data.get("vitamins")
                image = request.FILES.get("image")

                if not id:
                    return JsonResponse({"error": "id is required"}, status = 400)
                
                if name:
                    fruit.name = name
                if price:
                    fruit.price = price
                if image:
                    fruit.image = image

                fruit.save(using = "default")

                if vitamin_ids:
                    vitamin_ids = vitamin_ids.split(",")
                    vitamins = Vitamin.objects.using('default').filter(id__in = vitamin_ids)
                    fruit.vitamins.set(vitamins, through_defaults = None)

                data = model_to_dict(fruit)
                data['image'] = fruit.image.url
                data['vitamins'] = [{"id": v.id, "name": v.name} for v in fruit.vitamins.all()]
                return JsonResponse(data, status = 200)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status = 400)
        return JsonResponse({"error": "pk not provided"})
    
    if request.method == "DELETE":
        if pk:
            fruit = get_object_or_404(Fruit, id = pk)
            
            fruit.delete()

            return JsonResponse({"message": "fruit details deleted successfully"}, status = 204)
            
        return JsonResponse({"error": "No id provided"}, status = 400)

    return JsonResponse({"error": "Unsupported request method"}, status = 405)





""" 
HttpResponse and JsonResponse
request_data = json.loads(request.body)
request_data.get(keyname)
"""