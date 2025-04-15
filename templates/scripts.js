document.getElementById("menuButton").addEventListener("click", function() {
    document.getElementById("menu").classList.toggle("hidden");
});

function showRegistrationForm() {
    document.getElementById("registrationForm").classList.toggle("hidden");
}

function submitForm(event) {
    event.preventDefault();
    alert("درخواست شما برای تأیید ارسال شد!");
    document.getElementById("registrationForm").classList.add("hidden");
}

document.getElementById('menuButton').addEventListener('click', function() {
    var menu = document.getElementById('menu');
    menu.classList.toggle('hidden');
});

function filterBakeries(type) {
    let items = document.querySelectorAll('.bakery-item');
    items.forEach(item => {
        item.style.display = "none";
        if (item.dataset.type === type || type === "all") {
            item.style.display = "block";
        }
    });
}

function searchBakeries() {
    let input = document.getElementById('search').value.toLowerCase();
    let items = document.querySelectorAll('.bakery-item');
    items.forEach(item => {
        let title = item.querySelector('h2').innerText.toLowerCase();
        if (title.includes(input)) {
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}



function showCustomCakeForm() {
    document.getElementById("customCakeForm").classList.toggle("hidden");
}

function selectDesign(image) {
    document.getElementById('preview').innerHTML = `<img src="${image}" class="w-32 h-32 object-cover rounded-lg">`;
}

function submitCakeOrder(event) {
    event.preventDefault();
    let filling = document.getElementById("filling").value;
    let coating = document.getElementById("coating").value;
    let preview = document.getElementById("preview").innerHTML;
    
    if (!preview.includes("img")) {
        alert("لطفاً یک طرح انتخاب کنید!");
        return;
    }
    
    alert(`سفارش شما با فیلینگ ${filling} و روکش ${coating} ثبت شد!`);
    document.getElementById("customCakeForm").classList.add("hidden");
}