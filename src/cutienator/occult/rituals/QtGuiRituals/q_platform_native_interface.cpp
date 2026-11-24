//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformnativeinterface.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformnativeinterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QPlatformNativeInterface that Python can take functions over in. Every QPlatformNativeInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQPlatformNativeInterfaceCall0)(const void *, QPlatformWindow *, const QString *, int *);
typedef const QVariant * (*CuteQPlatformNativeInterfaceCall1)(const void *, QPlatformWindow *, const QString *, const QVariant *, int *);
typedef void (*CuteQPlatformNativeInterfaceCall2)(const void *, QPlatformWindow *, const QString *, const QVariant *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformNativeInterfaceCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformNativeInterfaceCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformNativeInterfaceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformNativeInterface : public QPlatformNativeInterface {
public:
  using QPlatformNativeInterface::QPlatformNativeInterface;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
  //      *window, const QString &name) const
  QVariant windowProperty(
      QPlatformWindow *window,
      const QString &name) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall0 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall0>(taken[0]);
      const QVariant * given = call(this, window, &name, &handled);
      if (handled && given) return *given;
    }
    return QPlatformNativeInterface::windowProperty(window, name);
  }

  //  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
  //      *window, const QString &name, const QVariant &defaultValue) const
  QVariant windowProperty(
      QPlatformWindow *window,
      const QString &name,
      const QVariant &defaultValue) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall1 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall1>(taken[1]);
      const QVariant * given = call(this, window, &name, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return QPlatformNativeInterface::windowProperty(window, name, defaultValue);
  }

  //  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow
  //      *window, const QString &name, const QVariant &value)
  void setWindowProperty(
      QPlatformWindow *window,
      const QString &name,
      const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall2 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall2>(taken[2]);
      call(this, window, &name, &value, &handled);
      if (handled) return;
    }
    QPlatformNativeInterface::setWindowProperty(window, name, value);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall3 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall4 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall5 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall6 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall7 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall8 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformNativeInterfaceCall9 call = reinterpret_cast<CuteQPlatformNativeInterfaceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformNativeInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPlatformNativeInterface10metaObjectEv(
    const QPlatformNativeInterface *self) {
  return self->metaObject();
}

//  QString QPlatformNativeInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPlatformNativeInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformNativeInterface::tr(s, c, n));
}

//  QVariantMap QPlatformNativeInterface::windowProperties(QPlatformWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK24QPlatformNativeInterface16windowPropertiesEP15QPlatformWindow(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window) {
  return new QMap<QString, QVariant>(self->windowProperties(window));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name) {
  return new QVariant(self->windowProperty(window, *name));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name, const QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *defaultValue) {
  return new QVariant(self->windowProperty(window, *name, *defaultValue));
}

//  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow *window,
//      const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *value) {
  self->setWindowProperty(window, *name, *value);
}

//  a Python function taken by a CuteQPlatformNativeInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformNativeInterface(
    QPlatformNativeInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformNativeInterface *>(self)->take(key, call);
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QString(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name) {
  return new QVariant(
      self->QPlatformNativeInterface::windowProperty(
          window,
          *name));
}

//  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
//      *window, const QString &name, const QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    const QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *defaultValue) {
  return new QVariant(
      self->QPlatformNativeInterface::windowProperty(
          window,
          *name,
          *defaultValue));
}

//  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow *window,
//      const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWindowRK7QStringRK8QVariant(
    QPlatformNativeInterface *self,
    QPlatformWindow *window,
    const QString *name,
    const QVariant *value) {
  self->QPlatformNativeInterface::setWindowProperty(window, *name, *value);
}
