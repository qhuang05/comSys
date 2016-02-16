
$(document).ready(function(){
    //用户名校验
    $("#username").blur(function(){
        var re_username =/\w+/g;
        var username = $("#username").val();
        if (re_username.test(username)) {
            $(".usernameBox span").text("");
        }
        else {
            $(".usernameBox span").text("用户名只能包含英文,字母,下划线且不能为空");
        }
    });

    //密码校验
    $("#password").blur(function(){
        var re_pwd =/\w+/g;
        var pwd = $("#password").val();
        if (re_pwd.test(pwd)) {
            $(".passwordBox span").text("");
        }
        else {
            $(".passwordBox span").text("密码只能包含英文,字母,下划线且不能为空");
        }
    });

    //邮箱校验
    $("#email").blur(function(){
        var re_mail =/^\w+@[a-z0-9]+\.[a-z]+$/g;
        //var re_mail = /\S/g;
        var mail = $("#email").val();
        if (re_mail.test(mail)) {
            $(".emailBox span").text("");
            //alert("合法的邮箱");
        }
        else {
            $(".emailBox span").text("请输入合法的邮箱");
            //alert("不合法的邮箱");
        }
    });

    // 验证手机号码
    $("#phonenum").blur(function(){
        var re_phone = /[1-9]\d{10}/i;
        var phone = $("#phonenum").val();
        if (re_phone.test(phone)) {
            $(".phoneBox span").text("")
        }
        else {
            $(".phoneBox span").text("请输入11位正确的手机号码");
        }
    });
});

// 提交注册表单信息之前检查填写的信息是否符合要求
function regCheck(){
    var oForm = document.getElementById('regForm');
    var oSpan = oForm.getElementsByTagName('span');
    var flag = 0;
    for(var i=0; i<oSpan.length; i++) {
        //alert(oSpan[i].innerHTML);
        if(oSpan[i].innerHTML != '') {
            flag =0;
            break;
        }
        else {
            flag =1;
        }
    }
    if(flag==0){
        //alert('无法提交');
        return false;
    }
    else{
        //alert('注册成功');
        return true;
    }
}

