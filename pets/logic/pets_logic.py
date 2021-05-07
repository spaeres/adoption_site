from ..models import Pet


def delete_pet(id):
    Pet.objects.filter(id=id).delete()
    return ()
