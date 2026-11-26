//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qaxis.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::QAxis that Python can take functions over in. Every Qt3DInput::QAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAxis : public Qt3DInput::QAxis {
public:
  using Qt3DInput::QAxis::QAxis;
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
      CuteQt3DInput_QAxisCall0 call = reinterpret_cast<CuteQt3DInput_QAxisCall0>(taken[0]);
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
      CuteQt3DInput_QAxisCall1 call = reinterpret_cast<CuteQt3DInput_QAxisCall1>(taken[1]);
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
      CuteQt3DInput_QAxisCall2 call = reinterpret_cast<CuteQt3DInput_QAxisCall2>(taken[2]);
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
      CuteQt3DInput_QAxisCall3 call = reinterpret_cast<CuteQt3DInput_QAxisCall3>(taken[3]);
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
      CuteQt3DInput_QAxisCall4 call = reinterpret_cast<CuteQt3DInput_QAxisCall4>(taken[4]);
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
      CuteQt3DInput_QAxisCall5 call = reinterpret_cast<CuteQt3DInput_QAxisCall5>(taken[5]);
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
      CuteQt3DInput_QAxisCall6 call = reinterpret_cast<CuteQt3DInput_QAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput5QAxis10metaObjectEv(
    const Qt3DInput::QAxis *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput5QAxis11qt_metacastEPKc(
    Qt3DInput::QAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAxis::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput5QAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput5QAxis2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAxis::tr(s, c, n));
}

//  Qt3DInput::QAxis::QAxis(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxis *ritual_ZN9Qt3DInput5QAxisC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAxis(parent);
}

//  Qt3DInput::QAxis::~QAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5QAxisD1Ev(Qt3DInput::QAxis *self) {
  delete self;
}

//  void Qt3DInput::QAxis::addInput(QAbstractAxisInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5QAxis8addInputEPNS_18QAbstractAxisInputE(
    Qt3DInput::QAxis *self,
    Qt3DInput::QAbstractAxisInput *input) {
  self->addInput(input);
}

//  void Qt3DInput::QAxis::removeInput(QAbstractAxisInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5QAxis11removeInputEPNS_18QAbstractAxisInputE(
    Qt3DInput::QAxis *self,
    Qt3DInput::QAbstractAxisInput *input) {
  self->removeInput(input);
}

//  QList<QAbstractAxisInput *> Qt3DInput::QAxis::inputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAbstractAxisInput *> *ritual_ZNK9Qt3DInput5QAxis6inputsEv(
    const Qt3DInput::QAxis *self) {
  return new QList<Qt3DInput::QAbstractAxisInput *>(self->inputs());
}

//  float Qt3DInput::QAxis::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5QAxis5valueEv(const Qt3DInput::QAxis *self) {
  return self->value();
}

//  void Qt3DInput::QAxis::valueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5QAxis12valueChangedEf(
    Qt3DInput::QAxis *self,
    float value) {
  self->valueChanged(value);
}

//  QAxisPrivate *Qt3DInput::QAxis::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisPrivate *ritual_ZN9Qt3DInput5QAxis6d_funcEv(
    Qt3DInput::QAxis *self) {
  return self->d_func();
}

//  const QAxisPrivate *Qt3DInput::QAxis::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAxisPrivate *ritual_ZNK9Qt3DInput5QAxis6d_funcEv(
    const Qt3DInput::QAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAxis(
    Qt3DInput::QAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAxis *>(self)->take(key, call);
}

//  a QList<Qt3DInput::QAbstractAxisInput *> a ritual of Qt3DInput::QAxis
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QAxis__QList_Qt3DInput_QAbstractAxisInput(
    QList<Qt3DInput::QAbstractAxisInput *> *self) {
  delete self;
}
