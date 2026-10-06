import re

html_content = """
<aside class="fixed left-0 top-0 h-full w-[268px] bg-[#0C2B3A] text-[#F1F5F7] z-50 flex flex-col justify-between shadow-[4px_0_24px_rgba(12,43,58,0.18)]">
<div class="flex flex-col flex-1 overflow-y-auto px-4 py-4">
<!-- LOGOTIPO BRAND OFICIAL SUELVO -->
<div class="flex items-center gap-2 px-2 pt-1 pb-6 border-b border-[#F1F5F7]/10 mb-4"><div class="flex flex-col gap-1"><img alt="Logo Suelvo" class="h-9 w-auto object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBWfEA0XNqQJ05IW8XtPb9rGy68tvs6jYugoeGdzb2heo2DM1ISLBd8Ic3y8FHfKh3CaW_0LQwthrw-nTT-67Ybrqcw9NuqjuT5xmM-YBZEC18V-aODfqMZ0U9JYmOXGGTSudqGjSByyFj4TiWR00miKThcQiCI5VsUOZ5hh20SoqjJYLTSBHKERUEFDxAbWKNtW8wEgHYvhcquifa7OfHaweVCpKSDPN8oceOnorquW3wb--3266gbvT2q_MDUIwUchtFUi_rTeIHPrbY"><span class="font-mono-val text-[10px] text-[#F1F5F7]/70 tracking-wider uppercase pl-1">Plataforma Legal Gas</span></div></div>
<!-- SECCIÓN OPERACIÓN Y CONTROL -->
<div class="mb-2 px-2.5">
<span class="font-mono-val text-[11px] text-[#4FB3D9] uppercase tracking-wider font-semibold">Operación y Control</span>
</div>
<nav class="flex flex-col gap-1 mb-5" id="sidebarNav"><!-- Dashboard -->
<button class={navButtonClasses(currentView === 'dashboard')} onClick={() => navigateTo('dashboard')} type="button">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-[20px] text-[#4FB3D9]/70 group-hover:text-[#4FB3D9]">grid_view</span>
<span class="text-[#F1F5F7]/90 group-hover:text-[#FFFFFF]">Dashboard</span>
</div>
</button>
<!-- Bóveda Documental -->
<button class={navButtonClasses(currentView === 'boveda')} onClick={() => navigateTo('boveda')} type="button">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-[20px] text-[#4FB3D9]/70 group-hover:text-[#4FB3D9]">folder_supervised</span>
<span class="text-[#F1F5F7]/90 group-hover:text-[#FFFFFF]">Bóveda Documental</span>
</div>
</button>
<!-- Instalaciones / Estaciones de Servicio (Activo) -->
<button class={navButtonClasses(currentView === 'instalaciones')} onClick={() => navigateTo('instalaciones')} type="button">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-[20px] text-[#4FB3D9]">local_gas_station</span>
<span class="text-[#FFFFFF]">Estaciones de Servicio</span>
</div>
{currentView === 'instalaciones' && <span class="font-mono-val text-[10px] bg-[#4FB3D9]/20 text-[#4FB3D9] px-2 py-0.5 rounded-full font-semibold">Activo</span>}
</button></nav>
<!-- SECCIÓN MÓDULOS REGULADOS BLOQUEADOS -->
<div class="mb-2 px-2.5 pt-2 border-t border-[#F1F5F7]/10">
<span class="font-mono-val text-[11px] text-[#F1F5F7]/50 uppercase tracking-wider">Módulos Regulados ASEA CNE</span>
</div>
<div class="flex flex-col gap-1 text-[13px]">
<div class="flex items-center justify-between px-3 py-2 rounded-lg text-[#F1F5F7]/40 select-none cursor-not-allowed">
<div class="flex items-center gap-2.5">
<span class="material-symbols-outlined text-[17px] text-[#F1F5F7]/30">lock</span>
<span class="">SASISOPA</span>
</div>
<span class="font-mono-val text-[10px] bg-[rgba(242,183,5,0.18)] text-[#F2B705] px-1.5 py-0.5 rounded font-medium">Próximamente</span>
</div>
<div class="flex items-center justify-between px-3 py-2 rounded-lg text-[#F1F5F7]/40 select-none cursor-not-allowed">
<div class="flex items-center gap-2.5">
<span class="material-symbols-outlined text-[17px] text-[#F1F5F7]/30">lock</span>
<span class="">NOM-005-ASEA</span>
</div>
<span class="font-mono-val text-[10px] bg-[rgba(242,183,5,0.18)] text-[#F2B705] px-1.5 py-0.5 rounded font-medium">Próximamente</span>
</div>
<div class="flex items-center justify-between px-3 py-2 rounded-lg text-[#F1F5F7]/40 select-none cursor-not-allowed">
<div class="flex items-center gap-2.5">
<span class="material-symbols-outlined text-[17px] text-[#F1F5F7]/30">lock</span>
<span class="">NOM-016</span>
</div>
<span class="font-mono-val text-[10px] bg-[rgba(242,183,5,0.18)] text-[#F2B705] px-1.5 py-0.5 rounded font-medium">Próximamente</span>
</div>
<div class="flex items-center justify-between px-3 py-2 rounded-lg text-[#F1F5F7]/40 select-none cursor-not-allowed">
<div class="flex items-center gap-2.5">
<span class="material-symbols-outlined text-[17px] text-[#F1F5F7]/30">lock</span>
<span class="">NOM-018-ASEA-2023</span>
</div>
<span class="font-mono-val text-[10px] bg-[rgba(242,183,5,0.18)] text-[#F2B705] px-1.5 py-0.5 rounded font-medium">Próximamente</span>
</div>
</div>
</div>
<!-- PIE DEL SIDEBAR (CIFRADO Y ESTÁNDAR) -->
<div class="p-3.5 bg-[#081F2B] border-t border-[#F1F5F7]/10 m-3 rounded-2xl flex flex-col gap-2">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[#4FB3D9] text-[18px]">verified_user</span>
<span class="font-mono-val text-[11px] text-[#FFFFFF] tracking-wider uppercase font-semibold">Cifrado Criptográfico</span>
</div>
<p class="font-mono-val text-[10px] text-[#F1F5F7]/60 leading-tight">Cumplimiento LFPDPPP y Estándar ISO 27001</p>
<div class="flex items-center justify-between pt-1 border-t border-[#F1F5F7]/10 font-mono-val text-[10px]">
<span class="text-[#F1F5F7]/70">RMF Fiscal 2026</span>
<span class="text-[#4FB3D9] font-medium">v4.18.0</span>
</div>
</div>
</aside>
<!-- CONTENEDOR PRINCIPAL DERECHO -->
<div class="pl-[268px] min-h-screen bg-[#F4F6F7]">
<!-- HEADER SUPERIOR FIJO -->
<header class="fixed top-0 left-[268px] right-0 h-16 bg-[#FFFFFF] border-b border-[#0C2B3A]/10 shadow-[0_1px_6px_rgba(12,43,58,0.05)] z-40 flex items-center justify-between px-8">
<div class="flex items-center gap-4">
<!-- Selector interactivo de Estación -->
<div class="relative">
<button class="flex items-center gap-3 bg-[#F4F6F7] hover:bg-[#0C2B3A]/5 py-1.5 px-3.5 rounded-xl border border-[#0C2B3A]/10 transition-colors group" id="stationSelectBtn" onClick={() => toggleStationMenu()} type="button">
<span class="material-symbols-outlined text-[#1C6E8C] text-[20px]">local_gas_station</span>
<div class="flex flex-col text-left">
<span class="font-mono-val text-[10px] text-[#1C6E8C] font-bold uppercase tracking-wider">Instalación Activa</span>
<span class="font-mono-val text-[12px] font-semibold text-[#0C2B3A]" id="currentStationLabel">{activeStation}</span>
</div>
<span class="material-symbols-outlined text-[#4A5F6B] text-[18px] ml-1 group-hover:text-[#0C2B3A]">expand_more</span>
</button>
<!-- Menú flotante de estaciones -->
<div class={`absolute left-0 mt-2 w-80 rounded-2xl bg-[#FFFFFF] p-2 shadow-xl border border-[#0C2B3A]/10 z-50 space-y-1 ${isStationMenuOpen ? '' : 'hidden'}`} id="stationMenu">
<button class="w-full text-left px-3 py-2 rounded-xl text-[13px] text-[#0C2B3A] hover:bg-[#F4F6F7] flex flex-col" onClick={() => setStation('Estación Las Palmas PL/12345/EXP/ES/2015')} type="button">
<span class="font-bold">Estación Las Palmas</span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">PL/12345/EXP/ES/2015 Activa</span>
</button>
<button class="w-full text-left px-3 py-2 rounded-xl text-[13px] text-[#0C2B3A] hover:bg-[#F4F6F7] flex flex-col" onClick={() => setStation('Estación San Jerónimo PL/09421/EXP/ES/2017')} type="button">
<span class="font-bold">Estación San Jerónimo</span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">PL/09421/EXP/ES/2017 Activa</span>
</button>
<button class="w-full text-left px-3 py-2 rounded-xl text-[13px] text-[#0C2B3A] hover:bg-[#F4F6F7] flex flex-col" onClick={() => setStation('Planta Gas El Roble G/33912/LPG/2019')} type="button">
<span class="font-bold">Planta Gas El Roble</span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">G/33912/LPG/2019 Activa</span>
</button>
<button class="w-full text-left px-3 py-2 rounded-xl text-[13px] text-[#0C2B3A] hover:bg-[#F4F6F7] flex flex-col" onClick={() => setStation('Servicentro Aeropuerto PL/98765/EXP/ES/2018')} type="button">
<span class="font-bold">Servicentro Aeropuerto</span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">PL/98765/EXP/ES/2018 Activa</span>
</button>
</div>
</div>
<!-- Indicador de enlace SAT -->
<div class="hidden xl:flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C6E8C]/10 border border-[#1C6E8C]/20">
<span class="w-2 h-2 rounded-full bg-[#1C6E8C] animate-pulse"></span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Sincronización SAT Anexo 21</span>
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold">En línea</span>
</div>
</div>
<!-- Área de Notificaciones y Usuario -->
<div class="flex items-center gap-4">
<button aria-label="Notificaciones Regulatorias" class="relative p-2 rounded-full text-[#4A5F6B] hover:text-[#0C2B3A] hover:bg-[#F4F6F7] transition-colors" onClick={() => showToast('No hay notificaciones críticas pendientes')} type="button">
<span class="material-symbols-outlined text-[22px]">notifications</span>
<span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-[#B42318] ring-2 ring-[#FFFFFF]"></span>
</button>
<div class="h-8 w-px bg-[#0C2B3A]/10"></div>
<div class="flex items-center gap-3">
<div class="flex flex-col text-right hidden sm:flex">
<span class="font-heading font-bold text-[14px] text-[#0C2B3A] leading-tight">Roberto Mendoza</span>
<span class="font-mono-val text-[10px] text-[#4A5F6B]">Gerente de Cumplimiento</span>
</div>
<div class="w-9 h-9 rounded-full bg-[#0C2B3A] flex items-center justify-center text-[#FFFFFF] shadow-sm">
<span class="material-symbols-outlined text-[20px]">person</span>
</div>
</div>
</div>
</header>
<!-- ÁREA DE CONTENIDO PRINCIPAL -->
<main class="pt-20 px-8 pb-12 bg-[#F4F6F7] min-h-screen">
<!-- ============================================== -->
<!-- VISTA 1: DASHBOARD PRINCIPAL                   -->
<!-- ============================================== -->
<div class={`space-y-6 ${currentView === 'dashboard' ? '' : 'hidden'}`} id="view-dashboard">
<!-- BANNER DE URGENCIA REGULATORIA (STICKY) -->
{isAlertVisible && (
<aside class="sticky top-20 z-30 flex items-center justify-between px-5 py-3 rounded-2xl bg-[rgba(242,183,5,0.18)] border border-[#8A5A00]/25 shadow-sm backdrop-blur-md">
<div class="flex items-center gap-3 min-w-0">
<span class="material-symbols-outlined text-[22px] text-[#8A5A00] flex-shrink-0">warning</span>
<p class="text-[14px] font-semibold text-[#8A5A00] truncate">
              Vence en 30 días el Dictamen NOM-005 de hermeticidad y pruebas de vapor para tanques de almacenamiento
            </p>
</div>
<div class="flex items-center gap-3 flex-shrink-0 ml-4">
<button class="px-4 py-1.5 rounded-full text-[13px] font-bold text-[#8A5A00] bg-[#FFFFFF] border border-[#8A5A00]/30 hover:bg-[#8A5A00]/10 transition-colors shadow-sm" onClick={() => openRenovacionModal()} type="button">
              Gestionar renovación
            </button>
<button aria-label="Cerrar notificación" class="p-1 rounded-full text-[#8A5A00] hover:bg-[#8A5A00]/20 transition-colors" onClick={() => setIsAlertVisible(false)} type="button">
<span class="material-symbols-outlined text-[18px]">close</span>
</button>
</div>
</aside>
)}
<!-- ENCABEZADO DE VISTA Y ACCIÓN PRINCIPAL ÚNICA -->
<section class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
<div class="space-y-1">
<div class="flex items-center gap-3">
<h1 class="font-heading text-[28px] font-bold text-[#0C2B3A] tracking-tight leading-none">Resumen Operativo y Cumplimiento</h1>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] bg-[#0C2B3A]/10 text-[#0C2B3A] font-bold uppercase tracking-wider">RMF 2026</span>
</div>
<p class="text-[14px] text-[#4A5F6B]">
              Monitoreo integral de obligaciones ante CNE ASEA y SAT para {activeStation}
            </p>
</div>
<!-- BOTÓN PRIMARIO ÚNICO EN LA VISTA -->
<div class="flex items-center gap-3">
<button class="h-11 px-6 rounded-full bg-[#1C6E8C] hover:bg-[#154F66] text-[#FFFFFF] font-heading font-semibold text-[14px] flex items-center gap-2.5 shadow-md shadow-[#1C6E8C]/20 transition-all active:scale-[0.98]" onClick={() => openVolumetricModal()} type="button">
<span class="material-symbols-outlined text-[20px]">upload_file</span>
<span class="">Cargar reporte volumétrico mensual</span>
</button>
</div>
</section>
<!-- GRID PRINCIPAL DEL DASHBOARD (8 COLS IZQ + 4 COLS DER) -->
<div class="grid grid-cols-12 gap-6">
<!-- COLUMNA PRINCIPAL (8 COLUMNAS) -->
<div class="col-span-12 xl:col-span-8 space-y-6">
<!-- TARJETA COMPLIANCE SCORE HERO -->
<section class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col md:flex-row items-center gap-6">
<!-- Anillo Circular SVG con Porcentaje en Plex Mono -->
<div class="relative flex-shrink-0 w-44 h-44 flex items-center justify-center">
<svg class="w-full h-full transform -rotate-90" viewBox="0 0 160 160">
<circle class="text-[#F4F6F7]" cx="80" cy="80" fill="transparent" r="68" stroke="currentColor" stroke-width="14"></circle>
<circle class="text-[#1C6E8C]" cx="80" cy="80" fill="transparent" r="68" stroke="currentColor" stroke-dasharray="427.25" stroke-dashoffset="17.09" stroke-linecap="round" stroke-width="14"></circle>
</svg>
<div class="absolute inset-0 flex flex-col items-center justify-center text-center">
<span class="font-mono-val text-[2.75rem] leading-none font-bold text-[#0C2B3A]">96%</span>
<span class="font-mono-val text-[11px] text-[#1C6E8C] uppercase font-bold mt-1 tracking-wider">Dictaminado</span>
</div>
</div>
<!-- Resumen de Obligaciones y Progreso de Cumplimiento -->
<div class="flex-1 w-full space-y-3">
<div class="flex flex-wrap items-center justify-between gap-2">
<div>
<div class="flex items-center gap-2.5">
<span class="font-heading text-[22px] text-[#0C2B3A] font-bold">Al día</span>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[#1C6E8C]/10 text-[#1C6E8C]">
                        Vigente con 24 de 25 obligaciones al corriente
                      </span>
</div>
<p class="text-[13px] text-[#4A5F6B] mt-1">
                      Evaluación automatizada contra normativas ASEA CNE y Anexo 21 RMF
                    </p>
</div>
<span class="font-mono-val text-[12px] text-[#4A5F6B]">Corte 29-mar-2026</span>
</div>
<!-- Barras de desglose por organismo -->
<div class="space-y-2.5 pt-1">
<div>
<div class="flex justify-between text-[12px] mb-1 font-medium">
<span class="text-[#0C2B3A]">Controles Volumétricos SAT</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">100% Al día</span>
</div>
<div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden">
<div class="h-full bg-[#1C6E8C] rounded-full" style="width: 100%;"></div>
</div>
</div>
<div>
<div class="flex justify-between text-[12px] mb-1 font-medium">
<span class="text-[#0C2B3A]">Licencias ambientales ASEA</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">95% Al día</span>
</div>
<div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden">
<div class="h-full bg-[#1C6E8C] rounded-full" style="width: 95%;"></div>
</div>
</div>
<div>
<div class="flex justify-between text-[12px] mb-1 font-medium">
<span class="text-[#0C2B3A]">Permisos CNE</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">100% Al día</span>
</div>
<div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden">
<div class="h-full bg-[#1C6E8C] rounded-full" style="width: 100%;"></div>
</div>
</div>
<div>
<div class="flex justify-between text-[12px] mb-1 font-medium">
<span class="text-[#0C2B3A]">Protocolos de emergencia</span>
<span class="font-mono-val text-[#8A5A00] font-bold">88% Por vencer</span>
</div>
<div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden">
<div class="h-full bg-[#F2B705] rounded-full" style="width: 88%;"></div>
</div>
</div>
</div>
</div>
</section>
<!-- GRID 2x2 DE TARJETAS REGULATORIAS -->
<section class="grid grid-cols-1 md:grid-cols-2 gap-5">
<!-- TARJETA 1: CONTROLES VOLUMÉTRICOS -->
<article class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col justify-between hover:border-[#1C6E8C]/40 transition-all">
<div>
<div class="flex items-center justify-between mb-3">
<span class="font-mono-val text-[11px] uppercase text-[#4A5F6B] tracking-wider font-semibold">Anexo 21 RMF 2026</span>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[#1C6E8C]/10 text-[#1C6E8C]">Al día</span>
</div>
<h2 class="font-heading text-[18px] font-bold text-[#0C2B3A] mb-1">Controles Volumétricos</h2>
<p class="text-[13px] text-[#4A5F6B] mb-4">Registro continuo de entradas inventarios y salidas en dispensarios certificados</p>
<div class="p-3.5 rounded-xl bg-[#F4F6F7] space-y-2 border border-[#0C2B3A]/5">
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Folio bitácora</span>
<span class="font-mono-val font-bold text-[#0C2B3A]">FOL-2026-03-882</span>
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Última transmisión</span>
<span class="font-mono-val text-[#0C2B3A]">28-mar-2026 23 59 hrs</span>
</div>
</div>
</div>
<div class="mt-4 pt-3 border-t border-[#0C2B3A]/5 flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="w-2.5 h-2.5 rounded-full bg-[#1C6E8C]"></span>
<span class="text-[12px] font-medium text-[#0C2B3A]">Dispersión sin incidencias</span>
</div>
<button class="text-[#1C6E8C] font-heading text-[13px] font-bold hover:underline" onClick={() => showToast('Verificando firmas de control volumétrico')} type="button">
                    Auditar
                  </button>
</div>
</article>
<!-- TARJETA 2: COMPLEMENTO CFDI 4.0 -->
<article class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col justify-between hover:border-[#1C6E8C]/40 transition-all">
<div>
<div class="flex items-center justify-between mb-3">
<span class="font-mono-val text-[11px] uppercase text-[#4A5F6B] tracking-wider font-semibold">SAT Facturación</span>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[#1C6E8C]/10 text-[#1C6E8C]">Al día</span>
</div>
<h2 class="font-heading text-[18px] font-bold text-[#0C2B3A] mb-1">Complemento CFDI 4.0</h2>
<p class="text-[13px] text-[#4A5F6B] mb-4">Cruce de facturas expedidas frente a lecturas de totalizadores de venta</p>
<div class="p-3.5 rounded-xl bg-[#F4F6F7] space-y-2 border border-[#0C2B3A]/5">
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Timbrados conciliados</span>
<span class="font-mono-val font-bold text-[#0C2B3A]">14,820 folios</span>
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Discrepancias fiscales</span>
<span class="font-mono-val font-bold text-[#1C6E8C]">0 detectadas</span>
</div>
</div>
</div>
<div class="mt-4 pt-3 border-t border-[#0C2B3A]/5 flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[18px] text-[#1C6E8C]">task_alt</span>
<span class="text-[12px] text-[#4A5F6B]">Conciliado con tanques</span>
</div>
<button class="text-[#1C6E8C] font-heading text-[13px] font-bold hover:underline" onClick={() => showToast('Cargando desglose de totalizadores fiscales')} type="button">
                    Detalles
                  </button>
</div>
</article>
<!-- TARJETA 3: DICTÁMENES NOM-005 -->
<article class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col justify-between hover:border-[#8A5A00]/40 transition-all">
<div>
<div class="flex items-center justify-between mb-3">
<span class="font-mono-val text-[11px] uppercase text-[#4A5F6B] tracking-wider font-semibold">NOM-005-ASEA</span>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[rgba(242,183,5,0.18)] text-[#8A5A00]">Por vencer</span>
</div>
<h2 class="font-heading text-[18px] font-bold text-[#0C2B3A] mb-1">Dictámenes y Calibración Tanques</h2>
<p class="text-[13px] text-[#4A5F6B] mb-4">Pruebas acústicas de hermeticidad y calibración volumétrica de sondas</p>
<div class="p-3.5 rounded-xl bg-[#F4F6F7] space-y-2 border border-[#0C2B3A]/5">
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Fecha límite improrrogable</span>
<span class="font-mono-val font-bold text-[#8A5A00]">30-abr-2026</span>
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Unidad Verificadora</span>
<span class="font-mono-val text-[#0C2B3A]">UV-ASEA-044 En sitio</span>
</div>
</div>
</div>
<div class="mt-4 pt-3 border-t border-[#0C2B3A]/5 flex items-center justify-between">
<span class="text-[12px] text-[#8A5A00] font-semibold">Inspección física en curso</span>
<button class="text-[#1C6E8C] font-heading text-[13px] font-bold hover:underline" onClick={() => openRenovacionModal()} type="button">
                    Cargar Acta
                  </button>
</div>
</article>
<!-- TARJETA 4: PÓLIZA DE SEGURO AMBIENTAL -->
<article class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col justify-between hover:border-[#1C6E8C]/40 transition-all">
<div>
<div class="flex items-center justify-between mb-3">
<span class="font-mono-val text-[11px] uppercase text-[#4A5F6B] tracking-wider font-semibold">Regulación ASEA</span>
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[#1C6E8C]/10 text-[#1C6E8C]">Al día</span>
</div>
<h2 class="font-heading text-[18px] font-bold text-[#0C2B3A] mb-1">Póliza de Seguro Ambiental</h2>
<p class="text-[13px] text-[#4A5F6B] mb-4">Responsabilidad civil y ambiental por derrames o contaminación de subsuelo</p>
<div class="p-3.5 rounded-xl bg-[#F4F6F7] space-y-2 border border-[#0C2B3A]/5">
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Folio ambiental activo</span>
<span class="font-mono-val font-bold text-[#0C2B3A]">ASEA-POL-8492</span>
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Vigencia contractual</span>
<span class="font-mono-val text-[#0C2B3A]">15-nov-2026</span>
</div>
</div>
</div>
<div class="mt-4 pt-3 border-t border-[#0C2B3A]/5 flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[18px] text-[#1C6E8C]">verified</span>
<span class="text-[12px] text-[#4A5F6B]">Cobertura integral activa</span>
</div>
<button class="text-[#1C6E8C] font-heading text-[13px] font-bold hover:underline" onClick={() => previewDocument('Póliza Integral Responsabilidad Civil y Ambiental')} type="button">
                    Ver póliza
                  </button>
</div>
</article>
</section>
<!-- SECCIÓN FOTOGRÁFICA DE INSTALACIONES EN SITIO -->
<section class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)]">
<div class="flex items-center justify-between mb-4">
<div>
<h3 class="font-heading text-[18px] font-bold text-[#0C2B3A]">Inspección de Infraestructura Crítica</h3>
<p class="text-[13px] text-[#4A5F6B]">Evidencia fotográfica georreferenciada para auditorías de campo</p>
</div>
<span class="font-mono-val text-[11px] text-[#4A5F6B] bg-[#F4F6F7] px-2.5 py-1 rounded-lg">3 puntos monitoreados</span>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
<div class="space-y-2">
<div class="h-36 rounded-xl overflow-hidden bg-[#F4F6F7] border border-[#0C2B3A]/10">
<img alt="Dispensarios Isla 1 y 2" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBj457S8FbVAuS7JXBxSTqJ6jsoIPyQ3xvSZseYDa0Iq7cCTul-Vj4hWg0VhjgR4mbNQTsZkgZRnCapgGnnqfq9AvthQjk4-8XF_KZmYF0X6s_-kBXKExMOJlOAhco8qIpdxZXKW4W9SW01wFZ5lTfeRRpZlU8-y5nS0BTbw4afRiJWz_aRTOweS6n7HD9CRp11WVyRHGN_Z58bOKWX0XslZvGcO_cer4D4MHN9DmDe5Sq0-LF4nHrqog" />
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="font-bold text-[#0C2B3A]">Dispensarios Isla 1 y 2</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">Sellos intactos</span>
</div>
</div>
<div class="space-y-2">
<div class="h-36 rounded-xl overflow-hidden bg-[#F4F6F7] border border-[#0C2B3A]/10">
<img alt="Boca de Tanque Magna" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCDi9ZmoYOhhe9Fl63RmOa7sMEtGYy3gqhE48G_v-rdHFrz298xOJMW7hpYv2lQ1pA6R4_m5w1NMup5vc8eC9-ZirD8CVeadUoCF6JgK8qpeb0FZ8bg9LOs504KTnkgKgD1f_0zwCfnDr1THDHZWXGCm91X2O_arLr_yyCa2-vEtFh0r5I9reqfDjbx3AuE53QOhvxJMbebRtvMHn9mvr6PVeLG03JqdjfucIpWp1qh6XOHluu1ZcjHfA" />
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="font-bold text-[#0C2B3A]">Boca de Tanque Magna</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">Sensor activo</span>
</div>
</div>
<div class="space-y-2">
<div class="h-36 rounded-xl overflow-hidden bg-[#F4F6F7] border border-[#0C2B3A]/10">
<img alt="Consola Telemetría Veeder" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAXC0W2w7_2AIq6-0f3GwXge8uVDwxOpTrh0ukV5APHzeOU8CWAjZClme_3f6ViMaRTS2dy3l9w8k319rMRBQidotXmr1fIXPqcUFGO1UtRw2Gb_8nlT9Ilhxf9h9hhwSy9HUQHpaoCxISplMzlJlkjsVqRdS9au3sQGvYybs0fq1jLpm6kZHI3v27O2T9UsptXlOOyyyW9Gv1l5gJbaht2_jaB_53Ozty2Q7-F5ijINWIkF_Qin4uDEA" />
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="font-bold text-[#0C2B3A]">Consola Telemetría Veeder</span>
<span class="font-mono-val text-[#1C6E8C] font-bold">Conectado</span>
</div>
</div>
</div>
</section>
</div>
<!-- COLUMNA DERECHA (4 COLUMNAS) -->
<aside class="col-span-12 xl:col-span-4 space-y-6">
<!-- TARJETA BITÁCORA DE ACTIVIDAD RECIENTE -->
<section class="p-6 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] flex flex-col">
<div class="flex items-center justify-between mb-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-[#1C6E8C] text-[22px]">history</span>
<h2 class="font-heading text-[17px] font-bold text-[#0C2B3A]">Bitácora de actividad reciente</h2>
</div>
<span class="font-mono-val text-[10px] bg-[#F4F6F7] px-2 py-0.5 rounded text-[#4A5F6B] font-semibold">En vivo</span>
</div>
<!-- Filtros rápidos de timeline -->
<div class="flex items-center gap-1.5 mb-4">
<button class={`px-3 py-1 rounded-full font-mono-val text-[11px] ${timelineFilter === 'all' ? 'bg-[#0C2B3A] text-[#FFFFFF] font-bold' : 'text-[#4A5F6B] hover:bg-[#F4F6F7]'}`} id="filterBtn-all" onClick={() => filterTimeline('all')} type="button">Todos</button>
<button class={`px-3 py-1 rounded-full font-mono-val text-[11px] ${timelineFilter === 'sat' ? 'bg-[#0C2B3A] text-[#FFFFFF] font-bold' : 'text-[#4A5F6B] hover:bg-[#F4F6F7]'}`} id="filterBtn-sat" onClick={() => filterTimeline('sat')} type="button">SAT</button>
<button class={`px-3 py-1 rounded-full font-mono-val text-[11px] ${timelineFilter === 'asea' ? 'bg-[#0C2B3A] text-[#FFFFFF] font-bold' : 'text-[#4A5F6B] hover:bg-[#F4F6F7]'}`} id="filterBtn-asea" onClick={() => filterTimeline('asea')} type="button">ASEA</button>
<button class={`px-3 py-1 rounded-full font-mono-val text-[11px] ${timelineFilter === 'alerta' ? 'bg-[#0C2B3A] text-[#FFFFFF] font-bold' : 'text-[#4A5F6B] hover:bg-[#F4F6F7]'}`} id="filterBtn-alerta" onClick={() => filterTimeline('alerta')} type="button">Alertas</button>
</div>
<!-- Lista de Eventos -->
<div class="space-y-4" id="timelineContainer">
<div class={`timeline-item flex items-start gap-3 ${(timelineFilter === 'all' || timelineFilter === 'sat') ? '' : 'hidden'}`} data-cat="sat">
<div class="w-8 h-8 rounded-full bg-[#1C6E8C]/15 text-[#1C6E8C] flex items-center justify-center font-heading text-[12px] font-bold flex-shrink-0">
                    AL
                  </div>
<div class="flex-1 min-w-0 space-y-1">
<p class="text-[13px] text-[#0C2B3A]">
<span class="font-bold text-[#0C2B3A]">Ana López</span> subió el certificado del Anexo 22
                    </p>
<div class="flex items-center gap-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Hace 2 horas</span>
<span class="text-[#0C2B3A]/20 text-[10px]">•</span>
<button class="font-mono-val text-[11px] text-[#1C6E8C] font-bold hover:underline" onClick={() => previewDocument('Certificado Anexo 22')} type="button">
                        Previsualizar archivo
                      </button>
</div>
</div>
</div>
<div class={`timeline-item flex items-start gap-3 ${(timelineFilter === 'all' || timelineFilter === 'sat') ? '' : 'hidden'}`} data-cat="sat">
<div class="w-8 h-8 rounded-full bg-[#1C6E8C]/15 text-[#1C6E8C] flex items-center justify-center flex-shrink-0">
<span class="material-symbols-outlined text-[17px]">verified</span>
</div>
<div class="flex-1 min-w-0 space-y-1">
<p class="text-[13px] text-[#0C2B3A]">
                      Validación automática de archivos JSON de control volumétrico aprobada sin discrepancias
                    </p>
<div class="flex items-center gap-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Hace 4 horas</span>
<span class="text-[#0C2B3A]/20 text-[10px]">•</span>
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-semibold">SAT Sync OK</span>
</div>
</div>
</div>
<div class={`timeline-item flex items-start gap-3 ${(timelineFilter === 'all' || timelineFilter === 'asea') ? '' : 'hidden'}`} data-cat="asea">
<div class="w-8 h-8 rounded-full bg-[#0C2B3A] text-[#FFFFFF] flex items-center justify-center font-heading text-[12px] font-bold flex-shrink-0">
                    RM
                  </div>
<div class="flex-1 min-w-0 space-y-1">
<p class="text-[13px] text-[#0C2B3A]">
<span class="font-bold text-[#0C2B3A]">Roberto Mendoza</span> actualizó la asignación del responsable técnico en SASISOPA
                    </p>
<div class="flex items-center gap-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Ayer</span>
<span class="text-[#0C2B3A]/20 text-[10px]">•</span>
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Firma digital registrada</span>
</div>
</div>
</div>
<div class={`timeline-item flex items-start gap-3 ${(timelineFilter === 'all' || timelineFilter === 'alerta') ? '' : 'hidden'}`} data-cat="alerta">
<div class="w-8 h-8 rounded-full bg-[rgba(242,183,5,0.18)] text-[#8A5A00] flex items-center justify-center flex-shrink-0">
<span class="material-symbols-outlined text-[17px]">crisis_alert</span>
</div>
<div class="flex-1 min-w-0 space-y-1">
<p class="text-[13px] text-[#0C2B3A]">
                      Alerta preventiva generada para dictamen de pruebas de fugas en líneas de distribución
                    </p>
<div class="flex items-center gap-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B]">Hace 2 días</span>
<span class="text-[#0C2B3A]/20 text-[10px]">•</span>
<span class="font-mono-val text-[11px] text-[#8A5A00] font-bold">NOM-005</span>
</div>
</div>
</div>
</div>
<button class="w-full mt-5 py-2.5 rounded-xl font-heading text-[13px] font-bold text-[#1C6E8C] bg-[#1C6E8C]/10 hover:bg-[#1C6E8C]/20 transition-colors" onClick={() => showToast('Cargando registros históricos completos de bitácora')} type="button">
                Ver bitácora completa
              </button>
</section>
<!-- RESUMEN TELEMETRÍA DE TANQUES (CARD DARK #0C2B3A) -->
<section class="p-6 rounded-[20px] bg-[#0C2B3A] text-[#F1F5F7] shadow-md space-y-3">
<div class="flex items-center justify-between">
<span class="font-mono-val text-[11px] uppercase text-[#4FB3D9] tracking-wider font-semibold">Telemetría de Tanques</span>
<span class="flex items-center gap-1.5 text-[#4FB3D9] font-mono-val text-[11px] font-bold">
<span class="w-2 h-2 rounded-full bg-[#4FB3D9] animate-pulse"></span>
                  En línea
                </span>
</div>
<h3 class="font-heading text-[18px] font-bold text-[#FFFFFF]">Inventario en Tiempo Real</h3>
<div class="space-y-3 pt-2">
<div class="p-3 rounded-xl bg-[#081F2B] space-y-1.5 border border-[#F1F5F7]/10">
<div class="flex justify-between items-center text-[13px]">
<span class="text-[#F1F5F7]">Tanque 1 Regular Magna</span>
<span class="font-mono-val text-[#4FB3D9] font-bold">24,350 L (68%)</span>
</div>
<div class="w-full h-1.5 rounded-full bg-[#0C2B3A] overflow-hidden">
<div class="h-full bg-[#4FB3D9] rounded-full" style="width: 68%;"></div>
</div>
</div>
<div class="p-3 rounded-xl bg-[#081F2B] space-y-1.5 border border-[#F1F5F7]/10">
<div class="flex justify-between items-center text-[13px]">
<span class="text-[#F1F5F7]">Tanque 2 Premium</span>
<span class="font-mono-val text-[#4FB3D9] font-bold">18,120 L (82%)</span>
</div>
<div class="w-full h-1.5 rounded-full bg-[#0C2B3A] overflow-hidden">
<div class="h-full bg-[#4FB3D9] rounded-full" style="width: 82%;"></div>
</div>
</div>
<div class="p-3 rounded-xl bg-[#081F2B] space-y-1.5 border border-[#F1F5F7]/10">
<div class="flex justify-between items-center text-[13px]">
<span class="text-[#F1F5F7]">Tanque 3 Diésel Automotriz</span>
<span class="font-mono-val text-[#4FB3D9] font-bold">31,040 L (45%)</span>
</div>
<div class="w-full h-1.5 rounded-full bg-[#0C2B3A] overflow-hidden">
<div class="h-full bg-[#4FB3D9] rounded-full" style="width: 45%;"></div>
</div>
</div>
</div>
<div class="pt-2 flex justify-between items-center font-mono-val text-[11px]">
<span class="text-[#F1F5F7]/60">Margen error permitido 0.5%</span>
<span class="text-[#4FB3D9] font-bold">Actual 0.08% OK</span>
</div>
</section>
</aside>
</div>
</div>
<!-- ============================================== -->
<!-- VISTA 2: BÓVEDA DOCUMENTAL SPA (CONMUTABLE)     -->
<!-- ============================================== -->
<div class={`space-y-6 ${currentView === 'boveda' ? '' : 'hidden'}`} id="view-boveda">
<div class="p-8 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] space-y-6">
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#0C2B3A]/10 pb-4">
<div>
<div class="flex items-center gap-2 mb-1">
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold uppercase tracking-wider">Repositorio Seguro</span>
<span class="px-2 py-0.2 rounded-full font-mono-val text-[10px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold">Cifrado AES-256</span>
</div>
<h2 class="font-heading text-[24px] font-bold text-[#0C2B3A]">Bóveda Documental Centralizada</h2>
<p class="text-[14px] text-[#4A5F6B]">Archivos probatorios dictámenes y certificados sellados criptográficamente para auditorías</p>
</div>

</div>
<!-- ZONA DRAG & DROP PARA SUBIR ARCHIVOS -->
<div class="p-10 rounded-2xl bg-[#F4F6F7] border-2 border-dashed border-[#1C6E8C]/30 flex flex-col items-center justify-center text-center cursor-pointer transition-all hover:border-[#1C6E8C]" id="dropzone" onDragLeave={(e) => e.currentTarget.classList.remove('border-[#1C6E8C]', 'bg-[#1C6E8C]/5')} onDragOver={(e) => { e.preventDefault(); e.currentTarget.classList.add('border-[#1C6E8C]', 'bg-[#1C6E8C]/5'); }} onDrop={(e) => handleDrop(e)}>
<div class="w-14 h-14 rounded-full bg-[#1C6E8C]/15 flex items-center justify-center text-[#1C6E8C] mb-3">
<span class="material-symbols-outlined text-[30px]">cloud_upload</span>
</div>
<h4 class="font-heading text-[17px] text-[#0C2B3A] font-bold">Arrastra tus archivos de dictamen o reporte aquí</h4>
<p class="text-[13px] text-[#4A5F6B] mt-1 mb-4">Admite formatos PDF firmados XML de volumetría y certificados emitidos por UV</p>
<span class="px-5 py-2 rounded-full font-heading text-[13px] font-bold bg-[#FFFFFF] text-[#1C6E8C] border border-[#1C6E8C]/30 shadow-sm hover:bg-[#1C6E8C]/5 transition-colors">
              Explorar almacenamiento local
            </span>
</div>
<!-- TABLA DE EXPEDIENTES OFICIALES -->
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="font-mono-val text-[11px] text-[#4A5F6B] uppercase border-b border-[#0C2B3A]/10">
<th class="py-3 px-4">Documento</th>
<th class="py-3 px-4">Organismo</th>
<th class="py-3 px-4">Folio Oficial</th>
<th class="py-3 px-4">Vigencia</th>
<th class="py-3 px-4">Estado</th>
<th class="py-3 px-4 text-right">Acción</th>
</tr>
</thead>
<tbody class="divide-y divide-[#0C2B3A]/5 text-[13px]">
<tr class="hover:bg-[#F4F6F7]/60 transition-colors">
<td class="py-3.5 px-4 font-bold text-[#0C2B3A] flex items-center gap-2.5">
<span class="material-symbols-outlined text-[#1C6E8C] text-[20px]">picture_as_pdf</span>
                    Pruebas de Hermeticidad NOM-005 Tanque 1
                  </td>
<td class="py-3.5 px-4 font-mono-val text-[#4A5F6B]">ASEA</td>
<td class="py-3.5 px-4 font-mono-val font-semibold text-[#0C2B3A]">EXP-NOM005-2025-A</td>
<td class="py-3.5 px-4 font-mono-val text-[#0C2B3A]">30-abr-2026</td>
<td class="py-3.5 px-4">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] bg-[rgba(242,183,5,0.18)] text-[#8A5A00] font-bold">Por vencer</span>
</td>
<td class="py-3.5 px-4 text-right">
<button class="text-[#1C6E8C] font-bold hover:underline" onClick={() => previewDocument('Pruebas de Hermeticidad NOM-005 Tanque 1')} type="button">
                      Ver acta
                    </button>
</td>
</tr>
<tr class="hover:bg-[#F4F6F7]/60 transition-colors">
<td class="py-3.5 px-4 font-bold text-[#0C2B3A] flex items-center gap-2.5">
<span class="material-symbols-outlined text-[#1C6E8C] text-[20px]">data_object</span>
                    Bitácora de Eventos Volumétricos Febrero 2026
                  </td>
<td class="py-3.5 px-4 font-mono-val text-[#4A5F6B]">SAT</td>
<td class="py-3.5 px-4 font-mono-val font-semibold text-[#0C2B3A]">SAT-ANX21-88941</td>
<td class="py-3.5 px-4 font-mono-val text-[#0C2B3A]">Permanente</td>
<td class="py-3.5 px-4">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold">Al día</span>
</td>
<td class="py-3.5 px-4 text-right">
<button class="text-[#1C6E8C] font-bold hover:underline" onClick={() => previewDocument('Bitácora de Eventos Volumétricos Febrero 2026')} type="button">
                      Ver JSON
                    </button>
</td>
</tr>
<tr class="hover:bg-[#F4F6F7]/60 transition-colors">
<td class="py-3.5 px-4 font-bold text-[#0C2B3A] flex items-center gap-2.5">
<span class="material-symbols-outlined text-[#1C6E8C] text-[20px]">verified_user</span>
                    Póliza Integral Responsabilidad Civil y Ambiental
                  </td>
<td class="py-3.5 px-4 font-mono-val text-[#4A5F6B]">ASEA</td>
<td class="py-3.5 px-4 font-mono-val font-semibold text-[#0C2B3A]">ASEA-POL-8492</td>
<td class="py-3.5 px-4 font-mono-val text-[#0C2B3A]">15-nov-2026</td>
<td class="py-3.5 px-4">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold">Al día</span>
</td>
<td class="py-3.5 px-4 text-right">
<button class="text-[#1C6E8C] font-bold hover:underline" onClick={() => previewDocument('Póliza Integral Responsabilidad Civil y Ambiental')} type="button">
                      Ver póliza
                    </button>
</td>
</tr>
<tr class="hover:bg-[#F4F6F7]/60 transition-colors">
<td class="py-3.5 px-4 font-bold text-[#0C2B3A] flex items-center gap-2.5">
<span class="material-symbols-outlined text-[#B42318] text-[20px]">gavel</span>
                    Manifiesto de Residuos Peligrosos 2024
                  </td>
<td class="py-3.5 px-4 font-mono-val text-[#4A5F6B]">SEMARNAT</td>
<td class="py-3.5 px-4 font-mono-val font-semibold text-[#0C2B3A]">MAN-SEM-2024-9</td>
<td class="py-3.5 px-4 font-mono-val text-[#0C2B3A]">31-dic-2025</td>
<td class="py-3.5 px-4">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] bg-[#B42318]/10 text-[#B42318] font-bold">Vencido</span>
</td>
<td class="py-3.5 px-4 text-right">
<button class="text-[#B42318] font-bold hover:underline" onClick={() => showToast('Abriendo expediente vencido')} type="button">
                      Regularizar
                    </button>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<!-- ============================================== -->
<!-- VISTA 3: CV-SAT ANEXO 21                       -->
<!-- ============================================== -->
<div class={`space-y-6 ${currentView === 'cvsat' ? '' : 'hidden'}`} id="view-cvsat">
<div class="p-8 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] space-y-6">
<div class="flex items-center justify-between border-b border-[#0C2B3A]/10 pb-4">
<div>
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold uppercase tracking-wider">Cumplimiento SAT RMF 2026</span>
<h2 class="font-heading text-[24px] font-bold text-[#0C2B3A]">Módulo Controles Volumétricos SAT Anexo 21</h2>
<p class="text-[14px] text-[#4A5F6B]">Generación validación y transmisión en tiempo real de archivos JSON criptográficos</p>
</div>
<button class="px-5 py-2 rounded-full font-heading text-[13px] font-bold text-[#FFFFFF] bg-[#1C6E8C] hover:bg-[#154F66] shadow-sm" onClick={() => openVolumetricModal()} type="button">
              Nueva Transmisión
            </button>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-5">
<div class="p-5 rounded-xl bg-[#F4F6F7] border border-[#0C2B3A]/10 space-y-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B] uppercase">Dispensarios Registrados</span>
<p class="font-mono-val text-[26px] font-bold text-[#0C2B3A]">8 mangueras</p>
<span class="text-[12px] font-bold text-[#1C6E8C]">Calibración profeco vigente</span>
</div>
<div class="p-5 rounded-xl bg-[#F4F6F7] border border-[#0C2B3A]/10 space-y-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B] uppercase">Transmisiones SAT Marzo</span>
<p class="font-mono-val text-[26px] font-bold text-[#0C2B3A]">28 de 28</p>
<span class="text-[12px] font-bold text-[#1C6E8C]">100% aceptadas sin error</span>
</div>
<div class="p-5 rounded-xl bg-[#F4F6F7] border border-[#0C2B3A]/10 space-y-2">
<span class="font-mono-val text-[11px] text-[#4A5F6B] uppercase">Margen Discrepancia Global</span>
<p class="font-mono-val text-[26px] font-bold text-[#0C2B3A]">0.04%</p>
<span class="text-[12px] font-bold text-[#1C6E8C]">Tolerancia fiscal máxima 0.5%</span>
</div>
</div>
</div>
</div>
<!-- ============================================== -->
<!-- VISTA 4: CALENDARIO ASEA CRE                   -->
<!-- ============================================== -->
<div class={`space-y-6 ${currentView === 'calendario' ? '' : 'hidden'}`} id="view-calendario">
<div class="p-8 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] space-y-6">
<div class="flex items-center justify-between border-b border-[#0C2B3A]/10 pb-4">
<div>
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold uppercase tracking-wider">Cronograma de Vencimientos</span>
<h2 class="font-heading text-[24px] font-bold text-[#0C2B3A]">Calendario Oficial de Obligaciones ASEA CRE 2026</h2>
<p class="text-[14px] text-[#4A5F6B]">Planificación de visitas de Unidades de Verificación e informes de cumplimiento</p>
</div>
<button class="px-4 py-2 rounded-full font-heading text-[13px] font-bold text-[#0C2B3A] bg-[#F4F6F7] hover:bg-[#0C2B3A]/5" onClick={() => navigateTo('dashboard')} type="button">
              Volver al Dashboard
            </button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-5">
<div class="p-5 rounded-2xl bg-[#F4F6F7] border border-[#0C2B3A]/10 space-y-2">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[rgba(242,183,5,0.18)] text-[#8A5A00]">Programada para 12-abr-2026</span>
<h4 class="font-heading text-[17px] font-bold text-[#0C2B3A]">Inspección de Hermeticidad en Tuberías</h4>
<p class="text-[13px] text-[#4A5F6B]">Prueba requerida bajo NOM-005-ASEA. Unidad Verificadora acreditada UV-CRE-099.</p>
<div class="pt-2 flex justify-between items-center text-[13px]">
<span class="font-mono-val text-[#0C2B3A] font-medium">Auditor Gabriel Zepeda</span>
<button class="text-[#1C6E8C] font-bold hover:underline" onClick={() => showToast('Abriendo citatorio de inspección')} type="button">Ver citatorio</button>
</div>
</div>
<div class="p-5 rounded-2xl bg-[#F4F6F7] border border-[#0C2B3A]/10 space-y-2">
<span class="px-2.5 py-0.5 rounded-full font-mono-val text-[11px] font-bold bg-[#1C6E8C]/10 text-[#1C6E8C]">Aprobada el 15-ene-2026</span>
<h4 class="font-heading text-[17px] font-bold text-[#0C2B3A]">Verificación SASISOPA Etapa Operación</h4>
<p class="text-[13px] text-[#4A5F6B]">Dictamen de cumplimiento con cero no-conformidades mayores detectadas.</p>
<div class="pt-2 flex justify-between items-center text-[13px]">
<span class="font-mono-val text-[#0C2B3A] font-medium">Dictamen DIC-ASEA-2026-04</span>
<button class="text-[#1C6E8C] font-bold hover:underline" onClick={() => previewDocument('Dictamen SASISOPA Etapa Operación')} type="button">Descargar acta</button>
</div>
</div>
</div>
</div>
</div>
<!-- ============================================== -->
<!-- VISTA 5: ESTACIONES DE SERVICIO                -->
<!-- ============================================== -->
<div class={`space-y-6 ${currentView === 'instalaciones' ? '' : 'hidden'}`} id="view-instalaciones"><div class="p-8 rounded-[20px] bg-[#FFFFFF] border border-[#0C2B3A]/10 shadow-[0_4px_16px_rgba(12,43,58,0.04)] space-y-6">
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#0C2B3A]/10 pb-4">
<div>
<div class="flex items-center gap-2 mb-1">
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold uppercase tracking-wider">Padrón Oficial Regulado</span>
<span class="px-2 py-0.2 rounded-full font-mono-val text-[10px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold">3 sucursales activas</span>
</div>
<h2 class="font-heading text-[24px] font-bold text-[#0C2B3A]">Estaciones de Servicio y Plantas</h2>
<p class="text-[14px] text-[#4A5F6B]">Catálogo corporativo de sucursales, permisos de expendio CNE y tanques regulados</p>
</div>
<div class="flex items-center gap-3">

<button class="h-10 px-5 rounded-full bg-[#1C6E8C] hover:bg-[#154F66] text-[#FFFFFF] font-heading font-semibold text-[13px] flex items-center gap-2 shadow-sm transition-all" onClick={() => showToast('Formulario de alta para nueva instalación')} type="button">
<span class="material-symbols-outlined text-[18px]">add_location_alt</span>
<span class="">Registrar estación</span>
</button>
</div>
</div>
<!-- FILTROS RÁPIDOS Y BUSCADOR -->
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
<div class="flex items-center gap-2 flex-wrap">
<button class="px-3.5 py-1.5 rounded-full font-mono-val text-[12px] bg-[#0C2B3A] text-[#FFFFFF] font-bold shadow-sm" type="button">Todas las sucursales (3)</button>
<button class="px-3.5 py-1.5 rounded-full font-mono-val text-[12px] text-[#4A5F6B] bg-[#F4F6F7] hover:bg-[#0C2B3A]/5 border border-[#0C2B3A]/5" type="button">Estaciones de servicio</button>
<button class="px-3.5 py-1.5 rounded-full font-mono-val text-[12px] text-[#4A5F6B] bg-[#F4F6F7] hover:bg-[#0C2B3A]/5 border border-[#0C2B3A]/5" type="button">Plantas de distribución</button>
</div>
<div class="flex items-center gap-2 text-[12px] font-mono-val text-[#4A5F6B]">
<span class="w-2 h-2 rounded-full bg-[#1C6E8C]"></span>
<span class="">Red en sincronía con CRE y ASEA</span>
</div>
</div>
<!-- TABLA COMPLETA DE SUCURSALES -->
<div class="space-y-4"><div class="hidden md:grid grid-cols-12 gap-4 px-6 py-3 bg-[#1C6E8C]/10 border border-[#1C6E8C]/20 rounded-xl text-[12px] font-mono-val font-bold uppercase tracking-wider text-[#0C2B3A] shadow-sm items-center"><div class="col-span-4 flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">domain</span><span class="">Estación o Planta</span></div><div class="col-span-2 flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">badge</span><span class="">Permiso CNE / CRE</span></div><div class="col-span-2 flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">pin_drop</span><span class="">Ubicación</span></div><div class="col-span-2 flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">database</span><span class="">Capacidad y Tanques</span></div><div class="col-span-1 text-center flex items-center justify-center gap-1"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">check_circle</span><span class="">Estatus</span></div><div class="col-span-1 text-right"><span class="">Acción</span></div></div><div class="space-y-3"><div class="relative overflow-hidden rounded-2xl bg-[#FFFFFF] border border-[#0C2B3A]/10 hover:border-[#1C6E8C]/40 shadow-sm hover:shadow-md transition-all"><div class="absolute left-0 top-0 bottom-0 w-1.5 bg-[#1C6E8C]"></div><div class="p-5 pl-7 grid grid-cols-1 md:grid-cols-12 gap-4 items-center"><div class="col-span-12 md:col-span-4 flex items-center gap-3.5"><div class="w-11 h-11 rounded-xl bg-[#1C6E8C]/10 text-[#1C6E8C] flex items-center justify-center flex-shrink-0 border border-[#1C6E8C]/20 shadow-sm"><span class="material-symbols-outlined text-[24px]">local_gas_station</span></div><div class="min-w-0"><div class="flex items-center gap-2"><h3 class="font-heading font-bold text-[16px] text-[#0C2B3A] truncate">Estación Las Palmas</h3><span class="px-2 py-0.2 rounded-full font-mono-val text-[10px] bg-[#0C2B3A]/5 text-[#4A5F6B]">Sucursal 001</span></div><span class="text-[12px] text-[#4A5F6B] block truncate">Carretera Nacional KM 18</span></div></div><div class="col-span-6 md:col-span-2"><span class="font-mono-val text-[12px] font-semibold text-[#0C2B3A] bg-[#F4F6F7] border border-[#0C2B3A]/5 px-2.5 py-1 rounded-lg block truncate">PL/12345/EXP/ES/2015</span></div><div class="col-span-6 md:col-span-2 flex items-center gap-1.5 text-[13px] text-[#4A5F6B]"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">location_on</span><span class="">Hermosillo Sonora</span></div><div class="col-span-6 md:col-span-2 space-y-1.5"><div class="flex items-center justify-between text-[12px]"><span class="font-mono-val font-semibold text-[#0C2B3A]">3 tanques</span><span class="font-mono-val text-[11px] text-[#4A5F6B]">73,510 L</span></div><div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden border border-[#0C2B3A]/5"><div class="h-full bg-[#1C6E8C] rounded-full" style="width: 78%;"></div></div></div><div class="col-span-3 md:col-span-1 text-left md:text-center"><span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full font-mono-val text-[11px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold"><span class="w-1.5 h-1.5 rounded-full bg-[#1C6E8C]"></span>Al día</span></div><div class="col-span-3 md:col-span-1 text-right"><button class="w-full md:w-auto px-4 py-1.5 rounded-full font-heading text-[12px] font-bold text-[#1C6E8C] bg-[#FFFFFF] border border-[#1C6E8C] hover:bg-[#1C6E8C] hover:text-[#FFFFFF] shadow-sm transition-all" onClick={() => seleccionarEstacionYVer('Estación Las Palmas PL/12345/EXP/ES/2015')} type="button">Ver estación</button></div></div></div><div class="relative overflow-hidden rounded-2xl bg-[#FFFFFF] border border-[#0C2B3A]/10 hover:border-[#8A5A00]/40 shadow-sm hover:shadow-md transition-all"><div class="absolute left-0 top-0 bottom-0 w-1.5 bg-[#F2B705]"></div><div class="p-5 pl-7 grid grid-cols-1 md:grid-cols-12 gap-4 items-center"><div class="col-span-12 md:col-span-4 flex items-center gap-3.5"><div class="w-11 h-11 rounded-xl bg-[#8A5A00]/10 text-[#8A5A00] flex items-center justify-center flex-shrink-0 border border-[#8A5A00]/25 shadow-sm"><span class="material-symbols-outlined text-[24px]">propane_tank</span></div><div class="min-w-0"><div class="flex items-center gap-2"><h3 class="font-heading font-bold text-[16px] text-[#0C2B3A] truncate">Planta Gas El Roble</h3><span class="px-2 py-0.2 rounded-full font-mono-val text-[10px] bg-[#0C2B3A]/5 text-[#4A5F6B]">Sucursal 002</span></div><span class="text-[12px] text-[#4A5F6B] block truncate">Parque Industrial Zona 4</span></div></div><div class="col-span-6 md:col-span-2"><span class="font-mono-val text-[12px] font-semibold text-[#0C2B3A] bg-[#F4F6F7] border border-[#0C2B3A]/5 px-2.5 py-1 rounded-lg block truncate">G/33912/LPG/2019</span></div><div class="col-span-6 md:col-span-2 flex items-center gap-1.5 text-[13px] text-[#4A5F6B]"><span class="material-symbols-outlined text-[16px] text-[#8A5A00]">location_on</span><span class="">Guadalajara Jalisco</span></div><div class="col-span-6 md:col-span-2 space-y-1.5"><div class="flex items-center justify-between text-[12px]"><span class="font-mono-val font-semibold text-[#0C2B3A]">2 tanques</span><span class="font-mono-val text-[11px] text-[#4A5F6B]">45,000 L</span></div><div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden border border-[#0C2B3A]/5"><div class="h-full bg-[#F2B705] rounded-full" style="width: 62%;"></div></div></div><div class="col-span-3 md:col-span-1 text-left md:text-center"><span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full font-mono-val text-[11px] bg-[rgba(242,183,5,0.18)] text-[#8A5A00] font-bold"><span class="w-1.5 h-1.5 rounded-full bg-[#F2B705]"></span>Por vencer</span></div><div class="col-span-3 md:col-span-1 text-right"><button class="w-full md:w-auto px-4 py-1.5 rounded-full font-heading text-[12px] font-bold text-[#8A5A00] bg-[#FFFFFF] border border-[#8A5A00]/40 hover:bg-[#8A5A00] hover:text-[#FFFFFF] shadow-sm transition-all" onClick={() => seleccionarEstacionYVer('Planta Gas El Roble G/33912/LPG/2019')} type="button">Ver planta</button></div></div></div><div class="relative overflow-hidden rounded-2xl bg-[#FFFFFF] border border-[#0C2B3A]/10 hover:border-[#1C6E8C]/40 shadow-sm hover:shadow-md transition-all"><div class="absolute left-0 top-0 bottom-0 w-1.5 bg-[#1C6E8C]"></div><div class="p-5 pl-7 grid grid-cols-1 md:grid-cols-12 gap-4 items-center"><div class="col-span-12 md:col-span-4 flex items-center gap-3.5"><div class="w-11 h-11 rounded-xl bg-[#1C6E8C]/10 text-[#1C6E8C] flex items-center justify-center flex-shrink-0 border border-[#1C6E8C]/20 shadow-sm"><span class="material-symbols-outlined text-[24px]">local_gas_station</span></div><div class="min-w-0"><div class="flex items-center gap-2"><h3 class="font-heading font-bold text-[16px] text-[#0C2B3A] truncate">Servicentro Aeropuerto</h3><span class="px-2 py-0.2 rounded-full font-mono-val text-[10px] bg-[#0C2B3A]/5 text-[#4A5F6B]">Sucursal 003</span></div><span class="text-[12px] text-[#4A5F6B] block truncate">Boulevard Aeropuerto KM 4</span></div></div><div class="col-span-6 md:col-span-2"><span class="font-mono-val text-[12px] font-semibold text-[#0C2B3A] bg-[#F4F6F7] border border-[#0C2B3A]/5 px-2.5 py-1 rounded-lg block truncate">PL/19824/EXP/ES/2018</span></div><div class="col-span-6 md:col-span-2 flex items-center gap-1.5 text-[13px] text-[#4A5F6B]"><span class="material-symbols-outlined text-[16px] text-[#1C6E8C]">location_on</span><span class="">Monterrey Nuevo León</span></div><div class="col-span-6 md:col-span-2 space-y-1.5"><div class="flex items-center justify-between text-[12px]"><span class="font-mono-val font-semibold text-[#0C2B3A]">4 tanques</span><span class="font-mono-val text-[11px] text-[#4A5F6B]">92,000 L</span></div><div class="w-full h-2 rounded-full bg-[#F4F6F7] overflow-hidden border border-[#0C2B3A]/5"><div class="h-full bg-[#1C6E8C] rounded-full" style="width: 91%;"></div></div></div><div class="col-span-3 md:col-span-1 text-left md:text-center"><span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full font-mono-val text-[11px] bg-[#1C6E8C]/10 text-[#1C6E8C] font-bold"><span class="w-1.5 h-1.5 rounded-full bg-[#1C6E8C]"></span>Al día</span></div><div class="col-span-3 md:col-span-1 text-right"><button class="w-full md:w-auto px-4 py-1.5 rounded-full font-heading text-[12px] font-bold text-[#1C6E8C] bg-[#FFFFFF] border border-[#1C6E8C] hover:bg-[#1C6E8C] hover:text-[#FFFFFF] shadow-sm transition-all" onClick={() => seleccionarEstacionYVer('Servicentro Aeropuerto PL/19824/EXP/ES/2018')} type="button">Ver estación</button></div></div></div></div></div>
</div></div>
</main>
</div>
<!-- ============================================== -->
<!-- MODAL: CARGA DE REPORTE VOLUMÉTRICO MENSUAL    -->
<!-- ============================================== -->
<div class={`fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#0C2B3A]/60 backdrop-blur-sm ${isVolumetricModalOpen ? '' : 'hidden'}`} id="volumetricModal">
<div class="w-full max-w-lg rounded-[20px] bg-[#FFFFFF] p-6 shadow-2xl border border-[#0C2B3A]/10 space-y-5">
<div class="flex items-center justify-between border-b border-[#0C2B3A]/10 pb-3">
<div>
<span class="font-mono-val text-[11px] text-[#1C6E8C] font-bold uppercase tracking-wider">SAT Anexo 21 RMF</span>
<h3 class="font-heading text-[20px] font-bold text-[#0C2B3A]">Cargar Reporte Volumétrico Mensual</h3>
</div>
<button class="p-1.5 rounded-full text-[#4A5F6B] hover:bg-[#F4F6F7] transition-colors" onClick={() => closeVolumetricModal()} type="button">
<span class="material-symbols-outlined text-[20px]">close</span>
</button>
</div>
<div class="space-y-4">
<div>
<label class="block font-mono-val text-[11px] uppercase text-[#0C2B3A] font-bold mb-1.5">Archivo JSON o XML Certificado</label>
<div class="p-6 rounded-xl bg-[#F4F6F7] border-2 border-dashed border-[#1C6E8C]/30 flex flex-col items-center justify-center text-center cursor-pointer hover:border-[#1C6E8C] transition-colors">
<span class="material-symbols-outlined text-[#1C6E8C] text-[32px] mb-2">upload_file</span>
<p class="text-[13px] text-[#0C2B3A] font-bold">Selecciona el paquete de control volumétrico</p>
<span class="font-mono-val text-[11px] text-[#4A5F6B] mt-1">Estructura validada contra Esquema SAT 2026</span>
</div>
</div>
<div>
<label class="block font-mono-val text-[11px] uppercase text-[#0C2B3A] font-bold mb-1.5">Periodo de reporte</label>
<div class="h-10 px-3.5 rounded-xl bg-[#F4F6F7] border border-[#0C2B3A]/10 flex items-center justify-between text-[13px] text-[#0C2B3A] font-mono-val font-semibold">
<span class="">Marzo 2026</span>
<span class="material-symbols-outlined text-[18px] text-[#4A5F6B]">calendar_today</span>
</div>
</div>
</div>
<div class="flex items-center justify-end gap-3 pt-3 border-t border-[#0C2B3A]/10">
<button class="px-5 py-2 rounded-full font-heading text-[13px] font-bold text-[#4A5F6B] hover:bg-[#F4F6F7] transition-colors" onClick={() => closeVolumetricModal()} type="button">
          Cancelar
        </button>
<button class="px-6 py-2 rounded-full font-heading text-[13px] font-bold bg-[#1C6E8C] hover:bg-[#154F66] text-[#FFFFFF] shadow-sm transition-all" onClick={() => submitVolumetric()} type="button">
          Transmitir al SAT
        </button>
</div>
</div>
</div>
<!-- ============================================== -->
<!-- MODAL: GESTIÓN DE RENOVACIÓN NOM-005           -->
<!-- ============================================== -->
<div class={`fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#0C2B3A]/60 backdrop-blur-sm ${isRenovacionModalOpen ? '' : 'hidden'}`} id="renovacionModal">
<div class="w-full max-w-lg rounded-[20px] bg-[#FFFFFF] p-6 shadow-2xl border border-[#0C2B3A]/10 space-y-5">
<div class="flex items-center justify-between border-b border-[#0C2B3A]/10 pb-3">
<div>
<span class="font-mono-val text-[11px] text-[#8A5A00] font-bold uppercase tracking-wider">NOM-005-ASEA</span>
<h3 class="font-heading text-[20px] font-bold text-[#0C2B3A]">Renovación Dictamen de Hermeticidad</h3>
</div>
<button class="p-1.5 rounded-full text-[#4A5F6B] hover:bg-[#F4F6F7] transition-colors" onClick={() => closeRenovacionModal()} type="button">
<span class="material-symbols-outlined text-[20px]">close</span>
</button>
</div>
<p class="text-[13px] text-[#4A5F6B]">
        El dictamen actual vence en 30 días. Para mantener la estación en estatus verde y evitar sellos de suspensión preventiva de la CRE asigna la unidad verificadora correspondiente.
      </p>
<div class="p-4 rounded-xl bg-[#F4F6F7] space-y-2 border border-[#0C2B3A]/5">
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Fecha límite de vencimiento</span>
<span class="font-mono-val font-bold text-[#8A5A00]">30-abr-2026</span>
</div>
<div class="flex justify-between items-center text-[12px]">
<span class="text-[#4A5F6B]">Tanques sujetos a prueba</span>
<span class="font-mono-val text-[#0C2B3A] font-bold">3 unidades Magna Premium Diésel</span>
</div>
</div>
<div class="flex items-center justify-end gap-3 pt-3 border-t border-[#0C2B3A]/10">
<button class="px-5 py-2 rounded-full font-heading text-[13px] font-bold text-[#4A5F6B] hover:bg-[#F4F6F7] transition-colors" onClick={() => closeRenovacionModal()} type="button">
          Cerrar
        </button>
<button class="px-6 py-2 rounded-full font-heading text-[13px] font-bold bg-[#1C6E8C] hover:bg-[#154F66] text-[#FFFFFF] shadow-sm transition-all" onClick={() => confirmRenovacion()} type="button">
          Solicitar Inspector UV
        </button>
</div>
</div>
</div>
<!-- TOAST FLOTANTE DE NOTIFICACIÓN -->
<div class={`fixed bottom-6 right-6 z-50 px-4 py-3 rounded-xl bg-[#0C2B3A] text-[#FFFFFF] shadow-2xl flex items-center gap-3 border border-[#4FB3D9]/30 transition-all ${toastMessage ? '' : 'hidden'}`} id="toastNotification">
<span class="material-symbols-outlined text-[#4FB3D9] text-[20px]">check_circle</span>
<span class="text-[13px] font-medium" id="toastMsg">{toastMessage}</span>
</div>
"""

# Replace all class="..." with className="..."
html_content = re.sub(r'class="([^"]*)"', r'className="\1"', html_content)
html_content = html_content.replace('class=', 'className=')
# Fix img tags without closing /
html_content = re.sub(r'(<img[^>]+)(?<!/)>', r'\1 />', html_content)
# Fix input tags without closing /
html_content = re.sub(r'(<input[^>]+)(?<!/)>', r'\1 />', html_content)

full_react_code = f"""import React, {{ useState, useEffect }} from 'react';

export default function App() {{
  const [currentView, setCurrentView] = useState('instalaciones');
  const [isStationMenuOpen, setIsStationMenuOpen] = useState(false);
  const [activeStation, setActiveStation] = useState('Servicentro Aeropuerto PL/98765/EXP/ES/2018');
  const [timelineFilter, setTimelineFilter] = useState('all');
  const [isVolumetricModalOpen, setIsVolumetricModalOpen] = useState(false);
  const [isRenovacionModalOpen, setIsRenovacionModalOpen] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [isAlertVisible, setIsAlertVisible] = useState(true);

  const showToast = (message) => {{
    setToastMessage(message);
    setTimeout(() => setToastMessage(''), 3500);
  }};

  const navigateTo = (viewName) => {{
    setCurrentView(viewName);
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }};

  const toggleStationMenu = () => {{
    setIsStationMenuOpen(!isStationMenuOpen);
  }};

  const setStation = (stationName) => {{
    setActiveStation(stationName);
    setIsStationMenuOpen(false);
    showToast('Estación activa cambiada a ' + stationName);
  }};

  const seleccionarEstacionYVer = (stationName) => {{
    setStation(stationName);
    navigateTo('dashboard');
  }};

  const filterTimeline = (category) => {{
    setTimelineFilter(category);
  }};

  const openVolumetricModal = () => setIsVolumetricModalOpen(true);
  const closeVolumetricModal = () => setIsVolumetricModalOpen(false);
  const submitVolumetric = () => {{
    closeVolumetricModal();
    showToast('Reporte volumétrico validado y transmitido al SAT con éxito');
  }};

  const openRenovacionModal = () => setIsRenovacionModalOpen(true);
  const closeRenovacionModal = () => setIsRenovacionModalOpen(false);
  const confirmRenovacion = () => {{
    closeRenovacionModal();
    showToast('Solicitud enviada a la Unidad Verificadora UV-ASEA-044');
  }};

  const previewDocument = (docName) => {{
    showToast('Abriendo visor criptográfico para ' + docName);
  }};

  const handleDrop = (e) => {{
    e.preventDefault();
    e.currentTarget.classList.remove('border-[#1C6E8C]', 'bg-[#1C6E8C]/5');
    showToast('Archivo recibido y firmado criptográficamente');
  }};

  const navButtonClasses = (isActive) =>
    isActive
      ? "w-full flex items-center justify-between px-3 py-2.5 rounded-xl transition-all bg-[#4FB3D9]/15 text-[#4FB3D9] font-medium text-[14px] text-left group"
      : "w-full flex items-center justify-between px-3 py-2.5 rounded-xl transition-all text-[#F1F5F7]/80 hover:bg-[#FFFFFF]/5 hover:text-[#FFFFFF] text-[14px] text-left group";

  return (
    <>
      {html_content}
    </>
  );
}}
"""

with open(r'c:\SuelvoSasi\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(full_react_code)

print("Done")
