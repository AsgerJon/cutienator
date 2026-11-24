//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QAbstractItemModelPrivate that Python can take functions over in. Every QAbstractItemModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQAbstractItemModelPrivate : public QAbstractItemModelPrivate {
public:
  using QAbstractItemModelPrivate::QAbstractItemModelPrivate;
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
      CuteQAbstractItemModelPrivateCall0 call = reinterpret_cast<CuteQAbstractItemModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QAbstractItemModel *QAbstractItemModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN25QAbstractItemModelPrivate6q_funcEv(
    QAbstractItemModelPrivate *self) {
  return self->q_func();
}

//  const QAbstractItemModel *QAbstractItemModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK25QAbstractItemModelPrivate6q_funcEv(
    const QAbstractItemModelPrivate *self) {
  return self->q_func();
}

//  QAbstractItemModelPrivate::QAbstractItemModelPrivate()
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate *ritual_ZN25QAbstractItemModelPrivateC1Ev() {
  return new CuteQAbstractItemModelPrivate();
}

//  QAbstractItemModelPrivate::~QAbstractItemModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivateD1Ev(
    QAbstractItemModelPrivate *self) {
  delete self;
}

//  const QAbstractItemModelPrivate *QAbstractItemModelPrivate::get(const
//      QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
const QAbstractItemModelPrivate *ritual_ZN25QAbstractItemModelPrivate3getEPK18QAbstractItemModel(
    const QAbstractItemModel *model) {
  return QAbstractItemModelPrivate::get(model);
}

//  void QAbstractItemModelPrivate::removePersistentIndexData(QPersistentMode
//      lIndexData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate25removePersistentIndexDataEP25QPersistentModelIndexData(
    QAbstractItemModelPrivate *self,
    QPersistentModelIndexData *data) {
  self->removePersistentIndexData(data);
}

//  void QAbstractItemModelPrivate::movePersistentIndexes(const
//      QList<QPersistentModelIndexData *> &indexes, int change, const
//      QModelIndex &parent, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate21movePersistentIndexesERK5QListIP25QPersistentModelIndexDataEiRK11QModelIndexN2Qt11OrientationE(
    QAbstractItemModelPrivate *self,
    const QList<QPersistentModelIndexData *> *indexes,
    int change,
    const QModelIndex *parent,
    Qt::Orientation orientation) {
  self->movePersistentIndexes(*indexes, change, *parent, orientation);
}

//  void QAbstractItemModelPrivate::rowsAboutToBeInserted(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate21rowsAboutToBeInsertedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->rowsAboutToBeInserted(*parent, first, last);
}

//  void QAbstractItemModelPrivate::rowsInserted(const QModelIndex &parent,
//      int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate12rowsInsertedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->rowsInserted(*parent, first, last);
}

//  void QAbstractItemModelPrivate::rowsAboutToBeRemoved(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate20rowsAboutToBeRemovedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->rowsAboutToBeRemoved(*parent, first, last);
}

//  void QAbstractItemModelPrivate::rowsRemoved(const QModelIndex &parent,
//      int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate11rowsRemovedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->rowsRemoved(*parent, first, last);
}

//  void QAbstractItemModelPrivate::columnsAboutToBeInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate24columnsAboutToBeInsertedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->columnsAboutToBeInserted(*parent, first, last);
}

//  void QAbstractItemModelPrivate::columnsInserted(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate15columnsInsertedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->columnsInserted(*parent, first, last);
}

//  void QAbstractItemModelPrivate::columnsAboutToBeRemoved(const QModelIndex
//      &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate23columnsAboutToBeRemovedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->columnsAboutToBeRemoved(*parent, first, last);
}

//  void QAbstractItemModelPrivate::columnsRemoved(const QModelIndex &parent,
//      int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate14columnsRemovedERK11QModelIndexii(
    QAbstractItemModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->columnsRemoved(*parent, first, last);
}

//  QAbstractItemModel *QAbstractItemModelPrivate::staticEmptyModel()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN25QAbstractItemModelPrivate16staticEmptyModelEv() {
  return QAbstractItemModelPrivate::staticEmptyModel();
}

//  bool QAbstractItemModelPrivate::variantLessThan(const QVariant &v1, const
//      QVariant &v2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractItemModelPrivate15variantLessThanERK8QVariantS2_(
    const QVariant *v1,
    const QVariant *v2) {
  return QAbstractItemModelPrivate::variantLessThan(*v1, *v2);
}

//  void QAbstractItemModelPrivate::itemsAboutToBeMoved(const QModelIndex
//      &srcParent, int srcFirst, int srcLast, const QModelIndex
//      &destinationParent, int destinationChild, Qt::Orientation a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate19itemsAboutToBeMovedERK11QModelIndexiiS2_iN2Qt11OrientationE(
    QAbstractItemModelPrivate *self,
    const QModelIndex *srcParent,
    int srcFirst,
    int srcLast,
    const QModelIndex *destinationParent,
    int destinationChild,
    Qt::Orientation a5) {
  self->itemsAboutToBeMoved(
      *srcParent,
      srcFirst,
      srcLast,
      *destinationParent,
      destinationChild,
      a5);
}

//  void QAbstractItemModelPrivate::itemsMoved(const QModelIndex &srcParent,
//      int srcFirst, int srcLast, const QModelIndex &destinationParent, int
//      destinationChild, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate10itemsMovedERK11QModelIndexiiS2_iN2Qt11OrientationE(
    QAbstractItemModelPrivate *self,
    const QModelIndex *srcParent,
    int srcFirst,
    int srcLast,
    const QModelIndex *destinationParent,
    int destinationChild,
    Qt::Orientation orientation) {
  self->itemsMoved(
      *srcParent,
      srcFirst,
      srcLast,
      *destinationParent,
      destinationChild,
      orientation);
}

//  bool QAbstractItemModelPrivate::allowMove(const QModelIndex &srcParent,
//      int srcFirst, int srcLast, const QModelIndex &destinationParent, int
//      destinationChild, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractItemModelPrivate9allowMoveERK11QModelIndexiiS2_iN2Qt11OrientationE(
    QAbstractItemModelPrivate *self,
    const QModelIndex *srcParent,
    int srcFirst,
    int srcLast,
    const QModelIndex *destinationParent,
    int destinationChild,
    Qt::Orientation orientation) {
  return self->allowMove(
      *srcParent,
      srcFirst,
      srcLast,
      *destinationParent,
      destinationChild,
      orientation);
}

//  void QAbstractItemModelPrivate::executePendingOperations() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv(
    const QAbstractItemModelPrivate *self) {
  self->executePendingOperations();
}

//  QModelIndex QAbstractItemModelPrivate::createIndex(int row, int column,
//      int id) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QAbstractItemModelPrivate11createIndexEiii(
    const QAbstractItemModelPrivate *self,
    int row,
    int column,
    int id) {
  return new QModelIndex(self->createIndex(row, column, id));
}

//  bool QAbstractItemModelPrivate::indexValid(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractItemModelPrivate10indexValidERK11QModelIndex(
    const QAbstractItemModelPrivate *self,
    const QModelIndex *index) {
  return self->indexValid(*index);
}

//  void QAbstractItemModelPrivate::invalidatePersistentIndexes()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate27invalidatePersistentIndexesEv(
    QAbstractItemModelPrivate *self) {
  self->invalidatePersistentIndexes();
}

//  void QAbstractItemModelPrivate::invalidatePersistentIndex(const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelPrivate25invalidatePersistentIndexERK11QModelIndex(
    QAbstractItemModelPrivate *self,
    const QModelIndex *index) {
  self->invalidatePersistentIndex(*index);
}

//  const QHash<int, QByteArray>
//      &QAbstractItemModelPrivate::defaultRoleNames()
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZN25QAbstractItemModelPrivate16defaultRoleNamesEv() {
  return new QHash<int, QByteArray>(
      QAbstractItemModelPrivate::defaultRoleNames());
}

//  a Python function taken by a CuteQAbstractItemModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemModelPrivate(
    QAbstractItemModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemModelPrivate *>(self)->take(key, call);
}

//  void QAbstractItemModelPrivate::executePendingOperations() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv(
    const QAbstractItemModelPrivate *self) {
  self->QAbstractItemModelPrivate::executePendingOperations();
}

#endif  // QT_CONFIG(itemmodel)
