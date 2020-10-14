;
var blog_Verifypsw_ops = {
    init:function(){
        this.eventBind();


    },
    eventBind:function(){
        $(".article-wrap .do-verify").click( function(){


            var psw = $(".article-wrap input[name=password]").val();
            var articleid = $(".article-wrap input[name=articleid]").val();
            var zqpsw = $(".article-wrap input[name=zqpsw]").val();

            if(psw!=zqpsw)
            {
                common_ops.alert( "请输入正确的密码~~" );
                return;
            }




            $.ajax({
                url:common_ops.buildUrl("/blog/test"),
                type:'POST',
                data:{
                    'articleid':articleid

                },
                dataType:'json',
               success:function(res){
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){

                            path="/blog/verify?id="+articleid
                            window.location.href = common_ops.buildUrl(path);
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    }
};

$(document).ready( function(){
    blog_Verifypsw_ops.init();
} );