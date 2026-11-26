//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsessionmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_SESSIONMANAGER)
#include <QtGui/qsessionmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QSessionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSessionManager10metaObjectEv(
    const QSessionManager *self) {
  return self->metaObject();
}

//  void *QSessionManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QSessionManager11qt_metacastEPKc(
    QSessionManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSessionManager::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QSessionManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QSessionManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSessionManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSessionManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSessionManager::tr(s, c, n));
}

//  QSessionManagerPrivate *QSessionManager::d_func()
extern "C" Q_DECL_EXPORT
QSessionManagerPrivate *ritual_ZN15QSessionManager6d_funcEv(
    QSessionManager *self) {
  return self->d_func();
}

//  const QSessionManagerPrivate *QSessionManager::d_func() const
extern "C" Q_DECL_EXPORT
const QSessionManagerPrivate *ritual_ZNK15QSessionManager6d_funcEv(
    const QSessionManager *self) {
  return self->d_func();
}

//  QSessionManager::QSessionManager(QGuiApplication *app, QString &id,
//      QString &key)
extern "C" Q_DECL_EXPORT
QSessionManager *ritual_ZN15QSessionManagerC1EP15QGuiApplicationR7QStringS3_(
    QGuiApplication *app,
    QString *id,
    QString *key) {
  return new QSessionManager(app, *id, *key);
}

//  QSessionManager::~QSessionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManagerD1Ev(QSessionManager *self) {
  delete self;
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

//  void QSessionManager::setRestartCommand(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager17setRestartCommandERK5QListI7QStringE(
    QSessionManager *self,
    const QList<QString> *a0) {
  self->setRestartCommand(*a0);
}

//  QStringList QSessionManager::restartCommand() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSessionManager14restartCommandEv(
    const QSessionManager *self) {
  return new QList<QString>(self->restartCommand());
}

//  void QSessionManager::setDiscardCommand(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager17setDiscardCommandERK5QListI7QStringE(
    QSessionManager *self,
    const QList<QString> *a0) {
  self->setDiscardCommand(*a0);
}

//  QStringList QSessionManager::discardCommand() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QSessionManager14discardCommandEv(
    const QSessionManager *self) {
  return new QList<QString>(self->discardCommand());
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

//  void QSessionManager::setManagerProperty(const QString &name, const
//      QStringList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSessionManager18setManagerPropertyERK7QStringRK5QListIS0_E(
    QSessionManager *self,
    const QString *name,
    const QList<QString> *value) {
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

#endif  // !defined(QT_NO_SESSIONMANAGER)
