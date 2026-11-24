//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtHttpServer/qhttpserver.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QHttpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHttpServer10metaObjectEv(
    const QHttpServer *self) {
  return self->metaObject();
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
