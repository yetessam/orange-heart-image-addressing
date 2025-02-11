document.addEventListener('DOMContentLoaded', () => {
    // Check if navbar-burger elements exist
    const navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    if (navbarBurgers.length === 0) {
        console.error('No navbar-burger elements found');
        return;
    }

    // Check if target menu exists
    const targetMenu = document.getElementById('navbarMenu');
    if (!targetMenu) {
        console.error('No element with id "navbarMenu" found');
        return;
    }

    const isDesktop = () => window.innerWidth >= 1024; // Adjust this breakpoint as needed

    const setInitialMenuState = () => {
        try {
            if (isDesktop() && localStorage.getItem('navbar-menu-state') === 'active') {
                targetMenu.classList.add('is-active');
                navbarBurgers.forEach(el => el.classList.add('is-active'));
            } else {
                targetMenu.classList.remove('is-active');
                navbarBurgers.forEach(el => el.classList.remove('is-active'));
            }
        } catch (error) {
            console.error('Error setting initial menu state:', error);
        }
    };

    setInitialMenuState();

    // Add click event to toggle state
    navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {
            try {
                el.classList.toggle('is-active');
                targetMenu.classList.toggle('is-active');

                // Save the state to localStorage if on desktop
                if (isDesktop()) {
                    if (targetMenu.classList.contains('is-active')) {
                        localStorage.setItem('navbar-menu-state', 'active');
                    } else {
                        localStorage.removeItem('navbar-menu-state');
                    }
                }
            } catch (error) {
                console.error('Error toggling menu state:', error);
            }
        });
    });

    // Recheck the menu state on window resize
    window.addEventListener('resize', () => {
        try {
            setInitialMenuState();
        } catch (error) {
            console.error('Error rechecking menu state on resize:', error);
        }
    });
});
