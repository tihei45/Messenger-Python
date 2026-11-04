registerPage = document.getElementById("register")


registerPage.addEventListener("click", async()=>{
    window.location.href = "/register"


})


login = document.getElementById("submitLogin")
login.addEventListener("click", function(){
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;


   if (username.trim() && password.trim()){
    fetch(`/login`,{
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
        if (text =="Erfolgreich Angemeldet"){
            window.location.href = "/"
        }
        else if(text =="Falsches Passwort eingegeben"){
        document.getElementById("password").value = "";
        }
        
    });
}

})
