Dropzone.options.dzDataForm = false;

$(document).ready(function(){
    $("#dzDataForm").dropzone({
        paramName: "file", // The name that will be used to transfer the file
        maxFiles: 2,
        uploadMultiple: true,
        autoProcessQueue: false,
        previewTemplate: "<div class=\"dz-preview dz-file-preview\">\n<div class=\"dz-details\">\n<img data-dz-thumbnail />\n<div class=\"dz-filename\"><span data-dz-name></span></div>\n<div class=\"dz-remove-container\"><a class=\"dz-remove\" href=\"javascript:undefined;\" data-dz-remove>Remove</a></div>\n<div class=\"dz-size\" data-dz-size></div>\n</div>\n<div hidden class=\"dz-progress\"><span class=\"dz-upload\" data-dz-uploadprogress></span></div>\n<div class=\"dz-success-mark\"><span></span></div>\n<div class=\"dz-error-mark\"><span></span></div>\n<div class=\"dz-error-message\"><span data-dz-errormessage></span></div></div>",

        init: function() {
            myDropzone = this;

            $("#droppedFilesCounter").text("2");

            document.querySelector("#dzDataSubmit").addEventListener("click", function() {
                if (myDropzone.getAcceptedFiles().length == 2) {
                    myDropzone.processQueue();
                }
            });

            myDropzone.on("addedfiles", function(file) {
               if (myDropzone.getAcceptedFiles().length == 2) {
                   $("#dzDataSubmit").addClass("fullForm");
               }
            });

            myDropzone.on("removedfile", function(file) {
               if (myDropzone.getAcceptedFiles().length < 2) {
                   $("#dzDataSubmit").removeClass("fullForm");
               }
            });

            myDropzone.on("successmultiple", function(file, responseText) {
                $('.dz-file-preview').css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0}, 200);
                $('.dz-file-preview').remove();

                $("#dzDataForm").css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0}, 200);
                $('#submission').css({opacity: 1.0, visibility: "visible"}).animate({opacity: 0}, 200, function(){
                    $('#request').prepend("<div id=\"downloadContainer\">\n<div id=\"download\">\n<img src=\"/static/img/download.png\"/>\n<p>\n<span class=\"mediumText\"><b><a href=\"\">Your report is ready</a></b></span>\n<br>\n<span class=\"smallText\">Download will start shortly</span>\n</p>\n</div>\n</div>");
                    $('#download > p > span:eq(0) > b > a').attr("href", responseText);
                });

                setTimeout(function(){
                    $('#download > p > span:eq(0) > b > a')[0].click();
                }, 500);
            });
        },

      maxfilesexceeded: function (file) {
          this.removeFile(file);
      },

      dragenter: function(event){
          console.log("here?");
         $("#dzDataForm").addClass("hover");
      },

      dragleave: function(event){
          console.log("left?")
          $("#dzDataForm").removeClass("hover");
      },

      drop: function(event){
          $("#dzDataForm").removeClass("hover");
      },

      accept: function(file, done) {
          var re = /(?:\.([^.]+))?$/;
          var ext = re.exec(file.name)[1];
          ext = ext.toUpperCase();

          if (ext == "XLS" || ext == "XLSX" || ext == "XLSM") {
              file.previewElement.querySelectorAll("[data-dz-thumbnail]")[0].src = "/static/img/excel.png";
              done();
          }
          else {
              file.previewElement.querySelectorAll("[data-dz-thumbnail]")[0].src = "/static/img/notexcel.png";
              file.previewElement.querySelectorAll(".dz-remove-container")[0].style.visibility = "hidden";
              file.previewElement.querySelectorAll(".dz-filename")[0].style["text-decoration"] = "line-through";

              myDropzone = this;
              setTimeout(function(){myDropzone.removeFile(file);}, 2000)
              done("Sorry, we accept only Excel files.");
          }
      },

      thumbnail: function thumbnail(file, dataUrl) {
          //disable showing previews for photos
      },
  });

});
