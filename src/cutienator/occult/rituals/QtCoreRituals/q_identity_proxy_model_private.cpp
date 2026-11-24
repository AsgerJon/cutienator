//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qidentityproxymodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qidentityproxymodel.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qidentityproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QIdentityProxyModelPrivate that Python can take functions over in. Every QIdentityProxyModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(proxymodel)
typedef void (*CuteQIdentityProxyModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQIdentityProxyModelPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQIdentityProxyModelPrivate : public QIdentityProxyModelPrivate {
public:
  using QIdentityProxyModelPrivate::QIdentityProxyModelPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    return false;
  }

#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()
  void _q_sourceModelDestroyed() override {
    if (taken[0]) {
      int handled = 0;
      CuteQIdentityProxyModelPrivateCall0 call = reinterpret_cast<CuteQIdentityProxyModelPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModelPrivate::_q_sourceModelDestroyed();
  }
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelPrivate::executePendingOperations() const
  void executePendingOperations() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIdentityProxyModelPrivateCall1 call = reinterpret_cast<CuteQIdentityProxyModelPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QIdentityProxyModel *QIdentityProxyModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QIdentityProxyModel *ritual_ZN26QIdentityProxyModelPrivate6q_funcEv(
    QIdentityProxyModelPrivate *self) {
  return self->q_func();
}

//  const QIdentityProxyModel *QIdentityProxyModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QIdentityProxyModel *ritual_ZNK26QIdentityProxyModelPrivate6q_funcEv(
    const QIdentityProxyModelPrivate *self) {
  return self->q_func();
}

//  QIdentityProxyModelPrivate::QIdentityProxyModelPrivate()
extern "C" Q_DECL_EXPORT
QIdentityProxyModelPrivate *ritual_ZN26QIdentityProxyModelPrivateC1Ev() {
  return new CuteQIdentityProxyModelPrivate();
}

//  QIdentityProxyModelPrivate::~QIdentityProxyModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivateD1Ev(
    QIdentityProxyModelPrivate *self) {
  delete self;
}

//  void QIdentityProxyModelPrivate::sourceRowsAboutToBeInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate27sourceRowsAboutToBeInsertedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceRowsAboutToBeInserted(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate18sourceRowsInsertedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceRowsInserted(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceRowsAboutToBeRemoved(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate26sourceRowsAboutToBeRemovedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceRowsAboutToBeRemoved(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate17sourceRowsRemovedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceRowsRemoved(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceRowsAboutToBeMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate24sourceRowsAboutToBeMovedERK11QModelIndexiiS2_i(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->sourceRowsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QIdentityProxyModelPrivate::sourceRowsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate15sourceRowsMovedERK11QModelIndexiiS2_i(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->sourceRowsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate30sourceColumnsAboutToBeInsertedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceColumnsAboutToBeInserted(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceColumnsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate21sourceColumnsInsertedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceColumnsInserted(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeRemoved(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate29sourceColumnsAboutToBeRemovedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceColumnsAboutToBeRemoved(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceColumnsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate20sourceColumnsRemovedERK11QModelIndexii(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->sourceColumnsRemoved(*parent, start, end);
}

//  void QIdentityProxyModelPrivate::sourceColumnsAboutToBeMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate27sourceColumnsAboutToBeMovedERK11QModelIndexiiS2_i(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->sourceColumnsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QIdentityProxyModelPrivate::sourceColumnsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destParent, int dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate18sourceColumnsMovedERK11QModelIndexiiS2_i(
    QIdentityProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destParent,
    int dest) {
  self->sourceColumnsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destParent,
      dest);
}

//  void QIdentityProxyModelPrivate::sourceHeaderDataChanged(Qt::Orientation
//      orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate23sourceHeaderDataChangedEN2Qt11OrientationEii(
    QIdentityProxyModelPrivate *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->sourceHeaderDataChanged(orientation, first, last);
}

//  void QIdentityProxyModelPrivate::sourceLayoutAboutToBeChanged(const
//      QList<QPersistentModelIndex> &sourceParents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate28sourceLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QIdentityProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *sourceParents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->sourceLayoutAboutToBeChanged(*sourceParents, hint);
}

//  void QIdentityProxyModelPrivate::sourceLayoutChanged(const
//      QList<QPersistentModelIndex> &sourceParents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate19sourceLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QIdentityProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *sourceParents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->sourceLayoutChanged(*sourceParents, hint);
}

//  void QIdentityProxyModelPrivate::sourceModelAboutToBeReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate25sourceModelAboutToBeResetEv(
    QIdentityProxyModelPrivate *self) {
  self->sourceModelAboutToBeReset();
}

//  void QIdentityProxyModelPrivate::sourceModelReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIdentityProxyModelPrivate16sourceModelResetEv(
    QIdentityProxyModelPrivate *self) {
  self->sourceModelReset();
}

//  a Python function taken by a CuteQIdentityProxyModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIdentityProxyModelPrivate(
    QIdentityProxyModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIdentityProxyModelPrivate *>(self)->take(key, call);
}
