let emailInput = document.querySelector('#email')
let passwordInput = document.querySelector('#password')
let repid_passwordInput = document.querySelector('#repid_password')
let firsName = document.querySelector('#firsName')
let lastName = document.querySelector('#lastName')


const validateEmail = (event) => {
    let emailPattern = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
    let errorEl = document.querySelector('#errorlogin')
    let errorSpan = document.querySelector('span')
    if (event.target.value == '' || emailPattern.test(event.target.value)) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
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
    }
}

emailInput.addEventListener('input', validateEmail)


const validtePassword = (event) => {
    let errorEl = document.querySelector('#errorPassword')
    let errorSpan = document.querySelector('span')
    if (event.target.value.length > 3 || !event.target.value) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
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
        }
}


passwordInput.addEventListener('input', validtePassword)


const validteRepidPassword = (event) => {
    let errorEl = document.querySelector('#errorRepidPassword')
    let errorSpan = document.querySelector('span')
    if (event.target.value === passwordInput.value) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
    } else {
        let login = document.querySelector('#loginForm')
        event.target.setAttribute('class', 'error')
        let elP = document.createElement('span')
        elP.setAttribute('id', 'errorRepidPassword')
        elP.style.color = 'red'
        let textErr = document.createTextNode('Пароль не совпадает!')
        elP.appendChild(textErr)
        if (!errorEl) {
            login.insertBefore(elP, event.target)
        }
    }
}

repid_passwordInput.addEventListener('input', validteRepidPassword)



const validateFirtNameLastName = (event) => {
    let errorEl = document.querySelector('#errorName')
    let errorSpan = document.querySelector('span')
    if (event.target.value.length > 3 || !event.target.value) {
        if (errorEl) {
            errorEl.remove()
            event.target.removeAttribute('class', 'error')
        }
        if (errorSpan) {
            errorSpan.remove()
        }
    } else if (event.target.value.length < 3) {
        let login = document.querySelector('#loginForm')
        event.target.setAttribute('class', 'error')
        let elP = document.createElement('span')
        elP.setAttribute('id', 'errorName')
        elP.style.color = 'red'
        let textErr = document.createTextNode('Должно быть больше 3 символов!')
        elP.appendChild(textErr)
        if (!errorEl) {
            login.insertBefore(elP, event.target)
        }
    }
}


lastName.addEventListener('input', validateFirtNameLastName)
firsName.addEventListener('input', validateFirtNameLastName)