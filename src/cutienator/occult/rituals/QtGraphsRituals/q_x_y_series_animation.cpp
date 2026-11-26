//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qxyseriesanimation_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QXYSeriesAnimation' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qxyseriesanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/qxyseriesanimation_p.h>
#include <QtGraphs/private/qgraphanimation_p.h>
#include <QtGraphs/private/qgraphanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__QXYSeriesAnimation.cpp, line 1, as moc:QXYSeriesAnimation
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QXYSeriesAnimationE_t {};
} // unnamed namespace

template <> constexpr inline auto QXYSeriesAnimation::qt_create_metaobjectdata<qt_meta_tag_ZN18QXYSeriesAnimationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QXYSeriesAnimation",
        "valueUpdated",
        "",
        "QVariant",
        "value"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'valueUpdated'
        QtMocHelpers::SlotData<void(const QVariant &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QXYSeriesAnimation, qt_meta_tag_ZN18QXYSeriesAnimationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QXYSeriesAnimation::staticMetaObject = { {
    QMetaObject::SuperData::link<QGraphAnimation::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QXYSeriesAnimationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QXYSeriesAnimationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QXYSeriesAnimationE_t>.metaTypes,
    nullptr
} };

void QXYSeriesAnimation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QXYSeriesAnimation *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->valueUpdated((*reinterpret_cast<std::add_pointer_t<QVariant>>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject *QXYSeriesAnimation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QXYSeriesAnimation::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QXYSeriesAnimationE_t>.strings))
        return static_cast<void*>(this);
    return QGraphAnimation::qt_metacast(_clname);
}

int QXYSeriesAnimation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QGraphAnimation::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/animation/qxyseriesanimation.cpp, line 29, as _ZN18QXYSeriesAnimationD0Ev
inline QXYSeriesAnimation::~QXYSeriesAnimation() {}

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 53, as _ZN15QGraphAnimationC2EP7QObject
inline QGraphAnimation::QGraphAnimation(QObject *parent)
    : QVariantAnimation(parent)
{
    connect(this, &QVariantAnimation::valueChanged, this, &QGraphAnimation::valueUpdated);
    connect(this, &QVariantAnimation::finished, this, &QGraphAnimation::end);
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 65, as _ZNK15QGraphAnimation9animatingEv
inline QGraphAnimation::AnimationState QGraphAnimation::animating() const
{
    return m_animating;
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 60, as _ZN15QGraphAnimationD2Ev
inline QGraphAnimation::~QGraphAnimation()
{
    stop();
}

//  from ../qtgraphs/src/graphs2d/animation/qxyseriesanimation.cpp, line 25, as _ZN18QXYSeriesAnimationC1EP7QObject
inline QXYSeriesAnimation::QXYSeriesAnimation(QObject *parent)
    : QGraphAnimation(parent)
{}

//  from ../qtgraphs/src/graphs2d/animation/qxyseriesanimation.cpp, line 31, as _ZN18QXYSeriesAnimation13updateCurrentEN16QGraphTransition14TransitionTypeEi7QPointF
inline void QXYSeriesAnimation::updateCurrent(QGraphTransition::TransitionType tt, int index, QPointF point)
{
    m_currentTransitionType = tt;
    m_newPointIndex = index;
    m_newPoint = point;

    if (m_previousTransitionType == QGraphTransition::TransitionType::None)
        m_previousTransitionType = m_currentTransitionType;

    if (animating() == QGraphAnimation::AnimationState::Stopped)
        m_activePointIndex = index;
}
//  -----------------------------------------------------------------------

//  A QXYSeriesAnimation that Python can take functions over in. Every QXYSeriesAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXYSeriesAnimationCall0)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQXYSeriesAnimationCall1)(const void *, int *);
typedef void (*CuteQXYSeriesAnimationCall2)(const void *, int *);
typedef void (*CuteQXYSeriesAnimationCall3)(const void *, const QVariant *, int *);
typedef int (*CuteQXYSeriesAnimationCall4)(const void *, int *);
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQXYSeriesAnimationCall5)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteQXYSeriesAnimationCall6)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQXYSeriesAnimationCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQXYSeriesAnimationCall8)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQXYSeriesAnimationCall9)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQXYSeriesAnimationCall10)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQXYSeriesAnimationCall11)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYSeriesAnimationCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesAnimationCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesAnimationCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesAnimationCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesAnimationCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesAnimationCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYSeriesAnimation : public QXYSeriesAnimation {
public:
  using QXYSeriesAnimation::QXYSeriesAnimation;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QGraphAnimation17setAnimatingValueERK8QVariantS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation7animateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation3endEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation12valueUpdatedERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation13animationTypeEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
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

  //  void QXYSeriesAnimation::setAnimatingValue(const QVariant &start,
  //      const QVariant &end)
  void setAnimatingValue(
      const QVariant &start,
      const QVariant &end) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall0 call = reinterpret_cast<CuteQXYSeriesAnimationCall0>(taken[0]);
      call(this, &start, &end, &handled);
      if (handled) return;
    }
  }

  //  void QXYSeriesAnimation::animate()
  void animate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall1 call = reinterpret_cast<CuteQXYSeriesAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QXYSeriesAnimation::end()
  void end() override {
    if (taken[2]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall2 call = reinterpret_cast<CuteQXYSeriesAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QXYSeriesAnimation::valueUpdated(const QVariant &value)
  void valueUpdated(const QVariant &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall3 call = reinterpret_cast<CuteQXYSeriesAnimationCall3>(taken[3]);
      call(this, &value, &handled);
      if (handled) return;
    }
  }

  //  GraphAnimationType QGraphAnimation::animationType()
  QGraphAnimation::GraphAnimationType animationType() override {
    if (taken[4]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall4 call = reinterpret_cast<CuteQXYSeriesAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGraphAnimation::GraphAnimationType>(given);
    }
    return {};
  }

#if QT_CONFIG(animation)
  //  QVariant QGraphAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall5 call = reinterpret_cast<CuteQXYSeriesAnimationCall5>(taken[5]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQXYSeriesAnimationCall6 call = reinterpret_cast<CuteQXYSeriesAnimationCall6>(taken[6]);
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
      CuteQXYSeriesAnimationCall7 call = reinterpret_cast<CuteQXYSeriesAnimationCall7>(taken[7]);
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
      CuteQXYSeriesAnimationCall8 call = reinterpret_cast<CuteQXYSeriesAnimationCall8>(taken[8]);
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
      CuteQXYSeriesAnimationCall9 call = reinterpret_cast<CuteQXYSeriesAnimationCall9>(taken[9]);
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
      CuteQXYSeriesAnimationCall10 call = reinterpret_cast<CuteQXYSeriesAnimationCall10>(taken[10]);
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
      CuteQXYSeriesAnimationCall11 call = reinterpret_cast<CuteQXYSeriesAnimationCall11>(taken[11]);
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
      CuteQXYSeriesAnimationCall12 call = reinterpret_cast<CuteQXYSeriesAnimationCall12>(taken[12]);
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
      CuteQXYSeriesAnimationCall13 call = reinterpret_cast<CuteQXYSeriesAnimationCall13>(taken[13]);
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
      CuteQXYSeriesAnimationCall14 call = reinterpret_cast<CuteQXYSeriesAnimationCall14>(taken[14]);
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
      CuteQXYSeriesAnimationCall15 call = reinterpret_cast<CuteQXYSeriesAnimationCall15>(taken[15]);
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
      CuteQXYSeriesAnimationCall16 call = reinterpret_cast<CuteQXYSeriesAnimationCall16>(taken[16]);
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
      CuteQXYSeriesAnimationCall17 call = reinterpret_cast<CuteQXYSeriesAnimationCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYSeriesAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QXYSeriesAnimation10metaObjectEv(
    const QXYSeriesAnimation *self) {
  return self->metaObject();
}

//  void *QXYSeriesAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QXYSeriesAnimation11qt_metacastEPKc(
    QXYSeriesAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYSeriesAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QXYSeriesAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYSeriesAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QXYSeriesAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QXYSeriesAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYSeriesAnimation::tr(s, c, n));
}

//  QXYSeriesAnimation::QXYSeriesAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QXYSeriesAnimation *ritual_ZN18QXYSeriesAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQXYSeriesAnimation(parent);
}

//  QXYSeriesAnimation::~QXYSeriesAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimationD1Ev(QXYSeriesAnimation *self) {
  delete self;
}

//  void QXYSeriesAnimation::updateCurrent(QGraphTransition::TransitionType
//      tt, int index, QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimation13updateCurrentEN16QGraphTransition14TransitionTypeEi7QPointF(
    QXYSeriesAnimation *self,
    QGraphTransition::TransitionType tt,
    int index,
    const QPointF *point) {
  self->updateCurrent(tt, index, *point);
}

//  void QXYSeriesAnimation::setAnimatingValue(const QVariant &start, const
//      QVariant &end)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimation17setAnimatingValueERK8QVariantS2_(
    QXYSeriesAnimation *self,
    const QVariant *start,
    const QVariant *end) {
  self->setAnimatingValue(*start, *end);
}

//  void QXYSeriesAnimation::animate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimation7animateEv(QXYSeriesAnimation *self) {
  self->animate();
}

//  void QXYSeriesAnimation::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimation3endEv(QXYSeriesAnimation *self) {
  self->end();
}

//  void QXYSeriesAnimation::valueUpdated(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXYSeriesAnimation12valueUpdatedERK8QVariant(
    QXYSeriesAnimation *self,
    const QVariant *value) {
  self->valueUpdated(*value);
}

//  a Python function taken by a CuteQXYSeriesAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYSeriesAnimation(
    QXYSeriesAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXYSeriesAnimation *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
