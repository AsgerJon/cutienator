//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtcpsocketwrappertask.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'd_func' gives the private class as
//  QtTaskTree::<Class>Private, as the compiler needs it written.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if QT_CONFIG(network)
#include <QtTaskTree/qtcpsocketwrappertask.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtTaskTree::QTcpSocketWrapper may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtTaskTree_QTcpSocketWrapper : QtTaskTree::QTcpSocketWrapper {
  using QtTaskTree::QTcpSocketWrapper::event;
};

//  A QtTaskTree::QTcpSocketWrapper that Python can take functions over in. Every QtTaskTree::QTcpSocketWrapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QTcpSocketWrapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QTcpSocketWrapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTcpSocketWrapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTcpSocketWrapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTcpSocketWrapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTcpSocketWrapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTcpSocketWrapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtTaskTree_QTcpSocketWrapper : public QtTaskTree::QTcpSocketWrapper {
public:
  using QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper;
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
  //  bool QtTaskTree::QTcpSocketWrapper::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtTaskTree_QTcpSocketWrapperCall0 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QtTaskTree::QTcpSocketWrapper::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtTaskTree_QTcpSocketWrapperCall1 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall1>(taken[1]);
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
      CuteQtTaskTree_QTcpSocketWrapperCall2 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall2>(taken[2]);
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
      CuteQtTaskTree_QTcpSocketWrapperCall3 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall3>(taken[3]);
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
      CuteQtTaskTree_QTcpSocketWrapperCall4 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall4>(taken[4]);
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
      CuteQtTaskTree_QTcpSocketWrapperCall5 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall5>(taken[5]);
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
      CuteQtTaskTree_QTcpSocketWrapperCall6 call = reinterpret_cast<CuteQtTaskTree_QTcpSocketWrapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtTaskTree::QTcpSocketWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtTaskTree17QTcpSocketWrapper10metaObjectEv(
    const QtTaskTree::QTcpSocketWrapper *self) {
  return self->metaObject();
}

//  void *QtTaskTree::QTcpSocketWrapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QtTaskTree17QTcpSocketWrapper11qt_metacastEPKc(
    QtTaskTree::QTcpSocketWrapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QtTaskTree::QTcpSocketWrapper::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtTaskTree17QTcpSocketWrapper2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtTaskTree::QTcpSocketWrapper::tr(s, c, n));
}

//  QTcpSocketWrapperPrivate *QtTaskTree::QTcpSocketWrapper::d_func()
extern "C" Q_DECL_EXPORT
QtTaskTree::QTcpSocketWrapperPrivate *ritual_ZN10QtTaskTree17QTcpSocketWrapper6d_funcEv(
    QtTaskTree::QTcpSocketWrapper *self) {
  return self->d_func();
}

//  const QTcpSocketWrapperPrivate *QtTaskTree::QTcpSocketWrapper::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QtTaskTree::QTcpSocketWrapperPrivate *ritual_ZNK10QtTaskTree17QTcpSocketWrapper6d_funcEv(
    const QtTaskTree::QTcpSocketWrapper *self) {
  return self->d_func();
}

//  QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper()
extern "C" Q_DECL_EXPORT
QtTaskTree::QTcpSocketWrapper *ritual_ZN10QtTaskTree17QTcpSocketWrapperC1Ev() {
  return new CuteQtTaskTree_QTcpSocketWrapper();
}

//  a Python function taken by a CuteQtTaskTree_QTcpSocketWrapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtTaskTree_QTcpSocketWrapper(
    QtTaskTree::QTcpSocketWrapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtTaskTree_QTcpSocketWrapper *>(self)->take(key, call);
}

//  bool QtTaskTree::QTcpSocketWrapper::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QtTaskTree17QTcpSocketWrapper5eventEP6QEvent(
    QtTaskTree::QTcpSocketWrapper *self,
    QEvent *event) {
  return static_cast<OwnQtTaskTree_QTcpSocketWrapper *>(self)->OwnQtTaskTree_QTcpSocketWrapper::event(
      event);
}

#endif  // QT_CONFIG(network)
