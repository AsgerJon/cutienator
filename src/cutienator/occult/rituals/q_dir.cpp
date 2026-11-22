//  Written by dev_tooling.RitualGenerator from the records of QtCore/qdir.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdir.h>
#include <QtCore/qstring.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qchar.h>

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

//  void QDir::addSearchPath(const QString &prefix, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QDir13addSearchPathERK7QStringS2_(
    const QString *prefix,
    const QString *path) {
  QDir::addSearchPath(*prefix, *path);
}

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

//  bool QDir::rmdir(const QString &dirName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QDir5rmdirERK7QString(
    const QDir *self,
    const QString *dirName) {
  return self->rmdir(*dirName);
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

//  bool QDir::match(const QString &filter, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QDir5matchERK7QStringS2_(
    const QString *filter,
    const QString *fileName) {
  return QDir::match(*filter, *fileName);
}

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
