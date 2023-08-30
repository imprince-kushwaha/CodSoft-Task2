$(function() {
	$('[data-toggle="tooltip"]').tooltip();
  })



  function validateForm(){
    let x=document.forms["contactform"][usernamepart].value;
    let y=document.forms["contactform"][emailpart].value;
    let z=document.forms["contactform"][phonepart].value;
    let a=document.forms["contactform"][textareapart].value;
    if(x=="" || y=="" || z=="" || a==""){
      alert("this field is required");
      return false;
    }
  }

  
