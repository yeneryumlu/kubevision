< script lang = "ts" >

import { defineComponent } from 'vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import VueApexCharts from "vue3-apexcharts";


export default defineComponent({

    components: {
        apexchart: VueApexCharts,
    },

    name: 'HelloWorld',
    props: {
        msg: String,
    },

    setup() {
    const chartOptions = ref({
        chart: {
                    width: 380,
                    type: 'donut',
                },
                plotOptions: {
                    pie: {
                    startAngle: -90,
                    endAngle: 270
                    }
                },
                dataLabels: {
                    enabled: false
                },
                fill: {
                    type: 'gradient',
                },
                legend: {
                    formatter: function(val, opts) {
                    return val + " - " + opts.w.globals.series[opts.seriesIndex]
                    }
                },
                title: {
                    text: 'Gradient Donut with custom Start-angle'
                },
                labels: [],
                responsive: [{
                    breakpoint: 480,
                    options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
                }]
    });

    onMounted(async () => {
        const res = await axios.get("http://127.0.0.1:5000/backend");

        res["data"].forEach(function(value) {
        series.value.push(value["ValueInEUR"]);

        // construct and assign label here
        chartOptions.value.labels.push(value["Name"] as never);
        });
    });

    return {
        series,
        chartOptions, // return chartOptions
    };
}

})
</script>

  <template>
    <div id="chart">
        <apexchart type="donut" width="380" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>