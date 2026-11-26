//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuahistoryreadresponse.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuahistoryreadresponse.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuahistorydata.h>
#include <QtOpcUa/qopcuahistoryevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaHistoryReadResponse that Python can take functions over in. Every QOpcUaHistoryReadResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaHistoryReadResponseCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaHistoryReadResponseCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaHistoryReadResponse : public QOpcUaHistoryReadResponse {
public:
  using QOpcUaHistoryReadResponse::QOpcUaHistoryReadResponse;
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
      CuteQOpcUaHistoryReadResponseCall0 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall0>(taken[0]);
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
      CuteQOpcUaHistoryReadResponseCall1 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall1>(taken[1]);
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
      CuteQOpcUaHistoryReadResponseCall2 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall2>(taken[2]);
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
      CuteQOpcUaHistoryReadResponseCall3 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall3>(taken[3]);
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
      CuteQOpcUaHistoryReadResponseCall4 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall4>(taken[4]);
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
      CuteQOpcUaHistoryReadResponseCall5 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall5>(taken[5]);
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
      CuteQOpcUaHistoryReadResponseCall6 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaHistoryReadResponse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QOpcUaHistoryReadResponse10metaObjectEv(
    const QOpcUaHistoryReadResponse *self) {
  return self->metaObject();
}

//  void *QOpcUaHistoryReadResponse::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QOpcUaHistoryReadResponse11qt_metacastEPKc(
    QOpcUaHistoryReadResponse *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpcUaHistoryReadResponse::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QOpcUaHistoryReadResponse11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpcUaHistoryReadResponse *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpcUaHistoryReadResponse::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QOpcUaHistoryReadResponse2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaHistoryReadResponse::tr(s, c, n));
}

//  QOpcUaHistoryReadResponsePrivate *QOpcUaHistoryReadResponse::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponsePrivate *ritual_ZN25QOpcUaHistoryReadResponse6d_funcEv(
    QOpcUaHistoryReadResponse *self) {
  return self->d_func();
}

//  const QOpcUaHistoryReadResponsePrivate
//      *QOpcUaHistoryReadResponse::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaHistoryReadResponsePrivate *ritual_ZNK25QOpcUaHistoryReadResponse6d_funcEv(
    const QOpcUaHistoryReadResponse *self) {
  return self->d_func();
}

//  QOpcUaHistoryReadResponse::QOpcUaHistoryReadResponse(QOpcUaHistoryReadRes
//      ponseImpl *impl)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN25QOpcUaHistoryReadResponseC1EP29QOpcUaHistoryReadResponseImpl(
    QOpcUaHistoryReadResponseImpl *impl) {
  return new CuteQOpcUaHistoryReadResponse(impl);
}

//  QOpcUaHistoryReadResponse::~QOpcUaHistoryReadResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaHistoryReadResponseD1Ev(
    QOpcUaHistoryReadResponse *self) {
  delete self;
}

//  bool QOpcUaHistoryReadResponse::hasMoreData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaHistoryReadResponse11hasMoreDataEv(
    const QOpcUaHistoryReadResponse *self) {
  return self->hasMoreData();
}

//  bool QOpcUaHistoryReadResponse::readMoreData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpcUaHistoryReadResponse12readMoreDataEv(
    QOpcUaHistoryReadResponse *self) {
  return self->readMoreData();
}

//  State QOpcUaHistoryReadResponse::state() const
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse::State ritual_ZNK25QOpcUaHistoryReadResponse5stateEv(
    const QOpcUaHistoryReadResponse *self) {
  return self->state();
}

//  bool QOpcUaHistoryReadResponse::releaseContinuationPoints()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpcUaHistoryReadResponse25releaseContinuationPointsEv(
    QOpcUaHistoryReadResponse *self) {
  return self->releaseContinuationPoints();
}

//  QList<QOpcUaHistoryData> QOpcUaHistoryReadResponse::data() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryData> *ritual_ZNK25QOpcUaHistoryReadResponse4dataEv(
    const QOpcUaHistoryReadResponse *self) {
  return new QList<QOpcUaHistoryData>(self->data());
}

//  QList<QOpcUaHistoryEvent> QOpcUaHistoryReadResponse::events() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryEvent> *ritual_ZNK25QOpcUaHistoryReadResponse6eventsEv(
    const QOpcUaHistoryReadResponse *self) {
  return new QList<QOpcUaHistoryEvent>(self->events());
}

//  QOpcUa::UaStatusCode QOpcUaHistoryReadResponse::serviceResult() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK25QOpcUaHistoryReadResponse13serviceResultEv(
    const QOpcUaHistoryReadResponse *self) {
  return self->serviceResult();
}

//  void QOpcUaHistoryReadResponse::readHistoryDataFinished(const
//      QList<QOpcUaHistoryData> &results, QOpcUa::UaStatusCode
//      serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaHistoryReadResponse23readHistoryDataFinishedERK5QListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE(
    QOpcUaHistoryReadResponse *self,
    const QList<QOpcUaHistoryData> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readHistoryDataFinished(*results, serviceResult);
}

//  void QOpcUaHistoryReadResponse::readHistoryEventsFinished(const
//      QList<QOpcUaHistoryEvent> &results, QOpcUa::UaStatusCode
//      serviceResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaHistoryReadResponse25readHistoryEventsFinishedERK5QListI18QOpcUaHistoryEventEN6QOpcUa12UaStatusCodeE(
    QOpcUaHistoryReadResponse *self,
    const QList<QOpcUaHistoryEvent> *results,
    QOpcUa::UaStatusCode serviceResult) {
  self->readHistoryEventsFinished(*results, serviceResult);
}

//  void QOpcUaHistoryReadResponse::stateChanged(State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaHistoryReadResponse12stateChangedENS_5StateE(
    QOpcUaHistoryReadResponse *self,
    QOpcUaHistoryReadResponse::State state) {
  self->stateChanged(state);
}

//  a Python function taken by a CuteQOpcUaHistoryReadResponse, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaHistoryReadResponse(
    QOpcUaHistoryReadResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaHistoryReadResponse *>(self)->take(key, call);
}
