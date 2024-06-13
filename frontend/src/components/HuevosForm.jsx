// src/components/HuevosForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const huevosConfig = [
  { name: 'ave_id', label: 'ID del Ave', type: 'number', required: true },
  { name: 'fecha_puesta', label: 'Fecha de Puesta', type: 'date', required: true },
  { name: 'peso_huevo', label: 'Peso del Huevo', type: 'number', required: true },
  { name: 'calidad_huevo', label: 'Calidad del Huevo', type: 'number', required: true },
];

const HuevosForm = () => (
  <div>
    <h1>Formulario huevos</h1>
    <GenericForm config={huevosConfig} endpoint="http://localhost:5000/api/huevos" />

  </div>
);

export default HuevosForm;
