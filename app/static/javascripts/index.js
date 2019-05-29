

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


var Reiknivel = (function(){

    var $form = $(form)

    var init = function(){
        console.log("init")   
    }

    var getData = function(){
        var data = $form.serializeArray()
        console.log(data)
        return 0
    }
    
    var calculateForm = function(){
        var data = getData()
        return data
    }

    return {
        calculateForm: calculateForm
    }

}).init()

$(document).on("keyup", ".format-money", function(e){
    var $input = $(this)
    var val = parseInt($input.val().split(".").join(""))

    if(val > 0 && (e.keyCode !== 9 || e.keyCode !== 16)){
        $input.val(val.formatMoney(0,"","."))
    }
});

$('.format-money').keyup(_.debounce(function(){
    Reiknivel.calculateForm()
} , 500));

$(document).on("click", ".dropdown a", function(){
    $el = $(this)
    $el.closest('.dropdown').find('button').text($el.text())
});

Highcharts.chart('graph-container', {

    title: {
        text: 'Heildartekjuþróun miðað við gefnar forsendur'
    },


    yAxis: {
        title: {
            text: 'Laun í krónum á mánuði'
        }
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 0
        }
    },

    series: [{
        name: 'Laun',
        data: [50000, 120000, 170000, 220000, 200000, 250000, 320000, 380000]
    }],

    credits: {
        enabled: false
    },

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});

