$(document).ready(function () {
    function checkReminders() {
        $.get("/get_reminders", function (reminders) {
            reminders.forEach(function (task) {
                alert("⏰ Reminder: " + task.task_name);
            });
        });
    }

    $(".delete-task").click(function () {
        let taskId = $(this).data("id");
        $.post("/delete/" + taskId, function () {
            location.reload();
        });
    });

    setInterval(checkReminders, 30000); // Check every 30 seconds
});
