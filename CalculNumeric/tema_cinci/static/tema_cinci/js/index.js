function deleteMatrix(matrix,n){
console.log("666666666666666666666")
    console.log(matrix.rows.length)
            for(var i = matrix.rows.length - 1; i >= 0; i--)
                {
                console.log(i+ "bun")
                    matrix.deleteRow(0);
                }
}
function createMatrix(matrix,n,text,m){
 for(let i=0;i<n;i++){
                var y = document.createElement("TR");
                y.setAttribute("id", text+"myTr"+i);
                matrix.appendChild(y);
                for(let j=0;j<m;j++){
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
    document.getElementById("inversaText").style.display = 'none';
            document.getElementById("matrixC").style.display = 'none';
     document.getElementById('norma').style.display='none'
    $("#ex1_wrap").slideToggle( "slow");
    $("#creare").click(function(){
    document.getElementById('norma').style.display='none'
            var matrixA = document.getElementById("matrixA");
             var matrixC = document.getElementById("matrixC");
            var buttonCalc = document.getElementById("calculare");
            document.getElementById("inversaText").style.display = 'none';
            document.getElementById("matrixC").style.display = 'none';
            buttonCalc.style.display = 'block';

            var n= $("#number").val()

            deleteMatrix(matrixA,n);
            deleteMatrix(matrixC,n);

            createMatrix(matrixA,n,'A',n);




        })

  });

});

function send(){

var n= $("#number").val()

if(checkInput('A',n,n) ){
    var matrixA=takeinputs('A',n,n)

    console.log(matrixA)
    console.log("inainte de post")
$.ajax({
    type : "POST",
    url : "/tema_cinci/inverse/",
    csrfmiddlewaretoken: '{{ csrf_token }}',
    data : JSON.stringify({matA:matrixA}),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
      },
    success: function(response){
        console.log("Saved! It worked.");
        showResult(response);

      },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
      }
    });
    }
    else
        alert("Completeaza toate campurile")
}

function checkInput(text,n,m){

for (let i=0;i<n;i++){

        var rows=[]
        for(let j=0;j<m;j++){

            if( !$("#"+text+"element"+i+j).val() )
            return false
            }

}
return true
}

function takeinputs(text,n,m){
var matrixA=[];

    console.log(n)
    var a=0;
    for (let i=0;i<n;i++){
        var rows=[]
        for(let j=0;j<m;j++){
            console.log($("#"+text+"element"+i+j).val())
            rows.push(parseFloat($("#"+text+"element"+i+j).val()))
            }
         matrixA.push(rows)
            }

    return matrixA;
}

function showResult(params){

    if(params['ok'] == 1){
        iterations = params['nrIteratii']
        inverse = params['inversa']
       // console.log(inverse)
        displayMatrix(inverse, iterations)
    }
    else{
        displayNorm(params);
    }

}

function displayMatrix(response, iterations){

document.getElementById("inversaText").style.display = 'block';
document.getElementById("inversaText").innerHTML ="Inversa matricii dupa " + iterations + " iteratii:"
document.getElementById("matrixC").style.display = 'block';
var n = response.length
console.log(n)
var text="C"
var matrix = document.getElementById("matrixC");
for(let i=0;i<n;i++){
                var y = document.createElement("TR");
                y.setAttribute("id", text+"myTr"+i);
                matrix.appendChild(y);
                for(let j=0;j<n;j++){
                     var z = document.createElement("TD");

                     var t = document.createTextNode(response[i][j]);


                     z.appendChild(t);
                     document.getElementById(text+"myTr"+i).appendChild(z);
              }
            }

            var buttonCalc = document.getElementById("calculare");
            buttonCalc.style.display = 'none';
            var textp = document.getElementById("matP");
            //textp.style.display = 'none';
}

function displayNorm(rsp){
    console.log(rsp);
    console.log(rsp['norma'])
    console.log(rsp['nrIteratii'])
    document.getElementById('norma').innerHTML = "Algoritmul s-a oprit dupa " + rsp['nrIteratii'] + ", norma fiind: "+rsp['norma']
    document.getElementById('norma').style.display='block';
    document.getElementById("calculare").style.display= 'none'
}