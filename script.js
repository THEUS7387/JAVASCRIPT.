function gerarTabuada() {
    const numeroInput = document.getElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    const resultadoDiv = document.getElementById('resultadoTabuada')
    resultadoDiv.innerHTML = ''
    
    resultadoDiv.innerHTML += `<h2>Tabuada do ${numero}</h2>`

    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`
    }
}

const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', gerarTabuada)