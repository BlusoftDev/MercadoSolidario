from .models import Bussiness

def ctx_dict(request):
    ctx={}
    bussiness = Bussiness.objects.all()[:1]
    for b in bussiness:
        print(b.name)
        ctx[b.key] = b
    return ctx
