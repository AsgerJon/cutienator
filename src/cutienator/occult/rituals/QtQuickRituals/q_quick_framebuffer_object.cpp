//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickframebufferobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/qquickframebufferobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickFramebufferObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFramebufferObject : QQuickFramebufferObject {
  using QQuickFramebufferObject::geometryChange;
  using QQuickFramebufferObject::updatePaintNode;
};

//  const QMetaObject *QQuickFramebufferObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickFramebufferObject10metaObjectEv(
    const QQuickFramebufferObject *self) {
  return self->metaObject();
}

//  QString QQuickFramebufferObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickFramebufferObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFramebufferObject::tr(s, c, n));
}

//  bool QQuickFramebufferObject::textureFollowsItemSize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickFramebufferObject22textureFollowsItemSizeEv(
    const QQuickFramebufferObject *self) {
  return self->textureFollowsItemSize();
}

//  void QQuickFramebufferObject::setTextureFollowsItemSize(bool follows)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject25setTextureFollowsItemSizeEb(
    QQuickFramebufferObject *self,
    bool follows) {
  self->setTextureFollowsItemSize(follows);
}

//  bool QQuickFramebufferObject::mirrorVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickFramebufferObject16mirrorVerticallyEv(
    const QQuickFramebufferObject *self) {
  return self->mirrorVertically();
}

//  void QQuickFramebufferObject::setMirrorVertically(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject19setMirrorVerticallyEb(
    QQuickFramebufferObject *self,
    bool enable) {
  self->setMirrorVertically(enable);
}

//  Renderer *QQuickFramebufferObject::createRenderer() const
extern "C" Q_DECL_EXPORT
QQuickFramebufferObject::Renderer *ritual_ZNK23QQuickFramebufferObject14createRendererEv(
    const QQuickFramebufferObject *self) {
  return self->createRenderer();
}

//  bool QQuickFramebufferObject::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickFramebufferObject17isTextureProviderEv(
    const QQuickFramebufferObject *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuickFramebufferObject::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK23QQuickFramebufferObject15textureProviderEv(
    const QQuickFramebufferObject *self) {
  return self->textureProvider();
}

//  void QQuickFramebufferObject::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject16releaseResourcesEv(
    QQuickFramebufferObject *self) {
  self->releaseResources();
}

//  void QQuickFramebufferObject::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject14geometryChangeERK6QRectFS2_(
    QQuickFramebufferObject *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *QQuickFramebufferObject::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN23QQuickFramebufferObject15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickFramebufferObject *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickFramebufferObject::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject20invalidateSceneGraphEv(
    QQuickFramebufferObject *self) {
  self->invalidateSceneGraph();
}

//  bool QQuickFramebufferObject::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QQuickFramebufferObject17isTextureProviderEv(
    const QQuickFramebufferObject *self) {
  return self->QQuickFramebufferObject::isTextureProvider();
}

//  QSGTextureProvider *QQuickFramebufferObject::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK23QQuickFramebufferObject15textureProviderEv(
    const QQuickFramebufferObject *self) {
  return self->QQuickFramebufferObject::textureProvider();
}

//  void QQuickFramebufferObject::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickFramebufferObject16releaseResourcesEv(
    QQuickFramebufferObject *self) {
  self->QQuickFramebufferObject::releaseResources();
}

//  void QQuickFramebufferObject::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickFramebufferObject14geometryChangeERK6QRectFS2_(
    QQuickFramebufferObject *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickFramebufferObject *>(self)->OwnQQuickFramebufferObject::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QSGNode *QQuickFramebufferObject::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN23QQuickFramebufferObject15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickFramebufferObject *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickFramebufferObject *>(self)->OwnQQuickFramebufferObject::updatePaintNode(
      a0,
      a1);
}
