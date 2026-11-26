//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qzipwriter_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qzipwriter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QFile>

//  QZipWriter::QZipWriter(const QString &fileName, QIODevice::OpenMode mode)
extern "C" Q_DECL_EXPORT
QZipWriter *ritual_ZN10QZipWriterC1ERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    const QString *fileName,
    int mode) {
  return new QZipWriter(
      *fileName,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QZipWriter::QZipWriter(QIODevice *device)
extern "C" Q_DECL_EXPORT
QZipWriter *ritual_ZN10QZipWriterC1EP9QIODevice(QIODevice *device) {
  return new QZipWriter(device);
}

//  QZipWriter::~QZipWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriterD1Ev(QZipWriter *self) {
  delete self;
}

//  QIODevice *QZipWriter::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK10QZipWriter6deviceEv(const QZipWriter *self) {
  return self->device();
}

//  bool QZipWriter::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipWriter10isWritableEv(const QZipWriter *self) {
  return self->isWritable();
}

//  bool QZipWriter::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipWriter6existsEv(const QZipWriter *self) {
  return self->exists();
}

//  Status QZipWriter::status() const
extern "C" Q_DECL_EXPORT
QZipWriter::Status ritual_ZNK10QZipWriter6statusEv(const QZipWriter *self) {
  return self->status();
}

//  void QZipWriter::setCompressionPolicy(CompressionPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter20setCompressionPolicyENS_17CompressionPolicyE(
    QZipWriter *self,
    QZipWriter::CompressionPolicy policy) {
  self->setCompressionPolicy(policy);
}

//  CompressionPolicy QZipWriter::compressionPolicy() const
extern "C" Q_DECL_EXPORT
QZipWriter::CompressionPolicy ritual_ZNK10QZipWriter17compressionPolicyEv(
    const QZipWriter *self) {
  return self->compressionPolicy();
}

//  void QZipWriter::setCreationPermissions(QFile::Permissions permissions)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter22setCreationPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QZipWriter *self,
    int permissions) {
  self->setCreationPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  QFile::Permissions QZipWriter::creationPermissions() const
extern "C" Q_DECL_EXPORT
QFile::Permissions *ritual_ZNK10QZipWriter19creationPermissionsEv(
    const QZipWriter *self) {
  return new QFile::Permissions(self->creationPermissions());
}

//  void QZipWriter::addFile(const QString &fileName, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter7addFileERK7QStringRK10QByteArray(
    QZipWriter *self,
    const QString *fileName,
    const QByteArray *data) {
  self->addFile(*fileName, *data);
}

//  void QZipWriter::addFile(const QString &fileName, QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter7addFileERK7QStringP9QIODevice(
    QZipWriter *self,
    const QString *fileName,
    QIODevice *device) {
  self->addFile(*fileName, device);
}

//  void QZipWriter::addDirectory(const QString &dirName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter12addDirectoryERK7QString(
    QZipWriter *self,
    const QString *dirName) {
  self->addDirectory(*dirName);
}

//  void QZipWriter::addSymLink(const QString &fileName, const QString
//      &destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter10addSymLinkERK7QStringS2_(
    QZipWriter *self,
    const QString *fileName,
    const QString *destination) {
  self->addSymLink(*fileName, *destination);
}

//  void QZipWriter::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipWriter5closeEv(QZipWriter *self) {
  self->close();
}

//  a QFile::Permissions a ritual of QZipWriter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QZipWriter__QFile_Permissions(QFile::Permissions *self) {
  delete self;
}
