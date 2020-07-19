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
    
    myValues = []

    myVal = $('.current_value')
    for (vals of myVal)
        myValues.push(parseFloat(vals.textContent.slice(1)))
    
    
    var data = {
        series: myValues
      };
      
      var sum = function(a, b) { return a + b };
      
      new Chartist.Pie('.ct-chart', data, {
        labelInterpolationFnc: function(value) {
          return Math.round(value / data.series.reduce(sum) * 100) + '%';
        }
      });
    
});