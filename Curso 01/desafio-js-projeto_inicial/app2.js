let dia = "segunda";
dia = prompt("Qual é o dia da semana?");

if((dia == "sabado") || (dia == "domingo")){

    alert("Bom fim de semana!");
}else{

    alert("Boa semana!")
}

let numero = 0;
numero = prompt("Digite um numero!");

if(numero < 0){
    alert("Esse número é negativo!");
}else{
    alert("Esse número é positivo!");
}

if(numero >= 100){
    alert("Parabéns, você venceu!");
}else{
    alert("Tente novamente para ganhar.");
}

let saldo = 12000;
alert(`Você possui um saldo de R$ ${saldo}.`);// tem que usar crase para funcionar e não aspas

let nome = " ";
nome = prompt("Digite seu nome!");
alert(`Bem vindo ao sistema ${nome}`);

