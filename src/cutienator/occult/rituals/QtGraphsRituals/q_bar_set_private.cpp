//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbarset_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarset.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbarset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/qbarset.h>
#include <private/qbarset_p.h>
#include <private/charthelpers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 908, as _ZN14QBarSetPrivate6appendE7QPointF
inline void QBarSetPrivate::append(QPointF value)
{
    if (isValidValue(value)) {
        Q_Q(QBarSet);
        m_values.append(value);
        emit q->valueAdded(m_values.size() - 1, 1);
    }
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 917, as _ZN14QBarSetPrivate6appendERK5QListI7QPointFE
inline void QBarSetPrivate::append(const QList<QPointF> &values)
{
    qsizetype originalIndex = m_values.size();
    for (const auto &value : values) {
        if (isValidValue(value))
            m_values.append(value);
    }
    Q_Q(QBarSet);
    emit q->valueAdded(originalIndex, values.size());
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 942, as _ZN14QBarSetPrivate6insertExd
inline void QBarSetPrivate::insert(qsizetype index, qreal value)
{
    m_values.insert(index, QPointF(index, value));
    Q_Q(QBarSet);
    emit q->valueAdded(index, 1);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 949, as _ZN14QBarSetPrivate6insertEx7QPointF
inline void QBarSetPrivate::insert(qsizetype index, QPointF value)
{
    m_values.insert(index, value);
    Q_Q(QBarSet);
    emit q->valueAdded(index, 1);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 956, as _ZN14QBarSetPrivate6removeExx
inline qsizetype QBarSetPrivate::remove(qsizetype index, qsizetype count)
{
    qsizetype removeCount = count;

    if ((index < 0) || (m_values.size() == 0))
        return 0; // Invalid index or not values in list, remove nothing.
    else if ((index + count) > m_values.size())
        removeCount = m_values.size() - index; // Trying to remove more items than list has. Limit amount to be removed.

    int c = 0;
    while (c < removeCount) {
        m_values.removeAt(index);
        c++;
    }

    bool callSignal = false;
    if (!m_selectedBars.empty()) {
        QSet<qsizetype> selectedAfterRemoving;

        for (const qsizetype &selectedBarIndex : std::as_const(m_selectedBars)) {
            if (selectedBarIndex < index) {
                selectedAfterRemoving << selectedBarIndex;
            } else if (selectedBarIndex >= index + removeCount) {
                selectedAfterRemoving << selectedBarIndex - removeCount;
                callSignal = true;
            } else {
                callSignal = true;
            }
        }

        m_selectedBars = selectedAfterRemoving;
    }
    Q_Q(QBarSet);
    emit q->valueRemoved(index, removeCount);
    if (callSignal)
        emit q->selectedBarsChanged(q->selectedBars());

    return removeCount;
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 996, as _ZN14QBarSetPrivate7replaceExd
inline void QBarSetPrivate::replace(qsizetype index, qreal value)
{
    if (index < 0 || index >= m_values.size())
        return;

    m_values.replace(index, QPointF(index, value));
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 1004, as _ZNK14QBarSetPrivate3posEx
inline qreal QBarSetPrivate::pos(qsizetype index) const
{
    if (index < 0 || index >= m_values.size())
        return 0;
    return m_values.at(index).x();
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 1011, as _ZNK14QBarSetPrivate5valueEx
inline qreal QBarSetPrivate::value(qsizetype index) const
{
    if (index < 0 || index >= m_values.size())
        return 0;
    return m_values.at(index).y();
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 1018, as _ZN14QBarSetPrivate14setBarSelectedExbRb
inline void QBarSetPrivate::setBarSelected(qsizetype index, bool selected, bool &callSignal)
{
    if (index < 0 || index > m_values.size() - 1)
        return;

    if (selected) {
        if (!isBarSelected(index)) {
            m_selectedBars << index;
            callSignal = true;
        }
    } else {
        if (isBarSelected(index)) {
            m_selectedBars.remove(index);
            callSignal = true;
        }
    }

    if (callSignal)
        setVisualsDirty(true);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarset.cpp, line 1039, as _ZNK14QBarSetPrivate13isBarSelectedEx
inline bool QBarSetPrivate::isBarSelected(qsizetype index) const
{
    return m_selectedBars.contains(index);
}
//  -----------------------------------------------------------------------

//  QBarSet *QBarSetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN14QBarSetPrivate6q_funcEv(QBarSetPrivate *self) {
  return self->q_func();
}

//  const QBarSet *QBarSetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarSet *ritual_ZNK14QBarSetPrivate6q_funcEv(
    const QBarSetPrivate *self) {
  return self->q_func();
}

//  void QBarSetPrivate::append(QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6appendE7QPointF(
    QBarSetPrivate *self,
    const QPointF *value) {
  self->append(*value);
}

//  void QBarSetPrivate::append(const QList<QPointF> &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6appendERK5QListI7QPointFE(
    QBarSetPrivate *self,
    const QList<QPointF> *values) {
  self->append(*values);
}

//  void QBarSetPrivate::insert(qsizetype index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6insertExd(
    QBarSetPrivate *self,
    qsizetype index,
    qreal value) {
  self->insert(index, value);
}

//  void QBarSetPrivate::insert(qsizetype index, QPointF value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate6insertEx7QPointF(
    QBarSetPrivate *self,
    qsizetype index,
    const QPointF *value) {
  self->insert(index, *value);
}

//  qsizetype QBarSetPrivate::remove(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QBarSetPrivate6removeExx(
    QBarSetPrivate *self,
    qsizetype index,
    qsizetype count) {
  return self->remove(index, count);
}

//  void QBarSetPrivate::replace(qsizetype index, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate7replaceExd(
    QBarSetPrivate *self,
    qsizetype index,
    qreal value) {
  self->replace(index, value);
}

//  qreal QBarSetPrivate::pos(qsizetype index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QBarSetPrivate3posEx(
    const QBarSetPrivate *self,
    qsizetype index) {
  return self->pos(index);
}

//  qreal QBarSetPrivate::value(qsizetype index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QBarSetPrivate5valueEx(
    const QBarSetPrivate *self,
    qsizetype index) {
  return self->value(index);
}

//  void QBarSetPrivate::setVisualsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate15setVisualsDirtyEb(
    QBarSetPrivate *self,
    bool dirty) {
  self->setVisualsDirty(dirty);
}

//  bool QBarSetPrivate::visualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate12visualsDirtyEv(const QBarSetPrivate *self) {
  return self->visualsDirty();
}

//  void QBarSetPrivate::setLabelsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate14setLabelsDirtyEb(
    QBarSetPrivate *self,
    bool dirty) {
  self->setLabelsDirty(dirty);
}

//  bool QBarSetPrivate::labelsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate11labelsDirtyEv(const QBarSetPrivate *self) {
  return self->labelsDirty();
}

//  void QBarSetPrivate::setBarSelected(qsizetype index, bool selected, bool
//      &callSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBarSetPrivate14setBarSelectedExbRb(
    QBarSetPrivate *self,
    qsizetype index,
    bool selected,
    bool *callSignal) {
  self->setBarSelected(index, selected, *callSignal);
}

//  bool QBarSetPrivate::isBarSelected(qsizetype index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QBarSetPrivate13isBarSelectedEx(
    const QBarSetPrivate *self,
    qsizetype index) {
  return self->isBarSelected(index);
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
