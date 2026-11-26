//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qbarriertask.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtTaskTree::QStartedBarrier may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtTaskTree_QStartedBarrier : QtTaskTree::QStartedBarrier {
  using QtTaskTree::QStartedBarrier::event;
};

//  A QtTaskTree::QStartedBarrier that Python can take functions over in. Every QtTaskTree::QStartedBarrier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QStartedBarrierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QStartedBarrierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QStartedBarrierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QStartedBarrierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QStartedBarrierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QStartedBarrierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QStartedBarrierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtTaskTree_QStartedBarrier : public QtTaskTree::QStartedBarrier {
public:
  using QtTaskTree::QStartedBarrier::QStartedBarrier;
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
  //  bool QtTaskTree::QStartedBarrier::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtTaskTree_QStartedBarrierCall0 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QtTaskTree::QStartedBarrier::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtTaskTree_QStartedBarrierCall1 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall1>(taken[1]);
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
      CuteQtTaskTree_QStartedBarrierCall2 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall2>(taken[2]);
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
      CuteQtTaskTree_QStartedBarrierCall3 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall3>(taken[3]);
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
      CuteQtTaskTree_QStartedBarrierCall4 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall4>(taken[4]);
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
      CuteQtTaskTree_QStartedBarrierCall5 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall5>(taken[5]);
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
      CuteQtTaskTree_QStartedBarrierCall6 call = reinterpret_cast<CuteQtTaskTree_QStartedBarrierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtTaskTree::QStartedBarrier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtTaskTree15QStartedBarrier10metaObjectEv(
    const QtTaskTree::QStartedBarrier *self) {
  return self->metaObject();
}

//  void *QtTaskTree::QStartedBarrier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QtTaskTree15QStartedBarrier11qt_metacastEPKc(
    QtTaskTree::QStartedBarrier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtTaskTree::QStartedBarrier::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QtTaskTree15QStartedBarrier11qt_metacallEN11QMetaObject4CallEiPPv(
    QtTaskTree::QStartedBarrier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtTaskTree::QStartedBarrier::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtTaskTree15QStartedBarrier2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtTaskTree::QStartedBarrier::tr(s, c, n));
}

//  QtTaskTree::QStartedBarrier::QStartedBarrier()
extern "C" Q_DECL_EXPORT
QtTaskTree::QStartedBarrier *ritual_ZN10QtTaskTree15QStartedBarrierC1Ev() {
  return new CuteQtTaskTree_QStartedBarrier();
}

//  QtTaskTree::QStartedBarrier::QStartedBarrier(QObject *parent)
extern "C" Q_DECL_EXPORT
QtTaskTree::QStartedBarrier *ritual_ZN10QtTaskTree15QStartedBarrierC1EP7QObject(
    QObject *parent) {
  return new CuteQtTaskTree_QStartedBarrier(parent);
}

//  QtTaskTree::QStartedBarrier::QStartedBarrier(qsizetype limit, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtTaskTree::QStartedBarrier *ritual_ZN10QtTaskTree15QStartedBarrierC1ExP7QObject(
    qsizetype limit,
    QObject *parent) {
  return new CuteQtTaskTree_QStartedBarrier(limit, parent);
}

//  QtTaskTree::QStartedBarrier::~QStartedBarrier()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree15QStartedBarrierD1Ev(
    QtTaskTree::QStartedBarrier *self) {
  delete self;
}

//  bool QtTaskTree::QStartedBarrier::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QtTaskTree15QStartedBarrier5eventEP6QEvent(
    QtTaskTree::QStartedBarrier *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQtTaskTree_QStartedBarrier, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtTaskTree_QStartedBarrier(
    QtTaskTree::QStartedBarrier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtTaskTree_QStartedBarrier *>(self)->take(key, call);
}

//  bool QtTaskTree::QStartedBarrier::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QtTaskTree15QStartedBarrier5eventEP6QEvent(
    QtTaskTree::QStartedBarrier *self,
    QEvent *event) {
  return static_cast<OwnQtTaskTree_QStartedBarrier *>(self)->OwnQtTaskTree_QStartedBarrier::event(
      event);
}
