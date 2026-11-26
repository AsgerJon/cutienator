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
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 68, as _ZN20QQuickTextNodeEngine14BinaryTreeNodeC1ERK9QGlyphRunNS_14SelectionStateERK6QRectFRK6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSH_SH_RK7QPointFd
inline QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const QGlyphRun &g,
                                                     SelectionState selState,
                                                     const QRectF &brect,
                                                     const Decorations &decs,
                                                     QTextCharFormat::UnderlineStyle us,
                                                     const QColor &c,
                                                     const QColor &bc, const QColor &dc,
                                                     const QPointF &pos, qreal a)
    : glyphRun(g)
    , boundingRect(brect)
    , selectionState(selState)
    , clipNode(nullptr)
    , decorations(decs)
    , underlineStyle(us)
    , color(c)
    , backgroundColor(bc)
    , decorationColor(dc)
    , position(pos)
    , ascent(a)
    , leftChildIndex(-1)
    , rightChildIndex(-1)
{
    QGlyphRunPrivate *d = QGlyphRunPrivate::get(g);
    ranges.append(std::make_pair(d->textRangeStart, d->textRangeEnd));
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 94, as _ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERK9QGlyphRunNS_14SelectionStateE6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSF_SF_RK7QPointF
inline void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QGlyphRun &glyphRun, SelectionState selectionState,
                                             Decorations decorations, QTextCharFormat::UnderlineStyle underlineStyle, const QColor &textColor,
                                             const QColor &backgroundColor, const QColor &decorationColor, const QPointF &position)
{
    QRectF searchRect = glyphRun.boundingRect();
    searchRect.translate(position);

    if (qFuzzyIsNull(searchRect.width()) || qFuzzyIsNull(searchRect.height()))
        return;

    if (glyphRun.underline() || underlineStyle != QTextCharFormat::NoUnderline)
        decorations |= Decoration::Underline;
    decorations |= (glyphRun.overline()  ? Decoration::Overline  : Decoration::NoDecoration);
    decorations |= (glyphRun.strikeOut() ? Decoration::StrikeOut : Decoration::NoDecoration);
    decorations |= (backgroundColor.isValid() ? Decoration::Background : Decoration::NoDecoration);

    qreal ascent = glyphRun.rawFont().ascent();
    insert(binaryTree, BinaryTreeNode(glyphRun,
                                      selectionState,
                                      searchRect,
                                      decorations,
                                      underlineStyle,
                                      textColor,
                                      backgroundColor,
                                      decorationColor,
                                      position,
                                      ascent));
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 123, as _ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERKS0_
inline void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const BinaryTreeNode &binaryTreeNode)
{
    int newIndex = binaryTree->size();
    binaryTree->append(binaryTreeNode);
    if (newIndex == 0)
        return;

    int searchIndex = 0;
    forever {
        BinaryTreeNode *node = binaryTree->data() + searchIndex;
        if (binaryTreeNode.boundingRect.left() < node->boundingRect.left()) {
            if (node->leftChildIndex < 0) {
                node->leftChildIndex = newIndex;
                break;
            } else {
                searchIndex = node->leftChildIndex;
            }
        } else {
            if (node->rightChildIndex < 0) {
                node->rightChildIndex = newIndex;
                break;
            } else {
                searchIndex = node->rightChildIndex;
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 151, as _ZN20QQuickTextNodeEngine14BinaryTreeNode7inOrderERK15QVarLengthArrayIS0_Lx16EEPS1_IiLx256EEi
inline void QQuickTextNodeEngine::BinaryTreeNode::inOrder(const QVarLengthArray<BinaryTreeNode, 16> &binaryTree,
                                              QVarLengthArray<int> *sortedIndexes, int currentIndex)
{
    Q_ASSERT(currentIndex < binaryTree.size());

    const BinaryTreeNode *node = binaryTree.data() + currentIndex;
    if (node->leftChildIndex >= 0)
        inOrder(binaryTree, sortedIndexes, node->leftChildIndex);

    sortedIndexes->append(currentIndex);

    if (node->rightChildIndex >= 0)
        inOrder(binaryTree, sortedIndexes, node->rightChildIndex);
}
//  -----------------------------------------------------------------------

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

//  QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const QGlyphRun &g,
//      SelectionState selState, const QRectF &brect, const Decorations
//      &decs, QTextCharFormat::UnderlineStyle us, const QColor &c, const
//      QColor &bc, const QColor &dc, const QPointF &pos, qreal a)
extern "C" Q_DECL_EXPORT
QQuickTextNodeEngine::BinaryTreeNode *ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeC1ERK9QGlyphRunNS_14SelectionStateERK6QRectFRK6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSH_SH_RK7QPointFd(
    const QGlyphRun *g,
    QQuickTextNodeEngine::SelectionState selState,
    const QRectF *brect,
    const QQuickTextNodeEngine::Decorations *decs,
    QTextCharFormat::UnderlineStyle us,
    const QColor *c,
    const QColor *bc,
    const QColor *dc,
    const QPointF *pos,
    qreal a) {
  return new QQuickTextNodeEngine::BinaryTreeNode(
      *g,
      selState,
      *brect,
      *decs,
      us,
      *c,
      *bc,
      *dc,
      *pos,
      a);
}

//  void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryT
//      reeNode, 16> *binaryTree, const QRectF &rect, const QImage &image,
//      qreal ascent, SelectionState selectionState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERK6QRectFRK6QImagedNS_14SelectionStateE(
    QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16> *binaryTree,
    const QRectF *rect,
    const QImage *image,
    qreal ascent,
    QQuickTextNodeEngine::SelectionState selectionState) {
  QQuickTextNodeEngine::BinaryTreeNode::insert(
      binaryTree,
      *rect,
      *image,
      ascent,
      selectionState);
}

//  void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryT
//      reeNode, 16> *binaryTree, const QGlyphRun &glyphRun, SelectionState
//      selectionState, Decorations decorations,
//      QTextCharFormat::UnderlineStyle underlineStyle, const QColor
//      &textColor, const QColor &backgroundColor, const QColor
//      &underlineColor, const QPointF &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERK9QGlyphRunNS_14SelectionStateE6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSF_SF_RK7QPointF(
    QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16> *binaryTree,
    const QGlyphRun *glyphRun,
    QQuickTextNodeEngine::SelectionState selectionState,
    int decorations,
    QTextCharFormat::UnderlineStyle underlineStyle,
    const QColor *textColor,
    const QColor *backgroundColor,
    const QColor *underlineColor,
    const QPointF *position) {
  QQuickTextNodeEngine::BinaryTreeNode::insert(
      binaryTree,
      *glyphRun,
      selectionState,
      QFlags<QQuickTextNodeEngine::Decoration>::fromInt(decorations),
      underlineStyle,
      *textColor,
      *backgroundColor,
      *underlineColor,
      *position);
}

//  void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryT
//      reeNode, 16> *binaryTree, const BinaryTreeNode &binaryTreeNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERKS0_(
    QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16> *binaryTree,
    const QQuickTextNodeEngine::BinaryTreeNode *binaryTreeNode) {
  QQuickTextNodeEngine::BinaryTreeNode::insert(binaryTree, *binaryTreeNode);
}

//  void QQuickTextNodeEngine::BinaryTreeNode::inOrder(const
//      QVarLengthArray<BinaryTreeNode, 16> &binaryTree, QVarLengthArray<int>
//      *sortedIndexes, int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNode7inOrderERK15QVarLengthArrayIS0_Lx16EEPS1_IiLx256EEi(
    const QVarLengthArray<QQuickTextNodeEngine::BinaryTreeNode, 16> *binaryTree,
    QVarLengthArray<int> *sortedIndexes,
    int currentIndex) {
  QQuickTextNodeEngine::BinaryTreeNode::inOrder(
      *binaryTree,
      sortedIndexes,
      currentIndex);
}

//  QQuickTextNodeEngine::BinaryTreeNode::~BinaryTreeNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14BinaryTreeNodeD1Ev(
    QQuickTextNodeEngine::BinaryTreeNode *self) {
  delete self;
}
