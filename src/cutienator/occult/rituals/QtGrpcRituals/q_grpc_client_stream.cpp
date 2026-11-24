//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcstream.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGrpcClientStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGrpcClientStream10metaObjectEv(
    const QGrpcClientStream *self) {
  return self->metaObject();
}

//  QString QGrpcClientStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGrpcClientStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcClientStream::tr(s, c, n));
}

//  QGrpcClientStream::~QGrpcClientStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcClientStreamD1Ev(QGrpcClientStream *self) {
  delete self;
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
