<script setup lang="ts">
import NamespaceTable from '@/components/cluster/NamespaceTable.vue';
</script>

<template>
    <v-row>
        <p><b>All Nodes</b></p>
        <br><br><br>
    </v-row>
    <v-row>
        <v-col cols="12" md="12">
            <NamespaceTable />
        </v-col>
    </v-row>
</template>



