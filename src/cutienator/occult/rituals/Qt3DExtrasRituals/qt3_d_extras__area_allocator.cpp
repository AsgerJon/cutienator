//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/areaallocator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/areaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/areaallocator_p.h>
#include <QtCore/qglobal.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 18, as local:areaallocator.cpp:SplitType
namespace Qt3DExtras {
enum SplitType
{
    VerticalSplit,
    HorizontalSplit
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 24, as local:areaallocator.cpp:maxMargin
namespace Qt3DExtras {
static const int maxMargin = 2;
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 26, as local:areaallocator.cpp:AreaAllocatorNode
namespace Qt3DExtras {
struct AreaAllocatorNode
{
    AreaAllocatorNode(AreaAllocatorNode *parent);
    ~AreaAllocatorNode();
    inline bool isLeaf();

    AreaAllocatorNode *parent;
    AreaAllocatorNode *left;
    AreaAllocatorNode *right;
    int split; // only valid for inner nodes.
    SplitType splitType;
    bool isOccupied; // only valid for leaf nodes.
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 40, as local:areaallocator.cpp:AreaAllocatorNode::AreaAllocatorNode
namespace Qt3DExtras {
inline AreaAllocatorNode::AreaAllocatorNode(AreaAllocatorNode *parent)
    : parent(parent)
    , left(0)
    , right(0)
    , isOccupied(false)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 48, as local:areaallocator.cpp:AreaAllocatorNode::~AreaAllocatorNode
namespace Qt3DExtras {
inline AreaAllocatorNode::~AreaAllocatorNode()
{
    delete left;
    delete right;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 54, as local:areaallocator.cpp:AreaAllocatorNode::isLeaf
namespace Qt3DExtras {
inline bool AreaAllocatorNode::isLeaf()
{
    Q_ASSERT((left != 0) == (right != 0));
    return !left;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 83, as _ZN10Qt3DExtras13AreaAllocator14allocateInNodeERK5QSizeR6QPointRK5QRectPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline bool AreaAllocator::allocateInNode(const QSize &size, QPoint &result, const QRect &currentRect, AreaAllocatorNode *node)
{
    if (size.width() > currentRect.width() || size.height() > currentRect.height())
        return false;

    if (node->isLeaf()) {
        if (node->isOccupied)
            return false;
        if (size.width() + maxMargin >= currentRect.width() && size.height() + maxMargin >= currentRect.height()) {
            //Snug fit, occupy entire rectangle.
            node->isOccupied = true;
            result = currentRect.topLeft();
            return true;
        }
        // TODO: Reuse nodes.
        // Split node.
        node->left = new AreaAllocatorNode(node);
        node->right = new AreaAllocatorNode(node);
        QRect splitRect = currentRect;
        if ((currentRect.width() - size.width()) * currentRect.height() < (currentRect.height() - size.height()) * currentRect.width()) {
            node->splitType = HorizontalSplit;
            node->split = currentRect.top() + size.height();
            splitRect.setHeight(size.height());
        } else {
            node->splitType = VerticalSplit;
            node->split = currentRect.left() + size.width();
            splitRect.setWidth(size.width());
        }
        return allocateInNode(size, result, splitRect, node->left);
    } else {
        // TODO: avoid unnecessary recursion.
        //  has been split.
        QRect leftRect = currentRect;
        QRect rightRect = currentRect;
        if (node->splitType == HorizontalSplit) {
            leftRect.setHeight(node->split - leftRect.top());
            rightRect.setTop(node->split);
        } else {
            leftRect.setWidth(node->split - leftRect.left());
            rightRect.setLeft(node->split);
        }
        if (allocateInNode(size, result, leftRect, node->left))
            return true;
        if (allocateInNode(size, result, rightRect, node->right))
            return true;
        return false;
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 132, as _ZN10Qt3DExtras13AreaAllocator16deallocateInNodeERK6QPointPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline bool AreaAllocator::deallocateInNode(const QPoint &pos, AreaAllocatorNode *node)
{
    while (!node->isLeaf()) {
        //  has been split.
        int cmp = node->splitType == HorizontalSplit ? pos.y() : pos.x();
        node = cmp < node->split ? node->left : node->right;
    }
    if (!node->isOccupied)
        return false;
    node->isOccupied = false;
    mergeNodeWithNeighbors(node);
    return true;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 146, as _ZN10Qt3DExtras13AreaAllocator22mergeNodeWithNeighborsEPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline void AreaAllocator::mergeNodeWithNeighbors(AreaAllocatorNode *node)
{
    bool done = false;
    AreaAllocatorNode *parent = 0;
    AreaAllocatorNode *current = 0;
    AreaAllocatorNode *sibling;
    while (!done) {
        Q_ASSERT(node->isLeaf());
        Q_ASSERT(!node->isOccupied);
        if (node->parent == 0)
            return; // No neighbors.

        SplitType splitType = SplitType(node->parent->splitType);
        done = true;

        /* Special case. Might be faster than going through the general code path.
        // Merge with sibling.
        parent = node->parent;
        sibling = (node == parent->left ? parent->right : parent->left);
        if (sibling->isLeaf() && !sibling->isOccupied) {
            Q_ASSERT(!sibling->right);
            node = parent;
            parent->isOccupied = false;
            delete parent->left;
            delete parent->right;
            parent->left = parent->right = 0;
            done = false;
            continue;
        }
        */

        // Merge with left neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->left && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->right);
            Q_ASSERT(parent->left);

            AreaAllocatorNode *neighbor = parent->left;
            while (neighbor->right && neighbor->splitType == splitType)
                neighbor = neighbor->right;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType && !neighbor->isOccupied) {
                // Left neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                AreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = 0;
                delete parent;
                delete neighbor;
                done = false;
            }
        }

        // Merge with right neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->right && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->left);
            Q_ASSERT(parent->right);

            AreaAllocatorNode *neighbor = parent->right;
            while (neighbor->left && neighbor->splitType == splitType)
                neighbor = neighbor->left;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType && !neighbor->isOccupied) {
                // Right neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                AreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = 0;
                delete parent;
                delete neighbor;
                done = false;
            }
        }
    } // end while (!done)
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 61, as _ZN10Qt3DExtras13AreaAllocatorC1ERK5QSize
namespace Qt3DExtras {
inline AreaAllocator::AreaAllocator(const QSize &size) : m_size(size)
{
    m_root = new AreaAllocatorNode(0);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 66, as _ZN10Qt3DExtras13AreaAllocatorD1Ev
namespace Qt3DExtras {
inline AreaAllocator::~AreaAllocator()
{
    delete m_root;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 71, as _ZN10Qt3DExtras13AreaAllocator8allocateERK5QSize
namespace Qt3DExtras {
inline QRect AreaAllocator::allocate(const QSize &size)
{
    QPoint point;
    bool result = allocateInNode(size, point, QRect(QPoint(0, 0), m_size), m_root);
    return result ? QRect(point, size) : QRect();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 78, as _ZN10Qt3DExtras13AreaAllocator10deallocateERK5QRect
namespace Qt3DExtras {
inline bool AreaAllocator::deallocate(const QRect &rect)
{
    return deallocateInNode(rect.topLeft(), m_root);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DExtras::AreaAllocator::AreaAllocator(const QSize &size)
extern "C" Q_DECL_EXPORT
Qt3DExtras::AreaAllocator *ritual_ZN10Qt3DExtras13AreaAllocatorC1ERK5QSize(
    const QSize *size) {
  return new Qt3DExtras::AreaAllocator(*size);
}

//  Qt3DExtras::AreaAllocator::~AreaAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13AreaAllocatorD1Ev(
    Qt3DExtras::AreaAllocator *self) {
  delete self;
}

//  QRect Qt3DExtras::AreaAllocator::allocate(const QSize &size)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN10Qt3DExtras13AreaAllocator8allocateERK5QSize(
    Qt3DExtras::AreaAllocator *self,
    const QSize *size) {
  return new QRect(self->allocate(*size));
}

//  bool Qt3DExtras::AreaAllocator::deallocate(const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DExtras13AreaAllocator10deallocateERK5QRect(
    Qt3DExtras::AreaAllocator *self,
    const QRect *rect) {
  return self->deallocate(*rect);
}

//  bool Qt3DExtras::AreaAllocator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13AreaAllocator7isEmptyEv(
    const Qt3DExtras::AreaAllocator *self) {
  return self->isEmpty();
}

//  QSize Qt3DExtras::AreaAllocator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras13AreaAllocator4sizeEv(
    const Qt3DExtras::AreaAllocator *self) {
  return new QSize(self->size());
}
