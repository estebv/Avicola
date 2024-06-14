// src/components/AveForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const aveConfig = [
  { name: 'raza', label: 'Raza', required: true },
  { name: 'fecha_nacimiento', label: 'Fecha de Nacimiento', type: 'date', required: true },
  { name: 'fecha_llegada', label: 'Fecha de Llegada', type: 'date', required: true },
  { name: 'origen', label: 'Origen', required: true },
  { name: 'total_aves', label: 'aves totales', type: 'number', required: true },
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
];

const AveForm = () => (
  <div>
  <h1>Formulario Aves</h1>
      <GenericForm config={aveConfig} endpoint="http://localhost:5000/api/aves" />
  </div>
);

export default AveForm;
