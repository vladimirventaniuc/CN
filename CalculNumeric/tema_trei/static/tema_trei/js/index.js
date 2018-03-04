jQuery(document).ready(function($)
{

$("#sum").click(function()
  {
    $.get( "getSum/", function( data ) {

      download("suma.txt",data)
      hideButtons()
    });
  })

$("#prod").click(function()
  {
    $.get( "getProd/", function( data ) {

      download("produs.txt",data)
      hideButtons()
    });
  })
 $("#ex2").click(function()
  {
    $("#ex2_wrap").slideToggle( "slow");
    $("#verificare").css("display","none")
    $("#upload2").on("click",function(){


    $(".myFile2").upload("check/",
     {myData:"hey",
     foo:"bar"
     },
     function(success){
        console.log("done");
    },$("#prog2"),1)


        });
    });


  $("#ex1").click(function()
  {
     $("#verificare").css("display","none")

    $("#ex1_wrap").slideToggle( "slow");

    $("#upload").on("click",function(){


    $(".myFile").upload("upload/",
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
			if(nr==0){
                console.log(response);
                $("#showButtons").css("display", "block");
                }
               else{

                displayResponse(response)
               }


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


function hideButtons(){
var file = document.getElementById("file1");
    file.value = file.defaultValue;
    var file = document.getElementById("file2");
    file.value = file.defaultValue;
    document.getElementById("prog").value=0;
    $("#showButtons").css("display", "none");
}

function displayResponse(response){
    $("#verificare").css("display","block")


    var div = document.getElementById('p1');

    div.innerHTML += response["result1"];
    var div = document.getElementById('p2');

    div.innerHTML += response["result2"];
    var file = document.getElementById("file12");
    file.value = file.defaultValue;
    var file = document.getElementById("file22");
    file.value = file.defaultValue;
    document.getElementById("prog2").value=0;
}
