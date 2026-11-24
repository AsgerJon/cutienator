//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiooperation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiooperation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIOOperation that Python can take functions over in. Every QIOOperation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIOOperationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIOOperationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOOperationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOOperationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOOperationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOOperationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOOperationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQIOOperation : public QIOOperation {
public:
  using QIOOperation::QIOOperation;
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
      CuteQIOOperationCall0 call = reinterpret_cast<CuteQIOOperationCall0>(taken[0]);
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
      CuteQIOOperationCall1 call = reinterpret_cast<CuteQIOOperationCall1>(taken[1]);
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
      CuteQIOOperationCall2 call = reinterpret_cast<CuteQIOOperationCall2>(taken[2]);
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
      CuteQIOOperationCall3 call = reinterpret_cast<CuteQIOOperationCall3>(taken[3]);
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
      CuteQIOOperationCall4 call = reinterpret_cast<CuteQIOOperationCall4>(taken[4]);
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
      CuteQIOOperationCall5 call = reinterpret_cast<CuteQIOOperationCall5>(taken[5]);
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
      CuteQIOOperationCall6 call = reinterpret_cast<CuteQIOOperationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QIOOperation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QIOOperation10metaObjectEv(
    const QIOOperation *self) {
  return self->metaObject();
}

//  QString QIOOperation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QIOOperation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIOOperation::tr(s, c, n));
}

//  QIOOperation::~QIOOperation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOOperationD1Ev(QIOOperation *self) {
  delete self;
}

//  Type QIOOperation::type() const
extern "C" Q_DECL_EXPORT
QIOOperation::Type ritual_ZNK12QIOOperation4typeEv(
    const QIOOperation *self) {
  return self->type();
}

//  Error QIOOperation::error() const
extern "C" Q_DECL_EXPORT
QIOOperation::Error ritual_ZNK12QIOOperation5errorEv(
    const QIOOperation *self) {
  return self->error();
}

//  bool QIOOperation::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QIOOperation10isFinishedEv(const QIOOperation *self) {
  return self->isFinished();
}

//  void QIOOperation::ensureCompleteOrCanceled()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOOperation24ensureCompleteOrCanceledEv(
    QIOOperation *self) {
  self->ensureCompleteOrCanceled();
}

//  QIOOperationPrivate *QIOOperation::d_func()
extern "C" Q_DECL_EXPORT
QIOOperationPrivate *ritual_ZN12QIOOperation6d_funcEv(QIOOperation *self) {
  return self->d_func();
}

//  const QIOOperationPrivate *QIOOperation::d_func() const
extern "C" Q_DECL_EXPORT
const QIOOperationPrivate *ritual_ZNK12QIOOperation6d_funcEv(
    const QIOOperation *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQIOOperation, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIOOperation(
    QIOOperation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIOOperation *>(self)->take(key, call);
}
