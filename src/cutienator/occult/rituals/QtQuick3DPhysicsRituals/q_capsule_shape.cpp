//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcapsuleshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcapsuleshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QCapsuleShape that Python can take functions over in. Every QCapsuleShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCapsuleShapeCall0)(const void *, int *);
typedef void (*CuteQCapsuleShapeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall4)(const void *, int *);
typedef void * (*CuteQCapsuleShapeCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQCapsuleShapeCall6)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQCapsuleShapeCall7)(const void *, int *);
typedef void (*CuteQCapsuleShapeCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCapsuleShapeCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCapsuleShapeCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCapsuleShapeCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCapsuleShape : public QCapsuleShape {
public:
  using QCapsuleShape::QCapsuleShape;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QAbstractCollisionShape13isStaticShapeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QCapsuleShape::isStaticShape() const
  bool isStaticShape() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCapsuleShapeCall0 call = reinterpret_cast<CuteQCapsuleShapeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCapsuleShape::isStaticShape();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCapsuleShapeCall1 call = reinterpret_cast<CuteQCapsuleShapeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCapsuleShapeCall2 call = reinterpret_cast<CuteQCapsuleShapeCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCapsuleShapeCall3 call = reinterpret_cast<CuteQCapsuleShapeCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQCapsuleShapeCall4 call = reinterpret_cast<CuteQCapsuleShapeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCapsuleShapeCall5 call = reinterpret_cast<CuteQCapsuleShapeCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQCapsuleShapeCall6 call = reinterpret_cast<CuteQCapsuleShapeCall6>(taken[6]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQCapsuleShapeCall7 call = reinterpret_cast<CuteQCapsuleShapeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQCapsuleShapeCall8 call = reinterpret_cast<CuteQCapsuleShapeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCapsuleShapeCall9 call = reinterpret_cast<CuteQCapsuleShapeCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCapsuleShapeCall10 call = reinterpret_cast<CuteQCapsuleShapeCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCapsuleShapeCall11 call = reinterpret_cast<CuteQCapsuleShapeCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCapsuleShapeCall12 call = reinterpret_cast<CuteQCapsuleShapeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCapsuleShapeCall13 call = reinterpret_cast<CuteQCapsuleShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCapsuleShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCapsuleShape10metaObjectEv(
    const QCapsuleShape *self) {
  return self->metaObject();
}

//  QString QCapsuleShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCapsuleShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCapsuleShape::tr(s, c, n));
}

//  QCapsuleShape::QCapsuleShape()
extern "C" Q_DECL_EXPORT
QCapsuleShape *ritual_ZN13QCapsuleShapeC1Ev() {
  return new CuteQCapsuleShape();
}

//  QCapsuleShape::~QCapsuleShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCapsuleShapeD1Ev(QCapsuleShape *self) {
  delete self;
}

//  float QCapsuleShape::diameter() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QCapsuleShape8diameterEv(const QCapsuleShape *self) {
  return self->diameter();
}

//  void QCapsuleShape::setDiameter(float newDiameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCapsuleShape11setDiameterEf(
    QCapsuleShape *self,
    float newDiameter) {
  self->setDiameter(newDiameter);
}

//  float QCapsuleShape::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QCapsuleShape6heightEv(const QCapsuleShape *self) {
  return self->height();
}

//  void QCapsuleShape::setHeight(float newHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCapsuleShape9setHeightEf(
    QCapsuleShape *self,
    float newHeight) {
  self->setHeight(newHeight);
}

//  bool QCapsuleShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCapsuleShape13isStaticShapeEv(const QCapsuleShape *self) {
  return self->isStaticShape();
}

//  void QCapsuleShape::updatePhysXGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCapsuleShape19updatePhysXGeometryEv(QCapsuleShape *self) {
  self->updatePhysXGeometry();
}

//  a Python function taken by a CuteQCapsuleShape, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCapsuleShape(
    QCapsuleShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCapsuleShape *>(self)->take(key, call);
}

//  bool QCapsuleShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QCapsuleShape13isStaticShapeEv(
    const QCapsuleShape *self) {
  return self->QCapsuleShape::isStaticShape();
}
