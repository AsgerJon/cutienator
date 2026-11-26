//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGesture that Python can take functions over in. Every QGesture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGestureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGestureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGesture : public QGesture {
public:
  using QGesture::QGesture;
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
      CuteQGestureCall0 call = reinterpret_cast<CuteQGestureCall0>(taken[0]);
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
      CuteQGestureCall1 call = reinterpret_cast<CuteQGestureCall1>(taken[1]);
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
      CuteQGestureCall2 call = reinterpret_cast<CuteQGestureCall2>(taken[2]);
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
      CuteQGestureCall3 call = reinterpret_cast<CuteQGestureCall3>(taken[3]);
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
      CuteQGestureCall4 call = reinterpret_cast<CuteQGestureCall4>(taken[4]);
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
      CuteQGestureCall5 call = reinterpret_cast<CuteQGestureCall5>(taken[5]);
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
      CuteQGestureCall6 call = reinterpret_cast<CuteQGestureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QGesture10metaObjectEv(const QGesture *self) {
  return self->metaObject();
}

//  void *QGesture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QGesture11qt_metacastEPKc(QGesture *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGesture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QGesture11qt_metacallEN11QMetaObject4CallEiPPv(
    QGesture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QGesture2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QGesture::tr(s, c, n));
}

//  QGesturePrivate *QGesture::d_func()
extern "C" Q_DECL_EXPORT
QGesturePrivate *ritual_ZN8QGesture6d_funcEv(QGesture *self) {
  return self->d_func();
}

//  const QGesturePrivate *QGesture::d_func() const
extern "C" Q_DECL_EXPORT
const QGesturePrivate *ritual_ZNK8QGesture6d_funcEv(const QGesture *self) {
  return self->d_func();
}

//  QGesture::QGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN8QGestureC1EP7QObject(QObject *parent) {
  return new CuteQGesture(parent);
}

//  QGesture::~QGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGestureD1Ev(QGesture *self) {
  delete self;
}

//  Qt::GestureType QGesture::gestureType() const
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZNK8QGesture11gestureTypeEv(const QGesture *self) {
  return self->gestureType();
}

//  Qt::GestureState QGesture::state() const
extern "C" Q_DECL_EXPORT
Qt::GestureState ritual_ZNK8QGesture5stateEv(const QGesture *self) {
  return self->state();
}

//  QPointF QGesture::hotSpot() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QGesture7hotSpotEv(const QGesture *self) {
  return new QPointF(self->hotSpot());
}

//  void QGesture::setHotSpot(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture10setHotSpotERK7QPointF(
    QGesture *self,
    const QPointF *value) {
  self->setHotSpot(*value);
}

//  bool QGesture::hasHotSpot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QGesture10hasHotSpotEv(const QGesture *self) {
  return self->hasHotSpot();
}

//  void QGesture::unsetHotSpot()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture12unsetHotSpotEv(QGesture *self) {
  self->unsetHotSpot();
}

//  void QGesture::setGestureCancelPolicy(GestureCancelPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGesture22setGestureCancelPolicyENS_19GestureCancelPolicyE(
    QGesture *self,
    QGesture::GestureCancelPolicy policy) {
  self->setGestureCancelPolicy(policy);
}

//  GestureCancelPolicy QGesture::gestureCancelPolicy() const
extern "C" Q_DECL_EXPORT
QGesture::GestureCancelPolicy ritual_ZNK8QGesture19gestureCancelPolicyEv(
    const QGesture *self) {
  return self->gestureCancelPolicy();
}

//  QGesture::QGesture(QGesturePrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN8QGestureC1ER15QGesturePrivateP7QObject(
    QGesturePrivate *dd,
    QObject *parent) {
  return new CuteQGesture(*dd, parent);
}

//  a Python function taken by a CuteQGesture, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGesture(QGesture *self, const char *key, void *call) {
  return static_cast<CuteQGesture *>(self)->take(key, call);
}

//  QList<QGesture *>::QList()
extern "C" Q_DECL_EXPORT
QList<QGesture *> *ritual_list_make_QGesture_ptr() {
  return new QList<QGesture *>();
}

//  void QList<QGesture *>::append(const QGesture * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGesture_ptr(
    QList<QGesture *> *self,
    QGesture *element) {
  self->append(element);
}

//  qsizetype QList<QGesture *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGesture_ptr(const QList<QGesture *> *self) {
  return self->size();
}

//  const QGesture * &QList<QGesture *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGesture *ritual_list_at_QGesture_ptr(
    const QList<QGesture *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QGesture *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGesture_ptr(QList<QGesture *> *self) {
  delete self;
}

#endif  // !defined(QT_NO_GESTURES)
