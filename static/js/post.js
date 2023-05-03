d$(document).ready(function(){
    setInterval(function () {
        $.ajax({
            type : 'GET',
            url : $('.comment-url').text(),
            success: function(response) {
                $('.comment').text('');
                for (var i = 0; i < response.comments.length; i++) {
                    var obj = response.comments[i],
                        date = new Date(obj.date);
                    var comment = '<h5>'+obj.comment_author+'</h5>';
                    comment += '<p>'+obj.comment_body+'</p>';
                    comment += '<div>'+date.toLocaleTimeString() + ' ' + date.toLocaleDateString()+'</div>';
                    $('.comment').append(comment);
                }

            }, 
            error: function(response) {
                console.log('An error occured while loading comments!')
            }
        })
    }, 1000);
});

$(document).on('submit', '#comment_form', function(event) {
    event.preventDefault();

    $.ajax({
        type:'POST',
        url : $('.comment-url').text(),
        data : {
            comment_body : $('#id_comment_body').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
        },
        success : function (data) {
            console.log('success');
        },

        error : function() {
            console.log('an error occured')
        }
    });
    $('#id_comment_body').val("");
});