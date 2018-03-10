jQuery(document).ready(function($)
{



  $("#ex1").click(function()
  {

    $("#file1").click(function(){
        $("#verificare").css("display","none")
    })

    $("#verificare").css("display","none")
    $("#ex1_wrap").slideToggle( "slow");
     $("#upload").on("click",function(){
        $("#verificare").css("display","none")

    $(".myFile").upload("uploadfile/",
     {myData:"hey",
     foo:"bar"
     },
     function(success){
        console.log("done");
    },$("#prog"),0)


        });

  });

 });




$.fn.upload = function(remote, data, successFn, progressFn,nr) {
	// if we dont have post data, move it along

	if (typeof data != "object") {
		progressFn = successFn;
		successFn = data;
	}

	var formData = new FormData();
    var name;
	var numFiles = 0;
	this.each(function() {
		var i, length = this.files.length;
		numFiles += length;
		for (i = 0; i < length; i++) {
		name = this.files[0]
			formData.append(this.name, this.files[i]);
			console.log(this.name)
			console.log(this.files[i])
		}
	});

	// if we have post data too

	var def = new $.Deferred();
	if (numFiles > 0) {
		// do the ajax request
		$.ajax({
			url: remote,
			type: "POST",
			xhr: function() {
				myXhr = $.ajaxSettings.xhr();
				if(myXhr.upload && progressFn){
					myXhr.upload.addEventListener("progress", function(prog) {
						var value = ~~((prog.loaded / prog.total) * 100);

						// if we passed a progress function
						if (typeof progressFn === "function") {
							progressFn(prog, value);

						// if we passed a progress element
						} else if (progressFn) {
							$(progressFn).val(value);
						}
					}, false);
				}
				return myXhr;
			},
			data: formData,
			dataType: "json",
			cache: false,
			contentType: false,
			processData: false,

			success: function(response){
            successFunction(response)
      },
			complete: function(res) {
				var json;
				try {
					json = JSON.parse(res.responseText);
				} catch(e) {
					json = res.responseText;
				}
				if (typeof successFn === "function") successFn(json);
				def.resolve(json);
			}
		});
	} else {
		def.reject();
	}

	return def.promise();
};


function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', URL.createObjectURL(new Blob([text], {
                  type: "application/octet-stream"
            })));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

function successFunction(response){
    console.log("functie")
    console.log(response)

    $("#verificare").css("display","block")
    var file = document.getElementById("file1");
    file.value = file.defaultValue;
    document.getElementById("prog").value=0;
    rsp = response["result"]

    var div = document.getElementById('p1');


    if( rsp == -1){
        div.innerHTML = "Fisierul incarcat nu respecta formatul sau elementele de pe coloana principala nu sunt nenule!";
    }
    else if(rsp == 0){
        div.innerHTML = "Verificarea valorilor a esuat!";
    }
    else{
        console.log("cazul fericit");
        div.innerHTML = "Vectorul rezultat a fost creat cu succes dupa " + rsp+" iteratii!"
        $.get( "getfile/", function( data ) {

         download("valori.txt",data)

    });
    }
}



