//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/enterkeyaction_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/enterkeyaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::EnterKeyAction that Python can take functions over in. Every QtVirtualKeyboard::EnterKeyAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_EnterKeyActionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_EnterKeyActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_EnterKeyActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_EnterKeyActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_EnterKeyActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_EnterKeyActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_EnterKeyActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_EnterKeyAction : public QtVirtualKeyboard::EnterKeyAction {
public:
  using QtVirtualKeyboard::EnterKeyAction::EnterKeyAction;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_EnterKeyActionCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_EnterKeyActionCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall1>(taken[1]);
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
      CuteQtVirtualKeyboard_EnterKeyActionCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall2>(taken[2]);
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
      CuteQtVirtualKeyboard_EnterKeyActionCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall3>(taken[3]);
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
      CuteQtVirtualKeyboard_EnterKeyActionCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall4>(taken[4]);
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
      CuteQtVirtualKeyboard_EnterKeyActionCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall5>(taken[5]);
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
      CuteQtVirtualKeyboard_EnterKeyActionCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_EnterKeyActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::EnterKeyAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard14EnterKeyAction10metaObjectEv(
    const QtVirtualKeyboard::EnterKeyAction *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::EnterKeyAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard14EnterKeyAction11qt_metacastEPKc(
    QtVirtualKeyboard::EnterKeyAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::EnterKeyAction::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard14EnterKeyAction11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::EnterKeyAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::EnterKeyAction::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard14EnterKeyAction2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::EnterKeyAction::tr(s, c, n));
}

//  void QtVirtualKeyboard::EnterKeyAction::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard14EnterKeyAction24qt_qmlMarker_uncreatableEv(
    QtVirtualKeyboard::EnterKeyAction *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QtVirtualKeyboard::EnterKeyAction::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard14EnterKeyAction21qt_qmlMarker_attachedEv(
    QtVirtualKeyboard::EnterKeyAction *self) {
  self->qt_qmlMarker_attached();
}

//  EnterKeyActionAttachedType
//      *QtVirtualKeyboard::EnterKeyAction::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::EnterKeyActionAttachedType *ritual_ZN17QtVirtualKeyboard14EnterKeyAction21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QtVirtualKeyboard::EnterKeyAction::qmlAttachedProperties(object);
}

//  a Python function taken by a CuteQtVirtualKeyboard_EnterKeyAction, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_EnterKeyAction(
    QtVirtualKeyboard::EnterKeyAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_EnterKeyAction *>(self)->take(key, call);
}
