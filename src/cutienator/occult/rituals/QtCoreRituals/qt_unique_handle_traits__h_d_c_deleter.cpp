//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/quniquehandle_types_windows_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. A handle of Windows, as 'HDC' or 'HWND', is
//  passed as an address.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/quniquehandle_types_windows_p.h>

//  QtUniqueHandleTraits::HDCDeleter::HDCDeleter()
extern "C" Q_DECL_EXPORT
QtUniqueHandleTraits::HDCDeleter *ritual_ZN20QtUniqueHandleTraits10HDCDeleterC1Ev() {
  return new QtUniqueHandleTraits::HDCDeleter();
}

//  QtUniqueHandleTraits::HDCDeleter::HDCDeleter(HWND hwnd)
extern "C" Q_DECL_EXPORT
QtUniqueHandleTraits::HDCDeleter *ritual_ZN20QtUniqueHandleTraits10HDCDeleterC1EP6HWND__(
    HWND hwnd) {
  return new QtUniqueHandleTraits::HDCDeleter(hwnd);
}

//  void QtUniqueHandleTraits::HDCDeleter::operator()(Type handle) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QtUniqueHandleTraits10HDCDeleterclEP5HDC__(
    const QtUniqueHandleTraits::HDCDeleter *self,
    HDC handle) {
  self->operator()(handle);
}

//  QtUniqueHandleTraits::HDCDeleter::~HDCDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QtUniqueHandleTraits10HDCDeleterD1Ev(
    QtUniqueHandleTraits::HDCDeleter *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
