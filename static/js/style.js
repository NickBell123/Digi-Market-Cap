$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.datepicker').datepicker();
    $('select').formSelect();
    
   
    $('#myCoinTable').DataTable({
        "dom":"ftip",
        "paging": true,
        "pageLength": 50           
    });

    $('#mybagTable').DataTable({
        "paging": false, 
        "searching": false,
        "columnDefs": [{
            "targets":[7,8,9],
            "orderable": false
        }]       
    });
    
    let myValues = []
    
    myVal = $('.pieChart_value')
    for (vals of myVal)
        myValues.push(parseFloat(vals.textContent.slice(1)))


    let myLabels = []
    
    myLab = $('.assetName')
    for (lab of myLab)
        myLabels.push(lab.textContent)

    var data = {
        series: myValues 
      }
      
      var sum = function(a, b) { return a + b };
      
      new Chartist.Pie('.ct-chart', data, {
        labelInterpolationFnc: function(value, idx) {
          let percentage = Math.round(value / data.series.reduce(sum) * 100) + '%';
          return myLabels[idx] +' '+ percentage;
        }, 
      });
});

