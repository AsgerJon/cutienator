//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qvalueaxis_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qvalueaxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qvalueaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/QAbstractAxis>
#include <QtGraphs/private/qabstractaxis_p.h>
#include <QtGraphs/QValueAxis>
#include <QtGraphs/private/qvalueaxis_p.h>
#include <QtGraphs/private/charthelpers_p.h>
#include <QtCore/QtMath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 697, as _ZN20QAbstractAxisPrivateC2Ev
inline QAbstractAxisPrivate::QAbstractAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 527, as _ZN17QValueAxisPrivateD1Ev
inline QValueAxisPrivate::~QValueAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 558, as _ZN17QValueAxisPrivate8setRangeEdd
inline void QValueAxisPrivate::setRange(qreal min, qreal max)
{
    Q_Q(QValueAxis);
    bool changed = false;

    if (min > max) {
        qCWarning(lcAxis2D, "min value is higher than max vaue.");
        return;
    }

    if (!isValidValue(min, max)) {
        qCWarning(lcAxis2D, "attempting to set invalid range for value axis: [%f - %f]", min, max);
        return;
    }

    if (m_min != min) {
        m_min = min;
        changed = true;
        emit q->minChanged(min);
    }

    if (m_max != max) {
        m_max = max;
        changed = true;
        emit q->maxChanged(max);
    }

    if (changed) {
        calculateVisualRange();
        emit q->rangeChanged(min, max);
    }
}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 529, as _ZN17QValueAxisPrivate6setMinERK8QVariant
inline void QValueAxisPrivate::setMin(const QVariant &min)
{
    Q_Q(QValueAxis);
    bool ok;
    qreal value = min.toReal(&ok);
    if (ok)
        q->setMin(value);
}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 538, as _ZN17QValueAxisPrivate6setMaxERK8QVariant
inline void QValueAxisPrivate::setMax(const QVariant &max)
{
    Q_Q(QValueAxis);
    bool ok;
    qreal value = max.toReal(&ok);
    if (ok)
        q->setMax(value);
}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 547, as _ZN17QValueAxisPrivate8setRangeERK8QVariantS2_
inline void QValueAxisPrivate::setRange(const QVariant &min, const QVariant &max)
{
    Q_Q(QValueAxis);
    bool ok1;
    bool ok2;
    qreal value1 = min.toReal(&ok1);
    qreal value2 = max.toReal(&ok2);
    if (ok1 && ok2)
        q->setRange(value1, value2);
}

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 310, as _Z8lcAxis2Dv
inline const QLoggingCategory &lcAxis2D()
{
    static const QLoggingCategory category("qt.graphs2d.axis.properties");
    return category;
}

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 699, as _ZN20QAbstractAxisPrivateD1Ev
inline QAbstractAxisPrivate::~QAbstractAxisPrivate()
{
    Q_Q(QAbstractAxis);
    if (m_graph)
        m_graph->removeAxis(q, true);
}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 516, as _ZN17QValueAxisPrivateC1Ev
inline QValueAxisPrivate::QValueAxisPrivate()
    : m_min(0)
    , m_max(10)
    , m_subTickCount(0)
    , m_format()
    , m_postFormat(QLatin1StringView("%1"))
    , m_decimals(-1)
    , m_tickAnchor(0.0)
    , m_tickInterval(0.0)
{}

//  from ../qtgraphs/src/graphs2d/axis/valueaxis/qvalueaxis.cpp, line 591, as _ZN17QValueAxisPrivate20calculateVisualRangeEv
inline void QValueAxisPrivate::calculateVisualRange()
{
    Q_Q(QValueAxis);
    qreal diff = m_max - m_min;
    qreal center = diff / 2.0f + m_min + m_pan;
    diff /= m_zoom;
    qreal min = center - diff / 2.0f;
    qreal max = center + diff / 2.0f;
    if (!QtPrivate::fuzzyCompare(m_visualMin, min)) {
        m_visualMin = min;
        emit q->visualMinChanged(min);
    }
    if (!QtPrivate::fuzzyCompare(m_visualMax, max)) {
        m_visualMax = max;
        emit q->visualMaxChanged(max);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QValueAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQValueAxisPrivate : QValueAxisPrivate {
  using QValueAxisPrivate::setMin;
  using QValueAxisPrivate::setMax;
  using QValueAxisPrivate::setRange;
};

//  A QValueAxisPrivate that Python can take functions over in. Every QValueAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQValueAxisPrivateCall0)(const void *, int *);
typedef qreal (*CuteQValueAxisPrivateCall1)(const void *, int *);
typedef void (*CuteQValueAxisPrivateCall2)(const void *, qreal, qreal, int *);
typedef void (*CuteQValueAxisPrivateCall3)(const void *, const QVariant *, int *);
typedef void (*CuteQValueAxisPrivateCall4)(const void *, const QVariant *, int *);
typedef void (*CuteQValueAxisPrivateCall5)(const void *, const QVariant *, const QVariant *, int *);
class CuteQValueAxisPrivate : public QValueAxisPrivate {
public:
  using QValueAxisPrivate::QValueAxisPrivate;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  qreal QValueAxisPrivate::min()
  qreal min() override {
    if (taken[0]) {
      int handled = 0;
      CuteQValueAxisPrivateCall0 call = reinterpret_cast<CuteQValueAxisPrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::min();
  }

  //  qreal QValueAxisPrivate::max()
  qreal max() override {
    if (taken[1]) {
      int handled = 0;
      CuteQValueAxisPrivateCall1 call = reinterpret_cast<CuteQValueAxisPrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::max();
  }

  //  void QValueAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValueAxisPrivateCall2 call = reinterpret_cast<CuteQValueAxisPrivateCall2>(taken[2]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }

  //  void QValueAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[3]) {
      int handled = 0;
      CuteQValueAxisPrivateCall3 call = reinterpret_cast<CuteQValueAxisPrivateCall3>(taken[3]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMin(min);
  }

  //  void QValueAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQValueAxisPrivateCall4 call = reinterpret_cast<CuteQValueAxisPrivateCall4>(taken[4]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMax(max);
  }

  //  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
  //      &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValueAxisPrivateCall5 call = reinterpret_cast<CuteQValueAxisPrivateCall5>(taken[5]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }
};

//  QValueAxisPrivate::QValueAxisPrivate()
extern "C" Q_DECL_EXPORT
QValueAxisPrivate *ritual_ZN17QValueAxisPrivateC1Ev() {
  return new CuteQValueAxisPrivate();
}

//  QValueAxisPrivate::~QValueAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivateD1Ev(QValueAxisPrivate *self) {
  delete self;
}

//  qreal QValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate3minEv(QValueAxisPrivate *self) {
  return self->min();
}

//  qreal QValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate3maxEv(QValueAxisPrivate *self) {
  return self->max();
}

//  void QValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate8setRangeEdd(
    QValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QValueAxisPrivate::calculateVisualRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate20calculateVisualRangeEv(
    QValueAxisPrivate *self) {
  self->calculateVisualRange();
}

//  void QValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate6setMinERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate6setMaxERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_(
    QValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QValueAxis *QValueAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QValueAxis *ritual_ZN17QValueAxisPrivate6q_funcEv(QValueAxisPrivate *self) {
  return self->q_func();
}

//  const QValueAxis *QValueAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QValueAxis *ritual_ZNK17QValueAxisPrivate6q_funcEv(
    const QValueAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQValueAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValueAxisPrivate(
    QValueAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValueAxisPrivate *>(self)->take(key, call);
}

//  qreal QValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QValueAxisPrivate3minEv(QValueAxisPrivate *self) {
  return self->QValueAxisPrivate::min();
}

//  qreal QValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QValueAxisPrivate3maxEv(QValueAxisPrivate *self) {
  return self->QValueAxisPrivate::max();
}

//  void QValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate8setRangeEdd(
    QValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QValueAxisPrivate::setRange(min, max);
}

//  void QValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate6setMinERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *min) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setMin(
      *min);
}

//  void QValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate6setMaxERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *max) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setMax(
      *max);
}

//  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_(
    QValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setRange(
      *min,
      *max);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
