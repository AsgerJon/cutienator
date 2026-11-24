//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/barinstancing_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/barinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A BarInstancing that Python can take functions over in. Every BarInstancing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteBarInstancingCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteBarInstancingCall1)(const void *, int *);
typedef void (*CuteBarInstancingCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteBarInstancingCall3)(const void *, int *);
typedef void (*CuteBarInstancingCall4)(const void *, int *);
typedef void (*CuteBarInstancingCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarInstancingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarInstancingCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarInstancingCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarInstancingCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarInstancingCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarInstancingCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarInstancingCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBarInstancing : public BarInstancing {
public:
  using BarInstancing::BarInstancing;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteBarInstancingCall0 call = reinterpret_cast<CuteBarInstancingCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstancing::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteBarInstancingCall1 call = reinterpret_cast<CuteBarInstancingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteBarInstancingCall2 call = reinterpret_cast<CuteBarInstancingCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteBarInstancingCall3 call = reinterpret_cast<CuteBarInstancingCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteBarInstancingCall4 call = reinterpret_cast<CuteBarInstancingCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteBarInstancingCall5 call = reinterpret_cast<CuteBarInstancingCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteBarInstancingCall6 call = reinterpret_cast<CuteBarInstancingCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteBarInstancingCall7 call = reinterpret_cast<CuteBarInstancingCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteBarInstancingCall8 call = reinterpret_cast<CuteBarInstancingCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteBarInstancingCall9 call = reinterpret_cast<CuteBarInstancingCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteBarInstancingCall10 call = reinterpret_cast<CuteBarInstancingCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteBarInstancingCall11 call = reinterpret_cast<CuteBarInstancingCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteBarInstancingCall12 call = reinterpret_cast<CuteBarInstancingCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BarInstancing::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13BarInstancing10metaObjectEv(
    const BarInstancing *self) {
  return self->metaObject();
}

//  QString BarInstancing::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13BarInstancing2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BarInstancing::tr(s, c, n));
}

//  BarInstancing::BarInstancing()
extern "C" Q_DECL_EXPORT
BarInstancing *ritual_ZN13BarInstancingC1Ev() {
  return new CuteBarInstancing();
}

//  BarInstancing::~BarInstancing()
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarInstancingD1Ev(BarInstancing *self) {
  delete self;
}

//  QList<BarItemHolder *> BarInstancing::dataArray() const
extern "C" Q_DECL_EXPORT
QList<BarItemHolder *> *ritual_ZNK13BarInstancing9dataArrayEv(
    const BarInstancing *self) {
  return new QList<BarItemHolder *>(self->dataArray());
}

//  void BarInstancing::setDataArray(const QList<BarItemHolder *>
//      &newDataArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarInstancing12setDataArrayERK5QListIP13BarItemHolderE(
    BarInstancing *self,
    const QList<BarItemHolder *> *newDataArray) {
  self->setDataArray(*newDataArray);
}

//  void BarInstancing::markDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarInstancing13markDataDirtyEv(BarInstancing *self) {
  self->markDataDirty();
}

//  bool BarInstancing::transparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13BarInstancing12transparencyEv(const BarInstancing *self) {
  return self->transparency();
}

//  void BarInstancing::setTransparency(bool newTransparencyValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarInstancing15setTransparencyEb(
    BarInstancing *self,
    bool newTransparencyValue) {
  self->setTransparency(newTransparencyValue);
}

//  void BarInstancing::clearDataArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarInstancing14clearDataArrayEv(BarInstancing *self) {
  self->clearDataArray();
}

//  QByteArray BarInstancing::getInstanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN13BarInstancing17getInstanceBufferEPi(
    BarInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

//  a Python function taken by a CuteBarInstancing, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BarInstancing(
    BarInstancing *self,
    const char *key,
    void *call) {
  return static_cast<CuteBarInstancing *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
