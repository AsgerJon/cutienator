//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3djoint_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3djoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DJoint may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DJoint : QQuick3DJoint {
  using QQuick3DJoint::updateSpatialNode;
  using QQuick3DJoint::markAllDirty;
};

//  A QQuick3DJoint that Python can take functions over in. Every QQuick3DJoint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DJointCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DJointCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall4)(const void *, int *);
typedef void (*CuteQQuick3DJointCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DJointCall6)(const void *, int *);
typedef void (*CuteQQuick3DJointCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DJointCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DJointCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DJointCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DJoint : public QQuick3DJoint {
public:
  using QQuick3DJoint::QQuick3DJoint;
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

  //  QSSGRenderGraphObject
  //      *QQuick3DJoint::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DJointCall0 call = reinterpret_cast<CuteQQuick3DJointCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DJoint::updateSpatialNode(node);
  }

  //  void QQuick3DJoint::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DJointCall1 call = reinterpret_cast<CuteQQuick3DJointCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DJoint::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DJointCall2 call = reinterpret_cast<CuteQQuick3DJointCall2>(taken[2]);
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
      CuteQQuick3DJointCall3 call = reinterpret_cast<CuteQQuick3DJointCall3>(taken[3]);
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
      CuteQQuick3DJointCall4 call = reinterpret_cast<CuteQQuick3DJointCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DJointCall5 call = reinterpret_cast<CuteQQuick3DJointCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DJointCall6 call = reinterpret_cast<CuteQQuick3DJointCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DJointCall7 call = reinterpret_cast<CuteQQuick3DJointCall7>(taken[7]);
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
      CuteQQuick3DJointCall8 call = reinterpret_cast<CuteQQuick3DJointCall8>(taken[8]);
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
      CuteQQuick3DJointCall9 call = reinterpret_cast<CuteQQuick3DJointCall9>(taken[9]);
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
      CuteQQuick3DJointCall10 call = reinterpret_cast<CuteQQuick3DJointCall10>(taken[10]);
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
      CuteQQuick3DJointCall11 call = reinterpret_cast<CuteQQuick3DJointCall11>(taken[11]);
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
      CuteQQuick3DJointCall12 call = reinterpret_cast<CuteQQuick3DJointCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DJoint::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuick3DJoint10metaObjectEv(
    const QQuick3DJoint *self) {
  return self->metaObject();
}

//  QString QQuick3DJoint::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuick3DJoint2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DJoint::tr(s, c, n));
}

//  QQuick3DJoint::QQuick3DJoint(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DJoint *ritual_ZN13QQuick3DJointC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DJoint(parent);
}

//  QQuick3DJoint::~QQuick3DJoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DJointD1Ev(QQuick3DJoint *self) {
  delete self;
}

//  qint32 QQuick3DJoint::index() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK13QQuick3DJoint5indexEv(const QQuick3DJoint *self) {
  return self->index();
}

//  QQuick3DSkeleton *QQuick3DJoint::skeletonRoot() const
extern "C" Q_DECL_EXPORT
QQuick3DSkeleton *ritual_ZNK13QQuick3DJoint12skeletonRootEv(
    const QQuick3DJoint *self) {
  return self->skeletonRoot();
}

//  void QQuick3DJoint::setIndex(qint32 index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DJoint8setIndexEi(QQuick3DJoint *self, qint32 index) {
  self->setIndex(index);
}

//  void QQuick3DJoint::setSkeletonRoot(QQuick3DSkeleton *skeleton)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DJoint15setSkeletonRootEP16QQuick3DSkeleton(
    QQuick3DJoint *self,
    QQuick3DSkeleton *skeleton) {
  self->setSkeletonRoot(skeleton);
}

//  QSSGRenderGraphObject
//      *QQuick3DJoint::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN13QQuick3DJoint17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DJoint *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DJoint::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuick3DJoint12markAllDirtyEv(QQuick3DJoint *self) {
  self->markAllDirty();
}

//  a Python function taken by a CuteQQuick3DJoint, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DJoint(
    QQuick3DJoint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DJoint *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DJoint::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN13QQuick3DJoint17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DJoint *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DJoint *>(self)->OwnQQuick3DJoint::updateSpatialNode(
      node);
}

//  void QQuick3DJoint::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuick3DJoint12markAllDirtyEv(QQuick3DJoint *self) {
  static_cast<OwnQQuick3DJoint *>(self)->OwnQQuick3DJoint::markAllDirty();
}
