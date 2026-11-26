//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qlogvalueaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qlogvalueaxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qlogvalueaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/QAbstractAxis>
#include <QtGraphs/private/qabstractaxis_p.h>
#include <QtGraphs/QLogValueAxis>
#include <QtGraphs/private/qlogvalueaxis_p.h>
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

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 540, as _ZN20QLogValueAxisPrivateD1Ev
inline QLogValueAxisPrivate::~QLogValueAxisPrivate() {}

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 571, as _ZN20QLogValueAxisPrivate8setRangeEdd
inline void QLogValueAxisPrivate::setRange(qreal min, qreal max)
{
    Q_Q(QLogValueAxis);
    bool changed = false;

    if (qFuzzyCompare(min, 0)) {
        qCWarning(lcAxis2D, "min value cannot be zero.");
        return;
    }

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

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 542, as _ZN20QLogValueAxisPrivate6setMinERK8QVariant
inline void QLogValueAxisPrivate::setMin(const QVariant &min)
{
    Q_Q(QLogValueAxis);
    bool ok;
    qreal value = min.toReal(&ok);
    if (ok)
        q->setMin(value);
}

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 551, as _ZN20QLogValueAxisPrivate6setMaxERK8QVariant
inline void QLogValueAxisPrivate::setMax(const QVariant &max)
{
    Q_Q(QLogValueAxis);
    bool ok;
    qreal value = max.toReal(&ok);
    if (ok)
        q->setMax(value);
}

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 560, as _ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_
inline void QLogValueAxisPrivate::setRange(const QVariant &min, const QVariant &max)
{
    Q_Q(QLogValueAxis);
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

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 529, as _ZN20QLogValueAxisPrivateC1Ev
inline QLogValueAxisPrivate::QLogValueAxisPrivate()
    : m_min(0)
    , m_max(10)
    , m_base(10.0)
    , m_subTickCount(-1)
    , m_format()
    , m_postFormat(QLatin1StringView("%1"))
    , m_precision(6)
    , m_tickCount(-1)
{}

//  from ../qtgraphs/src/graphs2d/axis/logvalueaxis/qlogvalueaxis.cpp, line 609, as _ZN20QLogValueAxisPrivate20calculateVisualRangeEv
inline void QLogValueAxisPrivate::calculateVisualRange()
{
    Q_Q(QLogValueAxis);
    qreal logBase = log(m_base);
    qreal logMin = log(m_min) / logBase;
    qreal logMax = log(m_max) / logBase;

    qreal diff = logMax - logMin;

    qreal center = diff / 2.0f + logMin + m_pan;
    diff /= m_zoom;
    logMin = center - diff / 2.0f;
    logMax = center + diff / 2.0f;

    qreal min = pow(m_base, logMin);
    qreal max = pow(m_base, logMax);

    if (!qFuzzyCompare(m_visualMin, min)) {
        m_visualMin = min;
        emit q->visualMinChanged(min);
    }
    if (!qFuzzyCompare(m_visualMax, max)) {
        m_visualMax = max;
        emit q->visualMaxChanged(max);
    }

    int tickCount = qFloor(logMax) - qCeil(logMin) + 1;
    if (m_tickCount != tickCount) {
        m_tickCount = tickCount;
        emit q->tickCountChanged(tickCount);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QLogValueAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLogValueAxisPrivate : QLogValueAxisPrivate {
  using QLogValueAxisPrivate::setMin;
  using QLogValueAxisPrivate::setMax;
  using QLogValueAxisPrivate::setRange;
};

//  A QLogValueAxisPrivate that Python can take functions over in. Every QLogValueAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQLogValueAxisPrivateCall0)(const void *, int *);
typedef qreal (*CuteQLogValueAxisPrivateCall1)(const void *, int *);
typedef void (*CuteQLogValueAxisPrivateCall2)(const void *, qreal, qreal, int *);
typedef void (*CuteQLogValueAxisPrivateCall3)(const void *, const QVariant *, int *);
typedef void (*CuteQLogValueAxisPrivateCall4)(const void *, const QVariant *, int *);
typedef void (*CuteQLogValueAxisPrivateCall5)(const void *, const QVariant *, const QVariant *, int *);
class CuteQLogValueAxisPrivate : public QLogValueAxisPrivate {
public:
  using QLogValueAxisPrivate::QLogValueAxisPrivate;
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

  //  qreal QLogValueAxisPrivate::min()
  qreal min() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall0 call = reinterpret_cast<CuteQLogValueAxisPrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QLogValueAxisPrivate::min();
  }

  //  qreal QLogValueAxisPrivate::max()
  qreal max() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall1 call = reinterpret_cast<CuteQLogValueAxisPrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QLogValueAxisPrivate::max();
  }

  //  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall2 call = reinterpret_cast<CuteQLogValueAxisPrivateCall2>(taken[2]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setRange(min, max);
  }

  //  void QLogValueAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall3 call = reinterpret_cast<CuteQLogValueAxisPrivateCall3>(taken[3]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setMin(min);
  }

  //  void QLogValueAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall4 call = reinterpret_cast<CuteQLogValueAxisPrivateCall4>(taken[4]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setMax(max);
  }

  //  void QLogValueAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall5 call = reinterpret_cast<CuteQLogValueAxisPrivateCall5>(taken[5]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setRange(min, max);
  }
};

//  QLogValueAxisPrivate::QLogValueAxisPrivate()
extern "C" Q_DECL_EXPORT
QLogValueAxisPrivate *ritual_ZN20QLogValueAxisPrivateC1Ev() {
  return new CuteQLogValueAxisPrivate();
}

//  QLogValueAxisPrivate::~QLogValueAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivateD1Ev(QLogValueAxisPrivate *self) {
  delete self;
}

//  qreal QLogValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QLogValueAxisPrivate3minEv(QLogValueAxisPrivate *self) {
  return self->min();
}

//  qreal QLogValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QLogValueAxisPrivate3maxEv(QLogValueAxisPrivate *self) {
  return self->max();
}

//  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate8setRangeEdd(
    QLogValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QLogValueAxisPrivate::calculateVisualRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate20calculateVisualRangeEv(
    QLogValueAxisPrivate *self) {
  self->calculateVisualRange();
}

//  void QLogValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate6setMinERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QLogValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate6setMaxERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QLogValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_(
    QLogValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QLogValueAxis *QLogValueAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLogValueAxis *ritual_ZN20QLogValueAxisPrivate6q_funcEv(
    QLogValueAxisPrivate *self) {
  return self->q_func();
}

//  const QLogValueAxis *QLogValueAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLogValueAxis *ritual_ZNK20QLogValueAxisPrivate6q_funcEv(
    const QLogValueAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQLogValueAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLogValueAxisPrivate(
    QLogValueAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLogValueAxisPrivate *>(self)->take(key, call);
}

//  qreal QLogValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QLogValueAxisPrivate3minEv(QLogValueAxisPrivate *self) {
  return self->QLogValueAxisPrivate::min();
}

//  qreal QLogValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QLogValueAxisPrivate3maxEv(QLogValueAxisPrivate *self) {
  return self->QLogValueAxisPrivate::max();
}

//  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate8setRangeEdd(
    QLogValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QLogValueAxisPrivate::setRange(min, max);
}

//  void QLogValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate6setMinERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *min) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setMin(
      *min);
}

//  void QLogValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate6setMaxERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *max) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setMax(
      *max);
}

//  void QLogValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_(
    QLogValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setRange(
      *min,
      *max);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
