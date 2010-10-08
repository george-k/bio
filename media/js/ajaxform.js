$(document).ready(function(){

    var options = {
        beforeSubmit: blockForm,
        success: processJson,
        type: 'post',
        dataType: 'json'
    };

    $("#contactform").ajaxForm(options);

    function processJson(data) {
        // alert(data);
        unblockForm();
        if(data.result == 'error') {
            formClean();
            for(var error in data.errors) {
                message = '<ul class="errorlist"><li>' +
                    data.errors[error] + '</li></ul>';
                $('#id_' + error).before(message);
            }
            $('#form_message').text(data.message);
            $('#form_message').addClass('message_error');
        }
        else if(data.result == 'ok') {
            formClean();
            $('#form_message').text(data.message);
            $('#form_message').addClass('message_ok');
        }
    }

    function formClean() {
        $('.errorlist').remove();
        $('#form_message').text('');
        $('#form_message').removeClass('message_error');
        $('#form_message').removeClass('message_ok');
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
