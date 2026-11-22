//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRegularExpressionValidator that Python can take functions over in. Every QRegularExpressionValidator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRegularExpressionValidatorCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQRegularExpressionValidatorCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQRegularExpressionValidatorCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQRegularExpressionValidatorCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQRegularExpressionValidatorCall4)(const void *, QEvent *, int *);
typedef void (*CuteQRegularExpressionValidatorCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQRegularExpressionValidatorCall6)(const void *, const QMetaMethod *, int *);
class CuteQRegularExpressionValidator : public QRegularExpressionValidator {
public:
  using QRegularExpressionValidator::QRegularExpressionValidator;
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
      CuteQRegularExpressionValidatorCall0 call = reinterpret_cast<CuteQRegularExpressionValidatorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall1 call = reinterpret_cast<CuteQRegularExpressionValidatorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall2 call = reinterpret_cast<CuteQRegularExpressionValidatorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall3 call = reinterpret_cast<CuteQRegularExpressionValidatorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall4 call = reinterpret_cast<CuteQRegularExpressionValidatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall5 call = reinterpret_cast<CuteQRegularExpressionValidatorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRegularExpressionValidatorCall6 call = reinterpret_cast<CuteQRegularExpressionValidatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QRegularExpressionValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QRegularExpressionValidator10metaObjectEv(
    const QRegularExpressionValidator *self) {
  return self->metaObject();
}

//  QString QRegularExpressionValidator::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QRegularExpressionValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRegularExpressionValidator::tr(s, c, n));
}

//  QRegularExpressionValidator::QRegularExpressionValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QRegularExpressionValidator *ritual_ZN27QRegularExpressionValidatorC1EP7QObject(
    QObject *parent) {
  return new CuteQRegularExpressionValidator(parent);
}

//  QRegularExpressionValidator::QRegularExpressionValidator(const
//      QRegularExpression &re, QObject *parent)
extern "C" Q_DECL_EXPORT
QRegularExpressionValidator *ritual_ZN27QRegularExpressionValidatorC1ERK18QRegularExpressionP7QObject(
    const QRegularExpression *re,
    QObject *parent) {
  return new CuteQRegularExpressionValidator(*re, parent);
}

//  QRegularExpressionValidator::~QRegularExpressionValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRegularExpressionValidatorD1Ev(
    QRegularExpressionValidator *self) {
  delete self;
}

//  QRegularExpression QRegularExpressionValidator::regularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK27QRegularExpressionValidator17regularExpressionEv(
    const QRegularExpressionValidator *self) {
  return new QRegularExpression(self->regularExpression());
}

//  void QRegularExpressionValidator::setRegularExpression(const
//      QRegularExpression &re)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRegularExpressionValidator20setRegularExpressionERK18QRegularExpression(
    QRegularExpressionValidator *self,
    const QRegularExpression *re) {
  self->setRegularExpression(*re);
}

//  a Python function taken by a CuteQRegularExpressionValidator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRegularExpressionValidator(
    QRegularExpressionValidator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRegularExpressionValidator *>(self)->take(key, call);
}
