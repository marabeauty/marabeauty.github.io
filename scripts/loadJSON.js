import { createCards } from "./createCards.js";

let allItems = [];

async function loadJSON() {
    const jsonFile = '/data/productos.json';
    try {
        const response = await fetch(jsonFile); // Ruta al archivo JSON
        if (!response.ok) {
            throw new Error('Error al cargar el archivo JSON');
        }
        const data = await response.json();
        allItems = data; // Guardar los datos originales
        createCards(allItems); // Generar las primeras tarjetas
    } catch (error) {
        console.error(error);
    }
}

document.addEventListener('DOMContentLoaded', loadJSON);