//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlbind_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlMeta/QtQmlMeta>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlbind_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQmlBind may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlBind : QQmlBind {
  using QQmlBind::setTarget;
  using QQmlBind::classBegin;
  using QQmlBind::componentComplete;
};

//  A QQmlBind that Python can take functions over in. Every QQmlBind
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlBindCall0)(const void *, const QQmlProperty *, int *);
typedef void (*CuteQQmlBindCall1)(const void *, int *);
typedef void (*CuteQQmlBindCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlBindCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlBindCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBindCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBindCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBindCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBindCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBindCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlBind : public QQmlBind {
public:
  using QQmlBind::QQmlBind;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
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

  //  void QQmlBind::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlBindCall0 call = reinterpret_cast<CuteQQmlBindCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlBind::setTarget(a0);
  }

  //  void QQmlBind::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlBindCall1 call = reinterpret_cast<CuteQQmlBindCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlBind::classBegin();
  }

  //  void QQmlBind::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlBindCall2 call = reinterpret_cast<CuteQQmlBindCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlBind::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlBindCall3 call = reinterpret_cast<CuteQQmlBindCall3>(taken[3]);
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
      CuteQQmlBindCall4 call = reinterpret_cast<CuteQQmlBindCall4>(taken[4]);
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
      CuteQQmlBindCall5 call = reinterpret_cast<CuteQQmlBindCall5>(taken[5]);
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
      CuteQQmlBindCall6 call = reinterpret_cast<CuteQQmlBindCall6>(taken[6]);
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
      CuteQQmlBindCall7 call = reinterpret_cast<CuteQQmlBindCall7>(taken[7]);
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
      CuteQQmlBindCall8 call = reinterpret_cast<CuteQQmlBindCall8>(taken[8]);
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
      CuteQQmlBindCall9 call = reinterpret_cast<CuteQQmlBindCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlBind::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QQmlBind10metaObjectEv(const QQmlBind *self) {
  return self->metaObject();
}

//  QString QQmlBind::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QQmlBind2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QQmlBind::tr(s, c, n));
}

//  QQmlBind::QQmlBind(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlBind *ritual_ZN8QQmlBindC1EP7QObject(QObject *parent) {
  return new CuteQQmlBind(parent);
}

//  QQmlBind::~QQmlBind()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBindD1Ev(QQmlBind *self) {
  delete self;
}

//  bool QQmlBind::when() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlBind4whenEv(const QQmlBind *self) {
  return self->when();
}

//  void QQmlBind::setWhen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind7setWhenEb(QQmlBind *self, bool a0) {
  self->setWhen(a0);
}

//  QObject *QQmlBind::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QQmlBind6objectEv(const QQmlBind *self) {
  return self->object();
}

//  void QQmlBind::setObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind9setObjectEP7QObject(QQmlBind *self, QObject *a0) {
  self->setObject(a0);
}

//  QString QQmlBind::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlBind8propertyEv(const QQmlBind *self) {
  return new QString(self->property());
}

//  void QQmlBind::setProperty(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind11setPropertyERK7QString(
    QQmlBind *self,
    const QString *a0) {
  self->setProperty(*a0);
}

//  QVariant QQmlBind::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QQmlBind5valueEv(const QQmlBind *self) {
  return new QVariant(self->value());
}

//  void QQmlBind::setValue(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind8setValueERK8QVariant(
    QQmlBind *self,
    const QVariant *a0) {
  self->setValue(*a0);
}

//  bool QQmlBind::delayed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlBind7delayedEv(const QQmlBind *self) {
  return self->delayed();
}

//  void QQmlBind::setDelayed(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind10setDelayedEb(QQmlBind *self, bool a0) {
  self->setDelayed(a0);
}

//  RestorationMode QQmlBind::restoreMode() const
extern "C" Q_DECL_EXPORT
QQmlBind::RestorationMode ritual_ZNK8QQmlBind11restoreModeEv(
    const QQmlBind *self) {
  return self->restoreMode();
}

//  void QQmlBind::setRestoreMode(RestorationMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind14setRestoreModeENS_15RestorationModeE(
    QQmlBind *self,
    QQmlBind::RestorationMode a0) {
  self->setRestoreMode(a0);
}

//  void QQmlBind::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind9setTargetERK12QQmlProperty(
    QQmlBind *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  void QQmlBind::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind10classBeginEv(QQmlBind *self) {
  self->classBegin();
}

//  void QQmlBind::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind17componentCompleteEv(QQmlBind *self) {
  self->componentComplete();
}

//  void QQmlBind::prepareEval()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind11prepareEvalEv(QQmlBind *self) {
  self->prepareEval();
}

//  void QQmlBind::eval()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind4evalEv(QQmlBind *self) {
  self->eval();
}

//  void QQmlBind::targetValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlBind18targetValueChangedEv(QQmlBind *self) {
  self->targetValueChanged();
}

//  QQmlBind as the QQmlPropertyValueSource it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueSource *ritual_cast_QQmlBind_QQmlPropertyValueSource(
    QQmlBind *self) {
  return static_cast<QQmlPropertyValueSource *>(self);
}

//  QQmlBind as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlBind_QQmlParserStatus(QQmlBind *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlBind, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlBind(QQmlBind *self, const char *key, void *call) {
  return static_cast<CuteQQmlBind *>(self)->take(key, call);
}

//  void QQmlBind::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QQmlBind9setTargetERK12QQmlProperty(
    QQmlBind *self,
    const QQmlProperty *a0) {
  static_cast<OwnQQmlBind *>(self)->OwnQQmlBind::setTarget(*a0);
}

//  void QQmlBind::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QQmlBind10classBeginEv(QQmlBind *self) {
  static_cast<OwnQQmlBind *>(self)->OwnQQmlBind::classBegin();
}

//  void QQmlBind::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QQmlBind17componentCompleteEv(QQmlBind *self) {
  static_cast<OwnQQmlBind *>(self)->OwnQQmlBind::componentComplete();
}
