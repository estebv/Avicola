// src/components/ClimaForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const climaConfig = [
  { name: 'fecha', label: 'Fecha', type: 'date', required: true },
  { name: 'temperatura', label: 'Temperatura (°C)', type: 'number', step: '0.1' },
  { name: 'precipitacion', label: 'Precipitación (mm)', type: 'number', step: '0.1' },
];

const ClimaForm = () => (
  <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
    <div className="max-w-2xl mx-auto">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">
          Formulario Clima
        </h1>
        <p className="text-gray-600">
          Registra los datos climáticos del día
        </p>
      </div>
      
      <div className="card">
        <GenericForm config={climaConfig} endpoint="http://localhost:5000/api/clima" />
      </div>
    </div>
  </div>
);

export default ClimaForm;
