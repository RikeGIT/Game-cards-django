document.addEventListener("DOMContentLoaded", function () {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const estrelas = document.querySelectorAll(".star");

    function preencherEstrelas(valorSelecionado) {
        estrelas.forEach(function (star) {
            const valor = parseInt(star.getAttribute("data-value"));
            if (valor <= valorSelecionado) {
                star.classList.add("preenchida");
            } else {
                star.classList.remove("preenchida");
            }
        });
    }

    estrelas.forEach(function (star) {
        star.addEventListener("click", function () {
            const valor = parseInt(this.getAttribute("data-value"));

            preencherEstrelas(valor); // Atualiza visualmente

            fetch(avaliarJogoUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": csrfToken
                },
                body: new URLSearchParams({ "estrelas": valor })
            }).then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById("media-de-estrelas").textContent = data.media_estrelas;
                } else {
                    alert("Erro ao registrar avaliação.");
                }
            }).catch(error => console.error("Erro ao enviar avaliação:", error));
        });
    });
});
