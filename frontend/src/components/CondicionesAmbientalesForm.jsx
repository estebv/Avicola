// src/components/CondicionesAmbientalesForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const condicionesConfig = [
  { name: 'fecha', label: 'Fecha', type: 'date', required: true },
  { name: 'temperatura', label: 'Temperatura', type: 'number', required: true },
  { name: 'humedad', label: 'Humedad', type: 'number', required: true },
  { name: 'ventilacion', label: 'Ventilación', type: 'number' },
  { name: 'iluminacion', label: 'Iluminación', type: 'number' },
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },

];

const CondicionesAmbientalesForm = () => (
  <div>
    <h1>Formulario Condiciones Ambientales</h1>
    <GenericForm config={condicionesConfig} endpoint="http://localhost:5000/api/condiciones" />
  </div>
);

export default CondicionesAmbientalesForm;
