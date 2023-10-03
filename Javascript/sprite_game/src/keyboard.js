
let key;

function keyPress(element){
    element.addEventListener('keydown',event=>{
        key = event.key
    })
}

export {keyPress, key}