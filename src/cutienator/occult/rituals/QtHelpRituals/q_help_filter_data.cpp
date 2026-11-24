//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpfilterdata.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelpfilterdata.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qlist.h>

//  QHelpFilterData::QHelpFilterData()
extern "C" Q_DECL_EXPORT
QHelpFilterData *ritual_ZN15QHelpFilterDataC1Ev() {
  return new QHelpFilterData();
}

//  QHelpFilterData::QHelpFilterData(const QHelpFilterData &other)
extern "C" Q_DECL_EXPORT
QHelpFilterData *ritual_ZN15QHelpFilterDataC1ERKS_(
    const QHelpFilterData *other) {
  return new QHelpFilterData(*other);
}

//  QHelpFilterData::~QHelpFilterData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpFilterDataD1Ev(QHelpFilterData *self) {
  delete self;
}

//  bool QHelpFilterData::operator==(const QHelpFilterData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QHelpFilterDataeqERKS_(
    const QHelpFilterData *self,
    const QHelpFilterData *other) {
  return self->operator==(*other);
}

//  void QHelpFilterData::setComponents(const QStringList &components)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpFilterData13setComponentsERK5QListI7QStringE(
    QHelpFilterData *self,
    const QList<QString> *components) {
  self->setComponents(*components);
}

//  void QHelpFilterData::setVersions(const QList<QVersionNumber> &versions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpFilterData11setVersionsERK5QListI14QVersionNumberE(
    QHelpFilterData *self,
    const QList<QVersionNumber> *versions) {
  self->setVersions(*versions);
}

//  QStringList QHelpFilterData::components() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QHelpFilterData10componentsEv(
    const QHelpFilterData *self) {
  return new QList<QString>(self->components());
}

//  QList<QVersionNumber> QHelpFilterData::versions() const
extern "C" Q_DECL_EXPORT
QList<QVersionNumber> *ritual_ZNK15QHelpFilterData8versionsEv(
    const QHelpFilterData *self) {
  return new QList<QVersionNumber>(self->versions());
}
