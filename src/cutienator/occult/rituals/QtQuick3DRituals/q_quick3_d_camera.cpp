//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcamera_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuick3DCamera may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DCamera : QQuick3DCamera {
  using QQuick3DCamera::updateSpatialNode;
};

//  const QMetaObject *QQuick3DCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DCamera10metaObjectEv(
    const QQuick3DCamera *self) {
  return self->metaObject();
}

//  void *QQuick3DCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DCamera11qt_metacastEPKc(
    QQuick3DCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DCamera::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuick3DCamera2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DCamera::tr(s, c, n));
}

//  void QQuick3DCamera::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera24qt_qmlMarker_uncreatableEv(
    QQuick3DCamera *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QVector3D QQuick3DCamera::mapToViewport(const QVector3D &scenePos) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QQuick3DCamera13mapToViewportERK9QVector3D(
    const QQuick3DCamera *self,
    const QVector3D *scenePos) {
  return new QVector3D(self->mapToViewport(*scenePos));
}

//  QVector3D QQuick3DCamera::mapFromViewport(const QVector3D &viewportPos)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QQuick3DCamera15mapFromViewportERK9QVector3D(
    const QQuick3DCamera *self,
    const QVector3D *viewportPos) {
  return new QVector3D(self->mapFromViewport(*viewportPos));
}

//  QVector3D QQuick3DCamera::mapToViewport(const QVector3D &scenePos, qreal
//      width, qreal height)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QQuick3DCamera13mapToViewportERK9QVector3Ddd(
    QQuick3DCamera *self,
    const QVector3D *scenePos,
    qreal width,
    qreal height) {
  return new QVector3D(self->mapToViewport(*scenePos, width, height));
}

//  QVector3D QQuick3DCamera::mapFromViewport(const QVector3D &viewportPos,
//      qreal width, qreal height)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QQuick3DCamera15mapFromViewportERK9QVector3Ddd(
    QQuick3DCamera *self,
    const QVector3D *viewportPos,
    qreal width,
    qreal height) {
  return new QVector3D(self->mapFromViewport(*viewportPos, width, height));
}

//  void QQuick3DCamera::lookAt(const QVector3D &scenePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera6lookAtERK9QVector3D(
    QQuick3DCamera *self,
    const QVector3D *scenePos) {
  self->lookAt(*scenePos);
}

//  void QQuick3DCamera::lookAt(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera6lookAtEP12QQuick3DNode(
    QQuick3DCamera *self,
    QQuick3DNode *node) {
  self->lookAt(node);
}

//  void QQuick3DCamera::updateGlobalVariables(const QRectF &inViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera21updateGlobalVariablesERK6QRectF(
    QQuick3DCamera *self,
    const QRectF *inViewport) {
  self->updateGlobalVariables(*inViewport);
}

//  bool QQuick3DCamera::frustumCullingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DCamera21frustumCullingEnabledEv(
    const QQuick3DCamera *self) {
  return self->frustumCullingEnabled();
}

//  QQuick3DNode *QQuick3DCamera::lookAtNode() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK14QQuick3DCamera10lookAtNodeEv(
    const QQuick3DCamera *self) {
  return self->lookAtNode();
}

//  float QQuick3DCamera::levelOfDetailBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QQuick3DCamera17levelOfDetailBiasEv(
    const QQuick3DCamera *self) {
  return self->levelOfDetailBias();
}

//  void QQuick3DCamera::setFrustumCullingEnabled(bool frustumCullingEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera24setFrustumCullingEnabledEb(
    QQuick3DCamera *self,
    bool frustumCullingEnabled) {
  self->setFrustumCullingEnabled(frustumCullingEnabled);
}

//  void QQuick3DCamera::setLookAtNode(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera13setLookAtNodeEP12QQuick3DNode(
    QQuick3DCamera *self,
    QQuick3DNode *node) {
  self->setLookAtNode(node);
}

//  void QQuick3DCamera::setLevelOfDetailBias(float newLevelOFDetailBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera20setLevelOfDetailBiasEf(
    QQuick3DCamera *self,
    float newLevelOFDetailBias) {
  self->setLevelOfDetailBias(newLevelOFDetailBias);
}

//  void QQuick3DCamera::frustumCullingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera28frustumCullingEnabledChangedEv(
    QQuick3DCamera *self) {
  self->frustumCullingEnabledChanged();
}

//  void QQuick3DCamera::lookAtNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera17lookAtNodeChangedEv(QQuick3DCamera *self) {
  self->lookAtNodeChanged();
}

//  void QQuick3DCamera::levelOfDetailBiasChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera24levelOfDetailBiasChangedEv(
    QQuick3DCamera *self) {
  self->levelOfDetailBiasChanged();
}

//  QQuick3DCamera::QQuick3DCamera(QQuick3DNodePrivate &dd, QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DCamera *ritual_ZN14QQuick3DCameraC1ER19QQuick3DNodePrivateP12QQuick3DNode(
    QQuick3DNodePrivate *dd,
    QQuick3DNode *parent) {
  return new QQuick3DCamera(*dd, parent);
}

//  QSSGRenderGraphObject
//      *QQuick3DCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN14QQuick3DCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCamera *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DCamera::updateLookAt()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DCamera12updateLookAtEv(QQuick3DCamera *self) {
  self->updateLookAt();
}

//  QSSGRenderGraphObject
//      *QQuick3DCamera::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN14QQuick3DCamera17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCamera *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DCamera *>(self)->OwnQQuick3DCamera::updateSpatialNode(
      node);
}
