import axios from 'axios'

const backendAPIURL = '/api/'


export default() => {
  const token = localStorage.getItem('token')
  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
  if (token) {
    headers.Authorization = 'Token ' + token;
  }
  return axios.create({
    baseURL: backendAPIURL,
    withCredentials: false,
    headers
  })
}
