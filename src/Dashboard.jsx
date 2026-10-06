import React, { useState } from 'react';

const initialTenants = [
  {
    id: "ten-1",
    name: "Grupo Hidrocarburos del Centro S.A. de C.V.",
    sub: "Estaciones de Servicio Bajío",
    rfc: "GHC160512AB3",
    initials: "GH",
    type: "Gasolinera",
    modules: ["SASISOPA", "NOM-005", "NOM-016", "CV-SAT"],
    status: "Activa"
  },
  {
    id: "ten-2",
    name: "Combustibles y Derivados del Norte S.A.P.I.",
    sub: "Logística Minera del Noreste",
    rfc: "CDN180920XYZ",
    initials: "CD",
    type: "Autoconsumo Industrial",
    modules: ["NOM-005", "CV-SAT"],
    status: "Activa"
  },
  {
    id: "ten-3",
    name: "Distribuidora Gas Imperial del Valle S.A.",
    sub: "Imperial Gas Tehuacán",
    rfc: "DGI140228KL9",
    initials: "DG",
    type: "Planta LP",
    modules: ["SASISOPA", "NOM-018", "CV-SAT"],
    status: "Activa"
  },
  {
    id: "ten-4",
    name: "Estaciones Río Bravo S.A. de C.V.",
    sub: "Río Bravo Servicarrusel",
    rfc: "ERB191104MN7",
    initials: "ER",
    type: "Gasolinera",
    modules: ["SASISOPA", "NOM-005", "NOM-016", "NOM-018", "CV-SAT"],
    status: "Activa"
  },
  {
    id: "ten-5",
    name: "Servicios Logísticos Petrolíferos de Occidente",
    sub: "LogiPetro Terminal Guadalajara",
    rfc: "SLP200315QQ2",
    initials: "SL",
    type: "Autoconsumo",
    modules: ["NOM-005", "CV-SAT"],
    status: "En Gracia"
  }
];

export default function Dashboard() {
  const [tenants, setTenants] = useState(initialTenants);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterType, setFilterType] = useState('todos');
  const [filterStatus, setFilterStatus] = useState('todos');
  const [currentTab, setCurrentTab] = useState('dashboard');

  const filteredTenants = tenants.filter(t => {
    const matchesSearch = t.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                          t.rfc.toLowerCase().includes(searchTerm.toLowerCase()) || 
                          t.sub.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesType = filterType === "todos" || t.type.toLowerCase().includes(filterType.toLowerCase());
    const matchesStatus = filterStatus === "todos" || t.status.toLowerCase() === filterStatus.toLowerCase();
    return matchesSearch && matchesType && matchesStatus;
  });

  const sidebarTabs = [
    { id: 'dashboard', icon: 'grid_view', label: 'Dashboard' },
    { id: 'instalaciones', icon: 'local_gas_station', label: 'Instalaciones' },
    { id: 'cvsat', icon: 'receipt_long', label: 'CV-SAT' },
    { id: 'boveda', icon: 'folder_supervised', label: 'Bóveda documental' },
    { id: 'calendario', icon: 'calendar_month', label: 'Calendario' },
    { id: 'alertas', icon: 'notifications_active', label: 'Alertas' },
    { id: 'sasisopa', icon: 'verified_user', label: 'SASISOPA' },
    { id: 'nom005', icon: 'security', label: 'NOM-005' },
    { id: 'nom016', icon: 'science', label: 'NOM-016' },
    { id: 'nom018', icon: 'warning', label: 'NOM-018' },
    { id: 'usuarios', icon: 'manage_accounts', label: 'Usuarios' },
    { id: 'configuracion', icon: 'settings', label: 'Configuración' },
    { id: 'facturacion', icon: 'credit_card', label: 'Facturación y Suscripción' },
    { id: 'bitacora', icon: 'history_edu', label: 'Bitácora de Auditoría' },
  ];

  return (
    <div className="bg-surface font-body-md text-on-surface antialiased selection:bg-secondary selection:text-on-secondary min-h-screen">
      
      {/* Sidebar */}
      <aside className="fixed left-0 top-0 h-screen w-72 bg-primary-container text-on-primary z-50 flex flex-col justify-between overflow-y-auto">
        <div className="flex flex-col">
          <div className="h-16 px-space-md flex items-center justify-between bg-primary-container border-b border-white/5">
            <div className="flex items-center gap-space-sm cursor-pointer">
              <svg width="110" height="32" viewBox="0 0 110 32" fill="none" xmlns="http://www.w3.org/2000/svg" className="h-8 w-auto">
                <path d="M 22 6 L 10 6 A 6 6 0 0 0 10 18 L 14 18" stroke="#F2B705" strokeWidth="6" strokeLinecap="round" fill="none" />
                <path d="M 8 14 L 18 14 A 6 6 0 0 1 18 26 L 10 26" stroke="#4FB3D9" strokeWidth="6" strokeLinecap="round" fill="none" />
                <text x="32" y="24" fontFamily="'Outfit', sans-serif" fontWeight="800" fontSize="26" fill="#FFFFFF" letterSpacing="-0.5">suelvo</text>
              </svg>
            </div>
            <span className="px-space-xs py-0.5 rounded bg-secondary text-on-secondary font-mono-label text-mono-label font-bold uppercase tracking-wider">Admin</span>
          </div>
          <div className="px-space-md py-space-sm">
            <div className="px-space-sm py-1.5 rounded-lg bg-tertiary-container flex items-center justify-between">
              <span className="font-mono-label text-mono-label text-on-tertiary-container uppercase tracking-wide font-semibold">Nivel de Acceso</span>
              <span className="font-mono-label text-mono-label text-secondary-container font-bold">Total Global</span>
            </div>
          </div>
          <nav className="flex flex-col gap-0.5 px-space-sm py-space-xs">
            {sidebarTabs.map(tab => (
              <button
                key={tab.id}
                onClick={() => setCurrentTab(tab.id)}
                className={`sidebar-item flex items-center gap-space-sm px-space-sm py-2 rounded-lg transition-colors font-body-md text-[15px] text-left ${
                  currentTab === tab.id 
                    ? 'bg-secondary text-on-secondary font-semibold' 
                    : 'text-on-primary-container hover:bg-tertiary-container hover:text-on-primary'
                }`}
                type="button"
              >
                <span className="material-symbols-outlined text-[20px]">{tab.icon}</span>
                <span>{tab.label}</span>
              </button>
            ))}
          </nav>
        </div>
        <div className="p-space-md">
          <div className="rounded-xl bg-tertiary-container p-space-sm flex items-center justify-between">
            <div className="flex flex-col">
              <span className="font-mono-label text-[10px] uppercase tracking-wider text-on-tertiary-container">Infraestructura</span>
              <span className="font-mono-data text-mono-data text-white font-bold">ASEA CRE SAT</span>
            </div>
            <span className="h-2.5 w-2.5 rounded-full bg-secondary-container animate-pulse"></span>
          </div>
        </div>
      </aside>

      {/* Workspace Container */}
      <div className="pl-72 flex flex-col min-h-screen">
        
        {/* Top Header */}
        <header className="fixed top-0 left-72 right-0 h-16 bg-surface-container-lowest z-40 border-b border-surface-container-low shadow-sm">
          <div className="h-16 w-full px-6 lg:px-8 flex items-center justify-between gap-4">
            <div className="flex items-center gap-4 flex-1 min-w-0">
              {/* Tenant Switcher */}
              <button className="flex items-center gap-2 px-4 py-1.5 rounded-xl bg-surface-container-low hover:bg-surface-container transition-colors text-left border border-transparent hover:border-secondary/30 truncate" type="button">
                <span className="material-symbols-outlined text-secondary text-[22px] shrink-0">domain</span>
                <div className="flex flex-col min-w-0 truncate hidden sm:flex">
                  <span className="font-mono-label text-[10px] text-secondary uppercase font-bold tracking-wider">Tenant Activo</span>
                  <div className="flex items-center gap-1.5 truncate">
                    <span className="font-body-md text-[14px] text-on-surface font-semibold truncate">Grupo Gasolinero del Norte S.A. de C.V.</span>
                    <span className="font-mono-data text-[11px] text-on-surface-variant font-bold px-1.5 py-0.5 rounded bg-surface-container-high shrink-0">RFC GGN120405KP2</span>
                  </div>
                </div>
                <span className="material-symbols-outlined text-on-surface-variant text-[20px] shrink-0">unfold_more</span>
              </button>
              
              <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#e2f3ff] text-on-surface hidden xl:flex border border-[#bce9ff] shrink-0">
                <span className="material-symbols-outlined text-secondary text-[16px]">admin_panel_settings</span>
                <span className="font-mono-label text-[10px] font-bold text-secondary uppercase whitespace-nowrap tracking-wider">Modo Super Admin Soporte Global</span>
              </div>
            </div>

            <div className="flex items-center gap-2 sm:gap-4 shrink-0">
              {/* Notificaciones */}
              <button className="h-10 w-10 rounded-full flex items-center justify-center text-on-surface-variant hover:bg-surface-container-low hover:text-on-surface transition-all relative group shrink-0" type="button">
                <span className="material-symbols-outlined text-[24px] group-hover:scale-110 transition-transform">notifications</span>
                <span className="absolute top-2 right-2.5 h-2 w-2 rounded-full bg-error border-[1.5px] border-surface-container-lowest"></span>
              </button>
              
              {/* Separador */}
              <div className="hidden sm:block h-8 w-px bg-[#c2c7cc]/50 mx-1 shrink-0"></div>
              
              {/* Perfil de Usuario */}
              <div className="flex items-center gap-3 cursor-pointer group hover:bg-surface-container-lowest px-2 py-1 rounded-xl transition-colors shrink-0">
                <div className="flex flex-col text-right hidden sm:flex">
                  <span className="font-headline-sm text-[14px] text-primary font-bold leading-tight group-hover:text-secondary transition-colors whitespace-nowrap">Super Admin</span>
                  <span className="font-body-sm text-[11px] text-on-surface-variant font-medium whitespace-nowrap">Soporte Nivel 4</span>
                </div>
                <div className="h-9 w-9 rounded-full bg-[#154F66] text-white flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow shrink-0">
                  <span className="material-symbols-outlined text-[20px]">person</span>
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main className="w-full pt-16 bg-surface flex-1 px-6 lg:px-8 py-8">
          
          {currentTab === 'dashboard' ? (
            <div className="flex flex-col w-full gap-space-lg">
            
            {/* Header Section */}
            <section className="flex flex-col gap-space-md">
              <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-space-md">
                <div className="flex flex-col">
                  <div className="flex items-center gap-space-xs text-secondary font-mono-label text-[10px] uppercase tracking-widest font-bold mb-1">
                    <span>Administración Central</span>
                    <span className="text-outline-variant">/</span>
                    <span>Gobernanza de Clientes</span>
                  </div>
                  <h1 className="font-headline-xl text-[34px] text-primary font-bold tracking-tight mb-2">
                    Gestión de Tenants y Módulos
                  </h1>
                  <p className="font-body-md text-[15px] text-on-surface-variant max-w-3xl leading-relaxed">
                    Supervisión regulatoria unificada, asignación modular de cumplimiento legal y control técnico de licencias comerciales vigentes para el sector hidrocarburos.
                  </p>
                </div>
                <div className="flex items-center gap-space-sm self-start lg:self-center">
                  <button className="h-11 px-6 rounded-full bg-[#154F66] hover:bg-[#0c2b3a] text-white font-headline-sm text-[14px] font-semibold transition-all shadow-md flex items-center gap-2" type="button">
                    <span className="material-symbols-outlined text-[20px]">add</span>
                    <span>Registrar Nueva Empresa</span>
                  </button>
                </div>
              </div>

              {/* Bento Grid Stats */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
                
                <div className="bg-surface-container-lowest p-6 rounded-[20px] shadow-sm flex items-center justify-between border border-[#c2c7cc]/40">
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-xl bg-surface-container-low flex items-center justify-center text-secondary">
                      <span className="material-symbols-outlined text-[26px]">corporate_fare</span>
                    </div>
                    <div className="flex flex-col">
                      <span className="font-mono-label text-[10px] uppercase tracking-wider text-on-surface-variant font-bold mb-1">Total de Tenants</span>
                      <div className="flex items-baseline gap-2">
                        <span className="font-headline-lg text-[32px] font-bold text-on-surface leading-none">48</span>
                        <span className="px-2 py-0.5 rounded-full bg-surface-container font-mono-label text-[10px] text-secondary font-bold">Activos</span>
                      </div>
                    </div>
                  </div>
                  <div className="h-10 w-24">
                    <svg className="w-full h-full text-secondary" fill="none" viewBox="0 0 100 40">
                      <path d="M0 32 L20 28 L40 30 L60 18 L80 22 L100 10" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5"></path>
                      <path d="M0 32 L20 28 L40 30 L60 18 L80 22 L100 10 V40 H0 Z" fill="currentColor" fillOpacity="0.08"></path>
                    </svg>
                  </div>
                </div>

                <div className="bg-surface-container-lowest p-6 rounded-[20px] shadow-sm flex items-center justify-between border border-[#c2c7cc]/40">
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-xl bg-surface-container-low flex items-center justify-center text-secondary">
                      <span className="material-symbols-outlined text-[26px]">ev_station</span>
                    </div>
                    <div className="flex flex-col">
                      <span className="font-mono-label text-[10px] uppercase tracking-wider text-on-surface-variant font-bold mb-1">Permisos CNE y CRE</span>
                      <div className="flex items-baseline gap-2">
                        <span className="font-headline-lg text-[32px] font-bold text-on-surface leading-none">142</span>
                        <span className="px-2 py-0.5 rounded-full bg-surface-container font-mono-label text-[10px] text-secondary font-bold">Estaciones</span>
                      </div>
                    </div>
                  </div>
                  <div className="h-10 w-24">
                    <svg className="w-full h-full text-secondary" fill="none" viewBox="0 0 100 40">
                      <path d="M0 25 L25 24 L50 15 L75 18 L100 6" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5"></path>
                      <path d="M0 25 L25 24 L50 15 L75 18 L100 6 V40 H0 Z" fill="currentColor" fillOpacity="0.08"></path>
                    </svg>
                  </div>
                </div>

                <div className="bg-surface-container-lowest p-6 rounded-[20px] shadow-sm flex items-center justify-between border border-[#c2c7cc]/40">
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-xl bg-surface-container-low flex items-center justify-center text-secondary">
                      <span className="material-symbols-outlined text-[26px]">fact_check</span>
                    </div>
                    <div className="flex flex-col">
                      <span className="font-mono-label text-[10px] uppercase tracking-wider text-on-surface-variant font-bold mb-1">Monitoreo SASISOPA</span>
                      <div className="flex items-baseline gap-2">
                        <span className="font-headline-lg text-[32px] font-bold text-on-surface leading-none">98.5%</span>
                        <span className="px-2 py-0.5 rounded-full bg-surface-container font-mono-label text-[10px] text-secondary font-bold">Operativo</span>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center justify-center relative w-12 h-12">
                    <svg className="w-12 h-12 transform -rotate-90" viewBox="0 0 36 36">
                      <path className="text-surface-container" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeWidth="3.5"></path>
                      <path className="text-[#154F66]" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeDasharray="98.5, 100" strokeLinecap="round" strokeWidth="3.5"></path>
                    </svg>
                    <span className="material-symbols-outlined absolute text-[16px] text-[#154F66]">verified</span>
                  </div>
                </div>

              </div>
            </section>

            {/* Filters */}
            <section className="bg-surface-container-lowest p-4 rounded-[20px] shadow-sm flex flex-col md:flex-row items-stretch md:items-center justify-between gap-4 border border-[#c2c7cc]/40">
              <div className="flex-1 flex flex-col sm:flex-row items-center gap-3">
                <div className="relative w-full sm:max-w-xs">
                  <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]">search</span>
                  <input 
                    type="text" 
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full h-11 pl-10 pr-4 rounded-xl bg-surface font-body-md text-[14px] text-on-surface placeholder:text-outline border border-outline-variant focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-colors"
                    placeholder="Buscar por razón social..." 
                  />
                </div>
                <div className="flex items-center gap-3 w-full sm:w-auto">
                  <div className="relative flex-1 sm:w-40">
                    <select 
                      value={filterType}
                      onChange={(e) => setFilterType(e.target.value)}
                      className="w-full h-11 appearance-none px-4 rounded-xl bg-surface font-body-md text-[14px] text-on-surface border border-outline-variant focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary cursor-pointer pr-10"
                    >
                      <option value="todos">Tipo Todos</option>
                      <option value="Gasolinera">Gasolinera</option>
                      <option value="Planta LP">Planta LP</option>
                      <option value="Autoconsumo">Autoconsumo</option>
                    </select>
                    <span className="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant text-[20px]">expand_more</span>
                  </div>
                  <div className="relative flex-1 sm:w-40">
                    <select 
                      value={filterStatus}
                      onChange={(e) => setFilterStatus(e.target.value)}
                      className="w-full h-11 appearance-none px-4 rounded-xl bg-surface font-body-md text-[14px] text-on-surface border border-outline-variant focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary cursor-pointer pr-10"
                    >
                      <option value="todos">Estatus Todos</option>
                      <option value="Activa">Activa</option>
                      <option value="En Gracia">En Gracia</option>
                      <option value="Suspendida">Suspendida</option>
                    </select>
                    <span className="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant text-[20px]">expand_more</span>
                  </div>
                </div>
              </div>
              <div className="flex items-center justify-end">
                <button className="h-11 px-5 rounded-xl bg-surface-container-lowest border border-outline-variant hover:bg-surface-container-low text-secondary font-headline-sm text-[14px] font-bold transition-colors flex items-center gap-2" type="button">
                  <span className="material-symbols-outlined text-[18px]">file_download</span>
                  <span>Exportar Directorio SAT / ASEA</span>
                </button>
              </div>
            </section>

            {/* Data Grid */}
            <section className="bg-surface-container-lowest rounded-[20px] shadow-sm overflow-hidden flex flex-col border border-[#c2c7cc]/40">
              <div className="overflow-x-auto w-full">
                <table className="w-full text-left border-collapse min-w-[1000px]">
                  <thead>
                    <tr className="bg-surface-container-low text-on-surface-variant font-mono-label text-[10px] uppercase tracking-wider">
                      <th className="py-4 px-6 font-bold">Razón Social y Comercial</th>
                      <th className="py-4 px-4 font-bold">RFC Fiscal</th>
                      <th className="py-4 px-4 font-bold">Tipo Operación</th>
                      <th className="py-4 px-4 font-bold">Módulos Activos</th>
                      <th className="py-4 px-4 font-bold">Estatus Suscripción</th>
                      <th className="py-4 px-6 text-right font-bold">Acciones</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-surface-container-low">
                    {filteredTenants.map(tenant => (
                      <tr key={tenant.id} className="hover:bg-surface-container/50 transition-colors">
                        <td className="py-4 px-6">
                          <div className="flex items-center gap-4">
                            <div className="w-10 h-10 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center font-headline-sm text-[15px] font-bold shrink-0">
                              {tenant.initials}
                            </div>
                            <div className="flex flex-col">
                              <span className="font-body-md text-[14px] font-bold text-on-surface">{tenant.name}</span>
                              <span className="font-mono-data text-[11px] text-on-surface-variant mt-0.5">{tenant.sub}</span>
                            </div>
                          </div>
                        </td>
                        <td className="py-4 px-4">
                          <span className="px-2.5 py-1 rounded bg-surface-container font-mono-data text-[11px] font-bold text-primary">
                            {tenant.rfc}
                          </span>
                        </td>
                        <td className="py-4 px-4">
                          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-surface-container-high font-mono-label text-[10px] font-bold text-secondary uppercase tracking-wider">
                            <span className="w-1.5 h-1.5 rounded-full bg-secondary"></span>
                            {tenant.type}
                          </span>
                        </td>
                        <td className="py-4 px-4">
                          <div className="flex flex-col gap-1.5 items-start">
                            {tenant.modules.map(mod => (
                              <span key={mod} className={`px-2 py-0.5 rounded font-mono-label text-[10px] font-bold tracking-wider uppercase ${mod === 'CV-SAT' ? 'bg-[#002c3a] text-white' : 'bg-[#e2f3ff] text-[#1c6e8c]'}`}>
                                {mod}
                              </span>
                            ))}
                          </div>
                        </td>
                        <td className="py-4 px-4">
                          {tenant.status === 'Activa' && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#e2f3ff] text-[#1c6e8c] font-mono-label text-[10px] font-bold uppercase tracking-wider">
                              <span className="w-1.5 h-1.5 rounded-full bg-[#1c6e8c]"></span>Activa
                            </span>
                          )}
                          {tenant.status === 'En Gracia' && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#d5ebfa] text-[#00617f] font-mono-label text-[10px] font-bold uppercase tracking-wider">
                              <span className="w-1.5 h-1.5 rounded-full bg-[#1c6e8c]"></span>En Gracia
                            </span>
                          )}
                          {tenant.status === 'Suspendida' && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#ffdad6] text-[#ba1a1a] font-mono-label text-[10px] font-bold uppercase tracking-wider">
                              <span className="w-1.5 h-1.5 rounded-full bg-[#ba1a1a]"></span>Suspendida
                            </span>
                          )}
                        </td>
                        <td className="py-4 px-6 text-right">
                          <div className="flex items-center justify-end gap-3">
                            <button className="h-9 px-3 rounded-full bg-surface-container hover:bg-surface-container-high text-[#1c6e8c] font-body-sm text-[13px] font-bold transition-colors flex items-center gap-1.5" type="button">
                              <span className="material-symbols-outlined text-[16px]">settings</span>
                              <span>Módulos</span>
                            </button>
                            <button className="w-9 h-9 rounded-full hover:bg-surface-container text-on-surface-variant flex items-center justify-center transition-colors" type="button">
                              <span className="material-symbols-outlined text-[18px]">block</span>
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              {/* Pagination */}
              <div className="py-4 px-6 bg-surface-container-lowest border-t border-[#c2c7cc]/40 flex items-center justify-between">
                <div className="font-mono-data text-[12px] text-on-surface-variant">
                  Mostrando registros <span className="font-bold text-on-surface">1 al 5</span> de un total de <span className="font-bold text-on-surface">48 empresas auditadas</span>
                </div>
                <div className="flex items-center gap-1">
                  <button className="h-9 w-9 rounded-xl hover:bg-surface-container flex items-center justify-center text-outline transition-colors" type="button">
                    <span className="material-symbols-outlined text-[18px]">chevron_left</span>
                  </button>
                  <button className="h-9 w-9 rounded-xl bg-[#154F66] text-white font-mono-label text-[12px] font-bold shadow-sm" type="button">1</button>
                  <button className="h-9 w-9 rounded-xl hover:bg-surface-container text-on-surface font-mono-label text-[12px] font-bold transition-colors" type="button">2</button>
                  <button className="h-9 w-9 rounded-xl hover:bg-surface-container text-on-surface font-mono-label text-[12px] font-bold transition-colors" type="button">3</button>
                  <span className="px-2 font-mono-label text-[12px] text-outline tracking-widest">...</span>
                  <button className="h-9 w-9 rounded-xl hover:bg-surface-container text-on-surface font-mono-label text-[12px] font-bold transition-colors" type="button">10</button>
                  <button className="h-9 w-9 rounded-xl hover:bg-surface-container flex items-center justify-center text-on-surface-variant transition-colors" type="button">
                    <span className="material-symbols-outlined text-[18px]">chevron_right</span>
                  </button>
                </div>
              </div>
            </section>

            {/* Banner Criptográfico */}
            <section className="bg-[#1e333e] p-6 rounded-[20px] text-white flex flex-col md:flex-row items-center justify-between gap-6 shadow-md mt-2">
              <div className="flex items-center gap-5">
                <div className="w-12 h-12 rounded-xl bg-[#002c3a] flex items-center justify-center text-[#95dbfd] shrink-0 border border-white/5">
                  <span className="material-symbols-outlined text-[24px]">shield</span>
                </div>
                <div className="flex flex-col">
                  <div className="font-mono-label text-[10px] text-[#95dbfd] uppercase tracking-wider font-bold mb-1">
                    Bitácora Criptográfica Inmutable • Soporte N4 Certificado
                  </div>
                  <p className="font-body-md text-[14px] text-white/80">
                    Última asignación ejecutada por el operador <strong className="text-white font-bold">Super Admin</strong> con registro de integridad criptográfico registrado en libro mayor.
                  </p>
                  <div className="flex items-center gap-3 mt-1.5">
                    <span className="font-mono-label text-[10px] text-white/50">Hash SHA-256</span>
                    <span className="font-mono-data text-[11px] text-[#bce9ff] font-bold tracking-wider">
                      a9f8742b6d13e9c5e4f80029b3ca738d99fec38b7123efb0114a873199bc45de
                    </span>
                  </div>
                </div>
              </div>
              <div className="shrink-0">
                <button className="h-11 px-6 rounded-full bg-[#002c3a] hover:bg-black/20 text-[#bce9ff] border border-[#bce9ff]/20 font-headline-sm text-[14px] font-bold transition-all flex items-center gap-2" type="button">
                  <span className="material-symbols-outlined text-[18px]">verified</span>
                  <span>Validar Sello Digital</span>
                </button>
              </div>
            </section>
          </div>
          ) : (
            <div className="flex flex-col items-center justify-center h-full w-full py-20 text-center">
              <span className="material-symbols-outlined text-[64px] text-surface-container-high mb-4">construction</span>
              <h2 className="font-headline-lg text-[24px] font-bold text-primary mb-2">
                Módulo en Construcción
              </h2>
              <p className="font-body-md text-on-surface-variant max-w-md">
                Esta sección de <span className="font-bold text-secondary capitalize">{currentTab}</span> está siendo adaptada para el Nivel Global del Super Admin.
              </p>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
