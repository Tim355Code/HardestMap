submitInfo=_=>{
	const submitButton=document.getElementsByClassName("submit-button")[0];
	submitButton.disabled = true;
	submitButton.style.opacity="0.6";
	if(submitButton.value=="Sign in"){
		submitButton.value="Signing in...";
	}else if(submitButton.value=="Create account"){
		submitButton.value="Creating account";
	}else{
		submitButton.value="Sending email";
	}
}