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
#include <QtGrpc/QGrpcBidiStream>

//  const QMetaObject *QGrpcBidiStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGrpcBidiStream10metaObjectEv(
    const QGrpcBidiStream *self) {
  return self->metaObject();
}

//  void *QGrpcBidiStream::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGrpcBidiStream11qt_metacastEPKc(
    QGrpcBidiStream *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcBidiStream::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGrpcBidiStream11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcBidiStream *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcBidiStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGrpcBidiStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcBidiStream::tr(s, c, n));
}

//  QGrpcBidiStream::QGrpcBidiStream(QLatin1StringView service,
//      QLatin1StringView method, const QGrpcCallOptions &options,
//      std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)
extern "C" Q_DECL_EXPORT
QGrpcBidiStream *ritual_ZN15QGrpcBidiStreamC1E13QLatin1StringS0_RK16QGrpcCallOptionsSt8weak_ptrI20QAbstractGrpcChannelENS_18PrivateConstructorE(
    const QLatin1String *service,
    const QLatin1String *method,
    const QGrpcCallOptions *options,
    const std::weak_ptr<QAbstractGrpcChannel> *channel,
    const QGrpcBidiStream::PrivateConstructor *a4) {
  return new QGrpcBidiStream(*service, *method, *options, *channel, *a4);
}

//  QGrpcBidiStream::~QGrpcBidiStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStreamD1Ev(QGrpcBidiStream *self) {
  delete self;
}

//  void QGrpcBidiStream::writeMessage(const QProtobufMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStream12writeMessageERK16QProtobufMessage(
    QGrpcBidiStream *self,
    const QProtobufMessage *message) {
  self->writeMessage(*message);
}

//  void QGrpcBidiStream::writesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStream10writesDoneEv(QGrpcBidiStream *self) {
  self->writesDone();
}

//  void QGrpcBidiStream::messageReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStream15messageReceivedEv(QGrpcBidiStream *self) {
  self->messageReceived();
}

//  bool QGrpcBidiStream::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGrpcBidiStream5eventEP6QEvent(
    QGrpcBidiStream *self,
    QEvent *event) {
  return self->event(event);
}
