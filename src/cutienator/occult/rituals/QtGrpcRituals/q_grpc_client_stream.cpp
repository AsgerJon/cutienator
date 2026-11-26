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
#include <QtGrpc/QGrpcClientStream>

//  const QMetaObject *QGrpcClientStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGrpcClientStream10metaObjectEv(
    const QGrpcClientStream *self) {
  return self->metaObject();
}

//  void *QGrpcClientStream::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QGrpcClientStream11qt_metacastEPKc(
    QGrpcClientStream *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcClientStream::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QGrpcClientStream11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcClientStream *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcClientStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGrpcClientStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcClientStream::tr(s, c, n));
}

//  QGrpcClientStream::QGrpcClientStream(QLatin1StringView service,
//      QLatin1StringView method, const QGrpcCallOptions &options,
//      std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)
extern "C" Q_DECL_EXPORT
QGrpcClientStream *ritual_ZN17QGrpcClientStreamC1E13QLatin1StringS0_RK16QGrpcCallOptionsSt8weak_ptrI20QAbstractGrpcChannelENS_18PrivateConstructorE(
    const QLatin1String *service,
    const QLatin1String *method,
    const QGrpcCallOptions *options,
    const std::weak_ptr<QAbstractGrpcChannel> *channel,
    const QGrpcClientStream::PrivateConstructor *a4) {
  return new QGrpcClientStream(*service, *method, *options, *channel, *a4);
}

//  QGrpcClientStream::~QGrpcClientStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcClientStreamD1Ev(QGrpcClientStream *self) {
  delete self;
}

//  void QGrpcClientStream::writeMessage(const QProtobufMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcClientStream12writeMessageERK16QProtobufMessage(
    QGrpcClientStream *self,
    const QProtobufMessage *message) {
  self->writeMessage(*message);
}

//  void QGrpcClientStream::writesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcClientStream10writesDoneEv(QGrpcClientStream *self) {
  self->writesDone();
}

//  bool QGrpcClientStream::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGrpcClientStream5eventEP6QEvent(
    QGrpcClientStream *self,
    QEvent *event) {
  return self->event(event);
}
