//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfrustumcamera_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfrustumcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuick3DFrustumCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DFrustumCamera : QQuick3DFrustumCamera {
  using QQuick3DFrustumCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DFrustumCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DFrustumCamera10metaObjectEv(
    const QQuick3DFrustumCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DFrustumCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuick3DFrustumCamera11qt_metacastEPKc(
    QQuick3DFrustumCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DFrustumCamera::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuick3DFrustumCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DFrustumCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DFrustumCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DFrustumCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DFrustumCamera::tr(s, c, n));
}

//  QQuick3DFrustumCamera::QQuick3DFrustumCamera(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DFrustumCamera *ritual_ZN21QQuick3DFrustumCameraC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DFrustumCamera(parent);
}

//  float QQuick3DFrustumCamera::top() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DFrustumCamera3topEv(
    const QQuick3DFrustumCamera *self) {
  return self->top();
}

//  float QQuick3DFrustumCamera::bottom() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DFrustumCamera6bottomEv(
    const QQuick3DFrustumCamera *self) {
  return self->bottom();
}

//  float QQuick3DFrustumCamera::right() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DFrustumCamera5rightEv(
    const QQuick3DFrustumCamera *self) {
  return self->right();
}

//  float QQuick3DFrustumCamera::left() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QQuick3DFrustumCamera4leftEv(
    const QQuick3DFrustumCamera *self) {
  return self->left();
}

//  void QQuick3DFrustumCamera::setTop(float top)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera6setTopEf(
    QQuick3DFrustumCamera *self,
    float top) {
  self->setTop(top);
}

//  void QQuick3DFrustumCamera::setBottom(float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera9setBottomEf(
    QQuick3DFrustumCamera *self,
    float bottom) {
  self->setBottom(bottom);
}

//  void QQuick3DFrustumCamera::setRight(float right)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera8setRightEf(
    QQuick3DFrustumCamera *self,
    float right) {
  self->setRight(right);
}

//  void QQuick3DFrustumCamera::setLeft(float left)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera7setLeftEf(
    QQuick3DFrustumCamera *self,
    float left) {
  self->setLeft(left);
}

//  void QQuick3DFrustumCamera::topChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera10topChangedEv(
    QQuick3DFrustumCamera *self) {
  self->topChanged();
}

//  void QQuick3DFrustumCamera::bottomChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera13bottomChangedEv(
    QQuick3DFrustumCamera *self) {
  self->bottomChanged();
}

//  void QQuick3DFrustumCamera::rightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera12rightChangedEv(
    QQuick3DFrustumCamera *self) {
  self->rightChanged();
}

//  void QQuick3DFrustumCamera::leftChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DFrustumCamera11leftChangedEv(
    QQuick3DFrustumCamera *self) {
  self->leftChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DFrustumCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN21QQuick3DFrustumCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DFrustumCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  QSSGRenderGraphObject
//      *QQuick3DFrustumCamera::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN21QQuick3DFrustumCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DFrustumCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DFrustumCamera *>(self)->OwnQQuick3DFrustumCamera::updateSpatialNode(
      node);
}
