/**
 * Created by mingyu.zhang on 2019/9/18.
 */
function nameinputcheckfunction() {
    var name = document.getElementById("nameinput").value
    try {
        if (name == null) throw "请输入";
        else if (typeof name != "string") throw "请输入正确格式";
        else if (name.length <= 0 || name.length >= 4) throw "长度不对";
        else {
            document.getElementById("nameinputchecknotice").innerHTML = "恭喜你";

        }
    }
    catch(err){
        document.getElementById("nameinputchecknotice").innerHTML=err
    }
}

var person={
    name:"Any",
    age:21,
    greet:function(){
        return this.name
    }
}

function people(name,age,gender){
    this.name=name,
    this.age=age,
     this.gener=gender,
      fullname=function(){
          return this.name+this.age
      }
}