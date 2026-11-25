//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/quniquehandle_types_windows_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. A handle of Windows, as 'HDC' or 'HWND', is
//  passed as an address.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/quniquehandle_types_windows_p.h>

//  Type QtUniqueHandleTraits::HDCTraits::invalidValue()
extern "C" Q_DECL_EXPORT
HDC ritual_ZN20QtUniqueHandleTraits9HDCTraits12invalidValueEv() {
  return QtUniqueHandleTraits::HDCTraits::invalidValue();
}

//  bool QtUniqueHandleTraits::HDCTraits::close(Type handle, HWND hwnd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QtUniqueHandleTraits9HDCTraits5closeEP5HDC__P6HWND__(
    HDC handle,
    HWND hwnd) {
  return QtUniqueHandleTraits::HDCTraits::close(handle, hwnd);
}

//  QtUniqueHandleTraits::HDCTraits::~HDCTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QtUniqueHandleTraits9HDCTraitsD1Ev(
    QtUniqueHandleTraits::HDCTraits *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
