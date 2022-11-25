/*$(document).ready(function(){    
      var i=1;
     $("#add_row").click(function(event){
       event.preventDefault();
      b=i-1;
      $('#addr'+i).html($('#addr'+b).html()).find('td:first-child').html(i+1);
      $('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
     
      i++; 
  });
     $("#delete_row").click(function(){
       if(i>1){
     $("#addr"+(i-1)).html('');
     i--;
     }
   });

});*/

$(document).ready(function(){    
     var i=1;
     $("#add_row").click(function(event){
      event.preventDefault();
      b=i-1;

      //elementos tr e td
      var tr = document.createElement("tr");
      tr.className = "tr"+i;
      var td = document.createElement("td");
      td.className = "td_nome"+i;
      var tda = document.createElement("td");
      tda.className = "td_temp"+i;
      var tdb = document.createElement("td");
      tdb.className = "td_massa"+i;
      var tdc = document.createElement("td");
      tdc.className = "td_rho"+i;
      var tdd = document.createElement("td");
      tdd.className = "td_rho_temp"+i;

      //elementos input
      var temp = document.createElement('input'); //crio um elemento do tipo input
      var massa = document.createElement('input'); //crio um elemento do tipo input
      var rho = document.createElement('input'); //crio um elemento do tipo input
      var rho_temp = document.createElement('input'); //crio um elemento do tipo input
      var nome = document.createElement("label");

      temp.name = "temp";
      temp.className = "form-control";
      temp.placeholder = "em °C";
      temp.required = "true";
      massa.name= "massa";
      massa.className = "form-control";
      massa.placeholder = "em gramas";
      rho.name = "rho";
      rho.className = "form-control";
      rho.placeholder = "Em g/cc";
      rho_temp.name = "rho_temp";
      rho_temp.className = "form-control";
      rho_temp.placeholder = "Em °C";

      nome.name = document.querySelector("#addr0").className + i;
     
      //anexando ao table
      document.querySelector('#tabela').appendChild(tr);

      document.querySelector(".tr"+i).appendChild(td);
      document.querySelector(".tr"+i).appendChild(tda);
      document.querySelector(".tr"+i).appendChild(tdb);
      document.querySelector(".tr"+i).appendChild(tdc);
      document.querySelector(".tr"+i).appendChild(tdd);
      //document.querySelector("#addr0").className + CHR(65+i);
      document.querySelector(".td_nome"+i).appendChild(nome);
      document.querySelector(".td_nome"+i).innerHTML = i+1;//CHR(65+i);;
      document.querySelector(".td_temp"+i).appendChild(temp);//.innerHTML = document.querySelector("#addr0").className + String.fromCharCode(65+i)//CHR(65+i);
      document.querySelector(".td_massa"+i).appendChild(massa);
      document.querySelector(".td_rho"+i).appendChild(rho);
      document.querySelector(".td_rho_temp"+i).appendChild(rho_temp);
      

      //$('#addr'+i).html($('#addr'+b).html()).find('td:first-child').html();
      //$('#tab_logic').append('<tr id="addr'+(i+1)+'"><input class="cu"></input><td>');
     
      i++; 
  });
     
     $("#delete_row").click(function(event){
      event.preventDefault();
       if(i>1){
     $(".tr"+(i-1)).html('');
     i--;
     }
   });

});