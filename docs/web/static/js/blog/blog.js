;
var blog_search_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".search_wrap .do-search").click( function(){


            var search = $(".search_wrap input[name=search]").val();


            $.ajax({
                url:common_ops.buildUrl("/blog/search"),
                type:'POST',
                data:{ 'search':search},
                dataType:'json',
                success:function(res){

                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            path="/blog/search?search="+search
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
    blog_search_ops.init();
} );