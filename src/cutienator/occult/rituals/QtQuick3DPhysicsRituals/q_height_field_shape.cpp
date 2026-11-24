//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qheightfieldshape_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qheightfieldshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QHeightFieldShape that Python can take functions over in. Every QHeightFieldShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQHeightFieldShapeCall0)(const void *, int *);
typedef void (*CuteQHeightFieldShapeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall4)(const void *, int *);
typedef void * (*CuteQHeightFieldShapeCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQHeightFieldShapeCall6)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQHeightFieldShapeCall7)(const void *, int *);
typedef void (*CuteQHeightFieldShapeCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightFieldShapeCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHeightFieldShapeCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeightFieldShapeCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHeightFieldShape : public QHeightFieldShape {
public:
  using QHeightFieldShape::QHeightFieldShape;
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

  //  bool QHeightFieldShape::isStaticShape() const
  bool isStaticShape() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeightFieldShapeCall0 call = reinterpret_cast<CuteQHeightFieldShapeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHeightFieldShape::isStaticShape();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQHeightFieldShapeCall1 call = reinterpret_cast<CuteQHeightFieldShapeCall1>(taken[1]);
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
      CuteQHeightFieldShapeCall2 call = reinterpret_cast<CuteQHeightFieldShapeCall2>(taken[2]);
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
      CuteQHeightFieldShapeCall3 call = reinterpret_cast<CuteQHeightFieldShapeCall3>(taken[3]);
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
      CuteQHeightFieldShapeCall4 call = reinterpret_cast<CuteQHeightFieldShapeCall4>(taken[4]);
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
      CuteQHeightFieldShapeCall5 call = reinterpret_cast<CuteQHeightFieldShapeCall5>(taken[5]);
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
      CuteQHeightFieldShapeCall6 call = reinterpret_cast<CuteQHeightFieldShapeCall6>(taken[6]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQHeightFieldShapeCall7 call = reinterpret_cast<CuteQHeightFieldShapeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQHeightFieldShapeCall8 call = reinterpret_cast<CuteQHeightFieldShapeCall8>(taken[8]);
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
      CuteQHeightFieldShapeCall9 call = reinterpret_cast<CuteQHeightFieldShapeCall9>(taken[9]);
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
      CuteQHeightFieldShapeCall10 call = reinterpret_cast<CuteQHeightFieldShapeCall10>(taken[10]);
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
      CuteQHeightFieldShapeCall11 call = reinterpret_cast<CuteQHeightFieldShapeCall11>(taken[11]);
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
      CuteQHeightFieldShapeCall12 call = reinterpret_cast<CuteQHeightFieldShapeCall12>(taken[12]);
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
      CuteQHeightFieldShapeCall13 call = reinterpret_cast<CuteQHeightFieldShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHeightFieldShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHeightFieldShape10metaObjectEv(
    const QHeightFieldShape *self) {
  return self->metaObject();
}

//  QString QHeightFieldShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QHeightFieldShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeightFieldShape::tr(s, c, n));
}

//  QHeightFieldShape::QHeightFieldShape()
extern "C" Q_DECL_EXPORT
QHeightFieldShape *ritual_ZN17QHeightFieldShapeC1Ev() {
  return new CuteQHeightFieldShape();
}

//  QHeightFieldShape::~QHeightFieldShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShapeD1Ev(QHeightFieldShape *self) {
  delete self;
}

//  const QUrl &QHeightFieldShape::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QHeightFieldShape6sourceEv(const QHeightFieldShape *self) {
  return new QUrl(self->source());
}

//  void QHeightFieldShape::setSource(const QUrl &newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape9setSourceERK4QUrl(
    QHeightFieldShape *self,
    const QUrl *newSource) {
  self->setSource(*newSource);
}

//  const QVector3D &QHeightFieldShape::hfOffset() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QHeightFieldShape8hfOffsetEv(
    const QHeightFieldShape *self) {
  return new QVector3D(self->hfOffset());
}

//  const QVector3D &QHeightFieldShape::extents() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QHeightFieldShape7extentsEv(
    const QHeightFieldShape *self) {
  return new QVector3D(self->extents());
}

//  void QHeightFieldShape::setExtents(const QVector3D &newExtents)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape10setExtentsERK9QVector3D(
    QHeightFieldShape *self,
    const QVector3D *newExtents) {
  self->setExtents(*newExtents);
}

//  bool QHeightFieldShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHeightFieldShape13isStaticShapeEv(
    const QHeightFieldShape *self) {
  return self->isStaticShape();
}

//  QQuickImage *QHeightFieldShape::image() const
extern "C" Q_DECL_EXPORT
QQuickImage *ritual_ZNK17QHeightFieldShape5imageEv(
    const QHeightFieldShape *self) {
  return self->image();
}

//  void QHeightFieldShape::setImage(QQuickImage *newImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape8setImageEP11QQuickImage(
    QHeightFieldShape *self,
    QQuickImage *newImage) {
  self->setImage(newImage);
}

//  void QHeightFieldShape::imageDestroyed(QObject *image)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape14imageDestroyedEP7QObject(
    QHeightFieldShape *self,
    QObject *image) {
  self->imageDestroyed(image);
}

//  void QHeightFieldShape::imageGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape20imageGeometryChangedEv(
    QHeightFieldShape *self) {
  self->imageGeometryChanged();
}

//  void QHeightFieldShape::updatePhysXGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape19updatePhysXGeometryEv(
    QHeightFieldShape *self) {
  self->updatePhysXGeometry();
}

//  void QHeightFieldShape::updateExtents()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHeightFieldShape13updateExtentsEv(QHeightFieldShape *self) {
  self->updateExtents();
}

//  a Python function taken by a CuteQHeightFieldShape, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeightFieldShape(
    QHeightFieldShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeightFieldShape *>(self)->take(key, call);
}

//  bool QHeightFieldShape::isStaticShape() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHeightFieldShape13isStaticShapeEv(
    const QHeightFieldShape *self) {
  return self->QHeightFieldShape::isStaticShape();
}
