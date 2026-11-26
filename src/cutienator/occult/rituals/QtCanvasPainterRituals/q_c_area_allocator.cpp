//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcareaallocator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcareaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcareaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 10, as local:qcareaallocator.cpp:QCAreaAllocatorNode
struct QCAreaAllocatorNode
{
    enum class SplitType { VerticalSplit, HorizontalSplit };

    QCAreaAllocatorNode(QCAreaAllocatorNode *parent);
    ~QCAreaAllocatorNode();
    inline bool isLeaf();

    QCAreaAllocatorNode *parent = nullptr;
    QCAreaAllocatorNode *left = nullptr;
    QCAreaAllocatorNode *right = nullptr;
    int split; // only valid for inner nodes.
    SplitType splitType;
    bool isOccupied = false; // only valid for leaf nodes.
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 26, as local:qcareaallocator.cpp:QCAreaAllocatorNode::QCAreaAllocatorNode
inline QCAreaAllocatorNode::QCAreaAllocatorNode(QCAreaAllocatorNode *parent)
    : parent(parent)
{}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 30, as local:qcareaallocator.cpp:QCAreaAllocatorNode::~QCAreaAllocatorNode
inline QCAreaAllocatorNode::~QCAreaAllocatorNode()
{
    delete left;
    delete right;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 36, as local:qcareaallocator.cpp:QCAreaAllocatorNode::isLeaf
inline bool QCAreaAllocatorNode::isLeaf()
{
    Q_ASSERT((left != nullptr) == (right != nullptr));
    return !left;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 65, as _ZN15QCAreaAllocator14allocateInNodeE5QSizeR6QPoint5QRectP19QCAreaAllocatorNode
inline bool QCAreaAllocator::allocateInNode(
    QSize size, QPoint &result, QRect currentRect, QCAreaAllocatorNode *node)
{
    if (size.width() > currentRect.width() || size.height() > currentRect.height())
        return false;

    if (node->isLeaf()) {
        if (node->isOccupied)
            return false;
        const int maxMargin = 2;
        if (size.width() + maxMargin >= currentRect.width()
            && size.height() + maxMargin >= currentRect.height()) {
            // Snug fit, occupy entire rectangle.
            node->isOccupied = true;
            result = currentRect.topLeft();
            return true;
        }
        // TODO: Reuse nodes.
        // Split node.
        node->left = new QCAreaAllocatorNode(node);
        node->right = new QCAreaAllocatorNode(node);
        QRect splitRect = currentRect;
        if ((currentRect.width() - size.width()) * currentRect.height()
            < (currentRect.height() - size.height()) * currentRect.width()) {
            node->splitType = QCAreaAllocatorNode::SplitType::HorizontalSplit;
            node->split = currentRect.top() + size.height();
            splitRect.setHeight(size.height());
        } else {
            node->splitType = QCAreaAllocatorNode::SplitType::VerticalSplit;
            node->split = currentRect.left() + size.width();
            splitRect.setWidth(size.width());
        }
        return allocateInNode(size, result, splitRect, node->left);
    } else {
        // TODO: avoid unnecessary recursion.
        //  has been split.
        QRect leftRect = currentRect;
        QRect rightRect = currentRect;
        if (node->splitType == QCAreaAllocatorNode::SplitType::HorizontalSplit) {
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 118, as _ZN15QCAreaAllocator16deallocateInNodeE6QPointP19QCAreaAllocatorNode
inline bool QCAreaAllocator::deallocateInNode(QPoint pos, QCAreaAllocatorNode *node)
{
    while (!node->isLeaf()) {
        //  has been split.
        int cmp = node->splitType == QCAreaAllocatorNode::SplitType::HorizontalSplit ? pos.y()
                                                                                    : pos.x();
        node = cmp < node->split ? node->left : node->right;
    }
    if (!node->isOccupied)
        return false;
    node->isOccupied = false;
    mergeNodeWithNeighbors(node);
    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 133, as _ZN15QCAreaAllocator22mergeNodeWithNeighborsEP19QCAreaAllocatorNode
inline void QCAreaAllocator::mergeNodeWithNeighbors(QCAreaAllocatorNode *node)
{
    bool done = false;
    QCAreaAllocatorNode *parent = nullptr;
    QCAreaAllocatorNode *current = nullptr;
    QCAreaAllocatorNode *sibling;
    while (!done) {
        Q_ASSERT(node->isLeaf());
        Q_ASSERT(!node->isOccupied);
        if (node->parent == nullptr)
            return; // No neighbors.

        QCAreaAllocatorNode::SplitType splitType = QCAreaAllocatorNode::SplitType(
            node->parent->splitType);
        done = true;

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

            QCAreaAllocatorNode *neighbor = parent->left;
            while (neighbor->right && neighbor->splitType == splitType)
                neighbor = neighbor->right;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType
                && !neighbor->isOccupied) {
                // Left neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                QCAreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = nullptr;
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

            QCAreaAllocatorNode *neighbor = parent->right;
            while (neighbor->left && neighbor->splitType == splitType)
                neighbor = neighbor->left;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType
                && !neighbor->isOccupied) {
                // Right neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                QCAreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = nullptr;
                delete parent;
                delete neighbor;
                done = false;
            }
        }
    } // end while (!done)
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 42, as _ZN15QCAreaAllocatorC1E5QSize
inline QCAreaAllocator::QCAreaAllocator(QSize size)
    : m_size(size)
{
    m_root = new QCAreaAllocatorNode(nullptr);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 53, as _ZN15QCAreaAllocator8allocateE5QSize
inline QRect QCAreaAllocator::allocate(QSize size)
{
    QPoint point;
    bool result = allocateInNode(size, point, QRect(QPoint(0, 0), m_size), m_root);
    return result ? QRect(point, size) : QRect();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 60, as _ZN15QCAreaAllocator10deallocateE5QRect
inline bool QCAreaAllocator::deallocate(QRect rect)
{
    return deallocateInNode(rect.topLeft(), m_root);
}
//  -----------------------------------------------------------------------

//  QCAreaAllocator::QCAreaAllocator(QSize size)
extern "C" Q_DECL_EXPORT
QCAreaAllocator *ritual_ZN15QCAreaAllocatorC1E5QSize(const QSize *size) {
  return new QCAreaAllocator(*size);
}

//  QCAreaAllocator::~QCAreaAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCAreaAllocatorD1Ev(QCAreaAllocator *self) {
  delete self;
}

//  QRect QCAreaAllocator::allocate(QSize size)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15QCAreaAllocator8allocateE5QSize(
    QCAreaAllocator *self,
    const QSize *size) {
  return new QRect(self->allocate(*size));
}

//  bool QCAreaAllocator::deallocate(QRect rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QCAreaAllocator10deallocateE5QRect(
    QCAreaAllocator *self,
    const QRect *rect) {
  return self->deallocate(*rect);
}

//  bool QCAreaAllocator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCAreaAllocator7isEmptyEv(const QCAreaAllocator *self) {
  return self->isEmpty();
}

//  QSize QCAreaAllocator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCAreaAllocator4sizeEv(const QCAreaAllocator *self) {
  return new QSize(self->size());
}
