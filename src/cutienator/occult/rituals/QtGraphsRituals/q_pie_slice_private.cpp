//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qpieslice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qpieslice.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qpieslice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/qpieseries.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtGraphs/private/qpieslice_p.h>
#if QT_CONFIG(graphs_2d_high_quality_backend)
#include <QtQuickShapes/private/qquickshape_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1384, as _ZN16QPieSlicePrivate13setPercentageEd
inline void QPieSlicePrivate::setPercentage(qreal percentage)
{
    Q_Q(QPieSlice);
    if (QtPrivate::fuzzyCompare(m_percentage, percentage))
        return;
    m_percentage = percentage;
    emit q->percentageChanged();
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1393, as _ZN16QPieSlicePrivate13setStartAngleEd
inline void QPieSlicePrivate::setStartAngle(qreal angle)
{
    Q_Q(QPieSlice);
    if (QtPrivate::fuzzyCompare(m_startAngle, angle))
        return;
    m_startAngle = angle;
    emit q->startAngleChanged();
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1402, as _ZN16QPieSlicePrivate12setAngleSpanEd
inline void QPieSlicePrivate::setAngleSpan(qreal span)
{
    Q_Q(QPieSlice);
    if (QtPrivate::fuzzyCompare(m_angleSpan, span))
        return;

    m_angleSpan = span;
    emit q->angleSpanChanged();
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1319, as _ZN16QPieSlicePrivate10updateDataEb
inline void QPieSlicePrivate::updateData(bool clearHidden)
{
    Q_Q(QPieSlice);
    // calculate sum of all slices
    qreal sum = 0;
    for (QPieSlice *s : std::as_const(m_subSlices))
        sum += s->value();

    Q_ASSERT(sum >= 0.0);

    if (!qFuzzyCompare(m_sum + 1, sum + 1)) {
        m_sum = sum;
        emit q->subSlicesSumChanged(m_sum);
    }
    // nothing to show..
    if (qFuzzyIsNull(m_sum))
        return;
    // update slice attributes
    for (QPieSlice *s : std::as_const(m_subSlices)) {
        QPieSlicePrivate *d = s->d_func();
        d->setPercentage(s->value() / m_sum);
        d->setAngleSpan(m_angleSpan * d->m_percentage);
    }
    if (!m_series)
        return;
    auto hideMode = m_series->angleSpanLabelVisibility();
    bool hideNextSmallSlice = false;
    for (QPieSlice *s : std::as_const(m_subSlices)) {
        QPieSlicePrivate *d = s->d_func();
        // Reset hidden status
        if (clearHidden) {
            d->m_hideLabel = false;
            d->setLabelVisible(true);
        }
        // Check if current slice is small, and if the previous slice was also small
        // Hide the label on this one if the mode matches
        if (d->m_angleSpan < m_series->angleSpanVisibleLimit()
            && ((!hideNextSmallSlice && hideMode == QPieSeries::LabelVisibility::Even)
                || (hideNextSmallSlice
                    && (hideMode == QPieSeries::LabelVisibility::Odd
                        || hideMode == QPieSeries::LabelVisibility::First))
                || hideMode == QPieSeries::LabelVisibility::None)) {
            d->setLabelVisible(false, true);
        }
        if (hideMode == QPieSeries::LabelVisibility::First) {
            // Hide every other small slice label after the first shown one
            hideNextSmallSlice = d->m_angleSpan < m_series->angleSpanVisibleLimit();
        } else {
            // Hide only every other odd/even small slice label
            hideNextSmallSlice = (!hideNextSmallSlice && d->m_angleSpan < m_series->angleSpanVisibleLimit());
        }
    }
    emit m_series->update();
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1374, as _ZN16QPieSlicePrivate12updateSeriesEP10QPieSeries
inline void QPieSlicePrivate::updateSeries(QPieSeries *series)
{
    m_series = series;

    for (QPieSlice *s : std::as_const(m_subSlices)) {
        QPieSlicePrivate *d = s->d_func();
        d->updateSeries(series);
    }
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1277, as _ZN16QPieSlicePrivate17handleSliceChangeEv
inline void QPieSlicePrivate::handleSliceChange()
{
    Q_Q(QPieSlice);

    QPieSlice *pSlice = qobject_cast<QPieSlice *>(q->sender());
    Q_ASSERT(m_subSlices.contains(pSlice));
    updateData();
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1412, as _ZN16QPieSlicePrivate15setLabelVisibleEbb
inline void QPieSlicePrivate::setLabelVisible(bool visible, bool forceHidden)
{
    if (m_hideLabel)
        return;

    m_hideLabel = forceHidden;
    m_isLabelVisible = (visible && !m_hideLabel);
    m_labelItem->setVisible(m_isLabelVisible);
#if QT_CONFIG(graphs_2d_high_quality_backend)
    if (m_labelPosition == QPieSlice::LabelPosition::Outside)
        m_labelShape->setVisible(m_isLabelVisible);
#endif
}

//  from ../qtgraphs/src/graphs2d/piechart/qpieslice.cpp, line 1426, as _ZN16QPieSlicePrivate16setLabelPositionEN9QPieSlice13LabelPositionE
inline void QPieSlicePrivate::setLabelPosition(QPieSlice::LabelPosition position)
{
    m_labelPosition = position;

    if (position == QPieSlice::LabelPosition::Outside) {
#if QT_CONFIG(graphs_2d_high_quality_backend)
        m_labelShape->setVisible(m_isLabelVisible);
#endif
        m_isLabelPathVisible = m_isLabelVisible;
        qreal radian = qDegreesToRadians(m_startAngle + (m_angleSpan * .5));
        QQuickText *labelItem = m_labelItem;
        qreal height = labelItem->height();
        qreal labelWidth = radian > M_PI ? -labelItem->width() : labelItem->width();
        if (labelWidth > 0)
            labelItem->setX(m_labelArm.x());
        else
            labelItem->setX(m_labelArm.x() + labelWidth);
        labelItem->setY(m_labelArm.y() - height);
        labelItem->setRotation(0);
    } else {
#if QT_CONFIG(graphs_2d_high_quality_backend)
        m_labelShape->setVisible(false);
#endif
        m_isLabelPathVisible = false;
        qreal centerX = (m_largeArc.x() + m_centerLine.x()) / 2.0;
        qreal centerY = (m_largeArc.y() + m_centerLine.y()) / 2.0;
        QQuickText *labelItem = m_labelItem;
        centerX -= labelItem->width() * .5;
        centerY -= labelItem->height() * .5;
        labelItem->setPosition(QPointF(centerX, centerY));

        if (position == QPieSlice::LabelPosition::InsideHorizontal) {
            labelItem->setRotation(0);
        } else if (position == QPieSlice::LabelPosition::InsideTangential) {
            labelItem->setRotation(m_startAngle + (m_angleSpan * .5));
        } else if (position == QPieSlice::LabelPosition::InsideNormal) {
            qreal angle = m_startAngle + (m_angleSpan * .5);
            if (angle > 180)
                angle += 90;
            else
                angle -= 90;
            labelItem->setRotation(angle);
        }
    }
}
//  -----------------------------------------------------------------------

//  QPieSlicePrivate *QPieSlicePrivate::get(QPieSlice *item)
extern "C" Q_DECL_EXPORT
QPieSlicePrivate *ritual_ZN16QPieSlicePrivate3getEP9QPieSlice(
    QPieSlice *item) {
  return QPieSlicePrivate::get(item);
}

//  const QPieSlicePrivate *QPieSlicePrivate::get(const QPieSlice *item)
extern "C" Q_DECL_EXPORT
const QPieSlicePrivate *ritual_ZN16QPieSlicePrivate3getEPK9QPieSlice(
    const QPieSlice *item) {
  return QPieSlicePrivate::get(item);
}

//  void QPieSlicePrivate::setPercentage(qreal percentage)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate13setPercentageEd(
    QPieSlicePrivate *self,
    qreal percentage) {
  self->setPercentage(percentage);
}

//  void QPieSlicePrivate::setStartAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate13setStartAngleEd(
    QPieSlicePrivate *self,
    qreal angle) {
  self->setStartAngle(angle);
}

//  void QPieSlicePrivate::setAngleSpan(qreal span)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate12setAngleSpanEd(
    QPieSlicePrivate *self,
    qreal span) {
  self->setAngleSpan(span);
}

//  void QPieSlicePrivate::updateData(bool clearHidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate10updateDataEb(
    QPieSlicePrivate *self,
    bool clearHidden) {
  self->updateData(clearHidden);
}

//  void QPieSlicePrivate::updateSeries(QPieSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate12updateSeriesEP10QPieSeries(
    QPieSlicePrivate *self,
    QPieSeries *series) {
  self->updateSeries(series);
}

//  void QPieSlicePrivate::handleSliceChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate17handleSliceChangeEv(
    QPieSlicePrivate *self) {
  self->handleSliceChange();
}

//  void QPieSlicePrivate::setLabelVisible(bool visible, bool forceHidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate15setLabelVisibleEbb(
    QPieSlicePrivate *self,
    bool visible,
    bool forceHidden) {
  self->setLabelVisible(visible, forceHidden);
}

//  void QPieSlicePrivate::setLabelPosition(QPieSlice::LabelPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate16setLabelPositionEN9QPieSlice13LabelPositionE(
    QPieSlicePrivate *self,
    QPieSlice::LabelPosition position) {
  self->setLabelPosition(position);
}

//  QPieSlice *QPieSlicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN16QPieSlicePrivate6q_funcEv(QPieSlicePrivate *self) {
  return self->q_func();
}

//  const QPieSlice *QPieSlicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieSlice *ritual_ZNK16QPieSlicePrivate6q_funcEv(
    const QPieSlicePrivate *self) {
  return self->q_func();
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
