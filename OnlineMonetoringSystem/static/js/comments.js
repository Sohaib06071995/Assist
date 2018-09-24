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
          $('#user_account_tablex tbody').html(data.control_panel);
          $('#post-text').val('');


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

  $('#user_account_table').on("click",".show-form-dashboard",ShowForm);
  $('#modal-user').on("submit",".show_dashboard",SaveForm);
  $('#user_account_table1').on("click",".show-form-dashboard1",ShowForm);
  $('#user_account_table3').on("click",".show-form-dashboard2",ShowForm);
  $(".show-form-dashboard2").click(ShowForm);

});
