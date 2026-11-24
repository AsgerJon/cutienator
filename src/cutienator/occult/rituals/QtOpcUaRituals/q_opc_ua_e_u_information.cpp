//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaeuinformation.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaeuinformation.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qvariant.h>

//  QOpcUaEUInformation::QOpcUaEUInformation()
extern "C" Q_DECL_EXPORT
QOpcUaEUInformation *ritual_ZN19QOpcUaEUInformationC1Ev() {
  return new QOpcUaEUInformation();
}

//  QOpcUaEUInformation::QOpcUaEUInformation(const QOpcUaEUInformation &a0)
extern "C" Q_DECL_EXPORT
QOpcUaEUInformation *ritual_ZN19QOpcUaEUInformationC1ERKS_(
    const QOpcUaEUInformation *a0) {
  return new QOpcUaEUInformation(*a0);
}

//  QOpcUaEUInformation::QOpcUaEUInformation(const QString &namespaceUri,
//      qint32 unitId, const QOpcUaLocalizedText &displayName, const
//      QOpcUaLocalizedText &description)
extern "C" Q_DECL_EXPORT
QOpcUaEUInformation *ritual_ZN19QOpcUaEUInformationC1ERK7QStringiRK19QOpcUaLocalizedTextS5_(
    const QString *namespaceUri,
    qint32 unitId,
    const QOpcUaLocalizedText *displayName,
    const QOpcUaLocalizedText *description) {
  return new QOpcUaEUInformation(
      *namespaceUri,
      unitId,
      *displayName,
      *description);
}

//  bool QOpcUaEUInformation::operator==(const QOpcUaEUInformation &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaEUInformationeqERKS_(
    const QOpcUaEUInformation *self,
    const QOpcUaEUInformation *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaEUInformation::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QOpcUaEUInformationcv8QVariantEv(
    const QOpcUaEUInformation *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaEUInformation::~QOpcUaEUInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaEUInformationD1Ev(QOpcUaEUInformation *self) {
  delete self;
}

//  QString QOpcUaEUInformation::namespaceUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpcUaEUInformation12namespaceUriEv(
    const QOpcUaEUInformation *self) {
  return new QString(self->namespaceUri());
}

//  void QOpcUaEUInformation::setNamespaceUri(const QString &namespaceUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaEUInformation15setNamespaceUriERK7QString(
    QOpcUaEUInformation *self,
    const QString *namespaceUri) {
  self->setNamespaceUri(*namespaceUri);
}

//  qint32 QOpcUaEUInformation::unitId() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK19QOpcUaEUInformation6unitIdEv(
    const QOpcUaEUInformation *self) {
  return self->unitId();
}

//  void QOpcUaEUInformation::setUnitId(qint32 unitId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaEUInformation9setUnitIdEi(
    QOpcUaEUInformation *self,
    qint32 unitId) {
  self->setUnitId(unitId);
}

//  QOpcUaLocalizedText QOpcUaEUInformation::displayName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK19QOpcUaEUInformation11displayNameEv(
    const QOpcUaEUInformation *self) {
  return new QOpcUaLocalizedText(self->displayName());
}

//  void QOpcUaEUInformation::setDisplayName(const QOpcUaLocalizedText
//      &displayName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaEUInformation14setDisplayNameERK19QOpcUaLocalizedText(
    QOpcUaEUInformation *self,
    const QOpcUaLocalizedText *displayName) {
  self->setDisplayName(*displayName);
}

//  QOpcUaLocalizedText QOpcUaEUInformation::description() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK19QOpcUaEUInformation11descriptionEv(
    const QOpcUaEUInformation *self) {
  return new QOpcUaLocalizedText(self->description());
}

//  void QOpcUaEUInformation::setDescription(const QOpcUaLocalizedText
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaEUInformation14setDescriptionERK19QOpcUaLocalizedText(
    QOpcUaEUInformation *self,
    const QOpcUaLocalizedText *description) {
  self->setDescription(*description);
}
