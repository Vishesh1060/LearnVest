const ctx = document.getElementById('myChart').getContext('2d');
let yvals=cval;
let yvalsb=[]
let i=0;
const myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [1],
    datasets: [{ 
        data: yvals,
        label: "Axis Bank",
        borderColor: "#e8c3b9",
        fill: false
      }, { 
        data: yvalsb,
        label: "Tata motors",
        borderColor: "#c45850",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: ''
    }
  }
});
let changedata = function (){
    i+=1;
    yvalsb.push(i*100+200);
    yvals.push(i+i*i*50);
    myChart["data"].labels.push(i);
    myChart.update();
}
    