//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/desktopinputselectioncontrol_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/desktopinputselectioncontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtVirtualKeyboard::DesktopInputSelectionControl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtVirtualKeyboard_DesktopInputSelectionControl : QtVirtualKeyboard::DesktopInputSelectionControl {
  using QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter;
};

//  A QtVirtualKeyboard::DesktopInputSelectionControl that Python can take functions over in. Every QtVirtualKeyboard::DesktopInputSelectionControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_DesktopInputSelectionControlCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_DesktopInputSelectionControl : public QtVirtualKeyboard::DesktopInputSelectionControl {
public:
  using QtVirtualKeyboard::DesktopInputSelectionControl::DesktopInputSelectionControl;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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
  //  bool
  //      QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter(QObj
  //      ect *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall2>(taken[2]);
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
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall3>(taken[3]);
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
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall4>(taken[4]);
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
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall5>(taken[5]);
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
      CuteQtVirtualKeyboard_DesktopInputSelectionControlCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControlCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtVirtualKeyboard::DesktopInputSelectionControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard28DesktopInputSelectionControl10metaObjectEv(
    const QtVirtualKeyboard::DesktopInputSelectionControl *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::DesktopInputSelectionControl::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControl2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtVirtualKeyboard::DesktopInputSelectionControl::tr(
          s,
          c,
          n));
}

//  QtVirtualKeyboard::DesktopInputSelectionControl::~DesktopInputSelectionCo
//      ntrol()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard28DesktopInputSelectionControlD1Ev(
    QtVirtualKeyboard::DesktopInputSelectionControl *self) {
  delete self;
}

//  a Python function taken by a
//      CuteQtVirtualKeyboard_DesktopInputSelectionControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_DesktopInputSelectionControl(
    QtVirtualKeyboard::DesktopInputSelectionControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_DesktopInputSelectionControl *>(self)->take(key, call);
}

//  bool QtVirtualKeyboard::DesktopInputSelectionControl::eventFilter(QObject
//      *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard28DesktopInputSelectionControl11eventFilterEP7QObjectP6QEvent(
    QtVirtualKeyboard::DesktopInputSelectionControl *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQtVirtualKeyboard_DesktopInputSelectionControl *>(self)->OwnQtVirtualKeyboard_DesktopInputSelectionControl::eventFilter(
      object,
      event);
}
