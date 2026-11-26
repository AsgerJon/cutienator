//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCore/6.12.0/QtQmlCore/private/qqmlsettings_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlCore/qtqmlcoreexports.h>
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#if QT_CONFIG(settings)
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#include <QtQmlCore/QtQmlCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQmlSettings may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlSettings : QQmlSettings {
  using QQmlSettings::timerEvent;
  using QQmlSettings::classBegin;
  using QQmlSettings::componentComplete;
};

//  A QQmlSettings that Python can take functions over in. Every QQmlSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall1)(const void *, int *);
typedef void (*CuteQQmlSettingsCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSettingsCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSettingsCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSettings : public QQmlSettings {
public:
  using QQmlSettings::QQmlSettings;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQmlSettings::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSettingsCall0 call = reinterpret_cast<CuteQQmlSettingsCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQmlSettings::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQmlSettings::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSettingsCall1 call = reinterpret_cast<CuteQQmlSettingsCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSettings::classBegin();
  }

  //  void QQmlSettings::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSettingsCall2 call = reinterpret_cast<CuteQQmlSettingsCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSettings::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSettingsCall3 call = reinterpret_cast<CuteQQmlSettingsCall3>(taken[3]);
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
      CuteQQmlSettingsCall4 call = reinterpret_cast<CuteQQmlSettingsCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlSettingsCall5 call = reinterpret_cast<CuteQQmlSettingsCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlSettingsCall6 call = reinterpret_cast<CuteQQmlSettingsCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlSettingsCall7 call = reinterpret_cast<CuteQQmlSettingsCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlSettingsCall8 call = reinterpret_cast<CuteQQmlSettingsCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQmlSettings10metaObjectEv(
    const QQmlSettings *self) {
  return self->metaObject();
}

//  void *QQmlSettings::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQmlSettings11qt_metacastEPKc(
    QQmlSettings *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlSettings::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQmlSettings11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlSettings *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlSettings::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQmlSettings2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSettings::tr(s, c, n));
}

//  QQmlSettingsPrivate *QQmlSettings::d_func()
extern "C" Q_DECL_EXPORT
QQmlSettingsPrivate *ritual_ZN12QQmlSettings6d_funcEv(QQmlSettings *self) {
  return self->d_func();
}

//  const QQmlSettingsPrivate *QQmlSettings::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSettingsPrivate *ritual_ZNK12QQmlSettings6d_funcEv(
    const QQmlSettings *self) {
  return self->d_func();
}

//  QQmlSettings::QQmlSettings(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSettings *ritual_ZN12QQmlSettingsC1EP7QObject(QObject *parent) {
  return new CuteQQmlSettings(parent);
}

//  QQmlSettings::~QQmlSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettingsD1Ev(QQmlSettings *self) {
  delete self;
}

//  QString QQmlSettings::category() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlSettings8categoryEv(const QQmlSettings *self) {
  return new QString(self->category());
}

//  void QQmlSettings::setCategory(const QString &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings11setCategoryERK7QString(
    QQmlSettings *self,
    const QString *category) {
  self->setCategory(*category);
}

//  QUrl QQmlSettings::location() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQmlSettings8locationEv(const QQmlSettings *self) {
  return new QUrl(self->location());
}

//  void QQmlSettings::setLocation(const QUrl &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings11setLocationERK4QUrl(
    QQmlSettings *self,
    const QUrl *location) {
  self->setLocation(*location);
}

//  QVariant QQmlSettings::value(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QQmlSettings5valueERK7QStringRK8QVariant(
    const QQmlSettings *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(*key, *defaultValue));
}

//  void QQmlSettings::setValue(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings8setValueERK7QStringRK8QVariant(
    QQmlSettings *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(*key, *value);
}

//  void QQmlSettings::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings4syncEv(QQmlSettings *self) {
  self->sync();
}

//  void QQmlSettings::categoryChanged(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings15categoryChangedERK7QString(
    QQmlSettings *self,
    const QString *arg) {
  self->categoryChanged(*arg);
}

//  void QQmlSettings::locationChanged(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings15locationChangedERK4QUrl(
    QQmlSettings *self,
    const QUrl *arg) {
  self->locationChanged(*arg);
}

//  void QQmlSettings::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings10timerEventEP11QTimerEvent(
    QQmlSettings *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQmlSettings::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings10classBeginEv(QQmlSettings *self) {
  self->classBegin();
}

//  void QQmlSettings::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlSettings17componentCompleteEv(QQmlSettings *self) {
  self->componentComplete();
}

//  QQmlSettings as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlSettings_QQmlParserStatus(
    QQmlSettings *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlSettings, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSettings(
    QQmlSettings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSettings *>(self)->take(key, call);
}

//  void QQmlSettings::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlSettings10timerEventEP11QTimerEvent(
    QQmlSettings *self,
    QTimerEvent *event) {
  static_cast<OwnQQmlSettings *>(self)->OwnQQmlSettings::timerEvent(event);
}

//  void QQmlSettings::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlSettings10classBeginEv(QQmlSettings *self) {
  static_cast<OwnQQmlSettings *>(self)->OwnQQmlSettings::classBegin();
}

//  void QQmlSettings::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQmlSettings17componentCompleteEv(QQmlSettings *self) {
  static_cast<OwnQQmlSettings *>(self)->OwnQQmlSettings::componentComplete();
}

#endif  // QT_CONFIG(settings)
