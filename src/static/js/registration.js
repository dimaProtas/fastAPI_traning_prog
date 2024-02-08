let first_name = document.querySelector('#firsName')
let last_name = document.querySelector('#lastName')
let email = document.querySelector('#email')
let password = document.querySelector('#password')


const registration = () => {

    fetch('http://127.0.0.1:8000/auth/register', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "email": email.value,
          "password": password.value,
          "is_active": true,
          "is_superuser": false,
          "is_verified": false,
          "first_name": first_name.value,
          "last_name": last_name.value,
          "role_id": 0
        })
    })
    .then(response => {
        if (response.status !== 201) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        } else {
            window.location.href = '/index/login/'
        }
    })
}