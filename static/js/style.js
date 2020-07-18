$(document).ready(function () {
    $('.datepicker').datepicker();
    $('select').formSelect();
   
    $('#myCoinTable').DataTable({
        "paging":   false,        
    });

    $('#mybagTable').DataTable({
        "paging":   false, 
        "searching": false,
        "columnDefs": [{
            "targets":[7,8],
            "orderable": false
        }]       
    });
    
});