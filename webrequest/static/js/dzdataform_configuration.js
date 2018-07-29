Dropzone.options.dzDataForm = false;

$(document).ready(function() {
    // change the button color if all necessary files are on board
    var submitButtonSwitch = function(file) {
        if ((dropzoneMaxFiles > 0 && myDropzone.getAcceptedFiles().length == dropzoneMaxFiles) || (dropzoneMaxFiles == -1 && myDropzone.getAcceptedFiles().length > 0)) {
            $("#dzDataSubmit").addClass("fullForm");
        } else {
            $("#dzDataSubmit").removeClass("fullForm");
        }
    }

    $("#dzDataForm").dropzone({
        paramName: "file", // The name that will be used to transfer the file
        uploadMultiple: true,
        parallelUploads: (dropzoneMaxFiles == -1) ? 1024 : dropzoneMaxFiles,
        autoProcessQueue: false,
        previewTemplate: "<div class=\"dz-preview dz-file-preview\">\n<div class=\"dz-details\">\n<img data-dz-thumbnail />\n<div class=\"dz-filename\"><span data-dz-name></span></div>\n<div class=\"dz-remove-container\"><a class=\"dz-remove\" href=\"javascript:undefined;\" data-dz-remove>Remove</a></div>\n<div class=\"dz-size\" data-dz-size></div>\n</div>\n<div hidden class=\"dz-progress\"><span class=\"dz-upload\" data-dz-uploadprogress></span></div>\n<div class=\"dz-success-mark\"><span></span></div>\n<div class=\"dz-error-mark\"><span></span></div>\n<div class=\"dz-error-message\"><span data-dz-errormessage></span></div></div>",

        init: function() {
            myDropzone = this;


            switch (dropzoneMaxFiles) {
                case -1:
                    $("#droppedFilesCounter").text("Drop your files here");
                    break
                case 1:
                    $("#droppedFilesCounter").text("Drop 1 file here");
                    break;
                default:
                    $("#droppedFilesCounter").text("Drop " + String(dropzoneMaxFiles) + " files here");
            }

            myDropzone.on("addedFiles", submitButtonSwitch);
            myDropzone.on("removedfile", submitButtonSwitch);

            document.querySelector("#dzDataSubmit").addEventListener("click", function() {
                if ((dropzoneMaxFiles > 0 && myDropzone.getAcceptedFiles().length == dropzoneMaxFiles) || (dropzoneMaxFiles == -1 && myDropzone.getAcceptedFiles().length > 0)) {
                    myDropzone.processQueue();

                    $("#dzDataForm, #submission").css({opacity: 0.0, visibility: "hidden"}).animate({opacity: 0}, 200, function(){
                        $("#dzDataForm, #submission").remove();
                    });
                    $('#request').prepend("<div id=\"downloadContainer\"></div>");
                    $('#downloadContainer').html("<div id=\"download\"><img src=\"/static/img/loading.gif\"/></div>");
                }
            });

            myDropzone.on("successmultiple", function(file, responseText) {
                $('#downloadContainer').html("<div id=\"download\">\n<img src=\"/static/img/download.png\"/>\n<p>\n<span class=\"mediumText\"><b><a href=\"\">Your report is ready</a></b></span>\n<br>\n<span class=\"smallText\">Download will start shortly</span>\n</p>\n</div>");
                $('#download > p > span:eq(0) > b > a').attr("href", responseText);

                setTimeout(function(){
                    $('#download > p > span:eq(0) > b > a')[0].click();
                }, 500);
            });
        },

        error: function (file, errorMessage) {
            if (typeof(errorMessage) !== "string") {
                $("div.serverError").css("visibility", "visible");
                $("div.serverError").text(errorMessage);
            }
        },

        dragenter: function(event){
            $("#dzDataForm").addClass("hover");
        },

        dragleave: function(event){
            $("#dzDataForm").removeClass("hover");
        },

        drop: function(event){
            $("#dzDataForm").removeClass("hover");
        },

        accept: function(file, done) {
            var re = /(?:\.([^.]+))?$/;
            var ext = re.exec(file.name)[1];
            ext = ext.toUpperCase();

            fileNameTrimmed = file.name.substr(0,Math.min(30, file.name.length)) + "..."

            if (allowedExtentions.split(",").includes(ext)) {
                file.previewElement.querySelectorAll("[data-dz-thumbnail]")[0].src = "/static/img/excel.png";
                file.previewElement.querySelectorAll("[data-dz-name]")[0].firstChild.nodeValue = fileNameTrimmed
                done();
                // have to call it here because there is not specific event for file added to queue in Dropzone.js
                submitButtonSwitch();
            }
            else {
                file.previewElement.querySelectorAll("[data-dz-thumbnail]")[0].src = "/static/img/notexcel.png";
                file.previewElement.querySelectorAll("[data-dz-name]")[0].firstChild.nodeValue = fileNameTrimmed
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
