
let container = document.querySelector('.container');


gsap.to('.elems',{
    x:"-400%",
    duration:17,
    repeat:-1,
    ease:"none",
})

document.getElementById("currentYear").textContent = new Date().getFullYear();

const take=document.querySelector("#taketoapply");
// Assuming `take` is the button element
take.addEventListener("click", function() {
    console.log("checked");
   var xhr = new XMLHttpRequest();
    xhr.open("GET", "/loanapply/", true);  
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              
                var responseData = (xhr.responseText);
                document.body.innerHTML = responseData;
                console.log(responseData);
            } else {
               
                console.error("Error:", xhr.status);
            }
        }
    };
    xhr.send();
});

