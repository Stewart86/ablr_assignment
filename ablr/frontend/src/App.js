import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home"
import Callback from "./pages/Callback"


function App() {
  return (
    <div className='flex flex-col h-screen min-w-full w-full justify-center'>
      <div className='flex h-full min-w-full justify-center bg-gray-100'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/callback" element={<Callback />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
