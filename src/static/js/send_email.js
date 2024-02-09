const send_email = () => {
    fetch(`http://127.0.0.1:8000/report/autoteka`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json()
    })
    .then(response => {
        if (response.status == 200) {
            let containerSendEmail = document.querySelector("#containerSendEmail")
            
            let elP = document.createElement('p')
            elP.style.color = 'red'
            let elText = document.createTextNode(response.data)
            elP.appendChild(elText)

            containerSendEmail.appendChild(elP)
        }
    })
    .catch(errror => {
        console.log(`Error: ${errror}`)
    })
}