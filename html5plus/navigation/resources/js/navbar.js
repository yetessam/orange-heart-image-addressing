
      document.addEventListener('DOMContentLoaded', () => {
            const navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
            const targetMenu = document.getElementById('navbarBasicExample');

            const isDesktop = () => window.innerWidth >= 1024; // Adjust this breakpoint as needed

            const setInitialMenuState = () => {
                if (isDesktop() && localStorage.getItem('navbar-menu-state') === 'active') {
                    targetMenu.classList.add('is-active');
                    navbarBurgers.forEach(el => el.classList.add('is-active'));
                } else {
                    targetMenu.classList.remove('is-active');
                    navbarBurgers.forEach(el => el.classList.remove('is-active'));
                }
            };

            setInitialMenuState();

            // Add click event to toggle state
            navbarBurgers.forEach(el => {
                el.addEventListener('click', () => {
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
                });
            });

            // Recheck the menu state on window resize
            window.addEventListener('resize', () => {
                setInitialMenuState();
            });
        });
