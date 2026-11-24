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

//  QString Qt3DCore::Debug::AsynchronousCommandReply::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Debug::AsynchronousCommandReply::tr(s, c, n));
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
