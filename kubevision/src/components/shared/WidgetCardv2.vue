<script setup lang="ts">
const props = defineProps({
    title: String,
    hideaction: Boolean
});
</script>

<template>
    <v-card variant="outlined" elevation="0" class="withbg mb-6 overflow-hidden">
        <v-card-item>
            <v-card-title class="text-18">{{ title }}</v-card-title>
        </v-card-item>
        <v-divider></v-divider>
        <slot />
        <v-divider></v-divider>
        <v-card-actions :class="`${hideaction ? 'd-none' : ''}`">
            <slot name="footer" />
        </v-card-actions>
    </v-card>
</template>
