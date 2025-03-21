function  generar_pdf(datos){
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();
  
  const encabezados = [["Nombre", "Edad", "Profesión"]];
  const cuerpo = [["alfredo_new","22","ingeniero"],["jorge","33","licenciado"]];

  
  /*doc.text(datos['nombre'],20,40);*/

  // Generar tabla
  doc.autoTable({
      head: encabezados,
      body: cuerpo,
      startY: 20,
  });

  doc.text("Nombre del personal que realizó el mantenimiento:",10,10);

  // Descargar el PDF
  doc.save("test.pdf");
  
}