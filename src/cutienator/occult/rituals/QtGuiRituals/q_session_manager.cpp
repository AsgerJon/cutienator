//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsessionmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsessionmanager.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSessionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSessionManager10metaObjectEv(
    const QSessionManager *self) {
  return self->metaObject();
}

//  QString QSessionManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSessionManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSessionManager::tr(s, c, n));
}

//  QString QSessionManager::sessionId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSessionManager9sessionIdEv(
    const QSessionManager *self) {
  return new QString(self->sessionId());
}

//  QString QSessionManager::sessionKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSessionManager10sessionKeyEv(
    const QSessionManager *self) {
  return new QString(self->sessionKey());
}

//  bool QSessionManager::allowsInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSessionManager17allowsInteractionEv(QSessionManager *self) {
  return self->allowsInteraction();
}

//  bool QSessionManager::allowsErrorInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSessionManager22allowsErrorInteractionEv(
    QSessionManager *self) {
  return self->allowsErrorInteraction();
}

//  void QSessionManager::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager7releaseEv(QSessionManager *self) {
  self->release();
}

//  void QSessionManager::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager6cancelEv(QSessionManager *self) {
  self->cancel();
}

//  void QSessionManager::setRestartHint(RestartHint a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager14setRestartHintENS_11RestartHintE(
    QSessionManager *self,
    QSessionManager::RestartHint a0) {
  self->setRestartHint(a0);
}

//  RestartHint QSessionManager::restartHint() const
extern "C" Q_DECL_EXPORT
QSessionManager::RestartHint ritual_ZNK15QSessionManager11restartHintEv(
    const QSessionManager *self) {
  return self->restartHint();
}

//  void QSessionManager::setManagerProperty(const QString &name, const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager18setManagerPropertyERK7QStringS2_(
    QSessionManager *self,
    const QString *name,
    const QString *value) {
  self->setManagerProperty(*name, *value);
}

//  bool QSessionManager::isPhase2() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSessionManager8isPhase2Ev(const QSessionManager *self) {
  return self->isPhase2();
}

//  void QSessionManager::requestPhase2()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager13requestPhase2Ev(QSessionManager *self) {
  self->requestPhase2();
}
