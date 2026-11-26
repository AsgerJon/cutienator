//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/qscxmlqmlglobals_p.h>
#include <QtScxmlQml/QtScxmlQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QBindable>
#include <QtScxml/QScxmlStateMachine>
#include <QtCore/QUrl>
#include <QtCore/QVariantMap>
#include <QtScxml/QScxmlDataModel>

//  const QMetaObject *QScxmlStateMachineLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QScxmlStateMachineLoader10metaObjectEv(
    const QScxmlStateMachineLoader *self) {
  return self->metaObject();
}

//  void *QScxmlStateMachineLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QScxmlStateMachineLoader11qt_metacastEPKc(
    QScxmlStateMachineLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlStateMachineLoader::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QScxmlStateMachineLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlStateMachineLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlStateMachineLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QScxmlStateMachineLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStateMachineLoader::tr(s, c, n));
}

//  QScxmlStateMachineLoader::QScxmlStateMachineLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlStateMachineLoader *ritual_ZN24QScxmlStateMachineLoaderC1EP7QObject(
    QObject *parent) {
  return new QScxmlStateMachineLoader(parent);
}

//  QScxmlStateMachine *QScxmlStateMachineLoader::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK24QScxmlStateMachineLoader12stateMachineEv(
    const QScxmlStateMachineLoader *self) {
  return self->stateMachine();
}

//  QBindable<QScxmlStateMachine *>
//      QScxmlStateMachineLoader::bindableStateMachine()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlStateMachine *> *ritual_ZN24QScxmlStateMachineLoader20bindableStateMachineEv(
    QScxmlStateMachineLoader *self) {
  return new QBindable<QScxmlStateMachine *>(self->bindableStateMachine());
}

//  QUrl QScxmlStateMachineLoader::source()
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN24QScxmlStateMachineLoader6sourceEv(
    QScxmlStateMachineLoader *self) {
  return new QUrl(self->source());
}

//  void QScxmlStateMachineLoader::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader9setSourceERK4QUrl(
    QScxmlStateMachineLoader *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QBindable<QUrl> QScxmlStateMachineLoader::bindableSource()
extern "C" Q_DECL_EXPORT
QBindable<QUrl> *ritual_ZN24QScxmlStateMachineLoader14bindableSourceEv(
    QScxmlStateMachineLoader *self) {
  return new QBindable<QUrl>(self->bindableSource());
}

//  QVariantMap QScxmlStateMachineLoader::initialValues() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK24QScxmlStateMachineLoader13initialValuesEv(
    const QScxmlStateMachineLoader *self) {
  return new QMap<QString, QVariant>(self->initialValues());
}

//  void QScxmlStateMachineLoader::setInitialValues(const QVariantMap
//      &initialValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader16setInitialValuesERK4QMapI7QString8QVariantE(
    QScxmlStateMachineLoader *self,
    const QMap<QString, QVariant> *initialValues) {
  self->setInitialValues(*initialValues);
}

//  QBindable<QVariantMap> QScxmlStateMachineLoader::bindableInitialValues()
extern "C" Q_DECL_EXPORT
QBindable<QVariantMap> *ritual_ZN24QScxmlStateMachineLoader21bindableInitialValuesEv(
    QScxmlStateMachineLoader *self) {
  return new QBindable<QVariantMap>(self->bindableInitialValues());
}

//  QScxmlDataModel *QScxmlStateMachineLoader::dataModel() const
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZNK24QScxmlStateMachineLoader9dataModelEv(
    const QScxmlStateMachineLoader *self) {
  return self->dataModel();
}

//  void QScxmlStateMachineLoader::setDataModel(QScxmlDataModel *dataModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader12setDataModelEP15QScxmlDataModel(
    QScxmlStateMachineLoader *self,
    QScxmlDataModel *dataModel) {
  self->setDataModel(dataModel);
}

//  QBindable<QScxmlDataModel *>
//      QScxmlStateMachineLoader::bindableDataModel()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlDataModel *> *ritual_ZN24QScxmlStateMachineLoader17bindableDataModelEv(
    QScxmlStateMachineLoader *self) {
  return new QBindable<QScxmlDataModel *>(self->bindableDataModel());
}

//  void QScxmlStateMachineLoader::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader13sourceChangedEv(
    QScxmlStateMachineLoader *self) {
  self->sourceChanged();
}

//  void QScxmlStateMachineLoader::initialValuesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader20initialValuesChangedEv(
    QScxmlStateMachineLoader *self) {
  self->initialValuesChanged();
}

//  void QScxmlStateMachineLoader::stateMachineChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader19stateMachineChangedEv(
    QScxmlStateMachineLoader *self) {
  self->stateMachineChanged();
}

//  void QScxmlStateMachineLoader::dataModelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader16dataModelChangedEv(
    QScxmlStateMachineLoader *self) {
  self->dataModelChanged();
}

//  bool QScxmlStateMachineLoader::parse(const QUrl &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QScxmlStateMachineLoader5parseERK4QUrl(
    QScxmlStateMachineLoader *self,
    const QUrl *source) {
  return self->parse(*source);
}

//  void QScxmlStateMachineLoader::setStateMachine(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScxmlStateMachineLoader15setStateMachineEP18QScxmlStateMachine(
    QScxmlStateMachineLoader *self,
    QScxmlStateMachine *stateMachine) {
  self->setStateMachine(stateMachine);
}

//  size_t QScxmlStateMachineLoader::_qt_property_m_source_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN24QScxmlStateMachineLoader28_qt_property_m_source_offsetEv() {
  return QScxmlStateMachineLoader::_qt_property_m_source_offset();
}

//  size_t QScxmlStateMachineLoader::_qt_property_m_initialValues_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN24QScxmlStateMachineLoader35_qt_property_m_initialValues_offsetEv() {
  return QScxmlStateMachineLoader::_qt_property_m_initialValues_offset();
}

//  size_t QScxmlStateMachineLoader::_qt_property_m_dataModel_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN24QScxmlStateMachineLoader31_qt_property_m_dataModel_offsetEv() {
  return QScxmlStateMachineLoader::_qt_property_m_dataModel_offset();
}

//  size_t QScxmlStateMachineLoader::_qt_property_m_stateMachine_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN24QScxmlStateMachineLoader34_qt_property_m_stateMachine_offsetEv() {
  return QScxmlStateMachineLoader::_qt_property_m_stateMachine_offset();
}

//  a QBindable<QScxmlStateMachine *> a ritual of QScxmlStateMachineLoader
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineLoader__QBindable_QScxmlStateMachine(
    QBindable<QScxmlStateMachine *> *self) {
  delete self;
}

//  a QBindable<QUrl> a ritual of QScxmlStateMachineLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineLoader__QBindable_QUrl(
    QBindable<QUrl> *self) {
  delete self;
}

//  a QBindable<QVariantMap> a ritual of QScxmlStateMachineLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineLoader__QBindable_QVariantMap(
    QBindable<QVariantMap> *self) {
  delete self;
}

//  a QBindable<QScxmlDataModel *> a ritual of QScxmlStateMachineLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineLoader__QBindable_QScxmlDataModel(
    QBindable<QScxmlDataModel *> *self) {
  delete self;
}
