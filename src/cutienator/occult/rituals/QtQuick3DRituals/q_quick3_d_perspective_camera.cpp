//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dperspectivecamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dperspectivecamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuick3DPerspectiveCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DPerspectiveCamera : QQuick3DPerspectiveCamera {
  using QQuick3DPerspectiveCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DPerspectiveCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuick3DPerspectiveCamera10metaObjectEv(
    const QQuick3DPerspectiveCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DPerspectiveCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuick3DPerspectiveCamera11qt_metacastEPKc(
    QQuick3DPerspectiveCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DPerspectiveCamera::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuick3DPerspectiveCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DPerspectiveCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DPerspectiveCamera::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuick3DPerspectiveCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DPerspectiveCamera::tr(s, c, n));
}

//  QQuick3DPerspectiveCamera::QQuick3DPerspectiveCamera(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DPerspectiveCamera *ritual_ZN25QQuick3DPerspectiveCameraC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DPerspectiveCamera(parent);
}

//  float QQuick3DPerspectiveCamera::clipNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QQuick3DPerspectiveCamera8clipNearEv(
    const QQuick3DPerspectiveCamera *self) {
  return self->clipNear();
}

//  float QQuick3DPerspectiveCamera::clipFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QQuick3DPerspectiveCamera7clipFarEv(
    const QQuick3DPerspectiveCamera *self) {
  return self->clipFar();
}

//  float QQuick3DPerspectiveCamera::fieldOfView() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QQuick3DPerspectiveCamera11fieldOfViewEv(
    const QQuick3DPerspectiveCamera *self) {
  return self->fieldOfView();
}

//  FieldOfViewOrientation
//      QQuick3DPerspectiveCamera::fieldOfViewOrientation() const
extern "C" Q_DECL_EXPORT
QQuick3DPerspectiveCamera::FieldOfViewOrientation ritual_ZNK25QQuick3DPerspectiveCamera22fieldOfViewOrientationEv(
    const QQuick3DPerspectiveCamera *self) {
  return self->fieldOfViewOrientation();
}

//  void QQuick3DPerspectiveCamera::setClipNear(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera11setClipNearEf(
    QQuick3DPerspectiveCamera *self,
    float clipNear) {
  self->setClipNear(clipNear);
}

//  void QQuick3DPerspectiveCamera::setClipFar(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera10setClipFarEf(
    QQuick3DPerspectiveCamera *self,
    float clipFar) {
  self->setClipFar(clipFar);
}

//  void QQuick3DPerspectiveCamera::setFieldOfView(float fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera14setFieldOfViewEf(
    QQuick3DPerspectiveCamera *self,
    float fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  void QQuick3DPerspectiveCamera::setFieldOfViewOrientation(QQuick3DPerspec
//      tiveCamera::FieldOfViewOrientation fieldOfViewOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera25setFieldOfViewOrientationENS_22FieldOfViewOrientationE(
    QQuick3DPerspectiveCamera *self,
    QQuick3DPerspectiveCamera::FieldOfViewOrientation fieldOfViewOrientation) {
  self->setFieldOfViewOrientation(fieldOfViewOrientation);
}

//  void QQuick3DPerspectiveCamera::clipNearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera15clipNearChangedEv(
    QQuick3DPerspectiveCamera *self) {
  self->clipNearChanged();
}

//  void QQuick3DPerspectiveCamera::clipFarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera14clipFarChangedEv(
    QQuick3DPerspectiveCamera *self) {
  self->clipFarChanged();
}

//  void QQuick3DPerspectiveCamera::fieldOfViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera18fieldOfViewChangedEv(
    QQuick3DPerspectiveCamera *self) {
  self->fieldOfViewChanged();
}

//  void QQuick3DPerspectiveCamera::fieldOfViewOrientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DPerspectiveCamera29fieldOfViewOrientationChangedEv(
    QQuick3DPerspectiveCamera *self) {
  self->fieldOfViewOrientationChanged();
}

//  QQuick3DPerspectiveCamera::QQuick3DPerspectiveCamera(QQuick3DNodePrivate
//      &dd, QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DPerspectiveCamera *ritual_ZN25QQuick3DPerspectiveCameraC1ER19QQuick3DNodePrivateP12QQuick3DNode(
    QQuick3DNodePrivate *dd,
    QQuick3DNode *parent) {
  return new QQuick3DPerspectiveCamera(*dd, parent);
}

//  QSSGRenderGraphObject
//      *QQuick3DPerspectiveCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN25QQuick3DPerspectiveCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPerspectiveCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  QSSGRenderGraphObject
//      *QQuick3DPerspectiveCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN25QQuick3DPerspectiveCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DPerspectiveCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DPerspectiveCamera *>(self)->OwnQQuick3DPerspectiveCamera::updateSpatialNode(
      node);
}
