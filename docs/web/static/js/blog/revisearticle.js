;
var blog_reviseariticl_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".revisearticle-wrap .do-modify").click( function(){


            var articleid = $(".revisearticle-wrap input[name=articleid]").val();


            $.ajax({
                url:common_ops.buildUrl("/blog/author"),
                type:'POST',
                data:{ 'articleid':articleid},
                dataType:'json',
                success:function(res){

                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            path="/blog/postblog?id="+articleid
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
    blog_reviseariticl_ops.init();
} );