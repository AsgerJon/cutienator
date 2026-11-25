//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h, Qt 6.12.0,
//  as the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  Not written: the template 'operator()'.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h>

//  QCoreAudioUtils::QFreeDeleter::~QFreeDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoreAudioUtils12QFreeDeleterD1Ev(
    QCoreAudioUtils::QFreeDeleter *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
