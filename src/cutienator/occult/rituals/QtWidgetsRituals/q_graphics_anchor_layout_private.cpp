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
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtCore/QtDebug>
#include <QtWidgets/private/qgraphicsanchorlayout_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qstack.h>
#ifdef QT_DEBUG
#include <QtCore/qfile.h>
#endif
#include <numeric>
#include <QtCore/qglobal.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 73, as _ZN26QGraphicsLayoutItemPrivateC2EP19QGraphicsLayoutItemb
inline QGraphicsLayoutItemPrivate::QGraphicsLayoutItemPrivate(QGraphicsLayoutItem *par, bool layout)
    : parent(par), userSizeHints(nullptr), isLayout(layout), ownedByLayout(false), graphicsItem(nullptr)
{
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 81, as _ZN26QGraphicsLayoutItemPrivateD2Ev
inline QGraphicsLayoutItemPrivate::~QGraphicsLayoutItemPrivate()
{
    // Remove any lazily allocated data
    delete[] userSizeHints;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1674, as _ZN28QGraphicsAnchorLayoutPrivate16addAnchor_helperEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_PN22QtGraphicsAnchorLayout10AnchorDataE
inline void QGraphicsAnchorLayoutPrivate::addAnchor_helper(QGraphicsLayoutItem *firstItem,
                                                    Qt::AnchorPoint firstEdge,
                                                    QGraphicsLayoutItem *secondItem,
                                                    Qt::AnchorPoint secondEdge,
                                                    AnchorData *data)
{
    Q_Q(QGraphicsAnchorLayout);

    const Qt::Orientation orientation = edgeOrientation(firstEdge);

    // Create or increase the reference count for the related vertices.
    AnchorVertex *v1 = addInternalVertex(firstItem, firstEdge);
    AnchorVertex *v2 = addInternalVertex(secondItem, secondEdge);

    // Remove previous anchor
    if (graph[orientation].edgeData(v1, v2)) {
        removeAnchor_helper(v1, v2);
    }

    // If its an internal anchor, set the associated item
    if (firstItem == secondItem)
        data->item = firstItem;

    data->isVertical = orientation == Qt::Vertical;

    // Create a bi-directional edge in the sense it can be transversed both
    // from v1 or v2. "data" however is shared between the two references
    // so we still know that the anchor direction is from 1 to 2.
    data->from = v1;
    data->to = v2;
#ifdef QT_DEBUG
    data->name = QString::fromLatin1("%1 --to--> %2").arg(v1->toString(), v2->toString());
#endif
    // ### bit to track internal anchors, since inside AnchorData methods
    // we don't have access to the 'q' pointer.
    data->isLayoutAnchor = (data->item == q);

    graph[orientation].createEdge(v1, v2, data);
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1135, as _ZN28QGraphicsAnchorLayoutPrivate23restoreSimplifiedAnchorEPN22QtGraphicsAnchorLayout10AnchorDataE
inline void QGraphicsAnchorLayoutPrivate::restoreSimplifiedAnchor(AnchorData *edge)
{
    const Qt::Orientation orientation = edge->isVertical ? Qt::Vertical : Qt::Horizontal;
#if 0
    static const char *anchortypes[] = {"Normal",
                                        "Sequential",
                                        "Parallel"};
    qDebug("Restoring %s edge.", anchortypes[int(edge->type)]);
#endif

    Graph<AnchorVertex, AnchorData> &g = graph[orientation];

    if (edge->type == AnchorData::Normal) {
        g.createEdge(edge->from, edge->to, edge);

    } else if (edge->type == AnchorData::Sequential) {
        const auto *sequence = static_cast<SequentialAnchorData *>(edge);

        for (AnchorData *data : sequence->m_edges)
            restoreSimplifiedAnchor(data);

        delete sequence;

    } else if (edge->type == AnchorData::Parallel) {

        // Skip parallel anchors that were created by vertex simplification, they will be processed
        // later, when restoring vertex simplification.
        // ### we could improve this check bit having a bit inside 'edge'
        if (anchorsFromSimplifiedVertices[orientation].contains(edge))
            return;

        ParallelAnchorData* parallel = static_cast<ParallelAnchorData*>(edge);
        restoreSimplifiedConstraints(parallel);

        // ### Because of the way parallel anchors are created in the anchor simplification
        // algorithm, we know that one of these will be a sequence, so it'll be safe if the other
        // anchor create an edge between the same vertices as the parallel.
        Q_ASSERT(parallel->firstEdge->type == AnchorData::Sequential
                 || parallel->secondEdge->type == AnchorData::Sequential);
        restoreSimplifiedAnchor(parallel->firstEdge);
        restoreSimplifiedAnchor(parallel->secondEdge);

        delete parallel;
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2517, as _ZN28QGraphicsAnchorLayoutPrivate18identifyFloatItemsERK4QSetIPN22QtGraphicsAnchorLayout10AnchorDataEEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::identifyFloatItems(const QSet<AnchorData *> &visited, Qt::Orientation orientation)
{
    QSet<QGraphicsLayoutItem *> nonFloating;

    for (const AnchorData *ad : visited)
        identifyNonFloatItems_helper(ad, &nonFloating);

    QSet<QGraphicsLayoutItem *> floatItems;
    for (QGraphicsLayoutItem *item : std::as_const(items)) {
        if (!nonFloating.contains(item))
            floatItems.insert(item);
    }
    m_floatItems[orientation] = std::move(floatItems);
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 70, as _ZNK22QGraphicsLayoutPrivate15visualDirectionEv
inline Qt::LayoutDirection QGraphicsLayoutPrivate::visualDirection() const
{
    if (QGraphicsItem *maybeWidget = parentItem()) {
        if (maybeWidget->isWidget())
            return static_cast<QGraphicsWidget*>(maybeWidget)->layoutDirection();
    }
    return QGuiApplication::layoutDirection();
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2540, as _ZN28QGraphicsAnchorLayoutPrivate28identifyNonFloatItems_helperEPKN22QtGraphicsAnchorLayout10AnchorDataEP4QSetIP19QGraphicsLayoutItemE
inline void QGraphicsAnchorLayoutPrivate::identifyNonFloatItems_helper(const AnchorData *ad, QSet<QGraphicsLayoutItem *> *nonFloatingItemsIdentifiedSoFar)
{
    Q_Q(QGraphicsAnchorLayout);

    switch(ad->type) {
    case AnchorData::Normal:
        if (ad->item && ad->item != q)
            nonFloatingItemsIdentifiedSoFar->insert(ad->item);
        break;
    case AnchorData::Sequential:
        for (const AnchorData *d : static_cast<const SequentialAnchorData *>(ad)->m_edges)
            identifyNonFloatItems_helper(d, nonFloatingItemsIdentifiedSoFar);
        break;
    case AnchorData::Parallel:
        identifyNonFloatItems_helper(static_cast<const ParallelAnchorData *>(ad)->firstEdge, nonFloatingItemsIdentifiedSoFar);
        identifyNonFloatItems_helper(static_cast<const ParallelAnchorData *>(ad)->secondEdge, nonFloatingItemsIdentifiedSoFar);
        break;
    }
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 175, as _ZNK26QGraphicsLayoutItemPrivate10parentItemEv
inline QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem() const
{
    Q_Q(const QGraphicsLayoutItem);

    const QGraphicsLayoutItem *parent = q;
    while (parent && parent->isLayout()) {
        parent = parent->parentLayoutItem();
    }
    return parent ? parent->graphicsItem() : nullptr;
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 591, as _ZN28QGraphicsAnchorLayoutPrivate12oppositeEdgeEN2Qt11AnchorPointE
inline Qt::AnchorPoint QGraphicsAnchorLayoutPrivate::oppositeEdge(Qt::AnchorPoint edge)
{
    switch (edge) {
    case Qt::AnchorLeft:
        edge = Qt::AnchorRight;
        break;
    case Qt::AnchorRight:
        edge = Qt::AnchorLeft;
        break;
    case Qt::AnchorTop:
        edge = Qt::AnchorBottom;
        break;
    case Qt::AnchorBottom:
        edge = Qt::AnchorTop;
        break;
    default:
        break;
    }
    return edge;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1307, as _ZN28QGraphicsAnchorLayoutPrivate15edgeOrientationEN2Qt11AnchorPointE
inline Qt::Orientation
QGraphicsAnchorLayoutPrivate::edgeOrientation(Qt::AnchorPoint edge) noexcept
{
    return edge > Qt::AnchorRight ? Qt::Vertical : Qt::Horizontal;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1537, as _ZN28QGraphicsAnchorLayoutPrivate23removeCenterConstraintsEP19QGraphicsLayoutItemN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::removeCenterConstraints(QGraphicsLayoutItem *item,
                                                           Qt::Orientation orientation)
{
    // Remove the item center constraints associated to this item
    // ### This is a temporary solution. We should probably use a better
    // data structure to hold items and/or their associated constraints
    // so that we can remove those easily

    AnchorVertex *first = internalVertex(item, orientation == Qt::Horizontal ?
                                       Qt::AnchorLeft :
                                       Qt::AnchorTop);
    AnchorVertex *center = internalVertex(item, orientation == Qt::Horizontal ?
                                        Qt::AnchorHorizontalCenter :
                                        Qt::AnchorVerticalCenter);

    // Skip if no center constraints exist
    if (!center)
        return;

    Q_ASSERT(first);
    AnchorData *internalAnchor = graph[orientation].edgeData(first, center);

    // Look for our anchor in all item center constraints, then remove it
    for (int i = 0; i < itemCenterConstraints[orientation].size(); ++i) {
        if (itemCenterConstraints[orientation].at(i)->variables.contains(internalAnchor)) {
            delete itemCenterConstraints[orientation].takeAt(i);
            break;
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1714, as _ZN28QGraphicsAnchorLayoutPrivate9getAnchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_
inline QGraphicsAnchor *QGraphicsAnchorLayoutPrivate::getAnchor(QGraphicsLayoutItem *firstItem,
                                                         Qt::AnchorPoint firstEdge,
                                                         QGraphicsLayoutItem *secondItem,
                                                         Qt::AnchorPoint secondEdge)
{
    // Do not expose internal anchors
    if (firstItem == secondItem)
        return nullptr;

    const Qt::Orientation orientation = edgeOrientation(firstEdge);
    AnchorVertex *v1 = internalVertex(firstItem, firstEdge);
    AnchorVertex *v2 = internalVertex(secondItem, secondEdge);

    QGraphicsAnchor *graphicsAnchor = nullptr;

    AnchorData *data = graph[orientation].edgeData(v1, v2);
    if (data) {
        // We could use "acquireGraphicsAnchor" here, but to avoid a regression where
        // an internal anchor was wrongly exposed, I want to ensure no new
        // QGraphicsAnchor instances are created by this call.
        // This assumption must hold because anchors are either user-created (and already
        // have their public object created), or they are internal (and must not reach
        // this point).
        Q_ASSERT(data->graphicsAnchor);
        graphicsAnchor = data->graphicsAnchor;
    }
    return graphicsAnchor;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2257, as _ZN28QGraphicsAnchorLayoutPrivate9findPathsEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::findPaths(Qt::Orientation orientation)
{
    QQueue<std::pair<AnchorVertex *, AnchorVertex *> > queue;

    QSet<AnchorData *> visited;

    AnchorVertex *root = layoutFirstVertex[orientation];

    graphPaths[orientation].insert(root, GraphPath());

    const auto adjacentVertices = graph[orientation].adjacentVertices(root);
    for (AnchorVertex *v : adjacentVertices)
        queue.enqueue(std::pair(root, v));

    while(!queue.isEmpty()) {
        std::pair<AnchorVertex *, AnchorVertex *>  pair = queue.dequeue();
        AnchorData *edge = graph[orientation].edgeData(pair.first, pair.second);

        if (visited.contains(edge))
            continue;

        visited.insert(edge);
        GraphPath current = graphPaths[orientation].value(pair.first);

        if (edge->from == pair.first)
            current.positives.insert(edge);
        else
            current.negatives.insert(edge);

        graphPaths[orientation].insert(pair.second, current);

        const auto adjacentVertices = graph[orientation].adjacentVertices(pair.second);
        for (AnchorVertex *v : adjacentVertices)
            queue.enqueue(std::pair(pair.second, v));
    }

    // We will walk through every reachable items (non-float) store them in a temporary set.
    // We them create a set of all items and subtract the non-floating items from the set in
    // order to get the floating items. The floating items is then stored in m_floatItems
    identifyFloatItems(visited, orientation);
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2328, as _ZN28QGraphicsAnchorLayoutPrivate17updateAnchorSizesEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::updateAnchorSizes(Qt::Orientation orientation)
{
    Graph<AnchorVertex, AnchorData> &g = graph[orientation];
    const QList<std::pair<AnchorVertex *, AnchorVertex *>> &vertices = g.connections();

    for (int i = 0; i < vertices.size(); ++i) {
        AnchorData *ad = g.edgeData(vertices.at(i).first, vertices.at(i).second);
        ad->updateChildrenSizes();
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2439, as _ZN28QGraphicsAnchorLayoutPrivate13getGraphPartsEN2Qt11OrientationE
inline QGraphicsAnchorLayoutPrivate::GraphParts
QGraphicsAnchorLayoutPrivate::getGraphParts(Qt::Orientation orientation)
{
    GraphParts result;

    Q_ASSERT(layoutFirstVertex[orientation] && layoutLastVertex[orientation]);

    AnchorData *edgeL1 = nullptr;
    AnchorData *edgeL2 = nullptr;

    // The layout may have a single anchor between Left and Right or two half anchors
    // passing through the center
    if (layoutCentralVertex[orientation]) {
        edgeL1 = graph[orientation].edgeData(layoutFirstVertex[orientation], layoutCentralVertex[orientation]);
        edgeL2 = graph[orientation].edgeData(layoutCentralVertex[orientation], layoutLastVertex[orientation]);
    } else {
        edgeL1 = graph[orientation].edgeData(layoutFirstVertex[orientation], layoutLastVertex[orientation]);
    }

    result.nonTrunkConstraints = constraints[orientation] + itemCenterConstraints[orientation];

    QSet<QSimplexVariable *> trunkVariables;

    trunkVariables += edgeL1;
    if (edgeL2)
        trunkVariables += edgeL2;

    bool dirty;
    auto end = result.nonTrunkConstraints.end();
    do {
        dirty = false;

        auto isMatch = [&result, &trunkVariables](QSimplexConstraint *c) -> bool {
            bool match = false;

            // Check if this constraint have some overlap with current
            // trunk variables...
            for (QSimplexVariable *ad : std::as_const(trunkVariables)) {
                if (c->variables.contains(ad)) {
                    match = true;
                    break;
                }
            }

            // If so, we add it to trunk, and erase it from the
            // remaining constraints.
            if (match) {
                result.trunkConstraints += c;
                for (auto jt = c->variables.cbegin(), end = c->variables.cend(); jt != end; ++jt)
                    trunkVariables.insert(jt.key());
                return true;
            } else {
                // Note that we don't erase the constraint if it's not
                // a match, since in a next iteration of a do-while we
                // can pass on it again and it will be a match.
                //
                // For example: if trunk share a variable with
                // remainingConstraints[1] and it shares with
                // remainingConstraints[0], we need a second iteration
                // of the do-while loop to match both.
                return false;
            }
        };
        const auto newEnd = std::remove_if(result.nonTrunkConstraints.begin(), end, isMatch);
        dirty = newEnd != end;
        end = newEnd;
    } while (dirty);

    result.nonTrunkConstraints.erase(end, result.nonTrunkConstraints.end());

    return result;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2566, as _ZN28QGraphicsAnchorLayoutPrivate18setItemsGeometriesERK6QRectF
inline void QGraphicsAnchorLayoutPrivate::setItemsGeometries(const QRectF &geom)
{
    Q_Q(QGraphicsAnchorLayout);
    AnchorVertex *firstH, *secondH, *firstV, *secondV;

    qreal top;
    qreal left;
    qreal right;

    q->getContentsMargins(&left, &top, &right, nullptr);
    const Qt::LayoutDirection visualDir = visualDirection();
    if (visualDir == Qt::RightToLeft)
        qSwap(left, right);

    left += geom.left();
    top += geom.top();
    right = geom.right() - right;

    for (QGraphicsLayoutItem *item : std::as_const(items)) {
        QRectF newGeom;
        QSizeF itemPreferredSize = item->effectiveSizeHint(Qt::PreferredSize);
        if (m_floatItems[Qt::Horizontal].contains(item)) {
            newGeom.setLeft(0);
            newGeom.setRight(itemPreferredSize.width());
        } else {
            firstH = internalVertex(item, Qt::AnchorLeft);
            secondH = internalVertex(item, Qt::AnchorRight);

            if (visualDir == Qt::LeftToRight) {
                newGeom.setLeft(left + firstH->distance);
                newGeom.setRight(left + secondH->distance);
            } else {
                newGeom.setLeft(right - secondH->distance);
                newGeom.setRight(right - firstH->distance);
            }
        }

        if (m_floatItems[Qt::Vertical].contains(item)) {
            newGeom.setTop(0);
            newGeom.setBottom(itemPreferredSize.height());
        } else {
            firstV = internalVertex(item, Qt::AnchorTop);
            secondV = internalVertex(item, Qt::AnchorBottom);

            newGeom.setTop(top + firstV->distance);
            newGeom.setBottom(top + secondV->distance);
        }

        item->setGeometry(newGeom);
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2911, as _ZN28QGraphicsAnchorLayoutPrivate9dumpGraphERK7QString
#if defined(QT_DEBUG)
inline void QGraphicsAnchorLayoutPrivate::dumpGraph(const QString &name)
{
    QFile file(QString::fromLatin1("anchorlayout.%1.dot").arg(name));
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text | QIODevice::Truncate))
        qWarning("Could not write to %ls", qUtf16Printable(file.fileName()));

    QString str = QString::fromLatin1("digraph anchorlayout {\nnode [shape=\"rect\"]\n%1}");
    QString dotContents = graph[Qt::Horizontal].serializeToDot();
    dotContents += graph[Qt::Vertical].serializeToDot();
    file.write(str.arg(dotContents).toLocal8Bit());

    file.close();
}
#endif  // defined(QT_DEBUG)
//  -----------------------------------------------------------------------

//  QGraphicsAnchorLayout *QGraphicsAnchorLayoutPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayout *ritual_ZN28QGraphicsAnchorLayoutPrivate6q_funcEv(
    QGraphicsAnchorLayoutPrivate *self) {
  return self->q_func();
}

//  const QGraphicsAnchorLayout *QGraphicsAnchorLayoutPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsAnchorLayout *ritual_ZNK28QGraphicsAnchorLayoutPrivate6q_funcEv(
    const QGraphicsAnchorLayoutPrivate *self) {
  return self->q_func();
}

//  QGraphicsAnchorLayoutPrivate
//      *QGraphicsAnchorLayoutPrivate::get(QGraphicsAnchorLayout *q)
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayoutPrivate *ritual_ZN28QGraphicsAnchorLayoutPrivate3getEP21QGraphicsAnchorLayout(
    QGraphicsAnchorLayout *q) {
  return QGraphicsAnchorLayoutPrivate::get(q);
}

//  Qt::AnchorPoint
//      QGraphicsAnchorLayoutPrivate::oppositeEdge(Qt::AnchorPoint edge)
extern "C" Q_DECL_EXPORT
Qt::AnchorPoint ritual_ZN28QGraphicsAnchorLayoutPrivate12oppositeEdgeEN2Qt11AnchorPointE(
    Qt::AnchorPoint edge) {
  return QGraphicsAnchorLayoutPrivate::oppositeEdge(edge);
}

//  Qt::Orientation
//      QGraphicsAnchorLayoutPrivate::edgeOrientation(Qt::AnchorPoint edge)
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZN28QGraphicsAnchorLayoutPrivate15edgeOrientationEN2Qt11AnchorPointE(
    Qt::AnchorPoint edge) {
  return QGraphicsAnchorLayoutPrivate::edgeOrientation(edge);
}

//  Qt::AnchorPoint QGraphicsAnchorLayoutPrivate::pickEdge(Qt::AnchorPoint
//      edge, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
Qt::AnchorPoint ritual_ZN28QGraphicsAnchorLayoutPrivate8pickEdgeEN2Qt11AnchorPointENS0_11OrientationE(
    Qt::AnchorPoint edge,
    Qt::Orientation orientation) {
  return QGraphicsAnchorLayoutPrivate::pickEdge(edge, orientation);
}

//  void
//      QGraphicsAnchorLayoutPrivate::removeCenterConstraints(QGraphicsLayout
//      Item *item, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate23removeCenterConstraintsEP19QGraphicsLayoutItemN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    QGraphicsLayoutItem *item,
    Qt::Orientation orientation) {
  self->removeCenterConstraints(item, orientation);
}

//  QGraphicsAnchor
//      *QGraphicsAnchorLayoutPrivate::getAnchor(QGraphicsLayoutItem
//      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
//      *secondItem, Qt::AnchorPoint secondEdge)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN28QGraphicsAnchorLayoutPrivate9getAnchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_(
    QGraphicsAnchorLayoutPrivate *self,
    QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge,
    QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge) {
  return self->getAnchor(firstItem, firstEdge, secondItem, secondEdge);
}

//  void QGraphicsAnchorLayoutPrivate::findPaths(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate9findPathsEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  self->findPaths(orientation);
}

//  void QGraphicsAnchorLayoutPrivate::updateAnchorSizes(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate17updateAnchorSizesEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  self->updateAnchorSizes(orientation);
}

//  GraphParts QGraphicsAnchorLayoutPrivate::getGraphParts(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayoutPrivate::GraphParts *ritual_ZN28QGraphicsAnchorLayoutPrivate13getGraphPartsEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  return new QGraphicsAnchorLayoutPrivate::GraphParts(
      self->getGraphParts(
          orientation));
}

//  void QGraphicsAnchorLayoutPrivate::setItemsGeometries(const QRectF &geom)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate18setItemsGeometriesERK6QRectF(
    QGraphicsAnchorLayoutPrivate *self,
    const QRectF *geom) {
  self->setItemsGeometries(*geom);
}

#if defined(QT_DEBUG)
//  void QGraphicsAnchorLayoutPrivate::dumpGraph(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate9dumpGraphERK7QString(
    QGraphicsAnchorLayoutPrivate *self,
    const QString *name) {
  self->dumpGraph(*name);
}
#endif  // defined(QT_DEBUG)

//  QGraphicsAnchorLayoutPrivate::~QGraphicsAnchorLayoutPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivateD1Ev(
    QGraphicsAnchorLayoutPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
