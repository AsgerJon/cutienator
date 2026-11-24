//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebviewsettings_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qtwebviewquickglobal_p.h>
#include <QtWebViewQuick/QtWebViewQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebviewsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebViewSettings that Python can take functions over in. Every QQuickWebViewSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewSettingsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewSettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewSettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewSettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewSettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewSettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewSettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebViewSettings : public QQuickWebViewSettings {
public:
  using QQuickWebViewSettings::QQuickWebViewSettings;
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
      CuteQQuickWebViewSettingsCall0 call = reinterpret_cast<CuteQQuickWebViewSettingsCall0>(taken[0]);
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
      CuteQQuickWebViewSettingsCall1 call = reinterpret_cast<CuteQQuickWebViewSettingsCall1>(taken[1]);
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
      CuteQQuickWebViewSettingsCall2 call = reinterpret_cast<CuteQQuickWebViewSettingsCall2>(taken[2]);
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
      CuteQQuickWebViewSettingsCall3 call = reinterpret_cast<CuteQQuickWebViewSettingsCall3>(taken[3]);
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
      CuteQQuickWebViewSettingsCall4 call = reinterpret_cast<CuteQQuickWebViewSettingsCall4>(taken[4]);
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
      CuteQQuickWebViewSettingsCall5 call = reinterpret_cast<CuteQQuickWebViewSettingsCall5>(taken[5]);
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
      CuteQQuickWebViewSettingsCall6 call = reinterpret_cast<CuteQQuickWebViewSettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebViewSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWebViewSettings10metaObjectEv(
    const QQuickWebViewSettings *self) {
  return self->metaObject();
}

//  QString QQuickWebViewSettings::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickWebViewSettings2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebViewSettings::tr(s, c, n));
}

//  void QQuickWebViewSettings::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettings24qt_qmlMarker_uncreatableEv(
    QQuickWebViewSettings *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebViewSettings::~QQuickWebViewSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettingsD1Ev(QQuickWebViewSettings *self) {
  delete self;
}

//  bool QQuickWebViewSettings::localStorageEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickWebViewSettings19localStorageEnabledEv(
    const QQuickWebViewSettings *self) {
  return self->localStorageEnabled();
}

//  bool QQuickWebViewSettings::javaScriptEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickWebViewSettings17javaScriptEnabledEv(
    const QQuickWebViewSettings *self) {
  return self->javaScriptEnabled();
}

//  bool QQuickWebViewSettings::localContentCanAccessFileUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickWebViewSettings29localContentCanAccessFileUrlsEv(
    const QQuickWebViewSettings *self) {
  return self->localContentCanAccessFileUrls();
}

//  bool QQuickWebViewSettings::allowFileAccess() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickWebViewSettings15allowFileAccessEv(
    const QQuickWebViewSettings *self) {
  return self->allowFileAccess();
}

//  void QQuickWebViewSettings::setLocalStorageEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettings22setLocalStorageEnabledEb(
    QQuickWebViewSettings *self,
    bool enabled) {
  self->setLocalStorageEnabled(enabled);
}

//  void QQuickWebViewSettings::setJavaScriptEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettings20setJavaScriptEnabledEb(
    QQuickWebViewSettings *self,
    bool enabled) {
  self->setJavaScriptEnabled(enabled);
}

//  void QQuickWebViewSettings::setAllowFileAccess(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettings18setAllowFileAccessEb(
    QQuickWebViewSettings *self,
    bool enabled) {
  self->setAllowFileAccess(enabled);
}

//  void QQuickWebViewSettings::setLocalContentCanAccessFileUrls(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWebViewSettings32setLocalContentCanAccessFileUrlsEb(
    QQuickWebViewSettings *self,
    bool enabled) {
  self->setLocalContentCanAccessFileUrls(enabled);
}

//  QQuickWebViewSettings::QQuickWebViewSettings(QWebViewSettings
//      *webviewsettings)
extern "C" Q_DECL_EXPORT
QQuickWebViewSettings *ritual_ZN21QQuickWebViewSettingsC1EP16QWebViewSettings(
    QWebViewSettings *webviewsettings) {
  return new CuteQQuickWebViewSettings(webviewsettings);
}

//  a Python function taken by a CuteQQuickWebViewSettings, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebViewSettings(
    QQuickWebViewSettings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebViewSettings *>(self)->take(key, call);
}
