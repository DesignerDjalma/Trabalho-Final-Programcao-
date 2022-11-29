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

let grupoInput = document.getElementById('grupo-inputs');
let grupoBtns = document.getElementById('grupo-btns');

for (var i=0; 10 > i; i++){
    var inputTxt = document.createElement("input")
    inputTxt.className = "input-type"
    inputTxt.id = `input-t-${i}`
    inputTxt.maxLength = "2"
    grupoInput.appendChild(inputTxt)
    // grupoInput.innerHTML += '<input type="text" maxlength="2" class="input-type">';
}


for (var i=0; questoes.length > i; i++){
    var btn = document.createElement("button");
    var text = document.createTextNode(questoes[i]);
    btn.style.backgroundColor = "white";
    
    btn.className = "btn-questao";
    btn.id = `btn-q-${i}`;
    btn.addEventListener("click", mudarCor);
    btn.addEventListener("mouseover", mouseEmCima);
    btn.addEventListener("mouseleave", mouseSai);

    btn.appendChild(text);
    grupoBtns.appendChild(btn);
}


function mouseEmCima(){
    if (this.style.backgroundColor == "white"){
        this.style.backgroundColor = "blue"
    }
}

function mouseSai(){
    if (this.style.backgroundColor == "blue"){
        this.style.backgroundColor = "white"
    }
}

function mudarCor(){

    this.style.backgroundColor = "red";

    for (i = 0; 10 > i; i++){

        document.getElementById(`input-t-${i}`).value = Math.floor(Math.random() * 10 * 2 - 10)

    }

    for (var i=0; questoes.length > i; i++){
        if (`btn-q-${i}` != this.id){
            var btn = document.getElementById(`btn-q-${i}`);
            btn.style.backgroundColor = "white";
        }
    }
}



// Ele muda de um jeito que nao faz sentido pra mim
// function mudarCor(){
//     console.log("clicou")
//     console.log(this.id)
//     for (var i = 0; questoes.length > i; i++){
//         if (this.id != `btn-q-${i}`){
//             var outroBtn = document.getElementById(`btn-q-${i}`)
//             if ( outroBtn.style.backgroundColor != "red" ){
//                 this.style.backgroundColor = "red"
//             } else {
//                 this.style.backgroundColor = "blue"
//             }
//         }
//     }
// }

// function mouseEmCima(){
//     // verificar lista:
//     console.log(`1. mouseEmCima: Printando lista: ${lista}`)
    
//     console.log(`1. mouseEmCima: cor="${this.style.backgroundColor}"`)
//     if (this.style.backgroundColor == "white"){
//         console.log(`2. mouseSai: Mudando cor de "${this.style.backgroundColor}" para "blue".`)
//         this.style.backgroundColor = "blue"
//         lista[parseInt(this.id[-1])] = "blue"
//     } else {
//         //nada
//     }

//     console.log(`2. mouseEmCima: Printando lista: ${lista}`)

// }

// function mouseSai(){
//     // verificar lista:
//     console.log(`1. mouseSai: Printando lista: ${lista}`)

//     console.log(`1. mouseSai: cor="${this.style.backgroundColor}"`)
//     if (this.style.backgroundColor == "blue"){
//         console.log(`2. mouseSai: Mudando cor de "${this.style.backgroundColor}" para "white".`)
//         this.style.backgroundColor = "white"
//         lista[parseInt(this.id[-1])] = "white"
//     }

//     console.log(`2. mouseSai: Printando lista: ${lista}`)

// }





// outra perola
// function mudarCor(){
//     const lista = [];
//     for (var i = 0; questoes.length > i; i++){
//         if (this.id == `btn-q-${i}`){
//             console.log(this.id);
//         } else {
//             var outroBtn = document.getElementById(`btn-q-${i}`);
//             lista.push(outroBtn.style.backgroundColor);
//             if (lista.includes("red")){
//                 outroBtn.style.backgroundColor = "white";
//                 this.style.backgroundColor = "red";
//                 this.addEventListener("mouseover", mouseEmCima)
//                 this.addEventListener("mouseleave", mouseSaiRed)
//             }
//         }
//     }
//     console.log(lista);
// }

// function mudarCor(){
//     const lista = [];
//     for (var i = 0; questoes.length > i; i++){
//         if (this.id == `btn-q-${i}`){
//             console.log(this.id);
//         } else {
//             var outroBtn = document.getElementById(`btn-q-${i}`);
//             lista.push(outroBtn.style.backgroundColor);
//             if (lista.includes("red")){
//                 outroBtn.style.backgroundColor = "white";
//                 this.style.backgroundColor = "red";
//             }
//         }
//     }
//     console.log(lista);
// }


