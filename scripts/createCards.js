import { productCard } from "../components/productCard.js";

export function createCards(items) {
    const container = document.getElementById('catalogo');
    if (items.length === 0 && currentIndex === 0) {
        // Mostrar mensaje de "No se encontraron resultados"
        container.innerHTML = ''; // Limpiar cualquier contenido previo
        const noResultsMessage = document.createElement('div');
        noResultsMessage.classList.add('card');
        noResultsMessage.innerHTML = `
            <figure style="display: grid; place-items: center;">
                <img src="/media/icons/404-error.webp" alt="No results" style="width: 250px; height: 250px; object-fit: contain;">
            </figure>
            <h2 style="width: 100%; text-align: center;">NOTHING TO SHOW HERE</h2>
        `;
        container.appendChild(noResultsMessage);
        return;
    }else{
        console.log(items.productos);
        items.productos.forEach(item => {
            const card = document.createElement('article');
            card.classList.add('producto');
            const CardContent = productCard(item);
            card.innerHTML = CardContent;
            container.appendChild(card);
        });
    }
}