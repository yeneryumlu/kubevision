<script setup lang="ts">
import ClusterTable from '@/components/cluster/ClusterTable.vue';
import ClusterCpuUsage from '@/components/cluster/ClusterCpuUsage.vue';
import ClusterMemoryUsage from '@/components/cluster/ClusterMemoryUsage.vue';
</script>

<template>
    <v-row>
        <p><b>All Clusters</b></p>
        <br><br><br>
    </v-row>
    <v-row>
        <v-col cols="12" md="6">
            <ClusterTable />
        </v-col>
        <v-col cols="3" md="3">
            <v-btn to="/ui/addcluster" color="primary" size="large" block flat>Add New Cluster</v-btn>
        </v-col>
    </v-row>
    <v-row>
        <v-col >
            <ClusterCpuUsage/>
        </v-col>
    </v-row>
    <v-row>
        <v-col >
            <ClusterMemoryUsage/>
        </v-col>
    </v-row>
</template>



