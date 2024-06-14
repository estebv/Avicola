// src/components/ClimaForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const mortalidadConfig = [
    { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
    { name: 'numero_aves', label: 'numero aves', type: 'number', required: true },
    { name: 'fecha_muerte', label: 'fecha muerte', type: 'date', required: true },
    { name: 'causa_muerte', label: 'causa muerte', required: true },

]

const  MortalidadForm = () => (
  <div>
  <h1>Formulario Mortalidad</h1>
      <GenericForm config={mortalidadConfig} endpoint="http://localhost:5000/api/mortalidad" />
  </div>
);

export default MortalidadForm;
