let email = document.querySelector('#email')
let password = document.querySelector('#password')


const login = () => {
    const formData = new FormData();
    formData.append('grant_type', '');
    formData.append('username', email.value);
    formData.append('password', password.value);
    formData.append('scope', '');
    formData.append('client_id', '');
    formData.append('client_secret', '');

    fetch('http://127.0.0.1:8000/auth/jwt/login', {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.status === 400) {
            let login = document.querySelector('#loginForm')
            let elError = document.createElement('span')
            elError.style.color = 'red'
            let textError = document.createTextNode('Неверный логин или пароль!')
            elError.appendChild(textError)

            login.appendChild(elError)
        } else if (response.status === 204) {
            window.location.href = '/index/base/'
        } else {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
    })

}

