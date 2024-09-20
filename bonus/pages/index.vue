<template>
    <div class="container">
      <p>{{ data }}</p>
      <tableau :tableau="[1, 4, 0, -1, 3]" />
    </div>
</template>

<script setup>
  import tableau from "~/components/table.vue"
  const { data, pending, error } = await useFetch('/api/process')

  // Optionnel : logue les erreurs ou l'état de la requête
  console.log(pending.value, error.value)
</script>
