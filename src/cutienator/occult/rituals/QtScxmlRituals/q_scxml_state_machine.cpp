//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlstatemachine.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlstatemachine.h>
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qobjectdefs.h>
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QScxmlStateMachinePrivate *QScxmlStateMachine::d_func()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate *ritual_ZN18QScxmlStateMachine6d_funcEv(
    QScxmlStateMachine *self) {
  return self->d_func();
}

//  const QScxmlStateMachinePrivate *QScxmlStateMachine::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlStateMachinePrivate *ritual_ZNK18QScxmlStateMachine6d_funcEv(
    const QScxmlStateMachine *self) {
  return self->d_func();
}

//  const QMetaObject *QScxmlStateMachine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QScxmlStateMachine10metaObjectEv(
    const QScxmlStateMachine *self) {
  return self->metaObject();
}

//  QString QScxmlStateMachine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QScxmlStateMachine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStateMachine::tr(s, c, n));
}

//  QScxmlStateMachine::QScxmlStateMachine(const QMetaObject *metaObject,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN18QScxmlStateMachineC1EPK11QMetaObjectP7QObject(
    const QMetaObject *metaObject,
    QObject *parent) {
  return new QScxmlStateMachine(metaObject, parent);
}

//  QScxmlStateMachine *QScxmlStateMachine::fromFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN18QScxmlStateMachine8fromFileERK7QString(
    const QString *fileName) {
  return QScxmlStateMachine::fromFile(*fileName);
}

//  QScxmlStateMachine *QScxmlStateMachine::fromData(QIODevice *data, const
//      QString &fileName)
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN18QScxmlStateMachine8fromDataEP9QIODeviceRK7QString(
    QIODevice *data,
    const QString *fileName) {
  return QScxmlStateMachine::fromData(data, *fileName);
}

//  QList<QScxmlError> QScxmlStateMachine::parseErrors() const
extern "C" Q_DECL_EXPORT
QList<QScxmlError> *ritual_ZNK18QScxmlStateMachine11parseErrorsEv(
    const QScxmlStateMachine *self) {
  return new QList<QScxmlError>(self->parseErrors());
}

//  QString QScxmlStateMachine::sessionId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QScxmlStateMachine9sessionIdEv(
    const QScxmlStateMachine *self) {
  return new QString(self->sessionId());
}

//  bool QScxmlStateMachine::isInvoked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine9isInvokedEv(
    const QScxmlStateMachine *self) {
  return self->isInvoked();
}

//  bool QScxmlStateMachine::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine13isInitializedEv(
    const QScxmlStateMachine *self) {
  return self->isInitialized();
}

//  void QScxmlStateMachine::setDataModel(QScxmlDataModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine12setDataModelEP15QScxmlDataModel(
    QScxmlStateMachine *self,
    QScxmlDataModel *model) {
  self->setDataModel(model);
}

//  QScxmlDataModel *QScxmlStateMachine::dataModel() const
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZNK18QScxmlStateMachine9dataModelEv(
    const QScxmlStateMachine *self) {
  return self->dataModel();
}

//  void QScxmlStateMachine::setLoader(QScxmlCompiler::Loader *loader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine9setLoaderEPN14QScxmlCompiler6LoaderE(
    QScxmlStateMachine *self,
    QScxmlCompiler::Loader *loader) {
  self->setLoader(loader);
}

//  QScxmlCompiler::Loader *QScxmlStateMachine::loader() const
extern "C" Q_DECL_EXPORT
QScxmlCompiler::Loader *ritual_ZNK18QScxmlStateMachine6loaderEv(
    const QScxmlStateMachine *self) {
  return self->loader();
}

//  bool QScxmlStateMachine::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine9isRunningEv(
    const QScxmlStateMachine *self) {
  return self->isRunning();
}

//  void QScxmlStateMachine::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine10setRunningEb(
    QScxmlStateMachine *self,
    bool running) {
  self->setRunning(running);
}

//  QVariantMap QScxmlStateMachine::initialValues()
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN18QScxmlStateMachine13initialValuesEv(
    QScxmlStateMachine *self) {
  return new QMap<QString, QVariant>(self->initialValues());
}

//  void QScxmlStateMachine::setInitialValues(const QVariantMap
//      &initialValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine16setInitialValuesERK4QMapI7QString8QVariantE(
    QScxmlStateMachine *self,
    const QMap<QString, QVariant> *initialValues) {
  self->setInitialValues(*initialValues);
}

//  QString QScxmlStateMachine::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QScxmlStateMachine4nameEv(
    const QScxmlStateMachine *self) {
  return new QString(self->name());
}

//  QStringList QScxmlStateMachine::stateNames(bool compress) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QScxmlStateMachine10stateNamesEb(
    const QScxmlStateMachine *self,
    bool compress) {
  return new QList<QString>(self->stateNames(compress));
}

//  QStringList QScxmlStateMachine::activeStateNames(bool compress) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QScxmlStateMachine16activeStateNamesEb(
    const QScxmlStateMachine *self,
    bool compress) {
  return new QList<QString>(self->activeStateNames(compress));
}

//  bool QScxmlStateMachine::isActive(const QString &scxmlStateName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine8isActiveERK7QString(
    const QScxmlStateMachine *self,
    const QString *scxmlStateName) {
  return self->isActive(*scxmlStateName);
}

//  QMetaObject::Connection QScxmlStateMachine::connectToState(const QString
//      &scxmlStateName, const QObject *receiver, const char *method,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN18QScxmlStateMachine14connectToStateERK7QStringPK7QObjectPKcN2Qt14ConnectionTypeE(
    QScxmlStateMachine *self,
    const QString *scxmlStateName,
    const QObject *receiver,
    const char *method,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connectToState(
          *scxmlStateName,
          receiver,
          method,
          type));
}

//  QMetaObject::Connection QScxmlStateMachine::connectToEvent(const QString
//      &scxmlEventSpec, const QObject *receiver, const char *method,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN18QScxmlStateMachine14connectToEventERK7QStringPK7QObjectPKcN2Qt14ConnectionTypeE(
    QScxmlStateMachine *self,
    const QString *scxmlEventSpec,
    const QObject *receiver,
    const char *method,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connectToEvent(
          *scxmlEventSpec,
          receiver,
          method,
          type));
}

//  void QScxmlStateMachine::submitEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine11submitEventEP11QScxmlEvent(
    QScxmlStateMachine *self,
    QScxmlEvent *event) {
  self->submitEvent(event);
}

//  void QScxmlStateMachine::submitEvent(const QString &eventName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine11submitEventERK7QString(
    QScxmlStateMachine *self,
    const QString *eventName) {
  self->submitEvent(*eventName);
}

//  void QScxmlStateMachine::submitEvent(const QString &eventName, const
//      QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine11submitEventERK7QStringRK8QVariant(
    QScxmlStateMachine *self,
    const QString *eventName,
    const QVariant *data) {
  self->submitEvent(*eventName, *data);
}

//  void QScxmlStateMachine::cancelDelayedEvent(const QString &sendId)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine18cancelDelayedEventERK7QString(
    QScxmlStateMachine *self,
    const QString *sendId) {
  self->cancelDelayedEvent(*sendId);
}

//  bool QScxmlStateMachine::isDispatchableTarget(const QString &target)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine20isDispatchableTargetERK7QString(
    const QScxmlStateMachine *self,
    const QString *target) {
  return self->isDispatchableTarget(*target);
}

//  QList<QScxmlInvokableService *> QScxmlStateMachine::invokedServices()
//      const
extern "C" Q_DECL_EXPORT
QList<QScxmlInvokableService *> *ritual_ZNK18QScxmlStateMachine15invokedServicesEv(
    const QScxmlStateMachine *self) {
  return new QList<QScxmlInvokableService *>(self->invokedServices());
}

//  QScxmlTableData *QScxmlStateMachine::tableData() const
extern "C" Q_DECL_EXPORT
QScxmlTableData *ritual_ZNK18QScxmlStateMachine9tableDataEv(
    const QScxmlStateMachine *self) {
  return self->tableData();
}

//  void QScxmlStateMachine::setTableData(QScxmlTableData *tableData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine12setTableDataEP15QScxmlTableData(
    QScxmlStateMachine *self,
    QScxmlTableData *tableData) {
  self->setTableData(tableData);
}

//  void QScxmlStateMachine::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine5startEv(QScxmlStateMachine *self) {
  self->start();
}

//  void QScxmlStateMachine::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine4stopEv(QScxmlStateMachine *self) {
  self->stop();
}

//  bool QScxmlStateMachine::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QScxmlStateMachine4initEv(QScxmlStateMachine *self) {
  return self->init();
}

//  bool QScxmlStateMachine::isActive(int stateIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QScxmlStateMachine8isActiveEi(
    const QScxmlStateMachine *self,
    int stateIndex) {
  return self->isActive(stateIndex);
}
