<script lang="ts">
import axios from "axios";
import NodeTable from '@/components/node/NodeTable.vue';

export default {
    components: {
        NodeTable
    },
    props: {
        name: String,
    },
    data() {
        return {
            node_number: 0,
            status: "loading",
            detail: {
                node_count: 0,
                environment: "",
                api_server: "",
                nodes: [
                    {
                        "name": "unknown",
                        "cpu_capacity":0,
                        "memory_capacity":0
                    }
                ]
            }
        };
    },
    mounted() {
        let vm = this;   
        let detail: any;
        const clusterPromises = axios
            .get("http://localhost:5001/cluster/detail/"+this.name)
            .then((response) => (detail = response.data));
        Promise.all([clusterPromises])
            .then(() => {
                this.status = "done";
                this.detail = detail;
            })
            .catch(() => {
                this.status = "error";
            });
    },
}
</script>
<template>
    <v-row>
        <v-col cols="12">
            <v-row>
                <v-col>
                    <v-card height="200" width="450" style="font-size:0.8em"  elevation="10" class="withbg">
                        <v-card-title style="font-size:1em">Cluster Details</v-card-title>
                        <v-card-item>
                            <v-row>
                                <v-col>
                                    <v-row>
                                        <v-col>
                                            <p>Name:</p>
                                        </v-col>
                                        <v-col>
                                            <p>{{ name }}</p>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <p>Environment:</p>
                                        </v-col>
                                        <v-col>
                                            <p>{{ detail.environment }}</p>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <p>Api server:</p>
                                        </v-col>
                                        <v-col>
                                            <p>{{ detail.api_server }}</p>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <p>Number of nodes:</p>
                                        </v-col>
                                        <v-col>
                                            <p>{{ detail.node_count }}</p>
                                        </v-col>
                                    </v-row>
                                </v-col>
                            </v-row>
                        </v-card-item>
                    </v-card>
                </v-col>
                <v-col>
                    <v-card height="500" width="450" style="font-size:0.8em"  elevation="10" class="withbg">
                        <v-card-title style="font-size:1em">Cluster Nodes</v-card-title>
                        <v-card-item>
                            <v-row>
                                <v-table density="compact" fixed-header height="300">
                                    <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>Cpu Capacity</th>
                                            <th>Memory Capacity</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="item in detail.nodes" key="item.name">
                                            <td>{{ item.name }}</td>
                                            <td>{{ item.cpu_capacity }}</td>
                                            <td>{{ item.memory_capacity }}</td>
                                        </tr>
                                    </tbody>
                                </v-table>
                            </v-row>
                        </v-card-item>
                    </v-card>
                    
                </v-col>
            </v-row>
        </v-col>
    </v-row>

</template>
