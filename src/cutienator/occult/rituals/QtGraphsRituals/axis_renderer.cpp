//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisrenderer_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-26: moc's output for 'AxisRenderer' is pasted in, cut
//  from what the moc of Qt 6.12.0 writes for its header: Qt's library keeps
//  it to itself; added are 9 rituals that lean on what moc writes for a
//  class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Edited by hand on 2026-11-27: the copy of
//  AxisTicker's constructor taken from Qt is taken out (1): under
//  Microsoft's ABI it had this file write AxisTicker's whole table of
//  virtual functions, each of which only the ritual file of AxisTicker
//  carries; that file now carries the constructor alone. Kept as it is when
//  the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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
#include <QtCore/qloggingcategory.h>
#include <QtGraphs/private/axisticker_p.h>
#include <QtGraphs/private/axisgrid_p.h>
#include <QtGraphs/private/axisline_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__AxisRenderer.cpp, line 1, as moc:AxisRenderer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN12AxisRendererE_t {};
} // unnamed namespace

template <> constexpr inline auto AxisRenderer::qt_create_metaobjectdata<qt_meta_tag_ZN12AxisRendererE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AxisRenderer"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AxisRenderer, qt_meta_tag_ZN12AxisRendererE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AxisRenderer::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AxisRendererE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AxisRendererE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN12AxisRendererE_t>.metaTypes,
    nullptr
} };

void AxisRenderer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AxisRenderer *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *AxisRenderer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AxisRenderer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AxisRendererE_t>.strings))
        return static_cast<void*>(this);
    return QQuickItem::qt_metacast(_clname);
}

int AxisRenderer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickItem::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 79, as _ZN12AxisRendererD0Ev
inline AxisRenderer::~AxisRenderer() {}

//  from ../qtgraphs/src/graphs2d/qgraphsview.cpp, line 108, as _Z10lcGraphs2Dv
inline const QLoggingCategory &lcGraphs2D()
{
    static const QLoggingCategory category("qt.graphs2d.general");
    return category;
}

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

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 67, as _ZN12AxisRendererC1EP10QQuickItem
inline AxisRenderer::AxisRenderer(QQuickItem *parent)
    : QQuickItem(parent)
{
    m_graph = qobject_cast<QGraphsView *>(parent);
    setFlag(QQuickItem::ItemHasContents);
    if (m_axes1.empty())
        m_axes1.emplace_back();

    if (m_axes2.empty())
        m_axes2.emplace_back();
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 86, as _ZN12AxisRenderer10initializeEv
inline void AxisRenderer::initialize()
{
    if (m_initialized) {
        return;
    }
    if (!window()) {
        qCDebug(lcGraphs2D, "window doesn't exist.");
        return;
    }

    if (m_axisGrid)
        m_axisGrid->componentComplete();
    if (m_axisGridShadow)
        m_axisGridShadow->componentComplete();

    for (auto&& ax : *m_horzAxes) {
        if (ax.line)
            ax.line->componentComplete();
        if (ax.ticker)
            ax.ticker->componentComplete();
        if (ax.lineShadow)
            ax.lineShadow->componentComplete();
        if (ax.tickerShadow)
            ax.tickerShadow->componentComplete();
    }

    for (auto&& ax : *m_vertAxes) {
        if (ax.line)
            ax.line->componentComplete();
        if (ax.ticker)
            ax.ticker->componentComplete();
        if (ax.lineShadow)
            ax.lineShadow->componentComplete();
        if (ax.tickerShadow)
            ax.tickerShadow->componentComplete();
    }

    m_initialized = true;
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

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 394, as _ZN12AxisRenderer17populateAxisItemsEv
inline void AxisRenderer::populateAxisItems()
{
    // See if series is horizontal, so axis should also switch places.
    bool vertical = true;
    if (m_graph->orientation() == Qt::Orientation::Horizontal)
        vertical = false;

    if (vertical) {
        m_horzAxes = &m_axes1;
        m_vertAxes = &m_axes2;
    } else {
        m_horzAxes = &m_axes2;
        m_vertAxes = &m_axes1;
    }

    if (vertical != m_wasVertical) {
        // Orientation has changed, so clear possible custom elements
        for (auto&& ax : m_axes1) {
            if (ax.title)
                ax.title->deleteLater();
            if (ax.line)
                ax.line->deleteLater();
            if (ax.ticker)
                ax.ticker->deleteLater();
            if (ax.lineShadow)
                ax.lineShadow->deleteLater();
            if (ax.tickerShadow)
                ax.tickerShadow->deleteLater();
            for (auto&& item : ax.textItems)
                item->deleteLater();
        }

        for (auto&& ax : m_axes2) {
            if (ax.title)
                ax.title->deleteLater();
            if (ax.line)
                ax.line->deleteLater();
            if (ax.ticker)
                ax.ticker->deleteLater();
            if (ax.lineShadow)
                ax.lineShadow->deleteLater();
            if (ax.tickerShadow)
                ax.tickerShadow->deleteLater();
            for (auto&& item : ax.textItems)
                item->deleteLater();
        }

        m_axes1.clear();
        m_axes2.clear();

        m_wasVertical = vertical;
    }

    if (m_axes1.empty())
        m_axes1.emplace_back();

    if (m_axes2.empty())
        m_axes2.emplace_back();

    m_axes1[0].axis = m_graph->axisX();
    m_axes2[0].axis = m_graph->axisY();

    for (auto&& s : m_graph->m_seriesList) {
        if (auto series = qobject_cast<QAbstractSeries *>(s)) {
            if (series->axisX() && series->axisX() != m_graph->axisX()) {
                bool contains = false;
                for (auto&& ax : m_axes1) {
                    if (ax.axis == series->axisX()) {
                        contains = true;
                        break;
                    }
                }

                if (!contains) {
                    auto &ax = m_axes1.emplace_back();
                    ax.axis = series->axisX();
                }
            }

            if (series->axisY() && series->axisY() != m_graph->axisY()) {
                bool contains = false;
                for (auto&& ax : m_axes2) {
                    if (ax.axis == series->axisY()) {
                        contains = true;
                        break;
                    }
                }

                if (!contains) {
                    auto &ax = m_axes2.emplace_back();
                    ax.axis = series->axisY();
                }
            }
        }
    }

    if (!m_axisGrid) {
        m_axisGrid = new AxisGrid(this);
        m_axisGrid->setZ(-1);
        m_axisGrid->setupShaders();
        m_axisGrid->setOrigo(0);
    }
    if (!m_axisGridShadow) {
        m_axisGridShadow = new AxisGrid(this);
        m_axisGridShadow->setZ(-3);
        m_axisGridShadow->setupShaders();
        m_axisGridShadow->setOrigo(0);
    }

    for (int i = 1; i < m_axes1.size(); i++) {
        auto& ax = m_axes1[i];

        bool used = false;

        for (auto&& s : m_graph->m_seriesList) {
            if (auto series = qobject_cast<QAbstractSeries *>(s)) {
                if (series->axisX() && series->axisX() == ax.axis) {
                    used = true;
                    break;
                }
            }
        }

        if (!used) {
            if (ax.title)
                ax.title->deleteLater();
            if (ax.line)
                ax.line->deleteLater();
            if (ax.ticker)
                ax.ticker->deleteLater();
            if (ax.lineShadow)
                ax.lineShadow->deleteLater();
            if (ax.tickerShadow)
                ax.tickerShadow->deleteLater();
            for (auto&& item : ax.textItems)
                item->deleteLater();
            m_axes1.removeAt(i);
            i--;
            continue;
        }
    }

    for (int i = 1; i < m_axes2.size(); i++) {
        auto& ax = m_axes2[i];

        bool used = false;

        for (auto&& s : m_graph->m_seriesList) {
            if (auto series = qobject_cast<QAbstractSeries *>(s)) {
                if (series->axisY() && series->axisY() == ax.axis) {
                    used = true;
                    break;
                }
            }
        }

        if (!used) {
            if (ax.title)
                ax.title->deleteLater();
            if (ax.line)
                ax.line->deleteLater();
            if (ax.ticker)
                ax.ticker->deleteLater();
            if (ax.lineShadow)
                ax.lineShadow->deleteLater();
            if (ax.tickerShadow)
                ax.tickerShadow->deleteLater();
            for (auto&& item : ax.textItems)
                item->deleteLater();
            m_axes2.removeAt(i);
            i--;
            continue;
        }
    }

    for (int i = 0; i < m_vertAxes->size(); i++) {
        auto& ax = (*m_vertAxes)[i];

        if (!ax.line) {
            ax.line = new AxisLine(this);
            ax.line->setZ(-1);
            ax.line->setupShaders();
        }
        if (!ax.ticker) {
            ax.ticker = new AxisTicker(this);
            ax.ticker->setZ(-2);
            ax.ticker->setOrigo(0);
            // TODO: Configurable in theme or axis?
            ax.ticker->setSubTickLength(0.5);
            ax.ticker->setupShaders();
        }
        if (!ax.lineShadow) {
            ax.lineShadow = new AxisLine(this);
            ax.lineShadow->setZ(-3);
            ax.lineShadow->setupShaders();
        }
        if (!ax.tickerShadow) {
            ax.tickerShadow = new AxisTicker(this);
            ax.tickerShadow->setZ(-3);
            ax.tickerShadow->setOrigo(0);
            // TODO: Configurable in theme or axis?
            ax.tickerShadow->setSubTickLength(ax.ticker->subTickLength());
            ax.tickerShadow->setupShaders();
        }
    }

    for (int i = 0; i < m_horzAxes->size(); i++) {
        auto& ax = (*m_horzAxes)[i];

        if (!ax.line) {
            ax.line = new AxisLine(this);
            ax.line->setZ(-1);
            ax.line->setIsHorizontal(true);
            ax.line->setupShaders();
        }
        if (!ax.ticker) {
            ax.ticker = new AxisTicker(this);
            ax.ticker->setZ(-2);
            ax.ticker->setIsHorizontal(true);
            ax.ticker->setOrigo(0);
            // TODO: Configurable in theme or axis?
            ax.ticker->setSubTickLength(0.2);
            ax.ticker->setupShaders();
        }
        if (!ax.lineShadow) {
            ax.lineShadow = new AxisLine(this);
            ax.lineShadow->setZ(-3);
            ax.lineShadow->setupShaders();
        }
        if (!ax.tickerShadow) {
            ax.tickerShadow = new AxisTicker(this);
            ax.tickerShadow->setZ(-3);
            ax.tickerShadow->setIsHorizontal(true);
            ax.tickerShadow->setOrigo(0);
            // TODO: Configurable in theme or axis?
            ax.tickerShadow->setSubTickLength(ax.ticker->subTickLength());
            ax.tickerShadow->setupShaders();
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1132, as _ZN12AxisRenderer17updateAxisTickersEv
inline void AxisRenderer::updateAxisTickers()
{
    for (auto&& ax : *m_vertAxes) {
        if (ax.axis) {
            QRectF yAxisRect = ax.tickersRect;

            // Note: Fix before enabling, see QTBUG-121207 and QTBUG-121211
            //if (theme()->themeDirty()) {
            if (ax.axis->subColor().isValid())
                ax.ticker->setSubTickColor(ax.axis->subColor());
            else
                ax.ticker->setSubTickColor(theme()->axisY().subColor());
            if (ax.axis->color().isValid())
                ax.ticker->setTickColor(ax.axis->color());
            else
                ax.ticker->setTickColor(theme()->axisY().mainColor());
            ax.ticker->setTickLineWidth(theme()->axisY().mainWidth());
            ax.ticker->setSubTickLineWidth(theme()->axisY().subWidth());
            ax.ticker->setSmoothing(m_graph->axisYSmoothing());
            //}

                float topPadding = m_axisGrid->gridLineWidth() * 0.5;
                float bottomPadding = topPadding;
                // TODO Only when changed
                ax.ticker->setDisplacement(ax.displacement);
                QRectF &rect = yAxisRect;
                ax.ticker->setX(rect.x() + ax.x);
                ax.ticker->setY(rect.y() + ax.y);
                ax.ticker->setWidth(rect.width());
                ax.ticker->setHeight(rect.height());
                ax.ticker->setFlipped(ax.axis->alignment() == Qt::AlignRight || ax.axis->alignment() == Qt::AlignBottom);

                ax.ticker->setSpacing((ax.ticker->height() - topPadding - bottomPadding)
                                       / (ax.valueRange / ax.valueStep));
                ax.ticker->setSubTicksVisible(!qFuzzyCompare(ax.subGridScale, 1.0));
                ax.ticker->setSubTickScale(ax.subGridScale);

                ax.ticker->setLogarithmic(ax.isLogarithmic);
                ax.ticker->setBase(ax.logBase);

                ax.ticker->setVisible(ax.axis->isVisible());

                // Axis line
                if (ax.axis->color().isValid())
                    ax.line->setColor(ax.axis->color());
                else
                    ax.line->setColor(theme()->axisY().mainColor());
                ax.line->setLineWidth(theme()->axisY().mainWidth());
                ax.line->setSmoothing(m_graph->axisYSmoothing());

                float xMovement = 0.5 * (ax.line->lineWidth() + ax.line->smoothing());
                if (ax.axis->alignment() == Qt::AlignRight || ax.axis->alignment() == Qt::AlignBottom)
                    ax.line->setX(ax.ticker->x() - xMovement);
                else
                    ax.line->setX(ax.ticker->x() + ax.ticker->width() - xMovement);
                ax.line->setY(ax.ticker->y());
                ax.line->setWidth(ax.line->lineWidth() + ax.line->smoothing());
                ax.line->setHeight(ax.ticker->height());
                ax.line->setVisible(ax.axis->isLineVisible());
        } else {
            // Hide all parts of vertical axis
            ax.ticker->setVisible(false);
            ax.line->setVisible(false);
            for (auto &textItem : ax.textItems)
                textItem->setVisible(false);
        }
    }

    for (auto&& ax : *m_horzAxes) {
        if (ax.axis) {
            QRectF xAxisRect = ax.tickersRect;

            //if (theme()->themeDirty()) {
            if (ax.axis->subColor().isValid())
                ax.ticker->setSubTickColor(ax.axis->subColor());
            else
                ax.ticker->setSubTickColor(theme()->axisX().subColor());
            if (ax.axis->color().isValid())
                ax.ticker->setTickColor(ax.axis->color());
            else
                ax.ticker->setTickColor(theme()->axisX().mainColor());
            ax.ticker->setTickLineWidth(theme()->axisX().mainWidth());
            ax.ticker->setSubTickLineWidth(theme()->axisX().subWidth());
            ax.ticker->setSmoothing(m_graph->axisXSmoothing());
            //}

            float leftPadding = m_axisGrid->gridLineWidth() * 0.5;
            float rightPadding = leftPadding;
            // TODO Only when changed
            ax.ticker->setDisplacement(ax.displacement);
            QRectF &rect = xAxisRect;
            ax.ticker->setX(rect.x() + ax.x);
            ax.ticker->setY(rect.y() + ax.y);
            ax.ticker->setWidth(rect.width());
            ax.ticker->setHeight(rect.height());
            ax.ticker->setFlipped(ax.axis->alignment() == Qt::AlignTop || ax.axis->alignment() == Qt::AlignLeft);

            ax.ticker->setSpacing((ax.ticker->width() - leftPadding - rightPadding)
                                             / (ax.valueRange / ax.valueStep));
            ax.ticker->setSubTicksVisible(!qFuzzyCompare(ax.subGridScale, 1.0));
            ax.ticker->setSubTickScale(ax.subGridScale);

            ax.ticker->setLogarithmic(ax.isLogarithmic);
            ax.ticker->setBase(ax.logBase);

            ax.ticker->setVisible(ax.axis->isVisible());
            // Axis line
            if (ax.axis->color().isValid())
                ax.line->setColor(ax.axis->color());
            else
                ax.line->setColor(theme()->axisX().mainColor());
            ax.line->setLineWidth(theme()->axisX().mainWidth());
            ax.line->setSmoothing(m_graph->axisXSmoothing());
            ax.line->setX(ax.ticker->x());
            float yMovement = 0.5 * (ax.line->lineWidth() + ax.line->smoothing());
            if (ax.axis->alignment() == Qt::AlignTop || ax.axis->alignment() == Qt::AlignLeft)
                ax.line->setY(ax.ticker->y() + ax.ticker->height() - yMovement);
            else
                ax.line->setY(ax.ticker->y() - yMovement);
            ax.line->setWidth(ax.ticker->width());
            ax.line->setHeight(ax.line->lineWidth() + ax.line->smoothing());
            ax.line->setVisible(ax.axis->isLineVisible());
        } else {
            // Hide all parts of horizontal axis
            ax.ticker->setVisible(false);
            ax.line->setVisible(false);
            for (auto &textItem : ax.textItems)
                textItem->setVisible(false);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1264, as _ZN12AxisRenderer23updateAxisTickersShadowEv
inline void AxisRenderer::updateAxisTickersShadow()
{
    for (auto&& ax : *m_vertAxes) {
        if (ax.axis && m_graph->isShadowVisible()) {
            ax.tickerShadow->setSubTickColor(m_graph->shadowColor());
            ax.tickerShadow->setTickColor(m_graph->shadowColor());
            ax.tickerShadow->setSubTickLineWidth(ax.ticker->subTickLineWidth()
                                                  + m_graph->shadowBarWidth());
            ax.tickerShadow->setTickLineWidth(ax.ticker->tickLineWidth()
                                               + m_graph->shadowBarWidth());
            ax.tickerShadow->setSmoothing(ax.ticker->smoothing() + m_graph->shadowSmoothing());

            // TODO Only when changed
            ax.tickerShadow->setDisplacement(ax.ticker->displacement());
            ax.tickerShadow->setX(ax.ticker->x() + m_graph->shadowXOffset());
            ax.tickerShadow->setY(ax.ticker->y() + m_graph->shadowYOffset()
                                   + m_graph->shadowBarWidth() * 0.5);
            ax.tickerShadow->setWidth(ax.ticker->width());
            ax.tickerShadow->setHeight(ax.ticker->height());
            ax.tickerShadow->setFlipped(ax.ticker->isFlipped());
            ax.tickerShadow->setSpacing(ax.ticker->spacing());
            ax.tickerShadow->setSubTicksVisible(ax.ticker->subTicksVisible());
            ax.tickerShadow->setSubTickScale(ax.ticker->subTickScale());

            ax.tickerShadow->setLogarithmic(ax.ticker->isLogarithmic());
            ax.tickerShadow->setBase(ax.ticker->base());

            ax.tickerShadow->setVisible(ax.ticker->isVisible());
            // Axis line
            ax.lineShadow->setColor(m_graph->shadowColor());
            ax.lineShadow->setLineWidth(ax.line->lineWidth() + m_graph->shadowBarWidth());
            ax.lineShadow->setSmoothing(ax.line->smoothing() + m_graph->shadowSmoothing());
            ax.lineShadow->setX(ax.line->x() + m_graph->shadowXOffset());
            ax.lineShadow->setY(ax.line->y() + m_graph->shadowYOffset()
                                 + m_graph->shadowBarWidth() * 0.5);
            ax.lineShadow->setWidth(ax.line->width());
            ax.lineShadow->setHeight(ax.line->height());
            ax.lineShadow->setVisible(ax.line->isVisible());
        } else {
            // Hide all parts of vertical axis
            ax.tickerShadow->setVisible(false);
            ax.lineShadow->setVisible(false);
        }
    }

    for (auto&& ax : *m_horzAxes) {
        if (ax.axis && m_graph->isShadowVisible()) {
            ax.tickerShadow->setSubTickColor(m_graph->shadowColor());
            ax.tickerShadow->setTickColor(m_graph->shadowColor());
            ax.tickerShadow->setSubTickLineWidth(ax.ticker->subTickLineWidth()
                                                  + m_graph->shadowBarWidth());
            ax.tickerShadow->setTickLineWidth(ax.ticker->tickLineWidth()
                                               + m_graph->shadowBarWidth());
            ax.tickerShadow->setSmoothing(ax.ticker->smoothing() + m_graph->shadowSmoothing());

            // TODO Only when changed
            ax.tickerShadow->setDisplacement(ax.ticker->displacement());
            ax.tickerShadow->setX(ax.ticker->x() + m_graph->shadowXOffset()
                                   - m_graph->shadowBarWidth() * 0.5);
            ax.tickerShadow->setY(ax.ticker->y() + m_graph->shadowYOffset());
            ax.tickerShadow->setWidth(ax.ticker->width());
            ax.tickerShadow->setHeight(ax.ticker->height());
            ax.tickerShadow->setFlipped(ax.ticker->isFlipped());
            ax.tickerShadow->setSpacing(ax.ticker->spacing());
            ax.tickerShadow->setSubTicksVisible(ax.ticker->subTicksVisible());
            ax.tickerShadow->setSubTickScale(ax.ticker->subTickScale());
            ax.tickerShadow->setVisible(ax.ticker->isVisible());
            // Axis line
            ax.lineShadow->setColor(m_graph->shadowColor());
            ax.lineShadow->setLineWidth(ax.line->width() + m_graph->shadowBarWidth());
            ax.lineShadow->setSmoothing(ax.line->smoothing() + m_graph->shadowSmoothing());
            ax.lineShadow->setX(ax.line->x() + m_graph->shadowXOffset()
                                 - m_graph->shadowBarWidth() * 0.5);
            ax.lineShadow->setY(ax.line->y() + m_graph->shadowYOffset());
            ax.lineShadow->setWidth(ax.line->width());
            ax.lineShadow->setHeight(ax.line->height());
            ax.lineShadow->setVisible(ax.line->isVisible());
        } else {
            // Hide all parts of horizontal axis
            ax.tickerShadow->setVisible(false);
            ax.lineShadow->setVisible(false);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1349, as _ZN12AxisRenderer14updateAxisGridEv
inline void AxisRenderer::updateAxisGrid()
{
    auto &hax = (*m_horzAxes)[0];
    auto &vax = (*m_vertAxes)[0];

    m_axisGrid->setGridColor(theme()->grid().mainColor());
    m_axisGrid->setSubGridColor(theme()->grid().subColor());
    m_axisGrid->setSubGridLineWidth(theme()->grid().subWidth());
    m_axisGrid->setGridLineWidth(theme()->grid().mainWidth());
    const double minimumSmoothing = 0.05;
    m_axisGrid->setSmoothing(m_graph->gridSmoothing() + minimumSmoothing);
    if (theme()->isPlotAreaBackgroundVisible())
        m_axisGrid->setPlotAreaBackgroundColor(theme()->plotAreaBackgroundColor());
    else
        m_axisGrid->setPlotAreaBackgroundColor(QColorConstants::Transparent);

    float topPadding = m_axisGrid->gridLineWidth() * 0.5;
    float bottomPadding = topPadding;
    float leftPadding = topPadding;
    float rightPadding = topPadding;
    // TODO Only when changed
    m_axisGrid->setGridMovement(QPointF(hax.displacement, vax.displacement));
    QRectF rect = m_graph->m_plotArea;
    m_axisGrid->setX(rect.x());
    m_axisGrid->setY(rect.y());
    m_axisGrid->setWidth(rect.width());
    m_axisGrid->setHeight(rect.height());

    m_axisGrid->setGridWidth((m_axisGrid->width() - leftPadding - rightPadding)
                             / (hax.valueRange / hax.valueStep));
    m_axisGrid->setGridHeight((m_axisGrid->height() - topPadding - bottomPadding)
                              / (vax.valueRange / vax.valueStep));
    m_axisGrid->setGridVisibility(QVector4D(m_gridHorizontalLinesVisible,
                                            m_gridVerticalLinesVisible,
                                            m_gridHorizontalSubLinesVisible,
                                            m_gridVerticalSubLinesVisible));
    m_axisGrid->setVerticalSubGridScale(vax.subGridScale);
    m_axisGrid->setHorizontalSubGridScale(hax.subGridScale);

    m_axisGrid->setVerticalLogarithmic(vax.isLogarithmic);
    m_axisGrid->setHorizontalLogarithmic(hax.isLogarithmic);
    m_axisGrid->setVerticalBase(vax.logBase);
    m_axisGrid->setHorizontalBase(hax.logBase);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 1394, as _ZN12AxisRenderer20updateAxisGridShadowEv
inline void AxisRenderer::updateAxisGridShadow()
{
    if (m_graph->isShadowVisible()) {
        m_axisGridShadow->setGridColor(m_graph->shadowColor());
        m_axisGridShadow->setSubGridColor(m_graph->shadowColor());
        m_axisGridShadow->setSubGridLineWidth(m_axisGrid->subGridLineWidth() + m_graph->shadowBarWidth());
        m_axisGridShadow->setGridLineWidth(m_axisGrid->gridLineWidth() + m_graph->shadowBarWidth());
        m_axisGridShadow->setSmoothing(m_axisGrid->smoothing() + m_graph->shadowSmoothing());

        // TODO Only when changed
        m_axisGridShadow->setGridMovement(m_axisGrid->gridMovement());
        m_axisGridShadow->setX(m_axisGrid->x() + m_graph->shadowXOffset() - m_graph->shadowBarWidth() * 0.5);
        m_axisGridShadow->setY(m_axisGrid->y() + m_graph->shadowYOffset() + m_graph->shadowBarWidth() * 0.5);
        m_axisGridShadow->setWidth(m_axisGrid->width());
        m_axisGridShadow->setHeight(m_axisGrid->height());
        m_axisGridShadow->setGridWidth(m_axisGrid->gridWidth());
        m_axisGridShadow->setGridHeight(m_axisGrid->gridHeight());
        m_axisGridShadow->setGridVisibility(m_axisGrid->gridVisibility());
        m_axisGridShadow->setVerticalSubGridScale(m_axisGrid->verticalSubGridScale());
        m_axisGridShadow->setHorizontalSubGridScale(m_axisGrid->horizontalSubGridScale());
        m_axisGridShadow->setVisible(true);

        m_axisGridShadow->setVerticalLogarithmic(m_axisGrid->isVerticalLogarithmic());
        m_axisGridShadow->setHorizontalLogarithmic(m_axisGrid->isHorizontalLogarithmic());
        m_axisGridShadow->setVerticalBase(m_axisGrid->verticalBase());
        m_axisGridShadow->setHorizontalBase(m_axisGrid->horizontalBase());
    } else {
        m_axisGridShadow->setVisible(false);
    }
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

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 792, as _ZN12AxisRenderer22updateAxisMeasurementsEv
inline void AxisRenderer::updateAxisMeasurements()
{
    populateAxisItems();

    if (!theme())
        return;

    const QFontMetricsF yFontMetrics(theme()->axisYLabelFont());

    for (auto &ax : *m_vertAxes)
        ax.labelSize = 0;

    for (auto &ax : *m_vertAxes) {
        if (auto vaxis = qobject_cast<QValueAxis *>(ax.axis)) {
            double step = vaxis->tickInterval();

            qreal diff = vaxis->max() - vaxis->min();
            qreal center = diff / 2.0f + vaxis->min() + vaxis->pan();

            diff /= vaxis->zoom();

            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;

            ax.valueRange = ax.maxValue - ax.minValue;
            ax.valueRangeZoomless = vaxis->max() - vaxis->min();

            // If step is not manually defined (or it is invalid), calculate autostep
            if (step <= 0)
                step = getValueStepsFromRange(vaxis->max() - vaxis->min());

            // Get smallest tick label value
            double minLabel = vaxis->tickAnchor();
            while (minLabel < ax.minValue)
                minLabel += step;
            while (minLabel >= (ax.minValue + step))
                minLabel -= step;
            ax.minLabel = minLabel;

            ax.valueStep = step;
            int axisVerticalSubTickCount = vaxis->subTickCount();
            ax.subGridScale = axisVerticalSubTickCount > 0 ? 1.0 / (axisVerticalSubTickCount + 1)
                                                            : 1.0;
            double axisVerticalValueDiff = ax.minLabel - ax.minValue;
            ax.displacement = -(axisVerticalValueDiff / ax.valueStep) * ax.stepPx;

            int decimals = vaxis->labelDecimals();
            if (decimals < 0)
                decimals = getValueDecimalsFromRange(ax.valueRange);

            const QString format = vaxis->labelFormat();
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    formatValueLabel(vaxis->min(), decimals, format)));
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    formatValueLabel(vaxis->max(), decimals, format)));
        } else if (auto vaxis = qobject_cast<QDateTimeAxis *>(ax.axis)) {
            // Todo: make constant for all axis, or clamp in class? (QTBUG-124736)
            const double MAX_DIVS = 100.0;

            double tickCount = std::clamp<double>(vaxis->tickCount(), 0.0, MAX_DIVS);
            qreal diff = vaxis->max().toMSecsSinceEpoch() - vaxis->min().toMSecsSinceEpoch();
            qreal center = diff / 2.0f + vaxis->min().toMSecsSinceEpoch() + vaxis->pan();

            diff /= vaxis->zoom();
            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;
            ax.valueRange = std::abs(ax.maxValue - ax.minValue);
            ax.valueRangeZoomless = vaxis->max().toMSecsSinceEpoch()
                                    - vaxis->min().toMSecsSinceEpoch();

            // in ms
            double segment;
            if (tickCount <= 0) {
                segment = getValueStepsFromRange(ax.valueRange);
                tickCount = ax.valueRange / segment;
            } else {
                segment = ax.valueRange / tickCount;
            }

            ax.minLabel = std::clamp(tickCount, 1.0, MAX_DIVS);

            ax.valueStep = segment;
            int axisVerticalSubTickCount = vaxis->subTickCount();
            ax.subGridScale = axisVerticalSubTickCount > 0 ? 1.0 / (axisVerticalSubTickCount + 1)
                                                           : 1.0;
            ax.tickCount = tickCount;
            double axisVerticalValueDiff = fmod(ax.minValue, ax.valueStep) / ax.valueStep;
            ax.displacement = axisVerticalValueDiff * ax.stepPx;

            const QString format = vaxis->labelFormat();
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    vaxis->min().toString(format)));
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    vaxis->max().toString(format)));
        } else if (auto vaxis = qobject_cast<QLogValueAxis *>(ax.axis)) {
            ax.isLogarithmic = true;
            ax.logBase = vaxis->base();

            qreal logBase = log(vaxis->base());
            qreal logMin = log(vaxis->min()) / logBase;
            qreal logMax = log(vaxis->max()) / logBase;

            qreal diff = logMax - logMin;
            qreal center = diff / 2.0f + logMin + vaxis->pan();

            diff /= vaxis->zoom();

            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;

            //use log scale to create value range
            ax.valueRange = ax.maxValue - ax.minValue;
            ax.valueRangeZoomless = logMax - logMin;

            // Get smallest tick label value
            ax.minLabel = qRound(ax.minValue);
            ax.valueStep = 1;

            int axisVerticalSubTickCount = vaxis->subTickCount();
            if (axisVerticalSubTickCount == -1)
                axisVerticalSubTickCount = int(qRound(vaxis->base()));
            ax.subGridScale = axisVerticalSubTickCount > 0 ? 1.0 / (axisVerticalSubTickCount + 1)
                                                           : 1.0;
            double axisVerticalValueDiff = ax.minLabel - ax.minValue;
            ax.displacement = -(axisVerticalValueDiff / ax.valueStep) * ax.stepPx;

            const QString format = vaxis->labelFormat();
            int precision = vaxis->labelPrecision();
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    formatValueLabel(vaxis->min(), precision, format, 'g')));
            ax.labelSize = qMax(ax.labelSize,
                                yFontMetrics.horizontalAdvance(
                                    formatValueLabel(vaxis->max(), precision, format, 'g')));
        }
#if QT_CONFIG(graphs_2d_bar)
        else if (auto vaxis = qobject_cast<QBarCategoryAxis *>(ax.axis)) {
            ax.maxValue = vaxis->categories().size();
            ax.minValue = 0;
            ax.valueRange = ax.maxValue - ax.minValue;

            for (const auto &category : vaxis->categories()) {
                ax.labelSize = qMax(ax.labelSize,
                                    yFontMetrics.horizontalAdvance(category));
            }
        }
#endif
    }

    for (auto&& ax : *m_horzAxes) {
        if (auto haxis = qobject_cast<QValueAxis *>(ax.axis)) {
            double step = haxis->tickInterval();

            qreal diff = haxis->max() - haxis->min();
            qreal center = diff / 2.0f + haxis->min() + haxis->pan();

            diff /= haxis->zoom();

            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;

            ax.valueRange = ax.maxValue - ax.minValue;
            ax.valueRangeZoomless = haxis->max() - haxis->min();

            // If step is not manually defined (or it is invalid), calculate autostep
            if (step <= 0)
                step = getValueStepsFromRange(haxis->max() - haxis->min());

            // Get smallest tick label value
            double minLabel = haxis->tickAnchor();
            while (minLabel < ax.minValue)
                minLabel += step;
            while (minLabel >= (ax.minValue + step))
                minLabel -= step;
            ax.minLabel = minLabel;

            ax.valueStep = step;
            int axisHorizontalSubTickCount = haxis->subTickCount();
            ax.subGridScale = axisHorizontalSubTickCount > 0
                                  ? 1.0 / (axisHorizontalSubTickCount + 1)
                                  : 1.0;
            double axisHorizontalValueDiff = ax.minLabel - ax.minValue;
            ax.displacement = -(axisHorizontalValueDiff / ax.valueStep) * ax.stepPx;

        } else if (auto haxis = qobject_cast<QDateTimeAxis *>(ax.axis)) {
            const double MAX_DIVS = 100.0;

            double tickCount = std::clamp<double>(haxis->tickCount(), 0.0, MAX_DIVS);
            double diff = haxis->max().toMSecsSinceEpoch() - haxis->min().toMSecsSinceEpoch();
            double center = diff / 2.0f + haxis->min().toMSecsSinceEpoch()
                                        + haxis->pan();

            diff /= haxis->zoom();
            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;
            ax.valueRange = std::abs(ax.maxValue - ax.minValue);
            ax.valueRangeZoomless = haxis->max().toMSecsSinceEpoch()
                                  - haxis->min().toMSecsSinceEpoch();

            // in ms
            double segment;
            if (tickCount <= 0) {
                segment = getValueStepsFromRange(ax.valueRange);
                tickCount = ax.valueRange / segment;
            } else {
                segment = ax.valueRange / tickCount;
            }

            ax.minLabel = std::clamp(tickCount, 1.0, MAX_DIVS);

            ax.valueStep = segment;
            int axisHorizontalSubTickCount = haxis->subTickCount();
            ax.subGridScale = axisHorizontalSubTickCount > 0
                                                 ? 1.0 / (axisHorizontalSubTickCount + 1)
                                                 : 1.0;
            ax.tickCount = tickCount;

            double axisHorizontalValueDiff = fmod(ax.minValue, ax.valueStep) / ax.valueStep;
            ax.displacement = axisHorizontalValueDiff * ax.stepPx;
        } else if (auto haxis = qobject_cast<QLogValueAxis *>(ax.axis)) {
            ax.isLogarithmic = true;
            ax.logBase = haxis->base();

            qreal logBase = log(haxis->base());
            qreal logMin = log(haxis->min()) / logBase;
            qreal logMax = log(haxis->max()) / logBase;

            qreal diff = logMax - logMin;
            qreal center = diff / 2.0f + logMin + haxis->pan();

            diff /= haxis->zoom();

            ax.maxValue = center + diff / 2.0f;
            ax.minValue = center - diff / 2.0f;

            //use log scale to create value range
            ax.valueRange = ax.maxValue - ax.minValue;
            ax.valueRangeZoomless = logMax - logMin;

            ax.minLabel = qRound(ax.minValue);
            ax.valueStep = 1;

            int axisHorizontalSubTickCount = haxis->subTickCount();
            if (axisHorizontalSubTickCount == -1)
                axisHorizontalSubTickCount = int(qRound(haxis->base()));
            ax.subGridScale = axisHorizontalSubTickCount > 0 ? 1.0 / (axisHorizontalSubTickCount + 1)
                : 1.0;
            double axisHorizontalValueDiff = ax.minLabel - ax.minValue;
            ax.displacement = -(axisHorizontalValueDiff / ax.valueStep) * ax.stepPx;
        }
#if QT_CONFIG(graphs_2d_bar)
        else if (auto haxis = qobject_cast<QBarCategoryAxis *>(ax.axis)) {
            ax.maxValue = haxis->categories().size();
            ax.minValue = 0;
            ax.valueRange = ax.maxValue - ax.minValue;
        }
#endif
    }

    // Add some arbitrary margin so that labels don't touch the title
    for (auto &ax : *m_vertAxes) {
        if (ax.labelSize > 0)
            ax.labelSize += 8;
    }

    // Calculate space needed for each axis
    const bool isDynamic = m_graph->dynamicLabelMargins();
    const qreal yLabelDefault = m_graph->m_defaultAxisLabelsWidth;
    const qreal xLabelDefault = m_graph->m_defaultAxisLabelsHeight;
    const qreal yMargin = m_graph->m_defaultAxisYLabelsMargin;
    const qreal xMargin = m_graph->m_defaultAxisXLabelsMargin;
    const qreal yTicker = m_graph->m_defaultAxisTickersWidth;
    const qreal xTicker = m_graph->m_defaultAxisTickersHeight;
    const qreal titleMargin = m_graph->m_defaultAxisTitleMargin;

    m_y1AxisWidth = 0;
    m_y2AxisWidth = 0;
    m_x1AxisHeight = 0;
    m_x2AxisHeight = 0;

    bool prevLeftTitled = false;
    bool prevRightTitled = false;
    bool prevTopTitled = false;
    bool prevBottomTitled = false;

    for (auto &ax : *m_vertAxes) {
        if (!ax.axis || !ax.axis->isVisible()) {
            ax.size = 0;
            continue;
        }

        ax.size = yMargin + yTicker;
        if (isDynamic)
            ax.size += qMax(ax.labelSize, yLabelDefault);
        else
            ax.size += yLabelDefault;

        if (isAxisBottomOrRight(ax)) {
            if (prevRightTitled)
                m_y2AxisWidth += titleMargin;
            m_y2AxisWidth += ax.size;
            prevRightTitled = hasAxisTitle(ax);
        } else {
            if (prevLeftTitled)
                m_y1AxisWidth += titleMargin;
            m_y1AxisWidth += ax.size;
            prevLeftTitled = hasAxisTitle(ax);
        }
    }

    for (auto &ax : *m_horzAxes) {
        if (!ax.axis || !ax.axis->isVisible()) {
            ax.size = 0;
            continue;
        }

        ax.size = xMargin + xTicker;
        if (isDynamic)
            ax.size += qMax(ax.labelSize, xLabelDefault);
        else
            ax.size += xLabelDefault;

        if (isAxisBottomOrRight(ax)) {
            if (prevBottomTitled)
                m_x1AxisHeight += titleMargin;
            m_x1AxisHeight += ax.size;
            prevBottomTitled = hasAxisTitle(ax);
        } else {
            if (prevTopTitled)
                m_x2AxisHeight += titleMargin;
            m_x2AxisHeight += ax.size;
            prevTopTitled = hasAxisTitle(ax);
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

//  from ../qtgraphs/src/graphs2d/qsgrenderer/axisrenderer.cpp, line 2046, as _ZN12AxisRenderer17createDragHandlerEv
inline void AxisRenderer::createDragHandler()
{
    m_dragHandler = new QQuickDragHandler(this);
    m_dragHandler->setDragThreshold(10);
    m_dragHandler->setTarget(nullptr);
    connect(m_dragHandler,
            &QQuickDragHandler::translationChanged,
            this,
            &AxisRenderer::onTranslationChanged);
    connect(m_dragHandler, &QQuickDragHandler::grabChanged, this, &AxisRenderer::onGrabChanged);
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

//  void *AxisRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12AxisRenderer11qt_metacastEPKc(
    AxisRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AxisRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12AxisRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    AxisRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AxisRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12AxisRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AxisRenderer::tr(s, c, n));
}

//  AxisRenderer::AxisRenderer(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
AxisRenderer *ritual_ZN12AxisRendererC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteAxisRenderer(parent);
}

//  AxisRenderer::~AxisRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRendererD1Ev(AxisRenderer *self) {
  delete self;
}

//  void AxisRenderer::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer10initializeEv(AxisRenderer *self) {
  self->initialize();
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

//  void AxisRenderer::populateAxisItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer17populateAxisItemsEv(AxisRenderer *self) {
  self->populateAxisItems();
}

//  void AxisRenderer::updateAxisTickers()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer17updateAxisTickersEv(AxisRenderer *self) {
  self->updateAxisTickers();
}

//  void AxisRenderer::updateAxisTickersShadow()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer23updateAxisTickersShadowEv(AxisRenderer *self) {
  self->updateAxisTickersShadow();
}

//  void AxisRenderer::updateAxisGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer14updateAxisGridEv(AxisRenderer *self) {
  self->updateAxisGrid();
}

//  void AxisRenderer::updateAxisGridShadow()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer20updateAxisGridShadowEv(AxisRenderer *self) {
  self->updateAxisGridShadow();
}

//  void AxisRenderer::updateAxisTitles()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer16updateAxisTitlesEv(AxisRenderer *self) {
  self->updateAxisTitles();
}

//  bool AxisRenderer::hasAxisTitle(const AxisProperties &ax) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12AxisRenderer12hasAxisTitleERKNS_14AxisPropertiesE(
    const AxisRenderer *self,
    const AxisRenderer::AxisProperties *ax) {
  return self->hasAxisTitle(*ax);
}

//  bool AxisRenderer::isAxisBottomOrRight(const AxisProperties &ax) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12AxisRenderer19isAxisBottomOrRightERKNS_14AxisPropertiesE(
    const AxisRenderer *self,
    const AxisRenderer::AxisProperties *ax) {
  return self->isAxisBottomOrRight(*ax);
}

//  void AxisRenderer::updateAxisMeasurements()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer22updateAxisMeasurementsEv(AxisRenderer *self) {
  self->updateAxisMeasurements();
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

//  void AxisRenderer::createDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AxisRenderer17createDragHandlerEv(AxisRenderer *self) {
  self->createDragHandler();
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

//  const AxisProperties &AxisRenderer::getAxisX(QAbstractSeries *series)
//      const
extern "C" Q_DECL_EXPORT
const AxisRenderer::AxisProperties *ritual_ZNK12AxisRenderer8getAxisXEP15QAbstractSeries(
    const AxisRenderer *self,
    QAbstractSeries *series) {
  return &(self->getAxisX(series));
}

//  const AxisProperties &AxisRenderer::getAxisY(QAbstractSeries *series)
//      const
extern "C" Q_DECL_EXPORT
const AxisRenderer::AxisProperties *ritual_ZNK12AxisRenderer8getAxisYEP15QAbstractSeries(
    const AxisRenderer *self,
    QAbstractSeries *series) {
  return &(self->getAxisY(series));
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

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
