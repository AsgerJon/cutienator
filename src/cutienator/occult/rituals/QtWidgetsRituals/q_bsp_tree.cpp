//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbsptree_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qbsptree.cpp, line 96, as _ZN8QBspTree6insertER5QListIiERK5QRectjNS_4DataE
inline void QBspTree::insert(QList<int> &leaf, const QRect &, uint, QBspTreeData data)
{
    leaf.append(data.i);
}

//  from src/widgets/itemviews/qbsptree.cpp, line 42, as _ZN8QBspTree9climbTreeERK5QRectPFvR5QListIiES2_jNS_4DataEES6_i
inline void QBspTree::climbTree(const QRect &area, callback *function, QBspTreeData data, int index)
{
    if (index >= nodes.size()) { // the index points to a leaf
        Q_ASSERT(!nodes.isEmpty());
        function(leaf(index - nodes.size()), area, visited, data);
        return;
    }

    Node::Type t = (Node::Type) nodes.at(index).type;

    int pos = nodes.at(index).pos;
    int idx = firstChildIndex(index);
    if (t == Node::VerticalPlane) {
        if (area.left() < pos)
            climbTree(area, function, data, idx); // back
        if (area.right() >= pos)
            climbTree(area, function, data, idx + 1); // front
    } else {
        if (area.top() < pos)
            climbTree(area, function, data, idx); // back
        if (area.bottom() >= pos)
            climbTree(area, function, data, idx + 1); // front
    }
}

//  from src/widgets/itemviews/qbsptree.cpp, line 101, as _ZN8QBspTree6removeER5QListIiERK5QRectjNS_4DataE
inline void QBspTree::remove(QList<int> &leaf, const QRect &, uint, QBspTreeData data)
{
    int i = leaf.indexOf(data.i);
    if (i != -1)
        leaf.remove(i);
}

//  from src/widgets/itemviews/qbsptree.cpp, line 11, as _ZN8QBspTree6createEii
inline void QBspTree::create(int n, int d)
{
    // simple heuristics to find the best tree depth
    if (d == -1) {
        int c;
        for (c = 0; n; ++c)
            n = n / 10;
        depth = c << 1;
    } else {
        depth = d;
    }
    depth = qMax(depth, uint(1));

    nodes.resize((1ll << depth) - 1); // resize to number of nodes
    leaves.resize(1ll << depth); // resize to number of leaves
}

//  from src/widgets/itemviews/qbsptree.cpp, line 28, as _ZN8QBspTree7destroyEv
inline void QBspTree::destroy()
{
    leaves.clear();
    nodes.clear();
}

//  from src/widgets/itemviews/qbsptree.cpp, line 67, as _ZN8QBspTree4initERK5QRectiNS_4Node4TypeEi
inline void QBspTree::init(const QRect &area, int depth, NodeType type, int index)
{
    Node::Type t = Node::None; // t should never have this value
    if (type == Node::Both) // if both planes are specified, use 2d bsp
        t = (depth & 1) ? Node::HorizontalPlane : Node::VerticalPlane;
    else
        t = type;
    QPoint center = area.center();
    nodes[index].pos = (t == Node::VerticalPlane ? center.x() : center.y());
    nodes[index].type = t;

    QRect front = area;
    QRect back = area;

    if (t == Node::VerticalPlane) {
        front.setLeft(center.x());
        back.setRight(center.x() - 1); // front includes the center
    } else { // t == Node::HorizontalPlane
        front.setTop(center.y());
        back.setBottom(center.y() - 1);
    }

    int idx = firstChildIndex(index);
    if (--depth) {
        init(back, depth, type, idx);
        init(front, depth, type, idx + 1);
    }
}
//  -----------------------------------------------------------------------

//  void QBspTree::create(int n, int d)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree6createEii(QBspTree *self, int n, int d) {
  self->create(n, d);
}

//  void QBspTree::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree7destroyEv(QBspTree *self) {
  self->destroy();
}

//  void QBspTree::init(const QRect &area, NodeType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree4initERK5QRectNS_4Node4TypeE(
    QBspTree *self,
    const QRect *area,
    QBspTree::NodeType type) {
  self->init(*area, type);
}

//  int QBspTree::leafCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QBspTree9leafCountEv(const QBspTree *self) {
  return self->leafCount();
}

//  void QBspTree::insertLeaf(const QRect &r, int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree10insertLeafERK5QRecti(
    QBspTree *self,
    const QRect *r,
    int i) {
  self->insertLeaf(*r, i);
}

//  void QBspTree::removeLeaf(const QRect &r, int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree10removeLeafERK5QRecti(
    QBspTree *self,
    const QRect *r,
    int i) {
  self->removeLeaf(*r, i);
}

//  void QBspTree::init(const QRect &area, int depth, NodeType type, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree4initERK5QRectiNS_4Node4TypeEi(
    QBspTree *self,
    const QRect *area,
    int depth,
    QBspTree::NodeType type,
    int index) {
  self->init(*area, depth, type, index);
}

//  int QBspTree::parentIndex(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QBspTree11parentIndexEi(const QBspTree *self, int i) {
  return self->parentIndex(i);
}

//  int QBspTree::firstChildIndex(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QBspTree15firstChildIndexEi(const QBspTree *self, int i) {
  return self->firstChildIndex(i);
}

//  QBspTree::~QBspTree()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTreeD1Ev(QBspTree *self) {
  delete self;
}
