/**
 * Created by rahilvora on 7/14/17.
 */
console.log("File loaded");
$("#pickup").on('click', function(){
    debugger;
    setTimeout(function () {
        $("#myModal").hide();
        $("#myModa2").show();

    }, 5000);
});
var secretCode = ["554-2355-998", "554-2325-998", "744-7655-934", "554-2555-945", "594-7345-945", "794-7385-945"];
function random() {
    debugger;
    setTimeout(function () {
        var indexOfSecretCode = Math.floor(Math.random() * 6) + 1; // Between 1 and 6
        $(".modal-body").text("Share this code with the receiver to assure his availability. " + secretCode[indexOfSecretCode-1]);
        $("#myModalLabel").text("Done");
        //$("#myModa2").show();

    }, 5000);
}

function acceptPackage() {
    debugger;
    console.log($("#package_number").val());
    if(secretCode.indexOf($("#package_number").val()) == -1){
        $(".modal-body").text("Secret Code is Invalid");
        $("#myModalLabel").text("Done");
    }
    else {
        $(".modal-body").text("Secret code accepted. Package is schedule for the delivary");
        $("#myModalLabel").text("Done");
    }
}
