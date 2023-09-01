<script>
import axios from 'axios';

export default {
    data() {
        return {
            nodes: {}
        };
    },
    mounted() {
        const clusterPromises = axios
            .get('http://localhost:5001/node')
            .then(response => (this.nodes = response.data));
    },
    methods: {
    }
};
</script>


<template>
    <v-table density="compact" fixed-header height="600">
        <thead>
            <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Cluster</th>
                <th class="text-left">Cpu Capacity (mCPU)</th>
                <th class="text-left">Memory Capacity (MB)</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in nodes" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.cluster }}</td>
                <td>{{ item.cpu_capacity }}</td>
                <td>{{ item.memory_capacity }}</td>
            </tr>
        </tbody>
    </v-table>
</template>


