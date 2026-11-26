//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_VALIDATOR)
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDoubleValidator that Python can take functions over in. Every QDoubleValidator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDoubleValidatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDoubleValidatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleValidatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleValidatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleValidatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleValidatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleValidatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDoubleValidator : public QDoubleValidator {
public:
  using QDoubleValidator::QDoubleValidator;
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
      CuteQDoubleValidatorCall0 call = reinterpret_cast<CuteQDoubleValidatorCall0>(taken[0]);
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
      CuteQDoubleValidatorCall1 call = reinterpret_cast<CuteQDoubleValidatorCall1>(taken[1]);
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
      CuteQDoubleValidatorCall2 call = reinterpret_cast<CuteQDoubleValidatorCall2>(taken[2]);
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
      CuteQDoubleValidatorCall3 call = reinterpret_cast<CuteQDoubleValidatorCall3>(taken[3]);
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
      CuteQDoubleValidatorCall4 call = reinterpret_cast<CuteQDoubleValidatorCall4>(taken[4]);
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
      CuteQDoubleValidatorCall5 call = reinterpret_cast<CuteQDoubleValidatorCall5>(taken[5]);
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
      CuteQDoubleValidatorCall6 call = reinterpret_cast<CuteQDoubleValidatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDoubleValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDoubleValidator10metaObjectEv(
    const QDoubleValidator *self) {
  return self->metaObject();
}

//  void *QDoubleValidator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QDoubleValidator11qt_metacastEPKc(
    QDoubleValidator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDoubleValidator::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QDoubleValidator11qt_metacallEN11QMetaObject4CallEiPPv(
    QDoubleValidator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDoubleValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDoubleValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDoubleValidator::tr(s, c, n));
}

//  QDoubleValidator::QDoubleValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QDoubleValidator *ritual_ZN16QDoubleValidatorC1EP7QObject(QObject *parent) {
  return new CuteQDoubleValidator(parent);
}

//  QDoubleValidator::QDoubleValidator(double bottom, double top, int
//      decimals, QObject *parent)
extern "C" Q_DECL_EXPORT
QDoubleValidator *ritual_ZN16QDoubleValidatorC1EddiP7QObject(
    double bottom,
    double top,
    int decimals,
    QObject *parent) {
  return new CuteQDoubleValidator(bottom, top, decimals, parent);
}

//  QDoubleValidator::~QDoubleValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidatorD1Ev(QDoubleValidator *self) {
  delete self;
}

//  QValidator::State QDoubleValidator::validate(QString &a0, int &a1) const
extern "C" Q_DECL_EXPORT
QValidator::State ritual_ZNK16QDoubleValidator8validateER7QStringRi(
    const QDoubleValidator *self,
    QString *a0,
    int *a1) {
  return self->validate(*a0, *a1);
}

//  void QDoubleValidator::fixup(QString &input) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QDoubleValidator5fixupER7QString(
    const QDoubleValidator *self,
    QString *input) {
  self->fixup(*input);
}

//  void QDoubleValidator::setRange(double bottom, double top, int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator8setRangeEddi(
    QDoubleValidator *self,
    double bottom,
    double top,
    int decimals) {
  self->setRange(bottom, top, decimals);
}

//  void QDoubleValidator::setRange(double bottom, double top)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator8setRangeEdd(
    QDoubleValidator *self,
    double bottom,
    double top) {
  self->setRange(bottom, top);
}

//  void QDoubleValidator::setBottom(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator9setBottomEd(
    QDoubleValidator *self,
    double a0) {
  self->setBottom(a0);
}

//  void QDoubleValidator::setTop(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator6setTopEd(
    QDoubleValidator *self,
    double a0) {
  self->setTop(a0);
}

//  void QDoubleValidator::setDecimals(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator11setDecimalsEi(
    QDoubleValidator *self,
    int a0) {
  self->setDecimals(a0);
}

//  void QDoubleValidator::setNotation(Notation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator11setNotationENS_8NotationE(
    QDoubleValidator *self,
    QDoubleValidator::Notation a0) {
  self->setNotation(a0);
}

//  double QDoubleValidator::bottom() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleValidator6bottomEv(const QDoubleValidator *self) {
  return self->bottom();
}

//  double QDoubleValidator::top() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleValidator3topEv(const QDoubleValidator *self) {
  return self->top();
}

//  int QDoubleValidator::decimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDoubleValidator8decimalsEv(const QDoubleValidator *self) {
  return self->decimals();
}

//  Notation QDoubleValidator::notation() const
extern "C" Q_DECL_EXPORT
QDoubleValidator::Notation ritual_ZNK16QDoubleValidator8notationEv(
    const QDoubleValidator *self) {
  return self->notation();
}

//  void QDoubleValidator::bottomChanged(double bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator13bottomChangedEd(
    QDoubleValidator *self,
    double bottom) {
  self->bottomChanged(bottom);
}

//  void QDoubleValidator::topChanged(double top)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator10topChangedEd(
    QDoubleValidator *self,
    double top) {
  self->topChanged(top);
}

//  void QDoubleValidator::decimalsChanged(int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator15decimalsChangedEi(
    QDoubleValidator *self,
    int decimals) {
  self->decimalsChanged(decimals);
}

//  void QDoubleValidator::notationChanged(QDoubleValidator::Notation
//      notation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator15notationChangedENS_8NotationE(
    QDoubleValidator *self,
    QDoubleValidator::Notation notation) {
  self->notationChanged(notation);
}

//  QDoubleValidatorPrivate *QDoubleValidator::d_func()
extern "C" Q_DECL_EXPORT
QDoubleValidatorPrivate *ritual_ZN16QDoubleValidator6d_funcEv(
    QDoubleValidator *self) {
  return self->d_func();
}

//  const QDoubleValidatorPrivate *QDoubleValidator::d_func() const
extern "C" Q_DECL_EXPORT
const QDoubleValidatorPrivate *ritual_ZNK16QDoubleValidator6d_funcEv(
    const QDoubleValidator *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDoubleValidator, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDoubleValidator(
    QDoubleValidator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDoubleValidator *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_VALIDATOR)
