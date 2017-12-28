$(function(){
    var clientToken = $('#id_client_token').val();
    braintree.setup(clientToken, "dropin", {
      container: "payment-form"
       });
    });
       