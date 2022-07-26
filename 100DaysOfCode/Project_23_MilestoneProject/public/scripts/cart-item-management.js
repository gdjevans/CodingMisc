const cartItemUpdateFormElements = document.querySelectorAll('.cart-item-management')

async function updateCartItem(event) {
    event.preventDefault();

    const form = event.target;

    const productId = form.dataset.productid;
    const csrfToken = form.dataset.csrf;
    const quantity = form.firstElementChild.value

    try{
        const response = await fetch('/cart/items', {
            method: 'PATCH',
            body: JSON.stringify({
                productId: productId,
                quantity: quantity,
                _csrf: csrfToken
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
    } catch(error) {
        alert('Something went wrong!');
        return;
    }

    if (!response.ok) {
        alert('Something went wrong!');
        return;
    }

    const responseData = await response.json();

    if (responseData.updatedCartData.updatedItemPrice === 0) {
        form.parentElement.parentElement.remove();
    } else {
        const cartItemTotalPriceElement = form.parentElement.querySelector('.cart-item-price'); 
        cartItemTotalPriceElement.textContent = responseData.updatedCartItem.updatedItemPrice.toFixed(2);
    }

    const cartTotalPriceElement = document.getElementById('cart-total-price');
    cartTotalPriceElement.textContent = responseData.updatedCartItem.newTotalPrice.toFixed(2);

    const cartBadge = document.querySelector('.nav-items .badge');
    cartBadge.textContent = responseData.updatedCartItem.newTotalQuantity;

}

for(const formElement of cartItemUpdateFormElements) {
    formElement.addEventListener('submit', updateCartItem);
}