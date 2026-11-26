//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpccallreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpccallreply.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtGrpc/qgrpccalloptions.h>
#include <QtCore/QLatin1String>
#include <QtGrpc/QGrpcCallOptions>
#include <memory>
#include <QtGrpc/QAbstractGrpcChannel>
#include <QtGrpc/QGrpcCallReply>

//  const QMetaObject *QGrpcCallReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGrpcCallReply10metaObjectEv(
    const QGrpcCallReply *self) {
  return self->metaObject();
}

//  void *QGrpcCallReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QGrpcCallReply11qt_metacastEPKc(
    QGrpcCallReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGrpcCallReply::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QGrpcCallReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QGrpcCallReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGrpcCallReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGrpcCallReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGrpcCallReply::tr(s, c, n));
}

//  QGrpcCallReply::QGrpcCallReply(QLatin1StringView service,
//      QLatin1StringView method, const QGrpcCallOptions &options,
//      std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)
extern "C" Q_DECL_EXPORT
QGrpcCallReply *ritual_ZN14QGrpcCallReplyC1E13QLatin1StringS0_RK16QGrpcCallOptionsSt8weak_ptrI20QAbstractGrpcChannelENS_18PrivateConstructorE(
    const QLatin1String *service,
    const QLatin1String *method,
    const QGrpcCallOptions *options,
    const std::weak_ptr<QAbstractGrpcChannel> *channel,
    const QGrpcCallReply::PrivateConstructor *a4) {
  return new QGrpcCallReply(*service, *method, *options, *channel, *a4);
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
