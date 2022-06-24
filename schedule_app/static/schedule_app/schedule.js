let datebtn = document.querySelector('#submit');
    datebtn.addEventListener('click',function(){
    let during = document.getElementById("during").value;
    window.location.href = '/schedule_app/create?during='+during;
    }, false);

let placebtn = document.querySelectorAll('.btntest');

if(placebtn.length != 0){
    for(let i = 0; i < placebtn.length; i++){
    placebtn[i].addEventListener('click',function(e){
    const tour_id = document.getElementById("fk").value;
    let btn_value = e.target.value
    let place = document.getElementById("place"+btn_value).value;

    window.location.href = '/schedule_app/day?place='+place+'&fk='+tour_id+'&test='+btn_value+'&t=1';
    }, false);
  }
}