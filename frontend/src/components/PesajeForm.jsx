// src/components/PesajeForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const pesajeConfig = [
  { name: 'ave_id', label: 'ID del Ave', type: 'number', required: true },
  { name: 'estado_salud', label: 'Estado de Salud', required: true },
  { name: 'peso', label: 'Peso', type: 'number', required: true },
  { name: 'fecha_Pesaje', label: 'Fecha de Pesaje', type: 'date', required: true },
];

const PesajeForm = () => (
  <div>
    <h1>Formulario pesaje</h1>
    <GenericForm config={pesajeConfig} endpoint="http://localhost:5000/api/pesaje" />

  </div>
);

export default PesajeForm;
