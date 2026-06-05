from django.shortcuts import render
from .models import ChaiVarity
from .models import ChaiReviews
from django.shortcuts import get_object_or_404
# Create your views here.
def all_chai(request):
    Chais = ChaiVarity.objects.all() # access  data 
    return render(request, 'chai/all_chai.html',{
        'chais': Chais
    })

# def jjsdj(request):
#     if request.method == "POST":
#     chai = ChaiVarity.create.
#     return render(request, 'chai/all_chai.html',{
#         'chais': Chai,
#         name : name,

#     })


        


 
def chai_details(request, chai_id):
    chai_detail = get_object_or_404(ChaiVarity, pk = chai_id)
    return render(request, 'chai/about.html', {
        'chai': chai_detail
    })


def chai_reviews(request, review_id):
    review_data = get_object_or_404(ChaiReviews,pk = review_id)  
    return render(request, 'chai/review.html', {
        'review': review_data
    })

def chai_store_view(request):
    return render(request, 'chai/chai_stores.html')
    


