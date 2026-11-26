//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphanimation_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QGraphAnimation' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__QGraphAnimation.cpp, line 1, as moc:QGraphAnimation
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QGraphAnimationE_t {};
} // unnamed namespace

template <> constexpr inline auto QGraphAnimation::qt_create_metaobjectdata<qt_meta_tag_ZN15QGraphAnimationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QGraphAnimation",
        "RegisterEnumClassesUnscoped",
        "false",
        "animatingChanged",
        "",
        "valueUpdated",
        "QVariant",
        "value",
        "animating",
        "AnimationState",
        "Playing",
        "Stopped",
        "GraphAnimationType",
        "GraphPoint",
        "ControlPoint"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'animatingChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
        // Slot 'valueUpdated'
        QtMocHelpers::SlotData<void(const QVariant &)>(5, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'animating'
        QtMocHelpers::PropertyData<enum AnimationState>(8, 0x80000000 | 9, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 0),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'AnimationState'
        QtMocHelpers::EnumData<enum AnimationState>(9, 9, QMC::EnumIsScoped).add({
            {   10, AnimationState::Playing },
            {   11, AnimationState::Stopped },
        }),
        // enum 'GraphAnimationType'
        QtMocHelpers::EnumData<enum GraphAnimationType>(12, 12, QMC::EnumIsScoped).add({
            {   13, GraphAnimationType::GraphPoint },
            {   14, GraphAnimationType::ControlPoint },
        }),
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QGraphAnimation, qt_meta_tag_ZN15QGraphAnimationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QGraphAnimation::staticMetaObject = { {
    QMetaObject::SuperData::link<QVariantAnimation::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QGraphAnimationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QGraphAnimationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QGraphAnimationE_t>.metaTypes,
    nullptr
} };

void QGraphAnimation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QGraphAnimation *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->animatingChanged(); break;
        case 1: _t->valueUpdated((*reinterpret_cast<std::add_pointer_t<QVariant>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QGraphAnimation::*)()>(_a, &QGraphAnimation::animatingChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<enum AnimationState*>(_v) = _t->animating(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setAnimating(*reinterpret_cast<enum AnimationState*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QGraphAnimation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QGraphAnimation::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QGraphAnimationE_t>.strings))
        return static_cast<void*>(this);
    return QVariantAnimation::qt_metacast(_clname);
}

int QGraphAnimation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QVariantAnimation::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QGraphAnimation::animatingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 51, as _Z11lcAnimationv
inline const QLoggingCategory &lcAnimation()
{
    static const QLoggingCategory category("qt.graphs2d.animation");
    return category;
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 60, as _ZN15QGraphAnimationD0Ev
inline QGraphAnimation::~QGraphAnimation()
{
    stop();
}

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 53, as _ZN15QGraphAnimationC1EP7QObject
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

//  from ../qtgraphs/src/graphs2d/animation/qgraphanimation.cpp, line 70, as _ZN15QGraphAnimation12setAnimatingENS_14AnimationStateE
inline void QGraphAnimation::setAnimating(AnimationState newAnimating)
{
    if (m_animating == newAnimating) {
        qCDebug(lcAnimation) << "QGraphAnimation::setAnimating. AnimationState is already set to: " << newAnimating;
        return;
    }
    m_animating = newAnimating;

    qCDebug(lcAnimation) << "animation state:" << m_animating;
    emit animatingChanged();
}
//  -----------------------------------------------------------------------

//  A QGraphAnimation that Python can take functions over in. Every QGraphAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQGraphAnimationCall0)(const void *, int *);
typedef void (*CuteQGraphAnimationCall1)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQGraphAnimationCall2)(const void *, int *);
typedef void (*CuteQGraphAnimationCall3)(const void *, int *);
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQGraphAnimationCall4)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
typedef void (*CuteQGraphAnimationCall5)(const void *, const QVariant *, int *);
#if QT_CONFIG(animation)
typedef int (*CuteQGraphAnimationCall6)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQGraphAnimationCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQGraphAnimationCall8)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQGraphAnimationCall9)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQGraphAnimationCall10)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQGraphAnimationCall11)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphAnimationCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphAnimationCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphAnimationCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphAnimationCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphAnimationCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphAnimationCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphAnimation : public QGraphAnimation {
public:
  using QGraphAnimation::QGraphAnimation;
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
    if (!std::strcmp(key, "_ZN15QGraphAnimation7animateEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphAnimation3endEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
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

  //  GraphAnimationType QGraphAnimation::animationType()
  QGraphAnimation::GraphAnimationType animationType() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphAnimationCall0 call = reinterpret_cast<CuteQGraphAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGraphAnimation::GraphAnimationType>(given);
    }
    return {};
  }

  //  void QGraphAnimation::setAnimatingValue(const QVariant &start, const
  //      QVariant &end)
  void setAnimatingValue(
      const QVariant &start,
      const QVariant &end) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphAnimationCall1 call = reinterpret_cast<CuteQGraphAnimationCall1>(taken[1]);
      call(this, &start, &end, &handled);
      if (handled) return;
    }
  }

  //  void QGraphAnimation::animate()
  void animate() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphAnimationCall2 call = reinterpret_cast<CuteQGraphAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGraphAnimation::end()
  void end() override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphAnimationCall3 call = reinterpret_cast<CuteQGraphAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(animation)
  //  QVariant QGraphAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphAnimationCall4 call = reinterpret_cast<CuteQGraphAnimationCall4>(taken[4]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(animation)

  //  void QGraphAnimation::valueUpdated(const QVariant &value)
  void valueUpdated(const QVariant &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphAnimationCall5 call = reinterpret_cast<CuteQGraphAnimationCall5>(taken[5]);
      call(this, &value, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphAnimationCall6 call = reinterpret_cast<CuteQGraphAnimationCall6>(taken[6]);
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
      CuteQGraphAnimationCall7 call = reinterpret_cast<CuteQGraphAnimationCall7>(taken[7]);
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
      CuteQGraphAnimationCall8 call = reinterpret_cast<CuteQGraphAnimationCall8>(taken[8]);
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
      CuteQGraphAnimationCall9 call = reinterpret_cast<CuteQGraphAnimationCall9>(taken[9]);
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
      CuteQGraphAnimationCall10 call = reinterpret_cast<CuteQGraphAnimationCall10>(taken[10]);
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
      CuteQGraphAnimationCall11 call = reinterpret_cast<CuteQGraphAnimationCall11>(taken[11]);
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
      CuteQGraphAnimationCall12 call = reinterpret_cast<CuteQGraphAnimationCall12>(taken[12]);
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
      CuteQGraphAnimationCall13 call = reinterpret_cast<CuteQGraphAnimationCall13>(taken[13]);
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
      CuteQGraphAnimationCall14 call = reinterpret_cast<CuteQGraphAnimationCall14>(taken[14]);
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
      CuteQGraphAnimationCall15 call = reinterpret_cast<CuteQGraphAnimationCall15>(taken[15]);
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
      CuteQGraphAnimationCall16 call = reinterpret_cast<CuteQGraphAnimationCall16>(taken[16]);
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
      CuteQGraphAnimationCall17 call = reinterpret_cast<CuteQGraphAnimationCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphAnimation10metaObjectEv(
    const QGraphAnimation *self) {
  return self->metaObject();
}

//  void *QGraphAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGraphAnimation11qt_metacastEPKc(
    QGraphAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphAnimation::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGraphAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGraphAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphAnimation::tr(s, c, n));
}

//  QGraphAnimation::QGraphAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphAnimation *ritual_ZN15QGraphAnimationC1EP7QObject(QObject *parent) {
  return new CuteQGraphAnimation(parent);
}

//  QGraphAnimation::~QGraphAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimationD1Ev(QGraphAnimation *self) {
  delete self;
}

//  GraphAnimationType QGraphAnimation::animationType()
extern "C" Q_DECL_EXPORT
QGraphAnimation::GraphAnimationType ritual_ZN15QGraphAnimation13animationTypeEv(
    QGraphAnimation *self) {
  return self->animationType();
}

//  void QGraphAnimation::setAnimatingValue(const QVariant &start, const
//      QVariant &end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation17setAnimatingValueERK8QVariantS2_(
    QGraphAnimation *self,
    const QVariant *start,
    const QVariant *end) {
  self->setAnimatingValue(*start, *end);
}

//  void QGraphAnimation::animate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation7animateEv(QGraphAnimation *self) {
  self->animate();
}

//  void QGraphAnimation::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation3endEv(QGraphAnimation *self) {
  self->end();
}

//  QVariant QGraphAnimation::interpolated(const QVariant &start, const
//      QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QGraphAnimation12interpolatedERK8QVariantS2_d(
    const QGraphAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(self->interpolated(*start, *end, progress));
}

//  AnimationState QGraphAnimation::animating() const
extern "C" Q_DECL_EXPORT
QGraphAnimation::AnimationState ritual_ZNK15QGraphAnimation9animatingEv(
    const QGraphAnimation *self) {
  return self->animating();
}

//  void QGraphAnimation::setAnimating(AnimationState newAnimating)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation12setAnimatingENS_14AnimationStateE(
    QGraphAnimation *self,
    QGraphAnimation::AnimationState newAnimating) {
  self->setAnimating(newAnimating);
}

//  void QGraphAnimation::valueUpdated(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation12valueUpdatedERK8QVariant(
    QGraphAnimation *self,
    const QVariant *value) {
  self->valueUpdated(*value);
}

//  void QGraphAnimation::animatingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphAnimation16animatingChangedEv(QGraphAnimation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGraphAnimation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "animatingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "animatingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQGraphAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphAnimation(
    QGraphAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphAnimation *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
