const brand = document.querySelector('#brand')

const search_brand_car = () => {
    if (brand.value) {
        console.log(brand.value, 'Принял')
        window.location.href = `/index/brand_cars/${brand.value}/${10}`
        brand.value = ''
    } else {
        window.location.href = `/index/cars/${0}/${10}`
    }
}


const add_car = () => {
    let brand = document.querySelector('#addBrand')
    let model = document.querySelector('#addmodel')
    let price = document.querySelector('#addPrice')
    let color = document.querySelector('#addColor')
    let userId = document.querySelector('#addUserId')

    fetch(`http://127.0.0.1:8000/cars/add_car`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "brand": brand.value,
            "model": model.value,
            "price": Number(price.value,),
            "color": color.value,
            "user_id": Number(userId.value)
          })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        console.log(response)
        return response.json()
    })
    .then(response => {
        if (response.status == 'OK') {
            let container = document.querySelector('#container')

            let divContainer = document.createElement('div')
            divContainer.setAttribute('class', 'divContainer')
            let img_title = document.createElement('div')
            img_title.setAttribute('class', 'img_title')
            let img = document.createElement('img')
            img.setAttribute('src', 'https://prorisuem.ru/foto/27/avtomobil_risunok_33.webp')
            img_title.appendChild(img)


            let divInImg = document.createElement('div')
            img_title.appendChild(divInImg)

            let pBrandModel = document.createElement('p')
            let pTextModelBrand = document.createTextNode(`${response.data.brand} ${response.data.model}`)
            pBrandModel.appendChild(pTextModelBrand)
            divInImg.appendChild(pBrandModel)

            let pColor = document.createElement('p')
            let pTextColor = document.createTextNode(response.data.color)
            pColor.appendChild(pTextColor)
            divInImg.appendChild(pColor)

            let spanColor = document.createElement('span')
            spanColor.style = `background-color: ${response.data.color}; width: 20px; height: 20px; border-radius: 50%; display: inline-block;`
            divInImg.appendChild(spanColor)
            
            img_title.appendChild(divInImg)
            divContainer.appendChild(img_title)

            let pPrice = document.createElement('p')
            let pTextPrice = document.createTextNode(`${response.data.price} руб.`)
            pPrice.appendChild(pTextPrice)

            divContainer.appendChild(pPrice)

            let divContainerOne = document.querySelector('.divContainer')
            container.insertBefore(divContainer, divContainerOne)
        }
    })
    .catch(error => {
        console.log(`Error: ${error}`)
    })
}


const deleteItem = (car_id) => {
    console.log(car_id)
    fetch(`http://127.0.0.1:8000/cars/delete/${car_id}`, {
        method: 'DELETE',
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
        if (response.succec == 'ok') {
            let divDeleteContainer = document.querySelector(`#car_${car_id}`)
            divDeleteContainer.remove()
        }
    })
}