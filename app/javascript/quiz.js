Array.prototype.forEach.call(document.getElementsByClassName("answer-button"), element => {
    element.addEventListener("click", function () {
        var text = this.textContent || this.innerText;
        console.log(text);
    });
});