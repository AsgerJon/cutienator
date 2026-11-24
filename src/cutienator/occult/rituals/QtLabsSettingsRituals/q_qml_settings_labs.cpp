//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsSettings/6.12.0/QtLabsSettings/private/qqmlsettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsSettings/6.12.0/QtLabsSettings/private/qqmlsettingsglobal_p.h>
#include <QtLabsSettings/QtLabsSettings>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSettings/6.12.0/QtLabsSettings/private/qqmlsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQmlSettingsLabs may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlSettingsLabs : QQmlSettingsLabs {
  using QQmlSettingsLabs::timerEvent;
  using QQmlSettingsLabs::classBegin;
  using QQmlSettingsLabs::componentComplete;
};

//  A QQmlSettingsLabs that Python can take functions over in. Every QQmlSettingsLabs
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall1)(const void *, int *);
typedef void (*CuteQQmlSettingsLabsCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSettingsLabsCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSettingsLabsCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSettingsLabsCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSettingsLabs : public QQmlSettingsLabs {
public:
  using QQmlSettingsLabs::QQmlSettingsLabs;
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
  //  void QQmlSettingsLabs::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSettingsLabsCall0 call = reinterpret_cast<CuteQQmlSettingsLabsCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQmlSettingsLabs::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQmlSettingsLabs::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSettingsLabsCall1 call = reinterpret_cast<CuteQQmlSettingsLabsCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSettingsLabs::classBegin();
  }

  //  void QQmlSettingsLabs::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSettingsLabsCall2 call = reinterpret_cast<CuteQQmlSettingsLabsCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSettingsLabs::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSettingsLabsCall3 call = reinterpret_cast<CuteQQmlSettingsLabsCall3>(taken[3]);
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
      CuteQQmlSettingsLabsCall4 call = reinterpret_cast<CuteQQmlSettingsLabsCall4>(taken[4]);
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
      CuteQQmlSettingsLabsCall5 call = reinterpret_cast<CuteQQmlSettingsLabsCall5>(taken[5]);
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
      CuteQQmlSettingsLabsCall6 call = reinterpret_cast<CuteQQmlSettingsLabsCall6>(taken[6]);
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
      CuteQQmlSettingsLabsCall7 call = reinterpret_cast<CuteQQmlSettingsLabsCall7>(taken[7]);
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
      CuteQQmlSettingsLabsCall8 call = reinterpret_cast<CuteQQmlSettingsLabsCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSettingsLabs::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlSettingsLabs10metaObjectEv(
    const QQmlSettingsLabs *self) {
  return self->metaObject();
}

//  QString QQmlSettingsLabs::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlSettingsLabs2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSettingsLabs::tr(s, c, n));
}

//  QQmlSettingsLabs::QQmlSettingsLabs(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSettingsLabs *ritual_ZN16QQmlSettingsLabsC1EP7QObject(QObject *parent) {
  return new CuteQQmlSettingsLabs(parent);
}

//  QQmlSettingsLabs::~QQmlSettingsLabs()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabsD1Ev(QQmlSettingsLabs *self) {
  delete self;
}

//  QString QQmlSettingsLabs::category() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlSettingsLabs8categoryEv(
    const QQmlSettingsLabs *self) {
  return new QString(self->category());
}

//  void QQmlSettingsLabs::setCategory(const QString &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs11setCategoryERK7QString(
    QQmlSettingsLabs *self,
    const QString *category) {
  self->setCategory(*category);
}

//  QString QQmlSettingsLabs::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlSettingsLabs8fileNameEv(
    const QQmlSettingsLabs *self) {
  return new QString(self->fileName());
}

//  void QQmlSettingsLabs::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs11setFileNameERK7QString(
    QQmlSettingsLabs *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QVariant QQmlSettingsLabs::value(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlSettingsLabs5valueERK7QStringRK8QVariant(
    const QQmlSettingsLabs *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(*key, *defaultValue));
}

//  void QQmlSettingsLabs::setValue(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs8setValueERK7QStringRK8QVariant(
    QQmlSettingsLabs *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(*key, *value);
}

//  void QQmlSettingsLabs::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs4syncEv(QQmlSettingsLabs *self) {
  self->sync();
}

//  void QQmlSettingsLabs::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs10timerEventEP11QTimerEvent(
    QQmlSettingsLabs *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQmlSettingsLabs::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs10classBeginEv(QQmlSettingsLabs *self) {
  self->classBegin();
}

//  void QQmlSettingsLabs::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlSettingsLabs17componentCompleteEv(
    QQmlSettingsLabs *self) {
  self->componentComplete();
}

//  QQmlSettingsLabs as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlSettingsLabs_QQmlParserStatus(
    QQmlSettingsLabs *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlSettingsLabs, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSettingsLabs(
    QQmlSettingsLabs *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSettingsLabs *>(self)->take(key, call);
}

//  void QQmlSettingsLabs::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlSettingsLabs10timerEventEP11QTimerEvent(
    QQmlSettingsLabs *self,
    QTimerEvent *event) {
  static_cast<OwnQQmlSettingsLabs *>(self)->OwnQQmlSettingsLabs::timerEvent(
      event);
}

//  void QQmlSettingsLabs::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlSettingsLabs10classBeginEv(QQmlSettingsLabs *self) {
  static_cast<OwnQQmlSettingsLabs *>(self)->OwnQQmlSettingsLabs::classBegin();
}

//  void QQmlSettingsLabs::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlSettingsLabs17componentCompleteEv(
    QQmlSettingsLabs *self) {
  static_cast<OwnQQmlSettingsLabs *>(self)->OwnQQmlSettingsLabs::componentComplete();
}
