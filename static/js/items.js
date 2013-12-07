$('#item-add').click(function() { 
    $.ajax({
        url: '/add',
        type: 'POST',
        data: {submit:true}, // An object with the key 'submit' and value 'true;
        success: function (result) {
	    $('#item-list').html(result);
        }
    });  
});
