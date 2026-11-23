//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiooperation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/QtCore>
#include <QtCore/6.12.0/QtCore/private/qiooperation_p.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIOReadWriteOperationBase that Python can take functions over in. Every QIOReadWriteOperationBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQIOReadWriteOperationBaseCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQIOReadWriteOperationBaseCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQIOReadWriteOperationBaseCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQIOReadWriteOperationBaseCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQIOReadWriteOperationBaseCall4)(const void *, QEvent *, int *);
typedef void (*CuteQIOReadWriteOperationBaseCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQIOReadWriteOperationBaseCall6)(const void *, const QMetaMethod *, int *);
class CuteQIOReadWriteOperationBase : public QIOReadWriteOperationBase {
public:
  using QIOReadWriteOperationBase::QIOReadWriteOperationBase;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall0 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall1 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall2 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall3 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall4 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall5 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQIOReadWriteOperationBaseCall6 call = reinterpret_cast<CuteQIOReadWriteOperationBaseCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  QIOReadWriteOperationBase::~QIOReadWriteOperationBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QIOReadWriteOperationBaseD1Ev(
    QIOReadWriteOperationBase *self) {
  delete self;
}

//  qint64 QIOReadWriteOperationBase::offset() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QIOReadWriteOperationBase6offsetEv(
    const QIOReadWriteOperationBase *self) {
  return self->offset();
}

//  qint64 QIOReadWriteOperationBase::numBytesProcessed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QIOReadWriteOperationBase17numBytesProcessedEv(
    const QIOReadWriteOperationBase *self) {
  return self->numBytesProcessed();
}

//  a Python function taken by a CuteQIOReadWriteOperationBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIOReadWriteOperationBase(
    QIOReadWriteOperationBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIOReadWriteOperationBase *>(self)->take(key, call);
}
