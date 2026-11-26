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
#include <QtCore/QBindable>
#include <QtScxml/QScxmlDataModel>
#include <QtScxml/QScxmlCompiler>
#include <QtCore/QVariantMap>
#include <functional>
#include <QtCore/QList>
#include <QtScxml/QScxmlInvokableService>
#include <QtScxml/QScxmlTableData>

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

//  void *QScxmlStateMachine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QScxmlStateMachine11qt_metacastEPKc(
    QScxmlStateMachine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlStateMachine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QScxmlStateMachine11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlStateMachine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QScxmlStateMachine::QScxmlStateMachine(QScxmlStateMachinePrivate &dd,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN18QScxmlStateMachineC1ER25QScxmlStateMachinePrivateP7QObject(
    QScxmlStateMachinePrivate *dd,
    QObject *parent) {
  return new QScxmlStateMachine(*dd, parent);
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

//  QBindable<bool> QScxmlStateMachine::bindableInitialized() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK18QScxmlStateMachine19bindableInitializedEv(
    const QScxmlStateMachine *self) {
  return new QBindable<bool>(self->bindableInitialized());
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

//  QBindable<QScxmlDataModel *> QScxmlStateMachine::bindableDataModel()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlDataModel *> *ritual_ZN18QScxmlStateMachine17bindableDataModelEv(
    QScxmlStateMachine *self) {
  return new QBindable<QScxmlDataModel *>(self->bindableDataModel());
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

//  QBindable<QScxmlCompiler::Loader *> QScxmlStateMachine::bindableLoader()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlCompiler::Loader *> *ritual_ZN18QScxmlStateMachine14bindableLoaderEv(
    QScxmlStateMachine *self) {
  return new QBindable<QScxmlCompiler::Loader *>(self->bindableLoader());
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

//  QBindable<QVariantMap> QScxmlStateMachine::bindableInitialValues()
extern "C" Q_DECL_EXPORT
QBindable<QVariantMap> *ritual_ZN18QScxmlStateMachine21bindableInitialValuesEv(
    QScxmlStateMachine *self) {
  return new QBindable<QVariantMap>(self->bindableInitialValues());
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

//  std::function<void (bool)> QScxmlStateMachine::onEntry(const QObject
//      *receiver, const char *method)
extern "C" Q_DECL_EXPORT
std::function<void (bool)> *ritual_ZN18QScxmlStateMachine7onEntryEPK7QObjectPKc(
    const QObject *receiver,
    const char *method) {
  return new std::function<void (bool)>(
      QScxmlStateMachine::onEntry(
          receiver,
          method));
}

//  std::function<void (bool)> QScxmlStateMachine::onExit(const QObject
//      *receiver, const char *method)
extern "C" Q_DECL_EXPORT
std::function<void (bool)> *ritual_ZN18QScxmlStateMachine6onExitEPK7QObjectPKc(
    const QObject *receiver,
    const char *method) {
  return new std::function<void (bool)>(
      QScxmlStateMachine::onExit(
          receiver,
          method));
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

//  QBindable<QList<QScxmlInvokableService *>>
//      QScxmlStateMachine::bindableInvokedServices()
extern "C" Q_DECL_EXPORT
QBindable<QList<QScxmlInvokableService *>> *ritual_ZN18QScxmlStateMachine23bindableInvokedServicesEv(
    QScxmlStateMachine *self) {
  return new QBindable<QList<QScxmlInvokableService *>>(
      self->bindableInvokedServices());
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

//  QBindable<QScxmlTableData *> QScxmlStateMachine::bindableTableData()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlTableData *> *ritual_ZN18QScxmlStateMachine17bindableTableDataEv(
    QScxmlStateMachine *self) {
  return new QBindable<QScxmlTableData *>(self->bindableTableData());
}

//  void QScxmlStateMachine::runningChanged(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine14runningChangedEb(
    QScxmlStateMachine *self,
    bool running) {
  self->runningChanged(running);
}

//  void QScxmlStateMachine::invokedServicesChanged(const
//      QList<QScxmlInvokableService *> &invokedServices)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine22invokedServicesChangedERK5QListIP22QScxmlInvokableServiceE(
    QScxmlStateMachine *self,
    const QList<QScxmlInvokableService *> *invokedServices) {
  self->invokedServicesChanged(*invokedServices);
}

//  void QScxmlStateMachine::log(const QString &label, const QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine3logERK7QStringS2_(
    QScxmlStateMachine *self,
    const QString *label,
    const QString *msg) {
  self->log(*label, *msg);
}

//  void QScxmlStateMachine::reachedStableState()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine18reachedStableStateEv(
    QScxmlStateMachine *self) {
  self->reachedStableState();
}

//  void QScxmlStateMachine::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine8finishedEv(QScxmlStateMachine *self) {
  self->finished();
}

//  void QScxmlStateMachine::dataModelChanged(QScxmlDataModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine16dataModelChangedEP15QScxmlDataModel(
    QScxmlStateMachine *self,
    QScxmlDataModel *model) {
  self->dataModelChanged(model);
}

//  void QScxmlStateMachine::initialValuesChanged(const QVariantMap
//      &initialValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine20initialValuesChangedERK4QMapI7QString8QVariantE(
    QScxmlStateMachine *self,
    const QMap<QString, QVariant> *initialValues) {
  self->initialValuesChanged(*initialValues);
}

//  void QScxmlStateMachine::initializedChanged(bool initialized)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine18initializedChangedEb(
    QScxmlStateMachine *self,
    bool initialized) {
  self->initializedChanged(initialized);
}

//  void QScxmlStateMachine::loaderChanged(QScxmlCompiler::Loader *loader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine13loaderChangedEPN14QScxmlCompiler6LoaderE(
    QScxmlStateMachine *self,
    QScxmlCompiler::Loader *loader) {
  self->loaderChanged(loader);
}

//  void QScxmlStateMachine::tableDataChanged(QScxmlTableData *tableData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlStateMachine16tableDataChangedEP15QScxmlTableData(
    QScxmlStateMachine *self,
    QScxmlTableData *tableData) {
  self->tableDataChanged(tableData);
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

//  QMetaObject::Connection QScxmlStateMachine::connectToStateImpl(const
//      QString &scxmlStateName, const QObject *receiver, void **slot,
//      QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN18QScxmlStateMachine18connectToStateImplERK7QStringPK7QObjectPPvPN9QtPrivate15QSlotObjectBaseEN2Qt14ConnectionTypeE(
    QScxmlStateMachine *self,
    const QString *scxmlStateName,
    const QObject *receiver,
    void **slot,
    QtPrivate::QSlotObjectBase *slotObj,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connectToStateImpl(
          *scxmlStateName,
          receiver,
          slot,
          slotObj,
          type));
}

//  QMetaObject::Connection QScxmlStateMachine::connectToEventImpl(const
//      QString &scxmlEventSpec, const QObject *receiver, void **slot,
//      QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN18QScxmlStateMachine18connectToEventImplERK7QStringPK7QObjectPPvPN9QtPrivate15QSlotObjectBaseEN2Qt14ConnectionTypeE(
    QScxmlStateMachine *self,
    const QString *scxmlEventSpec,
    const QObject *receiver,
    void **slot,
    QtPrivate::QSlotObjectBase *slotObj,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connectToEventImpl(
          *scxmlEventSpec,
          receiver,
          slot,
          slotObj,
          type));
}

//  a QBindable<bool> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_bool(QBindable<bool> *self) {
  delete self;
}

//  a QBindable<QScxmlDataModel *> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_QScxmlDataModel(
    QBindable<QScxmlDataModel *> *self) {
  delete self;
}

//  a QBindable<QScxmlCompiler::Loader *> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_QScxmlCompiler_Loader(
    QBindable<QScxmlCompiler::Loader *> *self) {
  delete self;
}

//  a QBindable<QVariantMap> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_QVariantMap(
    QBindable<QVariantMap> *self) {
  delete self;
}

//  a std::function<void (bool)> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__std_function_void_bool(
    std::function<void (bool)> *self) {
  delete self;
}

//  a QBindable<QList<QScxmlInvokableService *>> a ritual of
//      QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_QList_QScxmlInvokableService(
    QBindable<QList<QScxmlInvokableService *>> *self) {
  delete self;
}

//  a QBindable<QScxmlTableData *> a ritual of QScxmlStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachine__QBindable_QScxmlTableData(
    QBindable<QScxmlTableData *> *self) {
  delete self;
}
