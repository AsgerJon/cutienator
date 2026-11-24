//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPointerDeviceHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPointerDeviceHandler : QQuickPointerDeviceHandler {
  using QQuickPointerDeviceHandler::wantsPointerEvent;
};

//  A QQuickPointerDeviceHandler that Python can take functions over in. Every QQuickPointerDeviceHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPointerDeviceHandlerCall0)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerCall1)(const void *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerDeviceHandlerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerDeviceHandlerCall4)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerCall5)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickPointerDeviceHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickPointerDeviceHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerDeviceHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerDeviceHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerDeviceHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerDeviceHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerDeviceHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerDeviceHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPointerDeviceHandler : public QQuickPointerDeviceHandler {
public:
  using QQuickPointerDeviceHandler::QQuickPointerDeviceHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickPointerDeviceHandler::wantsPointerEvent(QPointerEvent
  //      *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall0 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickPointerDeviceHandler::wantsPointerEvent(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall1 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall2 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall3 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall3>(taken[3]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall4 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall4>(taken[4]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall5 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall6 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall7 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onActiveChanged();
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall8 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall8>(taken[8]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::canGrab(event, point);
  }

  //  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent
  //      *event, const QEventPoint &point, QObject *proposedGrabber)
  bool approveGrabTransition(
      QPointerEvent *event,
      const QEventPoint &point,
      QObject *proposedGrabber) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall9 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall9>(taken[9]);
      bool given = call(this, event, &point, proposedGrabber, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::approveGrabTransition(event, point, proposedGrabber);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall10 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall11 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall12 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall13 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall14 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerCall15 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPointerDeviceHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickPointerDeviceHandler10metaObjectEv(
    const QQuickPointerDeviceHandler *self) {
  return self->metaObject();
}

//  QString QQuickPointerDeviceHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickPointerDeviceHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPointerDeviceHandler::tr(s, c, n));
}

//  QQuickPointerDeviceHandler::QQuickPointerDeviceHandler(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickPointerDeviceHandler *ritual_ZN26QQuickPointerDeviceHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPointerDeviceHandler(parent);
}

//  QInputDevice::DeviceTypes QQuickPointerDeviceHandler::acceptedDevices()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickPointerDeviceHandler15acceptedDevicesEv(
    const QQuickPointerDeviceHandler *self) {
  return static_cast<int>(self->acceptedDevices().toInt());
}

//  QPointingDevice::PointerTypes
//      QQuickPointerDeviceHandler::acceptedPointerTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickPointerDeviceHandler20acceptedPointerTypesEv(
    const QQuickPointerDeviceHandler *self) {
  return static_cast<int>(self->acceptedPointerTypes().toInt());
}

//  Qt::MouseButtons QQuickPointerDeviceHandler::acceptedButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickPointerDeviceHandler15acceptedButtonsEv(
    const QQuickPointerDeviceHandler *self) {
  return static_cast<int>(self->acceptedButtons().toInt());
}

//  Qt::KeyboardModifiers QQuickPointerDeviceHandler::acceptedModifiers()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickPointerDeviceHandler17acceptedModifiersEv(
    const QQuickPointerDeviceHandler *self) {
  return static_cast<int>(self->acceptedModifiers().toInt());
}

//  void
//      QQuickPointerDeviceHandler::setAcceptedDevices(QInputDevice::DeviceTy
//      pes acceptedDevices)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPointerDeviceHandler18setAcceptedDevicesE6QFlagsIN12QInputDevice10DeviceTypeEE(
    QQuickPointerDeviceHandler *self,
    int acceptedDevices) {
  self->setAcceptedDevices(
      QFlags<QInputDevice::DeviceType>::fromInt(acceptedDevices));
}

//  void QQuickPointerDeviceHandler::setAcceptedPointerTypes(QPointingDevice:
//      :PointerTypes acceptedPointerTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPointerDeviceHandler23setAcceptedPointerTypesE6QFlagsIN15QPointingDevice11PointerTypeEE(
    QQuickPointerDeviceHandler *self,
    int acceptedPointerTypes) {
  self->setAcceptedPointerTypes(
      QFlags<QPointingDevice::PointerType>::fromInt(acceptedPointerTypes));
}

//  void QQuickPointerDeviceHandler::setAcceptedButtons(Qt::MouseButtons
//      buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPointerDeviceHandler18setAcceptedButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QQuickPointerDeviceHandler *self,
    int buttons) {
  self->setAcceptedButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  void
//      QQuickPointerDeviceHandler::setAcceptedModifiers(Qt::KeyboardModifier
//      s acceptedModifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPointerDeviceHandler20setAcceptedModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QQuickPointerDeviceHandler *self,
    int acceptedModifiers) {
  self->setAcceptedModifiers(
      QFlags<Qt::KeyboardModifier>::fromInt(acceptedModifiers));
}

//  bool QQuickPointerDeviceHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPointerDeviceHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPointerDeviceHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  QQuickPointerDeviceHandlerPrivate *QQuickPointerDeviceHandler::d_func()
extern "C" Q_DECL_EXPORT
QQuickPointerDeviceHandlerPrivate *ritual_ZN26QQuickPointerDeviceHandler6d_funcEv(
    QQuickPointerDeviceHandler *self) {
  return self->d_func();
}

//  const QQuickPointerDeviceHandlerPrivate
//      *QQuickPointerDeviceHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPointerDeviceHandlerPrivate *ritual_ZNK26QQuickPointerDeviceHandler6d_funcEv(
    const QQuickPointerDeviceHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPointerDeviceHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPointerDeviceHandler(
    QQuickPointerDeviceHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPointerDeviceHandler *>(self)->take(key, call);
}

//  bool QQuickPointerDeviceHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QQuickPointerDeviceHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPointerDeviceHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickPointerDeviceHandler *>(self)->OwnQQuickPointerDeviceHandler::wantsPointerEvent(
      event);
}
