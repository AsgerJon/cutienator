//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsmediafoundation_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  A 'QWindowsMediaFoundation *' is passed as an address. Of
//  QWindowsMediaFoundation, in the same header, nothing is written: Qt's
//  library offers nothing of it by name, and its header writes out nothing
//  of it.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsmediafoundation_p.h>

//  QMFRuntimeInit::QMFRuntimeInit()
extern "C" Q_DECL_EXPORT
QMFRuntimeInit *ritual_ZN14QMFRuntimeInitC1Ev() {
  return new QMFRuntimeInit();
}

//  QMFRuntimeInit::QMFRuntimeInit(QWindowsMediaFoundation *wmf)
extern "C" Q_DECL_EXPORT
QMFRuntimeInit *ritual_ZN14QMFRuntimeInitC1EP23QWindowsMediaFoundation(
    QWindowsMediaFoundation *wmf) {
  return new QMFRuntimeInit(wmf);
}

//  QMFRuntimeInit::~QMFRuntimeInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMFRuntimeInitD1Ev(QMFRuntimeInit *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
