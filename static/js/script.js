/* ver carrito */

const btnCart = document.querySelector('.container-cart-icon')
    const containerCartProducts = document.querySelector('.container-cart-products')

    btnCart.addEventListener('click', () => {
      containerCartProducts.classList.toggle('hidden-cart')
    })

/* agregar productos a carrito 
const cartInfo = document.querySelector('.cart-product')
const rowProduct = document.querySelector('.row-product')

const productList = document.querySelector('.content')

let allProducts = []


productList.addEventListener('click', e => {
    if(e.target.classList.contains('comprar')){
        console.log(e.target.parentElement)

        console.log(product.querySelector('h2'))
    }

})
 fin  */

document.getElementById("btnCarrito").addEventListener("click", function(){
    var detalles = document.getElementById("infCar").textContent;
    console.log(detalles);
});

/* ver mas*/ 
document.querySelectorAll(".ver").forEach(element => {
    const contenido = element.parentElement.parentElement.querySelector(".content");
    element.addEventListener("click", function () {
        contenido.classList.toggle("active")
        contenido.style.overflowY = "scroll";
    })
})