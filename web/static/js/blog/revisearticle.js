;
var blog_reviseariticl_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".revisearticle-wrap .do-modify").click( function(){

            var btn_target = $(this);
            var articleid = $(this).attr("value");


            $.ajax({
                url:common_ops.buildUrl("/blog/postblog"),
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

          $(".revisearticle-wrap .do-delete").click( function(){



              var articleid = $(this).attr("value");
              that.ops( "remove",articleid );



        } );
    },
     ops:function( act,id ){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl( "/blog/authordelete" ),
                    type:'POST',
                    data:{
                        act:act,
                        id:id
                    },
                    dataType:'json',
                    success:function( res ){
                        var callback = null;
                        if( res.code == 200 ){
                            callback = function(){
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert( res.msg,callback );
                    }
                });
            },
            'cancel':null
        };
        common_ops.confirm( ( act == "remove" ? "确定删除？":"确定恢复？" ), callback );
    }


};

$(document).ready( function(){
    blog_reviseariticl_ops.init();
} );