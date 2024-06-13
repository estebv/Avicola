// src/components/AveForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const aveConfig = [
  { name: 'raza', label: 'Raza', required: true },
  { name: 'fecha_nacimiento', label: 'Fecha de Nacimiento', type: 'date', required: true },
  { name: 'fecha_llegada', label: 'Fecha de Llegada', type: 'date', required: true },
  { name: 'origen', label: 'Origen', required: true },
  { name: 'estado_salud', label: 'Estado de Salud', required: true },
  { name: 'fecha_muerte', label: 'Fecha de Muerte', type: 'date' },
  { name: 'causa_muerte', label: 'Causa de Muerte' },
];

const AveForm = () => (
  <div>
  <h1>Formulario Aves</h1>
      <GenericForm config={aveConfig} endpoint="http://localhost:5000/api/aves" />
  </div>
);

export default AveForm;
