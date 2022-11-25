
var table = document.getElementById("myTable");
var x_mas = [];
var aet_g = [];
var api_g = []
for(var i = 1; i < table.rows.length; i++){
	x_mas.push(parseFloat(table.rows[i].cells[2].innerHTML));
	aet_g.push(parseFloat(table.rows[i].cells[1].innerHTML));
	api_g.push(parseFloat(table.rows[i].cells[3].innerHTML));
}

var cria_divg = document.createElement('canvas');
cria_divg.id = "chart_rea";
document.querySelector('#grafico').appendChild(cria_divg);
var ctx = document.getElementById('chart_rea').getContext('2d');
var li = [];
for (let i = 0; i < aet_g.length; i++) {
    var obj = {};
    obj['x'] = x_mas[i];
    obj['y'] = aet_g[i];
    li.push(obj)
}

var chart = new Chart(ctx, {
                    type: 'scatter',
                    
                    data: 
                    {
                        datasets: [
                            {
                                label: 'AET x Fração mássica',
                                data: li,
                                backgroundColor: 'blue',
                                pointRadius: 4,
                            },
                        ]
                    },

                    options: {
                    	responsive: true,
                    	aspectRatio: 1, 
                    
                        tooltips: {
                          mode: 'index',
                          intersect: false,
                        },
                        scales: {
                            xAxes: [{
                                type: 'linear',
                                scaleLabel: {
                                    display: true,
                                    labelString: "Fração mássica"
                                }, 
                            }],

                            yAxes: [{
                                type: 'linear',
                                scaleLabel: {
                                    display: true,
                                    labelString: "AET (°C)"
                                },
                            }],
                        }
                    },
                    
});
        
var cria_divg2 = document.createElement('canvas');
cria_divg2.id = "chart_rea2";
document.querySelector('#grafico2').appendChild(cria_divg2);
var ctx2 = document.getElementById('chart_rea2').getContext('2d');
var li2 = [];
for (let i = 0; i < api_g.length; i++) {
    var obj2 = {};
    obj2['x'] = x_mas[i];
    obj2['y'] = api_g[i];
    li2.push(obj2)
}

var chart2 = new Chart(ctx2, {
                    type: 'scatter',
                    data: 
                    {
                        datasets: [
                            {
                                label: 'API x Fração mássica',
                                data: li2,
                                backgroundColor: 'red',
                                pointRadius: 4,
                            },
                        ]
                    },

                    options: {
                    	responsive: true,
                    	aspectRatio: 1, 
                        tooltips: {
                          mode: 'index',
                          intersect: false,
                        },
                        scales: {
                            xAxes: [{
                                type: 'linear',
                                scaleLabel: {
                                    display: true,
                                    labelString: "Fração mássica"
                                }, 
                            }],

                            yAxes: [{
                                type: 'linear',
                                scaleLabel: {
                                    display: true,
                                    labelString: "°API"
                                },
                            }],
                        }
                    }
});
            
 //document.getElementById("val").innerHTML = "Sum Value = " + sumVal;
            
