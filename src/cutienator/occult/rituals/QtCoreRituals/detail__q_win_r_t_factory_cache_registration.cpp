//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qfactorycacheregistration_p.h, Qt 6.12.0,
//  as the Qt of Windows installs it. Kept as it is when the generator
//  runs again. Its header declares the class only where Qt is built
//  with C++/WinRT ('QT_CONFIG(cpp_winrt)'). A 'QFunctionPointer' is
//  passed as an address.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN) && !defined(QT_BOOTSTRAPPED) && QT_CONFIG(cpp_winrt)
#include <QtCore/6.12.0/QtCore/private/qfactorycacheregistration_p.h>

//  detail::QWinRTFactoryCacheRegistration::QWinRTFactoryCacheRegistration(
//      QFunctionPointer clearFunction)
extern "C" Q_DECL_EXPORT
detail::QWinRTFactoryCacheRegistration *ritual_ZN6detail30QWinRTFactoryCacheRegistrationC1EPFvvE(
    QFunctionPointer clearFunction) {
  return new detail::QWinRTFactoryCacheRegistration(clearFunction);
}

//  detail::QWinRTFactoryCacheRegistration::~QWinRTFactoryCacheRegistration()
extern "C" Q_DECL_EXPORT
void ritual_ZN6detail30QWinRTFactoryCacheRegistrationD1Ev(
    detail::QWinRTFactoryCacheRegistration *self) {
  delete self;
}

//  void detail::QWinRTFactoryCacheRegistration::clearAllCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN6detail30QWinRTFactoryCacheRegistration14clearAllCachesEv() {
  detail::QWinRTFactoryCacheRegistration::clearAllCaches();
}

#endif  // defined(Q_OS_WIN) && !defined(QT_BOOTSTRAPPED) && QT_CONFIG(cpp_winrt)
