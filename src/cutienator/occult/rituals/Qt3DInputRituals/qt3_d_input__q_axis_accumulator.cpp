//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qaxisaccumulator.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qaxisaccumulator.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QAxisAccumulator that Python can take functions over in. Every Qt3DInput::QAxisAccumulator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisAccumulatorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisAccumulatorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisAccumulatorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisAccumulatorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisAccumulatorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisAccumulatorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisAccumulatorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAxisAccumulator : public Qt3DInput::QAxisAccumulator {
public:
  using Qt3DInput::QAxisAccumulator::QAxisAccumulator;
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
      CuteQt3DInput_QAxisAccumulatorCall0 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall0>(taken[0]);
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
      CuteQt3DInput_QAxisAccumulatorCall1 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall1>(taken[1]);
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
      CuteQt3DInput_QAxisAccumulatorCall2 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall2>(taken[2]);
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
      CuteQt3DInput_QAxisAccumulatorCall3 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall3>(taken[3]);
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
      CuteQt3DInput_QAxisAccumulatorCall4 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall4>(taken[4]);
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
      CuteQt3DInput_QAxisAccumulatorCall5 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall5>(taken[5]);
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
      CuteQt3DInput_QAxisAccumulatorCall6 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAxisAccumulator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput16QAxisAccumulator10metaObjectEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAxisAccumulator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput16QAxisAccumulator11qt_metacastEPKc(
    Qt3DInput::QAxisAccumulator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAxisAccumulator::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput16QAxisAccumulator11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAxisAccumulator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAxisAccumulator::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput16QAxisAccumulator2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAxisAccumulator::tr(s, c, n));
}

//  Qt3DInput::QAxisAccumulator::QAxisAccumulator(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulator *ritual_ZN9Qt3DInput16QAxisAccumulatorC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAxisAccumulator(parent);
}

//  Qt3DInput::QAxisAccumulator::~QAxisAccumulator()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulatorD1Ev(
    Qt3DInput::QAxisAccumulator *self) {
  delete self;
}

//  Qt3DInput::QAxis *Qt3DInput::QAxisAccumulator::sourceAxis() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxis *ritual_ZNK9Qt3DInput16QAxisAccumulator10sourceAxisEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->sourceAxis();
}

//  SourceAxisType Qt3DInput::QAxisAccumulator::sourceAxisType() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulator::SourceAxisType ritual_ZNK9Qt3DInput16QAxisAccumulator14sourceAxisTypeEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->sourceAxisType();
}

//  float Qt3DInput::QAxisAccumulator::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QAxisAccumulator5valueEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->value();
}

//  float Qt3DInput::QAxisAccumulator::velocity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QAxisAccumulator8velocityEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->velocity();
}

//  float Qt3DInput::QAxisAccumulator::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput16QAxisAccumulator5scaleEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->scale();
}

//  void Qt3DInput::QAxisAccumulator::setSourceAxis(Qt3DInput::QAxis
//      *sourceAxis)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator13setSourceAxisEPNS_5QAxisE(
    Qt3DInput::QAxisAccumulator *self,
    Qt3DInput::QAxis *sourceAxis) {
  self->setSourceAxis(sourceAxis);
}

//  void Qt3DInput::QAxisAccumulator::setSourceAxisType(QAxisAccumulator::Sou
//      rceAxisType sourceAxisType)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator17setSourceAxisTypeENS0_14SourceAxisTypeE(
    Qt3DInput::QAxisAccumulator *self,
    Qt3DInput::QAxisAccumulator::SourceAxisType sourceAxisType) {
  self->setSourceAxisType(sourceAxisType);
}

//  void Qt3DInput::QAxisAccumulator::setScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator8setScaleEf(
    Qt3DInput::QAxisAccumulator *self,
    float scale) {
  self->setScale(scale);
}

//  void Qt3DInput::QAxisAccumulator::sourceAxisChanged(Qt3DInput::QAxis
//      *sourceAxis)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator17sourceAxisChangedEPNS_5QAxisE(
    Qt3DInput::QAxisAccumulator *self,
    Qt3DInput::QAxis *sourceAxis) {
  self->sourceAxisChanged(sourceAxis);
}

//  void Qt3DInput::QAxisAccumulator::sourceAxisTypeChanged(QAxisAccumulator:
//      :SourceAxisType sourceAxisType)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator21sourceAxisTypeChangedENS0_14SourceAxisTypeE(
    Qt3DInput::QAxisAccumulator *self,
    Qt3DInput::QAxisAccumulator::SourceAxisType sourceAxisType) {
  self->sourceAxisTypeChanged(sourceAxisType);
}

//  void Qt3DInput::QAxisAccumulator::valueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator12valueChangedEf(
    Qt3DInput::QAxisAccumulator *self,
    float value) {
  self->valueChanged(value);
}

//  void Qt3DInput::QAxisAccumulator::velocityChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator15velocityChangedEf(
    Qt3DInput::QAxisAccumulator *self,
    float value) {
  self->velocityChanged(value);
}

//  void Qt3DInput::QAxisAccumulator::scaleChanged(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput16QAxisAccumulator12scaleChangedEf(
    Qt3DInput::QAxisAccumulator *self,
    float scale) {
  self->scaleChanged(scale);
}

//  QAxisAccumulatorPrivate *Qt3DInput::QAxisAccumulator::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulatorPrivate *ritual_ZN9Qt3DInput16QAxisAccumulator6d_funcEv(
    Qt3DInput::QAxisAccumulator *self) {
  return self->d_func();
}

//  const QAxisAccumulatorPrivate *Qt3DInput::QAxisAccumulator::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAxisAccumulatorPrivate *ritual_ZNK9Qt3DInput16QAxisAccumulator6d_funcEv(
    const Qt3DInput::QAxisAccumulator *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAxisAccumulator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAxisAccumulator(
    Qt3DInput::QAxisAccumulator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAxisAccumulator *>(self)->take(key, call);
}
