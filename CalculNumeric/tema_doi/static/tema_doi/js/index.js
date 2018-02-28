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

    $("#ex1_wrap").slideToggle( "slow");
    $("#creare").click(function(){
            var matrixA = document.getElementById("matrixA");
            var matrixB = document.getElementById("matrixB");
            var matrixC = document.getElementById("matrixC");
            var buttonCalc = document.getElementById("calculare");
            var divDisp1=document.getElementById("displayResponsebun")
        divDisp1.style.display = 'none';

        var divDisp2=document.getElementById("verificare1")
        divDisp2.style.display = 'none';

        var divDisp3=document.getElementById("verificare2")
        divDisp3.style.display = 'none';

        var divDisp4=document.getElementById("verificare3")
        divDisp4.style.display = 'none';

        var divDisp=document.getElementById("displayResponserau")
        divDisp.style.display = 'none';

            buttonCalc.style.display = 'block';

            var n= $("#number").val()

            deleteMatrix(matrixA,n);
            deleteMatrix(matrixB,n);

            createMatrix(matrixA,n,'A',n);

            createMatrix(matrixB,n,'B',1);


        })

  });

});

function send(){
var n= $("#number").val()

if(checkInput('A',n,n) && checkInput('B',n,1) ){
    var matrixA=takeinputs('A',n,n)
    var matrixB=takeinputs('B',n,1)
    console.log(matrixA)
    console.log(matrixB)
$.ajax({
    type : "POST",
    url : "/tema_doi/terms/",
    csrfmiddlewaretoken: '{{ csrf_token }}',
    data : JSON.stringify({matA:matrixA,matB:matrixB}),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
      },
    success: function(response){
        console.log("Saved! It worked.");
        displayResponse(response)
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
console.log("merge")
console.log(n)
console.log(m)
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

function displayResponse(response){
console.log(response)
var buttonCalc = document.getElementById("calculare");
            buttonCalc.style.display = 'none';

    if(response.result==-1){
        var divDisp=document.getElementById("displayResponserau")
        divDisp.style.display = 'block';
    }
    else{
        var divDisp1=document.getElementById("displayResponsebun")
        divDisp1.style.display = 'block';
        divDisp1.innerHTML ="Solutia sistemului: "
        var arr=response.result
        for(let i=0;i<arr.length;i++)
            divDisp1.innerHTML=divDisp1.innerHTML+"x"+(i+1)+"= "+arr[i]+", "
        var divDisp2=document.getElementById("verificare1")
        divDisp2.style.display = 'block';
        divDisp2.innerHTML ="||A*x - b|| = " + response.ver1
        var divDisp3=document.getElementById("verificare2")
        divDisp3.style.display = 'block';
        divDisp3.innerHTML ="||x(gauss) - x(lib)|| = " + response.ver2
        var divDisp4=document.getElementById("verificare3")
        divDisp4.style.display = 'block';
        divDisp4.innerHTML ="||x(gauss) - A(inv)*b|| = " + 0
    }
}