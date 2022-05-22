downloadtxt=_=>{
	document.getElementById("downButTxt").innerHTML="wip";
}

document.addEventListener("DOMContentLoaded",_=>{
	const button_root=document.getElementsByClassName("slider")[0];
	const slide_root=document.getElementsByClassName("slides")[0];
	let index=0;
	let interval_handle;
	let pause_handle;
	let widths=[];
	restart_slides=_=>{
		interval_handle=setInterval(_=>{
			if (index==widths.length-1){
				slide_root.scroll(0,0);
				index=0;
			}
			else{
				slide_root.scrollBy(widths[index][0],0);
				index+=1;
			}
		},3000);
	}
	pause_slides=(evt)=>{
		clearInterval(interval_handle);
		clearTimeout(pause_handle);
		index=evt.target._idx;
		slide_root.scroll(widths[index][1],0);
		pause_handle=setTimeout(restart_slides,500);
	}
	let sum=0;
	slide_root.childNodes.forEach((e,i)=>{
		if (e.tagName=="SPAN"){
			let btn=document.createElement("a");
			btn.onclick=pause_slides;
			btn._idx=widths.length;
			button_root.appendChild(btn);
			let w=e.getBoundingClientRect().width;
			widths.push([w,sum]);
			sum+=w;
		}
	});
	restart_slides();
});
