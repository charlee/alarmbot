function post(action) {
  const form = $("#action-form")[0];
  form.action = action;
  form.submit();
}

function enableTask(id) {
  post('/tasks/enable/' + id + '/');
}

function disableTask(id) {
  post('/tasks/disable/' + id + '/');
}

function deleteTask(id) {
  if (confirm('Are you sure to delete task ' + id + '?')) {
    post('/tasks/delete/' + id + '/');
  }
}

$(document).ready(() => {

});