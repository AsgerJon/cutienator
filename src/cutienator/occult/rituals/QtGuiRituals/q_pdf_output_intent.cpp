//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpdfoutputintent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_PDF)
#include <QtGui/qpdfoutputintent.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qcolorspace.h>

//  QPdfOutputIntent::QPdfOutputIntent()
extern "C" Q_DECL_EXPORT
QPdfOutputIntent *ritual_ZN16QPdfOutputIntentC1Ev() {
  return new QPdfOutputIntent();
}

//  QPdfOutputIntent::QPdfOutputIntent(const QPdfOutputIntent &other)
extern "C" Q_DECL_EXPORT
QPdfOutputIntent *ritual_ZN16QPdfOutputIntentC1ERKS_(
    const QPdfOutputIntent *other) {
  return new QPdfOutputIntent(*other);
}

//  QPdfOutputIntent::~QPdfOutputIntent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfOutputIntentD1Ev(QPdfOutputIntent *self) {
  delete self;
}

//  QString QPdfOutputIntent::outputConditionIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QPdfOutputIntent25outputConditionIdentifierEv(
    const QPdfOutputIntent *self) {
  return new QString(self->outputConditionIdentifier());
}

//  void QPdfOutputIntent::setOutputConditionIdentifier(const QString
//      &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfOutputIntent28setOutputConditionIdentifierERK7QString(
    QPdfOutputIntent *self,
    const QString *identifier) {
  self->setOutputConditionIdentifier(*identifier);
}

//  QString QPdfOutputIntent::outputCondition() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QPdfOutputIntent15outputConditionEv(
    const QPdfOutputIntent *self) {
  return new QString(self->outputCondition());
}

//  void QPdfOutputIntent::setOutputCondition(const QString &condition)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfOutputIntent18setOutputConditionERK7QString(
    QPdfOutputIntent *self,
    const QString *condition) {
  self->setOutputCondition(*condition);
}

//  QUrl QPdfOutputIntent::registryName() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QPdfOutputIntent12registryNameEv(
    const QPdfOutputIntent *self) {
  return new QUrl(self->registryName());
}

//  void QPdfOutputIntent::setRegistryName(const QUrl &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfOutputIntent15setRegistryNameERK4QUrl(
    QPdfOutputIntent *self,
    const QUrl *name) {
  self->setRegistryName(*name);
}

//  QColorSpace QPdfOutputIntent::outputProfile() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK16QPdfOutputIntent13outputProfileEv(
    const QPdfOutputIntent *self) {
  return new QColorSpace(self->outputProfile());
}

//  void QPdfOutputIntent::setOutputProfile(const QColorSpace &profile)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfOutputIntent16setOutputProfileERK11QColorSpace(
    QPdfOutputIntent *self,
    const QColorSpace *profile) {
  self->setOutputProfile(*profile);
}

#endif  // !defined(QT_NO_PDF)
