//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qapple_utils_p.h, Qt 6.12.0, as
//  the Qt of macOS installs it. Kept as it is when the generator runs again.
//  An 'OSStatus' is passed as an 'int'. Not written: the templates
//  'CFArrayIterator' and 'CFArrayRange' of the same header.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qapple_utils_p.h>
#include <QtCore/qdebug.h>

//  QtMultimediaPrivate::QOSStatus::QOSStatus(OSStatus s)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QOSStatus *ritual_ZN19QtMultimediaPrivate9QOSStatusC1Ei(
    OSStatus s) {
  return new QtMultimediaPrivate::QOSStatus(s);
}

//  QtMultimediaPrivate::QOSStatus::~QOSStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate9QOSStatusD1Ev(
    QtMultimediaPrivate::QOSStatus *self) {
  delete self;
}

//  QDebug QtMultimediaPrivate::operator<<(QDebug dbg, const
//      QtMultimediaPrivate::QOSStatus &qos)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN19QtMultimediaPrivatelsE6QDebugRKNS_9QOSStatusE(
    const QDebug *dbg,
    const QtMultimediaPrivate::QOSStatus *qos) {
  return new QDebug(operator<<(*dbg, *qos));
}

#endif  // defined(Q_OS_DARWIN)
