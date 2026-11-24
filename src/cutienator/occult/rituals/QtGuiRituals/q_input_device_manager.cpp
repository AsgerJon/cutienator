//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputdevicemanager_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputdevicemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QInputDeviceManager that Python can take functions over in. Every QInputDeviceManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInputDeviceManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInputDeviceManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDeviceManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDeviceManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDeviceManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDeviceManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDeviceManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQInputDeviceManager : public QInputDeviceManager {
public:
  using QInputDeviceManager::QInputDeviceManager;
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
      CuteQInputDeviceManagerCall0 call = reinterpret_cast<CuteQInputDeviceManagerCall0>(taken[0]);
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
      CuteQInputDeviceManagerCall1 call = reinterpret_cast<CuteQInputDeviceManagerCall1>(taken[1]);
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
      CuteQInputDeviceManagerCall2 call = reinterpret_cast<CuteQInputDeviceManagerCall2>(taken[2]);
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
      CuteQInputDeviceManagerCall3 call = reinterpret_cast<CuteQInputDeviceManagerCall3>(taken[3]);
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
      CuteQInputDeviceManagerCall4 call = reinterpret_cast<CuteQInputDeviceManagerCall4>(taken[4]);
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
      CuteQInputDeviceManagerCall5 call = reinterpret_cast<CuteQInputDeviceManagerCall5>(taken[5]);
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
      CuteQInputDeviceManagerCall6 call = reinterpret_cast<CuteQInputDeviceManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QInputDeviceManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QInputDeviceManager10metaObjectEv(
    const QInputDeviceManager *self) {
  return self->metaObject();
}

//  QString QInputDeviceManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QInputDeviceManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputDeviceManager::tr(s, c, n));
}

//  QInputDeviceManagerPrivate *QInputDeviceManager::d_func()
extern "C" Q_DECL_EXPORT
QInputDeviceManagerPrivate *ritual_ZN19QInputDeviceManager6d_funcEv(
    QInputDeviceManager *self) {
  return self->d_func();
}

//  const QInputDeviceManagerPrivate *QInputDeviceManager::d_func() const
extern "C" Q_DECL_EXPORT
const QInputDeviceManagerPrivate *ritual_ZNK19QInputDeviceManager6d_funcEv(
    const QInputDeviceManager *self) {
  return self->d_func();
}

//  QInputDeviceManager::QInputDeviceManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QInputDeviceManager *ritual_ZN19QInputDeviceManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQInputDeviceManager(parent);
}

//  QInputDeviceManager::~QInputDeviceManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDeviceManagerD1Ev(QInputDeviceManager *self) {
  delete self;
}

//  int QInputDeviceManager::deviceCount(DeviceType type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QInputDeviceManager11deviceCountENS_10DeviceTypeE(
    const QInputDeviceManager *self,
    QInputDeviceManager::DeviceType type) {
  return self->deviceCount(type);
}

//  void QInputDeviceManager::setCursorPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDeviceManager12setCursorPosERK6QPoint(
    QInputDeviceManager *self,
    const QPoint *pos) {
  self->setCursorPos(*pos);
}

//  Qt::KeyboardModifiers QInputDeviceManager::keyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QInputDeviceManager17keyboardModifiersEv(
    const QInputDeviceManager *self) {
  return static_cast<int>(self->keyboardModifiers().toInt());
}

//  void QInputDeviceManager::setKeyboardModifiers(Qt::KeyboardModifiers
//      mods)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDeviceManager20setKeyboardModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QInputDeviceManager *self,
    int mods) {
  self->setKeyboardModifiers(QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  a Python function taken by a CuteQInputDeviceManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputDeviceManager(
    QInputDeviceManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputDeviceManager *>(self)->take(key, call);
}
