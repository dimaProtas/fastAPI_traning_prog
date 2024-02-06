const email = document.querySelector('#email')
const password = document.querySelector('#password')


const logout = () => {
    fetch('http://127.0.0.1:8000/auth/jwt/logout', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        })
    })
    .then(response => {
        console.log(response.status)
        if (response.status !== 204) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        } else {
            window.location.href = '/index/login/'
        }
    })
}