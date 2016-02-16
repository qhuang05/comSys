
$(document).ready(function() {
	// 添加评论, Ajax
	$('#addCommentBtn').click(function () {
		var txt = $("#txt").val();
		$.post("/addComment", {txt: txt}, function (data, status) {
			if (status == 'success') {
				var _data = JSON.parse(data);
				var oP = "<p>" + _data.body + "</p>";
				var oSpan1 = "<span>评论者: " + _data.author + "</span>";
				var sTime = _data.time;
				var eTime = sTime.substring(0,sTime.length-7);
				var oSpan2 = "<span>时间: " + eTime + "</span>";
				var oBtn = "<button type='button' onclick='deleteme(" +(_data.id) + ",this)'>删除评论</button>"
				//var oBtn = "<button>删除评论</button>"
				var oLi ="<li class='comment-body'>"+oP+"<hr />"+oSpan1+oSpan2+"<br />"+oBtn+"</li>";
				//alert(oLi);
				$('#comment_items').prepend(oLi);
				console.log('后台传回的数值为：' + data + '\n' + '状态：' + status);
				//alert('评论成功!!!');
			}
			else {
				alert('您的评论在提交过程中出错了!!!');
			}
		});
	});

});

// 删除评论, Ajax
function deleteme(id,target) {
    //window.location.href = '/delComment?id='+id;
    //alert('Clicked the delete button...');
    var delID = id;
    $.ajax({
        // type: 'POST',
        url: '/delComment',
        data: {delID: id},
        success: function(data){
            if(data =='1'){
                //$(this).parent().remove();			//不能使用this，由于this的作用域不指向button这个元素
                $(target).parent().remove();
                //alert("删除成功!!!");
            }
            else{
                alert("您没有权限删除别人的评论!!!");
            }
        }
    });
}