let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function consolePress(){
    console.log('Botão pressionado');
}

function alertPress(){
    alert('Eu amo JS!');
}

function promptPress(){
    let cidade = prompt('Digite o nome de uma cidade brasileira:');
    alert(`Estive em ${cidade} e lembrei de você.`);
}

function somaPress(){
    let numero1 = parseInt(prompt('Digite o primeiro número da soma:'));
    let numero2 = parseInt(prompt('Digite o segundo número da soma:'));
    let resultado = numero1 + numero2;
    alert(`A soma dos número é igual a ${resultado}`);
}