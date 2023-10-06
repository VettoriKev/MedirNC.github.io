var ctx = document.getElementById("myChart").getContext("2d");
var chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["2023-07-20", "2023-07-21", "2023-07-22"],
        datasets: [{
            label: "Temperatura",
            data: [25, 26, 27],
            borderColor: "red",
            fill: false
        }, {
            label: "Humedad",
            data: [50, 51, 52],
            borderColor: "blue",
            fill: false
        }]
    },
    options: {
        title: {
            text: "Gráfico de datos"
        }
    }
});
