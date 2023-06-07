/* ver carrito */

const btnProduct = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector('.container-cart-products')

btnProduct.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart');
})

/* agregar productos a carrito */
const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

const productList = document.querySelector('.contenedorCliente');
//variables de arreglos de productos
let allProducts = [];

const valorTotal = document.querySelector('.total-pagar')

const countProducts = document.querySelector('#contador-productos')

productList.addEventListener('click', e => {
    /*console.log(e.target.classList.contains('comprar'))*/
    if(e.target.classList.contains('comprar')){
        const product = e.target.parentElement.parentElement.querySelector(".infCar")
        
        const infoProduct = {
            quantity: 1,
            title: product.querySelector('h2').textContent,
            price: product.querySelector('p').textContent,
        }

        const exits = allProducts.some(product => product.title === infoProduct.title)
        
        if (exits){
            const products = allProducts.map(product => {
                if(product.title === infoProduct.title){
                    product.quantity++;
                    return product;
                } else{
                    return product;
                }
            });
            allProducts = [...products];
        } else {
            allProducts = [...allProducts, infoProduct];
        }

        showHTML();
    }
})

rowProduct.addEventListener('click', e => {
	if (e.target.classList.contains('icon-close')) {
		const product = e.target.parentElement;
		const title = product.querySelector('p').textContent;

		allProducts = allProducts.filter(
			product => product.title !== title
		);

		console.log(allProducts);

		showHTML()
	}
});

const showHTML = () => {

    if (!allProducts.length) {
		containerCartProducts.innerHTML=`
            <p class="cart-empty">El carrito esta vacio</p>
        `
	}
    //limpiar html
    rowProduct.innerHTML = '';

    let total = 0;
    let totalProducts = 0;

    allProducts.forEach(product => {
        const containerProduct = document.createElement('div')
        containerProduct.classList.add('cart-product')
    
        containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="icon-close"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            </svg>
        `;
        rowProduct.append(containerProduct);

        total = 
            total + parseInt(product.quantity * product.price.slice(1));
        totalProducts = totalProducts + product.quantity;
    });
    
    valorTotal.innerText = `$${total}`;
    countProducts.innerText = totalProducts;
    
};

/*    if(e.target.classList.contains('comprar')){
        console.log(e.target.parentElement)

        console.log(product.querySelector('h2'))
    }

    const product = e.target.previousElementSibling.previousElementSibling

        console.log(product.querySelector('h2').textContent)
 fin  */
/*
document.getElementById("btnCarrito").addEventListener("click", function(){
    var detalles = document.getElementById("infCar").textContent;
    console.log(detalles);
});*/

/* ver mas*/ 
document.querySelectorAll(".ver").forEach(element => {
    const contenido = element.parentElement.parentElement.querySelector(".content");
    element.addEventListener("click", function () {
        contenido.classList.toggle("active")
        contenido.style.overflowY = "scroll";
    })
})