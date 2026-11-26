//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsymbolsresolveutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if (defined(Q_OS_LINUX) || defined(Q_OS_ANDROID)) && QT_CONFIG(library)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsymbolsresolveutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool SymbolsResolver::isLazyLoadEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15SymbolsResolver17isLazyLoadEnabledEv() {
  return SymbolsResolver::isLazyLoadEnabled();
}

//  bool SymbolsResolver::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15SymbolsResolver8isLoadedEv(const SymbolsResolver *self) {
  return self->isLoaded();
}

//  SymbolsResolver::~SymbolsResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SymbolsResolverD1Ev(SymbolsResolver *self) {
  delete self;
}

//  SymbolsResolver::SymbolsResolver(const char *libLoggingName,
//      LibraryLoader loader)
extern "C" Q_DECL_EXPORT
SymbolsResolver *ritual_ZN15SymbolsResolverC1EPKcPFSt10unique_ptrI8QLibrarySt14default_deleteIS3_EEvE(
    const char *libLoggingName,
    void *loader) {
  return new SymbolsResolver(
      libLoggingName,
      reinterpret_cast<SymbolsResolver::LibraryLoader>(loader));
}

//  SymbolsResolver::SymbolsResolver(const char *libName, const char
//      *version, const char *libLoggingName)
extern "C" Q_DECL_EXPORT
SymbolsResolver *ritual_ZN15SymbolsResolverC1EPKcS1_S1_(
    const char *libName,
    const char *version,
    const char *libLoggingName) {
  return new SymbolsResolver(libName, version, libLoggingName);
}

//  QFunctionPointer SymbolsResolver::initOptionalFunction(const char *name)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15SymbolsResolver20initOptionalFunctionEPKc(
    SymbolsResolver *self,
    const char *name) {
  return reinterpret_cast<void *>(self->initOptionalFunction(name));
}

//  QFunctionPointer SymbolsResolver::initFunction(const char *name)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15SymbolsResolver12initFunctionEPKc(
    SymbolsResolver *self,
    const char *name) {
  return reinterpret_cast<void *>(self->initFunction(name));
}

//  void SymbolsResolver::checkLibrariesLoaded(SymbolsMarker *begin,
//      SymbolsMarker *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SymbolsResolver20checkLibrariesLoadedEPNS_13SymbolsMarkerES1_(
    SymbolsResolver *self,
    SymbolsResolver::SymbolsMarker *begin,
    SymbolsResolver::SymbolsMarker *end) {
  self->checkLibrariesLoaded(begin, end);
}

#endif  // (defined(Q_OS_LINUX) || defined(Q_OS_ANDROID)) && QT_CONFIG(library)
