//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qrangemodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRangeModelDetails::AutoConnectContext that Python can take functions over in. Every QRangeModelDetails::AutoConnectContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRangeModelDetails_AutoConnectContextCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRangeModelDetails_AutoConnectContextCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRangeModelDetails_AutoConnectContextCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRangeModelDetails_AutoConnectContextCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRangeModelDetails_AutoConnectContextCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRangeModelDetails_AutoConnectContextCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRangeModelDetails_AutoConnectContextCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRangeModelDetails_AutoConnectContext : public QRangeModelDetails::AutoConnectContext {
public:
  using QRangeModelDetails::AutoConnectContext::AutoConnectContext;
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
      CuteQRangeModelDetails_AutoConnectContextCall0 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall0>(taken[0]);
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
      CuteQRangeModelDetails_AutoConnectContextCall1 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall1>(taken[1]);
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
      CuteQRangeModelDetails_AutoConnectContextCall2 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall2>(taken[2]);
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
      CuteQRangeModelDetails_AutoConnectContextCall3 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall3>(taken[3]);
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
      CuteQRangeModelDetails_AutoConnectContextCall4 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall4>(taken[4]);
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
      CuteQRangeModelDetails_AutoConnectContextCall5 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall5>(taken[5]);
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
      CuteQRangeModelDetails_AutoConnectContextCall6 call = reinterpret_cast<CuteQRangeModelDetails_AutoConnectContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRangeModelDetails::AutoConnectContext::AutoConnectContext(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QRangeModelDetails::AutoConnectContext *ritual_ZN18QRangeModelDetails18AutoConnectContextC1EP7QObject(
    QObject *parent) {
  return new CuteQRangeModelDetails_AutoConnectContext(parent);
}

//  QRangeModelDetails::AutoConnectContext::~AutoConnectContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRangeModelDetails18AutoConnectContextD1Ev(
    QRangeModelDetails::AutoConnectContext *self) {
  delete self;
}

//  a Python function taken by a CuteQRangeModelDetails_AutoConnectContext,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRangeModelDetails_AutoConnectContext(
    QRangeModelDetails::AutoConnectContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRangeModelDetails_AutoConnectContext *>(self)->take(key, call);
}

#endif  // !defined(Q_QDOC)
