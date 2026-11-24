//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dcamera.h, Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/q3dcamera.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DCamera that Python can take functions over in. Every Q3DCamera
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DCamera : public Q3DCamera {
public:
  using Q3DCamera::Q3DCamera;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DCameraCall0 call = reinterpret_cast<CuteQ3DCameraCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DCameraCall1 call = reinterpret_cast<CuteQ3DCameraCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DCameraCall2 call = reinterpret_cast<CuteQ3DCameraCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DCameraCall3 call = reinterpret_cast<CuteQ3DCameraCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DCameraCall4 call = reinterpret_cast<CuteQ3DCameraCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DCameraCall5 call = reinterpret_cast<CuteQ3DCameraCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DCameraCall6 call = reinterpret_cast<CuteQ3DCameraCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Q3DCamera10metaObjectEv(
    const Q3DCamera *self) {
  return self->metaObject();
}

//  QString Q3DCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Q3DCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DCamera::tr(s, c, n));
}

//  Q3DCamera::Q3DCamera(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DCamera *ritual_ZN9Q3DCameraC1EP7QObject(QObject *parent) {
  return new CuteQ3DCamera(parent);
}

//  Q3DCamera::~Q3DCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCameraD1Ev(Q3DCamera *self) {
  delete self;
}

//  float Q3DCamera::xRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Q3DCamera9xRotationEv(const Q3DCamera *self) {
  return self->xRotation();
}

//  void Q3DCamera::setXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera12setXRotationEf(Q3DCamera *self, float rotation) {
  self->setXRotation(rotation);
}

//  float Q3DCamera::yRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Q3DCamera9yRotationEv(const Q3DCamera *self) {
  return self->yRotation();
}

//  void Q3DCamera::setYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera12setYRotationEf(Q3DCamera *self, float rotation) {
  self->setYRotation(rotation);
}

//  bool Q3DCamera::wrapXRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Q3DCamera13wrapXRotationEv(const Q3DCamera *self) {
  return self->wrapXRotation();
}

//  void Q3DCamera::setWrapXRotation(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera16setWrapXRotationEb(
    Q3DCamera *self,
    bool isEnabled) {
  self->setWrapXRotation(isEnabled);
}

//  bool Q3DCamera::wrapYRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Q3DCamera13wrapYRotationEv(const Q3DCamera *self) {
  return self->wrapYRotation();
}

//  void Q3DCamera::setWrapYRotation(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera16setWrapYRotationEb(
    Q3DCamera *self,
    bool isEnabled) {
  self->setWrapYRotation(isEnabled);
}

//  CameraPreset Q3DCamera::cameraPreset() const
extern "C" Q_DECL_EXPORT
Q3DCamera::CameraPreset ritual_ZNK9Q3DCamera12cameraPresetEv(
    const Q3DCamera *self) {
  return self->cameraPreset();
}

//  void Q3DCamera::setCameraPreset(CameraPreset preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera15setCameraPresetENS_12CameraPresetE(
    Q3DCamera *self,
    Q3DCamera::CameraPreset preset) {
  self->setCameraPreset(preset);
}

//  float Q3DCamera::zoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Q3DCamera9zoomLevelEv(const Q3DCamera *self) {
  return self->zoomLevel();
}

//  void Q3DCamera::setZoomLevel(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera12setZoomLevelEf(Q3DCamera *self, float zoomLevel) {
  self->setZoomLevel(zoomLevel);
}

//  float Q3DCamera::minZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Q3DCamera12minZoomLevelEv(const Q3DCamera *self) {
  return self->minZoomLevel();
}

//  void Q3DCamera::setMinZoomLevel(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera15setMinZoomLevelEf(
    Q3DCamera *self,
    float zoomLevel) {
  self->setMinZoomLevel(zoomLevel);
}

//  float Q3DCamera::maxZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Q3DCamera12maxZoomLevelEv(const Q3DCamera *self) {
  return self->maxZoomLevel();
}

//  void Q3DCamera::setMaxZoomLevel(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera15setMaxZoomLevelEf(
    Q3DCamera *self,
    float zoomLevel) {
  self->setMaxZoomLevel(zoomLevel);
}

//  void Q3DCamera::setCameraPosition(float horizontal, float vertical, float
//      zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera17setCameraPositionEfff(
    Q3DCamera *self,
    float horizontal,
    float vertical,
    float zoom) {
  self->setCameraPosition(horizontal, vertical, zoom);
}

//  QVector3D Q3DCamera::target() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9Q3DCamera6targetEv(const Q3DCamera *self) {
  return new QVector3D(self->target());
}

//  void Q3DCamera::setTarget(const QVector3D &target)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DCamera9setTargetERK9QVector3D(
    Q3DCamera *self,
    const QVector3D *target) {
  self->setTarget(*target);
}

//  a Python function taken by a CuteQ3DCamera, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DCamera(Q3DCamera *self, const char *key, void *call) {
  return static_cast<CuteQ3DCamera *>(self)->take(key, call);
}
