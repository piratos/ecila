// Credits goes to https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

$(function() {

    // When using HTTPS, use WSS too.
    var chat_zone = $("#chat_zone");
    
    showmsg = function(message) {
        var data = message['msg'];
        chat_zone.prepend(
            $("<p class='answer'></p>").text('ECILA: ' + data)
        );
    };

    $("#chat_form").on("submit", function(event) {

        try {
            var message_elem = $('#message');
            var message_val = message_elem.val();

            if (message_val) {
                // send message
                //$.get('http://192.168.187.128:5000/a/'+message_val).done(function(data){
                //    showmsg(data);
                //});
                $.ajax({
                       type: 'GET',
                       crossDomain: true,
                       dataType: 'jsonp',
                       jsonp: false,
                       url: 'http://main:5000/a/'+message_val,
                       success: function(data){
                            showmsg(data['msg']);
                       }
                    })
                message_elem.val('').focus();

                // Add the message to the chat
                chat_zone.prepend(
                    $("<p class='question'></p>").text('You: ' + message_val)
                );
            }
        }
        catch(err) {
            console.error(err.message);
        }

        return false;
    });
});
