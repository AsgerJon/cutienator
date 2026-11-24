//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::SpecialMenuAction that Python can take functions over in. Every qdesigner_internal::SpecialMenuAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
typedef bool (*Cuteqdesigner_internal_SpecialMenuActionCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_SpecialMenuActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_SpecialMenuAction : public qdesigner_internal::SpecialMenuAction {
public:
  using qdesigner_internal::SpecialMenuAction::SpecialMenuAction;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
  //  bool QAction::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall0 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAction::event(a0);
  }
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall1 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall2 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall3 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall4 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall5 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall6 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::SpecialMenuAction::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17SpecialMenuAction10metaObjectEv(
    const qdesigner_internal::SpecialMenuAction *self) {
  return self->metaObject();
}

//  a Python function taken by a Cuteqdesigner_internal_SpecialMenuAction,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_SpecialMenuAction(
    qdesigner_internal::SpecialMenuAction *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_SpecialMenuAction *>(self)->take(key, call);
}
