//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dcamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 630, as _ZN16Q3DCameraPrivateD1Ev
inline Q3DCameraPrivate::~Q3DCameraPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 636, as _ZN16Q3DCameraPrivate4syncER9Q3DCamera
inline void Q3DCameraPrivate::sync(Q3DCamera &other)
{
    if (q_ptr->isDirty()) {
        other.copyValuesFrom(*q_ptr);
        q_ptr->setDirty(false);
        other.setDirty(false);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 645, as _ZN16Q3DCameraPrivate12setXRotationEf
inline void Q3DCameraPrivate::setXRotation(const float rotation)
{
    if (m_xRotation != rotation) {
        m_xRotation = rotation;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 653, as _ZN16Q3DCameraPrivate12setYRotationEf
inline void Q3DCameraPrivate::setYRotation(const float rotation)
{
    if (m_yRotation != rotation) {
        m_yRotation = rotation;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 669, as _ZNK16Q3DCameraPrivate12minXRotationEv
inline float Q3DCameraPrivate::minXRotation() const
{
    return m_minXRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 698, as _ZNK16Q3DCameraPrivate12minYRotationEv
inline float Q3DCameraPrivate::minYRotation() const
{
    return m_minYRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 727, as _ZNK16Q3DCameraPrivate12maxXRotationEv
inline float Q3DCameraPrivate::maxXRotation() const
{
    return m_maxXRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 757, as _ZNK16Q3DCameraPrivate12maxYRotationEv
inline float Q3DCameraPrivate::maxYRotation() const
{
    return m_maxYRotation;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 815, as _ZNK16Q3DCameraPrivate10viewMatrixEv
inline QMatrix4x4 Q3DCameraPrivate::viewMatrix() const
{
    return m_viewMatrix;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 835, as _ZNK16Q3DCameraPrivate29isViewMatrixAutoUpdateEnabledEv
inline bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled() const
{
    return m_isViewMatrixUpdateActive;
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 854, as _ZN16Q3DCameraPrivate18setBaseOrientationERK9QVector3DS2_S2_
inline void Q3DCameraPrivate::setBaseOrientation(const QVector3D &basePosition,
                                          const QVector3D &target,
                                          const QVector3D &baseUp)
{
    if (q_ptr->position() != basePosition || m_actualTarget != target || m_up != baseUp) {
        q_ptr->setPosition(basePosition);
        m_actualTarget = target;
        m_up = baseUp;
        q_ptr->setDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dcamera.cpp, line 877, as _ZNK16Q3DCameraPrivate33calculatePositionRelativeToCameraERK9QVector3Dff
inline QVector3D Q3DCameraPrivate::calculatePositionRelativeToCamera(const QVector3D &relativePosition,
                                                              float fixedRotation,
                                                              float distanceModifier) const
{
    // Move the position with camera
    const float radiusFactor = cameraDistance * (1.5f + distanceModifier);
    float xAngle;
    float yAngle;

    if (!fixedRotation) {
        xAngle = qDegreesToRadians(m_xRotation);
        float yRotation = m_yRotation;
        // Light must not be paraller to eye vector, so fudge the y rotation a bit.
        // Note: This needs redoing if we ever allow arbitrary light positioning.
        const float yMargin = 0.1f; // Smaller margins cause weird shadow artifacts on tops of bars
        const float absYRotation = qAbs(yRotation);
        if (absYRotation < 90.0f + yMargin && absYRotation > 90.0f - yMargin) {
            if (yRotation < 0.0f)
                yRotation = -90.0f + yMargin;
            else
                yRotation = 90.0f - yMargin;
        }
        yAngle = qDegreesToRadians(yRotation);
    } else {
        xAngle = qDegreesToRadians(fixedRotation);
        yAngle = 0;
    }
    // Set radius to match the highest height of the position
    const float radius = (radiusFactor + relativePosition.y());
    const float zPos = radius * qCos(xAngle) * qCos(yAngle);
    const float xPos = radius * qSin(xAngle) * qCos(yAngle);
    const float yPos = radius * qSin(yAngle);

    // Keep in the set position in relation to camera
    return QVector3D(-xPos + relativePosition.x(),
                     yPos + relativePosition.y(),
                     zPos + relativePosition.z());
}
//  -----------------------------------------------------------------------

//  A Q3DCameraPrivate that Python can take functions over in. Every Q3DCameraPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DCameraPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DCameraPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DCameraPrivate : public Q3DCameraPrivate {
public:
  using Q3DCameraPrivate::Q3DCameraPrivate;
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
      CuteQ3DCameraPrivateCall0 call = reinterpret_cast<CuteQ3DCameraPrivateCall0>(taken[0]);
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
      CuteQ3DCameraPrivateCall1 call = reinterpret_cast<CuteQ3DCameraPrivateCall1>(taken[1]);
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
      CuteQ3DCameraPrivateCall2 call = reinterpret_cast<CuteQ3DCameraPrivateCall2>(taken[2]);
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
      CuteQ3DCameraPrivateCall3 call = reinterpret_cast<CuteQ3DCameraPrivateCall3>(taken[3]);
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
      CuteQ3DCameraPrivateCall4 call = reinterpret_cast<CuteQ3DCameraPrivateCall4>(taken[4]);
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
      CuteQ3DCameraPrivateCall5 call = reinterpret_cast<CuteQ3DCameraPrivateCall5>(taken[5]);
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
      CuteQ3DCameraPrivateCall6 call = reinterpret_cast<CuteQ3DCameraPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DCameraPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16Q3DCameraPrivate10metaObjectEv(
    const Q3DCameraPrivate *self) {
  return self->metaObject();
}

//  void *Q3DCameraPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16Q3DCameraPrivate11qt_metacastEPKc(
    Q3DCameraPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DCameraPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16Q3DCameraPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DCameraPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Q3DCameraPrivate::~Q3DCameraPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivateD1Ev(Q3DCameraPrivate *self) {
  delete self;
}

//  void Q3DCameraPrivate::sync(Q3DCamera &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate4syncER9Q3DCamera(
    Q3DCameraPrivate *self,
    Q3DCamera *other) {
  self->sync(*other);
}

//  void Q3DCameraPrivate::setXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate12setXRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setXRotation(rotation);
}

//  void Q3DCameraPrivate::setYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate12setYRotationEf(
    Q3DCameraPrivate *self,
    float rotation) {
  self->setYRotation(rotation);
}

//  float Q3DCameraPrivate::minXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12minXRotationEv(
    const Q3DCameraPrivate *self) {
  return self->minXRotation();
}

//  float Q3DCameraPrivate::minYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12minYRotationEv(
    const Q3DCameraPrivate *self) {
  return self->minYRotation();
}

//  float Q3DCameraPrivate::maxXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12maxXRotationEv(
    const Q3DCameraPrivate *self) {
  return self->maxXRotation();
}

//  float Q3DCameraPrivate::maxYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Q3DCameraPrivate12maxYRotationEv(
    const Q3DCameraPrivate *self) {
  return self->maxYRotation();
}

//  QMatrix4x4 Q3DCameraPrivate::viewMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK16Q3DCameraPrivate10viewMatrixEv(
    const Q3DCameraPrivate *self) {
  return new QMatrix4x4(self->viewMatrix());
}

//  bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16Q3DCameraPrivate29isViewMatrixAutoUpdateEnabledEv(
    const Q3DCameraPrivate *self) {
  return self->isViewMatrixAutoUpdateEnabled();
}

//  void Q3DCameraPrivate::setBaseOrientation(const QVector3D
//      &defaultPosition, const QVector3D &defaultTarget, const QVector3D
//      &defaultUp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate18setBaseOrientationERK9QVector3DS2_S2_(
    Q3DCameraPrivate *self,
    const QVector3D *defaultPosition,
    const QVector3D *defaultTarget,
    const QVector3D *defaultUp) {
  self->setBaseOrientation(*defaultPosition, *defaultTarget, *defaultUp);
}

//  QVector3D Q3DCameraPrivate::calculatePositionRelativeToCamera(const
//      QVector3D &relativePosition, float fixedRotation, float
//      distanceModifier) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16Q3DCameraPrivate33calculatePositionRelativeToCameraERK9QVector3Dff(
    const Q3DCameraPrivate *self,
    const QVector3D *relativePosition,
    float fixedRotation,
    float distanceModifier) {
  return new QVector3D(
      self->calculatePositionRelativeToCamera(
          *relativePosition,
          fixedRotation,
          distanceModifier));
}

//  void Q3DCameraPrivate::minXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19minXRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minXRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minXRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::minYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19minYRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minYRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minYRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::maxXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19maxXRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "maxXRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "maxXRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::maxYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate19maxYRotationChangedEf(
    Q3DCameraPrivate *self,
    float rotation) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "maxYRotationChanged(float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "maxYRotationChanged(float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&rotation)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::viewMatrixChanged(const QMatrix4x4 &viewMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate17viewMatrixChangedERK10QMatrix4x4(
    Q3DCameraPrivate *self,
    const QMatrix4x4 *viewMatrix) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "viewMatrixChanged(const QMatrix4x4 &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "viewMatrixChanged(const QMatrix4x4 &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(viewMatrix)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Q3DCameraPrivate27viewMatrixAutoUpdateChangedEb(
    Q3DCameraPrivate *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DCameraPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "viewMatrixAutoUpdateChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "viewMatrixAutoUpdateChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQ3DCameraPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DCameraPrivate(
    Q3DCameraPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DCameraPrivate *>(self)->take(key, call);
}
