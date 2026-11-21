//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfilesystemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfilesystemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdir.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>

//  const QMetaObject *QFileSystemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QFileSystemModel10metaObjectEv(
    const QFileSystemModel *self) {
  return self->metaObject();
}

//  QString QFileSystemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QFileSystemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSystemModel::tr(s, c, n));
}

//  QFileSystemModel::QFileSystemModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSystemModel *ritual_ZN16QFileSystemModelC1EP7QObject(QObject *parent) {
  return new QFileSystemModel(parent);
}

//  QFileSystemModel::~QFileSystemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModelD1Ev(QFileSystemModel *self) {
  delete self;
}

//  QModelIndex QFileSystemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel5indexEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QFileSystemModel::index(const QString &path, int column)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel5indexERK7QStringi(
    const QFileSystemModel *self,
    const QString *path,
    int column) {
  return new QModelIndex(self->index(*path, column));
}

//  QModelIndex QFileSystemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel6parentERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QFileSystemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QFileSystemModel7siblingEiiRK11QModelIndex(
    const QFileSystemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QFileSystemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel11hasChildrenERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  bool QFileSystemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel12canFetchMoreERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QFileSystemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9fetchMoreERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  int QFileSystemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel8rowCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QFileSystemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel11columnCountERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QFileSystemModel::myComputer(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel10myComputerEi(
    const QFileSystemModel *self,
    int role) {
  return new QVariant(self->myComputer(role));
}

//  QVariant QFileSystemModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel4dataERK11QModelIndexi(
    const QFileSystemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QFileSystemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel7setDataERK11QModelIndexRK8QVarianti(
    QFileSystemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QFileSystemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QFileSystemModel10headerDataEiN2Qt11OrientationEi(
    const QFileSystemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  Qt::ItemFlags QFileSystemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel5flagsERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QFileSystemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel4sortEiN2Qt9SortOrderE(
    QFileSystemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  bool QFileSystemModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QFileSystemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QFileSystemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel20supportedDropActionsEv(
    const QFileSystemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  QModelIndex QFileSystemModel::setRootPath(const QString &path)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN16QFileSystemModel11setRootPathERK7QString(
    QFileSystemModel *self,
    const QString *path) {
  return new QModelIndex(self->setRootPath(*path));
}

//  QString QFileSystemModel::rootPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8rootPathEv(
    const QFileSystemModel *self) {
  return new QString(self->rootPath());
}

//  QDir QFileSystemModel::rootDirectory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK16QFileSystemModel13rootDirectoryEv(
    const QFileSystemModel *self) {
  return new QDir(self->rootDirectory());
}

//  void QFileSystemModel::setIconProvider(QAbstractFileIconProvider
//      *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel15setIconProviderEP25QAbstractFileIconProvider(
    QFileSystemModel *self,
    QAbstractFileIconProvider *provider) {
  self->setIconProvider(provider);
}

//  QAbstractFileIconProvider *QFileSystemModel::iconProvider() const
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZNK16QFileSystemModel12iconProviderEv(
    const QFileSystemModel *self) {
  return self->iconProvider();
}

//  void QFileSystemModel::setFilter(QDir::Filters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9setFilterE6QFlagsIN4QDir6FilterEE(
    QFileSystemModel *self,
    int filters) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filters));
}

//  QDir::Filters QFileSystemModel::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel6filterEv(const QFileSystemModel *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QFileSystemModel::setResolveSymlinks(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel18setResolveSymlinksEb(
    QFileSystemModel *self,
    bool enable) {
  self->setResolveSymlinks(enable);
}

//  bool QFileSystemModel::resolveSymlinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel15resolveSymlinksEv(
    const QFileSystemModel *self) {
  return self->resolveSymlinks();
}

//  void QFileSystemModel::setReadOnly(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel11setReadOnlyEb(
    QFileSystemModel *self,
    bool enable) {
  self->setReadOnly(enable);
}

//  bool QFileSystemModel::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel10isReadOnlyEv(
    const QFileSystemModel *self) {
  return self->isReadOnly();
}

//  void QFileSystemModel::setNameFilterDisables(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel21setNameFilterDisablesEb(
    QFileSystemModel *self,
    bool enable) {
  self->setNameFilterDisables(enable);
}

//  bool QFileSystemModel::nameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel18nameFilterDisablesEv(
    const QFileSystemModel *self) {
  return self->nameFilterDisables();
}

//  void QFileSystemModel::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel9setOptionENS_6OptionEb(
    QFileSystemModel *self,
    QFileSystemModel::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFileSystemModel::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel10testOptionENS_6OptionE(
    const QFileSystemModel *self,
    QFileSystemModel::Option option) {
  return self->testOption(option);
}

//  void QFileSystemModel::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileSystemModel10setOptionsE6QFlagsINS_6OptionEE(
    QFileSystemModel *self,
    int options) {
  self->setOptions(QFlags<QFileSystemModel::Option>::fromInt(options));
}

//  Options QFileSystemModel::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFileSystemModel7optionsEv(const QFileSystemModel *self) {
  return static_cast<int>(self->options().toInt());
}

//  QString QFileSystemModel::filePath(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8filePathERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->filePath(*index));
}

//  bool QFileSystemModel::isDir(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileSystemModel5isDirERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return self->isDir(*index);
}

//  qint64 QFileSystemModel::size(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QFileSystemModel4sizeERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return self->size(*index);
}

//  QString QFileSystemModel::type(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel4typeERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->type(*index));
}

//  QDateTime QFileSystemModel::lastModified(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QDateTime(self->lastModified(*index));
}

//  QDateTime QFileSystemModel::lastModified(const QModelIndex &index, const
//      QTimeZone &tz) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndexRK9QTimeZone(
    const QFileSystemModel *self,
    const QModelIndex *index,
    const QTimeZone *tz) {
  return new QDateTime(self->lastModified(*index, *tz));
}

//  QModelIndex QFileSystemModel::mkdir(const QModelIndex &parent, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN16QFileSystemModel5mkdirERK11QModelIndexRK7QString(
    QFileSystemModel *self,
    const QModelIndex *parent,
    const QString *name) {
  return new QModelIndex(self->mkdir(*parent, *name));
}

//  bool QFileSystemModel::rmdir(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel5rmdirERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *index) {
  return self->rmdir(*index);
}

//  QString QFileSystemModel::fileName(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFileSystemModel8fileNameERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QString(self->fileName(*index));
}

//  QIcon QFileSystemModel::fileIcon(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QFileSystemModel8fileIconERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QIcon(self->fileIcon(*index));
}

//  QFileInfo QFileSystemModel::fileInfo(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK16QFileSystemModel8fileInfoERK11QModelIndex(
    const QFileSystemModel *self,
    const QModelIndex *index) {
  return new QFileInfo(self->fileInfo(*index));
}

//  bool QFileSystemModel::remove(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QFileSystemModel6removeERK11QModelIndex(
    QFileSystemModel *self,
    const QModelIndex *index) {
  return self->remove(*index);
}
