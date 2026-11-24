//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextnodeengine_p.h>
#include <QtCore/qpoint.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qrawfont.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextlayout.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qimageiohandler.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qtextimagehandler_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtGui/private/qglyphrun_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgdistancefieldglyphnode_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 60, as _ZN20QQuickTextNodeEngine17BinaryTreeNodeKeyC1EPNS_14BinaryTreeNodeE
inline QQuickTextNodeEngine::BinaryTreeNodeKey::BinaryTreeNodeKey(BinaryTreeNode *node)
    : fontEngine(QRawFontPrivate::get(node->glyphRun.rawFont())->fontEngine)
    , clipNode(node->clipNode)
    , color(node->color.rgba())
    , selectionState(node->selectionState)
{
}
//  -----------------------------------------------------------------------

//  QQuickTextNodeEngine::BinaryTreeNodeKey::BinaryTreeNodeKey(BinaryTreeNode
//      *node)
extern "C" Q_DECL_EXPORT
QQuickTextNodeEngine::BinaryTreeNodeKey *ritual_ZN20QQuickTextNodeEngine17BinaryTreeNodeKeyC1EPNS_14BinaryTreeNodeE(
    QQuickTextNodeEngine::BinaryTreeNode *node) {
  return new QQuickTextNodeEngine::BinaryTreeNodeKey(node);
}

//  bool QQuickTextNodeEngine::BinaryTreeNodeKey::operator==(const
//      BinaryTreeNodeKey &otherKey) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickTextNodeEngine17BinaryTreeNodeKeyeqERKS0_(
    const QQuickTextNodeEngine::BinaryTreeNodeKey *self,
    const QQuickTextNodeEngine::BinaryTreeNodeKey *otherKey) {
  return self->operator==(*otherKey);
}

//  QQuickTextNodeEngine::BinaryTreeNodeKey::~BinaryTreeNodeKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine17BinaryTreeNodeKeyD1Ev(
    QQuickTextNodeEngine::BinaryTreeNodeKey *self) {
  delete self;
}
