//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPinchGesture that Python can take functions over in. Every QPinchGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPinchGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPinchGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPinchGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPinchGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPinchGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPinchGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPinchGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPinchGesture : public QPinchGesture {
public:
  using QPinchGesture::QPinchGesture;
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
      CuteQPinchGestureCall0 call = reinterpret_cast<CuteQPinchGestureCall0>(taken[0]);
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
      CuteQPinchGestureCall1 call = reinterpret_cast<CuteQPinchGestureCall1>(taken[1]);
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
      CuteQPinchGestureCall2 call = reinterpret_cast<CuteQPinchGestureCall2>(taken[2]);
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
      CuteQPinchGestureCall3 call = reinterpret_cast<CuteQPinchGestureCall3>(taken[3]);
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
      CuteQPinchGestureCall4 call = reinterpret_cast<CuteQPinchGestureCall4>(taken[4]);
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
      CuteQPinchGestureCall5 call = reinterpret_cast<CuteQPinchGestureCall5>(taken[5]);
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
      CuteQPinchGestureCall6 call = reinterpret_cast<CuteQPinchGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPinchGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPinchGesture10metaObjectEv(
    const QPinchGesture *self) {
  return self->metaObject();
}

//  void *QPinchGesture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QPinchGesture11qt_metacastEPKc(
    QPinchGesture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPinchGesture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QPinchGesture11qt_metacallEN11QMetaObject4CallEiPPv(
    QPinchGesture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPinchGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPinchGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPinchGesture::tr(s, c, n));
}

//  QPinchGesturePrivate *QPinchGesture::d_func()
extern "C" Q_DECL_EXPORT
QPinchGesturePrivate *ritual_ZN13QPinchGesture6d_funcEv(
    QPinchGesture *self) {
  return self->d_func();
}

//  const QPinchGesturePrivate *QPinchGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QPinchGesturePrivate *ritual_ZNK13QPinchGesture6d_funcEv(
    const QPinchGesture *self) {
  return self->d_func();
}

//  QPinchGesture::QPinchGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QPinchGesture *ritual_ZN13QPinchGestureC1EP7QObject(QObject *parent) {
  return new CuteQPinchGesture(parent);
}

//  QPinchGesture::~QPinchGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGestureD1Ev(QPinchGesture *self) {
  delete self;
}

//  ChangeFlags QPinchGesture::totalChangeFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPinchGesture16totalChangeFlagsEv(
    const QPinchGesture *self) {
  return static_cast<int>(self->totalChangeFlags().toInt());
}

//  void QPinchGesture::setTotalChangeFlags(ChangeFlags value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setTotalChangeFlagsE6QFlagsINS_10ChangeFlagEE(
    QPinchGesture *self,
    int value) {
  self->setTotalChangeFlags(
      QFlags<QPinchGesture::ChangeFlag>::fromInt(value));
}

//  ChangeFlags QPinchGesture::changeFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPinchGesture11changeFlagsEv(const QPinchGesture *self) {
  return static_cast<int>(self->changeFlags().toInt());
}

//  void QPinchGesture::setChangeFlags(ChangeFlags value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setChangeFlagsE6QFlagsINS_10ChangeFlagEE(
    QPinchGesture *self,
    int value) {
  self->setChangeFlags(QFlags<QPinchGesture::ChangeFlag>::fromInt(value));
}

//  QPointF QPinchGesture::startCenterPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture16startCenterPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->startCenterPoint());
}

//  QPointF QPinchGesture::lastCenterPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture15lastCenterPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->lastCenterPoint());
}

//  QPointF QPinchGesture::centerPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture11centerPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->centerPoint());
}

//  void QPinchGesture::setStartCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setStartCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setStartCenterPoint(*value);
}

//  void QPinchGesture::setLastCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture18setLastCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setLastCenterPoint(*value);
}

//  void QPinchGesture::setCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setCenterPoint(*value);
}

//  qreal QPinchGesture::totalScaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture16totalScaleFactorEv(
    const QPinchGesture *self) {
  return self->totalScaleFactor();
}

//  qreal QPinchGesture::lastScaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture15lastScaleFactorEv(
    const QPinchGesture *self) {
  return self->lastScaleFactor();
}

//  qreal QPinchGesture::scaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture11scaleFactorEv(const QPinchGesture *self) {
  return self->scaleFactor();
}

//  void QPinchGesture::setTotalScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setTotalScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setTotalScaleFactor(value);
}

//  void QPinchGesture::setLastScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture18setLastScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setLastScaleFactor(value);
}

//  void QPinchGesture::setScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setScaleFactor(value);
}

//  qreal QPinchGesture::totalRotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture18totalRotationAngleEv(
    const QPinchGesture *self) {
  return self->totalRotationAngle();
}

//  qreal QPinchGesture::lastRotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture17lastRotationAngleEv(
    const QPinchGesture *self) {
  return self->lastRotationAngle();
}

//  qreal QPinchGesture::rotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture13rotationAngleEv(const QPinchGesture *self) {
  return self->rotationAngle();
}

//  void QPinchGesture::setTotalRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture21setTotalRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setTotalRotationAngle(value);
}

//  void QPinchGesture::setLastRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture20setLastRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setLastRotationAngle(value);
}

//  void QPinchGesture::setRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture16setRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setRotationAngle(value);
}

//  a Python function taken by a CuteQPinchGesture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPinchGesture(
    QPinchGesture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPinchGesture *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
