document.addEventListener("DOMContentLoaded", () => {
    var cont = document.querySelector('.prac');
    list_cont = cont.querySelectorAll('.panel')
    for (i = 0; i < list_cont.length; i++){ //console.log(list_cont[i].id);
        var div = document.querySelector('#' + list_cont[i].id);
        var cont_checkbox = div.querySelectorAll('input[type ="checkbox"]');
        //console.log(list_cont[i].id,cont_checkbox.length)
        var cont_checked = div.querySelectorAll('input[type ="checkbox"]:checked');
        var prog = document.getElementById(list_cont[i].id.slice(0,-3) + 'bar') ;
        var ac = document.getElementById(list_cont[i].id.slice(0,-3) + 'count') ;
        ac.innerText = "("+ cont_checked.length+"/"+cont_checkbox.length+")" ;
        prog.setAttribute("value",cont_checked.length);
        prog.setAttribute("max",cont_checkbox.length); 

       }; 
            
});

// This function is for show/hide accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
    panel.style.display = "none";
    } else {
    panel.style.display = "block";
    }
});
} ;

var prac_div = document.querySelector('.prac');
var cont_checkbox = prac_div.querySelectorAll('input[type ="checkbox"]');
var len ;
for (j = 0; j < cont_checkbox.length; j++) {
    cont_checkbox[j].addEventListener("click",function(){
        if(this.checked){
            // it is checked. Do something
            var pop = this.parentElement.parentElement.parentElement.parentElement.parentElement.id;
            cont = document.getElementById(pop);
            len_checkbox = cont.querySelectorAll('input[type ="checkbox"]');
            len = cont.querySelectorAll('input[type ="checkbox"]:checked');
            var prog = document.getElementById(pop.slice(0,-3) + 'bar') ;
            var ac = document.getElementById(pop.slice(0,-3) + 'count') ;
            ac.innerText = "("+ len.length+"/"+len_checkbox.length+")" ;
            prog.setAttribute("value",len.length);
            prog.setAttribute("max",len_checkbox.length); 
            
        }
        else{
            // it isn't checked. Do something else
            var pop = this.parentElement.parentElement.parentElement.parentElement.parentElement.id;
            cont = document.getElementById(pop);
            len_checkbox = cont.querySelectorAll('input[type ="checkbox"]');
            len = cont.querySelectorAll('input[type ="checkbox"]:checked');
            var prog = document.getElementById(pop.slice(0,-3) + 'bar') ;
            var ac = document.getElementById(pop.slice(0,-3) + 'count') ;
            ac.innerText = "("+ len.length+"/"+len_checkbox.length+")" ;
            prog.setAttribute("value",len.length);
            prog.setAttribute("max",len_checkbox.length); 
        }})};