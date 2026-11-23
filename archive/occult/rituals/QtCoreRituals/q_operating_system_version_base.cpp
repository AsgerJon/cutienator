//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qoperatingsystemversion.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>

//  QOperatingSystemVersionBase::QOperatingSystemVersionBase(OSType osType,
//      int vmajor, int vminor, int vmicro)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionBase *ritual_ZN27QOperatingSystemVersionBaseC1ENS_6OSTypeEiii(
    QOperatingSystemVersionBase::OSType osType,
    int vmajor,
    int vminor,
    int vmicro) {
  return new QOperatingSystemVersionBase(osType, vmajor, vminor, vmicro);
}

//  QOperatingSystemVersionBase QOperatingSystemVersionBase::current()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionBase *ritual_ZN27QOperatingSystemVersionBase7currentEv() {
  return new QOperatingSystemVersionBase(
      QOperatingSystemVersionBase::current());
}

//  QString QOperatingSystemVersionBase::name(QOperatingSystemVersionBase
//      osversion)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QOperatingSystemVersionBase4nameES_(
    const QOperatingSystemVersionBase *osversion) {
  return new QString(QOperatingSystemVersionBase::name(*osversion));
}

//  OSType QOperatingSystemVersionBase::currentType()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionBase::OSType ritual_ZN27QOperatingSystemVersionBase11currentTypeEv() {
  return QOperatingSystemVersionBase::currentType();
}

//  QVersionNumber QOperatingSystemVersionBase::version() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK27QOperatingSystemVersionBase7versionEv(
    const QOperatingSystemVersionBase *self) {
  return new QVersionNumber(self->version());
}

//  int QOperatingSystemVersionBase::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOperatingSystemVersionBase12majorVersionEv(
    const QOperatingSystemVersionBase *self) {
  return self->majorVersion();
}

//  int QOperatingSystemVersionBase::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOperatingSystemVersionBase12minorVersionEv(
    const QOperatingSystemVersionBase *self) {
  return self->minorVersion();
}

//  int QOperatingSystemVersionBase::microVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOperatingSystemVersionBase12microVersionEv(
    const QOperatingSystemVersionBase *self) {
  return self->microVersion();
}

//  int QOperatingSystemVersionBase::segmentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOperatingSystemVersionBase12segmentCountEv(
    const QOperatingSystemVersionBase *self) {
  return self->segmentCount();
}

//  OSType QOperatingSystemVersionBase::type() const
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionBase::OSType ritual_ZNK27QOperatingSystemVersionBase4typeEv(
    const QOperatingSystemVersionBase *self) {
  return self->type();
}

//  QString QOperatingSystemVersionBase::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QOperatingSystemVersionBase4nameEv(
    const QOperatingSystemVersionBase *self) {
  return new QString(self->name());
}

//  int QOperatingSystemVersionBase::compare(QOperatingSystemVersionBase v1,
//      QOperatingSystemVersionBase v2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QOperatingSystemVersionBase7compareES_S_(
    const QOperatingSystemVersionBase *v1,
    const QOperatingSystemVersionBase *v2) {
  return QOperatingSystemVersionBase::compare(*v1, *v2);
}

//  bool operator>(QOperatingSystemVersionBase lhs,
//      QOperatingSystemVersionBase rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zgt27QOperatingSystemVersionBaseS_(
    const QOperatingSystemVersionBase *lhs,
    const QOperatingSystemVersionBase *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator>=(QOperatingSystemVersionBase lhs,
//      QOperatingSystemVersionBase rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zge27QOperatingSystemVersionBaseS_(
    const QOperatingSystemVersionBase *lhs,
    const QOperatingSystemVersionBase *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator<(QOperatingSystemVersionBase lhs,
//      QOperatingSystemVersionBase rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zlt27QOperatingSystemVersionBaseS_(
    const QOperatingSystemVersionBase *lhs,
    const QOperatingSystemVersionBase *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator<=(QOperatingSystemVersionBase lhs,
//      QOperatingSystemVersionBase rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zle27QOperatingSystemVersionBaseS_(
    const QOperatingSystemVersionBase *lhs,
    const QOperatingSystemVersionBase *rhs) {
  return operator<=(*lhs, *rhs);
}

//  QOperatingSystemVersionBase::QOperatingSystemVersionBase()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionBase *ritual_ZN27QOperatingSystemVersionBaseC1Ev() {
  return new QOperatingSystemVersionBase();
}

//  QOperatingSystemVersionBase::~QOperatingSystemVersionBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOperatingSystemVersionBaseD1Ev(
    QOperatingSystemVersionBase *self) {
  delete self;
}
