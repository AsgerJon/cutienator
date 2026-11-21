//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qdatetime.h>

//  QString QDirListing::DirEntry::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry8fileNameEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->fileName());
}

//  QString QDirListing::DirEntry::baseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry8baseNameEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->baseName());
}

//  QString QDirListing::DirEntry::completeBaseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry16completeBaseNameEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->completeBaseName());
}

//  QString QDirListing::DirEntry::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry6suffixEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->suffix());
}

//  QString QDirListing::DirEntry::bundleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry10bundleNameEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->bundleName());
}

//  QString QDirListing::DirEntry::completeSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry14completeSuffixEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->completeSuffix());
}

//  QString QDirListing::DirEntry::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry8filePathEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->filePath());
}

//  bool QDirListing::DirEntry::isDir() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry5isDirEv(
    const QDirListing::DirEntry *self) {
  return self->isDir();
}

//  bool QDirListing::DirEntry::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry6isFileEv(
    const QDirListing::DirEntry *self) {
  return self->isFile();
}

//  bool QDirListing::DirEntry::isSymLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry9isSymLinkEv(
    const QDirListing::DirEntry *self) {
  return self->isSymLink();
}

//  bool QDirListing::DirEntry::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry6existsEv(
    const QDirListing::DirEntry *self) {
  return self->exists();
}

//  bool QDirListing::DirEntry::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry8isHiddenEv(
    const QDirListing::DirEntry *self) {
  return self->isHidden();
}

//  bool QDirListing::DirEntry::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry10isReadableEv(
    const QDirListing::DirEntry *self) {
  return self->isReadable();
}

//  bool QDirListing::DirEntry::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry10isWritableEv(
    const QDirListing::DirEntry *self) {
  return self->isWritable();
}

//  bool QDirListing::DirEntry::isExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing8DirEntry12isExecutableEv(
    const QDirListing::DirEntry *self) {
  return self->isExecutable();
}

//  QFileInfo QDirListing::DirEntry::fileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK11QDirListing8DirEntry8fileInfoEv(
    const QDirListing::DirEntry *self) {
  return new QFileInfo(self->fileInfo());
}

//  QString QDirListing::DirEntry::canonicalFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry17canonicalFilePathEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->canonicalFilePath());
}

//  QString QDirListing::DirEntry::absoluteFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry16absoluteFilePathEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->absoluteFilePath());
}

//  QString QDirListing::DirEntry::absolutePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing8DirEntry12absolutePathEv(
    const QDirListing::DirEntry *self) {
  return new QString(self->absolutePath());
}

//  qint64 QDirListing::DirEntry::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QDirListing8DirEntry4sizeEv(
    const QDirListing::DirEntry *self) {
  return self->size();
}

//  QDateTime QDirListing::DirEntry::birthTime(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QDirListing8DirEntry9birthTimeERK9QTimeZone(
    const QDirListing::DirEntry *self,
    const QTimeZone *tz) {
  return new QDateTime(self->birthTime(*tz));
}

//  QDateTime QDirListing::DirEntry::metadataChangeTime(const QTimeZone &tz)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QDirListing8DirEntry18metadataChangeTimeERK9QTimeZone(
    const QDirListing::DirEntry *self,
    const QTimeZone *tz) {
  return new QDateTime(self->metadataChangeTime(*tz));
}

//  QDateTime QDirListing::DirEntry::lastModified(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QDirListing8DirEntry12lastModifiedERK9QTimeZone(
    const QDirListing::DirEntry *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*tz));
}

//  QDateTime QDirListing::DirEntry::lastRead(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QDirListing8DirEntry8lastReadERK9QTimeZone(
    const QDirListing::DirEntry *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastRead(*tz));
}

//  QDateTime QDirListing::DirEntry::fileTime(QFileDevice::FileTime type,
//      const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QDirListing8DirEntry8fileTimeEN11QFileDevice8FileTimeERK9QTimeZone(
    const QDirListing::DirEntry *self,
    QFileDevice::FileTime type,
    const QTimeZone *tz) {
  return new QDateTime(self->fileTime(type, *tz));
}

//  QDirListing::DirEntry::~DirEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing8DirEntryD1Ev(QDirListing::DirEntry *self) {
  delete self;
}
