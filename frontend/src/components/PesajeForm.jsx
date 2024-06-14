// src/components/PesajeForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const pesajeConfig = [
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
  { name: 'estado_salud', label: 'Estado de Salud' },
  { name: 'numero_ave', label: 'numero ave', type: 'number', required: true },
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
