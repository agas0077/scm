$('#mentor-why-us').click(() => {
    const mentorDropdown = $('#header-mentor-dropdown')
    if (mentorDropdown.html() != 'Заявка уже подана') {
        mentorDropdown.addClass('get-started-btn');
        mentorDropdown.animate({ rotate: '40deg' }, 150)
        mentorDropdown.animate({ rotate: '-40deg' }, 150)
        mentorDropdown.animate({ rotate: '0deg' }, 150)
        window.setInterval(function () {
            mentorDropdown.animate({ rotate: '40deg' }, 200)
            mentorDropdown.animate({ rotate: '-40deg' }, 200)
            mentorDropdown.animate({ rotate: '0deg' }, 200)
        }, 5000);
    }
});