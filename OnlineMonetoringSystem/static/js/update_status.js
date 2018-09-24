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

          $(".content").show();
          setTimeout(function() {
            $(".content").fadeOut(5000);
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

  $(".show-form-update1").click(".show_dashboard",SaveForm);

});
