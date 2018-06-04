
// Based on http://bl.ocks.org/d3noob/b3ff6ae1c120eea654b5 :

// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 90, bottom: 30, left: 50},
    width = 700 - margin.left - margin.right,
    height = 320 - margin.top - margin.bottom;

// Set the ranges
var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

var formatValue = d3.format(",.0f"),
  bisect = d3.bisector(function(d) { return d.x; }).left;
  formatCurrency = function(d) { return formatValue(d) + " kr."; };

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.x); })
    .y(function(d) { return y(d.y); });

// Adds the svg canvas
d3.select("#maindiv${divnum}").selectAll("svg").remove();
var svg = d3.select("#maindiv${divnum}")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
//d3.csv("data.csv", function(error, data) {
var data = $data;

    data.forEach(function(d) {
        d.x = +d.x;
        d.y = +d.y;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.x; }));
    y.domain([0, d3.max(data, function(d) { return d.y; })]);

    // Add the valueline path
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 9)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Radstofunartekjur");

    svg.append("path")
        .datum(data)
        .attr("class", "valueline")
        .attr("d", valueline);

    var focus = svg.append("g")
        .attr("class", "focus")
        .style("display", "none");

    focus.append("circle")
        .attr("r", 4.5);

    focus.append("text")
        .attr("x", 9)
        .attr("dy", ".35em");

    focus.append("line")
        .attr("class", "x-hover-line hover-line")
        .attr("y1", 0)
        .attr("y2", height);



    // adding a background
    svg.append("rect")
        .attr("class", "overlay")
        .attr("width", width)
        .attr("height", height)
        .on("mouseover", function() { focus.style("display", null); })
        .on("mouseout", function() { focus.style("display", "none"); })
        .on("mousemove", mousemove);

    function mousemove() {
      var x0 = x.invert(d3.mouse(this)[0]),
          i = bisect(data, x0, 1),
          d0 = data[i - 1],
          d1 = data[i],
          d = x0 - d0.x > d1.x - x0 ? d1 : d0;
      focus.attr("transform", "translate(" + x(d.x) + "," + y(d.y) + ")");
      focus.select("text").text(formatCurrency(d.y));
      focus.select(".x-hover-line").attr("y2", height - y(d.y));
    }
//});
