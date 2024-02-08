let emailInput = document.querySelector('#email')
let passwordInput = document.querySelector('#password')


const validateEmail = (event) => {
    let emailPattern = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
    let errorEl = document.querySelector('#errorlogin')
    let errorSpan = document.querySelector('span')
    let buttonSend = document.querySelector('button')
    if (event.target.value == '' || emailPattern.test(event.target.value)) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
        buttonSend.setAttribute('onClick', 'login()')
    } else if (!emailPattern.test(event.target.value)) {
        let login = document.querySelector('#loginForm')
        event.target.setAttribute('class', 'error')
        let elP = document.createElement('span')
        elP.setAttribute('id', 'errorlogin')
        elP.style.color = 'red'
        let textErr = document.createTextNode('Неверный email!')
        elP.appendChild(textErr)
        if (!errorEl) {
            login.insertBefore(elP, event.target)
        }
        buttonSend.removeAttribute('onClick', 'login()')
    }
}

emailInput.addEventListener('input', validateEmail)


const validtePassword = (event) => {
    let errorEl = document.querySelector('#errorPassword')
    let errorSpan = document.querySelector('span')
    let buttonSend = document.querySelector('button')
    if (event.target.value.length > 3 || !event.target.value) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
        buttonSend.setAttribute('onClick', 'login()')
        } else if (event.target.value.length < 3) {
            let login = document.querySelector('#loginForm')
            event.target.setAttribute('class', 'error')
            let elP = document.createElement('span')
            elP.setAttribute('id', 'errorPassword')
            elP.style.color = 'red'
            let textErr = document.createTextNode('Пароль должен быть больше 3 символов!')
            elP.appendChild(textErr)
            if (!errorEl) {
                login.insertBefore(elP, event.target)
            }
            buttonSend.removeAttribute('onClick', 'login()')
        }
}


passwordInput.addEventListener('input', validtePassword)
