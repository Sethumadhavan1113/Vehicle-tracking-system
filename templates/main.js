$(document).ready(function () {
    // Get existing tasks from the backend
    $.get('/tasks', function (data) {
        data.forEach(function (task) {
            addTaskToUI(task);
        });
    });

    // Add a new task
    $('#task-form').submit(function (event) {
        event.preventDefault();
        var title = $('#title').val();
        var description = $('#description').val();
        $.post('/tasks', JSON.stringify({ title: title, description: description }), function () {
            var newTask = { title: title, description: description };
            addTaskToUI(newTask);
            $('#title').val('');
            $('#description').val('');
        });
    });

    // Helper function to add a task to the UI
    function addTaskToUI(task) {
        $('#task-list').append('<div><h3>' + task.title + '</h3><p>' + task.description + '</p></div>');
    }
});
