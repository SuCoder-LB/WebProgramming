// let counter=0;

if(!localStorage.getItem('counter')){
  localStorage.setItem('counter',0);
}


function count(){
  let counter=localStorage.getItem('counter');
  counter++;

  const heading=document.querySelector('h1');
  heading.innerHTML=counter;
  localStorage.setItem('counter',counter);
  //alert(counter);
  if(counter%10===0) {
  //  alert(`count is now ${counter}`);
  }
}

document.addEventListener('DOMContentLoaded',function (){
  //document.querySelector('button').addEventListener('click',count);
  document.querySelector('button').onclick=count;
  document.querySelector('h1').innerHTML=localStorage.getItem('counter');


  setInterval(count,1000);
});