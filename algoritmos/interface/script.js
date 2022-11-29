let questoes = [
    "Gerar números aleatórios",
    "Maior elemento",
    "Soma dos elementos",
    "Número de ocorrências do primeiro elemento",
    "Média dos elementos",
    "Valor mais próximo da média dos elementos",
    "Soma dos elementos com valor negativo",
    "Quantidade de vizinhos iguais",
];

var num_input_boxes = 10;

// var funcoes = { 'btn-q-0' : gerarNumerosAleatorios }

let grupoInput = document.getElementById('grupo-inputs');
let grupoBtns = document.getElementById('grupo-btns');

for (var i=0; num_input_boxes > i; i++){
    var inputTxt = document.createElement("input")
    inputTxt.className = "input-type"
    inputTxt.id = `input-t-${i}`
    inputTxt.maxLength = "2"
    grupoInput.appendChild(inputTxt)
}


for (var i=0; questoes.length > i; i++){
    var btn = document.createElement("button");
    var text = document.createTextNode(questoes[i]);
    
    btn.style.backgroundColor = "white";
    btn.style.fontFamily = "Kalam";
    
    btn.className = "btn-questao";
    btn.id = `btn-q-${i}`;
    btn.addEventListener("click", mudarCor);
    btn.addEventListener("mouseover", mouseEmCima);
    btn.addEventListener("mouseleave", mouseSai);

    btn.appendChild(text);
    grupoBtns.appendChild(btn);
}

function gerarNumerosAleatorios() {
    for (i = 0; num_input_boxes > i; i++) {
        var numero = Math.floor(Math.random() * 10 * 2 - 10) // intervalo de -10 a +10
        document.getElementById(`input-t-${i}`).value = numero
    }
}

function mouseEmCima(){
    if (this.style.backgroundColor == "white"){
        this.style.backgroundColor = "rgb(20, 107, 236)"
    }
}

function mouseSai(){
    if (this.style.backgroundColor == "rgb(20, 107, 236)"){
        this.style.backgroundColor = "white"
    }
}

function mudarCor(){

    this.style.backgroundColor = "rgb(14, 146, 36)";

    if (this.id == `btn-q-0`){gerarNumerosAleatorios();}
    if (this.id == `btn-q-1`){retornaMaiorValor();}
    if (this.id == `btn-q-2`){retornaSomaDosElementos(true);}
    if (this.id == `btn-q-3`){retornaNumeroDeOcorrenciaDo1Termo();}
    if (this.id == `btn-q-4`){retornaMediaDosElementos();}
    if (this.id == `btn-q-5`){}
    if (this.id == `btn-q-6`){}
    if (this.id == `btn-q-7`){}


    for (var i=0; questoes.length > i; i++){
        if (`btn-q-${i}` != this.id){
            var btn = document.getElementById(`btn-q-${i}`);
            btn.style.backgroundColor = "white";
        }
    }
}

// funções


function mostrarResultado(resultado){
    document.getElementById('result').innerText = resultado.toString()
}


function retornaMaiorValor(){
    var lista = coletarNumerosInput();
    var maior = -99;
    for (var i = 0; lista.length > i; i++){
        if (lista[i] > maior){
            maior = lista[i];
        }
    }
    mostrarResultado(maior);
}


function retornaSomaDosElementos(mostrar){
    var lista = coletarNumerosInput();

    var soma = lista.reduce(
        function(soma, i) {
        return soma + i;
        }
    );
    if (mostrar == true){
        mostrarResultado(soma);
    }
    return soma;
}


function retornaNumeroDeOcorrenciaDo1Termo(){
    let lista = coletarNumerosInput();
    let alvo = lista[0];
    let ocorrencias = 0;
    for (numero of lista){
        console.log('loop')
        if (numero == alvo){
            ocorrencias++;
        }
    }
    mostrarResultado(ocorrencias);
}


function retornaMediaDosElementos(){
    let soma = retornaSomaDosElementos();
    let media =  parseFloat(soma) / parseFloat(coletarNumerosInput().length)
    mostrarResultado(media)
    return media;
}


function coletarNumerosInput(){
    var lista_numeros = []
    for(i = 0; num_input_boxes > i; i++){
        lista_numeros.push(parseInt(document.getElementById(`input-t-${i}`).value))
    }
    return lista_numeros
}


function valorMaisProximaDaMedia(){
    var lista = coletarNumerosInput();
    var media = retornaMediaDosElementos();

    const nova_lista = lista.map(function(elemento){return elemento - media})
    
    console.log(nova_lista)

}
