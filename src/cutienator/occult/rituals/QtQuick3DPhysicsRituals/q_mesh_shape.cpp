//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qmeshshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qmeshshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QMeshShape that Python can take functions over in. Every QMeshShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQMeshShapeCall0)(const void *, int *);
typedef void * (*CuteQMeshShapeCall1)(const void *, int *);
typedef bool (*CuteQMeshShapeCall2)(const void *, int *);
typedef void (*CuteQMeshShapeCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall6)(const void *, int *);
typedef void * (*CuteQMeshShapeCall7)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQMeshShapeCall8)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQMeshShapeCall9)(const void *, int *);
typedef void (*CuteQMeshShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMeshShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMeshShapeCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMeshShapeCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMeshShape : public QMeshShape {
public:
  using QMeshShape::QMeshShape;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QMeshShape9shapeTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstractCollisionShape16getPhysXGeometryEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QAbstractCollisionShape13isStaticShapeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  MeshType QMeshShape::shapeType() const
  QMeshShape::MeshType shapeType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMeshShapeCall0 call = reinterpret_cast<CuteQMeshShapeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QMeshShape::MeshType>(given);
    }
    return {};
  }

  //  physx::PxGeometry *QMeshShape::getPhysXGeometry()
  physx::PxGeometry *getPhysXGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMeshShapeCall1 call = reinterpret_cast<CuteQMeshShapeCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<physx::PxGeometry *>(given);
    }
    return QMeshShape::getPhysXGeometry();
  }

  //  bool QAbstractCollisionShape::isStaticShape() const
  bool isStaticShape() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMeshShapeCall2 call = reinterpret_cast<CuteQMeshShapeCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMeshShapeCall3 call = reinterpret_cast<CuteQMeshShapeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMeshShapeCall4 call = reinterpret_cast<CuteQMeshShapeCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMeshShapeCall5 call = reinterpret_cast<CuteQMeshShapeCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQMeshShapeCall6 call = reinterpret_cast<CuteQMeshShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMeshShapeCall7 call = reinterpret_cast<CuteQMeshShapeCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQMeshShapeCall8 call = reinterpret_cast<CuteQMeshShapeCall8>(taken[8]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQMeshShapeCall9 call = reinterpret_cast<CuteQMeshShapeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMeshShapeCall10 call = reinterpret_cast<CuteQMeshShapeCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMeshShapeCall11 call = reinterpret_cast<CuteQMeshShapeCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMeshShapeCall12 call = reinterpret_cast<CuteQMeshShapeCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMeshShapeCall13 call = reinterpret_cast<CuteQMeshShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMeshShapeCall14 call = reinterpret_cast<CuteQMeshShapeCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQMeshShapeCall15 call = reinterpret_cast<CuteQMeshShapeCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMeshShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QMeshShape10metaObjectEv(
    const QMeshShape *self) {
  return self->metaObject();
}

//  void *QMeshShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QMeshShape11qt_metacastEPKc(
    QMeshShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMeshShape::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QMeshShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QMeshShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMeshShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QMeshShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMeshShape::tr(s, c, n));
}

//  void QMeshShape::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape24qt_qmlMarker_uncreatableEv(QMeshShape *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QMeshShape::~QMeshShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShapeD1Ev(QMeshShape *self) {
  delete self;
}

//  MeshType QMeshShape::shapeType() const
extern "C" Q_DECL_EXPORT
QMeshShape::MeshType ritual_ZNK10QMeshShape9shapeTypeEv(
    const QMeshShape *self) {
  return self->shapeType();
}

//  physx::PxGeometry *QMeshShape::getPhysXGeometry()
extern "C" Q_DECL_EXPORT
physx::PxGeometry *ritual_ZN10QMeshShape16getPhysXGeometryEv(
    QMeshShape *self) {
  return self->getPhysXGeometry();
}

//  const QUrl &QMeshShape::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QMeshShape6sourceEv(const QMeshShape *self) {
  return new QUrl(self->source());
}

//  void QMeshShape::setSource(const QUrl &newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape9setSourceERK4QUrl(
    QMeshShape *self,
    const QUrl *newSource) {
  self->setSource(*newSource);
}

//  QQuick3DGeometry *QMeshShape::geometry() const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry *ritual_ZNK10QMeshShape8geometryEv(const QMeshShape *self) {
  return self->geometry();
}

//  void QMeshShape::setGeometry(QQuick3DGeometry *newGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape11setGeometryEP16QQuick3DGeometry(
    QMeshShape *self,
    QQuick3DGeometry *newGeometry) {
  self->setGeometry(newGeometry);
}

//  void QMeshShape::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape13sourceChangedEv(QMeshShape *self) {
  self->sourceChanged();
}

//  void QMeshShape::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape15geometryChangedEv(QMeshShape *self) {
  self->geometryChanged();
}

//  void QMeshShape::geometryDestroyed(QObject *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape17geometryDestroyedEP7QObject(
    QMeshShape *self,
    QObject *geometry) {
  self->geometryDestroyed(geometry);
}

//  void QMeshShape::geometryContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape22geometryContentChangedEv(QMeshShape *self) {
  self->geometryContentChanged();
}

//  void QMeshShape::updatePhysXGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMeshShape19updatePhysXGeometryEv(QMeshShape *self) {
  self->updatePhysXGeometry();
}

//  a Python function taken by a CuteQMeshShape, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMeshShape(QMeshShape *self, const char *key, void *call) {
  return static_cast<CuteQMeshShape *>(self)->take(key, call);
}

//  physx::PxGeometry *QMeshShape::getPhysXGeometry()
extern "C" Q_DECL_EXPORT
physx::PxGeometry *ritual_own_ZN10QMeshShape16getPhysXGeometryEv(
    QMeshShape *self) {
  return self->QMeshShape::getPhysXGeometry();
}
