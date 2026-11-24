//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpccallreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpccallreply.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QGrpcCallReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGrpcCallReply10metaObjectEv(
    const QGrpcCallReply *self) {
  return self->metaObject();
}

//  QString QGrpcCallReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGrpcCallReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcCallReply::tr(s, c, n));
}

//  QGrpcCallReply::~QGrpcCallReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGrpcCallReplyD1Ev(QGrpcCallReply *self) {
  delete self;
}

//  bool QGrpcCallReply::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGrpcCallReply5eventEP6QEvent(
    QGrpcCallReply *self,
    QEvent *event) {
  return self->event(event);
}
