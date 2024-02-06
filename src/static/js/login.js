const email = document.querySelector('#email')
const password = document.querySelector('#password')


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
        if (response.status !== 204) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        } else {
            window.location.href = '/index/base/'
        }
    })
}