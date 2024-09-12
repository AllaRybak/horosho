let checkbox = document.getElementById("id_is_master");
let content = document.getElementsByTagName("p")[9];
let labelTags = document.getElementsByTagName("p")[7];
let tags = document.getElementById("id_tags");
checkbox.onclick = showHide;

function showHide (){
    if (checkbox.checked) {
      content.style.visibility = "visible";
      labelTags.style.visibility = "visible";
      tags.style.visibility = "visible";
    } else {
      content.style.visibility = "hidden";
      labelTags.style.visibility = "hidden";
      tags.style.visibility = "hidden";
    }
}
showHide ();