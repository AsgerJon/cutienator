//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_VALIDATOR)
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIntValidator that Python can take functions over in. Every QIntValidator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIntValidatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIntValidatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIntValidatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIntValidatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIntValidatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIntValidatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIntValidatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQIntValidator : public QIntValidator {
public:
  using QIntValidator::QIntValidator;
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
      CuteQIntValidatorCall0 call = reinterpret_cast<CuteQIntValidatorCall0>(taken[0]);
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
      CuteQIntValidatorCall1 call = reinterpret_cast<CuteQIntValidatorCall1>(taken[1]);
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
      CuteQIntValidatorCall2 call = reinterpret_cast<CuteQIntValidatorCall2>(taken[2]);
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
      CuteQIntValidatorCall3 call = reinterpret_cast<CuteQIntValidatorCall3>(taken[3]);
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
      CuteQIntValidatorCall4 call = reinterpret_cast<CuteQIntValidatorCall4>(taken[4]);
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
      CuteQIntValidatorCall5 call = reinterpret_cast<CuteQIntValidatorCall5>(taken[5]);
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
      CuteQIntValidatorCall6 call = reinterpret_cast<CuteQIntValidatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QIntValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QIntValidator10metaObjectEv(
    const QIntValidator *self) {
  return self->metaObject();
}

//  QString QIntValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QIntValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIntValidator::tr(s, c, n));
}

//  QIntValidator::QIntValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QIntValidator *ritual_ZN13QIntValidatorC1EP7QObject(QObject *parent) {
  return new CuteQIntValidator(parent);
}

//  QIntValidator::QIntValidator(int bottom, int top, QObject *parent)
extern "C" Q_DECL_EXPORT
QIntValidator *ritual_ZN13QIntValidatorC1EiiP7QObject(
    int bottom,
    int top,
    QObject *parent) {
  return new CuteQIntValidator(bottom, top, parent);
}

//  QIntValidator::~QIntValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidatorD1Ev(QIntValidator *self) {
  delete self;
}

//  void QIntValidator::setBottom(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator9setBottomEi(QIntValidator *self, int a0) {
  self->setBottom(a0);
}

//  void QIntValidator::setTop(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator6setTopEi(QIntValidator *self, int a0) {
  self->setTop(a0);
}

//  void QIntValidator::setRange(int bottom, int top)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator8setRangeEii(
    QIntValidator *self,
    int bottom,
    int top) {
  self->setRange(bottom, top);
}

//  int QIntValidator::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QIntValidator6bottomEv(const QIntValidator *self) {
  return self->bottom();
}

//  int QIntValidator::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QIntValidator3topEv(const QIntValidator *self) {
  return self->top();
}

//  a Python function taken by a CuteQIntValidator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIntValidator(
    QIntValidator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIntValidator *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_VALIDATOR)
