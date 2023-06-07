$('#mentor-why-us').click(() => {
    const mentorDropdown = $('#header-mentor-dropdown');
    const mobileMenu = $('.mobile-nav-toggle');

    if (mentorDropdown.html() != 'Заявка уже подана') {
        if ($(window).width() < 991) {
            mobileMenu.addClass('mobile-menu-btn');

            const intervalMenu = window.setInterval(function () {
                mobileMenu.animate({ rotate: '50deg' }, 300);
                mobileMenu.animate({ rotate: '-50deg' }, 300);
                mobileMenu.animate({ rotate: '0deg' }, 300);
            }, 2500);

            mobileMenu.click(() => {
                mobileMenu.removeClass('mobile-menu-btn');
                window.clearInterval(intervalMenu);
            });

        } else {

            mentorDropdown.addClass('mentor-btn');

            const intervalDropdown = window.setInterval(function () {
                mentorDropdown.animate({ rotate: '20deg' }, 300);
                mentorDropdown.animate({ rotate: '-20deg' }, 300);
                mentorDropdown.animate({ rotate: '0deg' }, 300);
            }, 2500);

            mentorDropdown.hover(() => {
                mentorDropdown.removeClass('mentor-btn');
                window.clearInterval(intervalDropdown);
            });
        }
    }
});