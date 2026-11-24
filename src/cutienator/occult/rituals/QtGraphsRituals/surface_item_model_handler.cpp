//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/surfaceitemmodelhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/surfaceitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A SurfaceItemModelHandler that Python can take functions over in. Every SurfaceItemModelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteSurfaceItemModelHandlerCall0)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall1)(const void *, QAbstractItemModel *, int *);
typedef void * (*CuteSurfaceItemModelHandlerCall2)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall3)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall4)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall5)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall6)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall7)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall9)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteSurfaceItemModelHandlerCall10)(const void *, int *);
typedef void (*CuteSurfaceItemModelHandlerCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurfaceItemModelHandlerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurfaceItemModelHandlerCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurfaceItemModelHandlerCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSurfaceItemModelHandler : public SurfaceItemModelHandler {
public:
  using SurfaceItemModelHandler::SurfaceItemModelHandler;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12resolveModelEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemModel")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24AbstractItemModelHandler9itemModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelIndexiiS2_i")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler16handleModelResetEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexiiS2_i")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelIndexii")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handleMappingChangedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24AbstractItemModelHandler20handlePendingResolveEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void SurfaceItemModelHandler::resolveModel()
  void resolveModel() override {
    if (taken[0]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall0 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    SurfaceItemModelHandler::resolveModel();
  }

  //  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
  //      *itemModel)
  void setItemModel(QAbstractItemModel *itemModel) override {
    if (taken[1]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall1 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall1>(taken[1]);
      call(this, itemModel, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::setItemModel(itemModel);
  }

  //  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
  QAbstractItemModel *itemModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall2 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractItemModel *>(given);
    }
    return AbstractItemModelHandler::itemModel();
  }

  //  void AbstractItemModelHandler::handleColumnsInserted(const
  //      QModelIndex &parent, int start, int end)
  void handleColumnsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[3]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall3 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall3>(taken[3]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsInserted(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex
  //      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
  //      &destinationParent, int destinationColumn)
  void handleColumnsMoved(
      const QModelIndex &sourceParent,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destinationParent,
      int destinationColumn) override {
    if (taken[4]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall4 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall4>(taken[4]);
      call(this, &sourceParent, sourceStart, sourceEnd, &destinationParent, destinationColumn, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsMoved(sourceParent, sourceStart, sourceEnd, destinationParent, destinationColumn);
  }

  //  void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void handleColumnsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[5]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall5 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall5>(taken[5]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleColumnsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleModelReset()
  void handleModelReset() override {
    if (taken[6]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall6 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleModelReset();
  }

  //  void AbstractItemModelHandler::handleRowsInserted(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[7]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall7 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall7>(taken[7]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsInserted(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleRowsMoved(const QModelIndex
  //      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
  //      &destinationParent, int destinationRow)
  void handleRowsMoved(
      const QModelIndex &sourceParent,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destinationParent,
      int destinationRow) override {
    if (taken[8]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall8 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall8>(taken[8]);
      call(this, &sourceParent, sourceStart, sourceEnd, &destinationParent, destinationRow, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsMoved(sourceParent, sourceStart, sourceEnd, destinationParent, destinationRow);
  }

  //  void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void handleRowsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[9]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall9 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall9>(taken[9]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleRowsRemoved(parent, start, end);
  }

  //  void AbstractItemModelHandler::handleMappingChanged()
  void handleMappingChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall10 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handleMappingChanged();
  }

  //  void AbstractItemModelHandler::handlePendingResolve()
  void handlePendingResolve() override {
    if (taken[11]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall11 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    AbstractItemModelHandler::handlePendingResolve();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall12 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall13 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall14 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall15 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall16 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall17 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteSurfaceItemModelHandlerCall18 call = reinterpret_cast<CuteSurfaceItemModelHandlerCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *SurfaceItemModelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23SurfaceItemModelHandler10metaObjectEv(
    const SurfaceItemModelHandler *self) {
  return self->metaObject();
}

//  a Python function taken by a CuteSurfaceItemModelHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SurfaceItemModelHandler(
    SurfaceItemModelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteSurfaceItemModelHandler *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
