
$(function () {

    $('#word').change(function () {
        $('#pwdmsg').html()
        pd = $('#word').val();
        $.getJSON('/app/pwdlogin/',{'p':pd},function (data) {
            if(data['stat'] == '200'){
                return true
            }else{
                $('#pwdmsg').html('密码错误').css('color','red')
            }
        })
    })
});
