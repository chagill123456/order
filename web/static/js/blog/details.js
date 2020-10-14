;
var blog_details_ops = {
    init:function(){
        this.eventBind();
        var hits = $(".search_wrap input[name=search]").val();

    },
    eventBind:function(){
        $(".pinglun_wrap .do-pinglun").click( function(){
             var btn_target = $(this);

            var name = $(".pinglun_wrap input[name=nickname]").val();
            var pinglun = $(".pinglun_wrap textarea[name=comment]").val();
            var articleid = $(".article-wrap input[name=articleid]").val();


            $.ajax({
                url:common_ops.buildUrl("/blog/pinglunset"),
                type:'POST',
                data:{
                    'name':name,
                    'pinglun':pinglun,
                    'articleid':articleid

                },
                dataType:'json',
                success:function(res){
                    btn_target.addClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                          window.location.href = common_ops.buildUrl("/blog/details");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );

         $(".article-wrap .do-dianzan").click( function(){
             var btn_target = $(this);


            var dianzan = $(".article-wrap a[name=dianzan]").val();
            var articleid = $(".article-wrap input[name=articleid]").val();

             btn_target.addClass("disabled");
            $.ajax({
                url:common_ops.buildUrl("/blog/dianzanset"),
                type:'POST',
                data:{
                    'dianzan':dianzan,
                    'articleid':articleid

                },
                dataType:'json',
                success:function(res){
                    btn_target.addClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                          window.location.href =  window.location.href;
                        }
                    }

                }
            });
        } );
    }
};

$(document).ready( function(){
    blog_details_ops.init();
} );