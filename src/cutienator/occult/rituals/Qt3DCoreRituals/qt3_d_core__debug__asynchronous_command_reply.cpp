//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject
//      *Qt3DCore::Debug::AsynchronousCommandReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply10metaObjectEv(
    const Qt3DCore::Debug::AsynchronousCommandReply *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Debug::AsynchronousCommandReply::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply11qt_metacastEPKc(
    Qt3DCore::Debug::AsynchronousCommandReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DCore::Debug::AsynchronousCommandReply::qt_metacall(QMetaObject::C
//      all a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Debug::AsynchronousCommandReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Debug::AsynchronousCommandReply::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Debug::AsynchronousCommandReply::tr(s, c, n));
}

//  Qt3DCore::Debug::AsynchronousCommandReply::AsynchronousCommandReply(const
//      QString &commandName, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Debug::AsynchronousCommandReply *ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReplyC1ERK7QStringP7QObject(
    const QString *commandName,
    QObject *parent) {
  return new Qt3DCore::Debug::AsynchronousCommandReply(*commandName, parent);
}

//  QByteArray Qt3DCore::Debug::AsynchronousCommandReply::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply4dataEv(
    const Qt3DCore::Debug::AsynchronousCommandReply *self) {
  return new QByteArray(self->data());
}

//  QString Qt3DCore::Debug::AsynchronousCommandReply::commandName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply11commandNameEv(
    const Qt3DCore::Debug::AsynchronousCommandReply *self) {
  return new QString(self->commandName());
}

//  bool Qt3DCore::Debug::AsynchronousCommandReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply10isFinishedEv(
    const Qt3DCore::Debug::AsynchronousCommandReply *self) {
  return self->isFinished();
}

//  void Qt3DCore::Debug::AsynchronousCommandReply::setFinished(bool
//      finished)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply11setFinishedEb(
    Qt3DCore::Debug::AsynchronousCommandReply *self,
    bool finished) {
  self->setFinished(finished);
}

//  void Qt3DCore::Debug::AsynchronousCommandReply::setData(const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply7setDataERK10QByteArray(
    Qt3DCore::Debug::AsynchronousCommandReply *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  void Qt3DCore::Debug::AsynchronousCommandReply::finished(AsynchronousComm
//      andReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply8finishedEPS1_(
    Qt3DCore::Debug::AsynchronousCommandReply *self,
    Qt3DCore::Debug::AsynchronousCommandReply *reply) {
  self->finished(reply);
}
