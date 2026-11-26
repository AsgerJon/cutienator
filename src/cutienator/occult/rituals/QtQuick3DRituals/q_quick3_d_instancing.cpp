//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dinstancing.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dinstancing.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DInstancing may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DInstancing : QQuick3DInstancing {
  using QQuick3DInstancing::updateSpatialNode;
};

//  A QQuick3DInstancing that Python can take functions over in. Every QQuick3DInstancing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DInstancingCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DInstancingCall1)(const void *, int *);
typedef void (*CuteQQuick3DInstancingCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DInstancingCall3)(const void *, int *);
typedef void (*CuteQQuick3DInstancingCall4)(const void *, int *);
typedef void (*CuteQQuick3DInstancingCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstancingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DInstancingCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstancingCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstancingCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstancingCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstancingCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DInstancingCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DInstancing : public QQuick3DInstancing {
public:
  using QQuick3DInstancing::QQuick3DInstancing;
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
      CuteQQuick3DInstancingCall0 call = reinterpret_cast<CuteQQuick3DInstancingCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstancing::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DInstancingCall1 call = reinterpret_cast<CuteQQuick3DInstancingCall1>(taken[1]);
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
      CuteQQuick3DInstancingCall2 call = reinterpret_cast<CuteQQuick3DInstancingCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DInstancingCall3 call = reinterpret_cast<CuteQQuick3DInstancingCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DInstancingCall4 call = reinterpret_cast<CuteQQuick3DInstancingCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DInstancingCall5 call = reinterpret_cast<CuteQQuick3DInstancingCall5>(taken[5]);
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
      CuteQQuick3DInstancingCall6 call = reinterpret_cast<CuteQQuick3DInstancingCall6>(taken[6]);
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
      CuteQQuick3DInstancingCall7 call = reinterpret_cast<CuteQQuick3DInstancingCall7>(taken[7]);
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
      CuteQQuick3DInstancingCall8 call = reinterpret_cast<CuteQQuick3DInstancingCall8>(taken[8]);
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
      CuteQQuick3DInstancingCall9 call = reinterpret_cast<CuteQQuick3DInstancingCall9>(taken[9]);
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
      CuteQQuick3DInstancingCall10 call = reinterpret_cast<CuteQQuick3DInstancingCall10>(taken[10]);
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
      CuteQQuick3DInstancingCall11 call = reinterpret_cast<CuteQQuick3DInstancingCall11>(taken[11]);
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
      CuteQQuick3DInstancingCall12 call = reinterpret_cast<CuteQQuick3DInstancingCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DInstancing::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuick3DInstancing10metaObjectEv(
    const QQuick3DInstancing *self) {
  return self->metaObject();
}

//  void *QQuick3DInstancing::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuick3DInstancing11qt_metacastEPKc(
    QQuick3DInstancing *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DInstancing::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuick3DInstancing11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DInstancing *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DInstancing::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuick3DInstancing2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DInstancing::tr(s, c, n));
}

//  QQuick3DInstancingPrivate *QQuick3DInstancing::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DInstancingPrivate *ritual_ZN18QQuick3DInstancing6d_funcEv(
    QQuick3DInstancing *self) {
  return self->d_func();
}

//  const QQuick3DInstancingPrivate *QQuick3DInstancing::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DInstancingPrivate *ritual_ZNK18QQuick3DInstancing6d_funcEv(
    const QQuick3DInstancing *self) {
  return self->d_func();
}

//  void QQuick3DInstancing::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing24qt_qmlMarker_uncreatableEv(
    QQuick3DInstancing *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DInstancing::~QQuick3DInstancing()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancingD1Ev(QQuick3DInstancing *self) {
  delete self;
}

//  QByteArray QQuick3DInstancing::instanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QQuick3DInstancing14instanceBufferEPi(
    QQuick3DInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->instanceBuffer(instanceCount));
}

//  int QQuick3DInstancing::instanceCountOverride() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuick3DInstancing21instanceCountOverrideEv(
    const QQuick3DInstancing *self) {
  return self->instanceCountOverride();
}

//  bool QQuick3DInstancing::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuick3DInstancing15hasTransparencyEv(
    const QQuick3DInstancing *self) {
  return self->hasTransparency();
}

//  bool QQuick3DInstancing::depthSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuick3DInstancing19depthSortingEnabledEv(
    const QQuick3DInstancing *self) {
  return self->depthSortingEnabled();
}

//  QVector3D QQuick3DInstancing::shadowBoundsMinimum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DInstancing19shadowBoundsMinimumEv(
    const QQuick3DInstancing *self) {
  return new QVector3D(self->shadowBoundsMinimum());
}

//  QVector3D QQuick3DInstancing::shadowBoundsMaximum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DInstancing19shadowBoundsMaximumEv(
    const QQuick3DInstancing *self) {
  return new QVector3D(self->shadowBoundsMaximum());
}

//  QVector3D QQuick3DInstancing::instancePosition(int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN18QQuick3DInstancing16instancePositionEi(
    QQuick3DInstancing *self,
    int index) {
  return new QVector3D(self->instancePosition(index));
}

//  QVector3D QQuick3DInstancing::instanceScale(int index)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN18QQuick3DInstancing13instanceScaleEi(
    QQuick3DInstancing *self,
    int index) {
  return new QVector3D(self->instanceScale(index));
}

//  QQuaternion QQuick3DInstancing::instanceRotation(int index)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN18QQuick3DInstancing16instanceRotationEi(
    QQuick3DInstancing *self,
    int index) {
  return new QQuaternion(self->instanceRotation(index));
}

//  QColor QQuick3DInstancing::instanceColor(int index)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN18QQuick3DInstancing13instanceColorEi(
    QQuick3DInstancing *self,
    int index) {
  return new QColor(self->instanceColor(index));
}

//  QVector4D QQuick3DInstancing::instanceCustomData(int index)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN18QQuick3DInstancing18instanceCustomDataEi(
    QQuick3DInstancing *self,
    int index) {
  return new QVector4D(self->instanceCustomData(index));
}

//  void QQuick3DInstancing::setInstanceCountOverride(int
//      instanceCountOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing24setInstanceCountOverrideEi(
    QQuick3DInstancing *self,
    int instanceCountOverride) {
  self->setInstanceCountOverride(instanceCountOverride);
}

//  void QQuick3DInstancing::setHasTransparency(bool hasTransparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing18setHasTransparencyEb(
    QQuick3DInstancing *self,
    bool hasTransparency) {
  self->setHasTransparency(hasTransparency);
}

//  void QQuick3DInstancing::setDepthSortingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing22setDepthSortingEnabledEb(
    QQuick3DInstancing *self,
    bool enabled) {
  self->setDepthSortingEnabled(enabled);
}

//  void QQuick3DInstancing::setShadowBoundsMinimum(const QVector3D
//      &newShadowBoundsMinimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing22setShadowBoundsMinimumERK9QVector3D(
    QQuick3DInstancing *self,
    const QVector3D *newShadowBoundsMinimum) {
  self->setShadowBoundsMinimum(*newShadowBoundsMinimum);
}

//  void QQuick3DInstancing::setShadowBoundsMaximum(const QVector3D
//      &newShadowBoundsMinimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing22setShadowBoundsMaximumERK9QVector3D(
    QQuick3DInstancing *self,
    const QVector3D *newShadowBoundsMinimum) {
  self->setShadowBoundsMaximum(*newShadowBoundsMinimum);
}

//  void QQuick3DInstancing::instanceTableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing20instanceTableChangedEv(
    QQuick3DInstancing *self) {
  self->instanceTableChanged();
}

//  void QQuick3DInstancing::instanceNodeDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing17instanceNodeDirtyEv(
    QQuick3DInstancing *self) {
  self->instanceNodeDirty();
}

//  void QQuick3DInstancing::instanceCountOverrideChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing28instanceCountOverrideChangedEv(
    QQuick3DInstancing *self) {
  self->instanceCountOverrideChanged();
}

//  void QQuick3DInstancing::hasTransparencyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing22hasTransparencyChangedEv(
    QQuick3DInstancing *self) {
  self->hasTransparencyChanged();
}

//  void QQuick3DInstancing::depthSortingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing26depthSortingEnabledChangedEv(
    QQuick3DInstancing *self) {
  self->depthSortingEnabledChanged();
}

//  void QQuick3DInstancing::shadowBoundsMinimumChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing26shadowBoundsMinimumChangedEv(
    QQuick3DInstancing *self) {
  self->shadowBoundsMinimumChanged();
}

//  void QQuick3DInstancing::shadowBoundsMaximumChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing26shadowBoundsMaximumChangedEv(
    QQuick3DInstancing *self) {
  self->shadowBoundsMaximumChanged();
}

//  QByteArray QQuick3DInstancing::getInstanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QQuick3DInstancing17getInstanceBufferEPi(
    QQuick3DInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

//  void QQuick3DInstancing::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing9markDirtyEv(QQuick3DInstancing *self) {
  self->markDirty();
}

//  InstanceTableEntry QQuick3DInstancing::calculateTableEntry(const
//      QVector3D &position, const QVector3D &scale, const QVector3D
//      &eulerRotation, const QColor &color, const QVector4D &customData)
extern "C" Q_DECL_EXPORT
QQuick3DInstancing::InstanceTableEntry *ritual_ZN18QQuick3DInstancing19calculateTableEntryERK9QVector3DS2_S2_RK6QColorRK9QVector4D(
    const QVector3D *position,
    const QVector3D *scale,
    const QVector3D *eulerRotation,
    const QColor *color,
    const QVector4D *customData) {
  return new QQuick3DInstancing::InstanceTableEntry(
      QQuick3DInstancing::calculateTableEntry(
          *position,
          *scale,
          *eulerRotation,
          *color,
          *customData));
}

//  InstanceTableEntry
//      QQuick3DInstancing::calculateTableEntryFromQuaternion(const QVector3D
//      &position, const QVector3D &scale, const QQuaternion &rotation, const
//      QColor &color, const QVector4D &customData)
extern "C" Q_DECL_EXPORT
QQuick3DInstancing::InstanceTableEntry *ritual_ZN18QQuick3DInstancing33calculateTableEntryFromQuaternionERK9QVector3DS2_RK11QQuaternionRK6QColorRK9QVector4D(
    const QVector3D *position,
    const QVector3D *scale,
    const QQuaternion *rotation,
    const QColor *color,
    const QVector4D *customData) {
  return new QQuick3DInstancing::InstanceTableEntry(
      QQuick3DInstancing::calculateTableEntryFromQuaternion(
          *position,
          *scale,
          *rotation,
          *color,
          *customData));
}

//  QSSGRenderGraphObject
//      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN18QQuick3DInstancing17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstancing *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  const InstanceTableEntry *QQuick3DInstancing::getInstanceEntry(int index)
extern "C" Q_DECL_EXPORT
const QQuick3DInstancing::InstanceTableEntry *ritual_ZN18QQuick3DInstancing16getInstanceEntryEi(
    QQuick3DInstancing *self,
    int index) {
  return self->getInstanceEntry(index);
}

//  a Python function taken by a CuteQQuick3DInstancing, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DInstancing(
    QQuick3DInstancing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DInstancing *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN18QQuick3DInstancing17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DInstancing *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DInstancing *>(self)->OwnQQuick3DInstancing::updateSpatialNode(
      node);
}
