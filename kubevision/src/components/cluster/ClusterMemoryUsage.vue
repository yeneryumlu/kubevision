<script setup lang="ts">
import { ref } from 'vue';
import { computed } from 'vue';
import { useTheme } from 'vuetify';
// import { onMounted } from 'vue'
import axios from 'axios';
const theme = useTheme();
const primary = theme.current.value.colors.primary;
const secondary = theme.current.value.colors.secondary;
const select = ref('March 2023');
const items = ref(['March 2023', 'April 2023', 'May 2023']);

let chartops = {};
const initialize = () => {
    axios
        .get('http://localhost:5001/clustermetrics')
        .then(response => (chartops = response.data))
};

initialize();

// let clusterSeries = ref()
// onMounted(async () => {
//     // axios
//     //     .get('http://localhost:5001/cluster')
//     //     .then(response => (chartOptions.value.series.name = response.data
//     //     ))
//     let result = await axios.get("http://localhost:5001/cluster")
//     console.warn(result.data)
//     // return result.data
//     clusterSeries.value = [
//             { name: "Vega", data: [355, 390, 300, 350, 390, 180, 355, 390] },
//             { name: "Titan", data: [280, 250, 325, 215, 250, 310, 280, 250] },
//         ]
    

//     var url = 'http://my-json-server.typicode.com/apexcharts/apexcharts.js/yearly';

//     axios({
//     method: 'GET',
//     url: url,
//     }).then(function(response) {
//     chartOptions.value.series =[
//             { name: "Vega", data: [355, 390, 300, 350, 390, 180, 355, 390] },
//             { name: "Titan", data: [280, 250, 325, 215, 250, 310, 280, 10] },
//         ]
// })
// });

let chartOptions = computed(() => {
    
    return {
        series: [
            {"name": "Alpha", "data": [1918,1820,1952,1910,2012,1978,2034,2224]},
            {"name": "Delta", "data": [25706,24280,24808,24640,25048,24912,25136,25896]},
            {"name": "Lambda", "data": [33754,33460,33856,33730,34036,33934,34102,34672]},
            {"name": "Theta", "data": [60672,60280,60808,60640,58048,60912,58136,58896]},
        ],
        chartOptions: {
            grid: {
                borderColor: 'rgba(0,0,0,0.1)',
                strokeDashArray: 3,
                xaxis: {
                    lines: {
                        show: false
                    }
                },
            },
            plotOptions: {
                bar: { horizontal: false, columnWidth: "35%", borderRadius: [8] },
            },
            colors: [primary, secondary],
            chart: {
                type: "bar",
                height: 370,
                offsetX: -15,
                toolbar: { show: true },
                foreColor: "#adb0bb",
                fontFamily: 'inherit',
                sparkline: { enabled: false },
            },
            dataLabels: { enabled: false },
            markers: { size: 0 },
            legend: { show: false },
            xaxis: {
                type: "category",
                categories: ["25/08", "26/08", "27/08", "28/08", "29/08", "30/08", "31/08", "01/09"],
                labels: {
                    style: { cssClass: "grey--text lighten-2--text fill-color" },
                },
            },
            yaxis: {
                show: true,
                min: 0,
                max: 65000,
                tickAmount: 4,
                labels: {
                    style: {
                        cssClass: "grey--text lighten-2--text fill-color",
                    },
                },
            },
            stroke: {
                show: true,
                width: 3,
                lineCap: "butt",
                colors: ["transparent"],
            },
            tooltip: { theme: "light" },

            responsive: [
            {
                breakpoint: 600,
                options: {
                    plotOptions: {
                        bar: {
                            borderRadius: 3,
                        }
                    },
                }
            }
        ]

        },
    };
});
</script>
<template>
    <v-card elevation="10" class="withbg">
        <v-card-item>
            <div class="d-sm-flex align-center justify-space-between pt-sm-2">
                <div><v-card-title class="text-h5">Cluster Memory Usage - Last 7 Days</v-card-title></div>
                <!-- <div class="my-sm-0 my-2">
                    <v-select v-model="select" :items="items" variant="outlined" density="compact"
                        hide-details></v-select>
                </div> -->
            </div>
            <div class="mt-6">
                <apexchart type="bar" height="370px" :options="chartOptions.chartOptions" :series="chartOptions.series" ref="chart">
                </apexchart>
            </div>
        </v-card-item>
    </v-card>
</template>