//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstorageinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstorageinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qbytearray.h>

//  QStorageInfo::QStorageInfo()
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN12QStorageInfoC1Ev() {
  return new QStorageInfo();
}

//  QStorageInfo::QStorageInfo(const QString &path)
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN12QStorageInfoC1ERK7QString(const QString *path) {
  return new QStorageInfo(*path);
}

//  QStorageInfo::QStorageInfo(const QDir &dir)
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN12QStorageInfoC1ERK4QDir(const QDir *dir) {
  return new QStorageInfo(*dir);
}

//  QStorageInfo::QStorageInfo(const QStorageInfo &other)
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN12QStorageInfoC1ERKS_(const QStorageInfo *other) {
  return new QStorageInfo(*other);
}

//  QStorageInfo::~QStorageInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStorageInfoD1Ev(QStorageInfo *self) {
  delete self;
}

//  void QStorageInfo::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStorageInfo7setPathERK7QString(
    QStorageInfo *self,
    const QString *path) {
  self->setPath(*path);
}

//  QString QStorageInfo::rootPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QStorageInfo8rootPathEv(const QStorageInfo *self) {
  return new QString(self->rootPath());
}

//  QByteArray QStorageInfo::device() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QStorageInfo6deviceEv(const QStorageInfo *self) {
  return new QByteArray(self->device());
}

//  QByteArray QStorageInfo::subvolume() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QStorageInfo9subvolumeEv(const QStorageInfo *self) {
  return new QByteArray(self->subvolume());
}

//  QByteArray QStorageInfo::fileSystemType() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QStorageInfo14fileSystemTypeEv(
    const QStorageInfo *self) {
  return new QByteArray(self->fileSystemType());
}

//  QString QStorageInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QStorageInfo4nameEv(const QStorageInfo *self) {
  return new QString(self->name());
}

//  QString QStorageInfo::displayName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QStorageInfo11displayNameEv(const QStorageInfo *self) {
  return new QString(self->displayName());
}

//  qint64 QStorageInfo::bytesTotal() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QStorageInfo10bytesTotalEv(const QStorageInfo *self) {
  return self->bytesTotal();
}

//  qint64 QStorageInfo::bytesFree() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QStorageInfo9bytesFreeEv(const QStorageInfo *self) {
  return self->bytesFree();
}

//  qint64 QStorageInfo::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QStorageInfo14bytesAvailableEv(const QStorageInfo *self) {
  return self->bytesAvailable();
}

//  int QStorageInfo::blockSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QStorageInfo9blockSizeEv(const QStorageInfo *self) {
  return self->blockSize();
}

//  bool QStorageInfo::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QStorageInfo6isRootEv(const QStorageInfo *self) {
  return self->isRoot();
}

//  bool QStorageInfo::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QStorageInfo10isReadOnlyEv(const QStorageInfo *self) {
  return self->isReadOnly();
}

//  bool QStorageInfo::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QStorageInfo7isReadyEv(const QStorageInfo *self) {
  return self->isReady();
}

//  bool QStorageInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QStorageInfo7isValidEv(const QStorageInfo *self) {
  return self->isValid();
}

//  void QStorageInfo::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStorageInfo7refreshEv(QStorageInfo *self) {
  self->refresh();
}

//  QStorageInfo QStorageInfo::root()
extern "C" Q_DECL_EXPORT
QStorageInfo *ritual_ZN12QStorageInfo4rootEv() {
  return new QStorageInfo(QStorageInfo::root());
}
