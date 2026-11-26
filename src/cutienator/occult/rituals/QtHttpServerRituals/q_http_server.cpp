//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtHttpServer/qhttpserver.h>
#include <QtCore/qstring.h>
#include <QtHttpServer/qhttpserverrequest.h>

//  const QMetaObject *QHttpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHttpServer10metaObjectEv(
    const QHttpServer *self) {
  return self->metaObject();
}

//  void *QHttpServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QHttpServer11qt_metacastEPKc(
    QHttpServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttpServer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QHttpServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttpServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHttpServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHttpServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttpServer::tr(s, c, n));
}

//  QHttpServerPrivate *QHttpServer::d_func()
extern "C" Q_DECL_EXPORT
QHttpServerPrivate *ritual_ZN11QHttpServer6d_funcEv(QHttpServer *self) {
  return self->d_func();
}

//  const QHttpServerPrivate *QHttpServer::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpServerPrivate *ritual_ZNK11QHttpServer6d_funcEv(
    const QHttpServer *self) {
  return self->d_func();
}

//  QHttpServer::QHttpServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QHttpServer *ritual_ZN11QHttpServerC1EP7QObject(QObject *parent) {
  return new QHttpServer(parent);
}

//  QHttpServer::~QHttpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServerD1Ev(QHttpServer *self) {
  delete self;
}

//  QHttpServerRouter *QHttpServer::router()
extern "C" Q_DECL_EXPORT
QHttpServerRouter *ritual_ZN11QHttpServer6routerEv(QHttpServer *self) {
  return self->router();
}

//  const QHttpServerRouter *QHttpServer::router() const
extern "C" Q_DECL_EXPORT
const QHttpServerRouter *ritual_ZNK11QHttpServer6routerEv(
    const QHttpServer *self) {
  return self->router();
}

//  void QHttpServer::clearMissingHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer19clearMissingHandlerEv(QHttpServer *self) {
  self->clearMissingHandler();
}

//  void QHttpServer::setMissingHandlerImpl(const QObject *context,
//      QtPrivate::QSlotObjectBase *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer21setMissingHandlerImplEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QHttpServer *self,
    const QObject *context,
    QtPrivate::QSlotObjectBase *handler) {
  self->setMissingHandlerImpl(context, handler);
}

//  void QHttpServer::addAfterRequestHandlerImpl(const QObject *context,
//      QtPrivate::QSlotObjectBase *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer26addAfterRequestHandlerImplEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QHttpServer *self,
    const QObject *context,
    QtPrivate::QSlotObjectBase *handler) {
  self->addAfterRequestHandlerImpl(context, handler);
}

//  bool QHttpServer::handleRequest(const QHttpServerRequest &request,
//      QHttpServerResponder &responder)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QHttpServer13handleRequestERK18QHttpServerRequestR20QHttpServerResponder(
    QHttpServer *self,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  return self->handleRequest(*request, *responder);
}

//  void QHttpServer::missingHandler(const QHttpServerRequest &request,
//      QHttpServerResponder &responder)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer14missingHandlerERK18QHttpServerRequestR20QHttpServerResponder(
    QHttpServer *self,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  self->missingHandler(*request, *responder);
}

//  void QHttpServer::sendResponse(QHttpServerResponse &&response, const
//      QHttpServerRequest &request, QHttpServerResponder &&responder)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer12sendResponseEO19QHttpServerResponseRK18QHttpServerRequestO20QHttpServerResponder(
    QHttpServer *self,
    QHttpServerResponse *response,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  self->sendResponse(std::move(*response), *request, std::move(*responder));
}

#if QT_CONFIG(future)
//  void QHttpServer::sendResponse(QFuture<QHttpServerResponse> &&response,
//      const QHttpServerRequest &request, QHttpServerResponder &&responder)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHttpServer12sendResponseEO7QFutureI19QHttpServerResponseERK18QHttpServerRequestO20QHttpServerResponder(
    QHttpServer *self,
    QFuture<QHttpServerResponse> *response,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  self->sendResponse(std::move(*response), *request, std::move(*responder));
}
#endif  // QT_CONFIG(future)
