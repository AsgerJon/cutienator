//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcstream.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/QLatin1String>
#include <QtGrpc/QGrpcCallOptions>
#include <memory>
#include <QtGrpc/QAbstractGrpcChannel>
#include <QtGrpc/QGrpcServerStream>

//  const QMetaObject *QGrpcServerStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGrpcServerStream10metaObjectEv(
    const QGrpcServerStream *self) {
  return self->metaObject();
}

//  void *QGrpcServerStream::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QGrpcServerStream11qt_metacastEPKc(
    QGrpcServerStream *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcServerStream::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QGrpcServerStream11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcServerStream *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcServerStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGrpcServerStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcServerStream::tr(s, c, n));
}

//  QGrpcServerStream::QGrpcServerStream(QLatin1StringView service,
//      QLatin1StringView method, const QGrpcCallOptions &options,
//      std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)
extern "C" Q_DECL_EXPORT
QGrpcServerStream *ritual_ZN17QGrpcServerStreamC1E13QLatin1StringS0_RK16QGrpcCallOptionsSt8weak_ptrI20QAbstractGrpcChannelENS_18PrivateConstructorE(
    const QLatin1String *service,
    const QLatin1String *method,
    const QGrpcCallOptions *options,
    const std::weak_ptr<QAbstractGrpcChannel> *channel,
    const QGrpcServerStream::PrivateConstructor *a4) {
  return new QGrpcServerStream(*service, *method, *options, *channel, *a4);
}

//  QGrpcServerStream::~QGrpcServerStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcServerStreamD1Ev(QGrpcServerStream *self) {
  delete self;
}

//  void QGrpcServerStream::messageReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcServerStream15messageReceivedEv(
    QGrpcServerStream *self) {
  self->messageReceived();
}

//  bool QGrpcServerStream::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGrpcServerStream5eventEP6QEvent(
    QGrpcServerStream *self,
    QEvent *event) {
  return self->event(event);
}
