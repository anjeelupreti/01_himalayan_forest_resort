// Main loader functionality
document.addEventListener('DOMContentLoaded', function() {
    const pageLoader = document.getElementById('pageLoader');
    
    if (pageLoader) {
        // Hide loader when page fully loads (images, scripts, etc.)
        window.addEventListener('load', function() {
            setTimeout(function() {
                pageLoader.classList.add('hidden');
                
                // Remove from DOM after animation completes
                setTimeout(function() {
                    pageLoader.style.display = 'none';
                }, 500);
            }, 300);
        });
        
        // Only show loader for full page navigations, not for modal/gallery clicks
        document.addEventListener('click', function(e) {
            let target = e.target;
            
            // Don't trigger loader for these cases:
            if (
                // Gallery/lightbox elements
                target.closest('.glightbox') ||
                target.closest('[data-glightbox]') ||
                target.closest('.gallery-item') ||
                
                // Modal triggers
                target.closest('[data-bs-toggle="modal"]') ||
                target.closest('[data-toggle="modal"]') ||
                target.closest('.modal') ||
                
                // Form elements that don't navigate
                target.closest('form') ||
                target.closest('button[type="submit"]') ||
                
                // In-page anchors
                target.closest('a[href^="#"]') ||
                target.closest('a[href="javascript:;"]') ||
                target.closest('a[href=""]') ||
                
                // External links
                target.closest('a[target="_blank"]') ||
                
                // Already loading
                pageLoader.classList.contains('hidden') === false
            ) {
                return;
            }
            
            // Check if it's an internal link that navigates to a new page
            const link = target.closest('a');
            if (link && 
                link.href && 
                link.href.includes(window.location.origin) && 
                !link.href.includes('#') && 
                !link.target) {
                
                // Check if it's a different page (not current page)
                const currentPath = window.location.pathname;
                const linkPath = new URL(link.href).pathname;
                
                if (currentPath !== linkPath) {
                    pageLoader.classList.remove('hidden');
                    pageLoader.style.display = 'flex';
                }
            }
        });
        
        // Handle browser back/forward buttons
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                pageLoader.classList.add('hidden');
                pageLoader.style.display = 'none';
            }
        });
        
        // Add no-loader class to gallery and modal elements
        setTimeout(function() {
            const galleryItems = document.querySelectorAll('.glightbox, [data-glightbox], .gallery-item');
            const modalTriggers = document.querySelectorAll('[data-bs-toggle="modal"], [data-toggle="modal"]');
            
            galleryItems.forEach(item => {
                item.classList.add('no-loader');
            });
            
            modalTriggers.forEach(item => {
                item.classList.add('no-loader');
            });
        }, 100);
    }
});

// Manual loader control functions (optional - for AJAX calls)
function showLoader() {
    const pageLoader = document.getElementById('pageLoader');
    if (pageLoader) {
        pageLoader.classList.remove('hidden');
        pageLoader.style.display = 'flex';
    }
}

function hideLoader() {
    const pageLoader = document.getElementById('pageLoader');
    if (pageLoader) {
        setTimeout(function() {
            pageLoader.classList.add('hidden');
            setTimeout(function() {
                pageLoader.style.display = 'none';
            }, 500);
        }, 300);
    }
}

// Prevent loader from showing on hash changes (in-page navigation)
window.addEventListener('hashchange', function() {
    const pageLoader = document.getElementById('pageLoader');
    if (pageLoader) {
        pageLoader.style.display = 'none';
        pageLoader.classList.add('hidden');
    }
});

// Initialize GLightbox with loader prevention
document.addEventListener('DOMContentLoaded', function() {
    if (typeof GLightbox !== 'undefined') {
        const lightbox = GLightbox({
            selector: '.glightbox',
            touchNavigation: true,
            loop: true,
            autoplayVideos: true,
            onOpen: () => {
                // Ensure loader doesn't show when lightbox opens
                const pageLoader = document.getElementById('pageLoader');
                if (pageLoader) {
                    pageLoader.style.display = 'none';
                    pageLoader.classList.add('hidden');
                }
            }
        });
    }
});