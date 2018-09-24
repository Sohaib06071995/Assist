$(document).ready(function(){
  var ShowForm = function(){
    var btn = $(this);

    $.ajax({
      url: btn.attr("data-url"),
      // url: 'register/',
      type: 'get',
      dataType: 'Json',
      beforeSend: function(){
        $('#modal-user').modal('show');
      },
      success: function(data){
        $('#modal-user .modal-content').html(data.html_form);
      }
    });
  };
  var SaveForm  = function(){
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      type: form.attr('method'),
      dataType: 'json',
      success: function(data){
        if(data.form_is_valid){
          $('#user_account_table tbody').html(data.control_panel);
          $('#modal-user').modal('hide');
          function doHide(){
		          document.getElementById( "success" ).style.display = "none" ;
	           }
          $(".content").show();
          setTimeout(function() {
            $(".content").fadeOut(4000);
    });
      } else{
            $('modal-user .modal-content').html(data.html_form)
        }
      }
    })
    function doHide1(){
        document.getElementById( "notsuccess" ).style.display = "none" ;
       }
    $(".content1").show();
    setTimeout(function() {
      $(".content1").fadeOut(5000);
});
    return false;

  }
  //create
  $(".show-form").click(ShowForm);
  $('#modal-user').on("submit",".register_user",SaveForm);
//update
  $('#user_account_table').on("click",".show-form-update",ShowForm);
  $('#modal-user').on("submit",".update_user",SaveForm);
//delete
  $('#user_account_table').on("click",".show-form-delete",ShowForm);
  $('#modal-user').on("submit",".delete_user",SaveForm);
});
