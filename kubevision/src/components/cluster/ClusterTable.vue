<script>
import axios from 'axios';

export default {
    data() {
        return {
            clusters: {}
        };
    },
    mounted() {
        const clusterPromises = axios
            .get('http://localhost:5001/cluster')
            .then(response => (this.clusters = response.data));
    },
    methods: {
    }
};
</script>

<template>
    <v-card elevation="10" class="withbg">
        <v-card-item>
            <v-table density="compact" fixed-header height="200">
                <thead>
                    <tr>
                        <th class="text-left">Name</th>
                        <th class="text-left">Environment</th>
                        <th class="text-left">Status</th>
                        <th class="text-left">Version</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in clusters" :key="item.name">
                        <td><router-link v-bind:to="'/ui/cluster/' + item.name">{{ item.name }}</router-link></td>
                        <td>{{ item.environment }}</td>
                        <td>{{ item.status }}</td>
                        <td>{{ item.version }}</td>
                    </tr>
                </tbody>
            </v-table>
        </v-card-item>
    </v-card>
</template>


