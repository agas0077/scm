var myModal = document.getElementById('exampleModal')
var myInput = document.getElementById('exampleModal')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})