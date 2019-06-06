

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

chart = new Highcharts.chart('graph-container', {

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


var Reiknivel = (function(){

    var getData = function(){
        let dropdowns = document.querySelectorAll('.dropdown-toggle')
        , inputs = document.querySelectorAll('input')
        
        let d = {}
        
        dropdowns.forEach(element => {
            d[element.getAttribute('name')] = element.textContent
        });
        inputs.forEach(element => {
            d[element.getAttribute('name')] = parseInt((element.value).replace(".",""))
        })
        return d
    }

    var calulateFormFromData = function(data){
        d = $.Deferred()
        $.post("/calculate", data, function(response){
            d.resolve(response)
        })
        return d.promise();
    }

    var reRenderGraph = function(data){
        chart.series[0].setData(data["data"],true)
    }
    
    var calculateFormAndRenderGraph = function(){
        var data = getData()
        calulateFormFromData(data).then(function(data){
            data = JSON.parse(data)
            reRenderGraph(data)
        })
    }
    
    return {
        calculateFormAndRenderGraph: calculateFormAndRenderGraph
    }

}())


$(document).on("keyup", ".format-money", function(e){
    var $input = $(this)
    var val = parseInt($input.val().split(".").join(""))

    if(val > 0 && (e.keyCode !== 9 || e.keyCode !== 16)){
        $input.val(val.formatMoney(0,"","."))
    }
});

$('.format-money').keyup(_.debounce(function(){
    output = Reiknivel.calculateFormAndRenderGraph()
} , 1000));

$(document).on("click", ".dropdown a", function(){
    $el = $(this)
    $el.closest('.dropdown').find('button').html($el.text() + " <span class='caret'></span>")
}).on("click", ".main-dropdown", function(){
    let $link = $(this)
    , $row = $link.parents('tr').nextUntil(".overgroup")
    if($row.css('display') === 'none'){
        $link.find('.glyphicon').removeClass('glyphicon-plus-sign').addClass('glyphicon-minus-sign')
    } else {
        $link.find('.glyphicon').removeClass('glyphicon-minus-sign').addClass('glyphicon-plus-sign')
    }
    $row.toggle()
})


