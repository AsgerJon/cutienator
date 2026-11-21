//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresource.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qresource.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>

//  QResource::QResource(const QString &file, const QLocale &locale)
extern "C" Q_DECL_EXPORT
QResource *ritual_ZN9QResourceC1ERK7QStringRK7QLocale(
    const QString *file,
    const QLocale *locale) {
  return new QResource(*file, *locale);
}

//  QResource::~QResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QResourceD1Ev(QResource *self) {
  delete self;
}

//  void QResource::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QResource11setFileNameERK7QString(
    QResource *self,
    const QString *file) {
  self->setFileName(*file);
}

//  QString QResource::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QResource8fileNameEv(const QResource *self) {
  return new QString(self->fileName());
}

//  QString QResource::absoluteFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QResource16absoluteFilePathEv(const QResource *self) {
  return new QString(self->absoluteFilePath());
}

//  void QResource::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QResource9setLocaleERK7QLocale(
    QResource *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QResource::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK9QResource6localeEv(const QResource *self) {
  return new QLocale(self->locale());
}

//  bool QResource::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QResource7isValidEv(const QResource *self) {
  return self->isValid();
}

//  Compression QResource::compressionAlgorithm() const
extern "C" Q_DECL_EXPORT
QResource::Compression ritual_ZNK9QResource20compressionAlgorithmEv(
    const QResource *self) {
  return self->compressionAlgorithm();
}

//  qint64 QResource::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QResource4sizeEv(const QResource *self) {
  return self->size();
}

//  qint64 QResource::uncompressedSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QResource16uncompressedSizeEv(const QResource *self) {
  return self->uncompressedSize();
}

//  QByteArray QResource::uncompressedData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QResource16uncompressedDataEv(const QResource *self) {
  return new QByteArray(self->uncompressedData());
}

//  QDateTime QResource::lastModified() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QResource12lastModifiedEv(const QResource *self) {
  return new QDateTime(self->lastModified());
}

//  bool QResource::registerResource(const QString &rccFilename, const
//      QString &resourceRoot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QResource16registerResourceERK7QStringS2_(
    const QString *rccFilename,
    const QString *resourceRoot) {
  return QResource::registerResource(*rccFilename, *resourceRoot);
}

//  bool QResource::unregisterResource(const QString &rccFilename, const
//      QString &resourceRoot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QResource18unregisterResourceERK7QStringS2_(
    const QString *rccFilename,
    const QString *resourceRoot) {
  return QResource::unregisterResource(*rccFilename, *resourceRoot);
}
