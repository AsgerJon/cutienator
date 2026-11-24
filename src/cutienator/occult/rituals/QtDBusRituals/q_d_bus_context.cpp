//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbuscontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbuscontext.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qstring.h>

//  QDBusContext::QDBusContext()
extern "C" Q_DECL_EXPORT
QDBusContext *ritual_ZN12QDBusContextC1Ev() {
  return new QDBusContext();
}

//  QDBusContext::~QDBusContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusContextD1Ev(QDBusContext *self) {
  delete self;
}

//  bool QDBusContext::calledFromDBus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusContext14calledFromDBusEv(const QDBusContext *self) {
  return self->calledFromDBus();
}

//  QDBusConnection QDBusContext::connection() const
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZNK12QDBusContext10connectionEv(
    const QDBusContext *self) {
  return new QDBusConnection(self->connection());
}

//  const QDBusMessage &QDBusContext::message() const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusContext7messageEv(const QDBusContext *self) {
  return new QDBusMessage(self->message());
}

//  bool QDBusContext::isDelayedReply() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusContext14isDelayedReplyEv(const QDBusContext *self) {
  return self->isDelayedReply();
}

//  void QDBusContext::setDelayedReply(bool enable) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QDBusContext15setDelayedReplyEb(
    const QDBusContext *self,
    bool enable) {
  self->setDelayedReply(enable);
}

//  void QDBusContext::sendErrorReply(const QString &name, const QString
//      &msg) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QDBusContext14sendErrorReplyERK7QStringS2_(
    const QDBusContext *self,
    const QString *name,
    const QString *msg) {
  self->sendErrorReply(*name, *msg);
}

//  void QDBusContext::sendErrorReply(QDBusError::ErrorType type, const
//      QString &msg) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QDBusContext14sendErrorReplyEN10QDBusError9ErrorTypeERK7QString(
    const QDBusContext *self,
    QDBusError::ErrorType type,
    const QString *msg) {
  self->sendErrorReply(type, *msg);
}

#endif  // !defined(QT_NO_DBUS)
