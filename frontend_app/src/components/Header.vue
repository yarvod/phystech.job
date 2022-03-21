<template>

  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="btn" @click="$router.push('/')">phystech.job</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

            <b-button id="popover-button-variant" href="#" tabindex="0" size="md">Аккаунт</b-button>
            <b-popover target="popover-button-variant" variant="primary" triggers="focus" placement="bottom" size="xl">
              <template #title>Вход</template>
              <div class="text-center">
                <b-form>
                <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
                  <b-form-input id="inline-form-input-username" placeholder="e-mail"></b-form-input>
                </b-input-group>
                  <br>
                <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                  <b-form-input id="inline-form-input-password" placeholder="password"></b-form-input>
                </b-input-group>
                  <br>
                <b-button size="md" class="my-2 my-sm-0" type="submit">Войти</b-button>
                  <hr>
                  <button size="md" class="my-2 my-sm-0 btn btn-outline-primary">Регистрация</button>
                </b-form>

              </div>

            </b-popover>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>


</template>

<script>
export default {
  name: "Header",
}
</script>
