//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractproxymodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(proxymodel)
#include <QtCore/qabstractproxymodel.h>
#endif
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <cstring>

//  A QAbstractProxyModelPrivate that Python can take functions over in. Every QAbstractProxyModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(proxymodel)
typedef void (*CuteQAbstractProxyModelPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractProxyModelPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
class CuteQAbstractProxyModelPrivate : public QAbstractProxyModelPrivate {
public:
  using QAbstractProxyModelPrivate::QAbstractProxyModelPrivate;
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
      CuteQAbstractProxyModelPrivateCall0 call = reinterpret_cast<CuteQAbstractProxyModelPrivateCall0>(taken[0]);
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
      CuteQAbstractProxyModelPrivateCall1 call = reinterpret_cast<CuteQAbstractProxyModelPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelPrivate::executePendingOperations();
  }
#endif  // QT_CONFIG(itemmodel)
};

//  QAbstractProxyModel *QAbstractProxyModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractProxyModel *ritual_ZN26QAbstractProxyModelPrivate6q_funcEv(
    QAbstractProxyModelPrivate *self) {
  return self->q_func();
}

//  const QAbstractProxyModel *QAbstractProxyModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractProxyModel *ritual_ZNK26QAbstractProxyModelPrivate6q_funcEv(
    const QAbstractProxyModelPrivate *self) {
  return self->q_func();
}

//  QAbstractProxyModelPrivate::QAbstractProxyModelPrivate()
extern "C" Q_DECL_EXPORT
QAbstractProxyModelPrivate *ritual_ZN26QAbstractProxyModelPrivateC1Ev() {
  return new CuteQAbstractProxyModelPrivate();
}

//  QAbstractProxyModelPrivate::~QAbstractProxyModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivateD1Ev(
    QAbstractProxyModelPrivate *self) {
  delete self;
}

//  void QAbstractProxyModelPrivate::setModelForwarder(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate17setModelForwarderEP18QAbstractItemModel(
    QAbstractProxyModelPrivate *self,
    QAbstractItemModel *sourceModel) {
  self->setModelForwarder(sourceModel);
}

//  void QAbstractProxyModelPrivate::modelChangedForwarder()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate21modelChangedForwarderEv(
    QAbstractProxyModelPrivate *self) {
  self->modelChangedForwarder();
}

//  QAbstractItemModel *QAbstractProxyModelPrivate::getModelForwarder() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK26QAbstractProxyModelPrivate17getModelForwarderEv(
    const QAbstractProxyModelPrivate *self) {
  return self->getModelForwarder();
}

//  size_t QAbstractProxyModelPrivate::_qt_property_model_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN26QAbstractProxyModelPrivate25_qt_property_model_offsetEv() {
  return QAbstractProxyModelPrivate::_qt_property_model_offset();
}

//  void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv(
    QAbstractProxyModelPrivate *self) {
  self->_q_sourceModelDestroyed();
}

//  void
//      QAbstractProxyModelPrivate::_q_sourceModelRowsAboutToBeInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate35_q_sourceModelRowsAboutToBeInsertedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelRowsAboutToBeInserted(*parent, first, last);
}

//  void QAbstractProxyModelPrivate::_q_sourceModelRowsInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate26_q_sourceModelRowsInsertedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelRowsInserted(*parent, first, last);
}

//  void QAbstractProxyModelPrivate::_q_sourceModelRowsRemoved(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate25_q_sourceModelRowsRemovedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelRowsRemoved(*parent, first, last);
}

//  void
//      QAbstractProxyModelPrivate::_q_sourceModelColumnsAboutToBeInserted(co
//      nst QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate38_q_sourceModelColumnsAboutToBeInsertedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelColumnsAboutToBeInserted(*parent, first, last);
}

//  void QAbstractProxyModelPrivate::_q_sourceModelColumnsInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate29_q_sourceModelColumnsInsertedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelColumnsInserted(*parent, first, last);
}

//  void QAbstractProxyModelPrivate::_q_sourceModelColumnsRemoved(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate28_q_sourceModelColumnsRemovedERK11QModelIndexii(
    QAbstractProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->_q_sourceModelColumnsRemoved(*parent, first, last);
}

//  void QAbstractProxyModelPrivate::mapDropCoordinatesToSource(int row, int
//      column, const QModelIndex &parent, int *source_row, int
//      *source_column, QModelIndex *source_parent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QAbstractProxyModelPrivate26mapDropCoordinatesToSourceEiiRK11QModelIndexPiS3_PS0_(
    const QAbstractProxyModelPrivate *self,
    int row,
    int column,
    const QModelIndex *parent,
    int *source_row,
    int *source_column,
    QModelIndex *source_parent) {
  self->mapDropCoordinatesToSource(
      row,
      column,
      *parent,
      source_row,
      source_column,
      source_parent);
}

//  void QAbstractProxyModelPrivate::scheduleHeaderUpdate(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate20scheduleHeaderUpdateEN2Qt11OrientationE(
    QAbstractProxyModelPrivate *self,
    Qt::Orientation orientation) {
  self->scheduleHeaderUpdate(orientation);
}

//  void QAbstractProxyModelPrivate::emitHeaderDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractProxyModelPrivate21emitHeaderDataChangedEv(
    QAbstractProxyModelPrivate *self) {
  self->emitHeaderDataChanged();
}

//  a Python function taken by a CuteQAbstractProxyModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractProxyModelPrivate(
    QAbstractProxyModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractProxyModelPrivate *>(self)->take(key, call);
}

//  void QAbstractProxyModelPrivate::_q_sourceModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAbstractProxyModelPrivate23_q_sourceModelDestroyedEv(
    QAbstractProxyModelPrivate *self) {
  self->QAbstractProxyModelPrivate::_q_sourceModelDestroyed();
}

#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(proxymodel)
