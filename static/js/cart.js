document.addEventListener("DOMContentLoaded", function() {
    const cartItems = document.querySelector('.cart-items');
    const totalElement = document.getElementById('total');
    let total = 0;

    function addToCart(itemName, itemPrice) {
        const item = document.createElement('li');
        item.classList.add('cart-item');
        item.innerHTML = `
            <span>${itemName}</span>
            <span>$${itemPrice.toFixed(2)}</span>
        `;
        cartItems.appendChild(item);
        total += itemPrice;
        totalElement.textContent = total.toFixed(2);
    }

    // Example items
    addToCart('Item 1', 10.99);
    addToCart('Item 2', 5.99);
    addToCart('Item 3', 8.49);

    // Checkout button event listener
    document.querySelector('.checkout-btn').addEventListener('click', function() {
        alert('Checkout functionality not implemented yet!');
    });
});
