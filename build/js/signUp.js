valid_email=_=>{
	let input=document.getElementById('mail').value;
	input=input.toLowerCase();
	let data;
	for(i=0;i<data.length;i++){
		if(data[i].toLowerCase().includes(input)){

		}
	}
}

document.addEventListener("DOMContentLoaded",_=>{
	const form=document.getElementsByClassName("information")[0];
	const offsetx = form.getBoundingClientRect().width;
	const offsety = form.getBoundingClientRect().height;
	let purple=document.getElementsByClassName("purple")[0];
	purple.style.boxShadow=`-${offsetx/2}px ${offsety+form.getBoundingClientRect().top}px 100px 100px`;
	const pink=document.getElementsByClassName("pink")[0];
	pink.style.boxShadow=`${offsetx/2}px ${form.getBoundingClientRect().top}px 100px 100px`;
	const blue=document.getElementsByClassName("blue")[0];
	blue.style.boxShadow=`0 ${offsety/2+form.getBoundingClientRect().top}px 100px 100px`;
});