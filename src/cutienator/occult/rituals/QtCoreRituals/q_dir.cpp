//  Written by dev_tooling.RitualGenerator from the records of QtCore/qdir.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 4. Kept as it is when the generator runs again.
#include <QtCore/qdir.h>
#include <QtCore/qstring.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>
#include <filesystem>
#include <QtCore/QString>
#include <optional>
#include <QtCore/QFile>

//  QDir::QDir(const QDir &a0)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1ERKS_(const QDir *a0) {
  return new QDir(*a0);
}

//  QDir::QDir(const QString &path)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1ERK7QString(const QString *path) {
  return new QDir(*path);
}

//  QDir::QDir(const QString &path, const QString &nameFilter, SortFlags
//      sort, Filters filter)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1ERK7QStringS2_6QFlagsINS_8SortFlagEES3_INS_6FilterEE(
    const QString *path,
    const QString *nameFilter,
    int sort,
    int filter) {
  return new QDir(
      *path,
      *nameFilter,
      QFlags<QDir::SortFlag>::fromInt(sort),
      QFlags<QDir::Filter>::fromInt(filter));
}

//  QDir::~QDir()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDirD1Ev(QDir *self) {
  delete self;
}

//  QDir &QDir::operator=(const QDir &a0)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDiraSERKS_(QDir *self, const QDir *a0) {
  return &(self->operator=(*a0));
}

//  QDir &QDir::operator=(QDir &&other)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDiraSEOS_(QDir *self, QDir *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QDir::swap(QDir &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir4swapERS_(QDir *self, QDir *other) {
  self->swap(*other);
}

//  void QDir::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir7setPathERK7QString(QDir *self, const QString *path) {
  self->setPath(*path);
}

//  QString QDir::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir4pathEv(const QDir *self) {
  return new QString(self->path());
}

//  QString QDir::absolutePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir12absolutePathEv(const QDir *self) {
  return new QString(self->absolutePath());
}

//  QString QDir::canonicalPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir13canonicalPathEv(const QDir *self) {
  return new QString(self->canonicalPath());
}

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QDir::filesystemPath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK4QDir14filesystemPathB5cxx11Ev(
    const QDir *self) {
  return new std::filesystem::path(self->filesystemPath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QDir::filesystemAbsolutePath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK4QDir22filesystemAbsolutePathB5cxx11Ev(
    const QDir *self) {
  return new std::filesystem::path(self->filesystemAbsolutePath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QDir::filesystemCanonicalPath() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK4QDir23filesystemCanonicalPathB5cxx11Ev(
    const QDir *self) {
  return new std::filesystem::path(self->filesystemCanonicalPath());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

#if !defined(QT_BOOTSTRAPPED)
//  void QDir::setSearchPaths(const QString &prefix, const QStringList
//      &searchPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir14setSearchPathsERK7QStringRK5QListIS0_E(
    const QString *prefix,
    const QList<QString> *searchPaths) {
  QDir::setSearchPaths(*prefix, *searchPaths);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  void QDir::addSearchPath(const QString &prefix, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir13addSearchPathERK7QStringS2_(
    const QString *prefix,
    const QString *path) {
  QDir::addSearchPath(*prefix, *path);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  QStringList QDir::searchPaths(const QString &prefix)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN4QDir11searchPathsERK7QString(
    const QString *prefix) {
  return new QList<QString>(QDir::searchPaths(*prefix));
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QString QDir::dirName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir7dirNameEv(const QDir *self) {
  return new QString(self->dirName());
}

//  QString QDir::filePath(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir8filePathERK7QString(
    const QDir *self,
    const QString *fileName) {
  return new QString(self->filePath(*fileName));
}

//  QString QDir::absoluteFilePath(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir16absoluteFilePathERK7QString(
    const QDir *self,
    const QString *fileName) {
  return new QString(self->absoluteFilePath(*fileName));
}

//  QString QDir::relativeFilePath(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDir16relativeFilePathERK7QString(
    const QDir *self,
    const QString *fileName) {
  return new QString(self->relativeFilePath(*fileName));
}

//  QString QDir::toNativeSeparators(const QString &pathName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir18toNativeSeparatorsERK7QString(
    const QString *pathName) {
  return new QString(QDir::toNativeSeparators(*pathName));
}

//  QString QDir::fromNativeSeparators(const QString &pathName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir20fromNativeSeparatorsERK7QString(
    const QString *pathName) {
  return new QString(QDir::fromNativeSeparators(*pathName));
}

//  bool QDir::cd(const QString &dirName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir2cdERK7QString(QDir *self, const QString *dirName) {
  return self->cd(*dirName);
}

//  bool QDir::cdUp()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir4cdUpEv(QDir *self) {
  return self->cdUp();
}

//  QStringList QDir::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK4QDir11nameFiltersEv(const QDir *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QDir::setNameFilters(const QStringList &nameFilters)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir14setNameFiltersERK5QListI7QStringE(
    QDir *self,
    const QList<QString> *nameFilters) {
  self->setNameFilters(*nameFilters);
}

//  Filters QDir::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QDir6filterEv(const QDir *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QDir::setFilter(Filters filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir9setFilterE6QFlagsINS_6FilterEE(QDir *self, int filter) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filter));
}

//  SortFlags QDir::sorting() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QDir7sortingEv(const QDir *self) {
  return static_cast<int>(self->sorting().toInt());
}

//  void QDir::setSorting(SortFlags sort)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir10setSortingE6QFlagsINS_8SortFlagEE(
    QDir *self,
    int sort) {
  self->setSorting(QFlags<QDir::SortFlag>::fromInt(sort));
}

//  qsizetype QDir::count(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK4QDir5countEN2Qt15Disambiguated_tE(
    const QDir *self,
    const Qt::Disambiguated_t *a0) {
  return self->count(*a0);
}

//  bool QDir::isEmpty(Filters filters) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir7isEmptyE6QFlagsINS_6FilterEE(
    const QDir *self,
    int filters) {
  return self->isEmpty(QFlags<QDir::Filter>::fromInt(filters));
}

//  QString QDir::operator[](qsizetype a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QDirixEx(const QDir *self, qsizetype a0) {
  return new QString(self->operator[](a0));
}

//  QStringList QDir::nameFiltersFromString(const QString &nameFilter)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN4QDir21nameFiltersFromStringERK7QString(
    const QString *nameFilter) {
  return new QList<QString>(QDir::nameFiltersFromString(*nameFilter));
}

//  QStringList QDir::entryList(Filters filters, SortFlags sort) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK4QDir9entryListE6QFlagsINS_6FilterEES0_INS_8SortFlagEE(
    const QDir *self,
    int filters,
    int sort) {
  return new QList<QString>(
      self->entryList(
          QFlags<QDir::Filter>::fromInt(filters),
          QFlags<QDir::SortFlag>::fromInt(sort)));
}

//  QStringList QDir::entryList(const QStringList &nameFilters, Filters
//      filters, SortFlags sort) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK4QDir9entryListERK5QListI7QStringE6QFlagsINS_6FilterEES5_INS_8SortFlagEE(
    const QDir *self,
    const QList<QString> *nameFilters,
    int filters,
    int sort) {
  return new QList<QString>(
      self->entryList(
          *nameFilters,
          QFlags<QDir::Filter>::fromInt(filters),
          QFlags<QDir::SortFlag>::fromInt(sort)));
}

//  QFileInfoList QDir::entryInfoList(Filters filters, SortFlags sort) const
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_ZNK4QDir13entryInfoListE6QFlagsINS_6FilterEES0_INS_8SortFlagEE(
    const QDir *self,
    int filters,
    int sort) {
  return new QList<QFileInfo>(
      self->entryInfoList(
          QFlags<QDir::Filter>::fromInt(filters),
          QFlags<QDir::SortFlag>::fromInt(sort)));
}

//  QFileInfoList QDir::entryInfoList(const QStringList &nameFilters, Filters
//      filters, SortFlags sort) const
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_ZNK4QDir13entryInfoListERK5QListI7QStringE6QFlagsINS_6FilterEES5_INS_8SortFlagEE(
    const QDir *self,
    const QList<QString> *nameFilters,
    int filters,
    int sort) {
  return new QList<QFileInfo>(
      self->entryInfoList(
          *nameFilters,
          QFlags<QDir::Filter>::fromInt(filters),
          QFlags<QDir::SortFlag>::fromInt(sort)));
}

//  bool QDir::mkdir(const QString &dirName,
//      std::optional<QFile::Permissions> p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir5mkdirERK7QStringSt8optionalI6QFlagsIN11QFileDevice10PermissionEEE(
    const QDir *self,
    const QString *dirName,
    const std::optional<QFile::Permissions> *p) {
  return self->mkdir(*dirName, *p);
}

//  bool QDir::rmdir(const QString &dirName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir5rmdirERK7QString(
    const QDir *self,
    const QString *dirName) {
  return self->rmdir(*dirName);
}

//  bool QDir::mkpath(const QString &dirPath,
//      std::optional<QFile::Permissions> p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir6mkpathERK7QStringSt8optionalI6QFlagsIN11QFileDevice10PermissionEEE(
    const QDir *self,
    const QString *dirPath,
    const std::optional<QFile::Permissions> *p) {
  return self->mkpath(*dirPath, *p);
}

//  bool QDir::rmpath(const QString &dirPath) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir6rmpathERK7QString(
    const QDir *self,
    const QString *dirPath) {
  return self->rmpath(*dirPath);
}

//  bool QDir::removeRecursively()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir17removeRecursivelyEv(QDir *self) {
  return self->removeRecursively();
}

//  bool QDir::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir10isReadableEv(const QDir *self) {
  return self->isReadable();
}

//  bool QDir::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir6existsEv(const QDir *self) {
  return self->exists();
}

//  bool QDir::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir6isRootEv(const QDir *self) {
  return self->isRoot();
}

//  bool QDir::isRelativePath(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir14isRelativePathERK7QString(const QString *path) {
  return QDir::isRelativePath(*path);
}

//  bool QDir::isAbsolutePath(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir14isAbsolutePathERK7QString(const QString *path) {
  return QDir::isAbsolutePath(*path);
}

//  bool QDir::isRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir10isRelativeEv(const QDir *self) {
  return self->isRelative();
}

//  bool QDir::isAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir10isAbsoluteEv(const QDir *self) {
  return self->isAbsolute();
}

//  bool QDir::makeAbsolute()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir12makeAbsoluteEv(QDir *self) {
  return self->makeAbsolute();
}

//  bool QDir::remove(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir6removeERK7QString(QDir *self, const QString *fileName) {
  return self->remove(*fileName);
}

//  bool QDir::rename(const QString &oldName, const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir6renameERK7QStringS2_(
    QDir *self,
    const QString *oldName,
    const QString *newName) {
  return self->rename(*oldName, *newName);
}

//  bool QDir::exists(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir6existsERK7QString(
    const QDir *self,
    const QString *name) {
  return self->exists(*name);
}

//  QFileInfoList QDir::drives()
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_ZN4QDir6drivesEv() {
  return new QList<QFileInfo>(QDir::drives());
}

//  QChar QDir::listSeparator()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN4QDir13listSeparatorEv() {
  return new QChar(QDir::listSeparator());
}

//  QChar QDir::separator()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN4QDir9separatorEv() {
  return new QChar(QDir::separator());
}

//  bool QDir::setCurrent(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir10setCurrentERK7QString(const QString *path) {
  return QDir::setCurrent(*path);
}

//  QDir QDir::current()
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDir7currentEv() {
  return new QDir(QDir::current());
}

//  QString QDir::currentPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir11currentPathEv() {
  return new QString(QDir::currentPath());
}

//  QDir QDir::home()
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDir4homeEv() {
  return new QDir(QDir::home());
}

//  QString QDir::homePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir8homePathEv() {
  return new QString(QDir::homePath());
}

//  QDir QDir::root()
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDir4rootEv() {
  return new QDir(QDir::root());
}

//  QString QDir::rootPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir8rootPathEv() {
  return new QString(QDir::rootPath());
}

//  QDir QDir::temp()
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDir4tempEv() {
  return new QDir(QDir::temp());
}

//  QString QDir::tempPath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir8tempPathEv() {
  return new QString(QDir::tempPath());
}

#if QT_CONFIG(regularexpression)
//  bool QDir::match(const QStringList &filters, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir5matchERK5QListI7QStringERKS1_(
    const QList<QString> *filters,
    const QString *fileName) {
  return QDir::match(*filters, *fileName);
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  bool QDir::match(const QString &filter, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir5matchERK7QStringS2_(
    const QString *filter,
    const QString *fileName) {
  return QDir::match(*filter, *fileName);
}
#endif  // QT_CONFIG(regularexpression)

//  QString QDir::cleanPath(const QString &path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QDir9cleanPathERK7QString(const QString *path) {
  return new QString(QDir::cleanPath(*path));
}

//  void QDir::refresh() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QDir7refreshEv(const QDir *self) {
  self->refresh();
}

//  QDir::QDir(QDirPrivate &d)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1ER11QDirPrivate(QDirPrivate *d) {
  return new QDir(*d);
}

//  bool operator==(const QDir &lhs, const QDir &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK4QDirS1_(const QDir *lhs, const QDir *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QDir &lhs, const QDir &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK4QDirS1_(const QDir *lhs, const QDir *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QDirPrivate *QDir::d_func()
extern "C" Q_DECL_EXPORT
QDirPrivate *ritual_ZN4QDir6d_funcEv(QDir *self) {
  return self->d_func();
}

//  const QDirPrivate *QDir::d_func() const
extern "C" Q_DECL_EXPORT
const QDirPrivate *ritual_ZNK4QDir6d_funcEv(const QDir *self) {
  return self->d_func();
}

//  a std::filesystem::path a ritual of QDir gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDir__std_filesystem_path(std::filesystem::path *self) {
  delete self;
}

#if QT_CONFIG(cxx17_filesystem)
//  QDir::QDir<std::filesystem::path, 0>(const std::filesystem::path &path)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1INSt10filesystem7__cxx114pathELi0EEERKT_(
    const std::filesystem::path *path) {
  return new QDir(*path);
}

//  QDir::QDir<std::filesystem::path, 0>(const std::filesystem::path &path,
//      const QString &nameFilter, SortFlags sort, Filters filter)
extern "C" Q_DECL_EXPORT
QDir *ritual_ZN4QDirC1INSt10filesystem7__cxx114pathELi0EEERKT_RK7QString6QFlagsINS_8SortFlagEES9_INS_6FilterEE(
    const std::filesystem::path *path,
    const QString *nameFilter,
    QDir::SortFlags sort,
    QDir::Filters filter) {
  return new QDir(*path, *nameFilter, sort, filter);
}

//  void QDir::setPath<std::filesystem::path, 0>(
//      const std::filesystem::path &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir7setPathINSt10filesystem7__cxx114pathELi0EEEvRKT_(
    QDir *self,
    const std::filesystem::path *path) {
  self->setPath(*path);
}

#if !defined(QT_BOOTSTRAPPED)
//  static void QDir::addSearchPath<std::filesystem::path, 0>(
//      const QString &prefix, const std::filesystem::path &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir13addSearchPathINSt10filesystem7__cxx114pathELi0EEEvRK7QStringRKT_(
    const QString *prefix,
    const std::filesystem::path *path) {
  QDir::addSearchPath(*prefix, *path);
}
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // QT_CONFIG(cxx17_filesystem)
