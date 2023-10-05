function prueba(lista){
  return lista.filter(function(item){
    return item[1] < 40;
  });
}