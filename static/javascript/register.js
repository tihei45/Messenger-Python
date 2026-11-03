register = document.getElementById("submitRegister")

register.addEventListener("click", function(){
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;


   if (username.trim() && password.trim()){
    fetch(`/register`,{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username : username.trim(),
            password: password.trim()
        })
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(text) {
        alert(text);
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
    });
}

})


