//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>

//  QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode()
extern "C" Q_DECL_EXPORT
QQuickTextNodeEngine::BinaryTreeNode *ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeC1Ev() {
  return new QQuickTextNodeEngine::BinaryTreeNode();
}

//  QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const QRectF &brect,
//      const QImage &i, SelectionState selState, qreal a)
extern "C" Q_DECL_EXPORT
QQuickTextNodeEngine::BinaryTreeNode *ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeC1ERK6QRectFRK6QImageNS_14SelectionStateEd(
    const QRectF *brect,
    const QImage *i,
    QQuickTextNodeEngine::SelectionState selState,
    qreal a) {
  return new QQuickTextNodeEngine::BinaryTreeNode(*brect, *i, selState, a);
}

//  QQuickTextNodeEngine::BinaryTreeNode::~BinaryTreeNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeD1Ev(
    QQuickTextNodeEngine::BinaryTreeNode *self) {
  delete self;
}
