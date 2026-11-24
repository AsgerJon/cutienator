//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickclipnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickclipnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QQuickDefaultClipNode::QQuickDefaultClipNode(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QQuickDefaultClipNode *ritual_ZN21QQuickDefaultClipNodeC1ERK6QRectF(
    const QRectF *a0) {
  return new QQuickDefaultClipNode(*a0);
}

//  void QQuickDefaultClipNode::setRect(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDefaultClipNode7setRectERK6QRectF(
    QQuickDefaultClipNode *self,
    const QRectF *a0) {
  self->setRect(*a0);
}

//  QRectF QQuickDefaultClipNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QQuickDefaultClipNode4rectEv(
    const QQuickDefaultClipNode *self) {
  return new QRectF(self->rect());
}

//  void QQuickDefaultClipNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDefaultClipNode9setRadiusEd(
    QQuickDefaultClipNode *self,
    qreal radius) {
  self->setRadius(radius);
}

//  qreal QQuickDefaultClipNode::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickDefaultClipNode6radiusEv(
    const QQuickDefaultClipNode *self) {
  return self->radius();
}

//  void QQuickDefaultClipNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDefaultClipNode6updateEv(QQuickDefaultClipNode *self) {
  self->update();
}

//  void QQuickDefaultClipNode::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDefaultClipNode14updateGeometryEv(
    QQuickDefaultClipNode *self) {
  self->updateGeometry();
}

//  void QQuickDefaultClipNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDefaultClipNode6updateEv(
    QQuickDefaultClipNode *self) {
  self->QQuickDefaultClipNode::update();
}
