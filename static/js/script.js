// Nav Bar
$(document).ready(function(){
    $('.sidenav').sidenav();
  });
// Flash Message Animation
$(document).ready(function() {
    const $messages = $('.flash-message');
    let delay = 0;
    
    $messages.each(function(index, message) {
        setTimeout(function() {
            $(message).addClass('show');
        }, delay);
        delay += 2000; // Adjust delay as needed
    });

    // Remove messages after they have been shown
    setTimeout(function() {
        $messages.each(function(index, message) {
            $(message).removeClass('show');
            setTimeout(function() {
                $(message).remove();
            }, 500); // Remove after animation
        });
    }, delay + 2000); // Adjust total time before removing messages

    // Handle close button clicks
    $('.close-btn').click(function() {
        const $message = $(this).closest('.flash-message');
        $message.addClass('hide');
        setTimeout(function() {
            $message.remove();
        }, 500); // Remove after animation
    });

   
});