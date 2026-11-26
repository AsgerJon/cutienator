//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfileinfo.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 3. Kept as it is when the
//  generator runs again.
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qlist.h>
#include <filesystem>
#include <QtCore/QFile>
#include <QtCore/QDateTime>
#include <QtCore/QTimeZone>

//  QFileInfo::QFileInfo(QFileInfoPrivate *d)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1EP16QFileInfoPrivate(QFileInfoPrivate *d) {
  return new QFileInfo(d);
}

//  QFileInfo::QFileInfo()
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1Ev() {
  return new QFileInfo();
}

//  QFileInfo::QFileInfo(const QString &file)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1ERK7QString(const QString *file) {
  return new QFileInfo(*file);
}

//  QFileInfo::QFileInfo(const QFileDevice &file)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1ERK11QFileDevice(const QFileDevice *file) {
  return new QFileInfo(*file);
}

//  QFileInfo::QFileInfo(const QDir &dir, const QString &file)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1ERK4QDirRK7QString(
    const QDir *dir,
    const QString *file) {
  return new QFileInfo(*dir, *file);
}

//  QFileInfo::QFileInfo(const QFileInfo &fileinfo)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1ERKS_(const QFileInfo *fileinfo) {
  return new QFileInfo(*fileinfo);
}

//  QFileInfo::QFileInfo(QFileInfo &&other)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1EOS_(QFileInfo *other) {
  return new QFileInfo(std::move(*other));
}

//  QFileInfo::~QFileInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfoD1Ev(QFileInfo *self) {
  delete self;
}

//  QFileInfo &QFileInfo::operator=(const QFileInfo &fileinfo)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoaSERKS_(
    QFileInfo *self,
    const QFileInfo *fileinfo) {
  return &(self->operator=(*fileinfo));
}

//  QFileInfo &QFileInfo::operator=(QFileInfo &&other)
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoaSEOS_(QFileInfo *self, QFileInfo *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QFileInfo::swap(QFileInfo &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo4swapERS_(QFileInfo *self, QFileInfo *other) {
  self->swap(*other);
}

//  void QFileInfo::setFile(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo7setFileERK7QString(
    QFileInfo *self,
    const QString *file) {
  self->setFile(*file);
}

//  void QFileInfo::setFile(const QFileDevice &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo7setFileERK11QFileDevice(
    QFileInfo *self,
    const QFileDevice *file) {
  self->setFile(*file);
}

//  void QFileInfo::setFile(const QDir &dir, const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo7setFileERK4QDirRK7QString(
    QFileInfo *self,
    const QDir *dir,
    const QString *file) {
  self->setFile(*dir, *file);
}

//  bool QFileInfo::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo6existsEv(const QFileInfo *self) {
  return self->exists();
}

//  bool QFileInfo::exists(const QString &file)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QFileInfo6existsERK7QString(const QString *file) {
  return QFileInfo::exists(*file);
}

//  void QFileInfo::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo7refreshEv(QFileInfo *self) {
  self->refresh();
}

//  QString QFileInfo::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo8filePathEv(const QFileInfo *self) {
  return new QString(self->filePath());
}

//  QString QFileInfo::absoluteFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo16absoluteFilePathEv(const QFileInfo *self) {
  return new QString(self->absoluteFilePath());
}

//  QString QFileInfo::canonicalFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo17canonicalFilePathEv(const QFileInfo *self) {
  return new QString(self->canonicalFilePath());
}

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemFilePath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo18filesystemFilePathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemFilePath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemAbsoluteFilePath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo26filesystemAbsoluteFilePathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemAbsoluteFilePath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemCanonicalFilePath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo27filesystemCanonicalFilePathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemCanonicalFilePath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

//  QString QFileInfo::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo8fileNameEv(const QFileInfo *self) {
  return new QString(self->fileName());
}

//  QString QFileInfo::baseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo8baseNameEv(const QFileInfo *self) {
  return new QString(self->baseName());
}

//  QString QFileInfo::completeBaseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo16completeBaseNameEv(const QFileInfo *self) {
  return new QString(self->completeBaseName());
}

//  QString QFileInfo::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo6suffixEv(const QFileInfo *self) {
  return new QString(self->suffix());
}

//  QString QFileInfo::bundleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo10bundleNameEv(const QFileInfo *self) {
  return new QString(self->bundleName());
}

//  QString QFileInfo::completeSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo14completeSuffixEv(const QFileInfo *self) {
  return new QString(self->completeSuffix());
}

//  QString QFileInfo::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo4pathEv(const QFileInfo *self) {
  return new QString(self->path());
}

//  QString QFileInfo::absolutePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo12absolutePathEv(const QFileInfo *self) {
  return new QString(self->absolutePath());
}

//  QString QFileInfo::canonicalPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo13canonicalPathEv(const QFileInfo *self) {
  return new QString(self->canonicalPath());
}

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemPath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo14filesystemPathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemPath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemAbsolutePath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo22filesystemAbsolutePathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemAbsolutePath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemCanonicalPath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo23filesystemCanonicalPathB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemCanonicalPath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

//  QDir QFileInfo::dir() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK9QFileInfo3dirEv(const QFileInfo *self) {
  return new QDir(self->dir());
}

//  QDir QFileInfo::absoluteDir() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK9QFileInfo11absoluteDirEv(const QFileInfo *self) {
  return new QDir(self->absoluteDir());
}

//  bool QFileInfo::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isReadableEv(const QFileInfo *self) {
  return self->isReadable();
}

//  bool QFileInfo::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isWritableEv(const QFileInfo *self) {
  return self->isWritable();
}

//  bool QFileInfo::isExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo12isExecutableEv(const QFileInfo *self) {
  return self->isExecutable();
}

//  bool QFileInfo::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo8isHiddenEv(const QFileInfo *self) {
  return self->isHidden();
}

//  bool QFileInfo::isNativePath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo12isNativePathEv(const QFileInfo *self) {
  return self->isNativePath();
}

//  bool QFileInfo::isRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isRelativeEv(const QFileInfo *self) {
  return self->isRelative();
}

//  bool QFileInfo::isAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isAbsoluteEv(const QFileInfo *self) {
  return self->isAbsolute();
}

//  bool QFileInfo::makeAbsolute()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QFileInfo12makeAbsoluteEv(QFileInfo *self) {
  return self->makeAbsolute();
}

//  bool QFileInfo::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo6isFileEv(const QFileInfo *self) {
  return self->isFile();
}

//  bool QFileInfo::isDir() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo5isDirEv(const QFileInfo *self) {
  return self->isDir();
}

//  bool QFileInfo::isSymLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo9isSymLinkEv(const QFileInfo *self) {
  return self->isSymLink();
}

//  bool QFileInfo::isSymbolicLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo14isSymbolicLinkEv(const QFileInfo *self) {
  return self->isSymbolicLink();
}

//  bool QFileInfo::isOther() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo7isOtherEv(const QFileInfo *self) {
  return self->isOther();
}

//  bool QFileInfo::isShortcut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isShortcutEv(const QFileInfo *self) {
  return self->isShortcut();
}

//  bool QFileInfo::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo7isAliasEv(const QFileInfo *self) {
  return self->isAlias();
}

//  bool QFileInfo::isJunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10isJunctionEv(const QFileInfo *self) {
  return self->isJunction();
}

//  bool QFileInfo::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo6isRootEv(const QFileInfo *self) {
  return self->isRoot();
}

//  bool QFileInfo::isBundle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo8isBundleEv(const QFileInfo *self) {
  return self->isBundle();
}

//  QString QFileInfo::symLinkTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo13symLinkTargetEv(const QFileInfo *self) {
  return new QString(self->symLinkTarget());
}

//  QString QFileInfo::readSymLink() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo11readSymLinkEv(const QFileInfo *self) {
  return new QString(self->readSymLink());
}

//  QString QFileInfo::junctionTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo14junctionTargetEv(const QFileInfo *self) {
  return new QString(self->junctionTarget());
}

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemSymLinkTarget() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo23filesystemSymLinkTargetB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemSymLinkTarget());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemReadSymLink() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo21filesystemReadSymLinkB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemReadSymLink());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFileInfo::filesystemJunctionTarget() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QFileInfo24filesystemJunctionTargetB5cxx11Ev(
    const QFileInfo *self) {
  return new std::filesystem::path(self->filesystemJunctionTarget());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

//  QString QFileInfo::owner() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo5ownerEv(const QFileInfo *self) {
  return new QString(self->owner());
}

//  uint QFileInfo::ownerId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK9QFileInfo7ownerIdEv(const QFileInfo *self) {
  return self->ownerId();
}

//  QString QFileInfo::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QFileInfo5groupEv(const QFileInfo *self) {
  return new QString(self->group());
}

//  uint QFileInfo::groupId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK9QFileInfo7groupIdEv(const QFileInfo *self) {
  return self->groupId();
}

//  bool QFileInfo::permission(QFile::Permissions permissions) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo10permissionE6QFlagsIN11QFileDevice10PermissionEE(
    const QFileInfo *self,
    int permissions) {
  return self->permission(
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  QFile::Permissions QFileInfo::permissions() const
extern "C" Q_DECL_EXPORT
QFile::Permissions *ritual_ZNK9QFileInfo11permissionsEv(
    const QFileInfo *self) {
  return new QFile::Permissions(self->permissions());
}

//  qint64 QFileInfo::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QFileInfo4sizeEv(const QFileInfo *self) {
  return self->size();
}

//  QDateTime QFileInfo::birthTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo9birthTimeEv(const QFileInfo *self) {
  return new QDateTime(self->birthTime());
}

//  QDateTime QFileInfo::metadataChangeTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo18metadataChangeTimeEv(
    const QFileInfo *self) {
  return new QDateTime(self->metadataChangeTime());
}

//  QDateTime QFileInfo::lastModified() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo12lastModifiedEv(const QFileInfo *self) {
  return new QDateTime(self->lastModified());
}

//  QDateTime QFileInfo::lastRead() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo8lastReadEv(const QFileInfo *self) {
  return new QDateTime(self->lastRead());
}

//  QDateTime QFileInfo::fileTime(QFile::FileTime time) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo8fileTimeEN11QFileDevice8FileTimeE(
    const QFileInfo *self,
    const QFile::FileTime *time) {
  return new QDateTime(self->fileTime(*time));
}

//  QDateTime QFileInfo::birthTime(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo9birthTimeERK9QTimeZone(
    const QFileInfo *self,
    const QTimeZone *tz) {
  return new QDateTime(self->birthTime(*tz));
}

//  QDateTime QFileInfo::metadataChangeTime(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo18metadataChangeTimeERK9QTimeZone(
    const QFileInfo *self,
    const QTimeZone *tz) {
  return new QDateTime(self->metadataChangeTime(*tz));
}

//  QDateTime QFileInfo::lastModified(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo12lastModifiedERK9QTimeZone(
    const QFileInfo *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*tz));
}

//  QDateTime QFileInfo::lastRead(const QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo8lastReadERK9QTimeZone(
    const QFileInfo *self,
    const QTimeZone *tz) {
  return new QDateTime(self->lastRead(*tz));
}

//  QDateTime QFileInfo::fileTime(QFile::FileTime time, const QTimeZone &tz)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK9QFileInfo8fileTimeEN11QFileDevice8FileTimeERK9QTimeZone(
    const QFileInfo *self,
    const QFile::FileTime *time,
    const QTimeZone *tz) {
  return new QDateTime(self->fileTime(*time, *tz));
}

//  bool QFileInfo::caching() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QFileInfo7cachingEv(const QFileInfo *self) {
  return self->caching();
}

//  void QFileInfo::setCaching(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo10setCachingEb(QFileInfo *self, bool on) {
  self->setCaching(on);
}

//  void QFileInfo::stat()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo4statEv(QFileInfo *self) {
  self->stat();
}

//  bool operator==(const QFileInfo &lhs, const QFileInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QFileInfoS1_(const QFileInfo *lhs, const QFileInfo *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QFileInfo &lhs, const QFileInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QFileInfoS1_(const QFileInfo *lhs, const QFileInfo *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QFileInfoPrivate *QFileInfo::d_func()
extern "C" Q_DECL_EXPORT
QFileInfoPrivate *ritual_ZN9QFileInfo6d_funcEv(QFileInfo *self) {
  return self->d_func();
}

//  const QFileInfoPrivate *QFileInfo::d_func() const
extern "C" Q_DECL_EXPORT
const QFileInfoPrivate *ritual_ZNK9QFileInfo6d_funcEv(
    const QFileInfo *self) {
  return self->d_func();
}

//  QList<QFileInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_list_make_QFileInfo() {
  return new QList<QFileInfo>();
}

//  void QList<QFileInfo>::append(const QFileInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QFileInfo(
    QList<QFileInfo> *self,
    const QFileInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QFileInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QFileInfo(const QList<QFileInfo> *self) {
  return self->size();
}

//  const QFileInfo &QList<QFileInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_list_at_QFileInfo(
    const QList<QFileInfo> *self,
    long long index) {
  return new QFileInfo(self->at(index));
}

//  QList<QFileInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QFileInfo(QList<QFileInfo> *self) {
  delete self;
}

//  a std::filesystem::path a ritual of QFileInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFileInfo__std_filesystem_path(
    std::filesystem::path *self) {
  delete self;
}

//  a QFile::Permissions a ritual of QFileInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFileInfo__QFile_Permissions(QFile::Permissions *self) {
  delete self;
}

#if QT_CONFIG(cxx17_filesystem)
//  QFileInfo::QFileInfo(const T &file) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1INSt10filesystem7__cxx114pathELi0EEERKT_(
    const std::filesystem::path *file) {
  return new QFileInfo(*file);
}

//  QFileInfo::QFileInfo(const QDir &dir, const T &file)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN9QFileInfoC1INSt10filesystem7__cxx114pathELi0EEERK4QDirRKT_(
    const QDir *dir,
    const std::filesystem::path *file) {
  return new QFileInfo(*dir, *file);
}

//  void QFileInfo::setFile(const T &file) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
void ritual_ZN9QFileInfo7setFileINSt10filesystem7__cxx114pathELi0EEEvRKT_(
    QFileInfo *self,
    const std::filesystem::path *file) {
  self->setFile<std::filesystem::path>(*file);
}
#endif  // QT_CONFIG(cxx17_filesystem)
