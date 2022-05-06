<template>

  <b-card-group deck>
    <TaskItem
      v-for="task of tasks"
      :key="task.id"
      :task="task"
      :edit="false"
    />
  </b-card-group>

</template>

<script>
import TaskItem from "@/components/TaskItem";

export default {
  name: "TaskList",
  props: ['tasks'],
  components: {TaskItem},
}
</script>

<style scoped>

</style>