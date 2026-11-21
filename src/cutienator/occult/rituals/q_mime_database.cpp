//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmimedatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmimedatabase.h>
#include <QtCore/qstring.h>
#include <QtCore/qmimetype.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>

//  QMimeDatabase::QMimeDatabase()
extern "C" Q_DECL_EXPORT
QMimeDatabase *ritual_ZN13QMimeDatabaseC1Ev() {
  return new QMimeDatabase();
}

//  QMimeDatabase::~QMimeDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMimeDatabaseD1Ev(QMimeDatabase *self) {
  delete self;
}

//  QMimeType QMimeDatabase::mimeTypeForName(const QString &nameOrAlias)
//      const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase15mimeTypeForNameERK7QString(
    const QMimeDatabase *self,
    const QString *nameOrAlias) {
  return new QMimeType(self->mimeTypeForName(*nameOrAlias));
}

//  QMimeType QMimeDatabase::mimeTypeForFile(const QString &fileName,
//      MatchMode mode) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase15mimeTypeForFileERK7QStringNS_9MatchModeE(
    const QMimeDatabase *self,
    const QString *fileName,
    QMimeDatabase::MatchMode mode) {
  return new QMimeType(self->mimeTypeForFile(*fileName, mode));
}

//  QMimeType QMimeDatabase::mimeTypeForFile(const QFileInfo &fileInfo,
//      MatchMode mode) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase15mimeTypeForFileERK9QFileInfoNS_9MatchModeE(
    const QMimeDatabase *self,
    const QFileInfo *fileInfo,
    QMimeDatabase::MatchMode mode) {
  return new QMimeType(self->mimeTypeForFile(*fileInfo, mode));
}

//  QMimeType QMimeDatabase::mimeTypeForData(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase15mimeTypeForDataERK10QByteArray(
    const QMimeDatabase *self,
    const QByteArray *data) {
  return new QMimeType(self->mimeTypeForData(*data));
}

//  QMimeType QMimeDatabase::mimeTypeForData(QIODevice *device) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase15mimeTypeForDataEP9QIODevice(
    const QMimeDatabase *self,
    QIODevice *device) {
  return new QMimeType(self->mimeTypeForData(device));
}

//  QMimeType QMimeDatabase::mimeTypeForUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase14mimeTypeForUrlERK4QUrl(
    const QMimeDatabase *self,
    const QUrl *url) {
  return new QMimeType(self->mimeTypeForUrl(*url));
}

//  QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const QString
//      &fileName, QIODevice *device) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase26mimeTypeForFileNameAndDataERK7QStringP9QIODevice(
    const QMimeDatabase *self,
    const QString *fileName,
    QIODevice *device) {
  return new QMimeType(self->mimeTypeForFileNameAndData(*fileName, device));
}

//  QMimeType QMimeDatabase::mimeTypeForFileNameAndData(const QString
//      &fileName, const QByteArray &data) const
extern "C" Q_DECL_EXPORT
QMimeType *ritual_ZNK13QMimeDatabase26mimeTypeForFileNameAndDataERK7QStringRK10QByteArray(
    const QMimeDatabase *self,
    const QString *fileName,
    const QByteArray *data) {
  return new QMimeType(self->mimeTypeForFileNameAndData(*fileName, *data));
}

//  QString QMimeDatabase::suffixForFileName(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QMimeDatabase17suffixForFileNameERK7QString(
    const QMimeDatabase *self,
    const QString *fileName) {
  return new QString(self->suffixForFileName(*fileName));
}
