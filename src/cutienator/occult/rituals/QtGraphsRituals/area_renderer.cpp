//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/arearenderer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AreaRenderer' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/arearenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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
#include <QtGraphs/qareaseries.h>
#if QT_CONFIG(graphs_2d_spline)
#include <QtGraphs/qsplineseries.h>
#endif
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtQuickShapes/private/qquickshape_p.h>
#include <QtGraphs/private/arearenderer_p.h>
#include <QtGraphs/private/axisrenderer_p.h>
#include <QtGraphs/private/pointrenderer_p.h>
#include <QtGraphs/private/qgraphsview_p.h>
#if QT_CONFIG(graphs_2d_high_performance_backend)
#include <QtCanvasPainter/QCanvasPainter>
#include <QtCanvasPainter/QCanvasLinearGradient>
#include <QtCanvasPainter/QCanvasConicalGradient>
#include <QtCanvasPainter/QCanvasRadialGradient>
#include <QtGui/QLinearGradient>
#include <QtGui/QRadialGradient>
#include <QtGui/QConicalGradient>
#endif
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

//  from QtGraphs__AreaRenderer.cpp, line 1, as moc:AreaRenderer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN12AreaRendererE_t {};
} // unnamed namespace

template <> constexpr inline auto AreaRenderer::qt_create_metaobjectdata<qt_meta_tag_ZN12AreaRendererE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AreaRenderer"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AreaRenderer, qt_meta_tag_ZN12AreaRendererE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AreaRenderer::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AreaRendererE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AreaRendererE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN12AreaRendererE_t>.metaTypes,
    nullptr
} };

void AreaRenderer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AreaRenderer *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *AreaRenderer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AreaRenderer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12AreaRendererE_t>.strings))
        return static_cast<void*>(this);
    return QQuickItem::qt_metacast(_clname);
}

int AreaRenderer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickItem::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 68, as _ZN12AreaRendererD0Ev
inline AreaRenderer::~AreaRenderer()
{
    qDeleteAll(m_groups);
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

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 73, as _ZN12AreaRenderer19resetShapePathCountEv
inline void AreaRenderer::resetShapePathCount()
{
    m_currentShapePathIndex = 0;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 79, as _ZNK12AreaRenderer13paintSnapshotEv
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline AreaRenderer::PaintSnapshot AreaRenderer::paintSnapshot() const
{
    return m_areaPaintSnapshot;
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 84, as _ZN12AreaRenderer15synchronizeDataEv
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline void AreaRenderer::synchronizeData()
{
    m_areaPaintSnapshot.clear();
    for (auto &&group : m_groups) {
        if (group->painterPath.elementCount() == 0)
            continue;

        const auto style = getSeriesStyle(group);
        AreaPaintData paintData;
        if (auto linear = qobject_cast<QQuickShapeLinearGradient *>(style.gradient)) {
            QLinearGradient gradient(linear->x1(), linear->y1(), linear->x2(), linear->y2());
            gradient.setStops(linear->gradientStops());
            paintData.gradient = gradient;
        } else if (auto radial = qobject_cast<QQuickShapeRadialGradient *>(style.gradient)) {
            QPointF center(radial->centerX(), radial->centerY());
            QPointF focal(radial->focalX(), radial->focalY());
            QRadialGradient gradient(center, radial->centerRadius(), focal, radial->focalRadius());
            gradient.setStops(radial->gradientStops());
            paintData.gradient = gradient;
        } else if (auto conical = qobject_cast<QQuickShapeConicalGradient *>(style.gradient)) {
            QConicalGradient gradient(conical->centerX(), conical->centerY(), conical->angle());
            gradient.setStops(conical->gradientStops());
            paintData.gradient = gradient;
        } else {
            paintData.resolvedColor = style.color;
        }
        paintData.resolvedBorderColor = style.borderColor;
        paintData.resolvedBorderWidth = style.borderWidth;
        paintData.painterPath = group->painterPath;
        m_areaPaintSnapshot.append(paintData);
    }
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 117, as _ZN12AreaRenderer13paintSnapshotERK5QListINS_13AreaPaintDataEEP14QCanvasPainter
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline void AreaRenderer::paintSnapshot(const PaintSnapshot &snapshot, QCanvasPainter *p)
{
    for (const auto &areaPaintSnapshot : snapshot) {
        const auto &gradient = areaPaintSnapshot.gradient;
        switch (gradient.type()) {
        case QGradient::LinearGradient: {
            const auto &lg = static_cast<const QLinearGradient &>(gradient);
            QCanvasLinearGradient canvasGradient(lg.start().x(),
                                                 lg.start().y(),
                                                 lg.finalStop().x(),
                                                 lg.finalStop().y());
            const QGradientStops stops = lg.stops();
            for (const auto &stop : stops)
                canvasGradient.setColorAt(stop.first, stop.second);
            p->setFillStyle(canvasGradient);
        } break;
        case QGradient::RadialGradient: {
            const auto &rg = static_cast<const QRadialGradient &>(gradient);
            QCanvasRadialGradient canvasGradient(rg.center().x(),
                                                 rg.center().y(),
                                                 rg.focalRadius(),
                                                 rg.centerRadius());
            const QGradientStops stops = rg.stops();
            for (const auto &stop : stops)
                canvasGradient.setColorAt(stop.first, stop.second);
            p->setFillStyle(canvasGradient);
        } break;
        case QGradient::ConicalGradient: {
            const auto &cg = static_cast<const QConicalGradient &>(gradient);
            QCanvasConicalGradient canvasGradient(cg.center().x(), cg.center().y(), cg.angle());
            const QGradientStops stops = cg.stops();
            for (const auto &stop : stops)
                canvasGradient.setColorAt(stop.first, stop.second);
            p->setFillStyle(canvasGradient);
        } break;
        case QGradient::NoGradient: {
            p->setFillStyle(areaPaintSnapshot.resolvedColor);
        }
        }
        p->setStrokeStyle(areaPaintSnapshot.resolvedBorderColor);
        p->setLineWidth(areaPaintSnapshot.resolvedBorderWidth);
        p->beginPath();
        p->addPath(areaPaintSnapshot.painterPath);
        p->fill();
        p->stroke();
    }
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 457, as _ZN12AreaRenderer11afterUpdateER5QListIP15QAbstractSeriesE
inline void AreaRenderer::afterUpdate(QList<QAbstractSeries *> &cleanupSeries)
{
    Q_UNUSED(cleanupSeries);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 462, as _ZN12AreaRenderer12updateSeriesEP11QAreaSeries
inline void AreaRenderer::updateSeries(QAreaSeries *series)
{
    Q_UNUSED(series);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 467, as _ZN12AreaRenderer22seriesAboutToBeRemovedEP15QAbstractSeries
inline void AreaRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
{
    if (auto *areaSeries = qobject_cast<QAreaSeries *>(series)) {
        auto iter = m_groups.find(areaSeries);

        if (iter != m_groups.end()) {
            delete *iter;
            m_groups.erase(iter);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 166, as _ZN12AreaRenderer14getSeriesStyleEPNS_10PointGroupE
inline AreaRenderer::SeriesStyle AreaRenderer::getSeriesStyle(PointGroup *group)
{
    auto theme = m_graph->theme();

    const auto &seriesColors = theme->seriesColors();
    qsizetype index = group->colorIndex % seriesColors.size();
    QColor color = group->series->color().alpha() != 0 ? group->series->color()
                                                       : seriesColors.at(index);
    const auto &borderColors = theme->borderColors();
    index = group->colorIndex % borderColors.size();
    QColor borderColor = group->series->borderColor().alpha() != 0 ? group->series->borderColor()
                                                                   : borderColors.at(index);

    QQuickShapeGradient *gradient = group->series->gradient();

    if (group->series->isSelected()) {
        color = group->series->selectedColor().alpha() != 0 ? group->series->selectedColor()
                                                            : color.lighter();
        borderColor = group->series->selectedBorderColor().alpha() != 0
                          ? group->series->selectedBorderColor()
                          : borderColor.lighter();
        if (group->series->selectedGradient())
            gradient = group->series->selectedGradient();
    }

    qreal borderWidth = group->series->borderWidth();
    if (qFuzzyCompare(borderWidth, qreal(-1.0)))
        borderWidth = theme->borderWidth();

    return {color, gradient, borderColor, borderWidth};
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 198, as _ZNK12AreaRenderer26calculateRenderCoordinatesEP11QAreaSeriesddPdS2_
inline void AreaRenderer::calculateRenderCoordinates(
    QAreaSeries *series, qreal origX, qreal origY, qreal *renderX, qreal *renderY) const
{
    auto &axY = m_graph->m_axisRenderer->getAxisY(series);
    auto &axX = m_graph->m_axisRenderer->getAxisX(series);

    float x = origX;
    float y = origY;

    if (axX.isLogarithmic) {
        float logBase = log(axX.logBase);
        x = log(origX) / logBase;
    }

    if (axY.isLogarithmic) {
        float logBase = log(axY.logBase);
        y = log(origY) / logBase;
    }

    if (m_graph->orientation() != Qt::Vertical) {
        std::swap(x, y);
        y = axY.maxValue - y;
    }

    *renderX = m_areaWidth * x * m_maxHorizontal - m_horizontalOffset;
    *renderY = m_areaHeight - m_areaHeight * y * m_maxVertical
               + m_verticalOffset;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/arearenderer.cpp, line 227, as _ZNK12AreaRenderer24calculateAxisCoordinatesEP11QAreaSeriesddPdS2_
inline void AreaRenderer::calculateAxisCoordinates(
    QAreaSeries *series, qreal origX, qreal origY, qreal *axisX, qreal *axisY) const
{
    auto &axY = m_graph->m_axisRenderer->getAxisY(series);
    auto &axX = m_graph->m_axisRenderer->getAxisX(series);

    if (m_graph->orientation() != Qt::Vertical) {
        std::swap(origX, origY);
        origY = axY.maxValue - origY;
    }

    qreal x = (origX + m_horizontalOffset) / (m_areaWidth * m_maxHorizontal);
    qreal y = (origY - m_areaHeight - m_verticalOffset)
             / (-1 * m_areaHeight * m_maxVertical);

    if (axX.isLogarithmic)
        x = pow(axX.logBase, x);

    if (axY.isLogarithmic)
        y = pow(axY.logBase, y);

    *axisX = x;
    *axisY = y;
}
//  -----------------------------------------------------------------------

//  A AreaRenderer that Python can take functions over in. Every AreaRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteAreaRendererCall0)(const void *, int *);
typedef const QRectF * (*CuteAreaRendererCall1)(const void *, int *);
typedef bool (*CuteAreaRendererCall2)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAreaRendererCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAreaRendererCall4)(const void *, int *);
typedef void * (*CuteAreaRendererCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAreaRendererCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteAreaRendererCall8)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteAreaRendererCall9)(const void *, int *);
typedef void (*CuteAreaRendererCall10)(const void *, int *);
typedef void (*CuteAreaRendererCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteAreaRendererCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAreaRendererCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAreaRendererCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteAreaRendererCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAreaRendererCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteAreaRendererCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAreaRendererCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAreaRendererCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAreaRendererCall20)(const void *, int *);
typedef void (*CuteAreaRendererCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAreaRendererCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAreaRendererCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteAreaRendererCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteAreaRendererCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAreaRendererCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAreaRendererCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAreaRendererCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAreaRendererCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAreaRendererCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAreaRendererCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteAreaRendererCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteAreaRendererCall33)(const void *, int *);
typedef void (*CuteAreaRendererCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAreaRendererCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAreaRendererCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAreaRenderer : public AreaRenderer {
public:
  using AreaRenderer::AreaRenderer;
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
      CuteAreaRendererCall0 call = reinterpret_cast<CuteAreaRendererCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAreaRendererCall1 call = reinterpret_cast<CuteAreaRendererCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteAreaRendererCall2 call = reinterpret_cast<CuteAreaRendererCall2>(taken[2]);
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
      CuteAreaRendererCall3 call = reinterpret_cast<CuteAreaRendererCall3>(taken[3]);
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
      CuteAreaRendererCall4 call = reinterpret_cast<CuteAreaRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteAreaRendererCall5 call = reinterpret_cast<CuteAreaRendererCall5>(taken[5]);
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
      CuteAreaRendererCall6 call = reinterpret_cast<CuteAreaRendererCall6>(taken[6]);
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
      CuteAreaRendererCall7 call = reinterpret_cast<CuteAreaRendererCall7>(taken[7]);
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
      CuteAreaRendererCall8 call = reinterpret_cast<CuteAreaRendererCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteAreaRendererCall9 call = reinterpret_cast<CuteAreaRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteAreaRendererCall10 call = reinterpret_cast<CuteAreaRendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteAreaRendererCall11 call = reinterpret_cast<CuteAreaRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAreaRendererCall12 call = reinterpret_cast<CuteAreaRendererCall12>(taken[12]);
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
      CuteAreaRendererCall13 call = reinterpret_cast<CuteAreaRendererCall13>(taken[13]);
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
      CuteAreaRendererCall14 call = reinterpret_cast<CuteAreaRendererCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteAreaRendererCall15 call = reinterpret_cast<CuteAreaRendererCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteAreaRendererCall16 call = reinterpret_cast<CuteAreaRendererCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAreaRendererCall17 call = reinterpret_cast<CuteAreaRendererCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAreaRendererCall18 call = reinterpret_cast<CuteAreaRendererCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAreaRendererCall19 call = reinterpret_cast<CuteAreaRendererCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteAreaRendererCall20 call = reinterpret_cast<CuteAreaRendererCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAreaRendererCall21 call = reinterpret_cast<CuteAreaRendererCall21>(taken[21]);
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
      CuteAreaRendererCall22 call = reinterpret_cast<CuteAreaRendererCall22>(taken[22]);
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
      CuteAreaRendererCall23 call = reinterpret_cast<CuteAreaRendererCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteAreaRendererCall24 call = reinterpret_cast<CuteAreaRendererCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAreaRendererCall25 call = reinterpret_cast<CuteAreaRendererCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAreaRendererCall26 call = reinterpret_cast<CuteAreaRendererCall26>(taken[26]);
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
      CuteAreaRendererCall27 call = reinterpret_cast<CuteAreaRendererCall27>(taken[27]);
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
      CuteAreaRendererCall28 call = reinterpret_cast<CuteAreaRendererCall28>(taken[28]);
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
      CuteAreaRendererCall29 call = reinterpret_cast<CuteAreaRendererCall29>(taken[29]);
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
      CuteAreaRendererCall30 call = reinterpret_cast<CuteAreaRendererCall30>(taken[30]);
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
      CuteAreaRendererCall31 call = reinterpret_cast<CuteAreaRendererCall31>(taken[31]);
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
      CuteAreaRendererCall32 call = reinterpret_cast<CuteAreaRendererCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAreaRendererCall33 call = reinterpret_cast<CuteAreaRendererCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAreaRendererCall34 call = reinterpret_cast<CuteAreaRendererCall34>(taken[34]);
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
      CuteAreaRendererCall35 call = reinterpret_cast<CuteAreaRendererCall35>(taken[35]);
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
      CuteAreaRendererCall36 call = reinterpret_cast<CuteAreaRendererCall36>(taken[36]);
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
      CuteAreaRendererCall37 call = reinterpret_cast<CuteAreaRendererCall37>(taken[37]);
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
      CuteAreaRendererCall38 call = reinterpret_cast<CuteAreaRendererCall38>(taken[38]);
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
      CuteAreaRendererCall39 call = reinterpret_cast<CuteAreaRendererCall39>(taken[39]);
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
      CuteAreaRendererCall40 call = reinterpret_cast<CuteAreaRendererCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AreaRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12AreaRenderer10metaObjectEv(
    const AreaRenderer *self) {
  return self->metaObject();
}

//  void *AreaRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12AreaRenderer11qt_metacastEPKc(
    AreaRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AreaRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12AreaRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    AreaRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AreaRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12AreaRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AreaRenderer::tr(s, c, n));
}

//  AreaRenderer::~AreaRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRendererD1Ev(AreaRenderer *self) {
  delete self;
}

//  void AreaRenderer::resetShapePathCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer19resetShapePathCountEv(AreaRenderer *self) {
  self->resetShapePathCount();
}

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  PaintSnapshot AreaRenderer::paintSnapshot() const
extern "C" Q_DECL_EXPORT
AreaRenderer::PaintSnapshot *ritual_ZNK12AreaRenderer13paintSnapshotEv(
    const AreaRenderer *self) {
  return new AreaRenderer::PaintSnapshot(self->paintSnapshot());
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void AreaRenderer::synchronizeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer15synchronizeDataEv(AreaRenderer *self) {
  self->synchronizeData();
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void AreaRenderer::paintSnapshot(const PaintSnapshot &snapshot,
//      QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer13paintSnapshotERK5QListINS_13AreaPaintDataEEP14QCanvasPainter(
    const AreaRenderer::PaintSnapshot *snapshot,
    QCanvasPainter *p) {
  AreaRenderer::paintSnapshot(*snapshot, p);
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  void AreaRenderer::afterUpdate(QList<QAbstractSeries *> &cleanupSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer11afterUpdateER5QListIP15QAbstractSeriesE(
    AreaRenderer *self,
    QList<QAbstractSeries *> *cleanupSeries) {
  self->afterUpdate(*cleanupSeries);
}

//  void AreaRenderer::updateSeries(QAreaSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer12updateSeriesEP11QAreaSeries(
    AreaRenderer *self,
    QAreaSeries *series) {
  self->updateSeries(series);
}

//  void AreaRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12AreaRenderer22seriesAboutToBeRemovedEP15QAbstractSeries(
    AreaRenderer *self,
    QAbstractSeries *series) {
  self->seriesAboutToBeRemoved(series);
}

//  SeriesStyle AreaRenderer::getSeriesStyle(PointGroup *group)
extern "C" Q_DECL_EXPORT
AreaRenderer::SeriesStyle *ritual_ZN12AreaRenderer14getSeriesStyleEPNS_10PointGroupE(
    AreaRenderer *self,
    AreaRenderer::PointGroup *group) {
  return new AreaRenderer::SeriesStyle(self->getSeriesStyle(group));
}

//  void AreaRenderer::calculateRenderCoordinates(QAreaSeries *series, qreal
//      origX, qreal origY, qreal *renderX, qreal *renderY) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12AreaRenderer26calculateRenderCoordinatesEP11QAreaSeriesddPdS2_(
    const AreaRenderer *self,
    QAreaSeries *series,
    qreal origX,
    qreal origY,
    qreal *renderX,
    qreal *renderY) {
  self->calculateRenderCoordinates(series, origX, origY, renderX, renderY);
}

//  void AreaRenderer::calculateAxisCoordinates(QAreaSeries *series, qreal
//      origX, qreal origY, qreal *axisX, qreal *axisY) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12AreaRenderer24calculateAxisCoordinatesEP11QAreaSeriesddPdS2_(
    const AreaRenderer *self,
    QAreaSeries *series,
    qreal origX,
    qreal origY,
    qreal *axisX,
    qreal *axisY) {
  self->calculateAxisCoordinates(series, origX, origY, axisX, axisY);
}

//  a Python function taken by a CuteAreaRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AreaRenderer(
    AreaRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteAreaRenderer *>(self)->take(key, call);
}

//  a AreaRenderer::PaintSnapshot a ritual of AreaRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_AreaRenderer__AreaRenderer_PaintSnapshot(
    AreaRenderer::PaintSnapshot *self) {
  delete self;
}

//  a AreaRenderer::SeriesStyle a ritual of AreaRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_AreaRenderer__AreaRenderer_SeriesStyle(
    AreaRenderer::SeriesStyle *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area))
