//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/axisticker_p.h>
#include <QtGraphs/private/axisgrid_p.h>
#include <QtGraphs/private/axisline_p.h>
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

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 31, as _ZN10AxisTicker12setupShadersEv
inline void AxisTicker::setupShaders()
{
    if (m_isHorizontal) {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.vert.qsb")));
    } else {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.vert.qsb")));
    }
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 195, as _ZN10AxisTicker15setIsHorizontalEb
inline void AxisTicker::setIsHorizontal(bool newIsHorizontal)
{
    if (m_isHorizontal == newIsHorizontal)
        return;
    m_isHorizontal = newIsHorizontal;
    setupShaders();
    emit isHorizontalChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 182, as _ZN10AxisTicker16setSubTickLengthEd
inline void AxisTicker::setSubTickLength(qreal newSubTickLength)
{
    if (QtPrivate::fuzzyCompare(m_subTickLength, newSubTickLength))
        return;
    m_subTickLength = newSubTickLength;
    emit subTickLengthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 65, as _ZN10AxisTicker8setOrigoEi
inline void AxisTicker::setOrigo(int newOrigo)
{
    if (m_origo == newOrigo)
        return;
    m_origo = newOrigo;
    emit origoChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 10, as _ZN10AxisTickerC1EP10QQuickItem
inline AxisTicker::AxisTicker(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 31, as _ZN8AxisGrid12setupShadersEv
inline void AxisGrid::setupShaders()
{
    setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.frag.qsb")));
    setVertexShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.vert.qsb")));
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 60, as _ZN8AxisGrid8setOrigoEi
inline void AxisGrid::setOrigo(int newOrigo)
{
    if (m_origo == newOrigo)
        return;
    m_origo = newOrigo;
    emit origoChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 10, as _ZN8AxisGridC1EP10QQuickItem
inline AxisGrid::AxisGrid(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 32, as _ZN8AxisLine12setupShadersEv
inline void AxisLine::setupShaders()
{
    if (m_isHorizontal) {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/lineshaderhorizontal.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/lineshaderhorizontal.vert.qsb")));
    } else {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/lineshadervertical.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/lineshadervertical.vert.qsb")));
    }
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 92, as _ZN8AxisLine15setIsHorizontalEb
inline void AxisLine::setIsHorizontal(bool newIsHorizontal)
{
    if (m_isHorizontal == newIsHorizontal)
        return;
    m_isHorizontal = newIsHorizontal;
    emit isHorizontalChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 10, as _ZN8AxisLineC1EP10QQuickItem
inline AxisLine::AxisLine(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{

}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 177, as _ZNK10AxisTicker13subTickLengthEv
inline qreal AxisTicker::subTickLength() const
{
    return m_subTickLength;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 209, as _ZN10AxisTicker10setFlippedEb
inline void AxisTicker::setFlipped(bool newFlipped)
{
    if (m_flipped == newFlipped)
        return;
    m_flipped = newFlipped;
    emit flippedChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 91, as _ZN10AxisTicker10setSpacingEd
inline void AxisTicker::setSpacing(qreal newSpacing)
{
    if (QtPrivate::fuzzyCompare(m_spacing, newSpacing))
        return;
    m_spacing = newSpacing;
    emit spacingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 52, as _ZN10AxisTicker12setSmoothingEd
inline void AxisTicker::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 130, as _ZN10AxisTicker12setTickColorE6QColor
inline void AxisTicker::setTickColor(QColor newTickColor)
{
    if (m_tickColor == newTickColor)
        return;
    m_tickColor = newTickColor;
    emit tickColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 222, as _ZN10AxisTicker14setLogarithmicEb
inline void AxisTicker::setLogarithmic(bool newLogarithmic)
{
    if (m_isLogarithmic == newLogarithmic)
        return;

    m_isLogarithmic = newLogarithmic;
    emit logarithmicChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 104, as _ZN10AxisTicker15setDisplacementEd
inline void AxisTicker::setDisplacement(qreal newDisplacement)
{
    if (QtPrivate::fuzzyCompare(m_displacement, newDisplacement))
        return;
    m_displacement = newDisplacement;
    emit displacementChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 117, as _ZN10AxisTicker15setSubTickColorE6QColor
inline void AxisTicker::setSubTickColor(QColor newSubTickColor)
{
    if (m_subTickColor == newSubTickColor)
        return;
    m_subTickColor = newSubTickColor;
    emit subTickColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 169, as _ZN10AxisTicker15setSubTickScaleEd
inline void AxisTicker::setSubTickScale(qreal newSubTickScale)
{
    if (QtPrivate::fuzzyCompare(m_subTickScale, newSubTickScale))
        return;
    m_subTickScale = newSubTickScale;
    emit subTickScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 156, as _ZN10AxisTicker16setTickLineWidthEd
inline void AxisTicker::setTickLineWidth(qreal newTickLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_tickLineWidth, newTickLineWidth))
        return;
    m_tickLineWidth = newTickLineWidth;
    emit tickLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 78, as _ZN10AxisTicker18setSubTicksVisibleEb
inline void AxisTicker::setSubTicksVisible(bool newSubTicksVisible)
{
    if (m_subTicksVisible == newSubTicksVisible)
        return;
    m_subTicksVisible = newSubTicksVisible;
    emit subTicksVisibleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 143, as _ZN10AxisTicker19setSubTickLineWidthEd
inline void AxisTicker::setSubTickLineWidth(qreal newSubTickLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_subTickLineWidth, newSubTickLineWidth))
        return;
    m_subTickLineWidth = newSubTickLineWidth;
    emit subTickLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 236, as _ZN10AxisTicker7setBaseEd
inline void AxisTicker::setBase(qreal newBase)
{
    if (qFuzzyCompare(m_base, newBase))
        return;

    m_base = newBase;
    emit baseChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 79, as _ZN8AxisLine12setLineWidthEd
inline void AxisLine::setLineWidth(qreal newLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_lineWidth, newLineWidth))
        return;
    m_lineWidth = newLineWidth;
    emit lineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 53, as _ZN8AxisLine12setSmoothingEd
inline void AxisLine::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 66, as _ZN8AxisLine8setColorE6QColor
inline void AxisLine::setColor(QColor newColor)
{
    if (m_color == newColor)
        return;
    m_color = newColor;
    emit colorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 172, as _ZNK8AxisGrid13gridLineWidthEv
inline qreal AxisGrid::gridLineWidth() const
{
    return m_gridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 74, as _ZNK8AxisLine9lineWidthEv
inline qreal AxisLine::lineWidth() const
{
    return m_lineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 48, as _ZNK8AxisLine9smoothingEv
inline qreal AxisLine::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 99, as _ZNK10AxisTicker12displacementEv
inline qreal AxisTicker::displacement() const
{
    return m_displacement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 164, as _ZNK10AxisTicker12subTickScaleEv
inline qreal AxisTicker::subTickScale() const
{
    return m_subTickScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 217, as _ZNK10AxisTicker13isLogarithmicEv
inline bool AxisTicker::isLogarithmic() const
{
    return m_isLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 151, as _ZNK10AxisTicker13tickLineWidthEv
inline qreal AxisTicker::tickLineWidth() const
{
    return m_tickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 73, as _ZNK10AxisTicker15subTicksVisibleEv
inline bool AxisTicker::subTicksVisible() const
{
    return m_subTicksVisible;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 138, as _ZNK10AxisTicker16subTickLineWidthEv
inline qreal AxisTicker::subTickLineWidth() const
{
    return m_subTickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 231, as _ZNK10AxisTicker4baseEv
inline qreal AxisTicker::base() const
{
    return m_base;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 86, as _ZNK10AxisTicker7spacingEv
inline qreal AxisTicker::spacing() const
{
    return m_spacing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 204, as _ZNK10AxisTicker9isFlippedEv
inline bool AxisTicker::isFlipped() const
{
    return m_flipped;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 47, as _ZNK10AxisTicker9smoothingEv
inline qreal AxisTicker::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 138, as _ZN8AxisGrid12setGridColorE6QColor
inline void AxisGrid::setGridColor(QColor newGridColor)
{
    if (m_gridColor == newGridColor)
        return;
    m_gridColor = newGridColor;
    emit gridColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 86, as _ZN8AxisGrid12setGridWidthEd
inline void AxisGrid::setGridWidth(qreal newGridWidth)
{
    if (QtPrivate::fuzzyCompare(m_gridWidth, newGridWidth))
        return;
    m_gridWidth = newGridWidth;
    emit gridWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 47, as _ZN8AxisGrid12setSmoothingEd
inline void AxisGrid::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 99, as _ZN8AxisGrid13setGridHeightEd
inline void AxisGrid::setGridHeight(qreal newGridHeight)
{
    if (QtPrivate::fuzzyCompare(m_gridHeight, newGridHeight))
        return;
    m_gridHeight = newGridHeight;
    emit gridHeightChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 112, as _ZN8AxisGrid15setGridMovementE7QPointF
inline void AxisGrid::setGridMovement(QPointF newGridMovement)
{
    if (m_gridMovement == newGridMovement)
        return;
    m_gridMovement = newGridMovement;
    emit gridMovementChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 125, as _ZN8AxisGrid15setSubGridColorE6QColor
inline void AxisGrid::setSubGridColor(QColor newSubGridColor)
{
    if (m_subGridColor == newSubGridColor)
        return;
    m_subGridColor = newSubGridColor;
    emit subGridColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 242, as _ZN8AxisGrid15setVerticalBaseEd
inline void AxisGrid::setVerticalBase(qreal newBase)
{
    if (qFuzzyCompare(m_verticalBase, newBase))
        return;
    m_verticalBase = newBase;
    emit verticalBaseChanged(newBase);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 177, as _ZN8AxisGrid16setGridLineWidthEd
inline void AxisGrid::setGridLineWidth(qreal newGridLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_gridLineWidth, newGridLineWidth))
        return;
    m_gridLineWidth = newGridLineWidth;
    emit gridLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 73, as _ZN8AxisGrid17setGridVisibilityERK9QVector4D
inline void AxisGrid::setGridVisibility(const QVector4D &newGridVisibility)
{
    if (m_gridVisibility == newGridVisibility)
        return;
    m_gridVisibility = newGridVisibility;
    emit gridVisibilityChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 255, as _ZN8AxisGrid17setHorizontalBaseEd
inline void AxisGrid::setHorizontalBase(qreal newBase)
{
    if (qFuzzyCompare(m_horizontalBase, newBase))
        return;
    m_horizontalBase = newBase;
    emit verticalBaseChanged(newBase);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 164, as _ZN8AxisGrid19setSubGridLineWidthEd
inline void AxisGrid::setSubGridLineWidth(qreal newSubGridLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_subGridLineWidth, newSubGridLineWidth))
        return;
    m_subGridLineWidth = newSubGridLineWidth;
    emit subGridLineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 216, as _ZN8AxisGrid22setVerticalLogarithmicEb
inline void AxisGrid::setVerticalLogarithmic(bool newLogarithmic)
{
    if (m_isVerticalLogarithmic == newLogarithmic)
        return;
    m_isVerticalLogarithmic = newLogarithmic;
    emit verticalLogarithmicChanged(newLogarithmic);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 190, as _ZN8AxisGrid23setVerticalSubGridScaleEd
inline void AxisGrid::setVerticalSubGridScale(qreal newVerticalSubGridScale)
{
    if (QtPrivate::fuzzyCompare(m_verticalSubGridScale, newVerticalSubGridScale))
        return;
    m_verticalSubGridScale = newVerticalSubGridScale;
    emit verticalSubGridScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 229, as _ZN8AxisGrid24setHorizontalLogarithmicEb
inline void AxisGrid::setHorizontalLogarithmic(bool newLogarithmic)
{
    if (m_isHorizontalLogarithmic == newLogarithmic)
        return;
    m_isHorizontalLogarithmic = newLogarithmic;
    emit horizontalLogarithmicChanged(newLogarithmic);
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 203, as _ZN8AxisGrid25setHorizontalSubGridScaleEd
inline void AxisGrid::setHorizontalSubGridScale(qreal newHorizontalSubGridScale)
{
    if (QtPrivate::fuzzyCompare(m_horizontalSubGridScale, newHorizontalSubGridScale))
        return;
    m_horizontalSubGridScale = newHorizontalSubGridScale;
    emit horizontalSubGridScaleChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 151, as _ZN8AxisGrid26setPlotAreaBackgroundColorE6QColor
inline void AxisGrid::setPlotAreaBackgroundColor(QColor color)
{
    if (m_plotAreaBackgroundColor == color)
        return;
    m_plotAreaBackgroundColor = color;
    emit plotAreaBackgroundColorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 94, as _ZNK8AxisGrid10gridHeightEv
inline qreal AxisGrid::gridHeight() const
{
    return m_gridHeight;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 107, as _ZNK8AxisGrid12gridMovementEv
inline QPointF AxisGrid::gridMovement() const
{
    return m_gridMovement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 237, as _ZNK8AxisGrid12verticalBaseEv
inline qreal AxisGrid::verticalBase() const
{
    return m_verticalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 68, as _ZNK8AxisGrid14gridVisibilityEv
inline QVector4D AxisGrid::gridVisibility() const
{
    return m_gridVisibility;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 250, as _ZNK8AxisGrid14horizontalBaseEv
inline qreal AxisGrid::horizontalBase() const
{
    return m_horizontalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 159, as _ZNK8AxisGrid16subGridLineWidthEv
inline qreal AxisGrid::subGridLineWidth() const
{
    return m_subGridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 185, as _ZNK8AxisGrid20verticalSubGridScaleEv
inline qreal AxisGrid::verticalSubGridScale() const
{
    return m_verticalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 211, as _ZNK8AxisGrid21isVerticalLogarithmicEv
inline bool AxisGrid::isVerticalLogarithmic() const
{
    return m_isVerticalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 198, as _ZNK8AxisGrid22horizontalSubGridScaleEv
inline qreal AxisGrid::horizontalSubGridScale() const
{
    return m_horizontalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 224, as _ZNK8AxisGrid23isHorizontalLogarithmicEv
inline bool AxisGrid::isHorizontalLogarithmic() const
{
    return m_isHorizontalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 81, as _ZNK8AxisGrid9gridWidthEv
inline qreal AxisGrid::gridWidth() const
{
    return m_gridWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 42, as _ZNK8AxisGrid9smoothingEv
inline qreal AxisGrid::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 782, as _ZNK12AxisRenderer12hasAxisTitleERKNS_14AxisPropertiesE
inline bool AxisRenderer::hasAxisTitle(const AxisProperties &ax) const
{
    return ax.axis && ax.axis->isTitleVisible() && !ax.axis->titleText().isEmpty();
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 787, as _ZNK12AxisRenderer19isAxisBottomOrRightERKNS_14AxisPropertiesE
inline bool AxisRenderer::isAxisBottomOrRight(const AxisProperties &ax) const
{
    return ax.axis->alignment() == Qt::AlignBottom || ax.axis->alignment() == Qt::AlignRight;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 211, as _ZN12AxisRenderer11handleWheelEP11QWheelEvent
inline bool AxisRenderer::handleWheel(QWheelEvent *event)
{
    return zoom(-event->angleDelta().y());
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 216, as _ZN12AxisRenderer16handlePinchScaleEd
inline void AxisRenderer::handlePinchScale(qreal delta)
{
    zoom(delta - 1.0);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 221, as _ZN12AxisRenderer15handlePinchGrabEN15QPointingDevice14GrabTransitionE11QEventPoint
inline void AxisRenderer::handlePinchGrab(QPointingDevice::GrabTransition transition, QEventPoint point)
{
    Q_UNUSED(transition)
    Q_UNUSED(point)
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1425, as _ZN12AxisRenderer16updateAxisTitlesEv
inline void AxisRenderer::updateAxisTitles()
{
    for (auto &&ax : *m_horzAxes) {
        if (!ax.title)
            ax.title = new QQuickText(this);

        if (ax.axis && ax.axis->isTitleVisible()) {
            ax.title->setVAlign(QQuickText::AlignVCenter);
            ax.title->setHAlign(QQuickText::AlignHCenter);
            ax.title->setText(ax.axis->titleText());

            const QRectF &xAxisRect = ax.labelsRect;
            if (ax.axis->alignment() == Qt::AlignTop || ax.axis->alignment() == Qt::AlignLeft)
                ax.title->setY(xAxisRect.y() - ax.title->height() * 0.5 + ax.y);
            else
                ax.title->setY(xAxisRect.y() + xAxisRect.height() - ax.title->height() * 0.5 + ax.y);

            ax.title->setX((2 * xAxisRect.x() - ax.title->width() + xAxisRect.width()) * 0.5 + ax.x);
            if (ax.axis->titleColor().isValid())
                ax.title->setColor(ax.axis->titleColor());
            else
                ax.title->setColor(theme()->labelTextColor());
            ax.title->setFont(ax.axis->titleFont());
            ax.title->setVisible(true);
        } else {
            ax.title->setVisible(false);
        }
    }

    for (auto &&ax : *m_vertAxes) {
        if (!ax.title)
            ax.title = new QQuickText(this);

        if (ax.axis && ax.axis->isTitleVisible()) {
            ax.title->setVAlign(QQuickText::AlignVCenter);
            ax.title->setHAlign(QQuickText::AlignHCenter);
            ax.title->setText(ax.axis->titleText());

            const QRectF &yAxisRect = ax.labelsRect;
            if (ax.axis->alignment() == Qt::AlignRight || ax.axis->alignment() == Qt::AlignBottom)
                ax.title->setX(yAxisRect.x() + yAxisRect.width() - ax.title->width() * 0.5 + ax.x);
            else
                ax.title->setX(yAxisRect.x() - ax.title->width() * 0.5 + ax.x);

            ax.title->setY((2 * yAxisRect.y() - ax.title->height() + yAxisRect.height()) * 0.5
                           + ax.y);
            ax.title->setRotation(-90);
            if (ax.axis->titleColor().isValid())
                ax.title->setColor(ax.axis->titleColor());
            else
                ax.title->setColor(theme()->labelTextColor());
            ax.title->setFont(ax.axis->titleFont());
            ax.title->setVisible(true);
        } else {
            ax.title->setVisible(false);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 2069, as _ZNK12AxisRenderer16formatValueLabelEdiRK7QStringc
inline QString AxisRenderer::formatValueLabel(double number,
                                       int decimals,
                                       const QString &format,
                                       char defaultFormat) const
{
    if (format.length() <= 1) {
        char f = format.isEmpty() ? defaultFormat : format.front().toLatin1();
        return QString::number(number, f, decimals);
    } else {
        return QString::asprintf(format.toLatin1().constData(), number);
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 2058, as _ZN12AxisRenderer17deleteDragHandlerEv
inline void AxisRenderer::deleteDragHandler()
{
    disconnect(m_dragHandler,
               &QQuickDragHandler::translationChanged,
               this,
               &AxisRenderer::onTranslationChanged);
    disconnect(m_dragHandler, &QQuickDragHandler::grabChanged, this, &AxisRenderer::onGrabChanged);
    m_dragHandler->deleteLater();
    m_dragHandler = nullptr;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 227, as _ZN12AxisRenderer20onTranslationChangedE9QVector2D
inline void AxisRenderer::onTranslationChanged(QVector2D delta)
{
    if (!m_dragState.dragging)
        return;

    m_dragState.delta += delta;

    auto hax = (*m_horzAxes)[0].axis;
    auto vax = (*m_vertAxes)[0].axis;

    if (m_graph->zoomAreaEnabled() && m_graph->m_zoomAreaItem) {
        m_graph->m_zoomAreaItem->setVisible(true);

        qreal x = m_dragState.touchPositionAtPress.x();
        if (m_dragState.delta.x() < 0)
            x += m_dragState.delta.x();

        qreal y = m_dragState.touchPositionAtPress.y();
        if (m_dragState.delta.y() < 0)
            y += m_dragState.delta.y();

        qreal width = qAbs(m_dragState.delta.x());
        qreal height = qAbs(m_dragState.delta.y());

        m_graph->m_zoomAreaItem->setX(x);
        m_graph->m_zoomAreaItem->setY(y);
        m_graph->m_zoomAreaItem->setWidth(width);
        m_graph->m_zoomAreaItem->setHeight(height);
    }

    if (m_graph->panStyle() != QGraphsView::PanStyle::Drag)
        return;

    QVector2D change(m_dragState.delta);
    change = windowToAxisCoords(change);
    change.setX(-change.x());

    if (hax->type() == QAbstractAxis::AxisType::Value) {
        auto axis = qobject_cast<QValueAxis *>(hax);
        axis->setPan(m_dragState.panAtPress.x() + change.x());
    } else if (hax->type() == QAbstractAxis::AxisType::DateTime) {
        auto axis = qobject_cast<QDateTimeAxis *>(hax);
        axis->setPan(m_dragState.panAtPress.x() + change.x());
    } else if (hax->type() == QAbstractAxis::AxisType::LogValue) {
        auto axis = qobject_cast<QLogValueAxis *>(hax);
        axis->setPan(m_dragState.panAtPress.x() + change.x());
    }

    if (vax->type() == QAbstractAxis::AxisType::Value) {
        auto axis = qobject_cast<QValueAxis *>(vax);
        axis->setPan(m_dragState.panAtPress.y() + change.y());
    } else if (vax->type() == QAbstractAxis::AxisType::DateTime) {
        auto axis = qobject_cast<QDateTimeAxis *>(vax);
        axis->setPan(m_dragState.panAtPress.y() + change.y());
    } else if (vax->type() == QAbstractAxis::AxisType::LogValue) {
        auto axis = qobject_cast<QLogValueAxis *>(vax);
        axis->setPan(m_dragState.panAtPress.y() + change.y());
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 287, as _ZN12AxisRenderer13onGrabChangedEN15QPointingDevice14GrabTransitionE11QEventPoint
inline void AxisRenderer::onGrabChanged(QPointingDevice::GrabTransition transition, QEventPoint point)
{
    const QPointF position = point.position();

    auto &hax = (*m_horzAxes)[0];
    auto &vax = (*m_vertAxes)[0];
    auto htype = hax.axis->type();
    auto vtype = vax.axis->type();

    if (transition == QPointingDevice::GrabPassive
        && point.pressPosition() == point.position()) {

        m_dragState.dragging = true;
        m_dragState.touchPositionAtPress = QVector2D(position);
        m_dragState.delta = QVector2D(0, 0);

        if (htype == QAbstractAxis::AxisType::Value) {
            auto axis = qobject_cast<QValueAxis *>(hax.axis);
            m_dragState.panAtPress.setX(axis->pan());
        } else if (htype == QAbstractAxis::AxisType::DateTime) {
            auto axis = qobject_cast<QDateTimeAxis *>(hax.axis);
            m_dragState.panAtPress.setX(axis->pan());
        } else if (htype == QAbstractAxis::AxisType::LogValue) {
            auto axis = qobject_cast<QLogValueAxis *>(hax.axis);
            m_dragState.panAtPress.setX(axis->pan());
        }

        if (vtype == QAbstractAxis::AxisType::Value) {
            auto axis = qobject_cast<QValueAxis *>(vax.axis);
            m_dragState.panAtPress.setY(axis->pan());
        } else if (vtype == QAbstractAxis::AxisType::DateTime) {
            auto axis = qobject_cast<QDateTimeAxis *>(vax.axis);
            m_dragState.panAtPress.setY(axis->pan());
        } else if (vtype == QAbstractAxis::AxisType::LogValue) {
            auto axis = qobject_cast<QLogValueAxis *>(vax.axis);
            m_dragState.panAtPress.setY(axis->pan());
        }

    } else if (m_dragState.dragging && transition == QPointingDevice::UngrabExclusive) {
        m_dragState.dragging = false;

        if (!m_graph->zoomAreaEnabled())
            return;

        if (m_graph->m_zoomAreaItem)
            m_graph->m_zoomAreaItem->setVisible(false);

        QVector2D zoomBoxEnd(position);
        auto center = (m_dragState.touchPositionAtPress + zoomBoxEnd) / 2;
        auto size = (m_dragState.touchPositionAtPress - zoomBoxEnd);
        size.setX(qAbs(size.x()));
        size.setY(qAbs(size.y()));

        if (int(size.x()) == 0 || int(size.y()) == 0)
            return;

        size = windowToAxisCoords(size);

        center -= QVector2D(m_graph->m_marginLeft + m_graph->m_y1AxisWidth, m_graph->m_marginTop);
        center = windowToAxisCoords(center);
        center -= QVector2D(hax.valueRange / 2.0f, vax.valueRange / 2.0f);

        if (htype == QAbstractAxis::AxisType::Value) {
            auto axis = qobject_cast<QValueAxis *>(hax.axis);
            axis->setZoom(hax.valueRangeZoomless / size.x());
            axis->setPan(axis->pan() + center.x());
        } else if (htype == QAbstractAxis::AxisType::DateTime){
            auto axis = qobject_cast<QDateTimeAxis *>(hax.axis);
            axis->setZoom(hax.valueRangeZoomless / size.x());
            axis->setPan(axis->pan() + center.x());
        } else if (htype == QAbstractAxis::AxisType::LogValue){
            auto axis = qobject_cast<QLogValueAxis *>(hax.axis);
            axis->setZoom(hax.valueRangeZoomless / size.x());
            axis->setPan(axis->pan() + center.x());
        }

        if (vtype == QAbstractAxis::AxisType::Value) {
            auto axis = qobject_cast<QValueAxis *>(vax.axis);
            axis->setZoom(vax.valueRangeZoomless / size.y());
            axis->setPan(axis->pan() - center.y());
        } else if (vtype == QAbstractAxis::AxisType::DateTime){
            auto axis = qobject_cast<QDateTimeAxis *>(vax.axis);
            axis->setZoom(vax.valueRangeZoomless / size.y());
            axis->setPan(axis->pan() - center.y());
        } else if (vtype == QAbstractAxis::AxisType::LogValue){
            auto axis = qobject_cast<QLogValueAxis *>(vax.axis);
            axis->setZoom(vax.valueRangeZoomless / size.y());
            axis->setPan(axis->pan() - center.y());
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 2083, as _ZNK12AxisRenderer22getValueStepsFromRangeEd
inline double AxisRenderer::getValueStepsFromRange(double range) const
{
    int digits = std::ceil(std::log10(range));
    double r = std::pow(10.0, -digits);
    r *= 10.0;
    double v = std::ceil(range * r) / r;
    double step = v * 0.1;
    // Step must always be bigger than 0
    step = qMax(0.0001, step);
    return step;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 2096, as _ZNK12AxisRenderer25getValueDecimalsFromRangeEd
inline int AxisRenderer::getValueDecimalsFromRange(double range) const
{
    if (range <= 0)
        return 0;
    int decimals = std::ceil(std::log10(10.0 / range));
    // Decimals must always be at least 0
    decimals = qMax(0, decimals);
    return decimals;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1512, as _ZN12AxisRenderer22setLabelTextPropertiesEP10QQuickItemRK7QStringbN10QQuickText10HAlignmentENS5_10VAlignmentEN2Qt13TextElideModeE
inline void AxisRenderer::setLabelTextProperties(QQuickItem *item, const QString &text, bool xAxis,
                                          QQuickText::HAlignment hAlign, QQuickText::VAlignment vAlign,
                                          Qt::TextElideMode elide)
{
    if (auto textItem = qobject_cast<QQuickText *>(item)) {
        // If the component is a Text item (default), then text
        // properties can be set directly.
        textItem->setText(text);
        textItem->setHeight(textItem->contentHeight()); // Default height
        textItem->setHAlign(hAlign);
        textItem->setVAlign(vAlign);
        if (xAxis) {
            textItem->setFont(theme()->axisXLabelFont());
            textItem->setColor(theme()->axisX().labelTextColor());
        } else {
            textItem->setFont(theme()->axisYLabelFont());
            textItem->setColor(theme()->axisY().labelTextColor());
        }

        QQuickText::TextElideMode e;
        switch (elide) {
        case Qt::ElideLeft:
            e = QQuickText::ElideLeft;
            break;
        case Qt::ElideRight:
            e = QQuickText::ElideRight;
            break;
        case Qt::ElideMiddle:
            e = QQuickText::ElideMiddle;
            break;
        default:
            e = QQuickText::ElideNone;
        }
        textItem->setElideMode(e);

    } else {
        // Check for specific dynamic properties
        if (item->property("text").isValid())
            item->setProperty("text", text);
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 126, as _ZN12AxisRenderer18windowToAxisCoordsE9QVector2D
inline QVector2D AxisRenderer::windowToAxisCoords(QVector2D coords)
{
    float x = coords.x();
    float y = coords.y();
    x /= width() - m_graph->m_marginLeft - m_graph->m_marginRight
         - m_y1AxisWidth - m_y2AxisWidth;
    y /= height() - m_graph->m_marginTop - m_graph->m_marginBottom
         - m_x1AxisHeight - m_x2AxisHeight;
    x *= (*m_horzAxes)[0].valueRange;
    y *= (*m_vertAxes)[0].valueRange;
    return QVector2D(x, y);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 139, as _ZN12AxisRenderer13calculateZoomEP13QAbstractAxisd
inline bool AxisRenderer::calculateZoom(QAbstractAxis *axis, qreal delta)
{
    qreal zoom = 1.0;
    std::function<void(qreal zoom)> setZoom;
    switch (axis->type()) {
        case QAbstractAxis::AxisType::Value: {
            auto valueAxis = qobject_cast<QValueAxis *>(axis);
            zoom = valueAxis->zoom();
            setZoom = [valueAxis](qreal zoom) {valueAxis->setZoom(zoom); };
            break;
        }
        case QAbstractAxis::AxisType::DateTime: {
            auto dateTimeAxis = qobject_cast<QDateTimeAxis *>(axis);
            zoom = dateTimeAxis->zoom();
            setZoom = [dateTimeAxis](qreal zoom) {dateTimeAxis->setZoom(zoom); };
            break;
        }
        case QAbstractAxis::AxisType::LogValue: {
            auto logAxis = qobject_cast<QLogValueAxis *>(axis);
            zoom = logAxis->zoom();
            setZoom = [logAxis](qreal zoom) {logAxis->setZoom(zoom); };
            break;
        }
        default: {
            return false;
        }
    }

    qreal change = 0.0;
    if (delta > 0)
        change = zoom * m_graph->m_zoomSensitivity;
    else if (delta < 0)
        change = -zoom * m_graph->m_zoomSensitivity;

    zoom += change;

    if (zoom < 0.01f)
        zoom = 0.01;

    setZoom(zoom);

    return true;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 183, as _ZN12AxisRenderer4zoomEd
inline bool AxisRenderer::zoom(qreal delta)
{
    if (m_graph->zoomStyle() != QGraphsView::ZoomStyle::Center)
        return false;

    bool hzoomed = calculateZoom((*m_horzAxes)[0].axis, delta);
    bool vzoomed = calculateZoom((*m_vertAxes)[0].axis, delta);
    return hzoomed && vzoomed;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 81, as _ZNK12AxisRenderer5themeEv
inline QGraphsTheme *AxisRenderer::theme() const
{
    return m_graph->m_theme;
}
//  -----------------------------------------------------------------------

//  A AxisRenderer that Python can take functions over in. Every AxisRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteAxisRendererCall0)(const void *, int *);
typedef const QRectF * (*CuteAxisRendererCall1)(const void *, int *);
typedef bool (*CuteAxisRendererCall2)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisRendererCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisRendererCall4)(const void *, int *);
typedef void * (*CuteAxisRendererCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisRendererCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteAxisRendererCall8)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteAxisRendererCall9)(const void *, int *);
typedef void (*CuteAxisRendererCall10)(const void *, int *);
typedef void (*CuteAxisRendererCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisRendererCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisRendererCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisRendererCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisRendererCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisRendererCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisRendererCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisRendererCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisRendererCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisRendererCall20)(const void *, int *);
typedef void (*CuteAxisRendererCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisRendererCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisRendererCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisRendererCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisRendererCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisRendererCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisRendererCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisRendererCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisRendererCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisRendererCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisRendererCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteAxisRendererCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteAxisRendererCall33)(const void *, int *);
typedef void (*CuteAxisRendererCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisRendererCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRendererCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisRenderer : public AxisRenderer {
public:
  using AxisRenderer::AxisRenderer;
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
      CuteAxisRendererCall0 call = reinterpret_cast<CuteAxisRendererCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisRendererCall1 call = reinterpret_cast<CuteAxisRendererCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisRendererCall2 call = reinterpret_cast<CuteAxisRendererCall2>(taken[2]);
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
      CuteAxisRendererCall3 call = reinterpret_cast<CuteAxisRendererCall3>(taken[3]);
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
      CuteAxisRendererCall4 call = reinterpret_cast<CuteAxisRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteAxisRendererCall5 call = reinterpret_cast<CuteAxisRendererCall5>(taken[5]);
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
      CuteAxisRendererCall6 call = reinterpret_cast<CuteAxisRendererCall6>(taken[6]);
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
      CuteAxisRendererCall7 call = reinterpret_cast<CuteAxisRendererCall7>(taken[7]);
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
      CuteAxisRendererCall8 call = reinterpret_cast<CuteAxisRendererCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteAxisRendererCall9 call = reinterpret_cast<CuteAxisRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisRendererCall10 call = reinterpret_cast<CuteAxisRendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisRendererCall11 call = reinterpret_cast<CuteAxisRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisRendererCall12 call = reinterpret_cast<CuteAxisRendererCall12>(taken[12]);
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
      CuteAxisRendererCall13 call = reinterpret_cast<CuteAxisRendererCall13>(taken[13]);
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
      CuteAxisRendererCall14 call = reinterpret_cast<CuteAxisRendererCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteAxisRendererCall15 call = reinterpret_cast<CuteAxisRendererCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisRendererCall16 call = reinterpret_cast<CuteAxisRendererCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisRendererCall17 call = reinterpret_cast<CuteAxisRendererCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisRendererCall18 call = reinterpret_cast<CuteAxisRendererCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisRendererCall19 call = reinterpret_cast<CuteAxisRendererCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisRendererCall20 call = reinterpret_cast<CuteAxisRendererCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisRendererCall21 call = reinterpret_cast<CuteAxisRendererCall21>(taken[21]);
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
      CuteAxisRendererCall22 call = reinterpret_cast<CuteAxisRendererCall22>(taken[22]);
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
      CuteAxisRendererCall23 call = reinterpret_cast<CuteAxisRendererCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteAxisRendererCall24 call = reinterpret_cast<CuteAxisRendererCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisRendererCall25 call = reinterpret_cast<CuteAxisRendererCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisRendererCall26 call = reinterpret_cast<CuteAxisRendererCall26>(taken[26]);
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
      CuteAxisRendererCall27 call = reinterpret_cast<CuteAxisRendererCall27>(taken[27]);
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
      CuteAxisRendererCall28 call = reinterpret_cast<CuteAxisRendererCall28>(taken[28]);
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
      CuteAxisRendererCall29 call = reinterpret_cast<CuteAxisRendererCall29>(taken[29]);
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
      CuteAxisRendererCall30 call = reinterpret_cast<CuteAxisRendererCall30>(taken[30]);
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
      CuteAxisRendererCall31 call = reinterpret_cast<CuteAxisRendererCall31>(taken[31]);
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
      CuteAxisRendererCall32 call = reinterpret_cast<CuteAxisRendererCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisRendererCall33 call = reinterpret_cast<CuteAxisRendererCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisRendererCall34 call = reinterpret_cast<CuteAxisRendererCall34>(taken[34]);
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
      CuteAxisRendererCall35 call = reinterpret_cast<CuteAxisRendererCall35>(taken[35]);
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
      CuteAxisRendererCall36 call = reinterpret_cast<CuteAxisRendererCall36>(taken[36]);
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
      CuteAxisRendererCall37 call = reinterpret_cast<CuteAxisRendererCall37>(taken[37]);
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
      CuteAxisRendererCall38 call = reinterpret_cast<CuteAxisRendererCall38>(taken[38]);
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
      CuteAxisRendererCall39 call = reinterpret_cast<CuteAxisRendererCall39>(taken[39]);
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
      CuteAxisRendererCall40 call = reinterpret_cast<CuteAxisRendererCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12AxisRenderer10metaObjectEv(
    const AxisRenderer *self) {
  return self->metaObject();
}

//  bool AxisRenderer::handleWheel(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12AxisRenderer11handleWheelEP11QWheelEvent(
    AxisRenderer *self,
    QWheelEvent *event) {
  return self->handleWheel(event);
}

//  void AxisRenderer::handlePinchScale(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer16handlePinchScaleEd(
    AxisRenderer *self,
    qreal delta) {
  self->handlePinchScale(delta);
}

//  void AxisRenderer::handlePinchGrab(QPointingDevice::GrabTransition
//      transition, QEventPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer15handlePinchGrabEN15QPointingDevice14GrabTransitionE11QEventPoint(
    AxisRenderer *self,
    QPointingDevice::GrabTransition transition,
    const QEventPoint *point) {
  self->handlePinchGrab(transition, *point);
}

//  void AxisRenderer::updateAxisTitles()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer16updateAxisTitlesEv(AxisRenderer *self) {
  self->updateAxisTitles();
}

//  QString AxisRenderer::formatValueLabel(double number, int decimals, const
//      QString &format, char defaultFormat) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12AxisRenderer16formatValueLabelEdiRK7QStringc(
    const AxisRenderer *self,
    double number,
    int decimals,
    const QString *format,
    char defaultFormat) {
  return new QString(
      self->formatValueLabel(
          number,
          decimals,
          *format,
          defaultFormat));
}

//  void AxisRenderer::deleteDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer17deleteDragHandlerEv(AxisRenderer *self) {
  self->deleteDragHandler();
}

//  void AxisRenderer::onTranslationChanged(QVector2D delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer20onTranslationChangedE9QVector2D(
    AxisRenderer *self,
    const QVector2D *delta) {
  self->onTranslationChanged(*delta);
}

//  void AxisRenderer::onGrabChanged(QPointingDevice::GrabTransition
//      transition, QEventPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer13onGrabChangedEN15QPointingDevice14GrabTransitionE11QEventPoint(
    AxisRenderer *self,
    QPointingDevice::GrabTransition transition,
    const QEventPoint *point) {
  self->onGrabChanged(transition, *point);
}

//  double AxisRenderer::getValueStepsFromRange(double range) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12AxisRenderer22getValueStepsFromRangeEd(
    const AxisRenderer *self,
    double range) {
  return self->getValueStepsFromRange(range);
}

//  int AxisRenderer::getValueDecimalsFromRange(double range) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12AxisRenderer25getValueDecimalsFromRangeEd(
    const AxisRenderer *self,
    double range) {
  return self->getValueDecimalsFromRange(range);
}

//  void AxisRenderer::setLabelTextProperties(QQuickItem *item, const QString
//      &text, bool xAxis, QQuickText::HAlignment hAlign,
//      QQuickText::VAlignment vAlign, Qt::TextElideMode elide)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer22setLabelTextPropertiesEP10QQuickItemRK7QStringbN10QQuickText10HAlignmentENS5_10VAlignmentEN2Qt13TextElideModeE(
    AxisRenderer *self,
    QQuickItem *item,
    const QString *text,
    bool xAxis,
    QQuickText::HAlignment hAlign,
    QQuickText::VAlignment vAlign,
    Qt::TextElideMode elide) {
  self->setLabelTextProperties(item, *text, xAxis, hAlign, vAlign, elide);
}

//  QVector2D AxisRenderer::windowToAxisCoords(QVector2D coords)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN12AxisRenderer18windowToAxisCoordsE9QVector2D(
    AxisRenderer *self,
    const QVector2D *coords) {
  return new QVector2D(self->windowToAxisCoords(*coords));
}

//  bool AxisRenderer::calculateZoom(QAbstractAxis *axis, qreal delta)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12AxisRenderer13calculateZoomEP13QAbstractAxisd(
    AxisRenderer *self,
    QAbstractAxis *axis,
    qreal delta) {
  return self->calculateZoom(axis, delta);
}

//  bool AxisRenderer::zoom(qreal delta)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12AxisRenderer4zoomEd(AxisRenderer *self, qreal delta) {
  return self->zoom(delta);
}

//  QGraphsTheme *AxisRenderer::theme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZNK12AxisRenderer5themeEv(const AxisRenderer *self) {
  return self->theme();
}

//  a Python function taken by a CuteAxisRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisRenderer(
    AxisRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteAxisRenderer *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
