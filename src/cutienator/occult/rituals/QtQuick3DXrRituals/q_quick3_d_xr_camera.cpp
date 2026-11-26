//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcamera_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DXrCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DXrCamera : QQuick3DXrCamera {
  using QQuick3DXrCamera::itemChange;
};

//  A QQuick3DXrCamera that Python can take functions over in. Every QQuick3DXrCamera
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrCameraCall0)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DXrCameraCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall4)(const void *, int *);
typedef void * (*CuteQQuick3DXrCameraCall5)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DXrCameraCall6)(const void *, int *);
typedef void (*CuteQQuick3DXrCameraCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrCameraCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrCameraCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrCameraCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrCamera : public QQuick3DXrCamera {
public:
  using QQuick3DXrCamera::QQuick3DXrCamera;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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

  //  void QQuick3DXrCamera::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuick3DObject::ItemChange change,
      const QQuick3DObject::ItemChangeData &data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrCameraCall0 call = reinterpret_cast<CuteQQuick3DXrCameraCall0>(taken[0]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuick3DXrCamera::itemChange(change, data);
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrCameraCall1 call = reinterpret_cast<CuteQQuick3DXrCameraCall1>(taken[1]);
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
      CuteQQuick3DXrCameraCall2 call = reinterpret_cast<CuteQQuick3DXrCameraCall2>(taken[2]);
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
      CuteQQuick3DXrCameraCall3 call = reinterpret_cast<CuteQQuick3DXrCameraCall3>(taken[3]);
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
      CuteQQuick3DXrCameraCall4 call = reinterpret_cast<CuteQQuick3DXrCameraCall4>(taken[4]);
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
      CuteQQuick3DXrCameraCall5 call = reinterpret_cast<CuteQQuick3DXrCameraCall5>(taken[5]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrCameraCall6 call = reinterpret_cast<CuteQQuick3DXrCameraCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrCameraCall7 call = reinterpret_cast<CuteQQuick3DXrCameraCall7>(taken[7]);
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
      CuteQQuick3DXrCameraCall8 call = reinterpret_cast<CuteQQuick3DXrCameraCall8>(taken[8]);
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
      CuteQQuick3DXrCameraCall9 call = reinterpret_cast<CuteQQuick3DXrCameraCall9>(taken[9]);
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
      CuteQQuick3DXrCameraCall10 call = reinterpret_cast<CuteQQuick3DXrCameraCall10>(taken[10]);
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
      CuteQQuick3DXrCameraCall11 call = reinterpret_cast<CuteQQuick3DXrCameraCall11>(taken[11]);
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
      CuteQQuick3DXrCameraCall12 call = reinterpret_cast<CuteQQuick3DXrCameraCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DXrCamera10metaObjectEv(
    const QQuick3DXrCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DXrCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuick3DXrCamera11qt_metacastEPKc(
    QQuick3DXrCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrCamera::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DXrCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DXrCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrCamera::tr(s, c, n));
}

//  QQuick3DXrCamera::QQuick3DXrCamera(QQuick3DXrOrigin *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrCamera *ritual_ZN16QQuick3DXrCameraC1EP16QQuick3DXrOrigin(
    QQuick3DXrOrigin *parent) {
  return new CuteQQuick3DXrCamera(parent);
}

//  QQuick3DXrCamera::~QQuick3DXrCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCameraD1Ev(QQuick3DXrCamera *self) {
  delete self;
}

//  float QQuick3DXrCamera::clipNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuick3DXrCamera8clipNearEv(const QQuick3DXrCamera *self) {
  return self->clipNear();
}

//  float QQuick3DXrCamera::clipFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQuick3DXrCamera7clipFarEv(const QQuick3DXrCamera *self) {
  return self->clipFar();
}

//  void QQuick3DXrCamera::setClipNear(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera11setClipNearEf(
    QQuick3DXrCamera *self,
    float clipNear) {
  self->setClipNear(clipNear);
}

//  void QQuick3DXrCamera::setClipFar(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera10setClipFarEf(
    QQuick3DXrCamera *self,
    float clipFar) {
  self->setClipFar(clipFar);
}

//  void QQuick3DXrCamera::clipNearChanged(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera15clipNearChangedEf(
    QQuick3DXrCamera *self,
    float clipNear) {
  self->clipNearChanged(clipNear);
}

//  void QQuick3DXrCamera::clipFarChanged(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera14clipFarChangedEf(
    QQuick3DXrCamera *self,
    float clipFar) {
  self->clipFarChanged(clipFar);
}

//  void QQuick3DXrCamera::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DXrCamera *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuick3DXrCamera::syncCameraSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrCamera18syncCameraSettingsEv(
    QQuick3DXrCamera *self) {
  self->syncCameraSettings();
}

//  a Python function taken by a CuteQQuick3DXrCamera, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrCamera(
    QQuick3DXrCamera *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrCamera *>(self)->take(key, call);
}

//  void QQuick3DXrCamera::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DXrCamera10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DXrCamera *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *data) {
  static_cast<OwnQQuick3DXrCamera *>(self)->OwnQQuick3DXrCamera::itemChange(
      change,
      *data);
}
