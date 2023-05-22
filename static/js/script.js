/* ver carrito */

const btnCart = document.querySelector('.container-icon')
    const containerCartProducts = document.querySelector('.container-cart-products')

    btnCart.addEventListener('click', () => {
      containerCartProducts.classList.toggle('hidden-cart')
    })


/* ver mas */
document.querySelectorAll(".ver").forEach(element => {
    const contenido = element.parentElement.parentElement.querySelector(".content");
    element.addEventListener("click", function () {
        contenido.classList.toggle("active")
        contenido.style.overflowY = "scroll";
    })
})