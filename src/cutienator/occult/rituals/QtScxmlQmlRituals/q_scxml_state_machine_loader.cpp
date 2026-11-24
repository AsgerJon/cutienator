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

//  const QMetaObject *QScxmlStateMachineLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QScxmlStateMachineLoader10metaObjectEv(
    const QScxmlStateMachineLoader *self) {
  return self->metaObject();
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
