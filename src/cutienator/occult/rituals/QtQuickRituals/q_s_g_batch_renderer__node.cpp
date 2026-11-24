//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Node *QSGBatchRenderer::Node::parent() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Node *ritual_ZNK16QSGBatchRenderer4Node6parentEv(
    const QSGBatchRenderer::Node *self) {
  return self->parent();
}

//  void QSGBatchRenderer::Node::append(Node *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Node6appendEPS0_(
    QSGBatchRenderer::Node *self,
    QSGBatchRenderer::Node *child) {
  self->append(child);
}

//  void QSGBatchRenderer::Node::remove(Node *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Node6removeEPS0_(
    QSGBatchRenderer::Node *self,
    QSGBatchRenderer::Node *child) {
  self->remove(child);
}

//  Node *QSGBatchRenderer::Node::firstChild() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Node *ritual_ZNK16QSGBatchRenderer4Node10firstChildEv(
    const QSGBatchRenderer::Node *self) {
  return self->firstChild();
}

//  Node *QSGBatchRenderer::Node::sibling() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Node *ritual_ZNK16QSGBatchRenderer4Node7siblingEv(
    const QSGBatchRenderer::Node *self) {
  return self->sibling();
}

//  void QSGBatchRenderer::Node::setParent(Node *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Node9setParentEPS0_(
    QSGBatchRenderer::Node *self,
    QSGBatchRenderer::Node *p) {
  self->setParent(p);
}

//  bool QSGBatchRenderer::Node::hasChild(Node *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer4Node8hasChildEPS0_(
    const QSGBatchRenderer::Node *self,
    QSGBatchRenderer::Node *child) {
  return self->hasChild(child);
}

//  QSGNode::NodeType QSGBatchRenderer::Node::type() const
extern "C" Q_DECL_EXPORT
QSGNode::NodeType ritual_ZNK16QSGBatchRenderer4Node4typeEv(
    const QSGBatchRenderer::Node *self) {
  return self->type();
}

//  Element *QSGBatchRenderer::Node::element() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Element *ritual_ZNK16QSGBatchRenderer4Node7elementEv(
    const QSGBatchRenderer::Node *self) {
  return self->element();
}

//  RenderNodeElement *QSGBatchRenderer::Node::renderNodeElement() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::RenderNodeElement *ritual_ZNK16QSGBatchRenderer4Node17renderNodeElementEv(
    const QSGBatchRenderer::Node *self) {
  return self->renderNodeElement();
}

//  ClipBatchRootInfo *QSGBatchRenderer::Node::clipInfo() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::ClipBatchRootInfo *ritual_ZNK16QSGBatchRenderer4Node8clipInfoEv(
    const QSGBatchRenderer::Node *self) {
  return self->clipInfo();
}

//  BatchRootInfo *QSGBatchRenderer::Node::rootInfo() const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::BatchRootInfo *ritual_ZNK16QSGBatchRenderer4Node8rootInfoEv(
    const QSGBatchRenderer::Node *self) {
  return self->rootInfo();
}

//  QSGBatchRenderer::Node::~Node()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4NodeD1Ev(QSGBatchRenderer::Node *self) {
  delete self;
}
