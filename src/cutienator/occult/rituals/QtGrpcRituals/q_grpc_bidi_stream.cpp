//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcstream.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGrpcBidiStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGrpcBidiStream10metaObjectEv(
    const QGrpcBidiStream *self) {
  return self->metaObject();
}

//  QString QGrpcBidiStream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGrpcBidiStream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcBidiStream::tr(s, c, n));
}

//  QGrpcBidiStream::~QGrpcBidiStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStreamD1Ev(QGrpcBidiStream *self) {
  delete self;
}

//  void QGrpcBidiStream::writesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGrpcBidiStream10writesDoneEv(QGrpcBidiStream *self) {
  self->writesDone();
}

//  bool QGrpcBidiStream::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGrpcBidiStream5eventEP6QEvent(
    QGrpcBidiStream *self,
    QEvent *event) {
  return self->event(event);
}
