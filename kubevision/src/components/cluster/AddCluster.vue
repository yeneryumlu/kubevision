<script lang="ts">

import axios from 'axios';

export default {
    data() {
        return {
            input: {
                apiserver: '',
                token: '',
                name: '',
                environment: ''
            },
            response: ''
        };
    },
    methods: {
        onSubmit(){
            console.log(this.input)
            const clusterPromises = axios
                .post('http://localhost:5001/cluster/add', {
                    apiserver: this.input.apiserver,
                    token: this.input.token,
                    name: this.input.name,
                    environment: this.input.environment
                })
                .then(response => (this.response = response.data))
                .then(response => (this.$router.push({path: '/ui/clusters'})))
                .catch(function (error) {
                    console.log(error);
                });
        },
    }
};

</script>

<template>
    <v-row class="d-flex mb-3">
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Api server</v-label>
            <v-text-field variant="outlined" hide-details color="primary" v-model="input.apiserver"></v-text-field>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Token</v-label>
            <v-text-field variant="outlined" type=password hide-details color="primary" v-model="input.token"></v-text-field>
        </v-col>
        <v-col cols="6">
            <v-label class="font-weight-bold mb-1">Name</v-label>
            <v-text-field variant="outlined" hide-details color="primary" v-model="input.name"></v-text-field>
        </v-col>
        <v-col cols="6">
            <v-label class="font-weight-bold mb-1">Environment</v-label>
            <v-text-field variant="outlined" hide-details color="primary" v-model="input.environment"></v-text-field>
        </v-col>
        <v-col cols="12" class="pt-0">
            <v-btn @click="onSubmit" to="/ui/addcluster/" color="primary" size="large" block flat>Add Cluster</v-btn>
        </v-col>
    </v-row>
</template>
