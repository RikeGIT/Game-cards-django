function scrollLeft() {
    const container = document.querySelector('.lista-jogos-container');
    container.scrollBy({
        left: -320, // Ajuste este valor conforme necessário
        behavior: 'smooth'
    });
}

function scrollRight() {
    const container = document.querySelector('.lista-jogos-container');
    container.scrollBy({
        left: 320, // Ajuste este valor conforme necessário
        behavior: 'smooth'
    });
}
