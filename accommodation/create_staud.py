from .models import Campus, AccommodationInfo, Accommodation, TopFeature, AccommodationImage
from datetime import date 

ACCOMMODATION_INFO = [str(acc.name) for acc in AccommodationInfo.objects.all()]
CAMPUS_INFO = [str(campus) for campus in Campus.objects.all()]

ACCOMMODATION_TYPE_INFO = [
    'Apartment', 
    'Hostel'
]


FURNISHED_INFO = [  
    'Yes', 
    'No', 
]

ROOM_SIZE_INFO = [ 
    'One man room', 
    'Two man room', 
    'Three man room', 
    'Four man room', 
    'Six man room', 
    'Eight man room',
    'Miniflat', 
    'Self contain'
]
SEX_INFO = [
    'Female',
    'Male',
    'Unisex',
]

MARKET_STATUS_INFO = [
    'Available',
    'Unavailable',
]

def create_staud_id(obj_id):
    year = int(date.today().year)
    return f'STD-{year}{"%02d" % int(date.today().day)}{"%02d" % int(obj_id)}' 


def create_staud(agent, name, accommodation_type, campus, room_size, furnished, sex, market_status, address, price, short_description, full_description, features, images):
    if AccommodationInfo.objects.filter(name__iexact=name).exists():
            acc_info = AccommodationInfo.objects.get(name=name)
            acc_obj = Accommodation.objects.create(
                accommodation = acc_info,
                accommodation_type = accommodation_type,
                campus = Campus.objects.get(name=campus),
                address = address,
                sex = sex,
                market_status=market_status,
                price = price,
                agent = agent,
                room_size = room_size,
                furnished = furnished,
                full_description = full_description,
                display_picture = images[0]
            )
            acc_obj.save()
            acc_obj.staud_id = create_staud_id(acc_obj.id)
            acc_obj.save()
            if features:
                for feature in features:
                    obj = TopFeature.objects.create(
                        accommodation=acc_obj,
                        feature=feature
                    )
                    obj.save()
            for image in images:
                    obj = AccommodationImage.objects.create(
                        accommodation=acc_obj,
                        images=image
                    )
                    obj.save()
    else:
        if agent.company:
            acc_info = AccommodationInfo.objects.create(
                name=name,
                company = agent.company,
                short_description = short_description
                )
        else:
            acc_info = AccommodationInfo.objects.create(
                name=name,
                short_description = short_description
                )
        acc_obj = Accommodation.objects.create(
            accommodation = acc_info,
            accommodation_type = accommodation_type,
            campus = Campus.objects.get(name=campus),
            address = address,
            sex = sex,
            market_status=market_status,
            price = price,
            agent = agent,
            room_size = room_size,
            furnished = furnished,
            full_description = full_description,
            display_picture = images[0]
        )
        acc_obj.save()
        acc_obj.staud_id = create_staud_id(acc_obj.id)
        acc_obj.save()
        if features:
            for feature in features:
                obj = TopFeature.objects.create(
                    accommodation=acc_obj,
                    feature=feature
                )
                obj.save()
        for image in images:
                obj = AccommodationImage.objects.create(
                    accommodation=acc_obj,
                    images=image
                )
                obj.save()

def edit_staud(agent, name, obj_id, accommodation_type, campus, room_size, furnished, sex, market_status, address, price, short_description, full_description, features, images):
    if AccommodationInfo.objects.filter(name__iexact=name).exists():
        acc_info = AccommodationInfo.objects.get(name=name)
        
        acc_obj = Accommodation.objects.get(id=obj_id) 
        
        acc_obj.accommodation = acc_info
        acc_obj.accommodation_type = accommodation_type
        acc_obj.campus = Campus.objects.get(name=campus)
        acc_obj.address = address
        acc_obj.sex = sex
        acc_obj.market_status=market_status
        acc_obj.price = price
        acc_obj.agent = agent
        acc_obj.room_size = room_size
        acc_obj.furnished = furnished
        acc_obj.full_description = full_description
        if images:
            acc_obj.display_picture = images[0]
        acc_obj.save()
        if features:
            for feature in TopFeature.objects.filter(accommodation=acc_obj):
                feature.delete()
            for feature in features:
                obj = TopFeature.objects.create(
                    accommodation=acc_obj,
                    feature=feature
                )
                obj.save()
        if images:
            for image in AccommodationImage.objects.filter(accommodation=acc_obj):
                image.delete()
            for image in images:
                obj = AccommodationImage.objects.create(
                    accommodation=acc_obj,
                    images=image
                )
                obj.save()
    else:
        if agent.company:
            acc_info = AccommodationInfo.objects.create(
                name=name,
                company = agent.company,
                short_description = short_description
                )
            acc_info.save()
        else:
            acc_info = AccommodationInfo.objects.create(
                name=name,
                short_description = short_description
                )
            acc_info.save() 
        acc_obj = Accommodation.objects.get(id=obj_id)    
        acc_obj.accommodation = acc_info
        acc_obj.accommodation_type = accommodation_type
        acc_obj.campus = Campus.objects.get(name=campus)
        acc_obj.address = address
        acc_obj.sex = sex
        acc_obj.market_status=market_status
        acc_obj.price = price
        acc_obj.agent = agent
        acc_obj.room_size = room_size
        acc_obj.furnished = furnished
        acc_obj.full_description = full_description
        if images:
            acc_obj.display_picture = images[0] 
        acc_obj.save()
        if features:
            for feature in TopFeature.objects.filter(accommodation=acc_obj):
                feature.delete()
            for feature in features:
                obj = TopFeature.objects.create(
                    accommodation=acc_obj,
                    feature=feature
                )
                obj.save()
        if images:
            for image in AccommodationImage.objects.filter(accommodation=acc_obj):
                image.delete()
            for image in images:
                obj = AccommodationImage.objects.create(
                    accommodation=acc_obj,
                    images=image
                )
                obj.save()