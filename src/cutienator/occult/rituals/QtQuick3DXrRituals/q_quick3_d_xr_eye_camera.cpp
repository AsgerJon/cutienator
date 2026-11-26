//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcamera_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>

//  Only a class built on QQuick3DXrEyeCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DXrEyeCamera : QQuick3DXrEyeCamera {
  using QQuick3DXrEyeCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DXrEyeCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DXrEyeCamera10metaObjectEv(
    const QQuick3DXrEyeCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DXrEyeCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DXrEyeCamera11qt_metacastEPKc(
    QQuick3DXrEyeCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrEyeCamera::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DXrEyeCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrEyeCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrEyeCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DXrEyeCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrEyeCamera::tr(s, c, n));
}

//  QQuick3DXrEyeCamera::QQuick3DXrEyeCamera(QQuick3DXrOrigin *parent)
extern "C" Q_DECL_EXPORT
QQuick3DXrEyeCamera *ritual_ZN19QQuick3DXrEyeCameraC1EP16QQuick3DXrOrigin(
    QQuick3DXrOrigin *parent) {
  return new QQuick3DXrEyeCamera(parent);
}

//  float QQuick3DXrEyeCamera::leftTangent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera11leftTangentEv(
    const QQuick3DXrEyeCamera *self) {
  return self->leftTangent();
}

//  float QQuick3DXrEyeCamera::rightTangent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera12rightTangentEv(
    const QQuick3DXrEyeCamera *self) {
  return self->rightTangent();
}

//  float QQuick3DXrEyeCamera::upTangent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera9upTangentEv(
    const QQuick3DXrEyeCamera *self) {
  return self->upTangent();
}

//  float QQuick3DXrEyeCamera::downTangent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera11downTangentEv(
    const QQuick3DXrEyeCamera *self) {
  return self->downTangent();
}

//  float QQuick3DXrEyeCamera::clipNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera8clipNearEv(
    const QQuick3DXrEyeCamera *self) {
  return self->clipNear();
}

//  float QQuick3DXrEyeCamera::clipFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DXrEyeCamera7clipFarEv(
    const QQuick3DXrEyeCamera *self) {
  return self->clipFar();
}

//  void QQuick3DXrEyeCamera::setLeftTangent(float leftTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera14setLeftTangentEf(
    QQuick3DXrEyeCamera *self,
    float leftTangent) {
  self->setLeftTangent(leftTangent);
}

//  void QQuick3DXrEyeCamera::setRightTangent(float rightTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera15setRightTangentEf(
    QQuick3DXrEyeCamera *self,
    float rightTangent) {
  self->setRightTangent(rightTangent);
}

//  void QQuick3DXrEyeCamera::setUpTangent(float upTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera12setUpTangentEf(
    QQuick3DXrEyeCamera *self,
    float upTangent) {
  self->setUpTangent(upTangent);
}

//  void QQuick3DXrEyeCamera::setDownTangent(float downTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera14setDownTangentEf(
    QQuick3DXrEyeCamera *self,
    float downTangent) {
  self->setDownTangent(downTangent);
}

//  void QQuick3DXrEyeCamera::setClipNear(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera11setClipNearEf(
    QQuick3DXrEyeCamera *self,
    float clipNear) {
  self->setClipNear(clipNear);
}

//  void QQuick3DXrEyeCamera::setClipFar(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera10setClipFarEf(
    QQuick3DXrEyeCamera *self,
    float clipFar) {
  self->setClipFar(clipFar);
}

//  void QQuick3DXrEyeCamera::setProjection(const QMatrix4x4 &projection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera13setProjectionERK10QMatrix4x4(
    QQuick3DXrEyeCamera *self,
    const QMatrix4x4 *projection) {
  self->setProjection(*projection);
}

//  void QQuick3DXrEyeCamera::leftTangentChanged(float leftTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera18leftTangentChangedEf(
    QQuick3DXrEyeCamera *self,
    float leftTangent) {
  self->leftTangentChanged(leftTangent);
}

//  void QQuick3DXrEyeCamera::rightTangentChanged(float rightTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera19rightTangentChangedEf(
    QQuick3DXrEyeCamera *self,
    float rightTangent) {
  self->rightTangentChanged(rightTangent);
}

//  void QQuick3DXrEyeCamera::upTangentChanged(float upTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera16upTangentChangedEf(
    QQuick3DXrEyeCamera *self,
    float upTangent) {
  self->upTangentChanged(upTangent);
}

//  void QQuick3DXrEyeCamera::downTangentChanged(float downTangent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera18downTangentChangedEf(
    QQuick3DXrEyeCamera *self,
    float downTangent) {
  self->downTangentChanged(downTangent);
}

//  void QQuick3DXrEyeCamera::clipNearChanged(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera15clipNearChangedEf(
    QQuick3DXrEyeCamera *self,
    float clipNear) {
  self->clipNearChanged(clipNear);
}

//  void QQuick3DXrEyeCamera::clipFarChanged(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera14clipFarChangedEf(
    QQuick3DXrEyeCamera *self,
    float clipFar) {
  self->clipFarChanged(clipFar);
}

//  QSSGRenderGraphObject
//      *QQuick3DXrEyeCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN19QQuick3DXrEyeCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DXrEyeCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DXrEyeCamera::markDirty(DirtyFlag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera9markDirtyENS_9DirtyFlagE(
    QQuick3DXrEyeCamera *self,
    QQuick3DXrEyeCamera::DirtyFlag flag) {
  self->markDirty(flag);
}

//  void QQuick3DXrEyeCamera::maybeUpdateProjection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrEyeCamera21maybeUpdateProjectionEv(
    QQuick3DXrEyeCamera *self) {
  self->maybeUpdateProjection();
}

//  QSSGRenderGraphObject
//      *QQuick3DXrEyeCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN19QQuick3DXrEyeCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DXrEyeCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DXrEyeCamera *>(self)->OwnQQuick3DXrEyeCamera::updateSpatialNode(
      node);
}
