$(document).ready(function () {
    $('.datepicker').datepicker();
    $('select').formSelect();
   
    $('#myTable').DataTable({
        "paging":   false,
        "search": false
    });
    
});