// src/components/ClimaForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const climaConfig = [
  { name: 'fecha', label: 'Fecha', type: 'date', required: true },
  { name: 'temperatura', label: 'Temperatura', type: 'number' },
  { name: 'precipitacion', label: 'Precipitación', type: 'number' },
  { name: 'evento_climatico', label: 'Evento Climático' },
];

const ClimaForm = () => (
  <div>
  <h1>Formulario Clima</h1>
      <GenericForm config={climaConfig} endpoint="http://localhost:5000/api/clima" />
  </div>
);

export default ClimaForm;
