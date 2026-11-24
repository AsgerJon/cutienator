//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qabstractaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstractaxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qabstractaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/QAbstractAxis>
#include <QtGraphs/private/qabstractaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 699, as _ZN20QAbstractAxisPrivateD1Ev
inline QAbstractAxisPrivate::~QAbstractAxisPrivate()
{
    Q_Q(QAbstractAxis);
    if (m_graph)
        m_graph->removeAxis(q, true);
}

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 714, as _ZN20QAbstractAxisPrivate18handleRangeChangedEdd
inline void QAbstractAxisPrivate::handleRangeChanged(qreal min, qreal max)
{
    setRange(min,max);
}
//  -----------------------------------------------------------------------

//  A QAbstractAxisPrivate that Python can take functions over in. Every QAbstractAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractAxisPrivateCall0)(const void *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall2)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall3)(const void *, qreal, qreal, int *);
typedef qreal (*CuteQAbstractAxisPrivateCall4)(const void *, int *);
typedef qreal (*CuteQAbstractAxisPrivateCall5)(const void *, int *);
class CuteQAbstractAxisPrivate : public QAbstractAxisPrivate {
public:
  using QAbstractAxisPrivate::QAbstractAxisPrivate;
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

  //  void QAbstractAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall0 call = reinterpret_cast<CuteQAbstractAxisPrivateCall0>(taken[0]);
      call(this, &min, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall1 call = reinterpret_cast<CuteQAbstractAxisPrivateCall1>(taken[1]);
      call(this, &max, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall2 call = reinterpret_cast<CuteQAbstractAxisPrivateCall2>(taken[2]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall3 call = reinterpret_cast<CuteQAbstractAxisPrivateCall3>(taken[3]);
      call(this, min, max, &handled);
      if (handled) return;
    }
  }

  //  qreal QAbstractAxisPrivate::min()
  qreal min() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall4 call = reinterpret_cast<CuteQAbstractAxisPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qreal QAbstractAxisPrivate::max()
  qreal max() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall5 call = reinterpret_cast<CuteQAbstractAxisPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QAbstractAxisPrivate::~QAbstractAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivateD1Ev(QAbstractAxisPrivate *self) {
  delete self;
}

//  void QAbstractAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate6setMinERK8QVariant(
    QAbstractAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QAbstractAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate6setMaxERK8QVariant(
    QAbstractAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QAbstractAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_(
    QAbstractAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate8setRangeEdd(
    QAbstractAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  qreal QAbstractAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QAbstractAxisPrivate3minEv(QAbstractAxisPrivate *self) {
  return self->min();
}

//  qreal QAbstractAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QAbstractAxisPrivate3maxEv(QAbstractAxisPrivate *self) {
  return self->max();
}

//  void QAbstractAxisPrivate::handleRangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate18handleRangeChangedEdd(
    QAbstractAxisPrivate *self,
    qreal min,
    qreal max) {
  self->handleRangeChanged(min, max);
}

//  QAbstractAxis *QAbstractAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20QAbstractAxisPrivate6q_funcEv(
    QAbstractAxisPrivate *self) {
  return self->q_func();
}

//  const QAbstractAxis *QAbstractAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractAxis *ritual_ZNK20QAbstractAxisPrivate6q_funcEv(
    const QAbstractAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQAbstractAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAxisPrivate(
    QAbstractAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAxisPrivate *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
