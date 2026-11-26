//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qstaticrigidbody_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qstaticrigidbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QStaticRigidBody that Python can take functions over in. Every QStaticRigidBody
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStaticRigidBodyCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall3)(const void *, int *);
typedef void * (*CuteQStaticRigidBodyCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQStaticRigidBodyCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQStaticRigidBodyCall6)(const void *, int *);
typedef void (*CuteQStaticRigidBodyCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStaticRigidBodyCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStaticRigidBodyCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStaticRigidBodyCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStaticRigidBody : public QStaticRigidBody {
public:
  using QStaticRigidBody::QStaticRigidBody;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[0]) {
      int handled = 0;
      CuteQStaticRigidBodyCall0 call = reinterpret_cast<CuteQStaticRigidBodyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStaticRigidBodyCall1 call = reinterpret_cast<CuteQStaticRigidBodyCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStaticRigidBodyCall2 call = reinterpret_cast<CuteQStaticRigidBodyCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQStaticRigidBodyCall3 call = reinterpret_cast<CuteQStaticRigidBodyCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQStaticRigidBodyCall4 call = reinterpret_cast<CuteQStaticRigidBodyCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStaticRigidBodyCall5 call = reinterpret_cast<CuteQStaticRigidBodyCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQStaticRigidBodyCall6 call = reinterpret_cast<CuteQStaticRigidBodyCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQStaticRigidBodyCall7 call = reinterpret_cast<CuteQStaticRigidBodyCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQStaticRigidBodyCall8 call = reinterpret_cast<CuteQStaticRigidBodyCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQStaticRigidBodyCall9 call = reinterpret_cast<CuteQStaticRigidBodyCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStaticRigidBodyCall10 call = reinterpret_cast<CuteQStaticRigidBodyCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStaticRigidBodyCall11 call = reinterpret_cast<CuteQStaticRigidBodyCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStaticRigidBodyCall12 call = reinterpret_cast<CuteQStaticRigidBodyCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStaticRigidBody::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QStaticRigidBody10metaObjectEv(
    const QStaticRigidBody *self) {
  return self->metaObject();
}

//  void *QStaticRigidBody::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QStaticRigidBody11qt_metacastEPKc(
    QStaticRigidBody *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QStaticRigidBody::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QStaticRigidBody11qt_metacallEN11QMetaObject4CallEiPPv(
    QStaticRigidBody *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QStaticRigidBody::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QStaticRigidBody2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStaticRigidBody::tr(s, c, n));
}

//  QStaticRigidBody::QStaticRigidBody()
extern "C" Q_DECL_EXPORT
QStaticRigidBody *ritual_ZN16QStaticRigidBodyC1Ev() {
  return new CuteQStaticRigidBody();
}

//  QAbstractPhysXNode *QStaticRigidBody::createPhysXBackend()
extern "C" Q_DECL_EXPORT
QAbstractPhysXNode *ritual_ZN16QStaticRigidBody18createPhysXBackendEv(
    QStaticRigidBody *self) {
  return self->createPhysXBackend();
}

//  a Python function taken by a CuteQStaticRigidBody, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStaticRigidBody(
    QStaticRigidBody *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStaticRigidBody *>(self)->take(key, call);
}
