document.addEventListener("DOMContentLoaded", function () {
    var ano = document.getElementById("ano");
    if (ano) { ano.textContent = new Date().getFullYear(); }
});