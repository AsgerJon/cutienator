//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED) && !defined(Q_QDOC)
#include <QtCore/qoperatingsystemversion.h>

//  QOperatingSystemVersion::QOperatingSystemVersion(const
//      QOperatingSystemVersionBase &osversion)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN23QOperatingSystemVersionC1ERK27QOperatingSystemVersionBase(
    const QOperatingSystemVersionBase *osversion) {
  return new QOperatingSystemVersion(*osversion);
}

//  QOperatingSystemVersion::QOperatingSystemVersion(OSType osType, int
//      vmajor, int vminor, int vmicro)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN23QOperatingSystemVersionC1ENS_6OSTypeEiii(
    QOperatingSystemVersion::OSType osType,
    int vmajor,
    int vminor,
    int vmicro) {
  return new QOperatingSystemVersion(osType, vmajor, vminor, vmicro);
}

//  QOperatingSystemVersion QOperatingSystemVersion::current()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN23QOperatingSystemVersion7currentEv() {
  return new QOperatingSystemVersion(QOperatingSystemVersion::current());
}

//  OSType QOperatingSystemVersion::currentType()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion::OSType ritual_ZN23QOperatingSystemVersion11currentTypeEv() {
  return QOperatingSystemVersion::currentType();
}

//  OSType QOperatingSystemVersion::type() const
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion::OSType ritual_ZNK23QOperatingSystemVersion4typeEv(
    const QOperatingSystemVersion *self) {
  return self->type();
}

//  QOperatingSystemVersion::QOperatingSystemVersion()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN23QOperatingSystemVersionC1Ev() {
  return new QOperatingSystemVersion();
}

//  QOperatingSystemVersion::~QOperatingSystemVersion()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOperatingSystemVersionD1Ev(QOperatingSystemVersion *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED) && !defined(Q_QDOC)
