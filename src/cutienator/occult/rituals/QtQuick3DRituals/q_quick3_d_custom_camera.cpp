//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcustomcamera_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcustomcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>

//  Only a class built on QQuick3DCustomCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DCustomCamera : QQuick3DCustomCamera {
  using QQuick3DCustomCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DCustomCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DCustomCamera10metaObjectEv(
    const QQuick3DCustomCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DCustomCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DCustomCamera11qt_metacastEPKc(
    QQuick3DCustomCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DCustomCamera::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DCustomCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DCustomCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DCustomCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuick3DCustomCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DCustomCamera::tr(s, c, n));
}

//  QQuick3DCustomCamera::QQuick3DCustomCamera(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DCustomCamera *ritual_ZN20QQuick3DCustomCameraC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DCustomCamera(parent);
}

//  QMatrix4x4 QQuick3DCustomCamera::projection() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK20QQuick3DCustomCamera10projectionEv(
    const QQuick3DCustomCamera *self) {
  return new QMatrix4x4(self->projection());
}

//  void QQuick3DCustomCamera::setProjection(const QMatrix4x4 &projection)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DCustomCamera13setProjectionERK10QMatrix4x4(
    QQuick3DCustomCamera *self,
    const QMatrix4x4 *projection) {
  self->setProjection(*projection);
}

//  void QQuick3DCustomCamera::projectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DCustomCamera17projectionChangedEv(
    QQuick3DCustomCamera *self) {
  self->projectionChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DCustomCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN20QQuick3DCustomCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCustomCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  QSSGRenderGraphObject
//      *QQuick3DCustomCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN20QQuick3DCustomCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCustomCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DCustomCamera *>(self)->OwnQQuick3DCustomCamera::updateSpatialNode(
      node);
}
