//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qwinregistry_p.h, Qt 6.12.0, as the Qt
//  of Windows installs it. Kept as it is when the generator runs again.
//  Not written: the constructors taking a 'QWinRegistryKey &&' or a
//  'const wchar_t *', and the signal 'valueChanged'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qwinregistry_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWinRegistryNotifier that Python can take functions over in. Every
//  QWinRegistryNotifier Python makes is one. Each function below asks
//  the Python function handed over for it, and runs Qt's own without
//  one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWinRegistryNotifierCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQWinRegistryNotifierCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWinRegistryNotifierCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWinRegistryNotifierCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQWinRegistryNotifierCall4)(const void *, QEvent *, int *);
typedef void (*CuteQWinRegistryNotifierCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWinRegistryNotifierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWinRegistryNotifier : public QWinRegistryNotifier {
public:
  using QWinRegistryNotifier::QWinRegistryNotifier;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
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
      CuteQWinRegistryNotifierCall0 call = reinterpret_cast<CuteQWinRegistryNotifierCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall1 call = reinterpret_cast<CuteQWinRegistryNotifierCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall2 call = reinterpret_cast<CuteQWinRegistryNotifierCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall3 call = reinterpret_cast<CuteQWinRegistryNotifierCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall4 call = reinterpret_cast<CuteQWinRegistryNotifierCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall5 call = reinterpret_cast<CuteQWinRegistryNotifierCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWinRegistryNotifierCall6 call = reinterpret_cast<CuteQWinRegistryNotifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWinRegistryNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWinRegistryNotifier10metaObjectEv(
    const QWinRegistryNotifier *self) {
  return self->metaObject();
}

//  QString QWinRegistryNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QWinRegistryNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWinRegistryNotifier::tr(s, c, n));
}

//  QWinRegistryNotifier::QWinRegistryNotifier(HKEY parentHandle, const
//      QString &subKey, QObject *parent)
extern "C" Q_DECL_EXPORT
QWinRegistryNotifier *ritual_ZN20QWinRegistryNotifierC1EP6HKEY__RK7QStringP7QObject(
    HKEY parentHandle,
    const QString *subKey,
    QObject *parent) {
  return new CuteQWinRegistryNotifier(parentHandle, *subKey, parent);
}

//  bool QWinRegistryNotifier::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWinRegistryNotifier7isValidEv(
    const QWinRegistryNotifier *self) {
  return self->isValid();
}

//  const QWinRegistryKey &QWinRegistryNotifier::key() const
extern "C" Q_DECL_EXPORT
const QWinRegistryKey *ritual_ZNK20QWinRegistryNotifier3keyEv(
    const QWinRegistryNotifier *self) {
  return &self->key();
}

//  a Python function taken by a CuteQWinRegistryNotifier, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWinRegistryNotifier(
    QWinRegistryNotifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWinRegistryNotifier *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
