//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qsplinecontrolanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qsplinecontrolanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qxyseriesanimation_p.h>
#include <QtCore/QPointF>
#include <QtGraphs/QSplineSeries>
#include <QtGraphs/private/qsplinecontrolanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/animation/qxyseriesanimation.cpp, line 25, as _ZN18QXYSeriesAnimationC2EP7QObject
inline QXYSeriesAnimation::QXYSeriesAnimation(QObject *parent)
    : QGraphAnimation(parent)
{}

//  from ../qtgraphs/src/graphs2d/animation/qxyseriesanimation.cpp, line 29, as _ZN18QXYSeriesAnimationD2Ev
inline QXYSeriesAnimation::~QXYSeriesAnimation() {}

//  from ../qtgraphs/src/graphs2d/animation/qsplinecontrolanimation.cpp, line 44, as _ZN23QSplineControlAnimation13animationTypeEv
inline QGraphAnimation::GraphAnimationType QSplineControlAnimation::animationType()
{
    return QGraphAnimation::GraphAnimationType::ControlPoint;
}

//  from ../qtgraphs/src/graphs2d/animation/qsplinecontrolanimation.cpp, line 49, as _ZN23QSplineControlAnimation17setAnimatingValueERK8QVariantS2_
inline void QSplineControlAnimation::setAnimatingValue(const QVariant &start, const QVariant &end)
{
    setStartValue(start);
    setEndValue(end);
}

//  from ../qtgraphs/src/graphs2d/animation/qsplinecontrolanimation.cpp, line 55, as _ZNK23QSplineControlAnimation12interpolatedERK8QVariantS2_d
inline QVariant QSplineControlAnimation::interpolated(const QVariant &start,
                                               const QVariant &end,
                                               qreal progress) const
{
    auto startList = qvariant_cast<QList<QPointF>>(start);
    auto endList = qvariant_cast<QList<QPointF>>(end);
    auto interpolateList = QList<QPointF>();

    for (int i = 0; i < qMin(startList.size(), endList.size()); ++i) {
        interpolateList.push_back(
            {qreal(startList[i].x() * (1.0 - progress) + endList[i].x() * progress),
             qreal(startList[i].y() * (1.0 - progress) + endList[i].y() * progress)});
    }

    return QVariant::fromValue(interpolateList);
}
//  -----------------------------------------------------------------------

//  A QSplineControlAnimation that Python can take functions over in. Every QSplineControlAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSplineControlAnimationCall0)(const void *, int *);
typedef void (*CuteQSplineControlAnimationCall1)(const void *, const QVariant *, const QVariant *, int *);
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQSplineControlAnimationCall2)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
typedef void (*CuteQSplineControlAnimationCall3)(const void *, int *);
typedef void (*CuteQSplineControlAnimationCall4)(const void *, int *);
typedef void (*CuteQSplineControlAnimationCall5)(const void *, const QVariant *, int *);
#if QT_CONFIG(animation)
typedef int (*CuteQSplineControlAnimationCall6)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQSplineControlAnimationCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQSplineControlAnimationCall8)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSplineControlAnimationCall9)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSplineControlAnimationCall10)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSplineControlAnimationCall11)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplineControlAnimationCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineControlAnimationCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineControlAnimationCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineControlAnimationCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineControlAnimationCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineControlAnimationCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSplineControlAnimation : public QSplineControlAnimation {
public:
  using QSplineControlAnimation::QSplineControlAnimation;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QGraphAnimation13animationTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation17setAnimatingValueERK8QVariantS2_")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN15QGraphAnimation7animateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation3endEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation12valueUpdatedERK8QVariant")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  GraphAnimationType QSplineControlAnimation::animationType()
  QGraphAnimation::GraphAnimationType animationType() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSplineControlAnimationCall0 call = reinterpret_cast<CuteQSplineControlAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGraphAnimation::GraphAnimationType>(given);
    }
    return QSplineControlAnimation::animationType();
  }

  //  void QSplineControlAnimation::setAnimatingValue(const QVariant
  //      &start, const QVariant &end)
  void setAnimatingValue(
      const QVariant &start,
      const QVariant &end) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplineControlAnimationCall1 call = reinterpret_cast<CuteQSplineControlAnimationCall1>(taken[1]);
      call(this, &start, &end, &handled);
      if (handled) return;
    }
    QSplineControlAnimation::setAnimatingValue(start, end);
  }

#if QT_CONFIG(animation)
  //  QVariant QSplineControlAnimation::interpolated(const QVariant &start,
  //      const QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplineControlAnimationCall2 call = reinterpret_cast<CuteQSplineControlAnimationCall2>(taken[2]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return QSplineControlAnimation::interpolated(start, end, progress);
  }
#endif  // QT_CONFIG(animation)

  //  void QSplineControlAnimation::animate()
  void animate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplineControlAnimationCall3 call = reinterpret_cast<CuteQSplineControlAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSplineControlAnimation::animate();
  }

  //  void QSplineControlAnimation::end()
  void end() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplineControlAnimationCall4 call = reinterpret_cast<CuteQSplineControlAnimationCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSplineControlAnimation::end();
  }

  //  void QSplineControlAnimation::valueUpdated(const QVariant &value)
  void valueUpdated(const QVariant &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplineControlAnimationCall5 call = reinterpret_cast<CuteQSplineControlAnimationCall5>(taken[5]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QSplineControlAnimation::valueUpdated(value);
  }

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplineControlAnimationCall6 call = reinterpret_cast<CuteQSplineControlAnimationCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QVariantAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplineControlAnimationCall7 call = reinterpret_cast<CuteQSplineControlAnimationCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplineControlAnimationCall8 call = reinterpret_cast<CuteQSplineControlAnimationCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplineControlAnimationCall9 call = reinterpret_cast<CuteQSplineControlAnimationCall9>(taken[9]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QVariantAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplineControlAnimationCall10 call = reinterpret_cast<CuteQSplineControlAnimationCall10>(taken[10]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplineControlAnimationCall11 call = reinterpret_cast<CuteQSplineControlAnimationCall11>(taken[11]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSplineControlAnimationCall12 call = reinterpret_cast<CuteQSplineControlAnimationCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSplineControlAnimationCall13 call = reinterpret_cast<CuteQSplineControlAnimationCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSplineControlAnimationCall14 call = reinterpret_cast<CuteQSplineControlAnimationCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSplineControlAnimationCall15 call = reinterpret_cast<CuteQSplineControlAnimationCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSplineControlAnimationCall16 call = reinterpret_cast<CuteQSplineControlAnimationCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSplineControlAnimationCall17 call = reinterpret_cast<CuteQSplineControlAnimationCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSplineControlAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QSplineControlAnimation10metaObjectEv(
    const QSplineControlAnimation *self) {
  return self->metaObject();
}

//  void *QSplineControlAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QSplineControlAnimation11qt_metacastEPKc(
    QSplineControlAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSplineControlAnimation::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QSplineControlAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QSplineControlAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSplineControlAnimation::~QSplineControlAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSplineControlAnimationD1Ev(QSplineControlAnimation *self) {
  delete self;
}

//  GraphAnimationType QSplineControlAnimation::animationType()
extern "C" Q_DECL_EXPORT
QGraphAnimation::GraphAnimationType ritual_ZN23QSplineControlAnimation13animationTypeEv(
    QSplineControlAnimation *self) {
  return self->animationType();
}

//  void QSplineControlAnimation::setAnimatingValue(const QVariant &start,
//      const QVariant &end)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSplineControlAnimation17setAnimatingValueERK8QVariantS2_(
    QSplineControlAnimation *self,
    const QVariant *start,
    const QVariant *end) {
  self->setAnimatingValue(*start, *end);
}

//  QVariant QSplineControlAnimation::interpolated(const QVariant &start,
//      const QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QSplineControlAnimation12interpolatedERK8QVariantS2_d(
    const QSplineControlAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(self->interpolated(*start, *end, progress));
}

//  void QSplineControlAnimation::animate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSplineControlAnimation7animateEv(
    QSplineControlAnimation *self) {
  self->animate();
}

//  void QSplineControlAnimation::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSplineControlAnimation3endEv(
    QSplineControlAnimation *self) {
  self->end();
}

//  void QSplineControlAnimation::valueUpdated(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSplineControlAnimation12valueUpdatedERK8QVariant(
    QSplineControlAnimation *self,
    const QVariant *value) {
  self->valueUpdated(*value);
}

//  a Python function taken by a CuteQSplineControlAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplineControlAnimation(
    QSplineControlAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSplineControlAnimation *>(self)->take(key, call);
}

//  GraphAnimationType QSplineControlAnimation::animationType()
extern "C" Q_DECL_EXPORT
QGraphAnimation::GraphAnimationType ritual_own_ZN23QSplineControlAnimation13animationTypeEv(
    QSplineControlAnimation *self) {
  return self->QSplineControlAnimation::animationType();
}

//  void QSplineControlAnimation::setAnimatingValue(const QVariant &start,
//      const QVariant &end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSplineControlAnimation17setAnimatingValueERK8QVariantS2_(
    QSplineControlAnimation *self,
    const QVariant *start,
    const QVariant *end) {
  self->QSplineControlAnimation::setAnimatingValue(*start, *end);
}

//  QVariant QSplineControlAnimation::interpolated(const QVariant &start,
//      const QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QSplineControlAnimation12interpolatedERK8QVariantS2_d(
    const QSplineControlAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(
      self->QSplineControlAnimation::interpolated(
          *start,
          *end,
          progress));
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_spline))
