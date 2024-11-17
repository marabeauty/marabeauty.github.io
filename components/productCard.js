export function productCard(item) {
    const cardContentBlog = `
        <figure>
            <img src="/media/utils/default.jpeg" alt="imagen por defecto">
        </figure>
        <div class="producto-info">
            <p class="marca"> ${item.marca} </p>
            <h4 class="referencia"> ${item.referencia} </h4>
            <p class="precio">$ ${item.precio.toLocaleString()} COP</p>
        </div>
    `;
    return cardContentBlog;
}