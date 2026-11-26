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
#include <QtCore/qglobal.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qapplication.h>
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

using namespace Qt::StringLiterals;

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 27, as local:qgraphicsanchorlayout_p.cpp:g_offset
const qreal g_offset = (sizeof(qreal) == sizeof(double)) ? QWIDGETSIZE_MAX : QWIDGETSIZE_MAX / 32;

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 382, as local:qgraphicsanchorlayout_p.cpp:getFactor
static std::pair<QGraphicsAnchorLayoutPrivate::Interval, qreal> getFactor(qreal value, qreal min,
                                                                          qreal minPref, qreal pref,
                                                                          qreal maxPref, qreal max)
{
    QGraphicsAnchorLayoutPrivate::Interval interval;
    qreal lower;
    qreal upper;

    if (value < minPref) {
        interval = QGraphicsAnchorLayoutPrivate::MinimumToMinPreferred;
        lower = min;
        upper = minPref;
    } else if (value < pref) {
        interval = QGraphicsAnchorLayoutPrivate::MinPreferredToPreferred;
        lower = minPref;
        upper = pref;
    } else if (value < maxPref) {
        interval = QGraphicsAnchorLayoutPrivate::PreferredToMaxPreferred;
        lower = pref;
        upper = maxPref;
    } else {
        interval = QGraphicsAnchorLayoutPrivate::MaxPreferredToMaximum;
        lower = maxPref;
        upper = max;
    }

    qreal progress;
    if (upper == lower) {
        progress = 0;
    } else {
        progress = (value - lower) / (upper - lower);
    }

    return std::pair(interval, progress);
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 418, as local:qgraphicsanchorlayout_p.cpp:interpolate
static qreal interpolate(const std::pair<QGraphicsAnchorLayoutPrivate::Interval, qreal> &factor,
                         qreal min, qreal minPref, qreal pref, qreal maxPref, qreal max)
{
    qreal lower = 0;
    qreal upper = 0;

    switch (factor.first) {
    case QGraphicsAnchorLayoutPrivate::MinimumToMinPreferred:
        lower = min;
        upper = minPref;
        break;
    case QGraphicsAnchorLayoutPrivate::MinPreferredToPreferred:
        lower = minPref;
        upper = pref;
        break;
    case QGraphicsAnchorLayoutPrivate::PreferredToMaxPreferred:
        lower = pref;
        upper = maxPref;
        break;
    case QGraphicsAnchorLayoutPrivate::MaxPreferredToMaximum:
        lower = maxPref;
        upper = max;
        break;
    }

    return lower + factor.second * (upper - lower);
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 696, as local:qgraphicsanchorlayout_p.cpp:createSequence
static AnchorData *createSequence(Graph<AnchorVertex, AnchorData> *graph, AnchorVertex *before,
                                  const QList<AnchorVertex *> &vertices, AnchorVertex *after)
{
#if defined(QT_DEBUG) && 0
    QString strVertices;
    for (int i = 0; i < vertices.count(); ++i) {
        strVertices += QString::fromLatin1("%1 - ").arg(vertices.at(i)->toString());
    }
    QString strPath = QString::fromLatin1("%1 - %2%3").arg(before->toString(), strVertices, after->toString());
    qDebug("simplifying [%s] to [%s - %s]", qPrintable(strPath), qPrintable(before->toString()), qPrintable(after->toString()));
#endif

    AnchorVertex *prev = before;
    QList<AnchorData *> edges;
    edges.reserve(vertices.size() + 1);

    const int numVertices = vertices.size();
    edges.reserve(numVertices + 1);
    // Take from the graph, the edges that will be simplificated
    for (int i = 0; i < numVertices; ++i) {
        AnchorVertex *next = vertices.at(i);
        AnchorData *ad = graph->takeEdge(prev, next);
        Q_ASSERT(ad);
        edges.append(ad);
        prev = next;
    }

    // Take the last edge (not covered in the loop above)
    AnchorData *ad = graph->takeEdge(vertices.last(), after);
    Q_ASSERT(ad);
    edges.append(ad);

    // Create sequence
    SequentialAnchorData *sequence = new SequentialAnchorData(vertices, edges);
    sequence->from = before;
    sequence->to = after;

    sequence->calculateSizeHints();

    return sequence;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 819, as local:qgraphicsanchorlayout_p.cpp:replaceVertex_helper
static AnchorVertex *replaceVertex_helper(AnchorData *data, AnchorVertex *oldV, AnchorVertex *newV)
{
    AnchorVertex *other;
    if (data->from == oldV) {
        data->from = newV;
        other = data->to;
    } else {
        data->to = newV;
        other = data->from;
    }
    return other;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2009, as local:qgraphicsanchorlayout_p.cpp:getVariables
inline QList<AnchorData *> getVariables(const QList<QSimplexConstraint *> &constraints)
{
    QSet<AnchorData *> variableSet;
    for (int i = 0; i < constraints.size(); ++i) {
        const QSimplexConstraint *c = constraints.at(i);
        for (auto it = c->variables.cbegin(), end = c->variables.cend(); it != end; ++it)
            variableSet.insert(static_cast<AnchorData *>(it.key()));
    }
    return variableSet.values();
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2125, as local:qgraphicsanchorlayout_p.cpp:shiftConstraints
static void shiftConstraints(const QList<QSimplexConstraint *> &constraints, qreal amount)
{
    for (int i = 0; i < constraints.size(); ++i) {
        QSimplexConstraint *c = constraints.at(i);
        const qreal multiplier = std::accumulate(c->variables.cbegin(), c->variables.cend(), qreal(0));
        c->constant += multiplier * amount;
    }
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 79, as local:qgraphicslayout_p.cpp:removeLayoutItemFromLayout
static bool removeLayoutItemFromLayout(QGraphicsLayout *lay, QGraphicsLayoutItem *layoutItem)
{
    if (!lay)
        return false;

    for (int i = lay->count() - 1; i >= 0; --i) {
        QGraphicsLayoutItem *child = lay->itemAt(i);
        if (child && child->isLayout()) {
            if (removeLayoutItemFromLayout(static_cast<QGraphicsLayout*>(child), layoutItem))
                return true;
        } else if (child == layoutItem) {
            lay->removeAt(i);
            return true;
        }
    }
    return false;
}

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

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 108, as _ZN22QGraphicsLayoutPrivate18addChildLayoutItemEP19QGraphicsLayoutItem
inline void QGraphicsLayoutPrivate::addChildLayoutItem(QGraphicsLayoutItem *layoutItem)
{
    Q_Q(QGraphicsLayout);
    if (QGraphicsLayoutItem *maybeLayout = layoutItem->parentLayoutItem()) {
        if (maybeLayout->isLayout())
            removeLayoutItemFromLayout(static_cast<QGraphicsLayout*>(maybeLayout), layoutItem);
    }
    layoutItem->setParentLayoutItem(q);
    if (layoutItem->isLayout()) {
        if (QGraphicsItem *parItem = parentItem()) {
            static_cast<QGraphicsLayout*>(layoutItem)->d_func()->reparentChildItems(parItem);
        }
    } else {
        if (QGraphicsItem *item = layoutItem->graphicsItem()) {
            QGraphicsItem *newParent = parentItem();
            QGraphicsItem *oldParent = item->parentItem();
            if (oldParent == newParent || !newParent)
                return;

#ifdef QT_DEBUG
            if (oldParent && item->isWidget()) {
                QGraphicsWidget *w = static_cast<QGraphicsWidget*>(item);
                qWarning("QGraphicsLayout::addChildLayoutItem: %s \"%s\" in wrong parent; moved to correct parent",
                    w->metaObject()->className(), w->objectName().toLocal8Bit().constData());
            }
#endif

            item->setParentItem(newParent);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2043, as _ZN28QGraphicsAnchorLayoutPrivate15calculateGraphsEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::calculateGraphs(Qt::Orientation orientation)
{
#if defined(QT_DEBUG) || defined(QT_BUILD_INTERNAL)
    lastCalculationUsedSimplex[orientation] = false;
#endif

    static bool simplificationEnabled = qEnvironmentVariableIsEmpty("QT_ANCHORLAYOUT_NO_SIMPLIFICATION");

    // Reset the nominal sizes of each anchor based on the current item sizes
    refreshAllSizeHints(orientation);

    // Simplify the graph
    if (simplificationEnabled && !simplifyGraph(orientation)) {
        qWarning("QGraphicsAnchorLayout: anchor setup is not feasible.");
        graphHasConflicts[orientation] = true;
        return;
    }

    // Traverse all graph edges and store the possible paths to each vertex
    findPaths(orientation);

    // From the paths calculated above, extract the constraints that the current
    // anchor setup impose, to our Linear Programming problem.
    constraintsFromPaths(orientation);

    // Split the constraints and anchors into groups that should be fed to the
    // simplex solver independently. Currently we find two groups:
    //
    //  1) The "trunk", that is, the set of anchors (items) that are connected
    //     to the two opposite sides of our layout, and thus need to stretch in
    //     order to fit in the current layout size.
    //
    //  2) The floating or semi-floating anchors (items) that are those which
    //     are connected to only one (or none) of the layout sides, thus are not
    //     influenced by the layout size.
    const auto parts = getGraphParts(orientation);

    // Now run the simplex solver to calculate Minimum, Preferred and Maximum sizes
    // of the "trunk" set of constraints and variables.
    // ### does trunk always exist? empty = trunk is the layout left->center->right
    const QList<AnchorData *> trunkVariables = getVariables(parts.trunkConstraints);

    // For minimum and maximum, use the path between the two layout sides as the
    // objective function.
    AnchorVertex *v = layoutLastVertex[orientation];
    GraphPath trunkPath = graphPaths[orientation].value(v);

    bool feasible = calculateTrunk(orientation, trunkPath, parts.trunkConstraints, trunkVariables);

    // For the other parts that not the trunk, solve only for the preferred size
    // that is the size they will remain at, since they are not stretched by the
    // layout.

    if (feasible && !parts.nonTrunkConstraints.isEmpty()) {
        const QList<AnchorData *> partVariables = getVariables(parts.nonTrunkConstraints);
        Q_ASSERT(!partVariables.isEmpty());
        feasible = calculateNonTrunk(parts.nonTrunkConstraints, partVariables);
    }

    // Propagate the new sizes down the simplified graph, ie. tell the
    // group anchors to set their children anchors sizes.
    updateAnchorSizes(orientation);

    graphHasConflicts[orientation] = !feasible;

    // Clean up our data structures. They are not needed anymore since
    // distribution uses just interpolation.
    qDeleteAll(constraints[orientation]);
    constraints[orientation].clear();
    graphPaths[orientation].clear(); // ###

    if (simplificationEnabled)
        restoreSimplifiedGraph(orientation);
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1236, as _ZN28QGraphicsAnchorLayoutPrivate15restoreVerticesEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::restoreVertices(Qt::Orientation orientation)
{
    Q_Q(QGraphicsAnchorLayout);

    Graph<AnchorVertex, AnchorData> &g = graph[orientation];
    QList<AnchorVertexPair *> &toRestore = simplifiedVertices[orientation];

    // Since we keep a list of parallel anchors and vertices that were created during vertex
    // simplification, we can now iterate on those lists instead of traversing the graph
    // recursively.

    // First, restore the constraints changed when we created parallel anchors. Note that this
    // works at this point because the constraints doesn't depend on vertex information and at
    // this point it's always safe to identify whether the second child is forward or backwards.
    // In the next step, we'll change the anchors vertices so that would not be possible anymore.
    QList<AnchorData *> &parallelAnchors = anchorsFromSimplifiedVertices[orientation];

    for (int i = parallelAnchors.size() - 1; i >= 0; --i) {
        ParallelAnchorData *parallel = static_cast<ParallelAnchorData *>(parallelAnchors.at(i));
        restoreSimplifiedConstraints(parallel);
    }

    // Then, we will restore the vertices in the inverse order of creation, this way we ensure that
    // the vertex being restored was not wrapped by another simplification.
    for (int i = toRestore.size() - 1; i >= 0; --i) {
        AnchorVertexPair *pair = toRestore.at(i);
        QList<AnchorVertex *> adjacents = g.adjacentVertices(pair);

        // Restore the removed edge, this will also restore both vertices 'first' and 'second' to
        // the graph structure.
        AnchorVertex *first = pair->m_first;
        AnchorVertex *second = pair->m_second;
        g.createEdge(first, second, pair->m_removedAnchor);

        // Restore the anchors for the first child vertex
        for (int j = 0; j < pair->m_firstAnchors.size(); ++j) {
            AnchorData *ad = pair->m_firstAnchors.at(j);
            Q_ASSERT(ad->from == pair || ad->to == pair);

            replaceVertex_helper(ad, pair, first);
            g.createEdge(ad->from, ad->to, ad);
        }

        // Restore the anchors for the second child vertex
        for (int j = 0; j < pair->m_secondAnchors.size(); ++j) {
            AnchorData *ad = pair->m_secondAnchors.at(j);
            Q_ASSERT(ad->from == pair || ad->to == pair);

            replaceVertex_helper(ad, pair, second);
            g.createEdge(ad->from, ad->to, ad);
        }

        for (int j = 0; j < adjacents.size(); ++j) {
            g.takeEdge(pair, adjacents.at(j));
        }

        // The pair simplified a layout vertex, so place back the correct vertex in the variable
        // that track layout vertices
        if (pair->m_item == q) {
            AnchorVertex *layoutVertex = first->m_item == q ? first : second;
            Q_ASSERT(layoutVertex->m_item == q);
            changeLayoutVertex(orientation, pair, layoutVertex);
        }

        delete pair;
    }
    qDeleteAll(parallelAnchors);
    parallelAnchors.clear();
    toRestore.clear();
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 775, as _ZN28QGraphicsAnchorLayoutPrivate13simplifyGraphEN2Qt11OrientationE
inline bool QGraphicsAnchorLayoutPrivate::simplifyGraph(Qt::Orientation orientation)
{
    if (items.isEmpty())
        return true;

#if defined(QT_DEBUG) && 0
    qDebug("Simplifying Graph for %s",
           orientation == Horizontal ? "Horizontal" : "Vertical");

    static int count = 0;
    if (orientation == Horizontal) {
        count++;
        dumpGraph(QString::fromLatin1("%1-full").arg(count));
    }
#endif

    // Vertex simplification
    if (!simplifyVertices(orientation)) {
        restoreVertices(orientation);
        return false;
    }

    // Anchor simplification
    bool dirty;
    bool feasible = true;
    do {
        dirty = simplifyGraphIteration(orientation, &feasible);
    } while (dirty && feasible);

    // Note that if we are not feasible, we fallback and make sure that the graph is fully restored
    if (!feasible) {
        restoreSimplifiedGraph(orientation);
        restoreVertices(orientation);
        return false;
    }

#if defined(QT_DEBUG) && 0
    dumpGraph(QString::fromLatin1("%1-simplified-%2").arg(count).arg(
                  QString::fromLatin1(orientation == Horizontal ? "Horizontal" : "Vertical")));
#endif

    return true;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2235, as _ZN28QGraphicsAnchorLayoutPrivate19refreshAllSizeHintsEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::refreshAllSizeHints(Qt::Orientation orientation)
{
    Graph<AnchorVertex, AnchorData> &g = graph[orientation];
    QList<std::pair<AnchorVertex *, AnchorVertex *>> vertices = g.connections();

    QLayoutStyleInfo styleInf = styleInfo();
    for (int i = 0; i < vertices.size(); ++i) {
        AnchorData *data = g.edgeData(vertices.at(i).first, vertices.at(i).second);
        data->refreshSizeHints(&styleInf);
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2309, as _ZN28QGraphicsAnchorLayoutPrivate20constraintsFromPathsEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::constraintsFromPaths(Qt::Orientation orientation)
{
    const auto vertices = graphPaths[orientation].uniqueKeys();
    for (AnchorVertex *vertex : vertices) {
        int valueCount = graphPaths[orientation].count(vertex);
        if (valueCount == 1)
            continue;

        QList<GraphPath> pathsToVertex = graphPaths[orientation].values(vertex);
        for (int i = 1; i < valueCount; ++i) {
            constraints[orientation] += \
                pathsToVertex[0].constraint(pathsToVertex.at(i));
        }
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 586, as _ZN28QGraphicsAnchorLayoutPrivateC1Ev
inline QGraphicsAnchorLayoutPrivate::QGraphicsAnchorLayoutPrivate()
    : calculateGraphCacheDirty(true), styleInfoDirty(true)
{
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1963, as _ZNK28QGraphicsAnchorLayoutPrivate9styleInfoEv
inline QLayoutStyleInfo &QGraphicsAnchorLayoutPrivate::styleInfo() const
{
    if (styleInfoDirty) {
        Q_Q(const QGraphicsAnchorLayout);
        //### Fix this if QGV ever gets support for Metal style or different Aqua sizes.
        QWidget *wid = nullptr;

        QGraphicsLayoutItem *parent = q->parentLayoutItem();
        while (parent && parent->isLayout()) {
            parent = parent->parentLayoutItem();
        }
        QGraphicsWidget *w = nullptr;
        if (parent) {
            QGraphicsItem *parentItem = parent->graphicsItem();
            if (parentItem && parentItem->isWidget())
                w = static_cast<QGraphicsWidget*>(parentItem);
        }

        QStyle *style = w ? w->style() : QApplication::style();
        cachedStyleInfo = QLayoutStyleInfo(style, wid);
        cachedStyleInfo.setDefaultSpacing(Qt::Horizontal, spacings[Qt::Horizontal]);
        cachedStyleInfo.setDefaultSpacing(Qt::Vertical, spacings[Qt::Vertical]);

        styleInfoDirty = false;
    }
    return cachedStyleInfo;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1207, as _ZN28QGraphicsAnchorLayoutPrivate22restoreSimplifiedGraphEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::restoreSimplifiedGraph(Qt::Orientation orientation)
{
#if 0
    qDebug("Restoring Simplified Graph for %s",
           orientation == Horizontal ? "Horizontal" : "Vertical");
#endif

    // Restore anchor simplification
    Graph<AnchorVertex, AnchorData> &g = graph[orientation];
    QList<std::pair<AnchorVertex *, AnchorVertex *>> connections = g.connections();
    for (int i = 0; i < connections.size(); ++i) {
        AnchorVertex *v1 = connections.at(i).first;
        AnchorVertex *v2 = connections.at(i).second;
        AnchorData *edge = g.edgeData(v1, v2);

        // We restore only sequential anchors and parallels that were not created by
        // vertex simplification.
        if (edge->type == AnchorData::Sequential
            || (edge->type == AnchorData::Parallel &&
                !anchorsFromSimplifiedVertices[orientation].contains(edge))) {

            g.takeEdge(v1, v2);
            restoreSimplifiedAnchor(edge);
        }
    }

    restoreVertices(orientation);
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1181, as _ZN28QGraphicsAnchorLayoutPrivate28restoreSimplifiedConstraintsEPN22QtGraphicsAnchorLayout18ParallelAnchorDataE
inline void QGraphicsAnchorLayoutPrivate::restoreSimplifiedConstraints(ParallelAnchorData *parallel)
{
    if (!parallel->isCenterAnchor)
        return;

    for (int i = 0; i < parallel->m_firstConstraints.size(); ++i) {
        QSimplexConstraint *c = parallel->m_firstConstraints.at(i);
        qreal v = c->variables[parallel];
        c->variables.remove(parallel);
        c->variables.insert(parallel->firstEdge, v);
    }

    // When restoring, we might have to revert constraints back. See comments on
    // addAnchorMaybeParallel().
    const bool needsReverse = !parallel->secondForward();

    for (int i = 0; i < parallel->m_secondConstraints.size(); ++i) {
        QSimplexConstraint *c = parallel->m_secondConstraints.at(i);
        qreal v = c->variables[parallel];
        if (needsReverse)
            v *= -1;
        c->variables.remove(parallel);
        c->variables.insert(parallel->secondEdge, v);
    }
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 1836, as _ZN28QGraphicsAnchorLayoutPrivate17addInternalVertexEP19QGraphicsLayoutItemN2Qt11AnchorPointE
inline AnchorVertex *QGraphicsAnchorLayoutPrivate::addInternalVertex(QGraphicsLayoutItem *item,
                                                              Qt::AnchorPoint edge)
{
    std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> pair(item, edge);
    std::pair<AnchorVertex *, int> v = m_vertexList.value(pair);

    if (!v.first) {
        Q_ASSERT(v.second == 0);
        v.first = new AnchorVertex(item, edge);
    }
    v.second++;
    m_vertexList.insert(pair, v);
    return v.first;
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

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2624, as _ZN28QGraphicsAnchorLayoutPrivate24calculateVertexPositionsEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::calculateVertexPositions(Qt::Orientation orientation)
{
    QQueue<std::pair<AnchorVertex *, AnchorVertex *> > queue;
    QSet<AnchorVertex *> visited;

    // Get root vertex
    AnchorVertex *root = layoutFirstVertex[orientation];

    root->distance = 0;
    visited.insert(root);

    // Add initial edges to the queue
    const auto adjacentVertices = graph[orientation].adjacentVertices(root);
    for (AnchorVertex *v : adjacentVertices)
        queue.enqueue(std::pair(root, v));

    // Do initial calculation required by "interpolateEdge()"
    setupEdgesInterpolation(orientation);

    // Traverse the graph and calculate vertex positions
    while (!queue.isEmpty()) {
        std::pair<AnchorVertex *, AnchorVertex *> pair = queue.dequeue();
        AnchorData *edge = graph[orientation].edgeData(pair.first, pair.second);

        if (visited.contains(pair.second))
            continue;

        visited.insert(pair.second);
        interpolateEdge(pair.first, edge);

        QList<AnchorVertex *> adjacents = graph[orientation].adjacentVertices(pair.second);
        for (int i = 0; i < adjacents.size(); ++i) {
            if (!visited.contains(adjacents.at(i)))
                queue.enqueue(std::pair(pair.second, adjacents.at(i)));
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2669, as _ZN28QGraphicsAnchorLayoutPrivate23setupEdgesInterpolationEN2Qt11OrientationE
inline void QGraphicsAnchorLayoutPrivate::setupEdgesInterpolation(
    Qt::Orientation orientation)
{
    Q_Q(QGraphicsAnchorLayout);

    qreal current;
    current = (orientation == Qt::Horizontal) ? q->contentsRect().width() : q->contentsRect().height();

    std::pair<Interval, qreal> result;
    result = getFactor(current,
                       sizeHints[orientation][Qt::MinimumSize],
                       sizeHints[orientation][Qt::PreferredSize],
                       sizeHints[orientation][Qt::PreferredSize],
                       sizeHints[orientation][Qt::PreferredSize],
                       sizeHints[orientation][Qt::MaximumSize]);

    interpolationInterval[orientation] = result.first;
    interpolationProgress[orientation] = result.second;
}

//  from src/widgets/graphicsview/qgraphicsanchorlayout_p.cpp, line 2704, as _ZN28QGraphicsAnchorLayoutPrivate15interpolateEdgeEPN22QtGraphicsAnchorLayout12AnchorVertexEPNS0_10AnchorDataE
inline void QGraphicsAnchorLayoutPrivate::interpolateEdge(AnchorVertex *base, AnchorData *edge)
{
    const Qt::Orientation orientation = edge->isVertical ? Qt::Vertical : Qt::Horizontal;
    const std::pair<Interval, qreal> factor(interpolationInterval[orientation],
                                            interpolationProgress[orientation]);

    qreal edgeDistance = interpolate(factor, edge->sizeAtMinimum, edge->sizeAtPreferred,
                                     edge->sizeAtPreferred, edge->sizeAtPreferred,
                                     edge->sizeAtMaximum);

    Q_ASSERT(edge->from == base || edge->to == base);

    // Calculate the distance for the vertex opposite to the base
    if (edge->from == base) {
        edge->to->distance = base->distance + edgeDistance;
    } else {
        edge->from->distance = base->distance - edgeDistance;
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

//  QGraphicsAnchorLayoutPrivate::QGraphicsAnchorLayoutPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayoutPrivate *ritual_ZN28QGraphicsAnchorLayoutPrivateC1Ev() {
  return new QGraphicsAnchorLayoutPrivate();
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
//      *QGraphicsAnchorLayoutPrivate::acquireGraphicsAnchor(AnchorData
//      *data)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN28QGraphicsAnchorLayoutPrivate21acquireGraphicsAnchorEPN22QtGraphicsAnchorLayout10AnchorDataE(
    QGraphicsAnchorLayoutPrivate *self,
    AnchorData *data) {
  return self->acquireGraphicsAnchor(data);
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

//  QLayoutStyleInfo &QGraphicsAnchorLayoutPrivate::styleInfo() const
extern "C" Q_DECL_EXPORT
QLayoutStyleInfo *ritual_ZNK28QGraphicsAnchorLayoutPrivate9styleInfoEv(
    const QGraphicsAnchorLayoutPrivate *self) {
  return &(self->styleInfo());
}

//  void QGraphicsAnchorLayoutPrivate::restoreSimplifiedGraph(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate22restoreSimplifiedGraphEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  self->restoreSimplifiedGraph(orientation);
}

//  void QGraphicsAnchorLayoutPrivate::restoreSimplifiedAnchor(AnchorData
//      *edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate23restoreSimplifiedAnchorEPN22QtGraphicsAnchorLayout10AnchorDataE(
    QGraphicsAnchorLayoutPrivate *self,
    AnchorData *edge) {
  self->restoreSimplifiedAnchor(edge);
}

//  void QGraphicsAnchorLayoutPrivate::restoreSimplifiedConstraints(ParallelA
//      nchorData *parallel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate28restoreSimplifiedConstraintsEPN22QtGraphicsAnchorLayout18ParallelAnchorDataE(
    QGraphicsAnchorLayoutPrivate *self,
    ParallelAnchorData *parallel) {
  self->restoreSimplifiedConstraints(parallel);
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

//  void QGraphicsAnchorLayoutPrivate::identifyFloatItems(const
//      QSet<AnchorData *> &visited, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate18identifyFloatItemsERK4QSetIPN22QtGraphicsAnchorLayout10AnchorDataEEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    const QSet<AnchorData *> *visited,
    Qt::Orientation orientation) {
  self->identifyFloatItems(*visited, orientation);
}

//  void QGraphicsAnchorLayoutPrivate::identifyNonFloatItems_helper(const
//      AnchorData *ad, QSet<QGraphicsLayoutItem *>
//      *nonFloatingItemsIdentifiedSoFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate28identifyNonFloatItems_helperEPKN22QtGraphicsAnchorLayout10AnchorDataEP4QSetIP19QGraphicsLayoutItemE(
    QGraphicsAnchorLayoutPrivate *self,
    const AnchorData *ad,
    QSet<QGraphicsLayoutItem *> *nonFloatingItemsIdentifiedSoFar) {
  self->identifyNonFloatItems_helper(ad, nonFloatingItemsIdentifiedSoFar);
}

//  AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
//      std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> &itemEdge) const
extern "C" Q_DECL_EXPORT
AnchorVertex *ritual_ZNK28QGraphicsAnchorLayoutPrivate14internalVertexERKSt4pairIP19QGraphicsLayoutItemN2Qt11AnchorPointEE(
    const QGraphicsAnchorLayoutPrivate *self,
    const std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> *itemEdge) {
  return self->internalVertex(*itemEdge);
}

//  AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
//      QGraphicsLayoutItem *item, Qt::AnchorPoint edge) const
extern "C" Q_DECL_EXPORT
AnchorVertex *ritual_ZNK28QGraphicsAnchorLayoutPrivate14internalVertexEPK19QGraphicsLayoutItemN2Qt11AnchorPointE(
    const QGraphicsAnchorLayoutPrivate *self,
    const QGraphicsLayoutItem *item,
    Qt::AnchorPoint edge) {
  return self->internalVertex(item, edge);
}

//  void QGraphicsAnchorLayoutPrivate::changeLayoutVertex(Qt::Orientation
//      orientation, AnchorVertex *oldV, AnchorVertex *newV)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate18changeLayoutVertexEN2Qt11OrientationEPN22QtGraphicsAnchorLayout12AnchorVertexES4_(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation,
    AnchorVertex *oldV,
    AnchorVertex *newV) {
  self->changeLayoutVertex(orientation, oldV, newV);
}

//  AnchorVertex
//      *QGraphicsAnchorLayoutPrivate::addInternalVertex(QGraphicsLayoutItem
//      *item, Qt::AnchorPoint edge)
extern "C" Q_DECL_EXPORT
AnchorVertex *ritual_ZN28QGraphicsAnchorLayoutPrivate17addInternalVertexEP19QGraphicsLayoutItemN2Qt11AnchorPointE(
    QGraphicsAnchorLayoutPrivate *self,
    QGraphicsLayoutItem *item,
    Qt::AnchorPoint edge) {
  return self->addInternalVertex(item, edge);
}

//  void QGraphicsAnchorLayoutPrivate::setItemsGeometries(const QRectF &geom)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate18setItemsGeometriesERK6QRectF(
    QGraphicsAnchorLayoutPrivate *self,
    const QRectF *geom) {
  self->setItemsGeometries(*geom);
}

//  void
//      QGraphicsAnchorLayoutPrivate::calculateVertexPositions(Qt::Orientatio
//      n orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate24calculateVertexPositionsEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  self->calculateVertexPositions(orientation);
}

//  void
//      QGraphicsAnchorLayoutPrivate::setupEdgesInterpolation(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate23setupEdgesInterpolationEN2Qt11OrientationE(
    QGraphicsAnchorLayoutPrivate *self,
    Qt::Orientation orientation) {
  self->setupEdgesInterpolation(orientation);
}

//  void QGraphicsAnchorLayoutPrivate::interpolateEdge(AnchorVertex *base,
//      AnchorData *edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsAnchorLayoutPrivate15interpolateEdgeEPN22QtGraphicsAnchorLayout12AnchorVertexEPNS0_10AnchorDataE(
    QGraphicsAnchorLayoutPrivate *self,
    AnchorVertex *base,
    AnchorData *edge) {
  self->interpolateEdge(base, edge);
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
