let timeLeft = document.querySelector(".time-left");
let quizContainer = document.getElementById("container");
let nextBtn = document.getElementById("next-button");
let countOfQuestion = document.querySelector(".number-of-question");
let displayContainer = document.getElementById("display-container");
let scoreContainer = document.querySelector(".score-container");
let restart = document.getElementById("restart");
let userScore = document.getElementById("user-score");
let startScreen = document.querySelector(".start-screen");
let startButton = document.getElementById("start-button");
const difficultySelect = document.getElementById('difficulty-select');
const submitButton = document.getElementById('submit-language');
let questionCount;
let scoreCount = 0;
let count = 11;
let countdown;
let text1;
let text2;
let text3;

let quizArray = [];

function createQuizQuestion(id, translatedText, options, correctAnswer) {
  return {
    id,
    question: translatedText,
    options,
    correct: correctAnswer,
  };
}

const options1 = ["7", "8", "9", "10"];
const correctAnswer1 = "8";

const options2 = ["1", "2", "3", "4"];
const correctAnswer2 = "2";

const options3 = ["7", "8", "9", "10"];
const correctAnswer3 = "7";

fetch('/translateText')
  .then(response => response.json())
  .then(translatedTexts => {
    const text1 = translatedTexts[0]; 
    console.log('Translated Text 1:', text1);
  
    const question1 = createQuizQuestion("0", text1, options1, correctAnswer1);
    quizArray.push(question1);
  })
  .catch(error => {
    console.error('Error fetching translation for Question 1:', error);
  });

fetch('/translateText1')
  .then(response => response.json())
  .then(translatedTexts => {
    const text2 = translatedTexts[0]; 
    console.log('Translated Text 2:', text2);
    const question2 = createQuizQuestion("1", text2, options2, correctAnswer2);
    quizArray.push(question2);
  })
  .catch(error => {
    console.error('Error fetching translation for Question 2:', error);
  });


fetch('/translateText2')
  .then(response => response.json())
  .then(translatedTexts => {
    const text3 = translatedTexts[0]; 
    console.log('Translated Text 3:', text3);
    const question3 = createQuizQuestion("2", text3, options3, correctAnswer3);
    quizArray.push(question3);
  })
  .catch(error => {
    console.error('Error fetching translation for Question 3:', error);
  });

restart.addEventListener("click", () => {
    initial();
    displayContainer.classList.remove("hide");
    scoreContainer.classList.add("hide");
});

nextBtn.addEventListener(
    "click",
    (displayNext = () => {
        questionCount += 1;
        if (questionCount == quizArray.length) {
            displayContainer.classList.add("hide");
            scoreContainer.classList.remove("hide");
            userScore.innerHTML =
                "Your score is " + scoreCount + " out of " + questionCount;
        } else {
            // Display questionCount
            countOfQuestion.innerHTML =
                questionCount + 1 + " of " + quizArray.length + " Question";
            // Display quiz
            quizDisplay(questionCount);
            count = 11;
            clearInterval(countdown);
            timerDisplay();
        }
    })
);

const timerDisplay = () => {
    countdown = setInterval(() => {
        count--;
        timeLeft.innerHTML = `${count}s`;
        if (count == 0) {
            clearInterval(countdown);
            displayNext();
        }
    }, 1000);
};

const quizDisplay = (questionCount) => {
    let quizCards = document.querySelectorAll(".container-mid");

    quizCards.forEach((card) => {
        card.classList.add("hide");
    });
    quizCards[questionCount].classList.remove("hide");
};


function quizCreator() {
    quizArray.sort(() => Math.random() - 0.5);
    for (let i of quizArray) {
        i.options.sort(() => Math.random() - 0.5);
        let div = document.createElement("div");
        div.classList.add("container-mid", "hide");
        countOfQuestion.innerHTML = 1 + " of " + quizArray.length + " Question";
        let question_DIV = document.createElement("p");
        question_DIV.classList.add("question");
        question_DIV.innerHTML = i.question;
        div.appendChild(question_DIV);
        div.innerHTML += `
    <button class="option-div" onclick="checker(this)">${i.options[0]}</button>
     <button class="option-div" onclick="checker(this)">${i.options[1]}</button>
      <button class="option-div" onclick="checker(this)">${i.options[2]}</button>
       <button class="option-div" onclick="checker(this)">${i.options[3]}</button>
    `;
        quizContainer.appendChild(div);
    }
}

function checker(userOption) {
    let userSolution = userOption.innerText;
    let question =
        document.getElementsByClassName("container-mid")[questionCount];
    let options = question.querySelectorAll(".option-div");
    if (userSolution === quizArray[questionCount].correct) {
        userOption.classList.add("correct");
        scoreCount++;
    } else {
        userOption.classList.add("incorrect");
        options.forEach((element) => {
            if (element.innerText == quizArray[questionCount].correct) {
                element.classList.add("correct");
            }
        });
    }

 
    clearInterval(countdown);
    options.forEach((element) => {
        element.disabled = true;
    });
}

function initial() {
    quizContainer.innerHTML = "";
    questionCount = 0;
    scoreCount = 0;
    count = 11;
    clearInterval(countdown);
    timerDisplay();
    quizCreator();
    quizDisplay(questionCount);
}

startButton.addEventListener("click", () => {
    startScreen.classList.add("hide");
    displayContainer.classList.remove("hide");
    initial();
});


window.onload = () => {
    startScreen.classList.remove("hide");
    displayContainer.classList.add("hide");
};
