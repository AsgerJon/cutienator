//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfiledevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>

//  const QMetaObject *QFileDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFileDevice10metaObjectEv(
    const QFileDevice *self) {
  return self->metaObject();
}

//  QString QFileDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileDevice::tr(s, c, n));
}

//  QFileDevice::~QFileDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDeviceD1Ev(QFileDevice *self) {
  delete self;
}

//  FileError QFileDevice::error() const
extern "C" Q_DECL_EXPORT
QFileDevice::FileError ritual_ZNK11QFileDevice5errorEv(
    const QFileDevice *self) {
  return self->error();
}

//  void QFileDevice::unsetError()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDevice10unsetErrorEv(QFileDevice *self) {
  self->unsetError();
}

//  void QFileDevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDevice5closeEv(QFileDevice *self) {
  self->close();
}

//  bool QFileDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDevice12isSequentialEv(const QFileDevice *self) {
  return self->isSequential();
}

//  int QFileDevice::handle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDevice6handleEv(const QFileDevice *self) {
  return self->handle();
}

//  QString QFileDevice::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDevice8fileNameEv(const QFileDevice *self) {
  return new QString(self->fileName());
}

//  qint64 QFileDevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QFileDevice3posEv(const QFileDevice *self) {
  return self->pos();
}

//  bool QFileDevice::seek(qint64 offset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice4seekEx(QFileDevice *self, qint64 offset) {
  return self->seek(offset);
}

//  bool QFileDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDevice5atEndEv(const QFileDevice *self) {
  return self->atEnd();
}

//  bool QFileDevice::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice5flushEv(QFileDevice *self) {
  return self->flush();
}

//  qint64 QFileDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QFileDevice4sizeEv(const QFileDevice *self) {
  return self->size();
}

//  bool QFileDevice::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice6resizeEx(QFileDevice *self, qint64 sz) {
  return self->resize(sz);
}

//  Permissions QFileDevice::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDevice11permissionsEv(const QFileDevice *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  bool QFileDevice::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE(
    QFileDevice *self,
    int permissionSpec) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  bool QFileDevice::unmap(uchar *address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice5unmapEPh(QFileDevice *self, uchar *address) {
  return self->unmap(address);
}

//  QDateTime QFileDevice::fileTime(QFileDevice::FileTime time) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QFileDevice8fileTimeENS_8FileTimeE(
    const QFileDevice *self,
    QFileDevice::FileTime time) {
  return new QDateTime(self->fileTime(time));
}

//  bool QFileDevice::setFileTime(const QDateTime &newDate,
//      QFileDevice::FileTime fileTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice11setFileTimeERK9QDateTimeNS_8FileTimeE(
    QFileDevice *self,
    const QDateTime *newDate,
    QFileDevice::FileTime fileTime) {
  return self->setFileTime(*newDate, fileTime);
}
