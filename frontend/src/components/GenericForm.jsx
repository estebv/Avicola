import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const GenericForm = ({ config, endpoint }) => {
    const { register, handleSubmit, formState: { errors }, reset } = useForm();
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitMessage, setSubmitMessage] = useState('');

    const onSubmit = data => {
        setIsSubmitting(true);
        setSubmitMessage('');
        
        axios.post(endpoint, data)
            .then(response => {
                console.log('Respuesta del servidor:', response.data);
                setSubmitMessage('¡Datos enviados exitosamente!');
                reset();
            })
            .catch(error => {
                console.error('Error al enviar el formulario:', error);
                setSubmitMessage('Error al enviar los datos. Intente nuevamente.');
            })
            .finally(() => {
                setIsSubmitting(false);
            });
    };

    return (
        <div className="max-w-md mx-auto">
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                {config.map(field => (
                    <div key={field.name} className="space-y-2">
                        <label 
                            htmlFor={field.name}
                            className="block text-sm font-medium text-gray-700"
                        >
                            {field.label}
                            {field.required && <span className="text-red-500 ml-1">*</span>}
                        </label>
                        <input
                            id={field.name}
                            type={field.type || 'text'}
                            {...register(field.name, { required: field.required })}
                            className="input-field"
                            disabled={isSubmitting}
                        />
                        {errors[field.name] && (
                            <span className="text-red-500 text-sm">
                                Este campo es obligatorio
                            </span>
                        )}
                    </div>
                ))}
                
                {submitMessage && (
                    <div className={`p-3 rounded-lg text-sm ${
                        submitMessage.includes('exitosamente') 
                            ? 'bg-green-100 text-green-700 border border-green-200' 
                            : 'bg-red-100 text-red-700 border border-red-200'
                    }`}>
                        {submitMessage}
                    </div>
                )}
                
                <button 
                    type="submit" 
                    disabled={isSubmitting}
                    className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isSubmitting ? 'Enviando...' : 'Enviar'}
                </button>
            </form>
        </div>
    );
};

export default GenericForm;
