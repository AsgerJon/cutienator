//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponseimpl_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponseimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuahistoryreadrawrequest.h>
#include <QtOpcUa/qopcuahistoryreadeventrequest.h>
#include <QtOpcUa/qopcuahistorydata.h>
#include <QtOpcUa/qopcuahistoryevent.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpcUaHistoryReadResponseImpl that Python can take functions over in. Every QOpcUaHistoryReadResponseImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaHistoryReadResponseImplCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaHistoryReadResponseImplCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseImplCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseImplCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseImplCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseImplCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaHistoryReadResponseImplCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaHistoryReadResponseImpl : public QOpcUaHistoryReadResponseImpl {
public:
  using QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl;
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
      CuteQOpcUaHistoryReadResponseImplCall0 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall0>(taken[0]);
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
      CuteQOpcUaHistoryReadResponseImplCall1 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall1>(taken[1]);
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
      CuteQOpcUaHistoryReadResponseImplCall2 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall2>(taken[2]);
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
      CuteQOpcUaHistoryReadResponseImplCall3 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall3>(taken[3]);
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
      CuteQOpcUaHistoryReadResponseImplCall4 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall4>(taken[4]);
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
      CuteQOpcUaHistoryReadResponseImplCall5 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall5>(taken[5]);
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
      CuteQOpcUaHistoryReadResponseImplCall6 call = reinterpret_cast<CuteQOpcUaHistoryReadResponseImplCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaHistoryReadResponseImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QOpcUaHistoryReadResponseImpl10metaObjectEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return self->metaObject();
}

//  QString QOpcUaHistoryReadResponseImpl::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QOpcUaHistoryReadResponseImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaHistoryReadResponseImpl::tr(s, c, n));
}

//  QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
//      QOpcUaHistoryReadRawRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponseImpl *ritual_ZN29QOpcUaHistoryReadResponseImplC1ERK27QOpcUaHistoryReadRawRequest(
    const QOpcUaHistoryReadRawRequest *request) {
  return new CuteQOpcUaHistoryReadResponseImpl(*request);
}

//  QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
//      QOpcUaHistoryReadEventRequest &request)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponseImpl *ritual_ZN29QOpcUaHistoryReadResponseImplC1ERK29QOpcUaHistoryReadEventRequest(
    const QOpcUaHistoryReadEventRequest *request) {
  return new CuteQOpcUaHistoryReadResponseImpl(*request);
}

//  QOpcUaHistoryReadResponseImpl::~QOpcUaHistoryReadResponseImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadResponseImplD1Ev(
    QOpcUaHistoryReadResponseImpl *self) {
  delete self;
}

//  bool QOpcUaHistoryReadResponseImpl::hasMoreData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QOpcUaHistoryReadResponseImpl11hasMoreDataEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return self->hasMoreData();
}

//  bool QOpcUaHistoryReadResponseImpl::readMoreData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QOpcUaHistoryReadResponseImpl12readMoreDataEv(
    QOpcUaHistoryReadResponseImpl *self) {
  return self->readMoreData();
}

//  QOpcUaHistoryReadResponse::State QOpcUaHistoryReadResponseImpl::state()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse::State ritual_ZNK29QOpcUaHistoryReadResponseImpl5stateEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return self->state();
}

//  bool QOpcUaHistoryReadResponseImpl::releaseContinuationPoints()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QOpcUaHistoryReadResponseImpl25releaseContinuationPointsEv(
    QOpcUaHistoryReadResponseImpl *self) {
  return self->releaseContinuationPoints();
}

//  QList<QOpcUaHistoryData> QOpcUaHistoryReadResponseImpl::data() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryData> *ritual_ZNK29QOpcUaHistoryReadResponseImpl4dataEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return new QList<QOpcUaHistoryData>(self->data());
}

//  QList<QOpcUaHistoryEvent> QOpcUaHistoryReadResponseImpl::events() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryEvent> *ritual_ZNK29QOpcUaHistoryReadResponseImpl6eventsEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return new QList<QOpcUaHistoryEvent>(self->events());
}

//  QOpcUa::UaStatusCode QOpcUaHistoryReadResponseImpl::serviceResult() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK29QOpcUaHistoryReadResponseImpl13serviceResultEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return self->serviceResult();
}

//  void QOpcUaHistoryReadResponseImpl::handleDataAvailable(const
//      QList<QOpcUaHistoryData> &data, const QList<QByteArray>
//      &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
//      responseHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadResponseImpl19handleDataAvailableERK5QListI17QOpcUaHistoryDataERKS0_I10QByteArrayEN6QOpcUa12UaStatusCodeEy(
    QOpcUaHistoryReadResponseImpl *self,
    const QList<QOpcUaHistoryData> *data,
    const QList<QByteArray> *continuationPoints,
    QOpcUa::UaStatusCode serviceResult,
    quint64 responseHandle) {
  self->handleDataAvailable(
      *data,
      *continuationPoints,
      serviceResult,
      responseHandle);
}

//  void QOpcUaHistoryReadResponseImpl::handleEventsAvailable(const
//      QList<QOpcUaHistoryEvent> &data, const QList<QByteArray>
//      &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
//      responseHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadResponseImpl21handleEventsAvailableERK5QListI18QOpcUaHistoryEventERKS0_I10QByteArrayEN6QOpcUa12UaStatusCodeEy(
    QOpcUaHistoryReadResponseImpl *self,
    const QList<QOpcUaHistoryEvent> *data,
    const QList<QByteArray> *continuationPoints,
    QOpcUa::UaStatusCode serviceResult,
    quint64 responseHandle) {
  self->handleEventsAvailable(
      *data,
      *continuationPoints,
      serviceResult,
      responseHandle);
}

//  void QOpcUaHistoryReadResponseImpl::handleRequestError(quint64
//      requestHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadResponseImpl18handleRequestErrorEy(
    QOpcUaHistoryReadResponseImpl *self,
    quint64 requestHandle) {
  self->handleRequestError(requestHandle);
}

//  quint64 QOpcUaHistoryReadResponseImpl::handle() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK29QOpcUaHistoryReadResponseImpl6handleEv(
    const QOpcUaHistoryReadResponseImpl *self) {
  return self->handle();
}

//  void
//      QOpcUaHistoryReadResponseImpl::setState(QOpcUaHistoryReadResponse::St
//      ate state)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadResponseImpl8setStateEN25QOpcUaHistoryReadResponse5StateE(
    QOpcUaHistoryReadResponseImpl *self,
    QOpcUaHistoryReadResponse::State state) {
  self->setState(state);
}

//  QOpcUaHistoryReadRawRequest QOpcUaHistoryReadResponseImpl::createReadRawR
//      equestWithContinuationPoints()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadRawRequest *ritual_ZN29QOpcUaHistoryReadResponseImpl42createReadRawRequestWithContinuationPointsEv(
    QOpcUaHistoryReadResponseImpl *self) {
  return new QOpcUaHistoryReadRawRequest(
      self->createReadRawRequestWithContinuationPoints());
}

//  QOpcUaHistoryReadEventRequest
//      QOpcUaHistoryReadResponseImpl::createEventRequestWithContinuationPoin
//      ts()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadEventRequest *ritual_ZN29QOpcUaHistoryReadResponseImpl40createEventRequestWithContinuationPointsEv(
    QOpcUaHistoryReadResponseImpl *self) {
  return new QOpcUaHistoryReadEventRequest(
      self->createEventRequestWithContinuationPoints());
}

//  a Python function taken by a CuteQOpcUaHistoryReadResponseImpl, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaHistoryReadResponseImpl(
    QOpcUaHistoryReadResponseImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaHistoryReadResponseImpl *>(self)->take(key, call);
}
