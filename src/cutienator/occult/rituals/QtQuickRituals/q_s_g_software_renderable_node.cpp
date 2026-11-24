//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qlist.h>

//  QSGSoftwareRenderableNode::QSGSoftwareRenderableNode(NodeType type,
//      QSGNode *node)
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderableNode *ritual_ZN25QSGSoftwareRenderableNodeC1ENS_8NodeTypeEP7QSGNode(
    QSGSoftwareRenderableNode::NodeType type,
    QSGNode *node) {
  return new QSGSoftwareRenderableNode(type, node);
}

//  QSGSoftwareRenderableNode::~QSGSoftwareRenderableNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNodeD1Ev(
    QSGSoftwareRenderableNode *self) {
  delete self;
}

//  void QSGSoftwareRenderableNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode6updateEv(
    QSGSoftwareRenderableNode *self) {
  self->update();
}

//  QRegion QSGSoftwareRenderableNode::renderNode(QPainter *painter, bool
//      forceOpaquePainting)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN25QSGSoftwareRenderableNode10renderNodeEP8QPainterb(
    QSGSoftwareRenderableNode *self,
    QPainter *painter,
    bool forceOpaquePainting) {
  return new QRegion(self->renderNode(painter, forceOpaquePainting));
}

//  QRect QSGSoftwareRenderableNode::boundingRectMin() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK25QSGSoftwareRenderableNode15boundingRectMinEv(
    const QSGSoftwareRenderableNode *self) {
  return new QRect(self->boundingRectMin());
}

//  QRect QSGSoftwareRenderableNode::boundingRectMax() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK25QSGSoftwareRenderableNode15boundingRectMaxEv(
    const QSGSoftwareRenderableNode *self) {
  return new QRect(self->boundingRectMax());
}

//  NodeType QSGSoftwareRenderableNode::type() const
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderableNode::NodeType ritual_ZNK25QSGSoftwareRenderableNode4typeEv(
    const QSGSoftwareRenderableNode *self) {
  return self->type();
}

//  bool QSGSoftwareRenderableNode::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGSoftwareRenderableNode8isOpaqueEv(
    const QSGSoftwareRenderableNode *self) {
  return self->isOpaque();
}

//  bool QSGSoftwareRenderableNode::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGSoftwareRenderableNode7isDirtyEv(
    const QSGSoftwareRenderableNode *self) {
  return self->isDirty();
}

//  bool QSGSoftwareRenderableNode::isDirtyRegionEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGSoftwareRenderableNode18isDirtyRegionEmptyEv(
    const QSGSoftwareRenderableNode *self) {
  return self->isDirtyRegionEmpty();
}

//  QSGNode *QSGSoftwareRenderableNode::handle() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK25QSGSoftwareRenderableNode6handleEv(
    const QSGSoftwareRenderableNode *self) {
  return self->handle();
}

//  void QSGSoftwareRenderableNode::setTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode12setTransformERK10QTransform(
    QSGSoftwareRenderableNode *self,
    const QTransform *transform) {
  self->setTransform(*transform);
}

//  void QSGSoftwareRenderableNode::setClipRegion(const QRegion &clipRegion,
//      bool hasClipRegion)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode13setClipRegionERK7QRegionb(
    QSGSoftwareRenderableNode *self,
    const QRegion *clipRegion,
    bool hasClipRegion) {
  self->setClipRegion(*clipRegion, hasClipRegion);
}

//  void QSGSoftwareRenderableNode::setOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode10setOpacityEf(
    QSGSoftwareRenderableNode *self,
    float opacity) {
  self->setOpacity(opacity);
}

//  QTransform QSGSoftwareRenderableNode::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK25QSGSoftwareRenderableNode9transformEv(
    const QSGSoftwareRenderableNode *self) {
  return new QTransform(self->transform());
}

//  QRegion QSGSoftwareRenderableNode::clipRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK25QSGSoftwareRenderableNode10clipRegionEv(
    const QSGSoftwareRenderableNode *self) {
  return new QRegion(self->clipRegion());
}

//  float QSGSoftwareRenderableNode::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QSGSoftwareRenderableNode7opacityEv(
    const QSGSoftwareRenderableNode *self) {
  return self->opacity();
}

//  void QSGSoftwareRenderableNode::markGeometryDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode17markGeometryDirtyEv(
    QSGSoftwareRenderableNode *self) {
  self->markGeometryDirty();
}

//  void QSGSoftwareRenderableNode::markMaterialDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode17markMaterialDirtyEv(
    QSGSoftwareRenderableNode *self) {
  self->markMaterialDirty();
}

//  void QSGSoftwareRenderableNode::addDirtyRegion(const QRegion
//      &dirtyRegion, bool forceDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode14addDirtyRegionERK7QRegionb(
    QSGSoftwareRenderableNode *self,
    const QRegion *dirtyRegion,
    bool forceDirty) {
  self->addDirtyRegion(*dirtyRegion, forceDirty);
}

//  void QSGSoftwareRenderableNode::subtractDirtyRegion(const QRegion
//      &dirtyRegion)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwareRenderableNode19subtractDirtyRegionERK7QRegion(
    QSGSoftwareRenderableNode *self,
    const QRegion *dirtyRegion) {
  self->subtractDirtyRegion(*dirtyRegion);
}

//  QRegion QSGSoftwareRenderableNode::previousDirtyRegion(bool wasRemoved)
//      const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK25QSGSoftwareRenderableNode19previousDirtyRegionEb(
    const QSGSoftwareRenderableNode *self,
    bool wasRemoved) {
  return new QRegion(self->previousDirtyRegion(wasRemoved));
}

//  QRegion QSGSoftwareRenderableNode::dirtyRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK25QSGSoftwareRenderableNode11dirtyRegionEv(
    const QSGSoftwareRenderableNode *self) {
  return new QRegion(self->dirtyRegion());
}

//  QList<QSGSoftwareRenderableNode *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSGSoftwareRenderableNode *> *ritual_list_make_QSGSoftwareRenderableNode_ptr() {
  return new QList<QSGSoftwareRenderableNode *>();
}

//  void QList<QSGSoftwareRenderableNode *>::append(const
//      QSGSoftwareRenderableNode * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSGSoftwareRenderableNode_ptr(
    QList<QSGSoftwareRenderableNode *> *self,
    QSGSoftwareRenderableNode *element) {
  self->append(element);
}

//  qsizetype QList<QSGSoftwareRenderableNode *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSGSoftwareRenderableNode_ptr(
    const QList<QSGSoftwareRenderableNode *> *self) {
  return self->size();
}

//  const QSGSoftwareRenderableNode * &QList<QSGSoftwareRenderableNode
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderableNode *ritual_list_at_QSGSoftwareRenderableNode_ptr(
    const QList<QSGSoftwareRenderableNode *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSGSoftwareRenderableNode *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSGSoftwareRenderableNode_ptr(
    QList<QSGSoftwareRenderableNode *> *self) {
  delete self;
}
