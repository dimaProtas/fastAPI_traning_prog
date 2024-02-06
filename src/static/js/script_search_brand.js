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