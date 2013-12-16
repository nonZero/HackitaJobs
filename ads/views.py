from ads.models import Ad
from django.shortcuts import render


def home(request):
    qs = Ad.objects.order_by('-created_at')
    return render(request, 'ads/ad_list.html', {
                            'object_list': qs})
def ad(request, pk):
    ad = Ad.objects.get(id=int(pk))
    return render(request, 'ads/ad_detail.html', {
                            'object': ad})

