//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/pointrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/pointrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qgraphsglobal_p.h>
#if QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area)
#include <QtGraphs/qlineseries.h>
#endif
#if QT_CONFIG(graphs_2d_scatter)
#include <QtGraphs/qscatterseries.h>
#endif
#if QT_CONFIG(graphs_2d_spline)
#include <QtGraphs/qsplineseries.h>
#endif
#if QT_CONFIG(graphs_2d_high_performance_backend)
#include <QtCanvasPainter/QCanvasPainter>
#endif
#include <QtQuick/private/qquickdraghandler_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtGraphs/private/axisrenderer_p.h>
#include <QtGraphs/private/charthelpers_p.h>
#include <QtGraphs/private/pointrenderer_p.h>
#include <QtGraphs/private/qgraphsview_p.h>
#include <QtGraphs/qabstractaxis.h>
#if QT_CONFIG(graphs_2d_bar)
#include <QtGraphs/QBarCategoryAxis>
#endif
#include <QtGraphs/QGraphsTheme>
#include <QtGraphs/private/axisrenderer_p.h>
#include <QtGraphs/private/qabstractaxis_p.h>
#include <QtGraphs/private/qdatetimeaxis_p.h>
#include <QtGraphs/private/qgraphsview_p.h>
#include <QtGraphs/private/qvalueaxis_p.h>
#include <QtGraphs/private/qlogvalueaxis_p.h>
#include <QtQuick/private/qquickdraghandler_p.h>
#include <QtGui/qfontmetrics.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 254, as _ZN13PointRenderer14getSeriesStyleEPNS_10PointGroupE
inline PointRenderer::SeriesStyle PointRenderer::getSeriesStyle(PointGroup *group)
{
    auto theme = m_graph->theme();

    const auto &seriesColors = theme->seriesColors();
    const auto &borderColors = theme->borderColors();

    qsizetype index = group->colorIndex % seriesColors.size();
    QColor color = group->series->color().alpha() != 0 ? group->series->color() : seriesColors.at(index);
    color.setAlpha(color.alpha() * group->series->opacity());

    QColor selectedColor = group->series->selectedColor().alpha() != 0
                               ? group->series->selectedColor()
                               : m_graph->theme()->singleHighlightColor();
    selectedColor.setAlpha(selectedColor.alpha() * group->series->opacity());

    index = group->colorIndex % borderColors.size();
    QColor borderColor = borderColors.at(index);
    borderColor.setAlpha(borderColor.alpha() * group->series->opacity());
    qreal borderWidth = theme->borderWidth();

    return {
        color,
        selectedColor,
        borderColor,
        borderWidth
    };
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 331, as _ZN13PointRenderer19destroyGroupMarkersEPNS_10PointGroupEx
inline void PointRenderer::destroyGroupMarkers(PointGroup *group, qsizetype keepCount)
{
    for (qsizetype i = keepCount; i < group->markers.size(); ++i)
        group->markers.at(i)->deleteLater();
    group->markers.resize(keepCount);
    group->dragHandlers.resize(keepCount);

    if (group == m_pressedGroup && m_pressedPointIndex >= keepCount)
        forgetPressedPoint(group->series);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 193, as _ZNK12AxisRenderer8getAxisXEP15QAbstractSeries
inline const AxisRenderer::AxisProperties &AxisRenderer::getAxisX(QAbstractSeries *series) const
{
    for (auto &&ax : *m_horzAxes) {
        if (ax.axis && (ax.axis == series->axisX() || ax.axis == series->axisY()))
            return ax;
    }
    return (*m_horzAxes)[0];
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 202, as _ZNK12AxisRenderer8getAxisYEP15QAbstractSeries
inline const AxisRenderer::AxisProperties &AxisRenderer::getAxisY(QAbstractSeries *series) const
{
    for (auto &&ax : *m_vertAxes) {
        if (ax.axis && (ax.axis == series->axisX() || ax.axis == series->axisY()))
            return ax;
    }
    return (*m_vertAxes)[0];
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 80, as _ZN13PointRendererD1Ev
inline PointRenderer::~PointRenderer()
{
    qDeleteAll(m_groups);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 85, as _ZN13PointRenderer19resetShapePathCountEv
inline void PointRenderer::resetShapePathCount()
{
    m_currentShapePathIndex = 0;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 105, as _ZN13PointRenderer15synchronizeDataEv
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline void PointRenderer::synchronizeData()
{
    m_pointPaintSnapshot.clear();
    for (const auto &group : std::as_const(m_groups)) {
        if (group->painterPath.elementCount() == 0)
            continue;

        const auto style = getSeriesStyle(group);

        qreal width = 1.0;
        QCanvasPainter::LineCap capStyle = QCanvasPainter::LineCap::Round;
#if QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area)
        if (auto line = qobject_cast<QLineSeries *>(group->series)) {
            width = line->width();
            switch (line->capStyle()) {
            case Qt::PenCapStyle::FlatCap:
                capStyle = QCanvasPainter::LineCap::Butt;
                break;
            case Qt::PenCapStyle::RoundCap:
                capStyle = QCanvasPainter::LineCap::Round;
                break;
            case Qt::PenCapStyle::SquareCap:
                capStyle = QCanvasPainter::LineCap::Square;
                break;
            default:
                break;
            }
        }
#endif
#if QT_CONFIG(graphs_2d_spline)
#if QT_CONFIG(graphs_2d_line)
        else
#endif
        if (auto spline = qobject_cast<QSplineSeries *>(group->series)) {
            width = spline->width();
            switch (spline->capStyle()) {
            case Qt::PenCapStyle::FlatCap:
                capStyle = QCanvasPainter::LineCap::Butt;
                break;
            case Qt::PenCapStyle::RoundCap:
                capStyle = QCanvasPainter::LineCap::Round;
                break;
            case Qt::PenCapStyle::SquareCap:
                capStyle = QCanvasPainter::LineCap::Square;
                break;
            default:
                break;
            }
        }
#endif
        m_pointPaintSnapshot.append({group->painterPath, style.color, width, capStyle});
    }
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 912, as _ZN13PointRenderer12updateSeriesEP9QXYSeries
inline void PointRenderer::updateSeries(QXYSeries *series)
{
    Q_UNUSED(series);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 917, as _ZN13PointRenderer22seriesAboutToBeRemovedEP15QAbstractSeries
inline void PointRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
{
    if (auto *xySeries = qobject_cast<QXYSeries *>(series)) {
        auto iter = m_groups.find(xySeries);

        if (iter != m_groups.end()) {
            auto group = (*iter);

            disconnect(xySeries, &QXYSeries::pointRemoved, this, nullptr);
            disconnect(xySeries, &QXYSeries::pointsRemoved, this, nullptr);
            disconnect(xySeries, &QXYSeries::pointAdded, this, nullptr);
            disconnect(xySeries, &QXYSeries::pointsAdded, this, nullptr);
            disconnect(xySeries, &QXYSeries::pointsReplaced, this, nullptr);

            destroyGroupMarkers(group);

            delete *iter;
            m_groups.erase(iter);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 944, as _ZN13PointRenderer15handleHoverMoveEP11QHoverEvent
inline bool PointRenderer::handleHoverMove(QHoverEvent *event)
{
    bool handled = false;
    const QPointF &position = event->position();

    for (auto &&group : m_groups) {
        if (!group->series->isHoverable() || !group->series->isVisible())
            continue;

        auto axisRenderer = group->series->graph()->m_axisRenderer;
        auto &axisX = axisRenderer->getAxisX(group->series);
        auto &axisY = axisRenderer->getAxisY(group->series);

        bool isHNegative = axisX.maxValue < axisX.minValue;
        bool isVNegative = axisY.maxValue < axisY.minValue;

        if (group->series->type() == QAbstractSeries::SeriesType::Scatter) {
            const QString &name = group->series->name();

            bool hovering = false;

            int index = 0;
            for (auto &&rect : group->rects) {
                if (rect.contains(position.toPoint())) {
                    if (!group->hover) {
                        group->hover = true;
                        emit group->series->hoverEnter(name, position, group->series->at(index));
                    }
                    emit group->series->hover(name, position, group->series->at(index));
                    hovering = true;
                }
                index++;
            }

            if (!hovering && group->hover) {
                group->hover = false;
                emit group->series->hoverExit(name, position);
            }
        } else {
            const qreal x0 = event->position().x();
            const qreal y0 = event->position().y();

            const qreal hoverSize = defaultSize(group->series) / 2.0;
            const QString &name = group->series->name();
            auto &&points = group->series->points();
            // True when line, false when spline
            const bool isLine = group->series->type() == QAbstractSeries::SeriesType::Line;
            if (points.size() >= 2) {
                bool hovering = false;
                auto subpath = group->painterPath.toSubpathPolygons();

                if (group->painterPath.elementCount() != points.size())
                    m_graph->ensurePolished();

                for (int i = 0; i < points.size() - 1; i++) {
                    qreal x1, y1, x2, y2;
                    if (i == 0) {
                        auto element1 = group->painterPath.elementAt(0);
                        auto element2 = group->painterPath.elementAt(isLine ? 1 : 3);
                        x1 = isHNegative ? element2.x : element1.x;
                        y1 = element1.y;
                        x2 = isHNegative ? element1.x : element2.x;
                        y2 = element2.y;
                    } else {
                        bool n = isVNegative | isHNegative;
                        // Each Spline (cubicTo) has 3 elements where third one is the x & y.
                        // So content of elements are:
                        // With Spline:
                        // [0] : MoveToElement
                        // [1] : 1. CurveToElement (c1x, c1y)
                        // [2] : 1. CurveToDataElement (c2x, c2y)
                        // [3] : 1. CurveToDataElement (x, y)
                        // [4] : 2. CurveToElement (c1x, c1y)
                        // ...
                        // With Line:
                        // [0] : MoveToElement
                        // [1] : 1. LineToElement (x, y)
                        // [2] : 2. LineToElement (x, y)
                        // ...
                        int element1Index = n ? (i + 1) : i;
                        int element2Index = n ? i : (i + 1);
                        element1Index = isLine ? element1Index : element1Index * 3;
                        element2Index = isLine ? element2Index : element2Index * 3;
                        auto element1 = group->painterPath.elementAt(element1Index);
                        auto element2 = group->painterPath.elementAt(element2Index);
                        x1 = element1.x;
                        y1 = element1.y;
                        x2 = element2.x;
                        y2 = element2.y;
                    }

                    if (isLine) {
                        qreal denominator = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
                        qreal hoverDistance = qAbs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
                                              / qSqrt(denominator);

                        if (hoverDistance < hoverSize) {
                            qreal alpha = 0;
                            qreal extrapolation = 0;
                            if (x2 - x1 >= y2 - y1) {
                                if (x2 - x1 != 0) {
                                    alpha = ((x2 - x1) - (x0 - x1)) / qAbs(x2 - x1);
                                    extrapolation = hoverSize / qAbs(x2 - x1);
                                }
                            } else {
                                if (y2 - y1 != 0) {
                                    alpha = ((y2 - y1) - (y0 - y1)) / qAbs(y2 - y1);
                                    extrapolation = hoverSize / qAbs(y2 - y1);
                                }
                            }

                            if (alpha >= -extrapolation && alpha <= 1.0 + extrapolation) {
                                bool n = isVNegative | isHNegative;

                                const QPointF &point1 = points[n ? i + 1 : i];
                                const QPointF &point2 = points[n ? i : i + 1];

                                QPointF point = (point2 * (1.0 - alpha)) + (point1 * alpha);

                                if (!group->hover) {
                                    group->hover = true;
                                    group->series->setHovered(true);
                                    emit group->series->hoverEnter(name, position, point);
                                }

                                emit group->series->hover(name, position, point);
                                hovering = true;
                                handled = true;
                            }
                        }
                    } else { // Spline
                        auto segments = subpath[0];

                        for (auto it = segments.begin(); it != segments.end(); ++it) {
                            if (std::next(it, 1) == segments.end())
                                break;

                            auto it2 = std::next(it, 1);

                            qreal denominator = (it2->x() - it->x()) * (it2->x() - it->x())
                                                + (it2->y() - it->y()) * (it2->y() - it->y());
                            qreal hoverDistance = qAbs((it2->x() - it->x()) * (it->y() - y0)
                                                       - (it->x() - x0) * (it2->y() - it->y()))
                                                  / qSqrt(denominator);

                            if (hoverDistance < hoverSize) {
                                qreal alpha = 0;
                                qreal extrapolation = 0;
                                if (it2->x() - it->x() >= it2->y() - it->y()) {
                                    if (it2->x() - it->x() != 0) {
                                        alpha = ((it2->x() - it->x()) - (x0 - it->x()))
                                                / qAbs(it2->x() - it->x());
                                        extrapolation = hoverSize / qAbs(it2->x() - it->x());
                                    }
                                } else {
                                    if (it2->y() - it->y() != 0) {
                                        alpha = ((it2->y() - it->y()) - (y0 - it->y()))
                                                / qAbs(it2->y() - it->y());
                                        extrapolation = hoverSize / qAbs(it2->y() - it->y());
                                    }
                                }

                                if (alpha >= -extrapolation && alpha <= 1.0 + extrapolation) {
                                    qreal cx1, cy1, cx2, cy2;

                                    reverseRenderCoordinates(axisRenderer,
                                                             group->series,
                                                             it->x(),
                                                             it->y(),
                                                             &cx1,
                                                             &cy1);
                                    reverseRenderCoordinates(axisRenderer,
                                                             group->series,
                                                             it2->x(),
                                                             it2->y(),
                                                             &cx2,
                                                             &cy2);

                                    const QPointF &point1 = {cx1, cy1};
                                    const QPointF &point2 = {cx2, cy2};

                                    QPointF point = (point2 * (1.0 - alpha)) + (point1 * alpha);

                                    if (!group->hover) {
                                        group->hover = true;
                                        emit group->series->hoverEnter(name, position, point);
                                    }

                                    emit group->series->hover(name, position, point);
                                    hovering = true;
                                    handled = true;
                                }
                            }
                        }
                    }
                }

                if (!hovering && group->hover) {
                    group->hover = false;
                    group->series->setHovered(false);
                    emit group->series->hoverExit(name, position);
                    handled = true;
                }
            }
        }
    }
    return handled;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 1154, as _ZN13PointRenderer24reverseRenderCoordinatesEP15QAbstractSeriesdd
inline QPointF PointRenderer::reverseRenderCoordinates(QAbstractSeries *series, qreal x, qreal y)
{
    m_areaWidth = width();
    m_areaHeight = height();

    auto &axisX = m_graph->m_axisRenderer->getAxisX(series);
    auto &axisY = m_graph->m_axisRenderer->getAxisY(series);

    m_maxVertical = axisY.valueRange > 0 ? 1.0 / axisY.valueRange : 100.0;
    m_maxHorizontal = axisX.valueRange > 0 ? 1.0 / axisX.valueRange : 100.0;

    auto vmin = axisY.minValue > axisY.maxValue ? std::abs(axisY.minValue) : axisY.minValue;
    m_verticalOffset = (vmin / axisY.valueRange) * m_areaHeight;

    auto hmin = axisX.minValue > axisX.maxValue ? std::abs(axisX.minValue) : axisX.minValue;
    m_horizontalOffset = (hmin / axisX.valueRange) * m_areaWidth;

    qreal x0;
    qreal y0;

    reverseRenderCoordinates(m_graph->m_axisRenderer, series, x, y, &x0, &y0);

    return QPointF(x0, y0);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 166, as _ZN13PointRenderer11defaultSizeEP9QXYSeries
inline qreal PointRenderer::defaultSize(QXYSeries *series)
{
    qreal size = 16.0;
    if (series != nullptr) {
#if QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area)
        if (auto line = qobject_cast<QLineSeries *>(series))
            size = qMax(size, line->width());
#endif
#if (QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area)) && QT_CONFIG(graphs_2d_spline)
        else
#endif
#if QT_CONFIG(graphs_2d_spline)
            if (auto spline = qobject_cast<QSplineSeries *>(series))
            size = qMax(size, spline->width());
#endif
    }
    return size;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 185, as _ZN13PointRenderer26calculateRenderCoordinatesEP12AxisRendererP15QAbstractSeriesddPdS4_
inline void PointRenderer::calculateRenderCoordinates(AxisRenderer *axisRenderer,
                                               QAbstractSeries *series,
                                               qreal origX,
                                               qreal origY,
                                               qreal *renderX,
                                               qreal *renderY)
{
    auto &axisX = axisRenderer->getAxisX(series);
    auto &axisY = axisRenderer->getAxisY(series);

    qreal x = origX;
    qreal y = origY;

    if (axisX.isLogarithmic) {
        float logBase = log(axisX.logBase);
        x = log(origX) / logBase;
    }

    if (axisY.isLogarithmic) {
        float logBase = log(axisY.logBase);
        y = log(origY) / logBase;
    }

    if (m_graph->orientation() != Qt::Vertical) {
        std::swap(x, y);
        y = axisY.maxValue - y;
    }

    auto flipX = axisX.maxValue < axisX.minValue ? -1 : 1;
    auto flipY = axisY.maxValue < axisY.minValue ? -1 : 1;

    *renderX = m_areaWidth * flipX * x * m_maxHorizontal - m_horizontalOffset;
    *renderY = m_areaHeight - m_areaHeight * flipY * y * m_maxVertical
               + m_verticalOffset;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 221, as _ZN13PointRenderer24reverseRenderCoordinatesEP12AxisRendererP15QAbstractSeriesddPdS4_
inline void PointRenderer::reverseRenderCoordinates(AxisRenderer *axisRenderer,
                                             QAbstractSeries *series,
                                             qreal renderX,
                                             qreal renderY,
                                             qreal *origX,
                                             qreal *origY)
{
    auto &axisX = axisRenderer->getAxisX(series);
    auto &axisY = axisRenderer->getAxisY(series);

    if (m_graph->orientation() != Qt::Vertical) {
        std::swap(renderX, renderY);
        renderY = m_areaHeight - renderY;
    }

    auto flipX = axisX.maxValue < axisX.minValue ? -1 : 1;
    auto flipY = axisY.maxValue < axisY.minValue ? -1 : 1;

    float x = (renderX + m_horizontalOffset) / (m_areaWidth * flipX * m_maxHorizontal);
    float y = (renderY - m_areaHeight - m_verticalOffset)
             / (-1 * m_areaHeight * flipY * m_maxVertical);

    if (axisX.isLogarithmic)
        x = pow(axisX.logBase, x);

    if (axisY.isLogarithmic)
        y = pow(axisY.logBase, y);

    *origX = x;
    *origY = y;

}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 319, as _ZN13PointRenderer18hidePointDelegatesEP9QXYSeries
inline void PointRenderer::hidePointDelegates(QXYSeries *series)
{
    auto *group = m_groups.value(series);
    if (group->currentMarker) {
        for (int i = 0; i < group->markers.size(); ++i) {
            auto *marker = group->markers[i];
            marker->setVisible(false);
        }
    }
    group->rects.clear();
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 348, as _ZN13PointRenderer14onSingleTappedE11QEventPointN2Qt11MouseButtonE
inline void PointRenderer::onSingleTapped(QEventPoint eventPoint, Qt::MouseButton button)
{
    Q_UNUSED(button)

    for (auto &&group : m_groups) {
        if (!group->series->isVisible())
            continue;

        if (!group->series->isSelectable() && !group->series->isDraggable())
            continue;

        int index = 0;
        for (auto &&rect : group->rects) {
            if (rect.contains(eventPoint.position())) {
                emit group->series->clicked(group->series->at(index).toPoint());
                return;
            }
            index++;
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 370, as _ZN13PointRenderer14onDoubleTappedE11QEventPointN2Qt11MouseButtonE
inline void PointRenderer::onDoubleTapped(QEventPoint eventPoint, Qt::MouseButton button)
{
    Q_UNUSED(button)

    for (auto &&group : m_groups) {
        if (!group->series->isVisible())
            continue;

        if (!group->series->isSelectable() && !group->series->isDraggable())
            continue;

        int index = 0;
        for (auto &&rect : group->rects) {
            if (rect.contains(eventPoint.position())) {
                emit group->series->doubleClicked(group->series->at(index).toPoint());
                return;
            }
            index++;
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 392, as _ZN13PointRenderer16onPressedChangedEv
inline void PointRenderer::onPressedChanged()
{
    if (m_tapHandler->isPressed()) {
        for (auto &&group : m_groups) {
            if (!group->series->isVisible())
                continue;

            if (!group->series->isSelectable() && !group->series->isDraggable())
                continue;

            int index = 0;
            for (auto &&rect : group->rects) {
                if (rect.contains(m_tapHandler->point().position())) {
                    m_pressedGroup = group;
                    m_pressedPointIndex = index;
                    emit group->series->pressed(m_pressedGroup->series->at(index).toPoint());
                }
                index++;
            }
        }
    } else {
        if (m_pressedGroup
            && m_pressedGroup->series->isSelectable()
            && m_pressedGroup->series->isVisible()) {
            if (m_pressedGroup->rects[m_pressedPointIndex].contains(
                    m_tapHandler->point().position())) {
                if (m_pressedGroup->series->isPointSelected(m_pressedPointIndex))
                    m_pressedGroup->series->deselectPoint(m_pressedPointIndex);
                else
                    m_pressedGroup->series->selectPoint(m_pressedPointIndex);
                m_previousDelta = QPoint(0, 0);
                emit m_pressedGroup->series->released(
                    m_pressedGroup->series->at(m_pressedPointIndex).toPoint());
            }
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 430, as _ZN13PointRenderer33adjustPressedPointIndexForRemovalEP9QXYSeriesxx
inline void PointRenderer::adjustPressedPointIndexForRemoval(QXYSeries *series,
                                                      qsizetype removedIndex,
                                                      qsizetype removedCount)
{
    if (!m_pressedGroup || m_pressedGroup->series != series)
        return;

    if (m_pressedPointIndex >= removedIndex + removedCount) {
        m_pressedPointIndex -= removedCount;
    } else if (m_pressedPointIndex >= removedIndex) {
        m_pressedGroup = nullptr;
        m_pressedPointIndex = 0;
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 445, as _ZN13PointRenderer35adjustPressedPointIndexForInsertionEP9QXYSeriesxx
inline void PointRenderer::adjustPressedPointIndexForInsertion(QXYSeries *series,
                                                        qsizetype insertedIndex,
                                                        qsizetype insertedCount)
{
    if (!m_pressedGroup || m_pressedGroup->series != series)
        return;

    if (m_pressedPointIndex >= insertedIndex)
        m_pressedPointIndex += insertedCount;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/pointrenderer.cpp, line 456, as _ZN13PointRenderer18forgetPressedPointEP9QXYSeries
inline void PointRenderer::forgetPressedPoint(QXYSeries *series)
{
    if (m_pressedGroup && m_pressedGroup->series == series) {
        m_pressedGroup = nullptr;
        m_pressedPointIndex = 0;
    }
}
//  -----------------------------------------------------------------------

//  A PointRenderer that Python can take functions over in. Every PointRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CutePointRendererCall0)(const void *, int *);
typedef const QRectF * (*CutePointRendererCall1)(const void *, int *);
typedef bool (*CutePointRendererCall2)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CutePointRendererCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CutePointRendererCall4)(const void *, int *);
typedef void * (*CutePointRendererCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePointRendererCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CutePointRendererCall8)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CutePointRendererCall9)(const void *, int *);
typedef void (*CutePointRendererCall10)(const void *, int *);
typedef void (*CutePointRendererCall11)(const void *, QKeyEvent *, int *);
typedef void (*CutePointRendererCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CutePointRendererCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CutePointRendererCall14)(const void *, QFocusEvent *, int *);
typedef void (*CutePointRendererCall15)(const void *, QFocusEvent *, int *);
typedef void (*CutePointRendererCall16)(const void *, QMouseEvent *, int *);
typedef void (*CutePointRendererCall17)(const void *, QMouseEvent *, int *);
typedef void (*CutePointRendererCall18)(const void *, QMouseEvent *, int *);
typedef void (*CutePointRendererCall19)(const void *, QMouseEvent *, int *);
typedef void (*CutePointRendererCall20)(const void *, int *);
typedef void (*CutePointRendererCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CutePointRendererCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CutePointRendererCall23)(const void *, QTouchEvent *, int *);
typedef void (*CutePointRendererCall24)(const void *, QHoverEvent *, int *);
typedef void (*CutePointRendererCall25)(const void *, QHoverEvent *, int *);
typedef void (*CutePointRendererCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CutePointRendererCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CutePointRendererCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CutePointRendererCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CutePointRendererCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CutePointRendererCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CutePointRendererCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CutePointRendererCall33)(const void *, int *);
typedef void (*CutePointRendererCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePointRendererCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePointRendererCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CutePointRenderer : public PointRenderer {
public:
  using PointRenderer::PointRenderer;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[0]) {
      int handled = 0;
      CutePointRendererCall0 call = reinterpret_cast<CutePointRendererCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[1]) {
      int handled = 0;
      CutePointRendererCall1 call = reinterpret_cast<CutePointRendererCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CutePointRendererCall2 call = reinterpret_cast<CutePointRendererCall2>(taken[2]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[3]) {
      int handled = 0;
      CutePointRendererCall3 call = reinterpret_cast<CutePointRendererCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[4]) {
      int handled = 0;
      CutePointRendererCall4 call = reinterpret_cast<CutePointRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CutePointRendererCall5 call = reinterpret_cast<CutePointRendererCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CutePointRendererCall6 call = reinterpret_cast<CutePointRendererCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[7]) {
      int handled = 0;
      CutePointRendererCall7 call = reinterpret_cast<CutePointRendererCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[8]) {
      int handled = 0;
      CutePointRendererCall8 call = reinterpret_cast<CutePointRendererCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CutePointRendererCall9 call = reinterpret_cast<CutePointRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CutePointRendererCall10 call = reinterpret_cast<CutePointRendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CutePointRendererCall11 call = reinterpret_cast<CutePointRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CutePointRendererCall12 call = reinterpret_cast<CutePointRendererCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CutePointRendererCall13 call = reinterpret_cast<CutePointRendererCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CutePointRendererCall14 call = reinterpret_cast<CutePointRendererCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CutePointRendererCall15 call = reinterpret_cast<CutePointRendererCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CutePointRendererCall16 call = reinterpret_cast<CutePointRendererCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CutePointRendererCall17 call = reinterpret_cast<CutePointRendererCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CutePointRendererCall18 call = reinterpret_cast<CutePointRendererCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CutePointRendererCall19 call = reinterpret_cast<CutePointRendererCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CutePointRendererCall20 call = reinterpret_cast<CutePointRendererCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CutePointRendererCall21 call = reinterpret_cast<CutePointRendererCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CutePointRendererCall22 call = reinterpret_cast<CutePointRendererCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CutePointRendererCall23 call = reinterpret_cast<CutePointRendererCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CutePointRendererCall24 call = reinterpret_cast<CutePointRendererCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CutePointRendererCall25 call = reinterpret_cast<CutePointRendererCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CutePointRendererCall26 call = reinterpret_cast<CutePointRendererCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CutePointRendererCall27 call = reinterpret_cast<CutePointRendererCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CutePointRendererCall28 call = reinterpret_cast<CutePointRendererCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CutePointRendererCall29 call = reinterpret_cast<CutePointRendererCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CutePointRendererCall30 call = reinterpret_cast<CutePointRendererCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CutePointRendererCall31 call = reinterpret_cast<CutePointRendererCall31>(taken[31]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CutePointRendererCall32 call = reinterpret_cast<CutePointRendererCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CutePointRendererCall33 call = reinterpret_cast<CutePointRendererCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CutePointRendererCall34 call = reinterpret_cast<CutePointRendererCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CutePointRendererCall35 call = reinterpret_cast<CutePointRendererCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CutePointRendererCall36 call = reinterpret_cast<CutePointRendererCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CutePointRendererCall37 call = reinterpret_cast<CutePointRendererCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CutePointRendererCall38 call = reinterpret_cast<CutePointRendererCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CutePointRendererCall39 call = reinterpret_cast<CutePointRendererCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CutePointRendererCall40 call = reinterpret_cast<CutePointRendererCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *PointRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13PointRenderer10metaObjectEv(
    const PointRenderer *self) {
  return self->metaObject();
}

//  PointRenderer::~PointRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRendererD1Ev(PointRenderer *self) {
  delete self;
}

//  void PointRenderer::resetShapePathCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer19resetShapePathCountEv(PointRenderer *self) {
  self->resetShapePathCount();
}

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void PointRenderer::synchronizeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer15synchronizeDataEv(PointRenderer *self) {
  self->synchronizeData();
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  void PointRenderer::updateSeries(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer12updateSeriesEP9QXYSeries(
    PointRenderer *self,
    QXYSeries *series) {
  self->updateSeries(series);
}

//  void PointRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer22seriesAboutToBeRemovedEP15QAbstractSeries(
    PointRenderer *self,
    QAbstractSeries *series) {
  self->seriesAboutToBeRemoved(series);
}

//  bool PointRenderer::handleHoverMove(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13PointRenderer15handleHoverMoveEP11QHoverEvent(
    PointRenderer *self,
    QHoverEvent *event) {
  return self->handleHoverMove(event);
}

//  QPointF PointRenderer::reverseRenderCoordinates(QAbstractSeries *series,
//      qreal x, qreal y)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN13PointRenderer24reverseRenderCoordinatesEP15QAbstractSeriesdd(
    PointRenderer *self,
    QAbstractSeries *series,
    qreal x,
    qreal y) {
  return new QPointF(self->reverseRenderCoordinates(series, x, y));
}

//  qreal PointRenderer::defaultSize(QXYSeries *series)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN13PointRenderer11defaultSizeEP9QXYSeries(
    PointRenderer *self,
    QXYSeries *series) {
  return self->defaultSize(series);
}

//  void PointRenderer::calculateRenderCoordinates(AxisRenderer
//      *axisRenderer, QAbstractSeries *series, qreal origX, qreal origY,
//      qreal *renderX, qreal *renderY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer26calculateRenderCoordinatesEP12AxisRendererP15QAbstractSeriesddPdS4_(
    PointRenderer *self,
    AxisRenderer *axisRenderer,
    QAbstractSeries *series,
    qreal origX,
    qreal origY,
    qreal *renderX,
    qreal *renderY) {
  self->calculateRenderCoordinates(
      axisRenderer,
      series,
      origX,
      origY,
      renderX,
      renderY);
}

//  void PointRenderer::reverseRenderCoordinates(AxisRenderer *axisRenderer,
//      QAbstractSeries *series, qreal renderX, qreal renderY, qreal *origX,
//      qreal *origY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer24reverseRenderCoordinatesEP12AxisRendererP15QAbstractSeriesddPdS4_(
    PointRenderer *self,
    AxisRenderer *axisRenderer,
    QAbstractSeries *series,
    qreal renderX,
    qreal renderY,
    qreal *origX,
    qreal *origY) {
  self->reverseRenderCoordinates(
      axisRenderer,
      series,
      renderX,
      renderY,
      origX,
      origY);
}

//  void PointRenderer::hidePointDelegates(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer18hidePointDelegatesEP9QXYSeries(
    PointRenderer *self,
    QXYSeries *series) {
  self->hidePointDelegates(series);
}

//  void PointRenderer::onSingleTapped(QEventPoint eventPoint,
//      Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer14onSingleTappedE11QEventPointN2Qt11MouseButtonE(
    PointRenderer *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->onSingleTapped(*eventPoint, button);
}

//  void PointRenderer::onDoubleTapped(QEventPoint eventPoint,
//      Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer14onDoubleTappedE11QEventPointN2Qt11MouseButtonE(
    PointRenderer *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->onDoubleTapped(*eventPoint, button);
}

//  void PointRenderer::onPressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer16onPressedChangedEv(PointRenderer *self) {
  self->onPressedChanged();
}

//  void PointRenderer::adjustPressedPointIndexForRemoval(QXYSeries *series,
//      qsizetype removedIndex, qsizetype removedCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer33adjustPressedPointIndexForRemovalEP9QXYSeriesxx(
    PointRenderer *self,
    QXYSeries *series,
    qsizetype removedIndex,
    qsizetype removedCount) {
  self->adjustPressedPointIndexForRemoval(
      series,
      removedIndex,
      removedCount);
}

//  void PointRenderer::adjustPressedPointIndexForInsertion(QXYSeries
//      *series, qsizetype insertedIndex, qsizetype insertedCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer35adjustPressedPointIndexForInsertionEP9QXYSeriesxx(
    PointRenderer *self,
    QXYSeries *series,
    qsizetype insertedIndex,
    qsizetype insertedCount) {
  self->adjustPressedPointIndexForInsertion(
      series,
      insertedIndex,
      insertedCount);
}

//  void PointRenderer::forgetPressedPoint(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13PointRenderer18forgetPressedPointEP9QXYSeries(
    PointRenderer *self,
    QXYSeries *series) {
  self->forgetPressedPoint(series);
}

//  a Python function taken by a CutePointRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PointRenderer(
    PointRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CutePointRenderer *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
