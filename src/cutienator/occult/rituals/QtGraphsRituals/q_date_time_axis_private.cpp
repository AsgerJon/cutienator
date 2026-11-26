//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qdatetimeaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qdatetimeaxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qdatetimeaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/QAbstractAxis>
#include <QtGraphs/private/qabstractaxis_p.h>
#include <QtGraphs/qdatetimeaxis.h>
#include <QtGraphs/private/qdatetimeaxis_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 697, as _ZN20QAbstractAxisPrivateC2Ev
inline QAbstractAxisPrivate::QAbstractAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 505, as _ZN20QDateTimeAxisPrivateD1Ev
inline QDateTimeAxisPrivate::~QDateTimeAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 507, as _ZN20QDateTimeAxisPrivate6setMinERK8QVariant
inline void QDateTimeAxisPrivate::setMin(const QVariant &min)
{
    Q_Q(QDateTimeAxis);
    if (min.canConvert<QDateTime>())
        q->setMin(min.toDateTime());
}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 514, as _ZN20QDateTimeAxisPrivate6setMaxERK8QVariant
inline void QDateTimeAxisPrivate::setMax(const QVariant &max)
{
    Q_Q(QDateTimeAxis);
    if (max.canConvert<QDateTime>())
        q->setMax(max.toDateTime());
}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 521, as _ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_
inline void QDateTimeAxisPrivate::setRange(const QVariant &min, const QVariant &max)
{
    Q_Q(QDateTimeAxis);
    if (min.canConvert<QDateTime>() && max.canConvert<QDateTime>())
        q->setRange(min.toDateTime(), max.toDateTime());
}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 528, as _ZN20QDateTimeAxisPrivate8setRangeEdd
inline void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
{
    Q_Q(QDateTimeAxis);

    bool changed = false;

    if (m_min != min) {
        m_min = min;
        changed = true;
        emit q->minChanged(QDateTime::fromMSecsSinceEpoch(min, QTimeZone::UTC));
    }

    if (m_max != max) {
        m_max = max;
        changed = true;
        emit q->maxChanged(QDateTime::fromMSecsSinceEpoch(max, QTimeZone::UTC));
    }

    if (changed) {
        calculateVisualRange();
        emit q->rangeChanged(min, max);
    }
}

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 699, as _ZN20QAbstractAxisPrivateD1Ev
inline QAbstractAxisPrivate::~QAbstractAxisPrivate()
{
    Q_Q(QAbstractAxis);
    if (m_graph)
        m_graph->removeAxis(q, true);
}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 503, as _ZN20QDateTimeAxisPrivateC1Ev
inline QDateTimeAxisPrivate::QDateTimeAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/datetimeaxis/qdatetimeaxis.cpp, line 552, as _ZN20QDateTimeAxisPrivate20calculateVisualRangeEv
inline void QDateTimeAxisPrivate::calculateVisualRange()
{
    Q_Q(QDateTimeAxis);
    qreal diff = m_max - m_min;
    qreal center = diff / 2.0f + m_min + m_pan;
    diff /= m_zoom;
    qreal max = center + diff / 2.0f;
    qreal min = center - diff / 2.0f;

    if (!QtPrivate::fuzzyCompare(m_visualMin, min)) {
        m_visualMin = min;
        emit q->visualMinChanged(QDateTime::fromMSecsSinceEpoch(min, m_timeZone));
    }

    if (!QtPrivate::fuzzyCompare(m_visualMax, max)) {
        m_visualMax = max;
        emit q->visualMaxChanged(QDateTime::fromMSecsSinceEpoch(max, m_timeZone));
    }
}
//  -----------------------------------------------------------------------

//  A QDateTimeAxisPrivate that Python can take functions over in. Every QDateTimeAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDateTimeAxisPrivateCall0)(const void *, const QVariant *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall2)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall3)(const void *, qreal, qreal, int *);
typedef qreal (*CuteQDateTimeAxisPrivateCall4)(const void *, int *);
typedef qreal (*CuteQDateTimeAxisPrivateCall5)(const void *, int *);
class CuteQDateTimeAxisPrivate : public QDateTimeAxisPrivate {
public:
  using QDateTimeAxisPrivate::QDateTimeAxisPrivate;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QDateTimeAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall0 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall0>(taken[0]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setMin(min);
  }

  //  void QDateTimeAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall1 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall1>(taken[1]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setMax(max);
  }

  //  void QDateTimeAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall2 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall2>(taken[2]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setRange(min, max);
  }

  //  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall3 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall3>(taken[3]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setRange(min, max);
  }

  //  qreal QDateTimeAxisPrivate::min()
  qreal min() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall4 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeAxisPrivate::min();
  }

  //  qreal QDateTimeAxisPrivate::max()
  qreal max() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall5 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeAxisPrivate::max();
  }
};

//  QDateTimeAxisPrivate::QDateTimeAxisPrivate()
extern "C" Q_DECL_EXPORT
QDateTimeAxisPrivate *ritual_ZN20QDateTimeAxisPrivateC1Ev() {
  return new CuteQDateTimeAxisPrivate();
}

//  QDateTimeAxisPrivate::~QDateTimeAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivateD1Ev(QDateTimeAxisPrivate *self) {
  delete self;
}

//  void QDateTimeAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate6setMinERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QDateTimeAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QDateTimeAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_(
    QDateTimeAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate8setRangeEdd(
    QDateTimeAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  qreal QDateTimeAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QDateTimeAxisPrivate3minEv(QDateTimeAxisPrivate *self) {
  return self->min();
}

//  qreal QDateTimeAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QDateTimeAxisPrivate3maxEv(QDateTimeAxisPrivate *self) {
  return self->max();
}

//  void QDateTimeAxisPrivate::calculateVisualRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate20calculateVisualRangeEv(
    QDateTimeAxisPrivate *self) {
  self->calculateVisualRange();
}

//  QDateTimeAxis *QDateTimeAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDateTimeAxis *ritual_ZN20QDateTimeAxisPrivate6q_funcEv(
    QDateTimeAxisPrivate *self) {
  return self->q_func();
}

//  const QDateTimeAxis *QDateTimeAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDateTimeAxis *ritual_ZNK20QDateTimeAxisPrivate6q_funcEv(
    const QDateTimeAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQDateTimeAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeAxisPrivate(
    QDateTimeAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeAxisPrivate *>(self)->take(key, call);
}

//  void QDateTimeAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate6setMinERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *min) {
  self->QDateTimeAxisPrivate::setMin(*min);
}

//  void QDateTimeAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *max) {
  self->QDateTimeAxisPrivate::setMax(*max);
}

//  void QDateTimeAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_(
    QDateTimeAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QDateTimeAxisPrivate::setRange(*min, *max);
}

//  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate8setRangeEdd(
    QDateTimeAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QDateTimeAxisPrivate::setRange(min, max);
}

//  qreal QDateTimeAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QDateTimeAxisPrivate3minEv(QDateTimeAxisPrivate *self) {
  return self->QDateTimeAxisPrivate::min();
}

//  qreal QDateTimeAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QDateTimeAxisPrivate3maxEv(QDateTimeAxisPrivate *self) {
  return self->QDateTimeAxisPrivate::max();
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
