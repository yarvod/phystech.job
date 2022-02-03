<template>

  <g-signin-button
    v-if="isEmpty(user)"
    :params="googleSignInParams"
    @success="onGoogleSignInSuccess"
    @error="onGoogleSignInError"
  >
    <button class="btn btn-block btn-success">
      Google Sign in
    </button>
  </g-signin-button>
  <router-link v-else to="/account">Личный кабинет</router-link>

</template>


<script>
import axios from 'axios'
export default {
  name: 'AuthSection',
  data () {
    return {
      user: {},
      googleSignInParams: {
        client_id: '118147770390-atqe10tv5h348abk8vbmn62db3700k0a.apps.googleusercontent.com'
      }
    }
  },
  methods: {
    onGoogleSignInSuccess (resp) {
      const token = resp.Zi.access_token
      // После успешного входа через Google,
      // отправляем токен доступа на бэкэнд и получаем взамен
      // пользователя и JWT токен
      // P.S. JWT токен в нашем примере не нужен, поэтому его не сохраняем
      axios.post('http://localhost/auth/google/', {
        access_token: token
      })
        .then(resp => {
          this.user = resp
        })
        .catch(err => {
          console.log(err.response)
        })
    },
    onGoogleSignInError (error) {
      console.log('OH NOES', error)
    },
    isEmpty (obj) {
      return Object.keys(obj).length === 0
    }
  }
}
</script>