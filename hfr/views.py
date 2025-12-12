from django.shortcuts import render

# Create your views here.
def home(request):
    # Resort Information Context
    context = {
        # Resort Identity
        'resort_name': 'Himalaya Forest Resort',
        'slogan': 'Escape to best view',
        'brand_promise': 'Where every moment is an unforgettable experience',
        'category': '3-Star Hotel/Resort',
        
        # Location Details
        'location': {
            'full_address': 'Himalaya Forest Resort, Pachabhaiya (Pokhara Metropolitan Ward No. 31), Pokhara, Nepal 33700',
            'locality': 'Deorāli, Pachabhaiya',
            'land_size': '5 Ropani (2,544 square meters)',
            'geographical_setting': 'Situated on hills of Pachabhaiya on the Royal Trekking Way at the top of Begnas Lake and Rupa Lake',
            'surroundings': 'Peaceful land surrounded by forest and local villages with natural beauty',
            'distance_from_lakeside': '11 mi / 17.7 km from main Pokhara Lakeside area',
        },
        
        # Contact Information
        'contact': {
            'telephone': ['+977 9856081271', '+977 9856081371'],
            'email': 'himalayaforestresort@gmail.com',
            'website': 'www.himalayaforestresort.com',  # Assuming this exists
        },
        
        # Room Types with Details
        'rooms': [
            {
                'type': 'Super Deluxe',
                'price': 'NPR 6,500',
                'per_night': True,
                'capacity': '2 Guests',
                'beds': '1 Bed',
                'status': 'Available',
                'booking_code': 'Available',
                'description': 'The super deluxe room offers a luxurious and comfortable space designed for your utmost relaxation and convenience.',
                'image': 'img/rooms/super-deluxe.jpg',
                'popular': True,
                'amenities': ['Mountain view', 'Balcony', 'SPA BATH/JACUZZI', 'Air conditioning', 'Free Internet', 'Television', 'Safe', 'Tea/Coffee maker']
            },
            {
                'type': 'Family Deluxe',
                'price': 'NPR 5,500',
                'per_night': True,
                'capacity': '3 Guests',
                'beds': '2 Beds',
                'status': 'Available',
                'booking_code': 'Available',
                'description': 'Perfect for families with spacious accommodation and comfortable bedding.',
                'image': 'img/rooms/family-deluxe.jpg',
                'popular': False,
                'amenities': ['Mountain view', 'Balcony', 'SPA BATH/JACUZZI', 'Air conditioning', 'Free Internet', 'Television', 'Safe', 'Tea/Coffee maker']
            },
            {
                'type': 'Deluxe Twin',
                'price': 'NPR 4,500',
                'per_night': True,
                'capacity': '2 Guests',
                'beds': '2 Beds',
                'status': 'Available',
                'booking_code': 'Available',
                'description': 'Ideal for friends or colleagues traveling together with separate beds.',
                'image': 'img/rooms/deluxe-twin.jpg',
                'popular': False,
                'amenities': ['Mountain view', 'Balcony', 'SPA BATH/JACUZZI', 'Air conditioning', 'Free Internet', 'Television', 'Safe', 'Tea/Coffee maker']
            }
        ],
        
        # Facilities & Amenities
        'facilities': [
            {
                'name': 'Dining & Restaurant',
                'description': 'Experience exquisite dining with panoramic views from our rooftop restaurant. Three separate dining areas including a wonderful restaurant and lavish bar.',
                'image': 'img/amenities/restaurant.jpg',
                'icon': 'bi bi-cup-hot',
                'features': ['360° rooftop view', '3 dining areas', 'Lavish bar', 'Continental breakfast included']
            },
            {
                'name': 'Conference Hall',
                'description': 'Annapurna Conference hall for business meetings, events, and special occasions. Fully equipped with modern facilities.',
                'image': 'img/amenities/conference.jpg',
                'icon': 'bi bi-building',
                'features': ['Modern setup', 'Capacity 50+', 'Business services available', 'Wake-up service']
            },
            {
                'name': 'Garden & Outdoor',
                'description': 'Open spacious garden for relaxation and events. Perfect for morning walks, meditation, or simply enjoying nature.',
                'image': 'img/amenities/garden.jpg',
                'icon': 'bi bi-flower1',
                'features': ['Spacious garden', 'Multiple terraces', 'Smoking zone', 'Natural setting']
            }
        ],
        
        # Popular Facilities
        'popular_facilities': [
            {'name': 'Free Parking', 'icon': 'bi bi-car-front'},
            {'name': 'Breakfast Included', 'icon': 'bi bi-cup-hot'},
            {'name': 'Free WiFi', 'icon': 'bi bi-wifi'},
            {'name': 'SPA Bath/Jacuzzi', 'icon': 'bi bi-droplet'},
            {'name': '24-Hour Check-in', 'icon': 'bi bi-clock'},
            {'name': 'Pet Friendly', 'icon': 'bi bi-heart'},
        ],
        
        # View Highlights
        'view_highlights': {
            'panoramic': '360-degree panoramic view from rooftop restaurant',
            'mountain_ranges': ['Annapurna', 'Dhaulagiri', 'Manaslu'],
            'mountain_peaks': '20+ individual mountain peaks',
            'lakes': ['Begnas Lake', 'Rupa Lake'],
            'vantage_points': 'Multiple viewing areas throughout property'
        },
        
        # Stats for Homepage
        'stats': [
            {'number': 3, 'label': 'Luxury Room Types', 'icon': 'bi bi-door-closed'},
            {'number': 5, 'label': 'Ropani Property', 'icon': 'bi bi-geo-alt'},
            {'number': 360, 'label': 'Degree View', 'icon': 'bi bi-compass'},
            {'number': 20, 'label': 'Mountain Peaks', 'icon': 'bi bi-mountain'},
        ],
        
        # Dining Information
        'dining': {
            'outlets': ['Main Restaurant', 'Rooftop Open Restaurant', 'Lavish Bar'],
            'total_dining_areas': 3,
            'breakfast': 'Continental breakfast included',
            'room_amenities': 'Tea/Coffee maker in all rooms',
            'special_features': 'Dining table in rooms for in-room dining'
        },
        
        # Policies Highlights
        'policies': {
            'check_in': '24 hours available',
            'check_out': '24 hours available',
            'children': 'Children of all ages welcome',
            'pets': 'Allowed on request (no extra charges)',
            'events': 'Not allowed',
            'smoking': 'Smoke-free property with designated smoking zone'
        },
        
        # Distance to Key Points (in km)
        'distances': {
            'pokhara_airport': {'distance': '9-10 km', 'time': '20-30 minutes'},
            'begnas_lake': {'distance': '2 km', 'time': '5-10 minutes'},
            'rupa_lake': {'distance': 'Proximity mentioned', 'time': 'Very close'},
            'pokhara_lakeside': {'distance': '17.7 km', 'time': '35-45 minutes'},
            'international_mountain_museum': {'distance': '16 km', 'time': '30-40 minutes'},
        },
        
        # Transportation Services
        'transportation': {
            'airport_shuttle': 'Not explicitly mentioned',
            'parking': 'Free private parking available (no reservation needed)',
            'self_drive': 'Recommended option'
        },
        
        # Nearby Attractions
        'nearby_attractions': [
            {'name': 'Begnas Lake', 'distance': '2.8 km', 'type': 'Natural'},
            {'name': 'Rupa Lake', 'distance': 'Very close', 'type': 'Natural'},
            {'name': 'Royal Trekking Way', 'distance': 'Direct access', 'type': 'Adventure'},
            {'name': 'International Mountain Museum', 'distance': '16 km', 'type': 'Cultural'},
            {'name': 'Local Villages and Forests', 'distance': 'Surrounding area', 'type': 'Cultural/Natural'},
        ],
        
        # Testimonials (Placeholder - can be updated with real reviews)
        'testimonials': [
            {
                'text': '"Absolutely stunning views! The service was impeccable and the location breathtaking."',
                'author': 'Happy Guest',
                'avatar': 'img/person/guest-avatar.jpg',
                'rating': 5
            },
            {
                'text': '"Perfect blend of luxury and nature. The panoramic views from the rooftop restaurant are unforgettable."',
                'author': 'Nature Lover',
                'avatar': 'img/person/guest2.jpg',
                'rating': 5
            }
        ],
        
        # Business Operations
        'business': {
            'languages': ['English'],
            'reservation': 'Online booking available',
            'payment': 'Credit card hold may apply',
            'price_match': 'We Price Match guarantee available',
            'newsletter': 'Available on website'
        },
        
        # Target Market
        'target_market': [
            'Nature lovers and view seekers',
            'Pet owners (pet-friendly policy)',
            'Trekkers (Royal Trekking Way access)',
            'Those wanting lake proximity without crowds',
            'Flexible schedule travelers (24-hour check-in/out)'
        ],
        
        # Images for Homepage (you need to add these images to static folder)
        'images': {
            'hero': 'img/hotel/resort-view.jpg',
            'mountain_view': 'img/hotel/mountain-view.jpg',
            'lake_view': 'img/hotel/lake-view.jpg',
            'panoramic_view': 'img/hotel/panoramic-view.jpg',
            # Add more image paths as needed
        },
        
        # Special Features
        'special_features': [
            '360° panoramic view of 3 major Himalayan ranges',
            'SPA BATH/JACUZZI in every room',
            'Pet-friendly with no extra charges',
            '24-hour check-in/check-out',
            'Free private parking',
            'Continental breakfast included',
            'Direct access to Royal Trekking Way'
        ]
    }
    
    return render(request, 'homepage.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def amenities(request):
    return render(request, 'amenities.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def gallery(request):
    return render(request, 'gallery.html')

def rooms(request):
    return render(request, 'rooms.html')

def booking(request):
    return render(request, 'booking.html')