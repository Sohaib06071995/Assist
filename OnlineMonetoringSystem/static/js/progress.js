$(document).ready(function(){
  var ShowForm = function(){
    var btn = $(this);

    $.ajax({
      url: btn.attr("data-url"),
      // url: 'register/',
      type: 'get',
      dataType: 'Json',
      beforeSend: function(){
        $('#modal-user1').modal('show');
      },
      success: function(data){
        $('#modal-user1 .modal-content').html(data.html_form);
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
          $('#user_account_tablep tbody').html(data.control_panel);
          $('#modal-user1').modal('hide');
          var elem = document.getElementById("myBar");
          elem.style.width = data.width + '%';
          elem.textContent = data.width+"%";


      } else{
            $('modal-user1 .modal-content').html(data.html_form)
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
  $(".show-formm").click(ShowForm);
  $('#modal-user1').on("submit",".progress_create",SaveForm);
//update

});
