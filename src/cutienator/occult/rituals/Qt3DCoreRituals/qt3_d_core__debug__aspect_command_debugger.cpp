//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/aspectcommanddebugger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/aspectcommanddebugger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *Qt3DCore::Debug::AspectCommandDebugger::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Debug21AspectCommandDebugger10metaObjectEv(
    const Qt3DCore::Debug::AspectCommandDebugger *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Debug::AspectCommandDebugger::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger11qt_metacastEPKc(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Debug::AspectCommandDebugger::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Debug::AspectCommandDebugger::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Debug::AspectCommandDebugger::tr(s, c, n));
}

//  Qt3DCore::Debug::AspectCommandDebugger::AspectCommandDebugger(QSystemInfo
//      rmationService *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Debug::AspectCommandDebugger *ritual_ZN8Qt3DCore5Debug21AspectCommandDebuggerC1EPNS_25QSystemInformationServiceE(
    Qt3DCore::QSystemInformationService *parent) {
  return new Qt3DCore::Debug::AspectCommandDebugger(parent);
}

//  void Qt3DCore::Debug::AspectCommandDebugger::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10initializeEv(
    Qt3DCore::Debug::AspectCommandDebugger *self) {
  self->initialize();
}

//  void Qt3DCore::Debug::AspectCommandDebugger::asynchronousReplyFinished(As
//      ynchronousCommandReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger25asynchronousReplyFinishedEPNS0_24AsynchronousCommandReplyE(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    Qt3DCore::Debug::AsynchronousCommandReply *reply) {
  self->asynchronousReplyFinished(reply);
}

//  void Qt3DCore::Debug::AspectCommandDebugger::sendReply(QTcpSocket
//      *socket, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger9sendReplyEP10QTcpSocketRK10QByteArray(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    QTcpSocket *socket,
    const QByteArray *data) {
  self->sendReply(socket, *data);
}

//  void Qt3DCore::Debug::AspectCommandDebugger::onCommandReceived(QTcpSocket
//      *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger17onCommandReceivedEP10QTcpSocket(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    QTcpSocket *socket) {
  self->onCommandReceived(socket);
}

//  void Qt3DCore::Debug::AspectCommandDebugger::executeCommand(const QString
//      &command, QTcpSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger14executeCommandERK7QStringP10QTcpSocket(
    Qt3DCore::Debug::AspectCommandDebugger *self,
    const QString *command,
    QTcpSocket *socket) {
  self->executeCommand(*command, socket);
}
