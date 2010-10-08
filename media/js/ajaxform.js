$(document).ready(function(){

    var options = {
        beforeSubmit: blockForm,
        success: processJson,
        type: 'post',
        dataType: 'json'
    };

    $("#contactform").ajaxForm(options);

    function processJson(data) {
        unblockForm();
        if(data.result == 'error') {
            clean_errors();
            for(var error in data.errors) {
                message = '<ul class="errorlist"><li>'+
                    data.errors[error]+'</li></ul>';
                $('#id_'+error).before(message);
            }
            $('#save_error_message').text(data.errors.save_error);
            $('#errors_message').text(data.errors.errors_message);
        }
        else if(data.result == 'ok') {
            clean_errors();
        }
    }

    function clean_errors() {
        $('.errorlist').text('');
        $('#save_error_message').text('');
        $('#errors_message').text('');
    }

    function disable() {
        $(this).attr('disabled', 'true');
    }

    function blockForm() {
        $('#contactform').find('input').each(disable);
        $('#contactform').find('textarea').each(disable);
        $('#contactform').find('select').each(disable);
        img = '<img height="20" class="loading" src="/media/img/loading.gif">';
        $('#contactform').find('input[type="submit"]').after(img);
    }

    function enable() {
        $(this).attr('disabled', '');
    }

    function unblockForm() {
        $('#contactform').find('input').each(enable);
        $('#contactform').find('textarea').each(enable);
        $('#contactform').find('select').each(enable);
        $('.loading').remove();
    }
});
