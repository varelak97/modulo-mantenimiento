function  generar_pdf(datos){
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();
  
  const encabezados = [["Nombre", "Edad", "Profesión"]];
  const cuerpo = [["alfredo","22","ingeniero"],["jorge","33","licenciado"]];

  // Generar tabla
  doc.autoTable({
      head: encabezados,
      body: cuerpo,
      startY: 20,
  });

  // Descargar el PDF
  doc.save("test.pdf");
  
}