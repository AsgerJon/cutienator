//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 2. Kept
//  as it is when the generator runs again.
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
#include <QtCore/QSharedPointer>
#include <QtQml/QQmlImageProviderBase>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#include <QtQml/qjsvalue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}
//  -----------------------------------------------------------------------

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

//  size_t QQmlEnginePrivate::_qt_property_translationLanguage_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN17QQmlEnginePrivate39_qt_property_translationLanguage_offsetEv() {
  return QQmlEnginePrivate::_qt_property_translationLanguage_offset();
}

//  QSharedPointer<QQmlImageProviderBase>
//      QQmlEnginePrivate::imageProvider(const QString &providerId) const
extern "C" Q_DECL_EXPORT
QSharedPointer<QQmlImageProviderBase> *ritual_ZNK17QQmlEnginePrivate13imageProviderERK7QString(
    const QQmlEnginePrivate *self,
    const QString *providerId) {
  return new QSharedPointer<QQmlImageProviderBase>(
      self->imageProvider(
          *providerId));
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

//  void QQmlEnginePrivate::incubate(QQmlIncubator &a0, const
//      QQmlRefPointer<QQmlContextData> &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate8incubateER13QQmlIncubatorRK14QQmlRefPointerI15QQmlContextDataE(
    QQmlEnginePrivate *self,
    QQmlIncubator *a0,
    const QQmlRefPointer<QQmlContextData> *a1) {
  self->incubate(*a0, *a1);
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

//  QQmlEnginePrivate *QQmlEnginePrivate::get(const
//      QQmlRefPointer<QQmlContextData> &c)
extern "C" Q_DECL_EXPORT
QQmlEnginePrivate *ritual_ZN17QQmlEnginePrivate3getERK14QQmlRefPointerI15QQmlContextDataE(
    const QQmlRefPointer<QQmlContextData> *c) {
  return QQmlEnginePrivate::get(*c);
}

//  QList<QQmlError> QQmlEnginePrivate::qmlErrorFromDiagnostics(const QString
//      &fileName, const QList<QQmlJS::DiagnosticMessage>
//      &diagnosticMessages)
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZN17QQmlEnginePrivate23qmlErrorFromDiagnosticsERK7QStringRK5QListIN6QQmlJS17DiagnosticMessageEE(
    const QString *fileName,
    const QList<QQmlJS::DiagnosticMessage> *diagnosticMessages) {
  return new QList<QQmlError>(
      QQmlEnginePrivate::qmlErrorFromDiagnostics(
          *fileName,
          *diagnosticMessages));
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

//  void QQmlEnginePrivate::executeRuntimeFunction(const QUrl &url, qsizetype
//      functionIndex, QObject *thisObject, int argc, void **args, QMetaType
//      *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate22executeRuntimeFunctionERK4QUrlxP7QObjectiPPvP9QMetaType(
    QQmlEnginePrivate *self,
    const QUrl *url,
    qsizetype functionIndex,
    QObject *thisObject,
    int argc,
    void **args,
    QMetaType *types) {
  self->executeRuntimeFunction(
      *url,
      functionIndex,
      thisObject,
      argc,
      args,
      types);
}

//  void QQmlEnginePrivate::executeRuntimeFunction(const
//      QV4::ExecutableCompilationUnit *unit, qsizetype functionIndex,
//      QObject *thisObject, int argc, void **args, QMetaType *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate22executeRuntimeFunctionEPKN3QV425ExecutableCompilationUnitExP7QObjectiPPvP9QMetaType(
    QQmlEnginePrivate *self,
    const QV4::ExecutableCompilationUnit *unit,
    qsizetype functionIndex,
    QObject *thisObject,
    int argc,
    void **args,
    QMetaType *types) {
  self->executeRuntimeFunction(
      unit,
      functionIndex,
      thisObject,
      argc,
      args,
      types);
}

//  QV4::ExecutableCompilationUnit
//      *QQmlEnginePrivate::compilationUnitFromUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZN17QQmlEnginePrivate22compilationUnitFromUrlERK4QUrl(
    QQmlEnginePrivate *self,
    const QUrl *url) {
  return self->compilationUnitFromUrl(*url);
}

//  QQmlRefPointer<QQmlContextData>
//      QQmlEnginePrivate::createBareContext(const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
//      QQmlRefPointer<QQmlContextData> &parentContext, int
//      subComponentIndex)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZN17QQmlEnginePrivate17createBareContextERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERKS0_I15QQmlContextDataEi(
    QQmlEnginePrivate *self,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *unit,
    const QQmlRefPointer<QQmlContextData> *parentContext,
    int subComponentIndex) {
  return new QQmlRefPointer<QQmlContextData>(
      self->createBareContext(
          *unit,
          *parentContext,
          subComponentIndex));
}

//  QQmlRefPointer<QQmlContextData>
//      QQmlEnginePrivate::createComponentRootContext(const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
//      QQmlRefPointer<QQmlContextData> &parentContex, int subComponentIndex)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZN17QQmlEnginePrivate26createComponentRootContextERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERKS0_I15QQmlContextDataEi(
    QQmlEnginePrivate *self,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *unit,
    const QQmlRefPointer<QQmlContextData> *parentContex,
    int subComponentIndex) {
  return new QQmlRefPointer<QQmlContextData>(
      self->createComponentRootContext(
          *unit,
          *parentContex,
          subComponentIndex));
}

//  void QQmlEnginePrivate::setInternalContext(QObject *This, const
//      QQmlRefPointer<QQmlContextData> &context,
//      QQmlContextData::QmlObjectKind kind)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate18setInternalContextEP7QObjectRK14QQmlRefPointerI15QQmlContextDataENS3_13QmlObjectKindE(
    QObject *This,
    const QQmlRefPointer<QQmlContextData> *context,
    QQmlContextData::QmlObjectKind kind) {
  QQmlEnginePrivate::setInternalContext(This, *context, kind);
}

//  void QQmlEnginePrivate::cleanupScarceResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlEnginePrivate22cleanupScarceResourcesEv(
    QQmlEnginePrivate *self) {
  self->cleanupScarceResources();
}

//  a QSharedPointer<QQmlImageProviderBase> a ritual of QQmlEnginePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlEnginePrivate__QSharedPointer_QQmlImageProviderBase(
    QSharedPointer<QQmlImageProviderBase> *self) {
  delete self;
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QQmlEnginePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlEnginePrivate__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}

//  QJSValue QQmlEnginePrivate::singletonInstance<QJSValue>(const QQmlType
//      &type)
extern "C" Q_DECL_EXPORT
QJSValue * ritual_ZN17QQmlEnginePrivate17singletonInstanceI8QJSValueEET_RK8QQmlType(
    QQmlEnginePrivate *self,
    const QQmlType *type) {
  return new QJSValue(self->singletonInstance<QJSValue>(*type));
}

//  QObject *QQmlEnginePrivate::singletonInstance<QObject *>(const QQmlType
//      &type)
extern "C" Q_DECL_EXPORT
QObject * ritual_ZN17QQmlEnginePrivate17singletonInstanceIP7QObjectEET_RK8QQmlType(
    QQmlEnginePrivate *self,
    const QQmlType *type) {
  return self->singletonInstance<QObject *>(*type);
}
