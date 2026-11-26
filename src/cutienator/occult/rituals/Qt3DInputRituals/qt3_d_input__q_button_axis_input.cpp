//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qbuttonaxisinput.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qbuttonaxisinput.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DInput::QButtonAxisInput that Python can take functions over in. Every Qt3DInput::QButtonAxisInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QButtonAxisInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QButtonAxisInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QButtonAxisInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QButtonAxisInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QButtonAxisInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QButtonAxisInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QButtonAxisInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QButtonAxisInput : public Qt3DInput::QButtonAxisInput {
public:
  using Qt3DInput::QButtonAxisInput::QButtonAxisInput;
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
      CuteQt3DInput_QButtonAxisInputCall0 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall0>(taken[0]);
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
      CuteQt3DInput_QButtonAxisInputCall1 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall1>(taken[1]);
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
      CuteQt3DInput_QButtonAxisInputCall2 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall2>(taken[2]);
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
      CuteQt3DInput_QButtonAxisInputCall3 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall3>(taken[3]);
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
      CuteQt3DInput_QButtonAxisInputCall4 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall4>(taken[4]);
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
      CuteQt3DInput_QButtonAxisInputCall5 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall5>(taken[5]);
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
      CuteQt3DInput_QButtonAxisInputCall6 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QButtonAxisInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput16QButtonAxisInput10metaObjectEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QButtonAxisInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput16QButtonAxisInput11qt_metacastEPKc(
    Qt3DInput::QButtonAxisInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QButtonAxisInput::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput16QButtonAxisInput11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QButtonAxisInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QButtonAxisInput::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput16QButtonAxisInput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QButtonAxisInput::tr(s, c, n));
}

//  Qt3DInput::QButtonAxisInput::QButtonAxisInput(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QButtonAxisInput *ritual_ZN9Qt3DInput16QButtonAxisInputC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QButtonAxisInput(parent);
}

//  Qt3DInput::QButtonAxisInput::~QButtonAxisInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInputD1Ev(
    Qt3DInput::QButtonAxisInput *self) {
  delete self;
}

//  float Qt3DInput::QButtonAxisInput::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QButtonAxisInput5scaleEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return self->scale();
}

//  QList<int> Qt3DInput::QButtonAxisInput::buttons() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput16QButtonAxisInput7buttonsEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return new QList<int>(self->buttons());
}

//  float Qt3DInput::QButtonAxisInput::acceleration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QButtonAxisInput12accelerationEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return self->acceleration();
}

//  float Qt3DInput::QButtonAxisInput::deceleration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QButtonAxisInput12decelerationEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return self->deceleration();
}

//  void Qt3DInput::QButtonAxisInput::setScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput8setScaleEf(
    Qt3DInput::QButtonAxisInput *self,
    float scale) {
  self->setScale(scale);
}

//  void Qt3DInput::QButtonAxisInput::setButtons(const QList<int> &buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput10setButtonsERK5QListIiE(
    Qt3DInput::QButtonAxisInput *self,
    const QList<int> *buttons) {
  self->setButtons(*buttons);
}

//  void Qt3DInput::QButtonAxisInput::setAcceleration(float acceleration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput15setAccelerationEf(
    Qt3DInput::QButtonAxisInput *self,
    float acceleration) {
  self->setAcceleration(acceleration);
}

//  void Qt3DInput::QButtonAxisInput::setDeceleration(float deceleration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput15setDecelerationEf(
    Qt3DInput::QButtonAxisInput *self,
    float deceleration) {
  self->setDeceleration(deceleration);
}

//  void Qt3DInput::QButtonAxisInput::scaleChanged(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput12scaleChangedEf(
    Qt3DInput::QButtonAxisInput *self,
    float scale) {
  self->scaleChanged(scale);
}

//  void Qt3DInput::QButtonAxisInput::buttonsChanged(const QList<int>
//      &buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput14buttonsChangedERK5QListIiE(
    Qt3DInput::QButtonAxisInput *self,
    const QList<int> *buttons) {
  self->buttonsChanged(*buttons);
}

//  void Qt3DInput::QButtonAxisInput::accelerationChanged(float acceleration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput19accelerationChangedEf(
    Qt3DInput::QButtonAxisInput *self,
    float acceleration) {
  self->accelerationChanged(acceleration);
}

//  void Qt3DInput::QButtonAxisInput::decelerationChanged(float deceleration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QButtonAxisInput19decelerationChangedEf(
    Qt3DInput::QButtonAxisInput *self,
    float deceleration) {
  self->decelerationChanged(deceleration);
}

//  QButtonAxisInputPrivate *Qt3DInput::QButtonAxisInput::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QButtonAxisInputPrivate *ritual_ZN9Qt3DInput16QButtonAxisInput6d_funcEv(
    Qt3DInput::QButtonAxisInput *self) {
  return self->d_func();
}

//  const QButtonAxisInputPrivate *Qt3DInput::QButtonAxisInput::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QButtonAxisInputPrivate *ritual_ZNK9Qt3DInput16QButtonAxisInput6d_funcEv(
    const Qt3DInput::QButtonAxisInput *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QButtonAxisInput, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QButtonAxisInput(
    Qt3DInput::QButtonAxisInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QButtonAxisInput *>(self)->take(key, call);
}

//  a QList<int> a ritual of Qt3DInput::QButtonAxisInput gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QButtonAxisInput__QList_int(QList<int> *self) {
  delete self;
}
