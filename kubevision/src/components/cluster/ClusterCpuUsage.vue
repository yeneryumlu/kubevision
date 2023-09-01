<script setup lang="ts">
import { ref } from 'vue';
import { computed } from 'vue';
import { useTheme } from 'vuetify';
// import { onMounted } from 'vue'
// import axios from 'axios';
const theme = useTheme();
const primary = theme.current.value.colors.primary;
const secondary = theme.current.value.colors.secondary;
const select = ref('March 2023');
const items = ref(['March 2023', 'April 2023', 'May 2023']);

// let clusterSeries = onMounted(async () => {
//     var url = 'http://localhost:5001/clustermetrics';

//     axios({
//         method: 'GET',
//         url: url,
//     }).then(function(response) {
//         console.warn(response.data)
//         charts.value.series = response.data.cpu_series
//     })
// });

let chartOptions = computed(() => {
    
    return {
        series: [
            { name: "Alpha", data: [1376,1389,1290,1398,1415,1308,1360,1390] },
            { name: "Delta", data: [14880,12656,12260,12692,12760,12432,12540,12660] },
            { name: "Lambda", data: [12428,12467,12170,12494,12545,12224,12380,12470] },
            { name: "Theta", data: [24904,24956,24560,24992,25060,24632,24840,24960] },
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
                max: 30000,
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
                <div><v-card-title class="text-h5">Cluster Cpu Usage - Last 7 Days</v-card-title></div>
            </div>
            <div class="mt-6">
                <apexchart type="bar" height="370px" :options="chartOptions.chartOptions" :series="chartOptions.series" ref="chart">
                </apexchart>
            </div>
        </v-card-item>
    </v-card>
</template>