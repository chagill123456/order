;
var user_register_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".register_wrap .do-register").click( function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var username = $(".register_wrap input[name=username]").val();
            var nickname = $(".register_wrap input[name=nickname]").val();
            var password = $(".register_wrap input[name=password]").val();
            var confirm_password = $(".register_wrap input[name=confirm_password]").val();

            var email = $(".register_wrap input[name=email]").val();


            if( username == undefined || username.length < 1){
                common_ops.alert( "请输入正确的登录用户名~~" );
                return;
            }
            if( password == undefined || password.length < 1){
                common_ops.alert( "请输入正确的密码~~" );
                return;
            }
              if( password !=confirm_password){
                common_ops.alert( "两次密码录入不一致~~" );
                return;
            }

            btn_target.addClass("disabled");
            $.ajax({
                url:common_ops.buildUrl("/register"),
                type:'POST',
                data:{
                    'username':username,
                    'nickname':nickname,
                    'password':password,
                     'email':email

        },
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    }
};

$(document).ready( function(){
    user_register_ops.init();
} );