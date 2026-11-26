//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qkeyboardhandler.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qkeyboardhandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QKeyboardHandler that Python can take functions over in. Every Qt3DInput::QKeyboardHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyboardHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyboardHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QKeyboardHandler : public Qt3DInput::QKeyboardHandler {
public:
  using Qt3DInput::QKeyboardHandler::QKeyboardHandler;
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
      CuteQt3DInput_QKeyboardHandlerCall0 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall0>(taken[0]);
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
      CuteQt3DInput_QKeyboardHandlerCall1 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall1>(taken[1]);
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
      CuteQt3DInput_QKeyboardHandlerCall2 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall2>(taken[2]);
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
      CuteQt3DInput_QKeyboardHandlerCall3 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall3>(taken[3]);
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
      CuteQt3DInput_QKeyboardHandlerCall4 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall4>(taken[4]);
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
      CuteQt3DInput_QKeyboardHandlerCall5 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall5>(taken[5]);
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
      CuteQt3DInput_QKeyboardHandlerCall6 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QKeyboardHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput16QKeyboardHandler10metaObjectEv(
    const Qt3DInput::QKeyboardHandler *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QKeyboardHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput16QKeyboardHandler11qt_metacastEPKc(
    Qt3DInput::QKeyboardHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QKeyboardHandler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput16QKeyboardHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QKeyboardHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QKeyboardHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput16QKeyboardHandler2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QKeyboardHandler::tr(s, c, n));
}

//  Qt3DInput::QKeyboardHandler::QKeyboardHandler(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardHandler *ritual_ZN9Qt3DInput16QKeyboardHandlerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QKeyboardHandler(parent);
}

//  Qt3DInput::QKeyboardHandler::~QKeyboardHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandlerD1Ev(
    Qt3DInput::QKeyboardHandler *self) {
  delete self;
}

//  Qt3DInput::QKeyboardDevice *Qt3DInput::QKeyboardHandler::sourceDevice()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevice *ritual_ZNK9Qt3DInput16QKeyboardHandler12sourceDeviceEv(
    const Qt3DInput::QKeyboardHandler *self) {
  return self->sourceDevice();
}

//  bool Qt3DInput::QKeyboardHandler::focus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput16QKeyboardHandler5focusEv(
    const Qt3DInput::QKeyboardHandler *self) {
  return self->focus();
}

//  void
//      Qt3DInput::QKeyboardHandler::setSourceDevice(Qt3DInput::QKeyboardDevi
//      ce *keyboardDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15setSourceDeviceEPNS_15QKeyboardDeviceE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyboardDevice *keyboardDevice) {
  self->setSourceDevice(keyboardDevice);
}

//  void Qt3DInput::QKeyboardHandler::setFocus(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler8setFocusEb(
    Qt3DInput::QKeyboardHandler *self,
    bool focus) {
  self->setFocus(focus);
}

//  void Qt3DInput::QKeyboardHandler::sourceDeviceChanged(QKeyboardDevice
//      *keyboardDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler19sourceDeviceChangedEPNS_15QKeyboardDeviceE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyboardDevice *keyboardDevice) {
  self->sourceDeviceChanged(keyboardDevice);
}

//  void Qt3DInput::QKeyboardHandler::focusChanged(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler12focusChangedEb(
    Qt3DInput::QKeyboardHandler *self,
    bool focus) {
  self->focusChanged(focus);
}

//  void Qt3DInput::QKeyboardHandler::digit0Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit0PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit0Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit1Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit1PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit1Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit2Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit2PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit2Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit3Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit3PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit3Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit4Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit4PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit4Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit5Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit5PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit5Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit6Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit6PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit6Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit7Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit7PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit7Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit8Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit8PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit8Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::digit9Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13digit9PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->digit9Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::leftPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11leftPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->leftPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::rightPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler12rightPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->rightPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::upPressed(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler9upPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->upPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::downPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11downPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->downPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::tabPressed(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler10tabPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->tabPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::backtabPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler14backtabPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->backtabPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::asteriskPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15asteriskPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->asteriskPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::numberSignPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler17numberSignPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->numberSignPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::escapePressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13escapePressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->escapePressed(event);
}

//  void Qt3DInput::QKeyboardHandler::returnPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13returnPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->returnPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::enterPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler12enterPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->enterPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::deletePressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13deletePressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->deletePressed(event);
}

//  void Qt3DInput::QKeyboardHandler::spacePressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler12spacePressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->spacePressed(event);
}

//  void Qt3DInput::QKeyboardHandler::backPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11backPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->backPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::cancelPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13cancelPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->cancelPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::selectPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13selectPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->selectPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::yesPressed(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler10yesPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->yesPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::noPressed(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler9noPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->noPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::context1Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15context1PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->context1Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::context2Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15context2PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->context2Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::context3Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15context3PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->context3Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::context4Pressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15context4PressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->context4Pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::callPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11callPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->callPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::hangupPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler13hangupPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->hangupPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::flipPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11flipPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->flipPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::menuPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler11menuPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->menuPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::volumeUpPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler15volumeUpPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->volumeUpPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::volumeDownPressed(Qt3DInput::QKeyEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler17volumeDownPressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->volumeDownPressed(event);
}

//  void Qt3DInput::QKeyboardHandler::pressed(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler7pressedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->pressed(event);
}

//  void Qt3DInput::QKeyboardHandler::released(Qt3DInput::QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QKeyboardHandler8releasedEPNS_9QKeyEventE(
    Qt3DInput::QKeyboardHandler *self,
    Qt3DInput::QKeyEvent *event) {
  self->released(event);
}

//  QKeyboardHandlerPrivate *Qt3DInput::QKeyboardHandler::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardHandlerPrivate *ritual_ZN9Qt3DInput16QKeyboardHandler6d_funcEv(
    Qt3DInput::QKeyboardHandler *self) {
  return self->d_func();
}

//  const QKeyboardHandlerPrivate *Qt3DInput::QKeyboardHandler::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QKeyboardHandlerPrivate *ritual_ZNK9Qt3DInput16QKeyboardHandler6d_funcEv(
    const Qt3DInput::QKeyboardHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QKeyboardHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QKeyboardHandler(
    Qt3DInput::QKeyboardHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QKeyboardHandler *>(self)->take(key, call);
}
