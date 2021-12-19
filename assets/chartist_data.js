console.log('************ Run Chartist *******************')

setTimeout(function() {

  new Chartist.Line('#traffic-chart', {
    labels: ['January', 'Februrary', 'March', 'April', 'May', 'June'],
    series: [
      [23000, 25000, 19000, 34000, 56000, 64000]
    ]
  }, {
    low: 0,
    showArea: true
  });

}, 1000);





