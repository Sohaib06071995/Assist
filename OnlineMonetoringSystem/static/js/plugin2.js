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
          $('#user_account_table2 tbody').html(data.control_panel);
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
  $(".show-form2").click(ShowForm);
  $('#modal-user').on("submit",".register_activity",SaveForm);
//update
$('#user_account_table2').on("click",".show-form-delete2",ShowForm);
$('#modal-user').on("submit",".delete_activity",SaveForm);
});
