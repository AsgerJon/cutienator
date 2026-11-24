//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrorigin_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrorigin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QQuick3DXrOrigin that Python can take functions over in. Every QQuick3DXrOrigin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrOriginCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall3)(const void *, int *);
typedef void * (*CuteQQuick3DXrOriginCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DXrOriginCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DXrOriginCall6)(const void *, int *);
typedef void (*CuteQQuick3DXrOriginCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrOriginCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrOriginCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrOriginCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrOrigin : public QQuick3DXrOrigin {
public:
  using QQuick3DXrOrigin::QQuick3DXrOrigin;
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
      CuteQQuick3DXrOriginCall0 call = reinterpret_cast<CuteQQuick3DXrOriginCall0>(taken[0]);
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
      CuteQQuick3DXrOriginCall1 call = reinterpret_cast<CuteQQuick3DXrOriginCall1>(taken[1]);
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
      CuteQQuick3DXrOriginCall2 call = reinterpret_cast<CuteQQuick3DXrOriginCall2>(taken[2]);
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
      CuteQQuick3DXrOriginCall3 call = reinterpret_cast<CuteQQuick3DXrOriginCall3>(taken[3]);
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
      CuteQQuick3DXrOriginCall4 call = reinterpret_cast<CuteQQuick3DXrOriginCall4>(taken[4]);
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
      CuteQQuick3DXrOriginCall5 call = reinterpret_cast<CuteQQuick3DXrOriginCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrOriginCall6 call = reinterpret_cast<CuteQQuick3DXrOriginCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrOriginCall7 call = reinterpret_cast<CuteQQuick3DXrOriginCall7>(taken[7]);
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
      CuteQQuick3DXrOriginCall8 call = reinterpret_cast<CuteQQuick3DXrOriginCall8>(taken[8]);
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
      CuteQQuick3DXrOriginCall9 call = reinterpret_cast<CuteQQuick3DXrOriginCall9>(taken[9]);
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
      CuteQQuick3DXrOriginCall10 call = reinterpret_cast<CuteQQuick3DXrOriginCall10>(taken[10]);
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
      CuteQQuick3DXrOriginCall11 call = reinterpret_cast<CuteQQuick3DXrOriginCall11>(taken[11]);
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
      CuteQQuick3DXrOriginCall12 call = reinterpret_cast<CuteQQuick3DXrOriginCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrOrigin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DXrOrigin10metaObjectEv(
    const QQuick3DXrOrigin *self) {
  return self->metaObject();
}

//  QString QQuick3DXrOrigin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DXrOrigin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrOrigin::tr(s, c, n));
}

//  QQuick3DXrOrigin::QQuick3DXrOrigin(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrOrigin *ritual_ZN16QQuick3DXrOriginC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DXrOrigin(parent);
}

//  QQuick3DXrOrigin::~QQuick3DXrOrigin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOriginD1Ev(QQuick3DXrOrigin *self) {
  delete self;
}

//  QQuick3DXrCamera *QQuick3DXrOrigin::camera() const
extern "C" Q_DECL_EXPORT
QQuick3DXrCamera *ritual_ZNK16QQuick3DXrOrigin6cameraEv(
    const QQuick3DXrOrigin *self) {
  return self->camera();
}

//  void QQuick3DXrOrigin::setCamera(QQuick3DXrCamera *newCamera)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOrigin9setCameraEP16QQuick3DXrCamera(
    QQuick3DXrOrigin *self,
    QQuick3DXrCamera *newCamera) {
  self->setCamera(newCamera);
}

//  QQuick3DXrEyeCamera *QQuick3DXrOrigin::eyeCamera(int index) const
extern "C" Q_DECL_EXPORT
QQuick3DXrEyeCamera *ritual_ZNK16QQuick3DXrOrigin9eyeCameraEi(
    const QQuick3DXrOrigin *self,
    int index) {
  return self->eyeCamera(index);
}

//  void QQuick3DXrOrigin::syncCameraSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOrigin18syncCameraSettingsEv(
    QQuick3DXrOrigin *self) {
  self->syncCameraSettings();
}

//  void QQuick3DXrOrigin::resetCameraSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOrigin19resetCameraSettingsEv(
    QQuick3DXrOrigin *self) {
  self->resetCameraSettings();
}

//  void QQuick3DXrOrigin::updateTrackedCamera(const QMatrix4x4 &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOrigin19updateTrackedCameraERK10QMatrix4x4(
    QQuick3DXrOrigin *self,
    const QMatrix4x4 *transform) {
  self->updateTrackedCamera(*transform);
}

//  void QQuick3DXrOrigin::updateTrackedCamera(QVector3D position,
//      QQuaternion rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DXrOrigin19updateTrackedCameraE9QVector3D11QQuaternion(
    QQuick3DXrOrigin *self,
    const QVector3D *position,
    const QQuaternion *rotation) {
  self->updateTrackedCamera(*position, *rotation);
}

//  a Python function taken by a CuteQQuick3DXrOrigin, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrOrigin(
    QQuick3DXrOrigin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrOrigin *>(self)->take(key, call);
}
