//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtPrivate::QQuickAttachedPropertyPropagator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtPrivate_QQuickAttachedPropertyPropagator : QtPrivate::QQuickAttachedPropertyPropagator {
  using QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange;
};

//  A QtPrivate::QQuickAttachedPropertyPropagator that Python can take functions over in. Every QtPrivate::QQuickAttachedPropertyPropagator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall0)(const void *, QtPrivate::QQuickAttachedPropertyPropagator *, QtPrivate::QQuickAttachedPropertyPropagator *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_QQuickAttachedPropertyPropagatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtPrivate_QQuickAttachedPropertyPropagator : public QtPrivate::QQuickAttachedPropertyPropagator {
public:
  using QtPrivate::QQuickAttachedPropertyPropagator::QQuickAttachedPropertyPropagator;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attachedParentChangeEPS0_S1_")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChang
  //      e(QQuickAttachedPropertyPropagator *newParent,
  //      QQuickAttachedPropertyPropagator *oldParent)
  void attachedParentChange(
      QtPrivate::QQuickAttachedPropertyPropagator *newParent,
      QtPrivate::QQuickAttachedPropertyPropagator *oldParent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall0 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall0>(taken[0]);
      call(this, newParent, oldParent, &handled);
      if (handled) return;
    }
    QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange(newParent, oldParent);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall1 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall2 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall3 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall4 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall5 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall6 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtPrivate_QQuickAttachedPropertyPropagatorCall7 call = reinterpret_cast<CuteQtPrivate_QQuickAttachedPropertyPropagatorCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtPrivate::QQuickAttachedPropertyPropagator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtPrivate32QQuickAttachedPropertyPropagator10metaObjectEv(
    const QtPrivate::QQuickAttachedPropertyPropagator *self) {
  return self->metaObject();
}

//  QString QtPrivate::QQuickAttachedPropertyPropagator::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtPrivate::QQuickAttachedPropertyPropagator::tr(
          s,
          c,
          n));
}

//  QQuickAttachedPropertyPropagator
//      *QtPrivate::QQuickAttachedPropertyPropagator::attachedObject(const
//      QMetaObject *attachedType, QObject *attachee, bool create)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator14attachedObjectEPK11QMetaObjectP7QObjectb(
    const QMetaObject *attachedType,
    QObject *attachee,
    bool create) {
  return QtPrivate::QQuickAttachedPropertyPropagator::attachedObject(
      attachedType,
      attachee,
      create);
}

//  void QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange(QQ
//      uickAttachedPropertyPropagator *newParent,
//      QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attachedParentChangeEPS0_S1_(
    QtPrivate::QQuickAttachedPropertyPropagator *self,
    QtPrivate::QQuickAttachedPropertyPropagator *newParent,
    QtPrivate::QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QQuickAttachedPropertyPropagator
//      *propagator)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN9QtPrivatelsE6QDebugPKNS_32QQuickAttachedPropertyPropagatorE(
    const QDebug *debug,
    const QtPrivate::QQuickAttachedPropertyPropagator *propagator) {
  return new QDebug(operator<<(*debug, propagator));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuickAttachedPropertyPropagatorPrivate
//      *QtPrivate::QQuickAttachedPropertyPropagator::d_func()
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagatorPrivate *ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator6d_funcEv(
    QtPrivate::QQuickAttachedPropertyPropagator *self) {
  return self->d_func();
}

//  const QQuickAttachedPropertyPropagatorPrivate
//      *QtPrivate::QQuickAttachedPropertyPropagator::d_func() const
extern "C" Q_DECL_EXPORT
const QtPrivate::QQuickAttachedPropertyPropagatorPrivate *ritual_ZNK9QtPrivate32QQuickAttachedPropertyPropagator6d_funcEv(
    const QtPrivate::QQuickAttachedPropertyPropagator *self) {
  return self->d_func();
}

//  a Python function taken by a
//      CuteQtPrivate_QQuickAttachedPropertyPropagator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtPrivate_QQuickAttachedPropertyPropagator(
    QtPrivate::QQuickAttachedPropertyPropagator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtPrivate_QQuickAttachedPropertyPropagator *>(self)->take(key, call);
}

//  void QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange(QQ
//      uickAttachedPropertyPropagator *newParent,
//      QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attachedParentChangeEPS0_S1_(
    QtPrivate::QQuickAttachedPropertyPropagator *self,
    QtPrivate::QQuickAttachedPropertyPropagator *newParent,
    QtPrivate::QQuickAttachedPropertyPropagator *oldParent) {
  static_cast<OwnQtPrivate_QQuickAttachedPropertyPropagator *>(self)->OwnQtPrivate_QQuickAttachedPropertyPropagator::attachedParentChange(
      newParent,
      oldParent);
}
