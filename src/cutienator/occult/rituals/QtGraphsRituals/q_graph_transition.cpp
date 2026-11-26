//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphtransition_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <QtGraphs/qgraphsglobal.h>
#include "QtGraphs/QXYSeries"
#include <QtGraphs/private/qgraphtransition_p.h>
#if QT_CONFIG(graphs_2d_spline)
#include <QtGraphs/private/qsplinecontrolanimation_p.h>
#endif
#include <QtGraphs/private/qxyseriesanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 168, as _ZN16QGraphTransition10classBeginEv
inline void QGraphTransition::classBegin() {}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 64, as _ZN16QGraphTransitionD0Ev
inline QGraphTransition::~QGraphTransition() {}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 107, as _ZN16QGraphTransition10initializeEv
inline void QGraphTransition::initialize()
{
    auto series = qobject_cast<QXYSeries *>(parent());

    if (!series || m_initialized)
        return;

    const auto &animationChildren = m_animationGroup.children();
    for (qsizetype i = 0; i < animationChildren.size(); ++i) {
        auto childAnimation = qobject_cast<QXYSeriesAnimation *>(animationChildren[i]);

        //GraphPointAnimation needs to be the first for the transition to work
        if (childAnimation->animationType() == QGraphAnimation::GraphAnimationType::GraphPoint
            && i != 0)
            return;
    }

    m_initialized = true;
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 127, as _ZN16QGraphTransition4stopEv
inline void QGraphTransition::stop()
{
    m_animationGroup.stop();

    for (auto child : m_animationGroup.children()) {
        auto childAnimation = qobject_cast<QXYSeriesAnimation *>(child);
        childAnimation->end();
    }
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 137, as _ZN16QGraphTransition11initializedEv
inline bool QGraphTransition::initialized()
{
    return m_initialized;
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 142, as _ZN16QGraphTransition8containsEN15QGraphAnimation18GraphAnimationTypeE
inline bool QGraphTransition::contains(QGraphAnimation::GraphAnimationType type)
{
    for (const auto anim : std::as_const(m_animations)) {
        if (anim->animationType() == type)
            return true;
    }

    return false;
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphtransition.cpp, line 181, as _ZN16QGraphTransition5clearEP16QQmlListPropertyI7QObjectE
inline void QGraphTransition::clear(QQmlListProperty<QObject> *)
{
    Q_UNIMPLEMENTED();
}
//  -----------------------------------------------------------------------

//  Only a class built on QGraphTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphTransition : QGraphTransition {
  using QGraphTransition::classBegin;
};

//  A QGraphTransition that Python can take functions over in. Every QGraphTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphTransitionCall0)(const void *, int *);
typedef void (*CuteQGraphTransitionCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphTransition : public QGraphTransition {
public:
  using QGraphTransition::QGraphTransition;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGraphTransition::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphTransitionCall0 call = reinterpret_cast<CuteQGraphTransitionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphTransition::classBegin();
  }

  //  void QGraphTransition::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphTransitionCall1 call = reinterpret_cast<CuteQGraphTransitionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphTransition::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphTransitionCall2 call = reinterpret_cast<CuteQGraphTransitionCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphTransitionCall3 call = reinterpret_cast<CuteQGraphTransitionCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphTransitionCall4 call = reinterpret_cast<CuteQGraphTransitionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphTransitionCall5 call = reinterpret_cast<CuteQGraphTransitionCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphTransitionCall6 call = reinterpret_cast<CuteQGraphTransitionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphTransitionCall7 call = reinterpret_cast<CuteQGraphTransitionCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphTransitionCall8 call = reinterpret_cast<CuteQGraphTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QGraphTransition10metaObjectEv(
    const QGraphTransition *self) {
  return self->metaObject();
}

//  void *QGraphTransition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QGraphTransition11qt_metacastEPKc(
    QGraphTransition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphTransition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QGraphTransition11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphTransition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QGraphTransition::~QGraphTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransitionD1Ev(QGraphTransition *self) {
  delete self;
}

//  void QGraphTransition::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransition10initializeEv(QGraphTransition *self) {
  self->initialize();
}

//  void QGraphTransition::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransition4stopEv(QGraphTransition *self) {
  self->stop();
}

//  bool QGraphTransition::initialized()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QGraphTransition11initializedEv(QGraphTransition *self) {
  return self->initialized();
}

//  bool QGraphTransition::contains(QGraphAnimation::GraphAnimationType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QGraphTransition8containsEN15QGraphAnimation18GraphAnimationTypeE(
    QGraphTransition *self,
    QGraphAnimation::GraphAnimationType type) {
  return self->contains(type);
}

//  void QGraphTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransition10classBeginEv(QGraphTransition *self) {
  self->classBegin();
}

//  void QGraphTransition::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransition17componentCompleteEv(
    QGraphTransition *self) {
  self->componentComplete();
}

//  void QGraphTransition::clear(QQmlListProperty<QObject> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGraphTransition5clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *a0) {
  QGraphTransition::clear(a0);
}

//  QGraphTransition as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QGraphTransition_QQmlParserStatus(
    QGraphTransition *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQGraphTransition, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphTransition(
    QGraphTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphTransition *>(self)->take(key, call);
}

//  void QGraphTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QGraphTransition10classBeginEv(QGraphTransition *self) {
  static_cast<OwnQGraphTransition *>(self)->OwnQGraphTransition::classBegin();
}

//  a QQmlListProperty<QObject> a ritual of QGraphTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGraphTransition__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
