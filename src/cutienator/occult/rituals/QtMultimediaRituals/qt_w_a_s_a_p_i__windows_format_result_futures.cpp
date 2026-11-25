//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevice_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsaudiodevice_p.h>

//  QtWASAPI::WindowsFormatResultFutures::~WindowsFormatResultFutures()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtWASAPI26WindowsFormatResultFuturesD1Ev(
    QtWASAPI::WindowsFormatResultFutures *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
