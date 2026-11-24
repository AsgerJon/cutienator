//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgnomeportalinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(dbus)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgnomeportalinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGnomePortalInterface that Python can take functions over in. Every QGnomePortalInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGnomePortalInterfaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGnomePortalInterfaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGnomePortalInterfaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGnomePortalInterfaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGnomePortalInterfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGnomePortalInterfaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGnomePortalInterfaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGnomePortalInterface : public QGnomePortalInterface {
public:
  using QGnomePortalInterface::QGnomePortalInterface;
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
      CuteQGnomePortalInterfaceCall0 call = reinterpret_cast<CuteQGnomePortalInterfaceCall0>(taken[0]);
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
      CuteQGnomePortalInterfaceCall1 call = reinterpret_cast<CuteQGnomePortalInterfaceCall1>(taken[1]);
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
      CuteQGnomePortalInterfaceCall2 call = reinterpret_cast<CuteQGnomePortalInterfaceCall2>(taken[2]);
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
      CuteQGnomePortalInterfaceCall3 call = reinterpret_cast<CuteQGnomePortalInterfaceCall3>(taken[3]);
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
      CuteQGnomePortalInterfaceCall4 call = reinterpret_cast<CuteQGnomePortalInterfaceCall4>(taken[4]);
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
      CuteQGnomePortalInterfaceCall5 call = reinterpret_cast<CuteQGnomePortalInterfaceCall5>(taken[5]);
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
      CuteQGnomePortalInterfaceCall6 call = reinterpret_cast<CuteQGnomePortalInterfaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGnomePortalInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGnomePortalInterface10metaObjectEv(
    const QGnomePortalInterface *self) {
  return self->metaObject();
}

//  QString QGnomePortalInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGnomePortalInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGnomePortalInterface::tr(s, c, n));
}

//  QGnomePortalInterface::QGnomePortalInterface(QObject *parent)
extern "C" Q_DECL_EXPORT
QGnomePortalInterface *ritual_ZN21QGnomePortalInterfaceC1EP7QObject(
    QObject *parent) {
  return new CuteQGnomePortalInterface(parent);
}

//  QGnomePortalInterface::~QGnomePortalInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterfaceD1Ev(QGnomePortalInterface *self) {
  delete self;
}

//  Qt::ColorScheme QGnomePortalInterface::colorScheme(Qt::ColorScheme
//      fallback) const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK21QGnomePortalInterface11colorSchemeEN2Qt11ColorSchemeE(
    const QGnomePortalInterface *self,
    Qt::ColorScheme fallback) {
  return self->colorScheme(fallback);
}

//  Qt::ContrastPreference
//      QGnomePortalInterface::contrastPreference(Qt::ContrastPreference
//      fallback) const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_ZNK21QGnomePortalInterface18contrastPreferenceEN2Qt18ContrastPreferenceE(
    const QGnomePortalInterface *self,
    Qt::ContrastPreference fallback) {
  return self->contrastPreference(fallback);
}

//  Qt::MotionPreference
//      QGnomePortalInterface::motionPreference(Qt::MotionPreference
//      fallback) const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_ZNK21QGnomePortalInterface16motionPreferenceEN2Qt16MotionPreferenceE(
    const QGnomePortalInterface *self,
    Qt::MotionPreference fallback) {
  return self->motionPreference(fallback);
}

//  void QGnomePortalInterface::querySettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterface13querySettingsEv(
    QGnomePortalInterface *self) {
  self->querySettings();
}

//  void QGnomePortalInterface::updateColorScheme(Qt::ColorScheme
//      colorScheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterface17updateColorSchemeEN2Qt11ColorSchemeE(
    QGnomePortalInterface *self,
    Qt::ColorScheme colorScheme) {
  self->updateColorScheme(colorScheme);
}

//  void QGnomePortalInterface::updateContrast(Qt::ContrastPreference
//      contrast)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterface14updateContrastEN2Qt18ContrastPreferenceE(
    QGnomePortalInterface *self,
    Qt::ContrastPreference contrast) {
  self->updateContrast(contrast);
}

//  void QGnomePortalInterface::updateMotion(Qt::MotionPreference motion)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterface12updateMotionEN2Qt16MotionPreferenceE(
    QGnomePortalInterface *self,
    Qt::MotionPreference motion) {
  self->updateMotion(motion);
}

//  void QGnomePortalInterface::dbusSettingChanged(QDBusListener::Provider
//      a0, QDBusListener::Setting a1, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGnomePortalInterface18dbusSettingChangedEN13QDBusListener8ProviderENS0_7SettingERK8QVariant(
    QGnomePortalInterface *self,
    QDBusListener::Provider a0,
    QDBusListener::Setting a1,
    const QVariant *value) {
  self->dbusSettingChanged(a0, a1, *value);
}

//  a Python function taken by a CuteQGnomePortalInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGnomePortalInterface(
    QGnomePortalInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGnomePortalInterface *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dbus)
