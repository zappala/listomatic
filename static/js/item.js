$.fn.editable.defaults.mode = 'inline';

$(document).ready(function() {
    setup();
});

function setup() {
    $('.item-text').editable({'anim':0.2,'highlight':true});
    $('.item-due').editable({'anim':0.2,'type':'combodate'});
};

function del(id,search) {
    $.ajax({
        url: '/delete',
        type: 'POST',
        data: {id:id,search:search,submit:true},
        success: function (result) {
	    $('#item-list').html(result);
	    setup();
        }
    });  
};

function done(id,search) {
    $.ajax({
        url: '/done',
        type: 'POST',
        data: {id:id,search:search,submit:true},
        success: function (result) {
	    $('#item-list').html(result);
	    setup();
        }
    });  
};

function undo(id,search) {
    $.ajax({
        url: '/undo',
        type: 'POST',
        data: {id:id,search:search,submit:true},
        success: function (result) {
	    $('#item-list').html(result);
	    setup();
        }
    });  
};

$('#item-add').click(function() { 
    $.ajax({
        url: '/add',
        type: 'POST',
        data: {submit:true},
        success: function (result) {
	    $('#item-list').html(result);
	    setup();
        }
    });  
});

