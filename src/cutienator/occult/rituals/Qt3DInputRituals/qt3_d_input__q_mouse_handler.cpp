//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qmousehandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <Qt3DInput/qmousehandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QMouseHandler that Python can take functions over in. Every Qt3DInput::QMouseHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QMouseHandler : public Qt3DInput::QMouseHandler {
public:
  using Qt3DInput::QMouseHandler::QMouseHandler;
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
      CuteQt3DInput_QMouseHandlerCall0 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall0>(taken[0]);
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
      CuteQt3DInput_QMouseHandlerCall1 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall1>(taken[1]);
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
      CuteQt3DInput_QMouseHandlerCall2 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall2>(taken[2]);
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
      CuteQt3DInput_QMouseHandlerCall3 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall3>(taken[3]);
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
      CuteQt3DInput_QMouseHandlerCall4 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall4>(taken[4]);
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
      CuteQt3DInput_QMouseHandlerCall5 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall5>(taken[5]);
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
      CuteQt3DInput_QMouseHandlerCall6 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QMouseHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput13QMouseHandler10metaObjectEv(
    const Qt3DInput::QMouseHandler *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QMouseHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput13QMouseHandler11qt_metacastEPKc(
    Qt3DInput::QMouseHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QMouseHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput13QMouseHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QMouseHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QMouseHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput13QMouseHandler2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QMouseHandler::tr(s, c, n));
}

//  Qt3DInput::QMouseHandler::QMouseHandler(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseHandler *ritual_ZN9Qt3DInput13QMouseHandlerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QMouseHandler(parent);
}

//  Qt3DInput::QMouseHandler::~QMouseHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandlerD1Ev(Qt3DInput::QMouseHandler *self) {
  delete self;
}

//  QMouseDevice *Qt3DInput::QMouseHandler::sourceDevice() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseDevice *ritual_ZNK9Qt3DInput13QMouseHandler12sourceDeviceEv(
    const Qt3DInput::QMouseHandler *self) {
  return self->sourceDevice();
}

//  bool Qt3DInput::QMouseHandler::containsMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput13QMouseHandler13containsMouseEv(
    const Qt3DInput::QMouseHandler *self) {
  return self->containsMouse();
}

//  void Qt3DInput::QMouseHandler::setSourceDevice(QMouseDevice *mouseDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler15setSourceDeviceEPNS_12QMouseDeviceE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseDevice *mouseDevice) {
  self->setSourceDevice(mouseDevice);
}

//  void Qt3DInput::QMouseHandler::sourceDeviceChanged(QMouseDevice
//      *mouseDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler19sourceDeviceChangedEPNS_12QMouseDeviceE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseDevice *mouseDevice) {
  self->sourceDeviceChanged(mouseDevice);
}

//  void Qt3DInput::QMouseHandler::containsMouseChanged(bool containsMouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler20containsMouseChangedEb(
    Qt3DInput::QMouseHandler *self,
    bool containsMouse) {
  self->containsMouseChanged(containsMouse);
}

//  void Qt3DInput::QMouseHandler::clicked(Qt3DInput::QMouseEvent *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler7clickedEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->clicked(mouse);
}

//  void Qt3DInput::QMouseHandler::doubleClicked(Qt3DInput::QMouseEvent
//      *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler13doubleClickedEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->doubleClicked(mouse);
}

//  void Qt3DInput::QMouseHandler::entered()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler7enteredEv(
    Qt3DInput::QMouseHandler *self) {
  self->entered();
}

//  void Qt3DInput::QMouseHandler::exited()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler6exitedEv(
    Qt3DInput::QMouseHandler *self) {
  self->exited();
}

//  void Qt3DInput::QMouseHandler::pressed(Qt3DInput::QMouseEvent *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler7pressedEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->pressed(mouse);
}

//  void Qt3DInput::QMouseHandler::released(Qt3DInput::QMouseEvent *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler8releasedEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->released(mouse);
}

//  void Qt3DInput::QMouseHandler::pressAndHold(Qt3DInput::QMouseEvent
//      *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler12pressAndHoldEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->pressAndHold(mouse);
}

//  void Qt3DInput::QMouseHandler::positionChanged(Qt3DInput::QMouseEvent
//      *mouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler15positionChangedEPNS_11QMouseEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QMouseEvent *mouse) {
  self->positionChanged(mouse);
}

#if QT_CONFIG(wheelevent)
//  void Qt3DInput::QMouseHandler::wheel(Qt3DInput::QWheelEvent *wheel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler5wheelEPNS_11QWheelEventE(
    Qt3DInput::QMouseHandler *self,
    Qt3DInput::QWheelEvent *wheel) {
  self->wheel(wheel);
}
#endif  // QT_CONFIG(wheelevent)

//  void Qt3DInput::QMouseHandler::setContainsMouse(bool contains)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QMouseHandler16setContainsMouseEb(
    Qt3DInput::QMouseHandler *self,
    bool contains) {
  self->setContainsMouse(contains);
}

//  QMouseHandlerPrivate *Qt3DInput::QMouseHandler::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseHandlerPrivate *ritual_ZN9Qt3DInput13QMouseHandler6d_funcEv(
    Qt3DInput::QMouseHandler *self) {
  return self->d_func();
}

//  const QMouseHandlerPrivate *Qt3DInput::QMouseHandler::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QMouseHandlerPrivate *ritual_ZNK9Qt3DInput13QMouseHandler6d_funcEv(
    const Qt3DInput::QMouseHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QMouseHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QMouseHandler(
    Qt3DInput::QMouseHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QMouseHandler *>(self)->take(key, call);
}
