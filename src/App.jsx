import React, { useState } from 'react';
import Login from './Login';
import Dashboard from './Dashboard';

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  if (!isAuthenticated) {
    return <Login onLogin={(role) => setIsAuthenticated(true)} />;
  }

  return <Dashboard />;
}
