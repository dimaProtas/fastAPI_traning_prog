fetch('http://127.0.0.1:8000/chat/last_message/', {
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
.then(data => {
    data.reverse().forEach(m => {
        let messages = document.querySelector('#messages')
        let message = document.createElement('li')
        let textMessage = document.createTextNode(m.message)
        message.appendChild(textMessage)

        messages.appendChild(message)
    })
})