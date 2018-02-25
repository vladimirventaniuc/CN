function deleteMatrix(matrix,n){
console.log("666666666666666666666")
    console.log(matrix.rows.length)
            for(var i = matrix.rows.length - 1; i >= 0; i--)
                {
                console.log(i+ "bun")
                    matrix.deleteRow(0);
                }
}
function createMatrix(matrix,n,text){
 for(let i=0;i<n;i++){
                var y = document.createElement("TR");
                y.setAttribute("id", text+"myTr"+i);
                matrix.appendChild(y);
                for(let j=0;j<n;j++){
                     var z = document.createElement("TD");

                     var t = document.createElement("INPUT");
                      t.setAttribute("type", "number");
                      t.setAttribute("id", text+"element"+i+j);
                     z.appendChild(t);
                     document.getElementById(text+"myTr"+i).appendChild(z);
              }
            }

}
jQuery(document).ready(function($)
{

  $("#ex1").click(function()
  {

    $("#ex1_wrap").slideToggle( "slow");


  });

  $("#ex2").click(function()
  {

    $("#ex2_wrap").slideToggle( "slow");


  });

  $("#ex3").click(function()
  {

    $("#ex3_wrap").slideToggle( "slow");
        $("#creare").click(function(){
            var matrixA = document.getElementById("matrixA");
            var matrixB = document.getElementById("matrixB");
            var matrixC = document.getElementById("matrixC");
            var buttonCalc = document.getElementById("calculare");
            var textp = document.getElementById("matP");
            buttonCalc.style.display = 'block';
            textp.style.display = 'block';
            var n= $("#number").val()

            deleteMatrix(matrixA,2**n);
            deleteMatrix(matrixB,2**n);
            deleteMatrix(matrixC,2**n);
            createMatrix(matrixA,2**n,'A');

            createMatrix(matrixB,2**n,'B');


        })



  });




});

function takeinputs(text){
var matrixA=[];
    var n= $("#number").val()
    n=2**n
    console.log(n)
    var a=0;
    for (let i=0;i<n;i++){
        var rows=[]
        for(let j=0;j<n;j++){
            console.log($("#"+text+"element"+i+j).val())
            rows.push($("#"+text+"element"+i+j).val())
            }
         matrixA.push(rows)
            }

    return matrixA;
}
function send(){
if(checkInput('A') && checkInput('B')){
 var matrixA=takeinputs('A')
    var matrixB=takeinputs('B')
    console.log(matrixA)
    console.log(matrixB)
$.ajax({
    type : "POST",
    url : "/tema_unu/multiply/",
    csrfmiddlewaretoken: '{{ csrf_token }}',
    data : JSON.stringify({matA:matrixA,matB:matrixB}),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
      },
    success: function(response){
        console.log("Saved! It worked.");
        displayProduct(response)
      },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
      }
    });
    }
    else
        alert("Completeaza toate campurile")
}

function displayProduct(response){
console.log("aaaaa")
console.log(response.result)
var n = response.result.length
console.log(n)
var text="C"
var matrix = document.getElementById("matrixC");
for(let i=0;i<n;i++){
                var y = document.createElement("TR");
                y.setAttribute("id", text+"myTr"+i);
                matrix.appendChild(y);
                for(let j=0;j<n;j++){
                     var z = document.createElement("TD");

                     var t = document.createTextNode(response.result[i][j]);


                     z.appendChild(t);
                     document.getElementById(text+"myTr"+i).appendChild(z);
              }
            }
            console.log("555555")
            console.log(matrix.rows.length)
            var buttonCalc = document.getElementById("calculare");
            buttonCalc.style.display = 'none';
            var textp = document.getElementById("matP");
            textp.style.display = 'none';
}

function checkInput(text){
var n= $("#number").val()
n=2**n
for (let i=0;i<n;i++){
        var rows=[]
        for(let j=0;j<n;j++){
            if( !$("#"+text+"element"+i+j).val() )
            return false
            }
   return true
}
}