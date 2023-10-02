const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelectorAll('button')

let userChoice
let computerChoice
let result

possibleChoices.forEach(possibleChoices => possibleChoices.addEventListener('click', (e) => {
    userChoice = e.target.id
    userChoiceDisplay.innerHTML = userChoice
    generateComputerChoice()
    getResult()
}))

function generateComputerChoice() {
    const randomNumber = Math.floor(Math.random() * possibleChoices.length)

    if (randomNumber === 0) {
        computerChoice = 'rock'
    }
    if (randomNumber === 1) {
        computerChoice = 'paper'
    }
    if (randomNumber === 2) {
        computerChoice = 'scissor'
    }

    computerChoiceDisplay.innerHTML = computerChoice
}

function getResult() {
    if (userChoice === computerChoice) {
        result = "Nobody Won or Lost..."
    }
    if (userChoice === "rock" && computerChoice === 'paper') {
        result = "You Lost..."
    }
    if (userChoice === "rock" && computerChoice === 'scissor') {
        result = "You Won!"
    }
    if (userChoice === "paper" && computerChoice === 'rock') {
        result = "You Won!"
    }
    if (userChoice === "paper" && computerChoice === 'scissor') {
        result = "You Lost..."
    }
    if (userChoice === "scissor" && computerChoice === 'rock') {
        result = "You Lost..."
    }
    if (userChoice === "scissor" && computerChoice === 'paper') {
        result = "You Won!"
    }

    resultDisplay.innerHTML = result
}