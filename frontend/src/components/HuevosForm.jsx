// src/components/HuevosForm.jsx

//descargar el file of github//

import React from 'react';
import GenericForm from './GenericForm';

const calcularTotalHuevos = (huevos) => {
  const totalHuevos = huevos.total_huevo1 + huevos.total_huevo2 + huevos.total_huevo3;
  huevos.total_huevos = totalHuevos;
  return totalHuevos;
};

// Ejemplo de uso:
const huevosRecogidos = {
  total_huevo1: 120,
  total_huevo2: 135,
  total_huevo3: 110,
};

const totalHuevos = calcularTotalHuevos(huevosRecogidos);
console.log(`El total de huevos recogidos hoy es: ${totalHuevos}`);


const huevosConfig = [
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
  { name: 'fecha_puesta', label: 'Fecha de Puesta', type: 'date', required: true },
  { name: 'hora1', label: 'recogida #1', type: 'number', required: true },
  { name: 'total_huevo1', label: 'numero huevos', type: 'number', required: true },
  { name: 'hora 2', label: 'recogida #2', type: 'number', required: true },
  { name: 'total_huevo2', label: 'numero huevos', type: 'number', required: true },
  { name: 'hora 3', label: 'recogida #3', type: 'number', required: true },
  { name: 'total_huevo3', label: 'numero huevos', type: 'number', required: true },
  { name: 'peso_huevo', label: 'Peso del Huevo promedio', type: 'number', required: true },
  { name: 'total_B', label: 'Tipo B', type: 'number', required: true },
  { name: 'total_A', label: 'Tipo A', type: 'number', required: true },
  { name: 'total_AA', label: 'Tipo AA', type: 'number', required: true },
  { name: 'total_AAA', label: 'Tipo AAA', type: 'number', required: true },
  { name: 'total_Jumbo', label: 'Tipo Jumbo', type: 'number', required: true },
  { name: 'total_huevos', label: 'total huevos', type: 'number', required: true },
];

const HuevosForm = () => (
  <div>
    <h1>Formulario huevos</h1>
    <GenericForm config={huevosConfig} endpoint="http://localhost:5000/api/huevos" />

  </div>
);

export default HuevosForm;
