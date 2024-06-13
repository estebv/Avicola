// src/components/CondicionesAmbientalesForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const condicionesConfig = [
  { name: 'fecha', label: 'Fecha', type: 'date', required: true },
  { name: 'temperatura', label: 'Temperatura', type: 'number' },
  { name: 'humedad', label: 'Humedad', type: 'number' },
  { name: 'ventilacion', label: 'Ventilación' },
  { name: 'iluminacion', label: 'Iluminación' },
];

const CondicionesAmbientalesForm = () => (
  <div>
    <h1>Formulario Condiciones Ambientales</h1>
    <GenericForm config={condicionesConfig} endpoint="http://localhost:5000/api/condicionesambientales" />
  </div>
);

export default CondicionesAmbientalesForm;
