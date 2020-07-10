/**
 * Created by mingyu.zhang on 2019/10/23.
 */
function login(){
    //var obj = {loginid:"xj",password:"96e79218965eb72c92a549dd5a330112"};
    var Id = document.getElementById("Id").value;
    var Password = document.getElementById("Password").value;
    var txt = "";
    //dbParm = JSON.stringify(obj);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange=function(){
         if( this.readyState == 4 && this.status == 200){
                myObj = JSON.parse(this.responseText);
                txt += "<table border='1'>";
                for (i in myObj){
                     txt += "<tr><td>" + myObj[i] + "</td></tr>";
                 }
                txt += "</table>";
                document.getElementById("demo2").innerHTML = txt;
          }
};
    xmlHttp.open("POST","http://10.3.2.190:6691/zh-CN/Home/BeforeLogon",true);
    xmlHttp.send("type=Login&loginid="+Id+"&password"+Password)
}
//>>>Air.append('air_9th')
//>>>Air.append('air_10th')
function show() {
    var element_1 =$("#demo3");
    var element_2 =$(".demo4");
    //element_1.text("showtime");
    var element_3 = $("b");
    element_3.textContent("showtime2");
    //element_1.innerHTML ="<b>hello</b>";
}

function create(){
    if(window.request) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST",url,true);
        xmlhttp.send();
        var xmldoc = xmlhttp.responseXML;
        var e1 = xmldoc.createElement("e1");
        var textnode1=el.createTextNode("hello");
        el.appendChild(textnode1);
        var fatherEl = xmldoc
    }
}
function test(){
    window.alert("OK");
}
function bt(){
    this.color="green";
}