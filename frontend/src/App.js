import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AveForm from './components/AveForm';
import CondicionesAmbientalesForm from './components/CondicionesAmbientalesForm';
import PesajeForm from './components/PesajeForm';
import VacunacionForm from './components/VacunacionForm';
import HuevosForm from './components/HuevosForm';
import AlimentosForm from './components/AlimentosForm';
import GalponForm from './components/GalponForm';
import ClimaForm from './components/ClimaForm';
import './styles/NavStyles.scss'; // Importa los estilos del menú de navegación

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/ave">Ave </Link>
            </li>
            <li>
              <Link to="/condiciones">Condiciones Ambientales </Link>
            </li>
            <li>
              <Link to="/pesaje">Pesaje </Link>
            </li>
            <li>
              <Link to="/vacunacion">Vacunación </Link>
            </li>
            <li>
              <Link to="/huevos">Huevos </Link>
            </li>
            <li>
              <Link to="/alimentos">Concentrado </Link>
            </li>
            <li>
              <Link to="/galpon">Galpones </Link>
            </li>
            <li>
              <Link to="/clima">Clima </Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/ave" element={<AveForm />} />
          <Route path="/condiciones" element={<CondicionesAmbientalesForm />} />
          <Route path="/pesaje" element={<PesajeForm />} />
          <Route path="/vacunacion" element={<VacunacionForm />} />
          <Route path="/huevos" element={<HuevosForm />} />
          <Route path="/alimentos" element={<AlimentosForm />} />
          <Route path="/galpon" element={<GalponForm />} />
          <Route path="/clima" element={<ClimaForm />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
