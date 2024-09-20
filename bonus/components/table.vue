<template>
    <div class="Hej d-flex flex-column justify-content-center align-items-center">
        <div class="ligne d-flex justify-content-center align-items-center" v-for="y in index" :key="y">
            <div class="block" v-for="x in index" :key="x">
                <div v-if="props.tableau[x - 1] == y - 1" style="height: 100%; width: 100%; background-color: black;"></div>
            </div>
        </div>
    </div>
</template>

<style>
    .Hej {
        background-color: red;
        height: 300px;
        width: 300px;
        -webkit-transform: scaleX(-1);
        transform: scaleX(-1);
        rotate: 180deg;
    }

    .ligne {
        background-color: rgb(143, 143, 143);
        height: 100%;
        width: 100%;
    }

    .block {
        background-color: rgb(233, 233, 233);
        height: 100%;
        width: 100%;
        border: 1px solid #000000;
    }
</style>

<script setup>
    const index = ref();
    const props = defineProps({
        tableau: Array
    });

    onMounted(() => {
        index.value = props.tableau.length;
    });
</script>