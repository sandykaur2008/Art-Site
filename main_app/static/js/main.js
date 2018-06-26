$('button').on('click', function(event){ 
  event.preventDefault();
  var element = $(this);
  $.ajax({
          url : '/like_piece/',
          type : 'GET',
          data : { piece_id : element.attr("data-id")},
          success : function(response){
                      element.html(' ' + response);
                    }
  });
});
