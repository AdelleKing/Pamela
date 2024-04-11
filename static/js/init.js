(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('select').formSelect();

  }); // end of document ready
})(jQuery); // end of jQuery name space



//send the email 
const btn = document.getElementById('button');

document.getElementById('form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Sending...';

   const serviceID = 'service_io15uze';
   const templateID = 'test';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Send Email';
      alert('Sent!');
      
    }, (err) => {
      btn.value = 'Send Email';
      alert(JSON.stringify(err));
    });
});




