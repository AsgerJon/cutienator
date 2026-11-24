//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickplatformtheme_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickplatformtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPlatformTheme that Python can take functions over in. Every QQuickPlatformTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformThemeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformThemeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformThemeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformThemeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformThemeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformThemeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformThemeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformTheme : public QQuickPlatformTheme {
public:
  using QQuickPlatformTheme::QQuickPlatformTheme;
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
      CuteQQuickPlatformThemeCall0 call = reinterpret_cast<CuteQQuickPlatformThemeCall0>(taken[0]);
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
      CuteQQuickPlatformThemeCall1 call = reinterpret_cast<CuteQQuickPlatformThemeCall1>(taken[1]);
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
      CuteQQuickPlatformThemeCall2 call = reinterpret_cast<CuteQQuickPlatformThemeCall2>(taken[2]);
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
      CuteQQuickPlatformThemeCall3 call = reinterpret_cast<CuteQQuickPlatformThemeCall3>(taken[3]);
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
      CuteQQuickPlatformThemeCall4 call = reinterpret_cast<CuteQQuickPlatformThemeCall4>(taken[4]);
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
      CuteQQuickPlatformThemeCall5 call = reinterpret_cast<CuteQQuickPlatformThemeCall5>(taken[5]);
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
      CuteQQuickPlatformThemeCall6 call = reinterpret_cast<CuteQQuickPlatformThemeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPlatformTheme10metaObjectEv(
    const QQuickPlatformTheme *self) {
  return self->metaObject();
}

//  QString QQuickPlatformTheme::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickPlatformTheme2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformTheme::tr(s, c, n));
}

//  const QMetaObject *QQuickPlatformTheme::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN19QQuickPlatformTheme20qmlExtendedNamespaceEv() {
  return QQuickPlatformTheme::qmlExtendedNamespace();
}

//  void QQuickPlatformTheme::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPlatformTheme30qt_qmlMarker_extendedNamespaceEv(
    QQuickPlatformTheme *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  void QQuickPlatformTheme::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPlatformTheme22qt_qmlMarker_singletonEv(
    QQuickPlatformTheme *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickPlatformTheme::QQuickPlatformTheme(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformTheme *ritual_ZN19QQuickPlatformThemeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformTheme(parent);
}

//  QVariant QQuickPlatformTheme::themeHint(QPlatformTheme::ThemeHint
//      themeHint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickPlatformTheme9themeHintEN14QPlatformTheme9ThemeHintE(
    const QQuickPlatformTheme *self,
    QPlatformTheme::ThemeHint themeHint) {
  return new QVariant(self->themeHint(themeHint));
}

//  QVariant QQuickPlatformTheme::getThemeHint(QPlatformTheme::ThemeHint
//      themeHint)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QQuickPlatformTheme12getThemeHintEN14QPlatformTheme9ThemeHintE(
    QPlatformTheme::ThemeHint themeHint) {
  return new QVariant(QQuickPlatformTheme::getThemeHint(themeHint));
}

//  a Python function taken by a CuteQQuickPlatformTheme, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformTheme(
    QQuickPlatformTheme *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformTheme *>(self)->take(key, call);
}
