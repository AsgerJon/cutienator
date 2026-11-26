//  Written by hand on 2026-11-26 from
//  QtCore/6.12.0/QtCore/private/qfactorycacheregistration_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again. Qt declares the class only where it is built with C++/WinRT
//  ('QT_CONFIG(cpp_winrt)'), on Windows; Qt's library offers its
//  functions. Compiled by C++20, as the next line asks 'Summon': the
//  header pulls in Qt's C++/WinRT headers, which wait with coroutines,
//  which 'clang++' has only from C++20 on. The function handed to the
//  constructor crosses as its address.
//  Summon: -std=c++20
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
#include <QtCore/6.12.0/QtCore/private/qfactorycacheregistration_p.h>
#ifdef QT_USE_FACTORY_CACHE_REGISTRATION

//  detail::QWinRTFactoryCacheRegistration::QWinRTFactoryCacheRegistration(
//      QFunctionPointer clearFunction)
extern "C" Q_DECL_EXPORT
detail::QWinRTFactoryCacheRegistration *ritual_ZN6detail30QWinRTFactoryCacheRegistrationC1EPFvvE(
    void *clearFunction) {
  return new detail::QWinRTFactoryCacheRegistration(
      reinterpret_cast<QFunctionPointer>(clearFunction));
}

//  detail::QWinRTFactoryCacheRegistration::~QWinRTFactoryCacheRegistration()
extern "C" Q_DECL_EXPORT
void ritual_ZN6detail30QWinRTFactoryCacheRegistrationD1Ev(
    detail::QWinRTFactoryCacheRegistration *self) {
  delete self;
}

//  static void detail::QWinRTFactoryCacheRegistration::clearAllCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN6detail30QWinRTFactoryCacheRegistration14clearAllCachesEv() {
  detail::QWinRTFactoryCacheRegistration::clearAllCaches();
}

#endif  // QT_USE_FACTORY_CACHE_REGISTRATION
#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
