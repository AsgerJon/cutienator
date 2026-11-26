//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbarcategoryaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarcategoryaxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbarcategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/QAbstractAxis>
#include <QtGraphs/private/qabstractaxis_p.h>
#include <QtGraphs/QBarCategoryAxis>
#include <QtGraphs/private/qbarcategoryaxis_p.h>
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

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 503, as _ZN23QBarCategoryAxisPrivateD1Ev
inline QBarCategoryAxisPrivate::~QBarCategoryAxisPrivate()
{

}

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 518, as _ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_
inline void QBarCategoryAxisPrivate::setRange(const QVariant &min, const QVariant &max)
{
    QString value1 = min.toString();
    QString value2 = max.toString();
    setRange(value1, value2);
}

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 508, as _ZN23QBarCategoryAxisPrivate6setMinERK8QVariant
inline void QBarCategoryAxisPrivate::setMin(const QVariant &min)
{
    setRange(min, m_maxCategory);
}

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 513, as _ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant
inline void QBarCategoryAxisPrivate::setMax(const QVariant &max)
{
    setRange(m_minCategory, max);
}

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 525, as _ZN23QBarCategoryAxisPrivate8setRangeEdd
inline void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
{
    Q_Q(QBarCategoryAxis);

    bool categoryChanged = false;
    bool changed = false;

    if (min > max) {
        qCWarning(lcAxis2D, "QBarCategoryAxis::setRange. Tried to use invalid values, min > max");
        return;
    }

    if (!qFuzzyIsNull(m_min - min)) {
        m_min = min;
        changed = true;

        int imin = m_min + 0.5;
        if (imin >= 0 && imin < m_categories.size()) {
            QString minCategory = m_categories.at(imin);
            if (m_minCategory != minCategory && !minCategory.isEmpty()) {
                m_minCategory = minCategory;
                categoryChanged = true;
                emit q->minChanged(minCategory);
            }
        }

    }

    if (!qFuzzyIsNull(m_max - max)) {
        m_max = max;
        changed = true;

        int imax = m_max - 0.5;
        if (imax >= 0 && imax < m_categories.size()) {
            QString maxCategory = m_categories.at(imax);
            if (m_maxCategory != maxCategory && !maxCategory.isEmpty()) {
                m_maxCategory = maxCategory;
                categoryChanged = true;
                emit q->maxChanged(maxCategory);
            }
        }
    }

    if (categoryChanged){
        emit q->categoryRangeChanged(m_minCategory, m_maxCategory);
    }

    if (changed) {
        emit q->rangeChanged(m_min, m_max);
    }
}

//  from ../qtgraphs/src/graphs2d/axis/qabstractaxis.cpp, line 310, as _Z8lcAxis2Dv
inline const QLoggingCategory &lcAxis2D()
{
    static const QLoggingCategory category("qt.graphs2d.axis.properties");
    return category;
}

//  from ../qtgraphs/src/graphs2d/axis/barcategoryaxis/qbarcategoryaxis.cpp, line 577, as _ZN23QBarCategoryAxisPrivate8setRangeERK7QStringS2_
inline void  QBarCategoryAxisPrivate::setRange(const QString &minCategory, const QString &maxCategory)
{
    Q_Q(QBarCategoryAxis);
    bool changed = false;

    //special case in case or clearing all categories
    if (minCategory.isNull() && maxCategory.isNull()) {
        m_minCategory = minCategory;
        m_maxCategory = maxCategory;
        m_min = 0;
        m_max = 0;
        m_count = 0;
        emit q->minChanged(minCategory);
        emit q->maxChanged(maxCategory);
        emit q->categoryRangeChanged(m_minCategory, m_maxCategory);
        emit q->rangeChanged(m_min, m_max);
        return;
    }

    if (m_categories.indexOf(maxCategory) < m_categories.indexOf(minCategory))
        return;

    if (!minCategory.isNull() && (m_minCategory != minCategory || m_minCategory.isNull())
            && m_categories.contains(minCategory)) {
        m_minCategory = minCategory;
        m_min = m_categories.indexOf(m_minCategory) - 0.5;
        changed = true;
        emit q->minChanged(minCategory);
    }

    if (!maxCategory.isNull() && (m_maxCategory != maxCategory || m_maxCategory.isNull())
            && m_categories.contains(maxCategory)) {
        m_maxCategory = maxCategory;
        m_max = m_categories.indexOf(m_maxCategory) + 0.5;
        changed = true;
        emit q->maxChanged(maxCategory);
    }

    if (changed) {
        m_count = m_max - m_min;
        emit q->categoryRangeChanged(m_minCategory, m_maxCategory);
        emit q->rangeChanged(m_min, m_max);
    }
}
//  -----------------------------------------------------------------------

//  A QBarCategoryAxisPrivate that Python can take functions over in. Every QBarCategoryAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBarCategoryAxisPrivateCall0)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall1)(const void *, const QVariant *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall2)(const void *, const QVariant *, int *);
typedef qreal (*CuteQBarCategoryAxisPrivateCall3)(const void *, int *);
typedef qreal (*CuteQBarCategoryAxisPrivateCall4)(const void *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall5)(const void *, qreal, qreal, int *);
class CuteQBarCategoryAxisPrivate : public QBarCategoryAxisPrivate {
public:
  using QBarCategoryAxisPrivate::QBarCategoryAxisPrivate;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall0 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall0>(taken[0]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setRange(min, max);
  }

  //  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall1 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall1>(taken[1]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setMin(min);
  }

  //  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall2 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall2>(taken[2]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setMax(max);
  }

  //  qreal QBarCategoryAxisPrivate::min()
  qreal min() override {
    if (taken[3]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall3 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QBarCategoryAxisPrivate::min();
  }

  //  qreal QBarCategoryAxisPrivate::max()
  qreal max() override {
    if (taken[4]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall4 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QBarCategoryAxisPrivate::max();
  }

  //  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall5 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall5>(taken[5]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setRange(min, max);
  }
};

//  QBarCategoryAxisPrivate::~QBarCategoryAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivateD1Ev(QBarCategoryAxisPrivate *self) {
  delete self;
}

//  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_(
    QBarCategoryAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  qreal QBarCategoryAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QBarCategoryAxisPrivate3minEv(
    QBarCategoryAxisPrivate *self) {
  return self->min();
}

//  qreal QBarCategoryAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QBarCategoryAxisPrivate3maxEv(
    QBarCategoryAxisPrivate *self) {
  return self->max();
}

//  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeEdd(
    QBarCategoryAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QBarCategoryAxisPrivate::setRange(const QString &minCategory, const
//      QString &maxCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeERK7QStringS2_(
    QBarCategoryAxisPrivate *self,
    const QString *minCategory,
    const QString *maxCategory) {
  self->setRange(*minCategory, *maxCategory);
}

//  QBarCategoryAxis *QBarCategoryAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarCategoryAxis *ritual_ZN23QBarCategoryAxisPrivate6q_funcEv(
    QBarCategoryAxisPrivate *self) {
  return self->q_func();
}

//  const QBarCategoryAxis *QBarCategoryAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarCategoryAxis *ritual_ZNK23QBarCategoryAxisPrivate6q_funcEv(
    const QBarCategoryAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBarCategoryAxisPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarCategoryAxisPrivate(
    QBarCategoryAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarCategoryAxisPrivate *>(self)->take(key, call);
}

//  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_(
    QBarCategoryAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QBarCategoryAxisPrivate::setRange(*min, *max);
}

//  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *min) {
  self->QBarCategoryAxisPrivate::setMin(*min);
}

//  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *max) {
  self->QBarCategoryAxisPrivate::setMax(*max);
}

//  qreal QBarCategoryAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN23QBarCategoryAxisPrivate3minEv(
    QBarCategoryAxisPrivate *self) {
  return self->QBarCategoryAxisPrivate::min();
}

//  qreal QBarCategoryAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN23QBarCategoryAxisPrivate3maxEv(
    QBarCategoryAxisPrivate *self) {
  return self->QBarCategoryAxisPrivate::max();
}

//  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate8setRangeEdd(
    QBarCategoryAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QBarCategoryAxisPrivate::setRange(min, max);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
