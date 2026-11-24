//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfilesystemmodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(filesystemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qfilesystemmodel.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfilesystemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qicon.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFileSystemModelPrivate that Python can take functions over in. Every QFileSystemModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQFileSystemModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQFileSystemModelPrivate : public QFileSystemModelPrivate {
public:
  using QFileSystemModelPrivate::QFileSystemModelPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileSystemModelPrivateCall0 call = reinterpret_cast<CuteQFileSystemModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QFileSystemModel *QFileSystemModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileSystemModel *ritual_ZN23QFileSystemModelPrivate6q_funcEv(
    QFileSystemModelPrivate *self) {
  return self->q_func();
}

//  const QFileSystemModel *QFileSystemModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileSystemModel *ritual_ZNK23QFileSystemModelPrivate6q_funcEv(
    const QFileSystemModelPrivate *self) {
  return self->q_func();
}

//  QFileSystemModelPrivate::QFileSystemModelPrivate()
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate *ritual_ZN23QFileSystemModelPrivateC1Ev() {
  return new CuteQFileSystemModelPrivate();
}

//  QFileSystemModelPrivate::~QFileSystemModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivateD1Ev(QFileSystemModelPrivate *self) {
  delete self;
}

//  void QFileSystemModelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate4initEv(
    QFileSystemModelPrivate *self) {
  self->init();
}

//  bool QFileSystemModelPrivate::isHiddenByFilter(QFileSystemNode
//      *indexNode, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate16isHiddenByFilterEPNS_15QFileSystemNodeERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *indexNode,
    const QModelIndex *index) {
  return self->isHiddenByFilter(indexNode, *index);
}

//  QFileSystemNode *QFileSystemModelPrivate::node(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate::QFileSystemNode *ritual_ZNK23QFileSystemModelPrivate4nodeERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return self->node(*index);
}

//  QFileSystemNode *QFileSystemModelPrivate::node(const QString &path, bool
//      fetch) const
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate::QFileSystemNode *ritual_ZNK23QFileSystemModelPrivate4nodeERK7QStringb(
    const QFileSystemModelPrivate *self,
    const QString *path,
    bool fetch) {
  return self->node(*path, fetch);
}

//  QModelIndex QFileSystemModelPrivate::index(const QString &path, int
//      column)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN23QFileSystemModelPrivate5indexERK7QStringi(
    QFileSystemModelPrivate *self,
    const QString *path,
    int column) {
  return new QModelIndex(self->index(*path, column));
}

//  QModelIndex QFileSystemModelPrivate::index(const QFileSystemNode *node,
//      int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK23QFileSystemModelPrivate5indexEPKNS_15QFileSystemNodeEi(
    const QFileSystemModelPrivate *self,
    const QFileSystemModelPrivate::QFileSystemNode *node,
    int column) {
  return new QModelIndex(self->index(node, column));
}

//  bool QFileSystemModelPrivate::filtersAcceptsNode(const QFileSystemNode
//      *node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate18filtersAcceptsNodeEPKNS_15QFileSystemNodeE(
    const QFileSystemModelPrivate *self,
    const QFileSystemModelPrivate::QFileSystemNode *node) {
  return self->filtersAcceptsNode(node);
}

//  bool QFileSystemModelPrivate::passNameFilters(const QFileSystemNode
//      *node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QFileSystemModelPrivate15passNameFiltersEPKNS_15QFileSystemNodeE(
    const QFileSystemModelPrivate *self,
    const QFileSystemModelPrivate::QFileSystemNode *node) {
  return self->passNameFilters(node);
}

//  void QFileSystemModelPrivate::removeNode(QFileSystemNode *parentNode,
//      const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate10removeNodeEPNS_15QFileSystemNodeERK7QString(
    QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *parentNode,
    const QString *name) {
  self->removeNode(parentNode, *name);
}

//  QFileSystemNode *QFileSystemModelPrivate::addNode(QFileSystemNode
//      *parentNode, const QString &fileName, const QFileInfo &info)
extern "C" Q_DECL_EXPORT
QFileSystemModelPrivate::QFileSystemNode *ritual_ZN23QFileSystemModelPrivate7addNodeEPNS_15QFileSystemNodeERK7QStringRK9QFileInfo(
    QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *parentNode,
    const QString *fileName,
    const QFileInfo *info) {
  return self->addNode(parentNode, *fileName, *info);
}

//  void QFileSystemModelPrivate::addVisibleFiles(QFileSystemNode
//      *parentNode, const QStringList &newFiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate15addVisibleFilesEPNS_15QFileSystemNodeERK5QListI7QStringE(
    QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *parentNode,
    const QList<QString> *newFiles) {
  self->addVisibleFiles(parentNode, *newFiles);
}

//  void QFileSystemModelPrivate::removeVisibleFile(QFileSystemNode
//      *parentNode, int visibleLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate17removeVisibleFileEPNS_15QFileSystemNodeEi(
    QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *parentNode,
    int visibleLocation) {
  self->removeVisibleFile(parentNode, visibleLocation);
}

//  void QFileSystemModelPrivate::sortChildren(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate12sortChildrenEiRK11QModelIndex(
    QFileSystemModelPrivate *self,
    int column,
    const QModelIndex *parent) {
  self->sortChildren(column, *parent);
}

//  int QFileSystemModelPrivate::translateVisibleLocation(QFileSystemNode
//      *parent, int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QFileSystemModelPrivate24translateVisibleLocationEPNS_15QFileSystemNodeEi(
    const QFileSystemModelPrivate *self,
    QFileSystemModelPrivate::QFileSystemNode *parent,
    int row) {
  return self->translateVisibleLocation(parent, row);
}

//  QString QFileSystemModelPrivate::myComputer()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QFileSystemModelPrivate10myComputerEv() {
  return new QString(QFileSystemModelPrivate::myComputer());
}

//  void QFileSystemModelPrivate::delayedSort()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate11delayedSortEv(
    QFileSystemModelPrivate *self) {
  self->delayedSort();
}

//  QIcon QFileSystemModelPrivate::icon(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK23QFileSystemModelPrivate4iconERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QIcon(self->icon(*index));
}

//  QString QFileSystemModelPrivate::name(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate4nameERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->name(*index));
}

//  QString QFileSystemModelPrivate::displayName(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate11displayNameERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->displayName(*index));
}

//  QString QFileSystemModelPrivate::filePath(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate8filePathERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->filePath(*index));
}

//  QString QFileSystemModelPrivate::size(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate4sizeERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->size(*index));
}

//  QString QFileSystemModelPrivate::size(qint64 bytes)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QFileSystemModelPrivate4sizeEx(qint64 bytes) {
  return new QString(QFileSystemModelPrivate::size(bytes));
}

//  QString QFileSystemModelPrivate::type(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate4typeERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->type(*index));
}

//  QString QFileSystemModelPrivate::time(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QFileSystemModelPrivate4timeERK11QModelIndex(
    const QFileSystemModelPrivate *self,
    const QModelIndex *index) {
  return new QString(self->time(*index));
}

//  void QFileSystemModelPrivate::directoryChanged(const QString &directory,
//      const QStringList &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate16directoryChangedERK7QStringRK5QListIS0_E(
    QFileSystemModelPrivate *self,
    const QString *directory,
    const QList<QString> *list) {
  self->directoryChanged(*directory, *list);
}

//  void QFileSystemModelPrivate::performDelayedSort()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate18performDelayedSortEv(
    QFileSystemModelPrivate *self) {
  self->performDelayedSort();
}

//  void QFileSystemModelPrivate::resolvedName(const QString &fileName, const
//      QString &resolvedName)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate12resolvedNameERK7QStringS2_(
    QFileSystemModelPrivate *self,
    const QString *fileName,
    const QString *resolvedName) {
  self->resolvedName(*fileName, *resolvedName);
}

#if QT_CONFIG(regularexpression)
//  void QFileSystemModelPrivate::rebuildNameFilterRegexps()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFileSystemModelPrivate24rebuildNameFilterRegexpsEv(
    QFileSystemModelPrivate *self) {
  self->rebuildNameFilterRegexps();
}
#endif  // QT_CONFIG(regularexpression)

//  a Python function taken by a CuteQFileSystemModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSystemModelPrivate(
    QFileSystemModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSystemModelPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemmodel)
