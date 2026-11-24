//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlengine.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QQmlEngine *QQmlEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZN17QQmlEnginePrivate6q_funcEv(QQmlEnginePrivate *self) {
  return self->q_func();
}

//  const QQmlEngine *QQmlEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlEngine *ritual_ZNK17QQmlEnginePrivate6q_funcEv(
    const QQmlEnginePrivate *self) {
  return self->q_func();
}

//  QQmlEnginePrivate::~QQmlEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivateD1Ev(QQmlEnginePrivate *self) {
  delete self;
}

//  void QQmlEnginePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate4initEv(QQmlEnginePrivate *self) {
  self->init();
}

//  void QQmlEnginePrivate::referenceScarceResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate24referenceScarceResourcesEv(
    QQmlEnginePrivate *self) {
  self->referenceScarceResources();
}

//  void QQmlEnginePrivate::dereferenceScarceResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate26dereferenceScarceResourcesEv(
    QQmlEnginePrivate *self) {
  self->dereferenceScarceResources();
}

//  QString QQmlEnginePrivate::offlineStorageDatabaseDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlEnginePrivate31offlineStorageDatabaseDirectoryEv(
    const QQmlEnginePrivate *self) {
  return new QString(self->offlineStorageDatabaseDirectory());
}

//  void QQmlEnginePrivate::sendQuit()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate8sendQuitEv(QQmlEnginePrivate *self) {
  self->sendQuit();
}

//  void QQmlEnginePrivate::sendExit(int retCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate8sendExitEi(
    QQmlEnginePrivate *self,
    int retCode) {
  self->sendExit(retCode);
}

//  void QQmlEnginePrivate::warning(const QQmlError &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningERK9QQmlError(
    QQmlEnginePrivate *self,
    const QQmlError *a0) {
  self->warning(*a0);
}

//  void QQmlEnginePrivate::warning(const QList<QQmlError> &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningERK5QListI9QQmlErrorE(
    QQmlEnginePrivate *self,
    const QList<QQmlError> *a0) {
  self->warning(*a0);
}

//  void QQmlEnginePrivate::warning(QQmlEngine *a0, const QQmlError &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningEP10QQmlEngineRK9QQmlError(
    QQmlEngine *a0,
    const QQmlError *a1) {
  QQmlEnginePrivate::warning(a0, *a1);
}

//  void QQmlEnginePrivate::warning(QQmlEngine *a0, const QList<QQmlError>
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningEP10QQmlEngineRK5QListI9QQmlErrorE(
    QQmlEngine *a0,
    const QList<QQmlError> *a1) {
  QQmlEnginePrivate::warning(a0, *a1);
}

//  void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const QQmlError
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningEPS_RK9QQmlError(
    QQmlEnginePrivate *a0,
    const QQmlError *a1) {
  QQmlEnginePrivate::warning(a0, *a1);
}

//  void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const
//      QList<QQmlError> &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate7warningEPS_RK5QListI9QQmlErrorE(
    QQmlEnginePrivate *a0,
    const QList<QQmlError> *a1) {
  QQmlEnginePrivate::warning(a0, *a1);
}

//  QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlEngine *e)
extern "C" Q_DECL_EXPORT
QQmlEnginePrivate *ritual_ZN17QQmlEnginePrivate3getEP10QQmlEngine(
    QQmlEngine *e) {
  return QQmlEnginePrivate::get(e);
}

//  const QQmlEnginePrivate *QQmlEnginePrivate::get(const QQmlEngine *e)
extern "C" Q_DECL_EXPORT
const QQmlEnginePrivate *ritual_ZN17QQmlEnginePrivate3getEPK10QQmlEngine(
    const QQmlEngine *e) {
  return QQmlEnginePrivate::get(e);
}

//  QQmlEngine *QQmlEnginePrivate::get(QQmlEnginePrivate *p)
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZN17QQmlEnginePrivate3getEPS_(QQmlEnginePrivate *p) {
  return QQmlEnginePrivate::get(p);
}

//  QQmlEnginePrivate *QQmlEnginePrivate::get(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QQmlEnginePrivate *ritual_ZN17QQmlEnginePrivate3getEPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QQmlEnginePrivate::get(e);
}

//  QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlContext *c)
extern "C" Q_DECL_EXPORT
QQmlEnginePrivate *ritual_ZN17QQmlEnginePrivate3getEP11QQmlContext(
    QQmlContext *c) {
  return QQmlEnginePrivate::get(c);
}

//  bool QQmlEnginePrivate::designerMode()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlEnginePrivate12designerModeEv() {
  return QQmlEnginePrivate::designerMode();
}

//  void QQmlEnginePrivate::activateDesignerMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate20activateDesignerModeEv() {
  QQmlEnginePrivate::activateDesignerMode();
}

//  QQmlGadgetPtrWrapper *QQmlEnginePrivate::valueTypeInstance(QMetaType
//      type)
extern "C" Q_DECL_EXPORT
QQmlGadgetPtrWrapper *ritual_ZN17QQmlEnginePrivate17valueTypeInstanceE9QMetaType(
    QQmlEnginePrivate *self,
    const QMetaType *type) {
  return self->valueTypeInstance(*type);
}

//  QV4::ExecutableCompilationUnit
//      *QQmlEnginePrivate::compilationUnitFromUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZN17QQmlEnginePrivate22compilationUnitFromUrlERK4QUrl(
    QQmlEnginePrivate *self,
    const QUrl *url) {
  return self->compilationUnitFromUrl(*url);
}

//  void QQmlEnginePrivate::cleanupScarceResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate22cleanupScarceResourcesEv(
    QQmlEnginePrivate *self) {
  self->cleanupScarceResources();
}
