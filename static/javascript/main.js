
console.log("JS geladen");

const chatSidebar = document.querySelector(".chatContainer");
const textarea = document.getElementById("content");
const chatContainer = document.getElementsByClassName("messages")[0];
const main = document.querySelector("main");
let userList = [];
let currentChat = 1;

textarea.addEventListener("input", () => {
    textarea.style.height = "auto";

    if (textarea.scrollHeight > 300) {
        textarea.style.height = "300px";
        textarea.style.overflowY = "auto";
    } else {
        textarea.style.height = textarea.scrollHeight + "px";
        textarea.style.overflowY = "hidden";
    }
});

const submit = document.getElementById("submit");

submit.addEventListener("click", async () => {

    let message = textarea.value;

    if (message.trim()) {

        await fetch("/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                chatid: currentChat,
                content: message
            })
        });

        textarea.value = "";
        textarea.style.height = "50px";

        await loadMessages();

        main.scrollTop = main.scrollHeight;
    }
});

async function loadMessages() {

    let response = await fetch(`/messages/${currentChat}`);
    let messages = await response.json();

    chatContainer.innerHTML = "";

    for (let message of messages) {
        let messageClass = "other";
        if (message.userid == 1){
            messageClass = "own"
        }
            
        let html = `
        <div class="message ${messageClass}">
            <div class="sender">${message.username}</div>
            <div class="content">${message.content}</div>
            <div class="timestamp">${message.timestamp}</div>
        </div>
        `;

        chatContainer.insertAdjacentHTML("beforeend", html);
    }

    main.scrollTop = main.scrollHeight;
}

async function loadChats() {

    let response = await fetch("/chats");
    let chats = await response.json();

    chatSidebar.innerHTML = "";

    for (let chat of chats) {
        let activeClass="";
        if (chat.chatid == currentChat){
            activeClass="chatActive";
        }
        let html = `
        <div class="chat ${activeClass}" data-chatid="${chat.chatid}">
            <div class="chatName">${chat.chatname}</div>
        </div>
        `;

        chatSidebar.insertAdjacentHTML("beforeend", html);
    }

    const chatElements = document.querySelectorAll(".chat");

    for (let chat of chatElements) {

        chat.addEventListener("click", async () => {

            currentChat = chat.dataset.chatid;

            console.log("Chat gewechselt zu:", currentChat);

            await loadChats();
            await loadMessages();
        });
    }
}

async function init() {
    await loadChats();
    await loadMessages();
}

init();

const chatName = document.getElementById("chatName")
const openBtn = document.getElementById("createChat");
const exitBtn = document.getElementById("exitChat");
const submitBtn = document.getElementById("submitChat");
const modal = document.getElementById("modal");

openBtn.addEventListener("click", async () =>{
    let response = await fetch("/users");
    userList = await response.json();

    console.log(userList)
    modal.style.display="flex";

    chatName.focus();
});


const suggestionContainer = document.getElementById("suggestions")
const memberAdd = document.getElementById("memberAdd");

    memberAdd.addEventListener("input", () => {
        let memberList = memberAdd.value.split(",");
        let search = memberList[memberList.length - 1].trim();
        if (search.trim() === "") {
            suggestionContainer.innerHTML = "";
            return;
}
        let matches = userList.filter(user =>

        user.toLowerCase().includes(search.toLowerCase())
);


        suggestionContainer.innerHTML = "";
        for (let match of matches){
            let html = `
            <div class="match">
                ${match}
            </div>
            `;
            suggestionContainer.insertAdjacentHTML("beforeend", html);
        }
        if (matches.length === 0) {
        suggestionContainer.innerHTML = "";}

        const matchElements = document.querySelectorAll(".match");



        for (let matchElement of matchElements) {

            matchElement.addEventListener("click", () => {

                let memberList = memberAdd.value.split(",");

                memberList[memberList.length - 1] =
                    matchElement.textContent.trim();

                memberAdd.value = memberList.join(", ") + ", ";

                suggestionContainer.innerHTML = "";

                memberAdd.focus();
            });
        }
        console.log(matches);
});



exitBtn.addEventListener("click", () =>{
    modal.style.display="none"
    
    chatName.value=""
    document.getElementById("memberAdd").value = "";

});

submitBtn.addEventListener("click", async()=>{
    let chatName = document.getElementById("chatName").value;
    let user = document.getElementById("memberAdd").value
    console.log(chatName);

    let response = await fetch("/create-chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            chatname: chatName,
            user: user
        })
    })



    let data = await response.json();
    document.getElementById("chatName").value = "";
    document.getElementById("memberAdd").value = "";
    currentChat = data.chatid;
    await loadChats();
    await loadMessages();




    modal.style.display="none"

}

)

let anmelden = document.getElementById("loginFooter")
if (anmelden){
anmelden.addEventListener("click", async()=>{
    window.location.href = "/login"
})
}


let logout = document.getElementById("logout")
if (logout){
logout.addEventListener("click", async() => {
    let response = await fetch("/logout", {
        method: "POST"
    });

    console.log(response.status);

    window.location.href = "/";
});
}




setInterval(loadMessages, 2000);


