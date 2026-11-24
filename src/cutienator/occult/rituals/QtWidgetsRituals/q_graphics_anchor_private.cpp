//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicsanchorlayout.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicsanchorlayout_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qstack.h>
#ifdef QT_DEBUG
#include <QtCore/qfile.h>
#endif
#include <numeric>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1749, as _ZN28QGraphicsAnchorLayoutPrivate12removeAnchorEPN22QtGraphicsAnchorLayout12AnchorVertexES2_
inline void QGraphicsAnchorLayoutPrivate::removeAnchor(AnchorVertex *firstVertex,
                                                AnchorVertex *secondVertex)
{
    Q_Q(QGraphicsAnchorLayout);

    // Save references to items while it's safe to assume the vertices exist
    QGraphicsLayoutItem *firstItem = firstVertex->m_item;
    QGraphicsLayoutItem *secondItem = secondVertex->m_item;

    // Delete the anchor (may trigger deletion of center vertices)
    removeAnchor_helper(firstVertex, secondVertex);

    // Ensure no dangling pointer is left behind
    firstVertex = secondVertex = nullptr;

    // Checking if the item stays in the layout or not
    bool keepFirstItem = false;
    bool keepSecondItem = false;

    std::pair<AnchorVertex *, int> v;
    int refcount = -1;

    if (firstItem != q) {
        for (int i = Qt::AnchorLeft; i <= Qt::AnchorBottom; ++i) {
            v = m_vertexList.value(std::pair(firstItem, static_cast<Qt::AnchorPoint>(i)));
            if (v.first) {
                if (i == Qt::AnchorHorizontalCenter || i == Qt::AnchorVerticalCenter)
                    refcount = 2;
                else
                    refcount = 1;

                if (v.second > refcount) {
                    keepFirstItem = true;
                    break;
                }
            }
        }
    } else
        keepFirstItem = true;

    if (secondItem != q) {
        for (int i = Qt::AnchorLeft; i <= Qt::AnchorBottom; ++i) {
            v = m_vertexList.value(std::pair(secondItem, static_cast<Qt::AnchorPoint>(i)));
            if (v.first) {
                if (i == Qt::AnchorHorizontalCenter || i == Qt::AnchorVerticalCenter)
                    refcount = 2;
                else
                    refcount = 1;

                if (v.second > refcount) {
                    keepSecondItem = true;
                    break;
                }
            }
        }
    } else
        keepSecondItem = true;

    if (!keepFirstItem)
        q->removeAt(items.indexOf(firstItem));

    if (!keepSecondItem)
        q->removeAt(items.indexOf(secondItem));

    // Removing anchors invalidates the layout
    q->invalidate();
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1823, as _ZN28QGraphicsAnchorLayoutPrivate19removeAnchor_helperEPN22QtGraphicsAnchorLayout12AnchorVertexES2_
inline void QGraphicsAnchorLayoutPrivate::removeAnchor_helper(AnchorVertex *v1, AnchorVertex *v2)
{
    Q_ASSERT(v1 && v2);

    // Remove edge from graph
    const Qt::Orientation o = edgeOrientation(v1->m_edge);
    graph[o].removeEdge(v1, v2);

    // Decrease vertices reference count (may trigger a deletion)
    removeInternalVertex(v1->m_item, v1->m_edge);
    removeInternalVertex(v2->m_item, v2->m_edge);
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1307, as _ZN28QGraphicsAnchorLayoutPrivate15edgeOrientationEN2Qt11AnchorPointE
inline Qt::Orientation
QGraphicsAnchorLayoutPrivate::edgeOrientation(Qt::AnchorPoint edge) noexcept
{
    return edge > Qt::AnchorRight ? Qt::Vertical : Qt::Horizontal;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1857, as _ZN28QGraphicsAnchorLayoutPrivate20removeInternalVertexEP19QGraphicsLayoutItemN2Qt11AnchorPointE
inline void QGraphicsAnchorLayoutPrivate::removeInternalVertex(QGraphicsLayoutItem *item,
                                                        Qt::AnchorPoint edge)
{
    std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> pair(item, edge);
    std::pair<AnchorVertex *, int> v = m_vertexList.value(pair);

    if (!v.first) {
        qWarning("This item with this edge is not in the graph");
        return;
    }

    v.second--;
    if (v.second == 0) {
        // Remove reference and delete vertex
        m_vertexList.remove(pair);
        delete v.first;
    } else {
        // Update reference count
        m_vertexList.insert(pair, v);

        if ((v.second == 2) &&
            ((edge == Qt::AnchorHorizontalCenter) ||
             (edge == Qt::AnchorVerticalCenter))) {
            removeCenterAnchors(item, edge, true);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1454, as _ZN28QGraphicsAnchorLayoutPrivate19removeCenterAnchorsEP19QGraphicsLayoutItemN2Qt11AnchorPointEb
inline void QGraphicsAnchorLayoutPrivate::removeCenterAnchors(
    QGraphicsLayoutItem *item, Qt::AnchorPoint centerEdge,
    bool substitute)
{
    Q_Q(QGraphicsAnchorLayout);

    Qt::Orientation orientation;
    switch (centerEdge) {
    case Qt::AnchorHorizontalCenter:
        orientation = Qt::Horizontal;
        break;
    case Qt::AnchorVerticalCenter:
        orientation = Qt::Vertical;
        break;
    default:
        // Don't remove edges that not the center ones
        return;
    }

    // Orientation code
    Qt::AnchorPoint firstEdge;
    Qt::AnchorPoint lastEdge;

    if (orientation == Qt::Horizontal) {
        firstEdge = Qt::AnchorLeft;
        lastEdge = Qt::AnchorRight;
    } else {
        firstEdge = Qt::AnchorTop;
        lastEdge = Qt::AnchorBottom;
    }

    AnchorVertex *center = internalVertex(item, centerEdge);
    if (!center)
        return;
    AnchorVertex *first = internalVertex(item, firstEdge);

    Q_ASSERT(first);
    Q_ASSERT(center);

    Graph<AnchorVertex, AnchorData> &g = graph[orientation];


    AnchorData *oldData = g.edgeData(first, center);
    // Remove center constraint
    for (int i = itemCenterConstraints[orientation].size() - 1; i >= 0; --i) {
        if (itemCenterConstraints[orientation].at(i)->variables.contains(oldData)) {
            delete itemCenterConstraints[orientation].takeAt(i);
            break;
        }
    }

    if (substitute) {
        // Create the new anchor that should substitute the left-center-right anchors.
        AnchorData *data = new AnchorData;
        addAnchor_helper(item, firstEdge, item, lastEdge, data);
        data->refreshSizeHints();

        // Remove old anchors
        removeAnchor_helper(first, center);
        removeAnchor_helper(center, internalVertex(item, lastEdge));

    } else {
        // this is only called from removeAnchors()
        // first, remove all non-internal anchors
        QList<AnchorVertex*> adjacents = g.adjacentVertices(center);
        for (int i = 0; i < adjacents.size(); ++i) {
            AnchorVertex *v = adjacents.at(i);
            if (v->m_item != item) {
                removeAnchor_helper(center, internalVertex(v->m_item, v->m_edge));
            }
        }
        // when all non-internal anchors is removed it will automatically merge the
        // center anchor into a left-right (or top-bottom) anchor. We must also delete that.
        // by this time, the center vertex is deleted and merged into a non-centered internal anchor
        removeAnchor_helper(first, internalVertex(item, lastEdge));
    }

    if (item == q) {
        layoutCentralVertex[orientation] = nullptr;
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 36, as _ZN22QGraphicsAnchorPrivateD1Ev
inline QGraphicsAnchorPrivate::~QGraphicsAnchorPrivate()
{
    if (data) {
        // The QGraphicsAnchor was already deleted at this moment. We must clean
        // the dangling pointer to avoid double deletion in the AnchorData dtor.
        data->graphicsAnchor = nullptr;

        layoutPrivate->removeAnchor(data->from, data->to);
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 55, as _ZN22QGraphicsAnchorPrivate10setSpacingEd
inline void QGraphicsAnchorPrivate::setSpacing(qreal value)
{
    if (!data) {
        qWarning("QGraphicsAnchor::setSpacing: The anchor does not exist.");
        return;
    }

    if (hasSize && (preferredSize == value))
        return;

    // The anchor has an user-defined size
    hasSize = true;
    preferredSize = value;

    layoutPrivate->q_func()->invalidate();
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 72, as _ZN22QGraphicsAnchorPrivate12unsetSpacingEv
inline void QGraphicsAnchorPrivate::unsetSpacing()
{
    if (!data) {
        qWarning("QGraphicsAnchor::setSpacing: The anchor does not exist.");
        return;
    }

    // Return to standard direction
    hasSize = false;

    layoutPrivate->q_func()->invalidate();
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 85, as _ZNK22QGraphicsAnchorPrivate7spacingEv
inline qreal QGraphicsAnchorPrivate::spacing() const
{
    if (!data) {
        qWarning("QGraphicsAnchor::setSpacing: The anchor does not exist.");
        return 0;
    }

    return preferredSize;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 47, as _ZN22QGraphicsAnchorPrivate13setSizePolicyEN11QSizePolicy6PolicyE
inline void QGraphicsAnchorPrivate::setSizePolicy(QSizePolicy::Policy policy)
{
    if (sizePolicy != policy) {
        sizePolicy = policy;
        layoutPrivate->q_func()->invalidate();
    }
}
//  -----------------------------------------------------------------------

//  QGraphicsAnchor *QGraphicsAnchorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN22QGraphicsAnchorPrivate6q_funcEv(
    QGraphicsAnchorPrivate *self) {
  return self->q_func();
}

//  const QGraphicsAnchor *QGraphicsAnchorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsAnchor *ritual_ZNK22QGraphicsAnchorPrivate6q_funcEv(
    const QGraphicsAnchorPrivate *self) {
  return self->q_func();
}

//  QGraphicsAnchorPrivate::~QGraphicsAnchorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsAnchorPrivateD1Ev(QGraphicsAnchorPrivate *self) {
  delete self;
}

//  void QGraphicsAnchorPrivate::setSpacing(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsAnchorPrivate10setSpacingEd(
    QGraphicsAnchorPrivate *self,
    qreal value) {
  self->setSpacing(value);
}

//  void QGraphicsAnchorPrivate::unsetSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsAnchorPrivate12unsetSpacingEv(
    QGraphicsAnchorPrivate *self) {
  self->unsetSpacing();
}

//  qreal QGraphicsAnchorPrivate::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsAnchorPrivate7spacingEv(
    const QGraphicsAnchorPrivate *self) {
  return self->spacing();
}

//  void QGraphicsAnchorPrivate::setSizePolicy(QSizePolicy::Policy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsAnchorPrivate13setSizePolicyEN11QSizePolicy6PolicyE(
    QGraphicsAnchorPrivate *self,
    QSizePolicy::Policy policy) {
  self->setSizePolicy(policy);
}

//  QGraphicsAnchorPrivate *QGraphicsAnchorPrivate::get(QGraphicsAnchor *q)
extern "C" Q_DECL_EXPORT
QGraphicsAnchorPrivate *ritual_ZN22QGraphicsAnchorPrivate3getEP15QGraphicsAnchor(
    QGraphicsAnchor *q) {
  return QGraphicsAnchorPrivate::get(q);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
