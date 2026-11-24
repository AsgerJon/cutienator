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

//  SymbolsResolver::SymbolsResolver(const char *libName, const char
//      *version, const char *libLoggingName)
extern "C" Q_DECL_EXPORT
SymbolsResolver *ritual_ZN15SymbolsResolverC1EPKcS1_S1_(
    const char *libName,
    const char *version,
    const char *libLoggingName) {
  return new SymbolsResolver(libName, version, libLoggingName);
}

#endif  // (defined(Q_OS_LINUX) || defined(Q_OS_ANDROID)) && QT_CONFIG(library)
