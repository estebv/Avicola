import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AveForm from './components/AveForm';
import CondicionesAmbientalesForm from './components/CondicionesAmbientalesForm';
import PesajeForm from './components/PesajeForm';
import VacunacionForm from './components/VacunacionForm';
import HuevosForm from './components/HuevosForm';
import AlimentosForm from './components/AlimentosForm';
import GalponForm from './components/GalponForm';
import ClimaForm from './components/ClimaForm';
import MortalidadForm from './components/Mortalidad';

const App = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-white shadow-lg border-b border-gray-200">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <h1 className="text-xl font-bold text-primary-600">Avícola</h1>
              </div>
              <div className="flex items-center space-x-1">
                <Link 
                  to="/ave" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Aves
                </Link>
                <Link 
                  to="/condiciones" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Condiciones
                </Link>
                <Link 
                  to="/pesaje" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Pesaje
                </Link>
                <Link 
                  to="/vacunacion" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Vacunación
                </Link>
                <Link 
                  to="/huevos" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Huevos
                </Link>
                <Link 
                  to="/alimentos" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Concentrado
                </Link>
                <Link 
                  to="/galpon" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Galpones
                </Link>
                <Link 
                  to="/clima" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Clima
                </Link>
                <Link 
                  to="/mortalidad" 
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-primary-50 transition-colors duration-200"
                >
                  Mortalidad
                </Link>
              </div>
            </div>
          </div>
        </nav>

        <main>
          <Routes>
            <Route path="/ave" element={<AveForm />} />
            <Route path="/condiciones" element={<CondicionesAmbientalesForm />} />
            <Route path="/pesaje" element={<PesajeForm />} />
            <Route path="/vacunacion" element={<VacunacionForm />} />
            <Route path="/huevos" element={<HuevosForm />} />
            <Route path="/alimentos" element={<AlimentosForm />} />
            <Route path="/galpon" element={<GalponForm />} />
            <Route path="/clima" element={<ClimaForm />} />
            <Route path="/mortalidad" element={<MortalidadForm />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
