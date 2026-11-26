//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuanodecreationattributes.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuanodecreationattributes.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qvariant.h>
#include <QtCore/QList>

//  QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes()
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributes *ritual_ZN28QOpcUaNodeCreationAttributesC1Ev() {
  return new QOpcUaNodeCreationAttributes();
}

//  QOpcUaNodeCreationAttributes::QOpcUaNodeCreationAttributes(const
//      QOpcUaNodeCreationAttributes &other)
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributes *ritual_ZN28QOpcUaNodeCreationAttributesC1ERKS_(
    const QOpcUaNodeCreationAttributes *other) {
  return new QOpcUaNodeCreationAttributes(*other);
}

//  QOpcUaNodeCreationAttributes
//      &QOpcUaNodeCreationAttributes::operator=(const
//      QOpcUaNodeCreationAttributes &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributes *ritual_ZN28QOpcUaNodeCreationAttributesaSERKS_(
    QOpcUaNodeCreationAttributes *self,
    const QOpcUaNodeCreationAttributes *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaNodeCreationAttributes::~QOpcUaNodeCreationAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributesD1Ev(
    QOpcUaNodeCreationAttributes *self) {
  delete self;
}

//  QOpcUa::AccessLevel QOpcUaNodeCreationAttributes::accessLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QOpcUaNodeCreationAttributes11accessLevelEv(
    const QOpcUaNodeCreationAttributes *self) {
  return static_cast<int>(self->accessLevel().toInt());
}

//  void QOpcUaNodeCreationAttributes::setAccessLevel(QOpcUa::AccessLevel
//      accessLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes14setAccessLevelE6QFlagsIN6QOpcUa14AccessLevelBitEE(
    QOpcUaNodeCreationAttributes *self,
    int accessLevel) {
  self->setAccessLevel(QFlags<QOpcUa::AccessLevelBit>::fromInt(accessLevel));
}

//  bool QOpcUaNodeCreationAttributes::hasAccessLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14hasAccessLevelEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasAccessLevel();
}

//  QList<quint32> QOpcUaNodeCreationAttributes::arrayDimensions() const
extern "C" Q_DECL_EXPORT
QList<quint32> *ritual_ZNK28QOpcUaNodeCreationAttributes15arrayDimensionsEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QList<quint32>(self->arrayDimensions());
}

//  void QOpcUaNodeCreationAttributes::setArrayDimensions(const
//      QList<quint32> &arrayDimensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes18setArrayDimensionsERK5QListIjE(
    QOpcUaNodeCreationAttributes *self,
    const QList<quint32> *arrayDimensions) {
  self->setArrayDimensions(*arrayDimensions);
}

//  bool QOpcUaNodeCreationAttributes::hasArrayDimensions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes18hasArrayDimensionsEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasArrayDimensions();
}

//  bool QOpcUaNodeCreationAttributes::containsNoLoops() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes15containsNoLoopsEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->containsNoLoops();
}

//  void QOpcUaNodeCreationAttributes::setContainsNoLoops(bool
//      containsNoLoops)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes18setContainsNoLoopsEb(
    QOpcUaNodeCreationAttributes *self,
    bool containsNoLoops) {
  self->setContainsNoLoops(containsNoLoops);
}

//  bool QOpcUaNodeCreationAttributes::hasContainsNoLoops() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes18hasContainsNoLoopsEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasContainsNoLoops();
}

//  QString QOpcUaNodeCreationAttributes::dataTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaNodeCreationAttributes10dataTypeIdEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QString(self->dataTypeId());
}

//  void QOpcUaNodeCreationAttributes::setDataTypeId(const QString
//      &dataTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes13setDataTypeIdERK7QString(
    QOpcUaNodeCreationAttributes *self,
    const QString *dataTypeId) {
  self->setDataTypeId(*dataTypeId);
}

//  bool QOpcUaNodeCreationAttributes::hasDataTypeId() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes13hasDataTypeIdEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasDataTypeId();
}

//  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::description() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK28QOpcUaNodeCreationAttributes11descriptionEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QOpcUaLocalizedText(self->description());
}

//  void QOpcUaNodeCreationAttributes::setDescription(const
//      QOpcUaLocalizedText &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes14setDescriptionERK19QOpcUaLocalizedText(
    QOpcUaNodeCreationAttributes *self,
    const QOpcUaLocalizedText *description) {
  self->setDescription(*description);
}

//  bool QOpcUaNodeCreationAttributes::hasDescription() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14hasDescriptionEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasDescription();
}

//  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::displayName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK28QOpcUaNodeCreationAttributes11displayNameEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QOpcUaLocalizedText(self->displayName());
}

//  void QOpcUaNodeCreationAttributes::setDisplayName(const
//      QOpcUaLocalizedText &displayName)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes14setDisplayNameERK19QOpcUaLocalizedText(
    QOpcUaNodeCreationAttributes *self,
    const QOpcUaLocalizedText *displayName) {
  self->setDisplayName(*displayName);
}

//  bool QOpcUaNodeCreationAttributes::hasDisplayName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14hasDisplayNameEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasDisplayName();
}

//  QOpcUa::EventNotifier QOpcUaNodeCreationAttributes::eventNotifier() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QOpcUaNodeCreationAttributes13eventNotifierEv(
    const QOpcUaNodeCreationAttributes *self) {
  return static_cast<int>(self->eventNotifier().toInt());
}

//  void QOpcUaNodeCreationAttributes::setEventNotifier(QOpcUa::EventNotifier
//      eventNotifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes16setEventNotifierE6QFlagsIN6QOpcUa16EventNotifierBitEE(
    QOpcUaNodeCreationAttributes *self,
    int eventNotifier) {
  self->setEventNotifier(
      QFlags<QOpcUa::EventNotifierBit>::fromInt(eventNotifier));
}

//  bool QOpcUaNodeCreationAttributes::hasEventNotifier() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes16hasEventNotifierEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasEventNotifier();
}

//  bool QOpcUaNodeCreationAttributes::executable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes10executableEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->executable();
}

//  void QOpcUaNodeCreationAttributes::setExecutable(bool executable)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes13setExecutableEb(
    QOpcUaNodeCreationAttributes *self,
    bool executable) {
  self->setExecutable(executable);
}

//  bool QOpcUaNodeCreationAttributes::hasExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes13hasExecutableEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasExecutable();
}

//  bool QOpcUaNodeCreationAttributes::historizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes11historizingEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->historizing();
}

//  void QOpcUaNodeCreationAttributes::setHistorizing(bool historizing)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes14setHistorizingEb(
    QOpcUaNodeCreationAttributes *self,
    bool historizing) {
  self->setHistorizing(historizing);
}

//  bool QOpcUaNodeCreationAttributes::hasHistorizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14hasHistorizingEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasHistorizing();
}

//  QOpcUaLocalizedText QOpcUaNodeCreationAttributes::inverseName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK28QOpcUaNodeCreationAttributes11inverseNameEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QOpcUaLocalizedText(self->inverseName());
}

//  void QOpcUaNodeCreationAttributes::setInverseName(const
//      QOpcUaLocalizedText &inverseName)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes14setInverseNameERK19QOpcUaLocalizedText(
    QOpcUaNodeCreationAttributes *self,
    const QOpcUaLocalizedText *inverseName) {
  self->setInverseName(*inverseName);
}

//  bool QOpcUaNodeCreationAttributes::hasInverseName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14hasInverseNameEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasInverseName();
}

//  bool QOpcUaNodeCreationAttributes::isAbstract() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes10isAbstractEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->isAbstract();
}

//  void QOpcUaNodeCreationAttributes::setIsAbstract(bool isAbstract)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes13setIsAbstractEb(
    QOpcUaNodeCreationAttributes *self,
    bool isAbstract) {
  self->setIsAbstract(isAbstract);
}

//  bool QOpcUaNodeCreationAttributes::hasIsAbstract() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes13hasIsAbstractEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasIsAbstract();
}

//  double QOpcUaNodeCreationAttributes::minimumSamplingInterval() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK28QOpcUaNodeCreationAttributes23minimumSamplingIntervalEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->minimumSamplingInterval();
}

//  void QOpcUaNodeCreationAttributes::setMinimumSamplingInterval(double
//      minimumSamplingInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes26setMinimumSamplingIntervalEd(
    QOpcUaNodeCreationAttributes *self,
    double minimumSamplingInterval) {
  self->setMinimumSamplingInterval(minimumSamplingInterval);
}

//  bool QOpcUaNodeCreationAttributes::hasMinimumSamplingInterval() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes26hasMinimumSamplingIntervalEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasMinimumSamplingInterval();
}

//  bool QOpcUaNodeCreationAttributes::symmetric() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes9symmetricEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->symmetric();
}

//  void QOpcUaNodeCreationAttributes::setSymmetric(bool symmetric)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes12setSymmetricEb(
    QOpcUaNodeCreationAttributes *self,
    bool symmetric) {
  self->setSymmetric(symmetric);
}

//  bool QOpcUaNodeCreationAttributes::hasSymmetric() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes12hasSymmetricEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasSymmetric();
}

//  QOpcUa::AccessLevel QOpcUaNodeCreationAttributes::userAccessLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QOpcUaNodeCreationAttributes15userAccessLevelEv(
    const QOpcUaNodeCreationAttributes *self) {
  return static_cast<int>(self->userAccessLevel().toInt());
}

//  void QOpcUaNodeCreationAttributes::setUserAccessLevel(QOpcUa::AccessLevel
//      userAccessLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes18setUserAccessLevelE6QFlagsIN6QOpcUa14AccessLevelBitEE(
    QOpcUaNodeCreationAttributes *self,
    int userAccessLevel) {
  self->setUserAccessLevel(
      QFlags<QOpcUa::AccessLevelBit>::fromInt(userAccessLevel));
}

//  bool QOpcUaNodeCreationAttributes::hasUserAccessLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes18hasUserAccessLevelEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasUserAccessLevel();
}

//  bool QOpcUaNodeCreationAttributes::userExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes14userExecutableEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->userExecutable();
}

//  void QOpcUaNodeCreationAttributes::setUserExecutable(bool userExecutable)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes17setUserExecutableEb(
    QOpcUaNodeCreationAttributes *self,
    bool userExecutable) {
  self->setUserExecutable(userExecutable);
}

//  bool QOpcUaNodeCreationAttributes::hasUserExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes17hasUserExecutableEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasUserExecutable();
}

//  QOpcUa::WriteMask QOpcUaNodeCreationAttributes::userWriteMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QOpcUaNodeCreationAttributes13userWriteMaskEv(
    const QOpcUaNodeCreationAttributes *self) {
  return static_cast<int>(self->userWriteMask().toInt());
}

//  void QOpcUaNodeCreationAttributes::setUserWriteMask(QOpcUa::WriteMask
//      userWriteMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes16setUserWriteMaskE6QFlagsIN6QOpcUa12WriteMaskBitEE(
    QOpcUaNodeCreationAttributes *self,
    int userWriteMask) {
  self->setUserWriteMask(
      QFlags<QOpcUa::WriteMaskBit>::fromInt(userWriteMask));
}

//  bool QOpcUaNodeCreationAttributes::hasUserWriteMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes16hasUserWriteMaskEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasUserWriteMask();
}

//  qint32 QOpcUaNodeCreationAttributes::valueRank() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK28QOpcUaNodeCreationAttributes9valueRankEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->valueRank();
}

//  void QOpcUaNodeCreationAttributes::setValueRank(qint32 valueRank)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes12setValueRankEi(
    QOpcUaNodeCreationAttributes *self,
    qint32 valueRank) {
  self->setValueRank(valueRank);
}

//  bool QOpcUaNodeCreationAttributes::hasValueRank() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes12hasValueRankEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasValueRank();
}

//  QOpcUa::WriteMask QOpcUaNodeCreationAttributes::writeMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QOpcUaNodeCreationAttributes9writeMaskEv(
    const QOpcUaNodeCreationAttributes *self) {
  return static_cast<int>(self->writeMask().toInt());
}

//  void QOpcUaNodeCreationAttributes::setWriteMask(QOpcUa::WriteMask
//      writeMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes12setWriteMaskE6QFlagsIN6QOpcUa12WriteMaskBitEE(
    QOpcUaNodeCreationAttributes *self,
    int writeMask) {
  self->setWriteMask(QFlags<QOpcUa::WriteMaskBit>::fromInt(writeMask));
}

//  bool QOpcUaNodeCreationAttributes::hasWriteMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes12hasWriteMaskEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasWriteMask();
}

//  QVariant QOpcUaNodeCreationAttributes::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QOpcUaNodeCreationAttributes5valueEv(
    const QOpcUaNodeCreationAttributes *self) {
  return new QVariant(self->value());
}

//  void QOpcUaNodeCreationAttributes::setValue(const QVariant &value,
//      QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaNodeCreationAttributes8setValueERK8QVariantN6QOpcUa5TypesE(
    QOpcUaNodeCreationAttributes *self,
    const QVariant *value,
    QOpcUa::Types type) {
  self->setValue(*value, type);
}

//  bool QOpcUaNodeCreationAttributes::hasValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaNodeCreationAttributes8hasValueEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->hasValue();
}

//  QOpcUa::Types QOpcUaNodeCreationAttributes::valueType() const
extern "C" Q_DECL_EXPORT
QOpcUa::Types ritual_ZNK28QOpcUaNodeCreationAttributes9valueTypeEv(
    const QOpcUaNodeCreationAttributes *self) {
  return self->valueType();
}

//  a QList<quint32> a ritual of QOpcUaNodeCreationAttributes gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaNodeCreationAttributes__QList_quint32(
    QList<quint32> *self) {
  delete self;
}
