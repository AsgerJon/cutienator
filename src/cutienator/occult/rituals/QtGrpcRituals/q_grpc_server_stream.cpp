//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcstream.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGrpcServerStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGrpcServerStream10metaObjectEv(
    const QGrpcServerStream *self) {
  return self->metaObject();
}

//  QString QGrpcServerStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGrpcServerStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcServerStream::tr(s, c, n));
}

//  QGrpcServerStream::~QGrpcServerStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcServerStreamD1Ev(QGrpcServerStream *self) {
  delete self;
}

//  bool QGrpcServerStream::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGrpcServerStream5eventEP6QEvent(
    QGrpcServerStream *self,
    QEvent *event) {
  return self->event(event);
}
