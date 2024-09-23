<template>
    <div class="d-flex flex-column justify-content-center align-items-center" style="width: 100%;">
        <template v-for="element in data.output">
            <div class="mb-3">
                <p style="background-color: gray; margin: 1;">{{ element.table }}</p>
                <tableau :tableau="element.table" />
            </div>
        </template>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import tableau from "~/components/table.vue"

    // Déclarer la variable qui stockera les données traitées (tableau vide)
    const truc = ref([]);
    const test = [0, -1, -1, -1, 3]

    // Attendre les données au moment du rendu initial avec useFetch
    const { data, error } = await useFetch('/api/process');

    console.log(data.value.output)

    // Vérifier que les données sont bien disponibles avant de les utiliser
    // if (data && data.value && data.value.output) {
    //     // Suppression des sauts de ligne avec split
    //     let list = data.value.output.split("\n");

    //     // Boucler sur chaque ligne de l'output
    //     list.forEach(element => {
    //         // Splitter chaque élément par " : "
    //         let tmp = element.split(" : ");

    //         // Corriger la structure pour un format JSON valide
    //         let correctedInput = tmp[1].replace(/\(/g, '[').replace(/\)/g, ']');

    //         try {
    //             // Parse la chaîne JSON corrigée
    //             let parsedArray = JSON.parse(correctedInput);

    //             // Transformer chaque élément du tableau en un objet
    //             let result = parsedArray.map(item => {
    //                 return {
    //                     table: item[0],
    //                     score: item[1]
    //                 };
    //             });

    //             // Ajouter les objets à truc.value
    //             truc.value.push(...result);
    //         } catch (error) {
    //             console.error("Erreur lors du parsing JSON:", error);
    //         }
    //     });
    // } else {
    //     console.error("Erreur: Les données ne contiennent pas 'output'.");
    // }
</script>

