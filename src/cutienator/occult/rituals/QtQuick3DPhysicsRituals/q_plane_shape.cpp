//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qplaneshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qplaneshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QPlaneShape that Python can take functions over in. Every QPlaneShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlaneShapeCall0)(const void *, int *);
typedef bool (*CuteQPlaneShapeCall1)(const void *, int *);
typedef void (*CuteQPlaneShapeCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall5)(const void *, int *);
typedef void * (*CuteQPlaneShapeCall6)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQPlaneShapeCall7)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQPlaneShapeCall8)(const void *, int *);
typedef void (*CuteQPlaneShapeCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaneShapeCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaneShapeCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaneShapeCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaneShape : public QPlaneShape {
public:
  using QPlaneShape::QPlaneShape;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstractCollisionShape16getPhysXGeometryEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QAbstractCollisionShape13isStaticShapeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  physx::PxGeometry *QPlaneShape::getPhysXGeometry()
  physx::PxGeometry *getPhysXGeometry() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaneShapeCall0 call = reinterpret_cast<CuteQPlaneShapeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<physx::PxGeometry *>(given);
    }
    return QPlaneShape::getPhysXGeometry();
  }

  //  bool QPlaneShape::isStaticShape() const
  bool isStaticShape() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaneShapeCall1 call = reinterpret_cast<CuteQPlaneShapeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlaneShape::isStaticShape();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaneShapeCall2 call = reinterpret_cast<CuteQPlaneShapeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlaneShapeCall3 call = reinterpret_cast<CuteQPlaneShapeCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlaneShapeCall4 call = reinterpret_cast<CuteQPlaneShapeCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlaneShapeCall5 call = reinterpret_cast<CuteQPlaneShapeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlaneShapeCall6 call = reinterpret_cast<CuteQPlaneShapeCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQPlaneShapeCall7 call = reinterpret_cast<CuteQPlaneShapeCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlaneShapeCall8 call = reinterpret_cast<CuteQPlaneShapeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlaneShapeCall9 call = reinterpret_cast<CuteQPlaneShapeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlaneShapeCall10 call = reinterpret_cast<CuteQPlaneShapeCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlaneShapeCall11 call = reinterpret_cast<CuteQPlaneShapeCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlaneShapeCall12 call = reinterpret_cast<CuteQPlaneShapeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlaneShapeCall13 call = reinterpret_cast<CuteQPlaneShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlaneShapeCall14 call = reinterpret_cast<CuteQPlaneShapeCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaneShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPlaneShape10metaObjectEv(
    const QPlaneShape *self) {
  return self->metaObject();
}

//  void *QPlaneShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QPlaneShape11qt_metacastEPKc(
    QPlaneShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaneShape::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QPlaneShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaneShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaneShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPlaneShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaneShape::tr(s, c, n));
}

//  QPlaneShape::QPlaneShape()
extern "C" Q_DECL_EXPORT
QPlaneShape *ritual_ZN11QPlaneShapeC1Ev() {
  return new CuteQPlaneShape();
}

//  QPlaneShape::~QPlaneShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaneShapeD1Ev(QPlaneShape *self) {
  delete self;
}

//  physx::PxGeometry *QPlaneShape::getPhysXGeometry()
extern "C" Q_DECL_EXPORT
physx::PxGeometry *ritual_ZN11QPlaneShape16getPhysXGeometryEv(
    QPlaneShape *self) {
  return self->getPhysXGeometry();
}

//  bool QPlaneShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPlaneShape13isStaticShapeEv(const QPlaneShape *self) {
  return self->isStaticShape();
}

//  void QPlaneShape::updatePhysXGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaneShape19updatePhysXGeometryEv(QPlaneShape *self) {
  self->updatePhysXGeometry();
}

//  a Python function taken by a CuteQPlaneShape, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaneShape(
    QPlaneShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaneShape *>(self)->take(key, call);
}

//  physx::PxGeometry *QPlaneShape::getPhysXGeometry()
extern "C" Q_DECL_EXPORT
physx::PxGeometry *ritual_own_ZN11QPlaneShape16getPhysXGeometryEv(
    QPlaneShape *self) {
  return self->QPlaneShape::getPhysXGeometry();
}

//  bool QPlaneShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QPlaneShape13isStaticShapeEv(const QPlaneShape *self) {
  return self->QPlaneShape::isStaticShape();
}
