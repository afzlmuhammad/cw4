from django.shortcuts import render
def form(request):
    if request.GET:
        email = request.GET.get('email')
        return render(request, 'form-data.html',{
            'formData' :request.GET,
            'email' : email
        })
    return render(request, 'form.html')

def ty(request):
    return render(request, 'thankyou.html')