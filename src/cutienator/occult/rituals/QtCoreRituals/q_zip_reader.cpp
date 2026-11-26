//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qzipreader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qzipreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QList>

//  QZipReader::QZipReader(const QString &fileName, QIODevice::OpenMode mode)
extern "C" Q_DECL_EXPORT
QZipReader *ritual_ZN10QZipReaderC1ERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    const QString *fileName,
    int mode) {
  return new QZipReader(
      *fileName,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QZipReader::QZipReader(QIODevice *device)
extern "C" Q_DECL_EXPORT
QZipReader *ritual_ZN10QZipReaderC1EP9QIODevice(QIODevice *device) {
  return new QZipReader(device);
}

//  QZipReader::~QZipReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipReaderD1Ev(QZipReader *self) {
  delete self;
}

//  QIODevice *QZipReader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK10QZipReader6deviceEv(const QZipReader *self) {
  return self->device();
}

//  bool QZipReader::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipReader10isReadableEv(const QZipReader *self) {
  return self->isReadable();
}

//  bool QZipReader::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipReader6existsEv(const QZipReader *self) {
  return self->exists();
}

//  QList<FileInfo> QZipReader::fileInfoList() const
extern "C" Q_DECL_EXPORT
QList<QZipReader::FileInfo> *ritual_ZNK10QZipReader12fileInfoListEv(
    const QZipReader *self) {
  return new QList<QZipReader::FileInfo>(self->fileInfoList());
}

//  int QZipReader::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QZipReader5countEv(const QZipReader *self) {
  return self->count();
}

//  FileInfo QZipReader::entryInfoAt(int index) const
extern "C" Q_DECL_EXPORT
QZipReader::FileInfo *ritual_ZNK10QZipReader11entryInfoAtEi(
    const QZipReader *self,
    int index) {
  return new QZipReader::FileInfo(self->entryInfoAt(index));
}

//  QByteArray QZipReader::fileData(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QZipReader8fileDataERK7QString(
    const QZipReader *self,
    const QString *fileName) {
  return new QByteArray(self->fileData(*fileName));
}

//  bool QZipReader::extractAll(const QString &destinationDir) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QZipReader10extractAllERK7QString(
    const QZipReader *self,
    const QString *destinationDir) {
  return self->extractAll(*destinationDir);
}

//  Status QZipReader::status() const
extern "C" Q_DECL_EXPORT
QZipReader::Status ritual_ZNK10QZipReader6statusEv(const QZipReader *self) {
  return self->status();
}

//  void QZipReader::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QZipReader5closeEv(QZipReader *self) {
  self->close();
}

//  a QList<QZipReader::FileInfo> a ritual of QZipReader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QZipReader__QList_QZipReader_FileInfo(
    QList<QZipReader::FileInfo> *self) {
  delete self;
}
