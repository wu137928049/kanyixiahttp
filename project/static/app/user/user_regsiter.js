$(function () {
    //检测两次输入的密码是否一致
    //change:失去焦点和获取焦点都会触发  检测password2的状态
    $('#Password2').change(
        function () {
            //val:获取属性的值 ，也就是获取的是用户输入的密码
            p1 = $('#Password1').val();
            p2 = $('#Password2').val();
        //    判断两次输入的密码是否一致
            if(p1 == p2){
                $('#pwdmsg').html('输入正确').css('color','green');
            }else{
                $('#pwdmsg').html('两次密码不一致').css('color','red');
            }
        }
    )
});

//监听用户名是否可用

$(function () {

    $('#name').change(function () {

        user = $('#name').val();
        $.getJSON('/app/monitor/',{'name':user},function (data) {
            if(data['stat'] == '600'){
                $('#b').html('该用户名可用').css('color','green');
            }else{
                $('#b').html('用户以存在 请更换用户名').css('color','red')
            }
        })
    })
});
