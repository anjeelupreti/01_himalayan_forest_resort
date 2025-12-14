from django.shortcuts import render
from django.contrib import messages 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import os
import base64
from django.conf import settings
import base64
from pathlib import Path
import re
from datetime import datetime

def home(request):
    context = {
        'resort_name': 'Himalaya Forest Resort',
        'slogan': 'Escape to best view',
        'brand_promise': 'Where every moment is an unforgettable experience',
        'category': '3-Star Hotel/Resort',
        
        'location': {
            'full_address': 'Himalaya Forest Resort, Pachabhaiya (Pokhara Metropolitan Ward No. 31), Pokhara, Nepal 33700',
            'locality': 'Deorāli, Pachabhaiya',
            'land_size': '5 Ropani (2,544 square meters)',
            'geographical_setting': 'Situated on hills of Pachabhaiya on the Royal Trekking Way at the top of Begnas Lake and Rupa Lake',
            'surroundings': 'Peaceful land surrounded by forest and local villages with natural beauty',
            'distance_from_lakeside': '11 mi / 17.7 km from main Pokhara Lakeside area',
        },
        
        'contact': {
            'telephone': ['+977 9856081271', '+977 9856081371'],
            'email': 'himalayaforestresort@gmail.com',
            'website': 'www.himalayaforestresort.com',  
        },
        
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
                'image': 'assets/img/rooms/super_deluxe_06.jpg',
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
                'image': 'assets/img/rooms/family_deluxe_02.jpg',
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
                'image': 'assets/img/rooms/deluxe_twin_01.jpg',
                'popular': False,
                'amenities': ['Mountain view', 'Balcony', 'SPA BATH/JACUZZI', 'Air conditioning', 'Free Internet', 'Television', 'Safe', 'Tea/Coffee maker']
            }
        ],
        
        'facilities': [
            {
                'name': 'Dining & Restaurant',
                'description': 'Experience exquisite dining with panoramic views from our rooftop restaurant. Three separate dining areas including a wonderful restaurant and lavish bar.',
                'image': 'assets/img/amenities/dining_01.jpg',
                'icon': 'bi bi-cup-hot',
                'features': ['360° rooftop view', '3 dining areas', 'Lavish bar', 'Continental breakfast included']
            },
            {
                'name': 'View',
                'description': 'Breathtaking 360-degree panoramic views of Begnas Lake, Rupa Lake, and the Himalayan ranges including Annapurna, Dhaulagiri, and Manaslu.',
                'image': 'assets/img/amenities/view_01.jpg',
                'icon': 'bi bi-binoculars',
                'features': ['Panoramic lake views', 'Himalayan mountain ranges', 'Multiple vantage points', 'Sunrise & sunset views']
            },
            {
                'name': 'Garden & Outdoor',
                'description': 'Open spacious garden for relaxation and events. Perfect for morning walks, meditation, or simply enjoying nature.',
                'image': 'assets/img/amenities/garden_01.jpg',
                'icon': 'bi bi-flower1',
                'features': ['Spacious garden', 'Multiple terraces', 'Smoking zone', 'Natural setting']
            }
        ],
        
        'popular_facilities': [
            {'name': 'Free Parking', 'icon': 'bi bi-car-front'},
            {'name': 'Breakfast Included', 'icon': 'bi bi-cup-hot'},
            {'name': 'Free WiFi', 'icon': 'bi bi-wifi'},
            {'name': 'SPA Bath/Jacuzzi', 'icon': 'bi bi-droplet'},
            {'name': '24-Hour Check-in', 'icon': 'bi bi-clock'},
            {'name': 'Pet Friendly', 'icon': 'bi bi-heart'},
        ],
        
        'view_highlights': {
            'panoramic': '360-degree panoramic view from rooftop restaurant',
            'mountain_ranges': ['Annapurna', 'Dhaulagiri', 'Manaslu'],
            'mountain_peaks': '20+ individual mountain peaks',
            'lakes': ['Begnas Lake', 'Rupa Lake'],
            'vantage_points': 'Multiple viewing areas throughout property'
        },
        
        'stats': [
            {'number': 3, 'label': 'Luxury Room Types', 'icon': 'bi bi-door-closed'},
            {'number': 5, 'label': 'Ropani Area', 'icon': 'bi bi-geo-alt'},
            {'number': 360, 'label': 'Degree View', 'icon': 'bi bi-compass'},
            {'number': 20, 'label': 'Mountain Peaks', 'icon': 'bi bi-mountain'},
        ],
        
        'dining': {
            'outlets': ['Main Restaurant', 'Rooftop Open Restaurant', 'Lavish Bar'],
            'total_dining_areas': 3,
            'breakfast': 'Continental breakfast included',
            'room_amenities': 'Tea/Coffee maker in all rooms',
            'special_features': 'Dining table in rooms for in-room dining'
        },
        
        'policies': {
            'check_in': '24 hours available',
            'check_out': '24 hours available',
            'children': 'Children of all ages welcome',
            'pets': 'Allowed on request (no extra charges)',
            'events': 'Not allowed',
            'smoking': 'Smoke-free property with designated smoking zone'
        },
        
        'distances': {
            'pokhara_airport': {'distance': '9-10 km', 'time': '20-30 minutes'},
            'begnas_lake': {'distance': '2 km', 'time': '5-10 minutes'},
            'rupa_lake': {'distance': 'Proximity mentioned', 'time': 'Very close'},
            'pokhara_lakeside': {'distance': '17.7 km', 'time': '35-45 minutes'},
            'international_mountain_museum': {'distance': '16 km', 'time': '30-40 minutes'},
        },
        
        'transportation': {
            'airport_shuttle': 'Not explicitly mentioned',
            'parking': 'Free private parking available (no reservation needed)',
            'self_drive': 'Recommended option'
        },
        
        'nearby_attractions': [
            {'name': 'Begnas Lake', 'distance': '2.8 km', 'type': 'Natural'},
            {'name': 'Rupa Lake', 'distance': 'Very close', 'type': 'Natural'},
            {'name': 'Royal Trekking Way', 'distance': 'Direct access', 'type': 'Adventure'},
            {'name': 'International Mountain Museum', 'distance': '16 km', 'type': 'Cultural'},
            {'name': 'Local Villages and Forests', 'distance': 'Surrounding area', 'type': 'Cultural/Natural'},
        ],
        
        'testimonials': [
            {
                'text': '"Absolutely stunning views! The service was impeccable and the location breathtaking."',
                'author': 'Happy Guest',
                'avatar': 'assets/img/person/guest_01.jpg',
                'rating': 5
            },
            {
                'text': '"Perfect blend of luxury and nature. The panoramic views from the rooftop restaurant are unforgettable."',
                'author': 'Nature Lover',
                'avatar': 'assets/img/person/guest_02.jpg',
                'rating': 5
            }
        ],
        
        'business': {
            'languages': ['English'],
            'reservation': 'Online booking available',
            'payment': 'Credit card hold may apply',
            'price_match': 'We Price Match guarantee available',
            'newsletter': 'Available on website'
        },
        
        'target_market': [
            'Nature lovers and view seekers',
            'Pet owners (pet-friendly policy)',
            'Trekkers (Royal Trekking Way access)',
            'Those wanting lake proximity without crowds',
            'Flexible schedule travelers (24-hour check-in/out)'
        ],
        
        'images': {
            'hero': 'assets/img/hotel/resort_02.jpg',
            'mountain_view': 'assets/img/views/mountain_01.jpg',
            'lake_view': 'assets/img/views/begnas_lake_01.jpg',
            'panoramic_view': 'assets/img/hotel/panoramic-view.jpg',
        },
        
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
    resort_info = {
        'name': 'Himalaya Forest Resort',
        'established_year': 2020,
        'location': 'Pachabhaiya (Pokhara Metropolitan Ward No. 31), Pokhara, Nepal',
        'category': '3-Star Hotel/Resort',
        'slogan': 'Escape to best view',
        'motto': 'Where Himalayan Beauty Meets Modern Luxury',
        'brand_promise': 'Where every moment is an unforgettable experience',
        'description': 'perfect blend of relaxation, adventure, and indulgence',
        
        'main_description': 'Nestled in the serene hills overlooking Begnas Lake and Rupa Lake, Himalaya Forest Resort offers a perfect blend of natural beauty and contemporary comfort.',
        'detailed_description': 'Located in Pachabhaiya (Pokhara Metropolitan Ward No. 31), our resort is designed to provide guests with an unforgettable escape from the ordinary. Every moment at our resort is crafted to offer peace, luxury, and memories that last a lifetime.',
        
        
        
        'main_image': 'assets/img/resort/resort_01.jpg',
        'secondary_image':'assets/img/resort/resort_02.jpg',
    }
    
    milestones = [
        {
            'year': 2020,
            'title': 'Grand Opening',
            'description': 'Founded as premium mountain retreat',
            'icon': 'bi-building'
        },
        {
            'year': 2022,
            'title': 'Major Expansion',
            'description': 'Added luxury rooms and conference facilities',
            'icon': 'bi-expand'
        },
        {
            'year': 2024,
            'title': 'Award Recognition',
            'description': 'Recognized as top resort in Pokhara region',
            'icon': 'bi-award'
        }
    ]
    
    features = [
        {
            'title': 'Panoramic Views',
            'description': 'Breathtaking views of Begnas Lake, Rupa Lake, and Himalayan ranges from every room',
            'image': 'assets/img/views/mountain_01.jpg',
            'icon': 'bi-flower1',
            'alt': 'Spa Services'
        },
        {
            'title': 'Local Cuisine',
            'description': 'Authentic Nepali and international cuisine prepared by expert chefs',
            'image': 'assets/img/amenities/food_01.jpg',
            'icon': 'bi-cup-hot',
            'alt': 'Fine Dining'
        },
        {
            'title': 'Prime Location',
            'description': 'Nestled between two beautiful lakes with easy access to Pokhara attractions',
            'image': 'assets/img/views/view_02.jpg',
            'icon': 'bi-geo-alt',
            'alt': 'Prime Location'
        }
    ]
    
    achievements = [
        {
            'count': 25,
            'suffix': '',
            'title': 'Luxury Rooms',
            'description': 'Beautifully appointed rooms with premium amenities'
        },
        {
            'count': 98,
            'suffix': '%',
            'title': 'Guest Satisfaction',
            'description': 'Highly rated by our valued guests'
        },
        {
            'count': 3,
            'suffix': '-Star',
            'title': 'Star Rating',
            'description': '3-star luxury with premium experience'
        },
        {
            'count': 1000,
            'suffix': '+',
            'title': 'Happy Guests',
            'description': 'Memorable experiences created'
        }
    ]
    
    rooms_data = [
        {
            'id': 1,
            'name': 'Super Deluxe Room',
            'price': 6500,
            'description': 'Our premium Super Deluxe rooms offer panoramic views of Begnas Lake and the surrounding Himalayan ranges. Featuring modern amenities and elegant decor for the ultimate comfort experience.',
            'image': 'assets/img/rooms/super_deluxe_06.jpg',
            'capacity': 2,
            'size': '45m²',
            'view': 'Lake View',
            'rating': 5.0,
            'amenities': ['High-Speed WiFi', 'Smart TV', 'Tea/Coffee Maker', 'Air Conditioning'],
            'booking_code': 'Available',
            'is_featured': True
        },
        {
            'id': 2,
            'name': 'Family Deluxe Room',
            'price': 5500,
            'description': 'Spacious accommodation perfect for families with connecting rooms and child-friendly amenities.',
            'image': 'assets/img/rooms/family_deluxe_02.jpg',
            'capacity': 3,
            'size': '50m²',
            'view': 'Garden View',
            'rating': 4.7,
            'amenities': ['Family Space', 'Garden View'],
            'booking_code': 'Available',
            'is_featured': False
        },
        {
            'id': 3,
            'name': 'Deluxe Twin Room',
            'price': 4500,
            'description': 'Perfect for friends or colleagues traveling together with two comfortable beds and shared space.',
            'image': 'assets/img/rooms/deluxe_twin_03.jpg',
            'capacity': 2,
            'size': '40m²',
            'view': 'Mountain View',
            'rating': 4.5,
            'amenities': ['Twin Beds', 'Private Balcony'],
            'booking_code': 'Available',
            'is_featured': False
        }
    ]
    
    context = {
        'resort': resort_info,
        'milestones': milestones,
        'features': features,
        'achievements': achievements,
        'rooms': rooms_data,
    }
    
    return render(request, 'about_us.html', context)
def amenities(request):
    return render(request, 'amenities.html')



def contact_us(request):
    contact_info = {
        'resort_name': 'Himalaya Forest Resort',
        'address': 'Pachabhaiya (Pokhara Metropolitan Ward No. 31)',
        'city': '33700 Deorāli, Nepal',
        'location_description': 'Near Begnas Lake & Rupa Lake',
        'phone_numbers': {
            'reservations': '+977 9856081271',
            'general': '+977 9856081371',
            'whatsapp': '+977 9856081271'
        },
        'emails': {
            'bookings': 'codevault.services@gmail.com',
            'general': 'codevault.services@gmail.com',
            'support': 'codevault.services@gmail.com'
        },
        'social_media': {
            'facebook': '#',
            'instagram': '#',
            'twitter': '#',
            'youtube': '#'
        },
        'office_hours': {
            'weekdays': '6:00 AM - 10:00 PM',
            'weekends': '6:00 AM - 10:00 PM',
            'reception': '24/7'
        },
        'check_times': {
            'check_in': '2:00 PM',
            'check_out': '12:00 PM',
            'early_check_in': 'Available on request',
            'late_check_out': 'Available on request'
        },
        'transportation': {
            'airport_pickup': 'Available (additional charge)',
            'taxi_service': 'Arranged upon request',
            'parking': 'Free private parking available',
            'distance_airport': '7.5 miles / 20-30 minutes',
            'distance_begnas_lake': '2 km / 5-10 minutes'
        },
        'google_maps_embed': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3510.487434756978!2d83.9857140754039!3d28.33638307579379!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3995937bbf0376ff%3A0x71dd9a54f9d4d3f!2sBegnas%20Lake!5e0!3m2!1sen!2snp!4v1700000000000!5m2!1sen!2snp',
        'google_maps_link': 'https://maps.google.com/?q=Himalaya+Forest+Resort+Pachabhaiya+Pokhara+Nepal'
    }
    
    contact_subjects = [
        {'value': 'booking', 'label': 'Booking Inquiry'},
        {'value': 'room', 'label': 'Room Information'},
        {'value': 'amenities', 'label': 'Amenities & Services'},
        {'value': 'event', 'label': 'Event Planning'},
        {'value': 'feedback', 'label': 'Feedback & Suggestions'},
        {'value': 'other', 'label': 'Other Inquiry'}
    ]
    
    form_submitted = False
    contact_name = ''
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        newsletter = request.POST.get('newsletter') == 'on'
        
        errors = []
        
        if not name:
            errors.append('Name is required')
        
        if not email:
            errors.append('Email is required')
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append('Please enter a valid email address')
        
        if not subject:
            errors.append('Subject is required')
        
        if not message:
            errors.append('Message is required')
        elif len(message) < 10:
            errors.append('Message should be at least 10 characters')
        
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                subject_dict = {s['value']: s['label'] for s in contact_subjects}
                subject_label = subject_dict.get(subject, "General Inquiry")
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ip_address = request.META.get('REMOTE_ADDR', 'N/A')
                
                # ========== FIXED: MOVE LOGO READING INSIDE TRY BLOCK ==========
                # Encode logo as base64 for emails
                logo_path = Path(settings.BASE_DIR) / 'static' / 'assets' / 'img' / 'logo.png'
                logo_base64_str = ""  # Changed variable name to avoid confusion
                
                if logo_path.exists():
                    with open(logo_path, "rb") as logo_file:
                        logo_base64_str = base64.b64encode(logo_file.read()).decode('utf-8')
                
                # Add debug logging
                import logging
                logger = logging.getLogger(__name__)
                logger.info(f"Logo base64 length: {len(logo_base64_str)}")
                logger.info(f"Logo path exists: {logo_path.exists()}")
                # =============================================================
                
                # Context for resort email
                resort_context = {
                    'name': name,
                    'email': email,
                    'phone': phone if phone else 'Not provided',
                    'subject': subject_label,
                    'message': message,
                    'newsletter': 'Yes' if newsletter else 'No',
                    'timestamp': timestamp,
                    'ip_address': ip_address,
                    'resort_name': contact_info['resort_name'],
                    'logo_base64': logo_base64_str,  # Use the new variable name
                    'resort_phone': contact_info['phone_numbers']['reservations'],
                    'resort_email': contact_info['emails']['bookings'],
                    'resort_address': f"{contact_info['address']}, {contact_info['city']}"
                }
                
                # Debug: Check context
                logger.info(f"Resort context has logo_base64: {'logo_base64' in resort_context}")
                logger.info(f"Resort context logo_base64 length: {len(resort_context.get('logo_base64', ''))}")
                
                user_context = {
                    'name': name,
                    'subject': subject_label,
                    'reservation_phone': contact_info['phone_numbers']['reservations'],
                    'resort_address': contact_info['address'],
                    'resort_city': contact_info['city'],
                    'resort_email': contact_info['emails']['bookings'],
                    'resort_name': contact_info['resort_name'],
                    'logo_base64': logo_base64_str,  # Use the new variable name
                    'timestamp': timestamp,
                    'contact_subject': subject_label
                }
                
                # Test render the templates
                resort_email_body = render_to_string('emails/contact_to_resort.html', resort_context)
                user_email_body = render_to_string('emails/contact_to_user.html', user_context)
                
                # Debug: Check if base64 is in rendered output
                logger.info(f"Resort email contains base64: {'data:image/png;base64' in resort_email_body}")
                logger.info(f"User email contains base64: {'data:image/png;base64' in user_email_body}")
                
                # If base64 not found, add fallback
                if 'data:image/png;base64' not in resort_email_body:
                    logger.warning("Base64 not found in resort email template!")
                    # Add fallback HTML
                    fallback_html = '<div style="color: white; font-size: 1.8rem; font-weight: 700;">HIMALAYA FOREST RESORT</div>'
                    resort_email_body = resort_email_body.replace('{% if logo_base64 %}', f'{fallback_html}{{% if logo_base64 %}}')
                
                resort_email_subject = f'Contact Form: {subject_label} - {name}'
                user_email_subject = f'Thank you for contacting Himalaya Forest Resort'
                
                # Send email to resort
                resort_email = EmailMessage(
                    subject=resort_email_subject,
                    body=resort_email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[contact_info['emails']['bookings']],  
                    reply_to=[email] 
                )
                resort_email.content_subtype = "html"
                
                # Debug: Log before sending
                logger.info(f"Sending resort email to: {contact_info['emails']['bookings']}")
                logger.info(f"Email subject: {resort_email_subject}")
                
                try:
                    resort_email.send(fail_silently=False)
                    logger.info("Resort email sent successfully")
                except Exception as send_error:
                    logger.error(f"Failed to send resort email: {send_error}")
                
                # Send confirmation email to user
                user_email = EmailMessage(
                    subject=user_email_subject,
                    body=user_email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email],
                )
                user_email.content_subtype = "html"
                
                try:
                    user_email.send(fail_silently=False)
                    logger.info("User email sent successfully")
                except Exception as send_error:
                    logger.error(f"Failed to send user email: {send_error}")
                
                form_submitted = True
                contact_name = name
                
                messages.success(request, f'Thank you {name}! Your message has been sent successfully. We will get back to you within 24 hours.')
                
                context = {
                    'contact': contact_info,
                    'subjects': contact_subjects,
                    'form_submitted': form_submitted,
                    'contact_name': contact_name,
                    'page_title': 'Contact Us | Himalaya Forest Resort, Pokhara',
                    'meta_description': 'Get in touch with Himalaya Forest Resort in Pokhara, Nepal. Contact us for bookings, inquiries, or to plan your perfect Himalayan getaway.',
                    'meta_keywords': 'Contact Himalaya Forest Resort, Pokhara Hotel Contact, Nepal Resort Contact, Booking Inquiry, Hotel Phone Number, Resort Email',
                }
                
                return render(request, 'contact_us.html', context)
                
            except Exception as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Email sending error in contact_us: {e}", exc_info=True)
                
                messages.error(request, 'There was an error sending your message. Please try again or contact us directly.')
    
    # For GET requests or if there are errors
    context = {
        'contact': contact_info,
        'subjects': contact_subjects,
        'form_submitted': form_submitted,
        'contact_name': contact_name,
        'page_title': 'Contact Us | Himalaya Forest Resort, Pokhara',
        'meta_description': 'Get in touch with Himalaya Forest Resort in Pokhara, Nepal. Contact us for bookings, inquiries, or to plan your perfect Himalayan getaway.',
        'meta_keywords': 'Contact Himalaya Forest Resort, Pokhara Hotel Contact, Nepal Resort Contact, Booking Inquiry, Hotel Phone Number, Resort Email',
    }
    
    return render(request, 'contact_us.html', context)


def gallery(request):
    gallery_images = [
        {
            'id': 1,
            'image': 'assets/img/rooms/deluxe_twin_01.jpg',
            'alt': 'Deluxe Twin Room - Interior View 1',
            'title': 'Deluxe Twin Room',
            'description': 'Comfortable room with twin beds and mountain view',
            'lightbox_title': 'Deluxe Twin Room - Spacious accommodation perfect for friends or colleagues',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 2,
            'image': 'assets/img/rooms/deluxe_twin_02.jpg',
            'alt': 'Deluxe Twin Room - Interior View 2',
            'title': 'Deluxe Twin Room',
            'description': 'Modern amenities and comfortable furnishings',
            'lightbox_title': 'Deluxe Twin Room - Featuring modern decor and essential amenities',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 3,
            'image': 'assets/img/rooms/deluxe_twin_03.jpg',
            'alt': 'Deluxe Twin Room - Bathroom',
            'title': 'Deluxe Twin Bathroom',
            'description': 'Private bathroom with spa bath facilities',
            'lightbox_title': 'Deluxe Twin Room Bathroom - Equipped with SPA bath and premium toiletries',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 4,
            'image': 'assets/img/rooms/family_deluxe_01.jpg',
            'alt': 'Family Deluxe Room - Main Area',
            'title': 'Family Deluxe Room',
            'description': 'Spacious accommodation perfect for families',
            'lightbox_title': 'Family Deluxe Room - Comfortable space for up to 3 guests',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 5,
            'image': 'assets/img/rooms/family_deluxe_02.jpg',
            'alt': 'Family Deluxe Room - Sleeping Area',
            'title': 'Family Deluxe Room',
            'description': 'Two comfortable beds with premium bedding',
            'lightbox_title': 'Family Deluxe Room - Sleeping area with two comfortable beds',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 6,
            'image': 'assets/img/rooms/family_deluxe_03.jpg',
            'alt': 'Family Deluxe Room - Seating Area',
            'title': 'Family Deluxe Room',
            'description': 'Cozy seating area with balcony access',
            'lightbox_title': 'Family Deluxe Room - Comfortable seating area perfect for family time',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 7,
            'image': 'assets/img/rooms/super_deluxe_02.jpg',
            'alt': 'Super Deluxe Room - Panoramic View',
            'title': 'Super Deluxe Room',
            'description': 'Luxurious room with breathtaking mountain views',
            'lightbox_title': 'Super Deluxe Room - Featuring panoramic views of Annapurna range',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-6',
            'height_class': 'tall'
        },
        {
            'id': 8,
            'image': 'assets/img/rooms/super_deluxe_03.jpg',
            'alt': 'Super Deluxe Room - Interior Luxury',
            'title': 'Super Deluxe Room',
            'description': 'Premium furnishings and elegant decor',
            'lightbox_title': 'Super Deluxe Room - Luxury interior with premium amenities',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 9,
            'image': 'assets/img/rooms/super_deluxe_04.jpg',
            'alt': 'Super Deluxe Room - Jacuzzi Bathroom',
            'title': 'Super Deluxe Jacuzzi',
            'description': 'Luxurious bathroom with spa bath/jacuzzi',
            'lightbox_title': 'Super Deluxe Room - Premium bathroom with SPA bath/Jacuzzi',
            'category': 'rooms',
            'category_name': 'Rooms & Suites',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 10,
            'image': 'assets/img/views/begnas_lake_01.jpg',
            'alt': 'Begnas Lake Panoramic View',
            'title': 'Begnas Lake View',
            'description': 'Stunning panoramic view of Begnas Lake',
            'lightbox_title': 'Panoramic view of Begnas Lake from Himalaya Forest Resort',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-8',
            'height_class': 'tall'
        },
        {
            'id': 11,
            'image': 'assets/img/views/mountain_01.jpg',
            'alt': 'Himalayan Mountain Range',
            'title': 'Himalayan Mountains',
            'description': 'View of Annapurna, Dhaulagiri, and Manaslu ranges',
            'lightbox_title': '360-degree panoramic view of three major Himalayan ranges',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 12,
            'image': 'assets/img/views/view_01.jpg',
            'alt': 'Resort Surroundings View 1',
            'title': 'Natural Surroundings',
            'description': 'Peaceful forest and village views',
            'lightbox_title': 'Natural beauty surrounding Himalaya Forest Resort',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 13,
            'image': 'assets/img/views/view_02.jpg',
            'alt': 'Resort Surroundings View 2',
            'title': 'Countryside View',
            'description': 'Scenic view of local villages and landscapes',
            'lightbox_title': 'View of local villages and Nepali countryside',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 14,
            'image': 'assets/img/views/view_03.jpg',
            'alt': 'Resort Surroundings View 3',
            'title': 'Forest View',
            'description': 'Lush forest surrounding the resort',
            'lightbox_title': 'Dense forest surrounding the resort property',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 15,
            'image': 'assets/img/views/view_04.jpg',
            'alt': 'Resort Surroundings View 4',
            'title': 'Garden View',
            'description': 'Beautiful garden and outdoor spaces',
            'lightbox_title': 'Well-maintained garden area of the resort',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 16,
            'image': 'assets/img/views/view_05.jpg',
            'alt': 'Resort Surroundings View 5',
            'title': 'Sunset View',
            'description': 'Breathtaking sunset over the mountains',
            'lightbox_title': 'Stunning sunset view from the rooftop restaurant',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 17,
            'image': 'assets/img/views/view_06.jpg',
            'alt': 'Resort Surroundings View 6',
            'title': 'Morning View',
            'description': 'Morning mist over the lakes and mountains',
            'lightbox_title': 'Early morning view with mist over Begnas Lake',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
        {
            'id': 18,
            'image': 'assets/img/views/view_07.jpg',
            'alt': 'Resort Surroundings View 7',
            'title': 'Panoramic Landscape',
            'description': '360-degree view from rooftop restaurant',
            'lightbox_title': 'Complete 360-degree panoramic view from resort rooftop',
            'category': 'views',
            'category_name': 'Lake & Mountain Views',
            'col_class': 'col-lg-8',
            'height_class': 'tall'
        },
        {
            'id': 19,
            'image': 'assets/img/amenities/dining_01.jpg',
            'alt': 'Restaurant Dining Area',
            'title': 'Restaurant Interior',
            'description': 'Elegant dining area with mountain views',
            'lightbox_title': 'Main restaurant serving authentic Nepali and international cuisine',
            'category': 'amenities',
            'category_name': 'Amenities & Facilities',
            'col_class': 'col-lg-6',
            'height_class': 'regular'
        },
        {
            'id': 20,
            'image': 'assets/img/amenities/garden_01.jpg',
            'alt': 'Resort Garden Area',
            'title': 'Landscaped Garden',
            'description': 'Beautiful open garden space',
            'lightbox_title': 'Open spacious garden perfect for relaxation',
            'category': 'amenities',
            'category_name': 'Amenities & Facilities',
            'col_class': 'col-lg-6',
            'height_class': 'regular'
        },
        {
            'id': 21,
            'image': 'assets/img/resort/resort_01.jpg',
            'alt': 'Aerial View of Resort',
            'title': 'Resort Aerial View',
            'description': 'Aerial view showing resort location',
            'lightbox_title': 'Aerial view of Himalaya Forest Resort amidst nature',
            'category': 'resort',
            'category_name': 'Resort Exterior',
            'col_class': 'col-lg-8',
            'height_class': 'tall'
        },
        {
            'id': 22,
            'image': 'assets/img/resort/resort_02.jpg',
            'alt': 'Closeup of Resort Building',
            'title': 'Resort Building',
            'description': 'Closeup view of resort architecture',
            'lightbox_title': 'Closeup view of Himalaya Forest Resort building',
            'category': 'resort',
            'category_name': 'Resort Exterior',
            'col_class': 'col-lg-4',
            'height_class': 'regular'
        },
    ]
    
    categories = []
    category_counts = {}
    
    for image in gallery_images:
        if image['category'] not in category_counts:
            category_counts[image['category']] = 0
            categories.append({
                'slug': image['category'],
                'name': image['category_name']
            })
        category_counts[image['category']] += 1
    
    categories.insert(0, {
        'slug': 'all',
        'name': 'All Photos'
    })
    
    total_images = len(gallery_images)
    room_images_count = len([img for img in gallery_images if img['category'] == 'rooms'])
    view_images_count = len([img for img in gallery_images if img['category'] == 'views'])
    
    for category in categories[1:]:
        category['count'] = category_counts.get(category['slug'], 0)
    
    context = {
        'gallery_images': gallery_images,
        'categories': categories,
        'total_images': total_images,
        'room_images_count': room_images_count,
        'view_images_count': view_images_count,
        'title': 'Photo Gallery - Himalaya Forest Resort',
        'meta_description': 'Explore our photo gallery showcasing the beauty of Himalaya Forest Resort in Pokhara. View our luxurious rooms, breathtaking panoramic views of Begnas Lake, Rupa Lake, and Himalayan mountains, resort amenities, and beautiful surroundings.',
        'meta_keywords': 'Resort Gallery, Pokhara Photos, Hotel Pictures, Room Images, Begnas Lake View, Rupa Lake Photos, Himalayan Mountains, Resort Amenities, Nepal Tourism'
    }
    
    return render(request, 'gallery.html', context)

def rooms(request):
    rooms_data = [
        {
            'id': 1,
            'slug': 'super-deluxe',
            'name': 'Super Deluxe Room',
            'price': 6500,
            'original_price': 6500,
            'capacity': 2,
            'bed_config': '1 Bed',
            'size': '45 sq m',
            'view_type': 'lake_mountain',
            'description': 'Experience luxury with panoramic views of Begnas Lake and Himalayas. Features modern amenities, comfortable seating area, and private balcony.',
            'image': 'assets/img/rooms/super_deluxe_06.jpg',
            'features': ['Lake View', 'Most Popular', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.9,
            'booking_code': 'Available',
            'category': 'super-deluxe',
            'is_popular': True,
            'badge': 'popular'
        },
        {
            'id': 2,
            'slug': 'family-deluxe',
            'name': 'Family Deluxe Room',
            'price': 5500,
            'original_price': 5500,
            'capacity': 3,
            'bed_config': '2 Beds',
            'size': '50 sq m',
            'view_type': 'lake_mountain',
            'description': 'Spacious accommodation perfect for families. Features connecting rooms option, kid-friendly amenities, and garden access.',
            'image': 'assets/img/rooms/family_deluxe_02.jpg',
            'features': ['Lake View', 'Family Friendly', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.7,
            'booking_code': 'Available',
            'category': 'family-deluxe',
            'is_popular': False,
            'badge': 'family'
        },
        {
            'id': 3,
            'slug': 'deluxe-twin',
            'name': 'Deluxe Twin Room',
            'price': 4500,
            'original_price': 4500,
            'capacity': 2,
            'bed_config': '2 Beds',
            'size': '40 sq m',
            'view_type': 'mountain',
            'description': 'Perfect for friends or colleagues. Features twin beds, comfortable workspace, and stunning mountain views.',
            'image': 'assets/img/rooms/deluxe_twin_03.jpg',
            'features': ['Mountain View', 'Best Value', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.5,
            'booking_code': 'Available',
            'category': 'deluxe-twin',
            'is_popular': False,
            'badge': 'value'
        }
    ]
    
    
    context = {
        'rooms': rooms_data,
        'total_rooms': len(rooms_data),
        'min_price': min(room['price'] for room in rooms_data),
        'max_price': max(room['price'] for room in rooms_data),
        'room_categories': ['Super Deluxe', 'Family Deluxe', 'Deluxe Twin']
    }
    
    return render(request, 'rooms.html', context)


def room_detail(request, room_id=None, room_slug=None):
    rooms_data = {
        1: {
            'id': 1,
            'slug': 'super-deluxe',
            'name': 'Super Deluxe Room',
            'price': 6500,
            'original_price': 6500,
            'capacity': 2,
            'bed_config': '1 Bed',
            'size': '45 sq m',
            'view_type': 'lake_mountain',
            'description': 'Experience luxury with panoramic views of Begnas Lake and Himalayas. Features modern amenities, comfortable seating area, and private balcony.',
            'image': 'assets/img/rooms/super_deluxe_06.jpg',
            'features': ['Lake View', 'Most Popular', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.9,
            'booking_code': 'Available',
            'category': 'super-deluxe',
            'is_popular': True,
            'badge': 'popular',
            'detailed_description': 'The Super Deluxe Room at Himalaya Forest Resort offers an unparalleled luxury experience with stunning 360-degree panoramic views of Begnas Lake, Rupa Lake, and the majestic Annapurna, Dhaulagiri, and Manaslu mountain ranges. This room features a private SPA bath/Jacuzzi, premium amenities, and a spacious balcony to enjoy the breathtaking Himalayan sunrise.',
            'included_services': ['Continental Breakfast', 'Free Parking', 'Free WiFi', '24/7 Room Service', 'Daily Housekeeping'],
            'additional_info': {
                'check_in': '24 hours available',
                'check_out': '24 hours available',
                'cancellation': 'Free cancellation up to 48 hours before check-in',
                'pets': 'Allowed on request (no extra charges)',
                'children': 'Children of all ages welcome',
                'smoking': 'Non-smoking room'
            },
            'gallery_images': [
                'assets/img/rooms/super_deluxe_02.jpg',
                'assets/img/rooms/super_deluxe_03.jpg',
                'assets/img/rooms/super_deluxe_05.jpg',
                'assets/img/rooms/super_deluxe_04.jpg',

                
            ]
        },
        2: {
            'id': 2,
            'slug': 'family-deluxe',
            'name': 'Family Deluxe Room',
            'price': 5500,
            'original_price': 5500,
            'capacity': 3,
            'bed_config': '2 Beds',
            'size': '50 sq m',
            'view_type': 'lake_mountain',
            'description': 'Spacious accommodation perfect for families. Features connecting rooms option, kid-friendly amenities, and garden access.',
            'image':  'assets/img/rooms/family_deluxe_02.jpg',
            'features': ['Lake View', 'Family Friendly', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.7,
            'booking_code': 'Available',
            'category': 'family-deluxe',
            'is_popular': False,
            'badge': 'family',
            'detailed_description': 'Perfect for families seeking comfort and space, our Family Deluxe Room offers ample room for up to 3 guests with two comfortable beds. Enjoy stunning views of both the lakes and mountains from your private terrace. The room includes all premium amenities with special attention to family needs.',
            'included_services': ['Continental Breakfast', 'Free Parking', 'Free WiFi', '24/7 Room Service', 'Daily Housekeeping'],
            'additional_info': {
                'check_in': '24 hours available',
                'check_out': '24 hours available',
                'cancellation': 'Free cancellation up to 48 hours before check-in',
                'pets': 'Allowed on request (no extra charges)',
                'children': 'Children of all ages welcome',
                'smoking': 'Non-smoking room'
            },
            'gallery_images': [
               'assets/img/rooms/family_deluxe_01.jpg',
               'assets/img/rooms/family_deluxe_03.jpg',
               'assets/img/rooms/family_deluxe_04.jpg',
               'assets/img/rooms/family_deluxe_05.jpg',



            ]
        },
        3: {
            'id': 3,
            'slug': 'deluxe-twin',
            'name': 'Deluxe Twin Room',
            'price': 4500,
            'original_price': 4500,
            'capacity': 2,
            'bed_config': '2 Beds',
            'size': '40 sq m',
            'view_type': 'mountain',
            'description': 'Perfect for friends or colleagues. Features twin beds, comfortable workspace, and stunning mountain views.',
            'image': 'assets/img/rooms/deluxe_twin_03.jpg',
            'features': ['Mountain View', 'Best Value', 'SPA Bath'],
            'amenities': ['Air Conditioning', 'Heating', 'Fan', 'Mountain View', 'Balcony', 'Terrace', 'SPA Bath/Jacuzzi', 'Bathrobes', 'Free Toiletries', 'Bidet', 'Shower', 'Tea/Coffee Maker', 'Electric Kettle', 'Dining Area', 'Work Desk', 'Television', 'Safe'],
            'rating': 4.5,
            'booking_code': 'Available',
            'category': 'deluxe-twin',
            'is_popular': False,
            'badge': 'value',
            'detailed_description': 'Our Deluxe Twin Room offers excellent value with two comfortable beds, perfect for friends traveling together or colleagues on business. Enjoy direct views of the Annapurna mountain range from your private balcony. This room includes all standard luxury amenities at an affordable price.',
            'included_services': ['Continental Breakfast', 'Free Parking', 'Free WiFi', '24/7 Room Service', 'Daily Housekeeping'],
            'additional_info': {
                'check_in': '24 hours available',
                'check_out': '24 hours available',
                'cancellation': 'Free cancellation up to 48 hours before check-in',
                'pets': 'Allowed on request (no extra charges)',
                'children': 'Children of all ages welcome',
                'smoking': 'Non-smoking room'
            },
            'gallery_images': [
                'assets/img/rooms/deluxe_twin_01.jpg',
                'assets/img/rooms/deluxe_twin_04.jpg',
                'assets/img/rooms/deluxe_twin_05.jpg',
                'assets/img/rooms/deluxe_twin_06.jpg',




               
            ]
        }
    }
    
    room = None
    if room_id and room_id in rooms_data:
        room = rooms_data[room_id]
    elif room_slug:
        for r_id, r_data in rooms_data.items():
            if r_data['slug'] == room_slug:
                room = r_data
                break
    
    if not room:
        from django.shortcuts import redirect
        return redirect('rooms')
    
    context = {
        'room': room,
        'related_rooms': [r for r_id, r in rooms_data.items() if r_id != room['id']][:2]
    }
    
    return render(request, 'room_detail.html', context)


def booking(request):
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'assets', 'img', 'logo.png')
    room_types = {
        'super_deluxe': {
            'name': 'Super Deluxe Room',
            'price': 'NPR 6,500',
            'per_night': 'per night',
            'capacity': '2 Guests',
            'bed': '1 King Bed',
            'description': 'Luxurious room with spa bath/jacuzzi, mountain views, and private balcony',
            'features': ['Spa Bath/Jacuzzi', 'Mountain View', 'Private Balcony', 'Free WiFi', 'Air Conditioning']
        },
        'family_deluxe': {
            'name': 'Family Deluxe Room',
            'price': 'NPR 5,500',
            'per_night': 'per night',
            'capacity': '3 Guests',
            'bed': '2 Beds',
            'description': 'Spacious family room perfect for small families or groups',
            'features': ['Two Beds', 'Mountain View', 'Private Bathroom', 'Free WiFi', 'Tea/Coffee Maker']
        },
        'deluxe_twin': {
            'name': 'Deluxe Twin Room',
            'price': 'NPR 4,500',
            'per_night': 'per night',
            'capacity': '2 Guests',
            'bed': '2 Twin Beds',
            'description': 'Comfortable room with two separate beds and beautiful views',
            'features': ['Two Twin Beds', 'Lake View', 'Private Bathroom', 'Free WiFi', 'Work Desk']
        }
    }
    
    resort_info = {
        'name': 'Himalaya Forest Resort',
        'address': 'Pachabhaiya (Pokhara Metropolitan Ward No. 31), Pokhara, Nepal 33700',
        'phone': '+977 9856081271',
        'whatsapp': '+977 9856081271',
        'email': 'himalayaforestresort@gmail.com',
        'check_in': '2:00 PM',
        'check_out': '12:00 PM',
        'reception': '24/7'
    }
    
    form_submitted = False
    booking_data = {}
    
    if request.method == 'POST':
        arrival_date = request.POST.get('arrival_date', '').strip()
        departure_date = request.POST.get('departure_date', '').strip()
        guest_count = request.POST.get('guest_count', '').strip()
        room_count = request.POST.get('room_count', '').strip()
        room_type = request.POST.get('room_type', '').strip()
        special_requests = request.POST.get('special_requests', '').strip()
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        newsletter = request.POST.get('newsletter') == 'on'
        terms = request.POST.get('terms') == 'on'
        
        errors = []
        
        if not arrival_date:
            errors.append('Arrival date is required')
        if not departure_date:
            errors.append('Departure date is required')
        if not guest_count:
            errors.append('Number of guests is required')
        if not room_count:
            errors.append('Number of rooms is required')
        if not room_type:
            errors.append('Room type is required')
        if not full_name:
            errors.append('Full name is required')
        if not email:
            errors.append('Email is required')
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append('Please enter a valid email address')
        if not phone:
            errors.append('Phone number is required')
        if not terms:
            errors.append('You must agree to the terms and conditions')
        
        if arrival_date and departure_date:
            try:
                arrival = datetime.strptime(arrival_date, '%Y-%m-%d')
                departure = datetime.strptime(departure_date, '%Y-%m-%d')
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                
                if arrival < today:
                    errors.append('Arrival date cannot be in the past')
                if departure <= arrival:
                    errors.append('Departure date must be after arrival date')
            except ValueError:
                errors.append('Invalid date format')
        
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                arrival = datetime.strptime(arrival_date, '%Y-%m-%d')
                departure = datetime.strptime(departure_date, '%Y-%m-%d')
                nights = (departure - arrival).days
                
                room_name = room_types.get(room_type, {}).get('name', 'Deluxe Twin Room')
                
                import random
                import string
                booking_ref = f"HFR-{''.join(random.choices(string.digits, k=6))}"
                
                booking_data = {
                    'booking_reference': booking_ref,
                    'arrival_date': arrival.strftime('%B %d, %Y'),
                    'departure_date': departure.strftime('%B %d, %Y'),
                    'nights': nights,
                    'guest_count': guest_count,
                    'room_count': room_count,
                    'room_type': room_name,
                    'special_requests': special_requests if special_requests else 'No special requests',
                    'full_name': full_name,
                    'email': email,
                    'phone': phone,
                    'country': country if country else 'Not specified',
                    'newsletter': 'Yes' if newsletter else 'No',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'ip_address': request.META.get('REMOTE_ADDR', 'N/A'),
                    'resort_name': resort_info['name'],
                    'resort_phone': resort_info['phone'],
                    'resort_email': resort_info['email'],
                    'resort_address': resort_info['address'],
                    'check_in_time': resort_info['check_in'],
                    'check_out_time': resort_info['check_out'],
                }
                
                resort_context = booking_data.copy()
                user_context = booking_data.copy()
                
                resort_email_subject = f'Booking Request - {full_name} - {booking_data["arrival_date"]}'
                resort_email_body = render_to_string('emails/booking_to_resort.html', resort_context)
                
                user_email_subject = f'Booking Request Received - {booking_ref}'
                user_email_body = render_to_string('emails/booking_to_user.html', user_context)
                
                resort_email = EmailMessage(
                    subject=resort_email_subject,
                    body=resort_email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.DEFAULT_FROM_EMAIL],
                    reply_to=[email]
                )
                resort_email.content_subtype = "html"
                resort_email.send()
                
                user_email = EmailMessage(
                    subject=user_email_subject,
                    body=user_email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email],
                )
                user_email.content_subtype = "html"
                user_email.send()
                
                form_submitted = True
                
                messages.success(request, f'Thank you {full_name}! Your booking request has been submitted. Reference: {booking_ref}')
                
                context = {
                    'room_types': room_types,
                    'resort_info': resort_info,
                    'form_submitted': form_submitted,
                    'booking_data': booking_data,
                    'page_title': 'Book Your Stay | Himalaya Forest Resort, Pokhara',
                    'meta_description': 'Book your luxurious stay at Himalaya Forest Resort in Pokhara. Enjoy stunning views of Begnas Lake and Rupa Lake with our easy online booking system.',
                    'meta_keywords': 'Book Hotel, Resort Booking, Online Reservation, Pokhara Stay, Nepal Hotel Booking, Luxury Resort Booking',
                }
                
                return render(request, 'booking.html', context)
                
            except Exception as e:
                print(f"Booking email error: {e}")
                messages.error(request, 'There was an error processing your booking. Please try again or contact us directly.')
    
    context = {
        'room_types': room_types,
        'resort_info': resort_info,
        'form_submitted': form_submitted,
        'booking_data': booking_data,
        'page_title': 'Book Your Stay | Himalaya Forest Resort, Pokhara',
        'meta_description': 'Book your luxurious stay at Himalaya Forest Resort in Pokhara. Enjoy stunning views of Begnas Lake and Rupa Lake with our easy online booking system.',
        'meta_keywords': 'Book Hotel, Resort Booking, Online Reservation, Pokhara Stay, Nepal Hotel Booking, Luxury Resort Booking',
    }
    
    return render(request, 'booking.html', context)
