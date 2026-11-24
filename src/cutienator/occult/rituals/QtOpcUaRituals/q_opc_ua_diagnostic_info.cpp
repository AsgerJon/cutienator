//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuadiagnosticinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuadiagnosticinfo.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo()
extern "C" Q_DECL_EXPORT
QOpcUaDiagnosticInfo *ritual_ZN20QOpcUaDiagnosticInfoC1Ev() {
  return new QOpcUaDiagnosticInfo();
}

//  QOpcUaDiagnosticInfo::~QOpcUaDiagnosticInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfoD1Ev(QOpcUaDiagnosticInfo *self) {
  delete self;
}

//  QOpcUaDiagnosticInfo::QOpcUaDiagnosticInfo(const QOpcUaDiagnosticInfo
//      &other)
extern "C" Q_DECL_EXPORT
QOpcUaDiagnosticInfo *ritual_ZN20QOpcUaDiagnosticInfoC1ERKS_(
    const QOpcUaDiagnosticInfo *other) {
  return new QOpcUaDiagnosticInfo(*other);
}

//  QVariant QOpcUaDiagnosticInfo::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaDiagnosticInfocv8QVariantEv(
    const QOpcUaDiagnosticInfo *self) {
  return new QVariant(self->operator QVariant());
}

//  qint32 QOpcUaDiagnosticInfo::symbolicId() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK20QOpcUaDiagnosticInfo10symbolicIdEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->symbolicId();
}

//  void QOpcUaDiagnosticInfo::setSymbolicId(qint32 newSymbolicId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo13setSymbolicIdEi(
    QOpcUaDiagnosticInfo *self,
    qint32 newSymbolicId) {
  self->setSymbolicId(newSymbolicId);
}

//  bool QOpcUaDiagnosticInfo::hasSymbolicId() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo13hasSymbolicIdEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasSymbolicId();
}

//  void QOpcUaDiagnosticInfo::setHasSymbolicId(bool newHasSymbolicId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo16setHasSymbolicIdEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasSymbolicId) {
  self->setHasSymbolicId(newHasSymbolicId);
}

//  qint32 QOpcUaDiagnosticInfo::namespaceUri() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK20QOpcUaDiagnosticInfo12namespaceUriEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->namespaceUri();
}

//  void QOpcUaDiagnosticInfo::setNamespaceUri(qint32 newNamespaceUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo15setNamespaceUriEi(
    QOpcUaDiagnosticInfo *self,
    qint32 newNamespaceUri) {
  self->setNamespaceUri(newNamespaceUri);
}

//  bool QOpcUaDiagnosticInfo::hasNamespaceUri() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo15hasNamespaceUriEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasNamespaceUri();
}

//  void QOpcUaDiagnosticInfo::setHasNamespaceUri(bool newHasNamespaceUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo18setHasNamespaceUriEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasNamespaceUri) {
  self->setHasNamespaceUri(newHasNamespaceUri);
}

//  qint32 QOpcUaDiagnosticInfo::locale() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK20QOpcUaDiagnosticInfo6localeEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->locale();
}

//  void QOpcUaDiagnosticInfo::setLocale(qint32 newLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo9setLocaleEi(
    QOpcUaDiagnosticInfo *self,
    qint32 newLocale) {
  self->setLocale(newLocale);
}

//  bool QOpcUaDiagnosticInfo::hasLocale() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo9hasLocaleEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasLocale();
}

//  void QOpcUaDiagnosticInfo::setHasLocale(bool newHasLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo12setHasLocaleEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasLocale) {
  self->setHasLocale(newHasLocale);
}

//  qint32 QOpcUaDiagnosticInfo::localizedText() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK20QOpcUaDiagnosticInfo13localizedTextEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->localizedText();
}

//  void QOpcUaDiagnosticInfo::setLocalizedText(qint32 newLocalizedText)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo16setLocalizedTextEi(
    QOpcUaDiagnosticInfo *self,
    qint32 newLocalizedText) {
  self->setLocalizedText(newLocalizedText);
}

//  bool QOpcUaDiagnosticInfo::hasLocalizedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo16hasLocalizedTextEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasLocalizedText();
}

//  void QOpcUaDiagnosticInfo::setHasLocalizedText(bool newHasLocalizedText)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo19setHasLocalizedTextEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasLocalizedText) {
  self->setHasLocalizedText(newHasLocalizedText);
}

//  QString QOpcUaDiagnosticInfo::additionalInfo() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpcUaDiagnosticInfo14additionalInfoEv(
    const QOpcUaDiagnosticInfo *self) {
  return new QString(self->additionalInfo());
}

//  void QOpcUaDiagnosticInfo::setAdditionalInfo(const QString
//      &newAdditionalInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo17setAdditionalInfoERK7QString(
    QOpcUaDiagnosticInfo *self,
    const QString *newAdditionalInfo) {
  self->setAdditionalInfo(*newAdditionalInfo);
}

//  bool QOpcUaDiagnosticInfo::hasAdditionalInfo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo17hasAdditionalInfoEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasAdditionalInfo();
}

//  void QOpcUaDiagnosticInfo::setHasAdditionalInfo(bool
//      newHasAdditionalInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo20setHasAdditionalInfoEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasAdditionalInfo) {
  self->setHasAdditionalInfo(newHasAdditionalInfo);
}

//  QOpcUa::UaStatusCode QOpcUaDiagnosticInfo::innerStatusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK20QOpcUaDiagnosticInfo15innerStatusCodeEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->innerStatusCode();
}

//  void QOpcUaDiagnosticInfo::setInnerStatusCode(QOpcUa::UaStatusCode
//      newInnerStatusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo18setInnerStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaDiagnosticInfo *self,
    QOpcUa::UaStatusCode newInnerStatusCode) {
  self->setInnerStatusCode(newInnerStatusCode);
}

//  bool QOpcUaDiagnosticInfo::hasInnerStatusCode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo18hasInnerStatusCodeEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasInnerStatusCode();
}

//  void QOpcUaDiagnosticInfo::setHasInnerStatusCode(bool
//      newHasInnerStatusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo21setHasInnerStatusCodeEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasInnerStatusCode) {
  self->setHasInnerStatusCode(newHasInnerStatusCode);
}

//  QOpcUaDiagnosticInfo QOpcUaDiagnosticInfo::innerDiagnosticInfo() const
extern "C" Q_DECL_EXPORT
QOpcUaDiagnosticInfo *ritual_ZNK20QOpcUaDiagnosticInfo19innerDiagnosticInfoEv(
    const QOpcUaDiagnosticInfo *self) {
  return new QOpcUaDiagnosticInfo(self->innerDiagnosticInfo());
}

//  void QOpcUaDiagnosticInfo::setInnerDiagnosticInfo(const
//      QOpcUaDiagnosticInfo &newInnerDiagnosticInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo22setInnerDiagnosticInfoERKS_(
    QOpcUaDiagnosticInfo *self,
    const QOpcUaDiagnosticInfo *newInnerDiagnosticInfo) {
  self->setInnerDiagnosticInfo(*newInnerDiagnosticInfo);
}

//  bool QOpcUaDiagnosticInfo::hasInnerDiagnosticInfo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaDiagnosticInfo22hasInnerDiagnosticInfoEv(
    const QOpcUaDiagnosticInfo *self) {
  return self->hasInnerDiagnosticInfo();
}

//  void QOpcUaDiagnosticInfo::setHasInnerDiagnosticInfo(bool
//      newHasInnerDiagnosticInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaDiagnosticInfo25setHasInnerDiagnosticInfoEb(
    QOpcUaDiagnosticInfo *self,
    bool newHasInnerDiagnosticInfo) {
  self->setHasInnerDiagnosticInfo(newHasInnerDiagnosticInfo);
}

//  bool operator==(const QOpcUaDiagnosticInfo &lhs, const
//      QOpcUaDiagnosticInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpcUaDiagnosticInfoS1_(
    const QOpcUaDiagnosticInfo *lhs,
    const QOpcUaDiagnosticInfo *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaDiagnosticInfo &lhs, const
//      QOpcUaDiagnosticInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpcUaDiagnosticInfoS1_(
    const QOpcUaDiagnosticInfo *lhs,
    const QOpcUaDiagnosticInfo *rhs) {
  return operator!=(*lhs, *rhs);
}
