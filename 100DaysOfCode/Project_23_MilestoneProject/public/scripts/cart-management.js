const addToCartButtonElement = document.querySelector('#product-details button');
const cartBadgeElements = document.querySelectorAll('.nav-item .badge');

async function addToCart() {
    const productId = addToCartButtonElement.dataset.productId;
    const csrfToken = addToCartButtonElement.dataset.csrf;

    let response;
    try {
        response = await fetch('/cart/items', {
            method: 'POST',
            body: JSON.stringify({
                productId: productId,
                _csrf: csrfToken
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
    } catch (error) {
        alert('Somthing went wrong!');
        return;
    }
    
    if(!response.ok) {
        alert('Somthing went wrong!');
        return;
    }

    const responseData = await response.json();

    const newTotalQuantity = responseData.newTotalItems;

    for (const cartBadgeElement of cartBadgeElements) {
        cartBadgeElements.textContent = newTotalQuantity;
    }
}

addToCartButtonElement.addEventListener('.click', addToCart);