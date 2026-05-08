var correct = 0;
var total = 0;

var image = document.getElementById("quiz-image");

function newQuestion() {
    image.src = "/images/Untitled1.jpg"
}

Array.prototype.forEach.call(document.getElementsByClassName("answer-button"), element => {
    element.addEventListener("click", function () {
        var text = this.textContent || this.innerText;
        var imageSrc = image.src;

        if (imageSrc.includes(text)) {
            correct += 1;
        }
        total += 1;

        console.log("current score: " + correct + " / " + total);

        newQuestion()
    });
});