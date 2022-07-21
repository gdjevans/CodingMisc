const Cart = require("../models/cart.model");

function initialiseCart() {
    let cart;

    if(!req.session.cart) {
        cart = new Cart();
    } else {
        const sessionCart = req.session.cart;
        cart = new Cart(
            sessionCart.items, 
            sessionCart.totalQuantity, 
            sessionCart.totalPrice
        );
    }

    res.locals.cart = cart;

    next();
}

module.exports = initialiseCart;