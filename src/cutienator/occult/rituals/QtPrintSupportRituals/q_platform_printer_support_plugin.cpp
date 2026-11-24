//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintplugin.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintplugin.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformPrinterSupportPlugin that Python can take functions over in. Every QPlatformPrinterSupportPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef void * (*CuteQPlatformPrinterSupportPluginCall0)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformPrinterSupportPluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformPrinterSupportPluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformPrinterSupportPluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformPrinterSupportPluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformPrinterSupportPluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformPrinterSupportPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformPrinterSupportPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformPrinterSupportPlugin : public QPlatformPrinterSupportPlugin {
public:
  using QPlatformPrinterSupportPlugin::QPlatformPrinterSupportPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN29QPlatformPrinterSupportPlugin6createERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
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

#if !defined(QT_NO_PRINTER)
  //  QPlatformPrinterSupport *QPlatformPrinterSupportPlugin::create(const
  //      QString &key)
  QPlatformPrinterSupport *create(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformPrinterSupportPluginCall0 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QPlatformPrinterSupport *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformPrinterSupportPluginCall1 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall1>(taken[1]);
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
      CuteQPlatformPrinterSupportPluginCall2 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall2>(taken[2]);
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
      CuteQPlatformPrinterSupportPluginCall3 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall3>(taken[3]);
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
      CuteQPlatformPrinterSupportPluginCall4 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall4>(taken[4]);
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
      CuteQPlatformPrinterSupportPluginCall5 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall5>(taken[5]);
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
      CuteQPlatformPrinterSupportPluginCall6 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall6>(taken[6]);
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
      CuteQPlatformPrinterSupportPluginCall7 call = reinterpret_cast<CuteQPlatformPrinterSupportPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformPrinterSupportPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QPlatformPrinterSupportPlugin10metaObjectEv(
    const QPlatformPrinterSupportPlugin *self) {
  return self->metaObject();
}

//  QString QPlatformPrinterSupportPlugin::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QPlatformPrinterSupportPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformPrinterSupportPlugin::tr(s, c, n));
}

//  QPlatformPrinterSupportPlugin::~QPlatformPrinterSupportPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QPlatformPrinterSupportPluginD1Ev(
    QPlatformPrinterSupportPlugin *self) {
  delete self;
}

//  QPlatformPrinterSupport *QPlatformPrinterSupportPlugin::create(const
//      QString &key)
extern "C" Q_DECL_EXPORT
QPlatformPrinterSupport *ritual_ZN29QPlatformPrinterSupportPlugin6createERK7QString(
    QPlatformPrinterSupportPlugin *self,
    const QString *key) {
  return self->create(*key);
}

//  QPlatformPrinterSupport *QPlatformPrinterSupportPlugin::get()
extern "C" Q_DECL_EXPORT
QPlatformPrinterSupport *ritual_ZN29QPlatformPrinterSupportPlugin3getEv() {
  return QPlatformPrinterSupportPlugin::get();
}

//  a Python function taken by a CuteQPlatformPrinterSupportPlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformPrinterSupportPlugin(
    QPlatformPrinterSupportPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformPrinterSupportPlugin *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_PRINTER)
