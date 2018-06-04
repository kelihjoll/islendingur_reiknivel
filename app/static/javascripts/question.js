
    // Extend the default Number object with a formatMoney() method:
    // usage: someVar.formatMoney(decimalPlaces, symbol, thousandsSeparator, decimalSeparator)
    // defaults: (2, "$", ",", ".")
    Number.prototype.formatMoney = function(places, symbol, thousand, decimal) {
        places = !isNaN(places = Math.abs(places)) ? places : 2;
        symbol = symbol !== undefined ? symbol : "$";
        thousand = thousand || ",";
        decimal = decimal || ".";
        var number = this, 
            negative = number < 0 ? "-" : "",
            i = parseInt(number = Math.abs(+number || 0).toFixed(places), 10) + "",
            j = (j = i.length) > 3 ? j % 3 : 0;
        return symbol + negative + (j ? i.substr(0, j) + thousand : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thousand) + (places ? decimal + Math.abs(number - i).toFixed(places).slice(2) : "");
    };


// $('.continue-btn').delegate("click", function(){
//     var form = $('.question-form').serializeArray();

//     form.forEach(function(val){
//         question_obj[val.name] = val.value;
//     })

//     console.log(form)

//     var url = location.href;
//     var q_no = parseInt(url.match(/([^\/]*)\/*$/)[1])

//     sessionStorage.setItem("question_obj", JSON.stringify(question_obj))

//     // the last question
//     if(q_no === 7){
//         redirect_url = "/analyze_results"
//     } else {
//         redirect_url = "/questions/"+(++q_no)
//     }
//     window.location.href = redirect_url;
//     return false;
// });


// single multiple choice
$(document).on("click", ".choice-container", function(){
    var $choice = $(this);
    
    $('.chosen').hide()
    $choice.find(".circle").html("<div class='chosen'></div>")
    var choiceText = $choice.find("p").text();
    $choice.siblings('form').find('input').val(choiceText)
});

// check box choice
$('.choice-container-multiple').on("click", function(){
    var $choice = $(this)
    , $input = $choice.prev('input')
    , $chosen = $choice.find(".chosen")

    if($chosen.length > 0){
        $chosen.remove()
        $input.val('')
    } else {
        $choice.find(".circle").html("<div class='chosen'></div>")
        
        var choiceText = $choice.find('p').text();
        $input.val(choiceText)
    }
});

$(document).on("keyup", ".format-money", function(e){
    var $input = $(this)
    var val = parseInt($input.val().split(".").join(""))

    if(val > 0 && (e.keyCode !== 9 || e.keyCode !== 16)){
        $input.val(val.formatMoney(0,"","."))
    }
})

var typewriter_text = ["Sæki Jónas..."]

var speed = 100, i = 0;

function typeWriter() {
  if (i < typewriter_text[0].length) {
    document.getElementsByClassName("typewriter-text")[0].innerHTML += typewriter_text[0].charAt(i);
    i++;

    // when done writing..
    if(i === typewriter_text[0].length){
        document.getElementsByClassName("typewriter-text")[0].innerHTML += "<span class='blink'>|</>";
    }
    setTimeout(typeWriter, speed);
  }
}

typeWriter()

var changeQuestion = function(html){
    var $mainContainer = $('.main-container');
    $mainContainer.children().remove()
    $mainContainer.html(html)
}

var renderQuestion = function(html){
    var $mainContainer = $('.main-container')
    $mainContainer.find(".loader-container").hide()
    $mainContainer.html(html)
}

$(document).on("click", ".btn-continue", function(){
        var url = location.href;
        var q_no = parseInt(url[url.length-1])

        
        var q_no = sessionStorage.getItem("question_number")

        console.log(q_no)

        q_no++;
        sessionStorage.setItem("question_number", q_no)

        $.get("/get_template", { question_number: q_no}, function(html){
            changeQuestion(html)
        })

        // window.location.href = redirect_url;
});

$('.format-money').on("keyup", function(e){
    var $input = $(this)
    var val = parseInt($input.val().split(".").join(""))

    if(val > 0 && (e.keyCode !== 9 || e.keyCode !== 16)){
        $input.val(val.formatMoney(0,"","."))
    }
});

setTimeout(function(){
    $.get("/get_template", { question_number: 0 }, function(html){
        sessionStorage.setItem("question_number", 0)
        renderQuestion(html)
    })
},2000)
