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

    let myAsset = []

    chartAsset = $('.current_asset')
    for(coin of chartAsset){
        myAsset.push(coin.textContent)
    }
    console.log(chartAsset)
    
    let myData = []

    chartData = $('.current_value')
    for (value of chartData){
        v = value.textContent
        vnum = v.slice(1)
        num = parseFloat(vnum)
        myData.push(num)
        console.log(typeof(num))
    }

    console.log(myData)

    var data = {
        // labels: myAsset,
        series: myData
      };
      
      var sum = function(a, b) { return a + b };
      
      new Chartist.Pie('.ct-chart', data, {
        labelInterpolationFnc: function(value, idx) {
          let percentage = Math.round(value / data.series.reduce(sum) * 100) + '%';
          return myAsset[idx] + ' ' + percentage;
        }
      });
    
});