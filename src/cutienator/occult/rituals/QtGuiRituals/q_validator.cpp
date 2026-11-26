//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_VALIDATOR)
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QValidator that Python can take functions over in. Every QValidator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValidatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValidatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValidatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValidatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValidatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValidatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValidatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValidator : public QValidator {
public:
  using QValidator::QValidator;
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
      CuteQValidatorCall0 call = reinterpret_cast<CuteQValidatorCall0>(taken[0]);
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
      CuteQValidatorCall1 call = reinterpret_cast<CuteQValidatorCall1>(taken[1]);
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
      CuteQValidatorCall2 call = reinterpret_cast<CuteQValidatorCall2>(taken[2]);
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
      CuteQValidatorCall3 call = reinterpret_cast<CuteQValidatorCall3>(taken[3]);
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
      CuteQValidatorCall4 call = reinterpret_cast<CuteQValidatorCall4>(taken[4]);
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
      CuteQValidatorCall5 call = reinterpret_cast<CuteQValidatorCall5>(taken[5]);
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
      CuteQValidatorCall6 call = reinterpret_cast<CuteQValidatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QValidator10metaObjectEv(
    const QValidator *self) {
  return self->metaObject();
}

//  void *QValidator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QValidator11qt_metacastEPKc(
    QValidator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QValidator::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QValidator11qt_metacallEN11QMetaObject4CallEiPPv(
    QValidator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  State QValidator::validate(QString &a0, int &a1) const
extern "C" Q_DECL_EXPORT
QValidator::State ritual_ZNK10QValidator8validateER7QStringRi(
    const QValidator *self,
    QString *a0,
    int *a1) {
  return self->validate(*a0, *a1);
}

//  void QValidator::fixup(QString &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QValidator5fixupER7QString(
    const QValidator *self,
    QString *a0) {
  self->fixup(*a0);
}

//  void QValidator::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValidator7changedEv(QValidator *self) {
  self->changed();
}

//  QValidatorPrivate *QValidator::d_func()
extern "C" Q_DECL_EXPORT
QValidatorPrivate *ritual_ZN10QValidator6d_funcEv(QValidator *self) {
  return self->d_func();
}

//  const QValidatorPrivate *QValidator::d_func() const
extern "C" Q_DECL_EXPORT
const QValidatorPrivate *ritual_ZNK10QValidator6d_funcEv(
    const QValidator *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQValidator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValidator(QValidator *self, const char *key, void *call) {
  return static_cast<CuteQValidator *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_VALIDATOR)
