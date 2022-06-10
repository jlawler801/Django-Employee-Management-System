document.getElementById("button-addemployee").addEventListener('click', function() {
    document.querySelector('.bg-modal-addemployee').style.display ='flex'; 
});

document.querySelector('.close-addemployee').addEventListener('click', function() {
    document.querySelector('.bg-modal-addemployee').style.display = 'none';
});

document.getElementById("buutton-addemployeedeptt").addEventListener('click', function() {
    document.querySelector('.bg-modal-addemployeedeptt').style.display ='flex'; 
});

document.querySelector('.close-addemployeedeptt').addEventListener('click', function() {
    document.querySelector('.bg-modal-addemployeedeptt').style.display = 'none';
});

document.getElementById("button").addEventListener('click', function() {
    document.querySelector('.bg-modal').style.display ='flex'; 
});

document.querySelector('.close').addEventListener('click', function() {
    document.querySelector('.bg-modal').style.display = 'none';
});







//Submit post on submit




// document.getElementById('button').addEventListener('click', (e) => {
//     let url = 'http://127.0.0.1:8000/login/';
//     let other = window.open(url, 'myFrame');
    
    
    
    // setTimeout(()=>{
    //     var iframe = document.getElementById('button');
    //     var innerDoc = iframe.contentDocument || iframe.contentWindow.document;
    //     innerDoc.getElementById('myForm')
    //     }, 1000);

    // })


// document.getElementById('login-user').addEventListener('click', (e) =>{
//     e.defaultPrevented()
// })