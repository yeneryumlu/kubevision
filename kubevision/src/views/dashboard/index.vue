<script setup lang="ts">
/*Call Components*/
import YearlyBreakup from '@/components/dashboard/YearlyBreakup.vue';
import MonthlyEarning from '@/components/dashboard/MonthlyEarnings.vue';
import RecentTransaction from '@/components/dashboard/RecentTransaction.vue';
import ClusterCpuUsage from '@/components/cluster/ClusterCpuUsage.vue'
</script>
<template>
    <v-row>
        <v-col cols="12">
            <v-row>
                <v-col cols="12" lg="8">
                    <ClusterCpuUsage/>
                </v-col>
                <v-col cols="12" lg="4">
                    <div class="mb-6">
                        <YearlyBreakup />
                    </div>
                    <div>
                        <MonthlyEarning />
                    </div>
                </v-col>
                <v-col cols="12" lg="12">
                    <RecentTransaction />
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>