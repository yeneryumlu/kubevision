
<script>
import axios from "axios";
import VueApexCharts from "vue3-apexcharts";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      status: "loading",
      series: null,
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
        },
        stroke: {
          width: 1,
          colors: ["#fff"],
        },
        title: {
          text: "Frontend Test 1 - Stacked Bar Chart",
        },
        yaxis: {
          title: {
            text: undefined,
          },
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val;
            },
          },
        },
        fill: {
          opacity: 1,
        },
      },
    };
  },
  mounted() {
    let users;
    let taskInfo;
    const userPromises = axios
      .get("https://mocki.io/v1/429711e1-59f6-4910-96bb-4e390c6b0063")
      .then((response) => (users = response.data));
    const taskInfoPromises = axios
      .get("https://mocki.io/v1/932711ca-96f8-453d-90e6-dd114ac25c25")
      .then((response) => (taskInfo = response.data));
    Promise.all([userPromises, taskInfoPromises])
      .then(() => {
        this.status = "done";
        let formatedUserData = this.maxUserDataWithTaskData(users, taskInfo);
        const xAxisLabel = formatedUserData.map((user) => {
          return user.name.split(" ")[0];
        });
        this.chartOptions = {
          ...this.chartOptions,
          xaxis: {
            categories: xAxisLabel,
            labels: {
              formatter: function (val) {
                return val;
              },
            },
          },
        };
        this.series = [
          {
            name: "Finished",
            data: formatedUserData.map((user) => {
              return user.taskComplete;
            }),
          },
          {
            name: "Remain",
            data: formatedUserData.map((user) => {
              return user.taskRemain;
            }),
          },
        ];
      })
      .catch(() => {
        this.status = "error";
      });
  },
  methods: {
    maxUserDataWithTaskData(users, taskInfo) {
      let formatedUserData = users;
      taskInfo.forEach((task) => {
        formatedUserData = formatedUserData.map((user) => {
          if (user.id === task.userId) {
            if (task.completed) {
              user.taskComplete = user.taskComplete ? user.taskComplete + 1 : 1;
            } else {
              user.taskRemain = user.taskRemain ? user.taskRemain + 1 : 1;
            }
          }
          return user;
        });
      });
      return formatedUserData;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
pre {
  max-height: 200px;
  overflow: scroll;
}
.small {
  max-width: 600px;
  margin: 150px auto;
}
</style>

<template>
  <div>
    <h4 v-if="status === 'loading'">loading...</h4>
    <apexchart
      width="500"
      type="bar"
      :options="chartOptions"
      :series="series"
      v-if="series"
    ></apexchart>
  </div>
</template>
