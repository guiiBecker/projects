
// cada pessoa como 400g de carne +6 horas 650 g pessoas
// cada pessoa toma 1.200ml +6 horas 2000ml
// 1 litro de refri ou água por pessoa +6 horas 1.500ml
// criança vale por meio 
//

let inputAdultos = document.getElementById("adulto");
let inputCrianca = document.getElementById("crianca");
let inputDuracao = document.getElementById("duracao");

console.log(inputAdultos.value, inputCrianca.value, inputDuracao.value);

let resultado = document.getElementById("resultado")


function calcular(){
    console.log("calculando")
    let duracao = inputDuracao.value;
    let adulto = inputAdultos.value;
    let crianca = inputCrianca.value;
    if(duracao >= 6){
        carne = 650
        cerveja = 2000
        bebida = 1500
        let qntCarne = carne * adulto + ((carne/2)*crianca);
        let qntCerveja = cerveja * adulto;
        let qntBebida = bebida * adulto + ((bebida/2)*crianca);
        console.log(qntCarne, qntCerveja, qntBebida)

        resultado.innerHTML = `<p>${qntCarne / 1000} KG de carne </p>`
        resultado.innerHTML += `<p>${qntCerveja / 355} latas de cerveja </p>`
        resultado.innerHTML += `<p>${qntBebida / 2000} Garrafas de refrigerante </p>`
    }

    else{
        carne = 400
        cerveja = 1200
        bebida = 1000
        let qntCarne = carne * adulto + ((carne/2)*crianca);
        let qntCerveja = cerveja * adulto;
        let qntBebida = bebida * adulto + ((bebida/2)*crianca);
        console.log(qntCarne, qntCerveja, qntBebida)

        resultado.innerHTML = `<p>${qntCarne}g de carne </p>`
        resultado.innerHTML += `<p>${qntCerveja}ml de cerveja </p>`
        resultado.innerHTML += `<p>${qntBebida}ml de bebidas </p>`
    }

}

