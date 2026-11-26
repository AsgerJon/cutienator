//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/barsrenderer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'BarsRenderer' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/barsrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qeventpoint.h>
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
#include <QtGraphs/qbarseries.h>
#include <QtGraphs/qbarset.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtGraphs/private/axisrenderer_p.h>
#include <QtGraphs/private/barsrenderer_p.h>
#include <QtGraphs/private/qgraphsview_p.h>
#include <utility>
#if QT_CONFIG(graphs_2d_high_performance_backend)
#include <QtCanvasPainter/QCanvasPainter>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 316, as local:barsrenderer.cpp:calculateCategoryTotalValues
inline void calculateCategoryTotalValues(QBarSeries *series, QList<float> &totalValues, qsizetype valuesPerSet)
{
    totalValues.fill(0, valuesPerSet);
    auto barsets = series->barSets();
    for (auto s : std::as_const(barsets)) {
        QVariantList v = s->values();
        int setIndex = 0;
        for (const auto &variantValue : std::as_const(v)) {
            if (setIndex < totalValues.size())
                totalValues[setIndex] += qAbs(variantValue.toReal());
            setIndex++;
        }
    }
}

//  from QtGraphs__BarsRenderer.cpp, line 1, as moc:BarsRenderer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN12BarsRendererE_t {};
} // unnamed namespace

template <> constexpr inline auto BarsRenderer::qt_create_metaobjectdata<qt_meta_tag_ZN12BarsRendererE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "BarsRenderer"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<BarsRenderer, qt_meta_tag_ZN12BarsRendererE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject BarsRenderer::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12BarsRendererE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12BarsRendererE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN12BarsRendererE_t>.metaTypes,
    nullptr
} };

void BarsRenderer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<BarsRenderer *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *BarsRenderer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *BarsRenderer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12BarsRendererE_t>.strings))
        return static_cast<void*>(this);
    return QQuickItem::qt_metacast(_clname);
}

int BarsRenderer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickItem::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 62, as _ZN12BarsRendererD0Ev
inline BarsRenderer::~BarsRenderer() {}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 49, as _ZN12BarsRendererC1EP11QGraphsViewb
inline BarsRenderer::BarsRenderer(QGraphsView *graph, bool clipPlotArea)
    : QQuickItem(graph)
    , m_graph(graph)
{
    setFlag(QQuickItem::ItemHasContents);
    setClip(clipPlotArea);

    m_tapHandler = new QQuickTapHandler(this);
    connect(m_tapHandler, &QQuickTapHandler::singleTapped, this, &BarsRenderer::onSingleTapped);
    connect(m_tapHandler, &QQuickTapHandler::doubleTapped, this, &BarsRenderer::onDoubleTapped);
    connect(m_tapHandler, &QQuickTapHandler::pressedChanged, this, &BarsRenderer::onPressedChanged);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 65, as _ZN12BarsRenderer13paintSnapshotERK5QHashIP10QBarSeries5QListINS_13BarSeriesDataEEEP14QCanvasPainter
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline void BarsRenderer::paintSnapshot(const PaintSnapshot &snapshot,
                                 QCanvasPainter *p)
{
    for (const auto &dataList : snapshot) {
        for (const auto &d : dataList) {
            p->setFillStyle(d.color);
            p->setStrokeStyle(d.borderColor);
            p->setLineWidth(d.borderWidth);
            p->beginPath();
            p->rect(d.rect);
            p->fill();
            p->stroke();
        }
    }
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 86, as _ZNK12BarsRenderer13paintSnapshotEv
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline BarsRenderer::PaintSnapshot BarsRenderer::paintSnapshot() const
{
    return m_paintSnapshot;
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 81, as _ZN12BarsRenderer15synchronizeDataEv
#if QT_CONFIG(graphs_2d_high_performance_backend)
inline void BarsRenderer::synchronizeData()
{
    m_paintSnapshot = m_seriesData;
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 655, as _ZN12BarsRenderer12updateSeriesEP10QBarSeries
inline void BarsRenderer::updateSeries(QBarSeries *series)
{
    Q_UNUSED(series);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 660, as _ZN12BarsRenderer22seriesAboutToBeRemovedEP15QAbstractSeries
inline void BarsRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
{
    if (auto *barsSeries = qobject_cast<QBarSeries *>(series)) {
        auto barItemsIter = m_barItems.find(barsSeries);
        if (barItemsIter != m_barItems.end()) {
            // Remove custom bar items
            auto &barItems = *barItemsIter;
            for (const auto &item : std::as_const(barItems))
                item->deleteLater();
            barItems.clear();
            m_barItems.erase(barItemsIter);
        }

        auto textItemsIter = m_labelTextItems.find(barsSeries);
        if (textItemsIter != m_labelTextItems.end()) {
            // Remove bar label items
            auto &labelTextItems = *textItemsIter;
            for (const auto &item : std::as_const(labelTextItems))
                item->deleteLater();
            labelTextItems.clear();
            m_labelTextItems.erase(textItemsIter);
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 685, as _ZN12BarsRenderer11afterUpdateER5QListIP15QAbstractSeriesE
inline void BarsRenderer::afterUpdate(QList<QAbstractSeries *> &cleanupSeries)
{
    Q_UNUSED(cleanupSeries);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 690, as _ZN12BarsRenderer11afterPolishER5QListIP15QAbstractSeriesE
inline void BarsRenderer::afterPolish(QList<QAbstractSeries *> &cleanupSeries)
{
    Q_UNUSED(cleanupSeries);
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 695, as _ZN12BarsRenderer15handleHoverMoveEP11QHoverEvent
inline bool BarsRenderer::handleHoverMove(QHoverEvent *event)
{
    bool handled = false;
    const QPointF &position = event->position();

    bool hovering = false;
    for (auto &rectNodesInputRects : m_rectNodesInputRects) {
        for (auto &barSelection : rectNodesInputRects) {
            int indexInSet = 0;

            for (auto &rect : barSelection.rects) {
                if (rect.contains(event->position().toPoint())) {
                    const QString &name = barSelection.series->name();
                    const QPointF point(indexInSet, barSelection.barSet->at(indexInSet));

                    if (!m_currentHoverSeries) {
                        m_currentHoverSeries = barSelection.series;
                        barSelection.series->setHovered(true);
                        emit barSelection.series->hoverEnter(name, position, point);
                    }

                    emit barSelection.series->hover(name, position, point);
                    hovering = true;
                    handled = true;
                }
                indexInSet++;
            }
        }
    }

    if (!hovering && m_currentHoverSeries) {
        m_currentHoverSeries->setHovered(false);
        emit m_currentHoverSeries->hoverExit(m_currentHoverSeries->name(), position);
        m_currentHoverSeries = nullptr;
        handled = true;
    }
    return handled;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 97, as _ZN12BarsRenderer11getSetColorEP10QBarSeriesP7QBarSetx
inline QColor BarsRenderer::getSetColor(QBarSeries *series, QBarSet *set, qsizetype barSeriesIndex)
{
    const auto &seriesColors = !series->seriesColors().isEmpty()
            ? series->seriesColors() : m_graph->theme()->seriesColors();
    if (seriesColors.isEmpty())
        return QColorConstants::Black;
    qsizetype index = m_colorIndex + barSeriesIndex;
    index = index % seriesColors.size();
    QColor color = set->color().alpha() != 0
            ? set->color()
            : seriesColors.at(index);
    return color;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 111, as _ZN12BarsRenderer19getSetSelectedColorEP10QBarSeriesP7QBarSet
inline QColor BarsRenderer::getSetSelectedColor(QBarSeries *series, QBarSet *set)
{
    Q_UNUSED(series);
    auto theme = m_graph->theme();
    QColor color = set->selectedColor().alpha() != 0
            ? set->selectedColor()
            : theme->singleHighlightColor();
    return color;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 121, as _ZN12BarsRenderer17getSetBorderColorEP10QBarSeriesP7QBarSetx
inline QColor BarsRenderer::getSetBorderColor(QBarSeries *series, QBarSet *set, qsizetype barSeriesIndex)
{
    const auto &borderColors = !series->borderColors().isEmpty()
            ? series->borderColors() : m_graph->theme()->borderColors();
    if (borderColors.isEmpty())
        return QColorConstants::Black;
    qsizetype index = m_colorIndex + barSeriesIndex;
    index = index % borderColors.size();
    QColor color = set->borderColor().alpha() != 0
            ? set->borderColor()
            : borderColors.at(index);
    return color;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 135, as _ZN12BarsRenderer17getSetBorderWidthEP10QBarSeriesP7QBarSet
inline qreal BarsRenderer::getSetBorderWidth(QBarSeries *series, QBarSet *set)
{
    Q_UNUSED(series);
    auto theme = m_graph->theme();
    qreal borderWidth = set->borderWidth();
    if (qFuzzyCompare(borderWidth, qreal(-1.0)))
        borderWidth = theme->borderWidth();
    return borderWidth;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 145, as _ZN12BarsRenderer17generateLabelTextEP10QBarSeriesd
inline QString BarsRenderer::generateLabelText(QBarSeries *series, qreal value)
{
    static const QString valueTag(QLatin1String("@value"));
    QString valueString = QString::number(value, 'f', series->labelsPrecision());
    QString valueLabel;
    if (series->labelsFormat().isEmpty()) {
        valueLabel = valueString;
    } else {
        valueLabel = series->labelsFormat();
        valueLabel.replace(valueTag, valueString);
    }
    return valueLabel;
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 159, as _ZN12BarsRenderer17positionLabelItemEP10QBarSeriesP10QQuickTextRKNS_13BarSeriesDataE
inline void BarsRenderer::positionLabelItem(QBarSeries *series, QQuickText *textItem, const BarSeriesData &d)
{
    auto pos = series->labelsPosition();
    const bool vertical = m_graph->orientation() == Qt::Orientation::Vertical;
    const float w = textItem->contentWidth() + series->labelsMargin() * 2;
    const float h = textItem->contentHeight() + series->labelsMargin() * 2;
    textItem->setWidth(w);
    textItem->setHeight(h);
    textItem->setHAlign(QQuickText::HAlignment::AlignHCenter);
    textItem->setVAlign(QQuickText::VAlignment::AlignVCenter);
    if (pos == QBarSeries::LabelsPosition::Center) {
        textItem->setX(d.rect.x() + d.rect.width() * 0.5 - w * 0.5);
        textItem->setY(d.rect.y() + d.rect.height() * 0.5 - h * 0.5);
    } else if (pos == QBarSeries::LabelsPosition::InsideEnd) {
        if (vertical) {
            textItem->setX(d.rect.x() + d.rect.width() * 0.5 - w * 0.5);
            textItem->setY(d.rect.y());
        } else {
            textItem->setX(d.rect.x() + d.rect.width() - w);
            textItem->setY(d.rect.y() + d.rect.height() * 0.5 - h * 0.5);
        }
    } else if (pos == QBarSeries::LabelsPosition::InsideBase) {
        if (vertical) {
            textItem->setX(d.rect.x() + d.rect.width() * 0.5 - w * 0.5);
            textItem->setY(d.rect.y() + d.rect.height() - h);
        } else {
            textItem->setX(d.rect.x());
            textItem->setY(d.rect.y() + d.rect.height() * 0.5 - h * 0.5);
        }
    } else {
        // OutsideEnd
        if (vertical) {
            textItem->setX(d.rect.x() + d.rect.width() * 0.5 - w * 0.5);
            textItem->setY(d.rect.y() - h);
        } else {
            textItem->setX(d.rect.x() + d.rect.width());
            textItem->setY(d.rect.y() + d.rect.height() * 0.5 - h * 0.5);
        }
    }
    textItem->update();
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 734, as _ZN12BarsRenderer14onSingleTappedE11QEventPointN2Qt11MouseButtonE
inline void BarsRenderer::onSingleTapped(QEventPoint eventPoint, Qt::MouseButton button)
{
    Q_UNUSED(button)

    for (auto &rectNodesInputRects : m_rectNodesInputRects) {
        for (auto &barSelection : rectNodesInputRects) {
            if (!barSelection.series->isSelectable())
                continue;
            qsizetype indexInSet = 0;
            for (auto &rect : barSelection.rects) {
                if (rect.contains(eventPoint.position())) {
                    emit barSelection.series->clicked(indexInSet, barSelection.barSet);
                    return;
                }
                indexInSet++;
            }
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 754, as _ZN12BarsRenderer14onDoubleTappedE11QEventPointN2Qt11MouseButtonE
inline void BarsRenderer::onDoubleTapped(QEventPoint eventPoint, Qt::MouseButton button)
{
    Q_UNUSED(button)

    for (auto &rectNodesInputRects : m_rectNodesInputRects) {
        for (auto &barSelection : rectNodesInputRects) {
            if (!barSelection.series->isSelectable())
                continue;
            qsizetype indexInSet = 0;
            for (auto &rect : barSelection.rects) {
                if (rect.contains(eventPoint.position())) {
                    emit barSelection.series->doubleClicked(indexInSet, barSelection.barSet);
                    return;
                }
                indexInSet++;
            }
        }
    }
}

//  from ../qtgraphs/src/graphs2d/qsgrenderer/barsrenderer.cpp, line 774, as _ZN12BarsRenderer16onPressedChangedEv
inline void BarsRenderer::onPressedChanged()
{
    for (auto &rectNodesInputRects : m_rectNodesInputRects) {
        for (auto &barSelection : rectNodesInputRects) {
            if (!barSelection.series->isSelectable())
                continue;
            qsizetype indexInSet = 0;
            for (auto &rect : barSelection.rects) {
                if (rect.contains(m_tapHandler->point().position())) {
                    // TODO: Currently just toggling selection
                    if (m_tapHandler->isPressed()) {
                        QList<qsizetype> indexList = {indexInSet};
                        barSelection.barSet->toggleSelection(indexList);
                        emit barSelection.series->pressed(indexInSet, barSelection.barSet);
                    } else {
                        emit barSelection.series->released(indexInSet, barSelection.barSet);
                    }
                }
                indexInSet++;
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  A BarsRenderer that Python can take functions over in. Every BarsRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteBarsRendererCall0)(const void *, int *);
typedef const QRectF * (*CuteBarsRendererCall1)(const void *, int *);
typedef bool (*CuteBarsRendererCall2)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteBarsRendererCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteBarsRendererCall4)(const void *, int *);
typedef void * (*CuteBarsRendererCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarsRendererCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteBarsRendererCall8)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteBarsRendererCall9)(const void *, int *);
typedef void (*CuteBarsRendererCall10)(const void *, int *);
typedef void (*CuteBarsRendererCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteBarsRendererCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteBarsRendererCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteBarsRendererCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteBarsRendererCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteBarsRendererCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteBarsRendererCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteBarsRendererCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteBarsRendererCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteBarsRendererCall20)(const void *, int *);
typedef void (*CuteBarsRendererCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteBarsRendererCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteBarsRendererCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteBarsRendererCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteBarsRendererCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteBarsRendererCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteBarsRendererCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteBarsRendererCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteBarsRendererCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteBarsRendererCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteBarsRendererCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteBarsRendererCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteBarsRendererCall33)(const void *, int *);
typedef void (*CuteBarsRendererCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarsRendererCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarsRendererCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBarsRenderer : public BarsRenderer {
public:
  using BarsRenderer::BarsRenderer;
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
      CuteBarsRendererCall0 call = reinterpret_cast<CuteBarsRendererCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteBarsRendererCall1 call = reinterpret_cast<CuteBarsRendererCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[2]) {
      int handled = 0;
      CuteBarsRendererCall2 call = reinterpret_cast<CuteBarsRendererCall2>(taken[2]);
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
      CuteBarsRendererCall3 call = reinterpret_cast<CuteBarsRendererCall3>(taken[3]);
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
      CuteBarsRendererCall4 call = reinterpret_cast<CuteBarsRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteBarsRendererCall5 call = reinterpret_cast<CuteBarsRendererCall5>(taken[5]);
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
      CuteBarsRendererCall6 call = reinterpret_cast<CuteBarsRendererCall6>(taken[6]);
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
      CuteBarsRendererCall7 call = reinterpret_cast<CuteBarsRendererCall7>(taken[7]);
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
      CuteBarsRendererCall8 call = reinterpret_cast<CuteBarsRendererCall8>(taken[8]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteBarsRendererCall9 call = reinterpret_cast<CuteBarsRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteBarsRendererCall10 call = reinterpret_cast<CuteBarsRendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteBarsRendererCall11 call = reinterpret_cast<CuteBarsRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteBarsRendererCall12 call = reinterpret_cast<CuteBarsRendererCall12>(taken[12]);
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
      CuteBarsRendererCall13 call = reinterpret_cast<CuteBarsRendererCall13>(taken[13]);
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
      CuteBarsRendererCall14 call = reinterpret_cast<CuteBarsRendererCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteBarsRendererCall15 call = reinterpret_cast<CuteBarsRendererCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteBarsRendererCall16 call = reinterpret_cast<CuteBarsRendererCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteBarsRendererCall17 call = reinterpret_cast<CuteBarsRendererCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteBarsRendererCall18 call = reinterpret_cast<CuteBarsRendererCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteBarsRendererCall19 call = reinterpret_cast<CuteBarsRendererCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteBarsRendererCall20 call = reinterpret_cast<CuteBarsRendererCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteBarsRendererCall21 call = reinterpret_cast<CuteBarsRendererCall21>(taken[21]);
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
      CuteBarsRendererCall22 call = reinterpret_cast<CuteBarsRendererCall22>(taken[22]);
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
      CuteBarsRendererCall23 call = reinterpret_cast<CuteBarsRendererCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteBarsRendererCall24 call = reinterpret_cast<CuteBarsRendererCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteBarsRendererCall25 call = reinterpret_cast<CuteBarsRendererCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteBarsRendererCall26 call = reinterpret_cast<CuteBarsRendererCall26>(taken[26]);
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
      CuteBarsRendererCall27 call = reinterpret_cast<CuteBarsRendererCall27>(taken[27]);
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
      CuteBarsRendererCall28 call = reinterpret_cast<CuteBarsRendererCall28>(taken[28]);
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
      CuteBarsRendererCall29 call = reinterpret_cast<CuteBarsRendererCall29>(taken[29]);
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
      CuteBarsRendererCall30 call = reinterpret_cast<CuteBarsRendererCall30>(taken[30]);
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
      CuteBarsRendererCall31 call = reinterpret_cast<CuteBarsRendererCall31>(taken[31]);
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
      CuteBarsRendererCall32 call = reinterpret_cast<CuteBarsRendererCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteBarsRendererCall33 call = reinterpret_cast<CuteBarsRendererCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteBarsRendererCall34 call = reinterpret_cast<CuteBarsRendererCall34>(taken[34]);
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
      CuteBarsRendererCall35 call = reinterpret_cast<CuteBarsRendererCall35>(taken[35]);
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
      CuteBarsRendererCall36 call = reinterpret_cast<CuteBarsRendererCall36>(taken[36]);
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
      CuteBarsRendererCall37 call = reinterpret_cast<CuteBarsRendererCall37>(taken[37]);
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
      CuteBarsRendererCall38 call = reinterpret_cast<CuteBarsRendererCall38>(taken[38]);
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
      CuteBarsRendererCall39 call = reinterpret_cast<CuteBarsRendererCall39>(taken[39]);
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
      CuteBarsRendererCall40 call = reinterpret_cast<CuteBarsRendererCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BarsRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12BarsRenderer10metaObjectEv(
    const BarsRenderer *self) {
  return self->metaObject();
}

//  void *BarsRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12BarsRenderer11qt_metacastEPKc(
    BarsRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int BarsRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12BarsRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    BarsRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString BarsRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12BarsRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BarsRenderer::tr(s, c, n));
}

//  BarsRenderer::BarsRenderer(QGraphsView *graph, bool clipPlotArea)
extern "C" Q_DECL_EXPORT
BarsRenderer *ritual_ZN12BarsRendererC1EP11QGraphsViewb(
    QGraphsView *graph,
    bool clipPlotArea) {
  return new CuteBarsRenderer(graph, clipPlotArea);
}

//  BarsRenderer::~BarsRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRendererD1Ev(BarsRenderer *self) {
  delete self;
}

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void BarsRenderer::paintSnapshot(const PaintSnapshot &snapshot,
//      QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer13paintSnapshotERK5QHashIP10QBarSeries5QListINS_13BarSeriesDataEEEP14QCanvasPainter(
    const BarsRenderer::PaintSnapshot *snapshot,
    QCanvasPainter *p) {
  BarsRenderer::paintSnapshot(*snapshot, p);
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  PaintSnapshot BarsRenderer::paintSnapshot() const
extern "C" Q_DECL_EXPORT
BarsRenderer::PaintSnapshot *ritual_ZNK12BarsRenderer13paintSnapshotEv(
    const BarsRenderer *self) {
  return new BarsRenderer::PaintSnapshot(self->paintSnapshot());
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

#if QT_CONFIG(graphs_2d_high_performance_backend)
//  void BarsRenderer::synchronizeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer15synchronizeDataEv(BarsRenderer *self) {
  self->synchronizeData();
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend)

//  void BarsRenderer::updateSeries(QBarSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer12updateSeriesEP10QBarSeries(
    BarsRenderer *self,
    QBarSeries *series) {
  self->updateSeries(series);
}

//  void BarsRenderer::seriesAboutToBeRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer22seriesAboutToBeRemovedEP15QAbstractSeries(
    BarsRenderer *self,
    QAbstractSeries *series) {
  self->seriesAboutToBeRemoved(series);
}

//  void BarsRenderer::afterUpdate(QList<QAbstractSeries *> &cleanupSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer11afterUpdateER5QListIP15QAbstractSeriesE(
    BarsRenderer *self,
    QList<QAbstractSeries *> *cleanupSeries) {
  self->afterUpdate(*cleanupSeries);
}

//  void BarsRenderer::afterPolish(QList<QAbstractSeries *> &cleanupSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer11afterPolishER5QListIP15QAbstractSeriesE(
    BarsRenderer *self,
    QList<QAbstractSeries *> *cleanupSeries) {
  self->afterPolish(*cleanupSeries);
}

//  bool BarsRenderer::handleHoverMove(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12BarsRenderer15handleHoverMoveEP11QHoverEvent(
    BarsRenderer *self,
    QHoverEvent *event) {
  return self->handleHoverMove(event);
}

//  QColor BarsRenderer::getSetColor(QBarSeries *series, QBarSet *set,
//      qsizetype barSerieIndex)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12BarsRenderer11getSetColorEP10QBarSeriesP7QBarSetx(
    BarsRenderer *self,
    QBarSeries *series,
    QBarSet *set,
    qsizetype barSerieIndex) {
  return new QColor(self->getSetColor(series, set, barSerieIndex));
}

//  QColor BarsRenderer::getSetSelectedColor(QBarSeries *series, QBarSet
//      *set)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12BarsRenderer19getSetSelectedColorEP10QBarSeriesP7QBarSet(
    BarsRenderer *self,
    QBarSeries *series,
    QBarSet *set) {
  return new QColor(self->getSetSelectedColor(series, set));
}

//  QColor BarsRenderer::getSetBorderColor(QBarSeries *series, QBarSet *set,
//      qsizetype barSerieIndex)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12BarsRenderer17getSetBorderColorEP10QBarSeriesP7QBarSetx(
    BarsRenderer *self,
    QBarSeries *series,
    QBarSet *set,
    qsizetype barSerieIndex) {
  return new QColor(self->getSetBorderColor(series, set, barSerieIndex));
}

//  qreal BarsRenderer::getSetBorderWidth(QBarSeries *series, QBarSet *set)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN12BarsRenderer17getSetBorderWidthEP10QBarSeriesP7QBarSet(
    BarsRenderer *self,
    QBarSeries *series,
    QBarSet *set) {
  return self->getSetBorderWidth(series, set);
}

//  QString BarsRenderer::generateLabelText(QBarSeries *series, qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12BarsRenderer17generateLabelTextEP10QBarSeriesd(
    BarsRenderer *self,
    QBarSeries *series,
    qreal value) {
  return new QString(self->generateLabelText(series, value));
}

//  void BarsRenderer::positionLabelItem(QBarSeries *series, QQuickText
//      *textItem, const BarSeriesData &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer17positionLabelItemEP10QBarSeriesP10QQuickTextRKNS_13BarSeriesDataE(
    BarsRenderer *self,
    QBarSeries *series,
    QQuickText *textItem,
    const BarsRenderer::BarSeriesData *d) {
  self->positionLabelItem(series, textItem, *d);
}

//  void BarsRenderer::onSingleTapped(QEventPoint eventPoint, Qt::MouseButton
//      button)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer14onSingleTappedE11QEventPointN2Qt11MouseButtonE(
    BarsRenderer *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->onSingleTapped(*eventPoint, button);
}

//  void BarsRenderer::onDoubleTapped(QEventPoint eventPoint, Qt::MouseButton
//      button)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer14onDoubleTappedE11QEventPointN2Qt11MouseButtonE(
    BarsRenderer *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->onDoubleTapped(*eventPoint, button);
}

//  void BarsRenderer::onPressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarsRenderer16onPressedChangedEv(BarsRenderer *self) {
  self->onPressedChanged();
}

//  a Python function taken by a CuteBarsRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BarsRenderer(
    BarsRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteBarsRenderer *>(self)->take(key, call);
}

//  a BarsRenderer::PaintSnapshot a ritual of BarsRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_BarsRenderer__BarsRenderer_PaintSnapshot(
    BarsRenderer::PaintSnapshot *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
