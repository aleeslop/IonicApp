import React, { useState } from 'react';

export default function Login({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mfaCode, setMfaCode] = useState(['', '', '', '', '', '']);
  const [error, setError] = useState('');

  const handleMfaChange = (index, value) => {
    if (value.length > 1) return; // limit to 1 char
    const newCode = [...mfaCode];
    newCode[index] = value;
    setMfaCode(newCode);
    
    // Auto-focus next input
    if (value && index < 5) {
      const nextInput = document.getElementById(`mfa-${index + 1}`);
      if (nextInput) nextInput.focus();
    }
  };

  const handleMfaKeyDown = (index, e) => {
    // Handle backspace to focus previous input
    if (e.key === 'Backspace' && !mfaCode[index] && index > 0) {
      const prevInput = document.getElementById(`mfa-${index - 1}`);
      if (prevInput) prevInput.focus();
    }
  };

  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const validateEmail = (val) => {
    if (!val) {
      setEmailError('El correo es obligatorio.');
      return false;
    }
    if (!val.includes('@')) {
      setEmailError(`Incluye un signo "@" en la dirección de correo electrónico.`);
      return false;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(val)) {
      setEmailError('El formato del correo no es válido. Revisa que esté completo.');
      return false;
    }
    setEmailError('');
    return true;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const isEmailValid = validateEmail(email);
    const isPasswordValid = password.length > 0;
    const currentMfa = mfaCode.join('');
    const isMfaValid = currentMfa.length === 6;
    
    if (!isPasswordValid) {
      setPasswordError('Ingresa tu contraseña.');
    } else {
      setPasswordError('');
    }

    if (!isMfaValid) {
      setError('Ingresa el código MFA completo de 6 dígitos.');
      return;
    }

    if (!isEmailValid || !isPasswordValid) return;

    if (email === 'admin@sasisopa.com' && password === '12345678' && currentMfa === '123456') {
      onLogin('superadmin');
    } else {
      setError('Credenciales incorrectas. Verifica tu correo, contraseña o código MFA.');
    }
  };

  return (
    <div className="h-screen flex bg-surface-container-lowest font-body-md selection:bg-secondary selection:text-on-secondary overflow-hidden">
      
      {/* LEFT PANEL - DARK */}
      <div className="hidden lg:flex lg:w-5/12 bg-primary text-on-primary flex-col justify-between p-8 xl:p-12 relative overflow-hidden">
        {/* Abstract background lines (simulated) */}
        <div className="absolute inset-0 opacity-10 pointer-events-none">
          <svg className="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
            <path d="M0,50 Q25,25 50,50 T100,50" fill="none" stroke="currentColor" strokeWidth="0.5" strokeDasharray="2,2"/>
            <path d="M0,80 Q50,10 100,80" fill="none" stroke="currentColor" strokeWidth="0.5" strokeDasharray="2,2"/>
          </svg>
        </div>

        {/* Logo */}
        <div className="relative z-10">
          <svg width="150" height="40" viewBox="0 0 110 32" fill="none" xmlns="http://www.w3.org/2000/svg" className="h-10 w-auto">
            <path d="M 22 6 L 10 6 A 6 6 0 0 0 10 18 L 14 18" stroke="#F2B705" strokeWidth="6" strokeLinecap="round" fill="none" />
            <path d="M 8 14 L 18 14 A 6 6 0 0 1 18 26 L 10 26" stroke="#4FB3D9" strokeWidth="6" strokeLinecap="round" fill="none" />
            <text x="32" y="24" fontFamily="'Outfit', sans-serif" fontWeight="800" fontSize="26" fill="#FFFFFF" letterSpacing="-0.5">suelvo</text>
          </svg>
        </div>

        {/* Center Content */}
        <div className="relative z-10 space-y-4 my-auto">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-surface-container-highest/20 border border-surface-container-highest/30">
            <span className="material-symbols-outlined text-[14px]">shield</span>
            <span className="font-mono-label text-[10px] uppercase tracking-wider font-semibold">Arquitectura de Cumplimiento Nacional</span>
          </div>

          <h1 className="font-headline-xl text-[32px] xl:text-[38px] leading-[1.15] font-bold text-white tracking-tight">
            Gobernanza y Cumplimiento Regulatorio para el Sector Hidrocarburos
          </h1>

          <p className="text-[14px] xl:text-[15px] text-surface-dim leading-relaxed max-w-md">
            Plataforma centralizada de fiscalización ASEA, CNE y SAT para estaciones de servicio, plantas de distribución y autoconsumos industriales.
          </p>
        </div>

        {/* Bottom Cards */}
        <div className="relative z-10 flex gap-3">
          <div className="bg-surface-container-highest/10 border border-surface-container-highest/20 rounded-xl p-3 xl:p-4 flex-1">
            <span className="font-mono-label text-[9px] xl:text-[10px] text-surface-dim uppercase tracking-wider block mb-1">Auditorías SAT</span>
            <span className="font-mono-metric text-[14px] xl:text-[16px] text-white font-semibold">Anexo 21</span>
          </div>
          <div className="bg-surface-container-highest/10 border border-surface-container-highest/20 rounded-xl p-3 xl:p-4 flex-1">
            <span className="font-mono-label text-[9px] xl:text-[10px] text-surface-dim uppercase tracking-wider block mb-1">Protocolo ASEA</span>
            <span className="font-mono-metric text-[14px] xl:text-[16px] text-white font-semibold">SASISOPA</span>
          </div>
          <div className="bg-surface-container-highest/10 border border-surface-container-highest/20 rounded-xl p-3 xl:p-4 flex-1">
            <span className="font-mono-label text-[9px] xl:text-[10px] text-surface-dim uppercase tracking-wider block mb-1">Supervisión CNE</span>
            <span className="font-mono-metric text-[14px] xl:text-[16px] text-white font-semibold">Tiempo Real</span>
          </div>
        </div>
      </div>

      {/* RIGHT PANEL - LIGHT */}
      <div className="w-full lg:w-7/12 flex flex-col justify-center px-6 sm:px-12 md:px-20 py-6 bg-surface-container-lowest h-full overflow-y-auto">
        
        <div className="max-w-[460px] w-full mx-auto">
          {/* Top Pill */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-surface-container mb-6">
            <span className="w-2 h-2 rounded-full bg-secondary"></span>
            <span className="font-mono-label text-[10px] text-secondary uppercase font-semibold tracking-wider">
              Entorno de Producción Nivel Global
            </span>
          </div>

          <div className="space-y-1 mb-6">
            <h2 className="font-headline-xl text-[28px] font-bold text-on-surface">
              Iniciar Sesión
            </h2>
            <p className="text-on-surface-variant text-[13px]">
              Ingresa tus credenciales maestras y la llave de seguridad de doble factor.
            </p>
          </div>

          {error && (
            <div className="mb-4 p-3 rounded-xl bg-error-container text-error font-body-sm text-[13px] flex items-center gap-2">
              <span className="material-symbols-outlined text-[18px]">error</span>
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} noValidate className="space-y-4">
            
            {/* Email Input */}
            <div className="space-y-1.5">
              <label className={`font-mono-label text-[10px] uppercase tracking-wider font-semibold ${emailError ? 'text-error' : 'text-on-surface-variant'}`}>
                Correo Electrónico Corporativo
              </label>
              <div className="relative">
                <span className={`material-symbols-outlined absolute left-3.5 top-1/2 -translate-y-1/2 text-[18px] ${emailError ? 'text-error' : 'text-outline'}`}>
                  mail
                </span>
                <input 
                  type="email" 
                  value={email}
                  onChange={e => {
                    setEmail(e.target.value);
                    if (emailError) validateEmail(e.target.value);
                  }}
                  onBlur={(e) => validateEmail(e.target.value)}
                  className={`w-full h-11 pl-10 pr-4 rounded-xl bg-surface-container-lowest border text-[14px] focus:outline-none focus:ring-1 transition-colors ${emailError ? 'border-error text-error placeholder:text-error/50 focus:border-error focus:ring-error' : 'border-outline-variant text-on-surface placeholder:text-outline focus:border-secondary focus:ring-secondary'}`}
                  placeholder="correoelectronico@suelvo.mx"
                />
              </div>
              {emailError && (
                <p className="text-error text-[12px] mt-1 flex items-start gap-1">
                  <span className="material-symbols-outlined text-[14px] mt-0.5">info</span>
                  {emailError}
                </p>
              )}
            </div>

            {/* Password Input */}
            <div className="space-y-1.5">
              <div className="flex justify-between items-center">
                <label className={`font-mono-label text-[10px] uppercase tracking-wider font-semibold ${passwordError ? 'text-error' : 'text-on-surface-variant'}`}>
                  Contraseña Maestra
                </label>
                <a href="#" className="font-mono-label text-[10px] text-secondary font-semibold hover:underline">
                  ¿Olvidaste tu contraseña?
                </a>
              </div>
              <div className="relative">
                <span className={`material-symbols-outlined absolute left-3.5 top-1/2 -translate-y-1/2 text-[18px] ${passwordError ? 'text-error' : 'text-outline'}`}>
                  lock
                </span>
                <input 
                  type="password"
                  value={password}
                  onChange={e => {
                    setPassword(e.target.value);
                    if (passwordError && e.target.value.length > 0) setPasswordError('');
                  }}
                  className={`w-full h-11 pl-10 pr-10 rounded-xl bg-surface-container-lowest border text-[14px] font-mono-val tracking-[0.2em] focus:outline-none focus:ring-1 transition-colors ${passwordError ? 'border-error text-error placeholder:text-error/50 focus:border-error focus:ring-error' : 'border-outline-variant text-on-surface placeholder:text-outline focus:border-secondary focus:ring-secondary'}`}
                  placeholder="•••••••••••••"
                />
                <button type="button" className={`absolute right-3.5 top-1/2 -translate-y-1/2 transition-colors flex items-center justify-center ${passwordError ? 'text-error hover:text-error/80' : 'text-outline hover:text-on-surface'}`}>
                  <span className="material-symbols-outlined text-[18px]">
                    visibility
                  </span>
                </button>
              </div>
              {passwordError && (
                <p className="text-error text-[12px] mt-1 flex items-start gap-1">
                  <span className="material-symbols-outlined text-[14px] mt-0.5">info</span>
                  {passwordError}
                </p>
              )}
            </div>

            {/* MFA Section */}
            <div className="bg-[#f0f8fb] border border-[#d2eaf4] rounded-2xl p-4 xl:p-5 space-y-3">
              <div className="flex justify-between items-start gap-3">
                <div className="flex gap-2.5">
                  <span className="material-symbols-outlined text-secondary text-[20px] mt-0.5">
                    gpp_good
                  </span>
                  <div>
                    <h4 className="font-body-md text-[13px] font-bold text-on-surface">
                      Autenticación de Dos Factores (MFA Obligatorio)
                    </h4>
                    <p className="text-[12px] text-on-surface-variant mt-0.5 leading-relaxed">
                      Abre tu aplicación Google Authenticator o llave física y escribe el código temporal de 6 dígitos.
                    </p>
                  </div>
                </div>
                <span className="px-2 py-0.5 rounded bg-[#ffdad6] text-[#ba1a1a] font-mono-label text-[9px] font-bold uppercase tracking-wider shrink-0 mt-0.5">
                  Requerido
                </span>
              </div>

              <div className="flex items-center justify-center gap-2 py-1">
                {mfaCode.map((digit, index) => (
                  <React.Fragment key={index}>
                    <input
                      id={`mfa-${index}`}
                      type="text"
                      inputMode="numeric"
                      maxLength={1}
                      value={digit}
                      onChange={(e) => handleMfaChange(index, e.target.value.replace(/\D/g, ''))}
                      onKeyDown={(e) => handleMfaKeyDown(index, e)}
                      className="w-10 h-12 rounded-xl bg-surface-container-lowest border border-outline-variant text-center font-mono-metric text-[20px] font-bold text-on-surface focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-colors shadow-sm"
                    />
                    {index === 2 && <span className="text-outline-variant font-bold mx-0.5">-</span>}
                  </React.Fragment>
                ))}
              </div>

              <div className="flex justify-between items-center pt-1">
                <div className="flex items-center gap-1.5 text-secondary">
                  <span className="material-symbols-outlined text-[14px]">timer</span>
                  <span className="font-mono-label text-[10px] font-semibold">El código se renueva en 23s</span>
                </div>
                <button type="button" className="font-mono-label text-[10px] text-outline hover:text-on-surface transition-colors font-medium">
                  Usar llave de seguridad FIDO2
                </button>
              </div>
            </div>

            {/* Submit Button */}
            <button 
              type="submit"
              className="w-full h-11 rounded-full bg-[#154F66] hover:bg-[#0c2b3a] text-white font-headline-sm text-[14px] font-semibold transition-all shadow-md flex items-center justify-center gap-2 mt-2"
            >
              <span>Ingresar al Panel Global</span>
              <span className="material-symbols-outlined text-[16px]">key</span>
            </button>
          </form>

          {/* Footer Links */}
          <div className="flex justify-between items-center mt-6 pt-4 border-t border-outline-variant/30">
            <a href="#" className="font-body-sm text-[11px] text-on-surface-variant hover:text-secondary underline decoration-on-surface-variant/30 underline-offset-4 transition-colors">
              Soporte de Seguridad Crítica
            </a>
            <span className="text-outline-variant text-[10px]">•</span>
            <a href="#" className="font-body-sm text-[11px] text-on-surface-variant hover:text-secondary underline decoration-on-surface-variant/30 underline-offset-4 transition-colors">
              Políticas de Auditoría Criptográfica
            </a>
          </div>

        </div>
      </div>

    </div>
  );
}
