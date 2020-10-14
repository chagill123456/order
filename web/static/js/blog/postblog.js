;
var blog_post_ops = {
    init:function(){
        this.ue = null;
        this.eventBind();
        this.initEditor();


    },
    eventBind:function(){
        var that = this;
        $(".blogpost_wrap .save").click( function(){

            var heji_id_target = $(".blogpost_wrap select[name=heji_id]");
            var heji_id = heji_id_target.val();

            var name_target = $(".blogpost_wrap input[name=name]");
            var name = name_target.val();

            var biaoqian_id_target = $(".blogpost_wrap select[name=biaoqian_id]");
            var biaoqian_id = biaoqian_id_target.val();


            var articleid =$(".blogpost_wrap input[name=articleid]").val();

            var heji =$("#heji_id").find("option:selected").text();

            var jianjie =$(".blogpost_wrap textarea[name=jianjie]").val();

             var psw =$(".blogpost_wrap input[name=psw]").val();

             var summary = $.trim(that.ue.getPlainTxt());
             if (summary.length < 10) {
                common_ops.tip("请输入描述，并不能少于10个字符~~");
                return;
            }

            var data = {
                heji_id: heji_id,
                name: name,
                biaoqian_id: biaoqian_id,
                summary: summary,
                articleid:articleid,
                psw:psw,
                jianjie:jianjie,
                heji:heji

            };




            $.ajax({
                url:common_ops.buildUrl("/blog/postdetail"),
                type:'POST',
                data:data,
                dataType:'json',
               success:function(res){
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){

                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    },
    initEditor: function () {
        var that = this;
        that.ue = UE.getEditor('editor', {
            toolbars: [
                ['undo', 'redo', '|',
                    'bold', 'italic', 'underline', 'strikethrough', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', '|', 'rowspacingtop', 'rowspacingbottom', 'lineheight'],
                ['customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                    'directionalityltr', 'directionalityrtl', 'indent', '|',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                    'link', 'unlink'],
                ['imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                    'insertimage', 'insertvideo', '|',
                    'horizontal', 'spechars', '|', 'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']

            ],
            enableAutoSave: true,
            saveInterval: 60000,
            elementPathEnabled: false,
            maximumWords:60000,
            zIndex: 4,
            contextMenu:[],
            serverUrl: common_ops.buildUrl('/upload/ueditor')
        });
    }
};

$(document).ready( function(){
    blog_post_ops.init();
} );