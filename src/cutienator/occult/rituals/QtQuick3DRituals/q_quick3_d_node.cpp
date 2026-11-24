//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuick3DNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DNode : QQuick3DNode {
  using QQuick3DNode::connectNotify;
  using QQuick3DNode::disconnectNotify;
  using QQuick3DNode::componentComplete;
  using QQuick3DNode::updateSpatialNode;
  using QQuick3DNode::itemChange;
};

//  A QQuick3DNode that Python can take functions over in. Every QQuick3DNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DNodeCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall3)(const void *, int *);
typedef void * (*CuteQQuick3DNodeCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DNodeCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DNodeCall6)(const void *, int *);
typedef void (*CuteQQuick3DNodeCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DNodeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DNodeCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DNodeCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DNode : public QQuick3DNode {
public:
  using QQuick3DNode::QQuick3DNode;
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
      CuteQQuick3DNodeCall0 call = reinterpret_cast<CuteQQuick3DNodeCall0>(taken[0]);
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
      CuteQQuick3DNodeCall1 call = reinterpret_cast<CuteQQuick3DNodeCall1>(taken[1]);
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
      CuteQQuick3DNodeCall2 call = reinterpret_cast<CuteQQuick3DNodeCall2>(taken[2]);
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
      CuteQQuick3DNodeCall3 call = reinterpret_cast<CuteQQuick3DNodeCall3>(taken[3]);
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
      CuteQQuick3DNodeCall4 call = reinterpret_cast<CuteQQuick3DNodeCall4>(taken[4]);
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
      CuteQQuick3DNodeCall5 call = reinterpret_cast<CuteQQuick3DNodeCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DNodeCall6 call = reinterpret_cast<CuteQQuick3DNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DNodeCall7 call = reinterpret_cast<CuteQQuick3DNodeCall7>(taken[7]);
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
      CuteQQuick3DNodeCall8 call = reinterpret_cast<CuteQQuick3DNodeCall8>(taken[8]);
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
      CuteQQuick3DNodeCall9 call = reinterpret_cast<CuteQQuick3DNodeCall9>(taken[9]);
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
      CuteQQuick3DNodeCall10 call = reinterpret_cast<CuteQQuick3DNodeCall10>(taken[10]);
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
      CuteQQuick3DNodeCall11 call = reinterpret_cast<CuteQQuick3DNodeCall11>(taken[11]);
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
      CuteQQuick3DNodeCall12 call = reinterpret_cast<CuteQQuick3DNodeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuick3DNode10metaObjectEv(
    const QQuick3DNode *self) {
  return self->metaObject();
}

//  QString QQuick3DNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuick3DNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DNode::tr(s, c, n));
}

//  QQuick3DNode::QQuick3DNode(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN12QQuick3DNodeC1EPS_(QQuick3DNode *parent) {
  return new CuteQQuick3DNode(parent);
}

//  QQuick3DNode::~QQuick3DNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNodeD1Ev(QQuick3DNode *self) {
  delete self;
}

//  float QQuick3DNode::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QQuick3DNode1xEv(const QQuick3DNode *self) {
  return self->x();
}

//  float QQuick3DNode::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QQuick3DNode1yEv(const QQuick3DNode *self) {
  return self->y();
}

//  float QQuick3DNode::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QQuick3DNode1zEv(const QQuick3DNode *self) {
  return self->z();
}

//  QQuaternion QQuick3DNode::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK12QQuick3DNode8rotationEv(const QQuick3DNode *self) {
  return new QQuaternion(self->rotation());
}

//  QVector3D QQuick3DNode::eulerRotation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode13eulerRotationEv(
    const QQuick3DNode *self) {
  return new QVector3D(self->eulerRotation());
}

//  QVector3D QQuick3DNode::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode8positionEv(const QQuick3DNode *self) {
  return new QVector3D(self->position());
}

//  QVector3D QQuick3DNode::scale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode5scaleEv(const QQuick3DNode *self) {
  return new QVector3D(self->scale());
}

//  QVector3D QQuick3DNode::pivot() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode5pivotEv(const QQuick3DNode *self) {
  return new QVector3D(self->pivot());
}

//  float QQuick3DNode::localOpacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QQuick3DNode12localOpacityEv(const QQuick3DNode *self) {
  return self->localOpacity();
}

//  bool QQuick3DNode::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuick3DNode7visibleEv(const QQuick3DNode *self) {
  return self->visible();
}

//  int QQuick3DNode::staticFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuick3DNode11staticFlagsEv(const QQuick3DNode *self) {
  return self->staticFlags();
}

//  QQuick3DNode *QQuick3DNode::parentNode() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK12QQuick3DNode10parentNodeEv(
    const QQuick3DNode *self) {
  return self->parentNode();
}

//  QVector3D QQuick3DNode::forward() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode7forwardEv(const QQuick3DNode *self) {
  return new QVector3D(self->forward());
}

//  QVector3D QQuick3DNode::up() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode2upEv(const QQuick3DNode *self) {
  return new QVector3D(self->up());
}

//  QVector3D QQuick3DNode::right() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode5rightEv(const QQuick3DNode *self) {
  return new QVector3D(self->right());
}

//  QVector3D QQuick3DNode::scenePosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode13scenePositionEv(
    const QQuick3DNode *self) {
  return new QVector3D(self->scenePosition());
}

//  QQuaternion QQuick3DNode::sceneRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK12QQuick3DNode13sceneRotationEv(
    const QQuick3DNode *self) {
  return new QQuaternion(self->sceneRotation());
}

//  QVector3D QQuick3DNode::sceneScale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode10sceneScaleEv(const QQuick3DNode *self) {
  return new QVector3D(self->sceneScale());
}

//  QMatrix4x4 QQuick3DNode::sceneTransform() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK12QQuick3DNode14sceneTransformEv(
    const QQuick3DNode *self) {
  return new QMatrix4x4(self->sceneTransform());
}

//  void QQuick3DNode::rotate(qreal degrees, const QVector3D &axis,
//      QQuick3DNode::TransformSpace space)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode6rotateEdRK9QVector3DNS_14TransformSpaceE(
    QQuick3DNode *self,
    qreal degrees,
    const QVector3D *axis,
    QQuick3DNode::TransformSpace space) {
  self->rotate(degrees, *axis, space);
}

//  QVector3D QQuick3DNode::mapPositionToScene(const QVector3D
//      &localPosition) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode18mapPositionToSceneERK9QVector3D(
    const QQuick3DNode *self,
    const QVector3D *localPosition) {
  return new QVector3D(self->mapPositionToScene(*localPosition));
}

//  QVector3D QQuick3DNode::mapPositionFromScene(const QVector3D
//      &scenePosition) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode20mapPositionFromSceneERK9QVector3D(
    const QQuick3DNode *self,
    const QVector3D *scenePosition) {
  return new QVector3D(self->mapPositionFromScene(*scenePosition));
}

//  QVector3D QQuick3DNode::mapPositionToNode(const QQuick3DNode *node, const
//      QVector3D &localPosition) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode17mapPositionToNodeEPKS_RK9QVector3D(
    const QQuick3DNode *self,
    const QQuick3DNode *node,
    const QVector3D *localPosition) {
  return new QVector3D(self->mapPositionToNode(node, *localPosition));
}

//  QVector3D QQuick3DNode::mapPositionFromNode(const QQuick3DNode *node,
//      const QVector3D &localPosition) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode19mapPositionFromNodeEPKS_RK9QVector3D(
    const QQuick3DNode *self,
    const QQuick3DNode *node,
    const QVector3D *localPosition) {
  return new QVector3D(self->mapPositionFromNode(node, *localPosition));
}

//  QVector3D QQuick3DNode::mapDirectionToScene(const QVector3D
//      &localDirection) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode19mapDirectionToSceneERK9QVector3D(
    const QQuick3DNode *self,
    const QVector3D *localDirection) {
  return new QVector3D(self->mapDirectionToScene(*localDirection));
}

//  QVector3D QQuick3DNode::mapDirectionFromScene(const QVector3D
//      &sceneDirection) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode21mapDirectionFromSceneERK9QVector3D(
    const QQuick3DNode *self,
    const QVector3D *sceneDirection) {
  return new QVector3D(self->mapDirectionFromScene(*sceneDirection));
}

//  QVector3D QQuick3DNode::mapDirectionToNode(const QQuick3DNode *node,
//      const QVector3D &localDirection) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode18mapDirectionToNodeEPKS_RK9QVector3D(
    const QQuick3DNode *self,
    const QQuick3DNode *node,
    const QVector3D *localDirection) {
  return new QVector3D(self->mapDirectionToNode(node, *localDirection));
}

//  QVector3D QQuick3DNode::mapDirectionFromNode(const QQuick3DNode *node,
//      const QVector3D &localDirection) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK12QQuick3DNode20mapDirectionFromNodeEPKS_RK9QVector3D(
    const QQuick3DNode *self,
    const QQuick3DNode *node,
    const QVector3D *localDirection) {
  return new QVector3D(self->mapDirectionFromNode(node, *localDirection));
}

//  void QQuick3DNode::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode12markAllDirtyEv(QQuick3DNode *self) {
  self->markAllDirty();
}

//  int QQuick3DNode::layers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuick3DNode6layersEv(const QQuick3DNode *self) {
  return self->layers();
}

//  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode13connectNotifyERK11QMetaMethod(
    QQuick3DNode *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode16disconnectNotifyERK11QMetaMethod(
    QQuick3DNode *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  void QQuick3DNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode17componentCompleteEv(QQuick3DNode *self) {
  self->componentComplete();
}

//  void QQuick3DNode::setX(float x)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode4setXEf(QQuick3DNode *self, float x) {
  self->setX(x);
}

//  void QQuick3DNode::setY(float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode4setYEf(QQuick3DNode *self, float y) {
  self->setY(y);
}

//  void QQuick3DNode::setZ(float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode4setZEf(QQuick3DNode *self, float z) {
  self->setZ(z);
}

//  void QQuick3DNode::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode11setRotationERK11QQuaternion(
    QQuick3DNode *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  void QQuick3DNode::setEulerRotation(const QVector3D &eulerRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode16setEulerRotationERK9QVector3D(
    QQuick3DNode *self,
    const QVector3D *eulerRotation) {
  self->setEulerRotation(*eulerRotation);
}

//  void QQuick3DNode::setPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode11setPositionERK9QVector3D(
    QQuick3DNode *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  void QQuick3DNode::setScale(const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode8setScaleERK9QVector3D(
    QQuick3DNode *self,
    const QVector3D *scale) {
  self->setScale(*scale);
}

//  void QQuick3DNode::setPivot(const QVector3D &pivot)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode8setPivotERK9QVector3D(
    QQuick3DNode *self,
    const QVector3D *pivot) {
  self->setPivot(*pivot);
}

//  void QQuick3DNode::setLocalOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode15setLocalOpacityEf(
    QQuick3DNode *self,
    float opacity) {
  self->setLocalOpacity(opacity);
}

//  void QQuick3DNode::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode10setVisibleEb(
    QQuick3DNode *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QQuick3DNode::setStaticFlags(int staticFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode14setStaticFlagsEi(
    QQuick3DNode *self,
    int staticFlags) {
  self->setStaticFlags(staticFlags);
}

//  void QQuick3DNode::setLayers(int newLayers)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode9setLayersEi(QQuick3DNode *self, int newLayers) {
  self->setLayers(newLayers);
}

//  QSSGRenderGraphObject
//      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN12QQuick3DNode17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DNode *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuick3DNode10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DNode *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  QQuick3DNodePrivate *QQuick3DNode::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DNodePrivate *ritual_ZN12QQuick3DNode6d_funcEv(QQuick3DNode *self) {
  return self->d_func();
}

//  const QQuick3DNodePrivate *QQuick3DNode::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DNodePrivate *ritual_ZNK12QQuick3DNode6d_funcEv(
    const QQuick3DNode *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuick3DNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DNode(
    QQuick3DNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DNode *>(self)->take(key, call);
}

//  void QQuick3DNode::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuick3DNode12markAllDirtyEv(QQuick3DNode *self) {
  self->QQuick3DNode::markAllDirty();
}

//  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuick3DNode13connectNotifyERK11QMetaMethod(
    QQuick3DNode *self,
    const QMetaMethod *signal) {
  static_cast<OwnQQuick3DNode *>(self)->OwnQQuick3DNode::connectNotify(
      *signal);
}

//  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuick3DNode16disconnectNotifyERK11QMetaMethod(
    QQuick3DNode *self,
    const QMetaMethod *signal) {
  static_cast<OwnQQuick3DNode *>(self)->OwnQQuick3DNode::disconnectNotify(
      *signal);
}

//  void QQuick3DNode::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuick3DNode17componentCompleteEv(QQuick3DNode *self) {
  static_cast<OwnQQuick3DNode *>(self)->OwnQQuick3DNode::componentComplete();
}

//  QSSGRenderGraphObject
//      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN12QQuick3DNode17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DNode *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DNode *>(self)->OwnQQuick3DNode::updateSpatialNode(
      node);
}

//  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuick3DNode10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DNode *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DNode *>(self)->OwnQQuick3DNode::itemChange(a0, *a1);
}

//  QList<QQuick3DNode *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuick3DNode *> *ritual_list_make_QQuick3DNode_ptr() {
  return new QList<QQuick3DNode *>();
}

//  void QList<QQuick3DNode *>::append(const QQuick3DNode * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuick3DNode_ptr(
    QList<QQuick3DNode *> *self,
    QQuick3DNode *element) {
  self->append(element);
}

//  qsizetype QList<QQuick3DNode *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuick3DNode_ptr(
    const QList<QQuick3DNode *> *self) {
  return self->size();
}

//  const QQuick3DNode * &QList<QQuick3DNode *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_list_at_QQuick3DNode_ptr(
    const QList<QQuick3DNode *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuick3DNode *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuick3DNode_ptr(QList<QQuick3DNode *> *self) {
  delete self;
}
