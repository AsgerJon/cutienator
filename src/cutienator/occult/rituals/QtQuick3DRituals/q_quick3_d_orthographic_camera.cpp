//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dorthographiccamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dorthographiccamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuick3DOrthographicCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DOrthographicCamera : QQuick3DOrthographicCamera {
  using QQuick3DOrthographicCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DOrthographicCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuick3DOrthographicCamera10metaObjectEv(
    const QQuick3DOrthographicCamera *self) {
  return self->metaObject();
}

//  QString QQuick3DOrthographicCamera::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuick3DOrthographicCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DOrthographicCamera::tr(s, c, n));
}

//  QQuick3DOrthographicCamera::QQuick3DOrthographicCamera(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DOrthographicCamera *ritual_ZN26QQuick3DOrthographicCameraC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DOrthographicCamera(parent);
}

//  float QQuick3DOrthographicCamera::clipNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DOrthographicCamera8clipNearEv(
    const QQuick3DOrthographicCamera *self) {
  return self->clipNear();
}

//  float QQuick3DOrthographicCamera::clipFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DOrthographicCamera7clipFarEv(
    const QQuick3DOrthographicCamera *self) {
  return self->clipFar();
}

//  float QQuick3DOrthographicCamera::horizontalMagnification() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DOrthographicCamera23horizontalMagnificationEv(
    const QQuick3DOrthographicCamera *self) {
  return self->horizontalMagnification();
}

//  float QQuick3DOrthographicCamera::verticalMagnification() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DOrthographicCamera21verticalMagnificationEv(
    const QQuick3DOrthographicCamera *self) {
  return self->verticalMagnification();
}

//  void QQuick3DOrthographicCamera::setClipNear(float clipNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DOrthographicCamera11setClipNearEf(
    QQuick3DOrthographicCamera *self,
    float clipNear) {
  self->setClipNear(clipNear);
}

//  void QQuick3DOrthographicCamera::setClipFar(float clipFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DOrthographicCamera10setClipFarEf(
    QQuick3DOrthographicCamera *self,
    float clipFar) {
  self->setClipFar(clipFar);
}

//  void QQuick3DOrthographicCamera::setHorizontalMagnification(float
//      horizontalMagnification)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DOrthographicCamera26setHorizontalMagnificationEf(
    QQuick3DOrthographicCamera *self,
    float horizontalMagnification) {
  self->setHorizontalMagnification(horizontalMagnification);
}

//  void QQuick3DOrthographicCamera::setVerticalMagnification(float
//      horizontalMagnification)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DOrthographicCamera24setVerticalMagnificationEf(
    QQuick3DOrthographicCamera *self,
    float horizontalMagnification) {
  self->setVerticalMagnification(horizontalMagnification);
}

//  QSSGRenderGraphObject
//      *QQuick3DOrthographicCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN26QQuick3DOrthographicCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DOrthographicCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  QSSGRenderGraphObject
//      *QQuick3DOrthographicCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN26QQuick3DOrthographicCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DOrthographicCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DOrthographicCamera *>(self)->OwnQQuick3DOrthographicCamera::updateSpatialNode(
      node);
}
