
document.addEventListener('DOMContentLoaded', function() {
    const pageLoader = document.getElementById('pageLoader');
    
    if (pageLoader) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                pageLoader.classList.add('hidden');
                
                setTimeout(function() {
                    pageLoader.style.display = 'none';
                }, 500); 
            }, 500);
        });
        
        window.addEventListener('beforeunload', function() {
            pageLoader.classList.remove('hidden');
            pageLoader.style.display = 'flex';
        });
    }
});


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

document.addEventListener('click', function(e) {
    const target = e.target.closest('a');
    if (target && target.href && target.href.includes(window.location.origin) && 
        !target.href.includes('#') && !target.target) {
        const pageLoader = document.getElementById('pageLoader');
        if (pageLoader) {
            pageLoader.classList.remove('hidden');
            pageLoader.style.display = 'flex';
        }
    }
});