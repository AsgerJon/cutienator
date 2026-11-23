//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QValidator that Python can take functions over in. Every QValidator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQValidatorCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQValidatorCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQValidatorCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQValidatorCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQValidatorCall4)(const void *, QEvent *, int *);
typedef void (*CuteQValidatorCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQValidatorCall6)(const void *, const QMetaMethod *, int *);
class CuteQValidator : public QValidator {
public:
  using QValidator::QValidator;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
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
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQValidatorCall0 call = reinterpret_cast<CuteQValidatorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValidatorCall1 call = reinterpret_cast<CuteQValidatorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValidatorCall2 call = reinterpret_cast<CuteQValidatorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQValidatorCall3 call = reinterpret_cast<CuteQValidatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQValidatorCall4 call = reinterpret_cast<CuteQValidatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValidatorCall5 call = reinterpret_cast<CuteQValidatorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQValidatorCall6 call = reinterpret_cast<CuteQValidatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QValidator10metaObjectEv(
    const QValidator *self) {
  return self->metaObject();
}

//  QString QValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValidator::tr(s, c, n));
}

//  QValidator::~QValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValidatorD1Ev(QValidator *self) {
  delete self;
}

//  void QValidator::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValidator9setLocaleERK7QLocale(
    QValidator *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QValidator::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK10QValidator6localeEv(const QValidator *self) {
  return new QLocale(self->locale());
}

//  a Python function taken by a CuteQValidator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValidator(QValidator *self, const char *key, void *call) {
  return static_cast<CuteQValidator *>(self)->take(key, call);
}
