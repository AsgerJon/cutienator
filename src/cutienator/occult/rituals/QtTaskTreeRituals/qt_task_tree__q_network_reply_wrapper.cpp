//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qnetworkreplywrappertask.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if QT_CONFIG(network)
#include <QtTaskTree/qnetworkreplywrappertask.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtTaskTree::QNetworkReplyWrapper may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtTaskTree_QNetworkReplyWrapper : QtTaskTree::QNetworkReplyWrapper {
  using QtTaskTree::QNetworkReplyWrapper::event;
};

//  A QtTaskTree::QNetworkReplyWrapper that Python can take functions over in. Every QtTaskTree::QNetworkReplyWrapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QNetworkReplyWrapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QNetworkReplyWrapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QNetworkReplyWrapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QNetworkReplyWrapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QNetworkReplyWrapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QNetworkReplyWrapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QNetworkReplyWrapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtTaskTree_QNetworkReplyWrapper : public QtTaskTree::QNetworkReplyWrapper {
public:
  using QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper;
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
  //  bool QtTaskTree::QNetworkReplyWrapper::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtTaskTree_QNetworkReplyWrapperCall0 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QtTaskTree::QNetworkReplyWrapper::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtTaskTree_QNetworkReplyWrapperCall1 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall1>(taken[1]);
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
      CuteQtTaskTree_QNetworkReplyWrapperCall2 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall2>(taken[2]);
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
      CuteQtTaskTree_QNetworkReplyWrapperCall3 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall3>(taken[3]);
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
      CuteQtTaskTree_QNetworkReplyWrapperCall4 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall4>(taken[4]);
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
      CuteQtTaskTree_QNetworkReplyWrapperCall5 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall5>(taken[5]);
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
      CuteQtTaskTree_QNetworkReplyWrapperCall6 call = reinterpret_cast<CuteQtTaskTree_QNetworkReplyWrapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtTaskTree::QNetworkReplyWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtTaskTree20QNetworkReplyWrapper10metaObjectEv(
    const QtTaskTree::QNetworkReplyWrapper *self) {
  return self->metaObject();
}

//  QString QtTaskTree::QNetworkReplyWrapper::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtTaskTree20QNetworkReplyWrapper2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtTaskTree::QNetworkReplyWrapper::tr(s, c, n));
}

//  QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper()
extern "C" Q_DECL_EXPORT
QtTaskTree::QNetworkReplyWrapper *ritual_ZN10QtTaskTree20QNetworkReplyWrapperC1Ev() {
  return new CuteQtTaskTree_QNetworkReplyWrapper();
}

//  a Python function taken by a CuteQtTaskTree_QNetworkReplyWrapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtTaskTree_QNetworkReplyWrapper(
    QtTaskTree::QNetworkReplyWrapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtTaskTree_QNetworkReplyWrapper *>(self)->take(key, call);
}

//  bool QtTaskTree::QNetworkReplyWrapper::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QtTaskTree20QNetworkReplyWrapper5eventEP6QEvent(
    QtTaskTree::QNetworkReplyWrapper *self,
    QEvent *event) {
  return static_cast<OwnQtTaskTree_QNetworkReplyWrapper *>(self)->OwnQtTaskTree_QNetworkReplyWrapper::event(
      event);
}

#endif  // QT_CONFIG(network)
