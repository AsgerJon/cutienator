//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_bsp_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_bsp_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicsscene_bsp_p.h>
#include <QtCore/qstring.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 13, as _ZN21QGraphicsSceneBspTreeC1Ev
inline QGraphicsSceneBspTree::QGraphicsSceneBspTree()
    : leafCnt(0)
{
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 18, as _ZN21QGraphicsSceneBspTreeD1Ev
inline QGraphicsSceneBspTree::~QGraphicsSceneBspTree()
{
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 22, as _ZN21QGraphicsSceneBspTree10initializeERK6QRectFi
inline void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth)
{
    this->rect = rect;
    leafCnt = 0;
    nodes.resize((1 << (depth + 1)) - 1);
    nodes.fill(Node());
    leaves.resize(1ll << depth);
    leaves.fill(QList<QGraphicsItem *>());

    initialize(rect, depth, 0);
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 34, as _ZN21QGraphicsSceneBspTree5clearEv
inline void QGraphicsSceneBspTree::clear()
{
    leafCnt = 0;
    nodes.clear();
    leaves.clear();
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 55, as _ZN21QGraphicsSceneBspTree11removeItemsERK4QSetIP13QGraphicsItemE
inline void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem *> &items)
{
    for (int i = 0; i < leaves.size(); ++i) {
        QList<QGraphicsItem *> newItemList;
        const QList<QGraphicsItem *> &oldItemList = leaves[i];
        for (int j = 0; j < oldItemList.size(); ++j) {
            QGraphicsItem *item = oldItemList.at(j);
            if (!items.contains(item))
                newItemList << item;
        }
        leaves[i] = newItemList;
    }
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 89, as _ZNK21QGraphicsSceneBspTree9leafCountEv
inline int QGraphicsSceneBspTree::leafCount() const
{
    return leafCnt;
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 94, as _ZNK21QGraphicsSceneBspTree5debugEi
inline QString QGraphicsSceneBspTree::debug(int index) const
{
    const Node *node = &nodes.at(index);

    QString tmp;
    if (node->type == Node::Leaf) {
        QRectF rect = rectForIndex(index);
        if (!leaves[node->leafIndex].isEmpty()) {
            tmp += QString::fromLatin1("[%1, %2, %3, %4] contains %5 items\n")
                   .arg(rect.left()).arg(rect.top())
                   .arg(rect.width()).arg(rect.height())
                   .arg(leaves[node->leafIndex].size());
        }
    } else {
        if (node->type == Node::Horizontal) {
            tmp += debug(firstChildIndex(index));
            tmp += debug(firstChildIndex(index) + 1);
        } else {
            tmp += debug(firstChildIndex(index));
            tmp += debug(firstChildIndex(index) + 1);
        }
    }

    return tmp;
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 120, as _ZN21QGraphicsSceneBspTree10initializeERK6QRectFii
inline void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth, int index)
{
    Node *node = &nodes[index];
    if (index == 0) {
        node->type = Node::Horizontal;
        node->offset = rect.center().y();
    }

    if (depth) {
        Node::Type type;
        QRectF rect1, rect2;
        qreal offset1, offset2;

        if (node->type == Node::Horizontal) {
            type = Node::Vertical;
            rect1.setRect(rect.left(), rect.top(), rect.width(), rect.height() / 2);
            rect2.setRect(rect1.left(), rect1.bottom(), rect1.width(), rect.height() - rect1.height());
            offset1 = rect1.center().x();
            offset2 = rect2.center().x();
        } else {
            type = Node::Horizontal;
            rect1.setRect(rect.left(), rect.top(), rect.width() / 2, rect.height());
            rect2.setRect(rect1.right(), rect1.top(), rect.width() - rect1.width(), rect1.height());
            offset1 = rect1.center().y();
            offset2 = rect2.center().y();
        }

        int childIndex = firstChildIndex(index);

        Node *child = &nodes[childIndex];
        child->offset = offset1;
        child->type = type;

        child = &nodes[childIndex + 1];
        child->offset = offset2;
        child->type = type;

        initialize(rect1, depth - 1, childIndex);
        initialize(rect2, depth - 1, childIndex + 1);
    } else {
        node->type = Node::Leaf;
        node->leafIndex = leafCnt++;
    }
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 199, as _ZNK21QGraphicsSceneBspTree12rectForIndexEi
inline QRectF QGraphicsSceneBspTree::rectForIndex(int index) const
{
    if (index <= 0)
        return rect;

    int parentIdx = parentIndex(index);
    QRectF rect = rectForIndex(parentIdx);
    const Node *parent = &nodes.at(parentIdx);

    if (parent->type == Node::Vertical) {
        if (index & 1)
            rect.setRight(parent->offset);
        else
            rect.setLeft(parent->offset);
    } else {
        if (index & 1)
            rect.setBottom(parent->offset);
        else
            rect.setTop(parent->offset);
    }

    return rect;
}
//  -----------------------------------------------------------------------

//  QGraphicsSceneBspTree::QGraphicsSceneBspTree()
extern "C" Q_DECL_EXPORT
QGraphicsSceneBspTree *ritual_ZN21QGraphicsSceneBspTreeC1Ev() {
  return new QGraphicsSceneBspTree();
}

//  QGraphicsSceneBspTree::~QGraphicsSceneBspTree()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsSceneBspTreeD1Ev(QGraphicsSceneBspTree *self) {
  delete self;
}

//  void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsSceneBspTree10initializeERK6QRectFi(
    QGraphicsSceneBspTree *self,
    const QRectF *rect,
    int depth) {
  self->initialize(*rect, depth);
}

//  void QGraphicsSceneBspTree::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsSceneBspTree5clearEv(QGraphicsSceneBspTree *self) {
  self->clear();
}

//  void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem *>
//      &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsSceneBspTree11removeItemsERK4QSetIP13QGraphicsItemE(
    QGraphicsSceneBspTree *self,
    const QSet<QGraphicsItem *> *items) {
  self->removeItems(*items);
}

//  int QGraphicsSceneBspTree::leafCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsSceneBspTree9leafCountEv(
    const QGraphicsSceneBspTree *self) {
  return self->leafCount();
}

//  int QGraphicsSceneBspTree::firstChildIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsSceneBspTree15firstChildIndexEi(
    const QGraphicsSceneBspTree *self,
    int index) {
  return self->firstChildIndex(index);
}

//  int QGraphicsSceneBspTree::parentIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsSceneBspTree11parentIndexEi(
    const QGraphicsSceneBspTree *self,
    int index) {
  return self->parentIndex(index);
}

//  QString QGraphicsSceneBspTree::debug(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QGraphicsSceneBspTree5debugEi(
    const QGraphicsSceneBspTree *self,
    int index) {
  return new QString(self->debug(index));
}

//  void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsSceneBspTree10initializeERK6QRectFii(
    QGraphicsSceneBspTree *self,
    const QRectF *rect,
    int depth,
    int index) {
  self->initialize(*rect, depth, index);
}

//  QRectF QGraphicsSceneBspTree::rectForIndex(int index) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QGraphicsSceneBspTree12rectForIndexEi(
    const QGraphicsSceneBspTree *self,
    int index) {
  return new QRectF(self->rectForIndex(index));
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
