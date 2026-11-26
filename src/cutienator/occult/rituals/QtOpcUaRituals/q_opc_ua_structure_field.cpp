//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuastructurefield.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuastructurefield.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  QOpcUaStructureField::QOpcUaStructureField(qint32 valueRank)
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_ZN20QOpcUaStructureFieldC1Ei(qint32 valueRank) {
  return new QOpcUaStructureField(valueRank);
}

//  QOpcUaStructureField::QOpcUaStructureField(const QOpcUaStructureField
//      &other)
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_ZN20QOpcUaStructureFieldC1ERKS_(
    const QOpcUaStructureField *other) {
  return new QOpcUaStructureField(*other);
}

//  void QOpcUaStructureField::swap(QOpcUaStructureField &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField4swapERS_(
    QOpcUaStructureField *self,
    QOpcUaStructureField *other) {
  self->swap(*other);
}

//  QOpcUaStructureField
//      &QOpcUaStructureField::operator=(QOpcUaStructureField &&other)
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_ZN20QOpcUaStructureFieldaSEOS_(
    QOpcUaStructureField *self,
    QOpcUaStructureField *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpcUaStructureField::QOpcUaStructureField(QOpcUaStructureField &&other)
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_ZN20QOpcUaStructureFieldC1EOS_(
    QOpcUaStructureField *other) {
  return new QOpcUaStructureField(std::move(*other));
}

//  QOpcUaStructureField &QOpcUaStructureField::operator=(const
//      QOpcUaStructureField &other)
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_ZN20QOpcUaStructureFieldaSERKS_(
    QOpcUaStructureField *self,
    const QOpcUaStructureField *other) {
  return &(self->operator=(*other));
}

//  QVariant QOpcUaStructureField::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaStructureFieldcv8QVariantEv(
    const QOpcUaStructureField *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaStructureField::~QOpcUaStructureField()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureFieldD1Ev(QOpcUaStructureField *self) {
  delete self;
}

//  QString QOpcUaStructureField::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpcUaStructureField4nameEv(
    const QOpcUaStructureField *self) {
  return new QString(self->name());
}

//  void QOpcUaStructureField::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField7setNameERK7QString(
    QOpcUaStructureField *self,
    const QString *name) {
  self->setName(*name);
}

//  QOpcUaLocalizedText QOpcUaStructureField::description() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK20QOpcUaStructureField11descriptionEv(
    const QOpcUaStructureField *self) {
  return new QOpcUaLocalizedText(self->description());
}

//  void QOpcUaStructureField::setDescription(const QOpcUaLocalizedText
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField14setDescriptionERK19QOpcUaLocalizedText(
    QOpcUaStructureField *self,
    const QOpcUaLocalizedText *description) {
  self->setDescription(*description);
}

//  QString QOpcUaStructureField::dataType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QOpcUaStructureField8dataTypeEv(
    const QOpcUaStructureField *self) {
  return new QString(self->dataType());
}

//  void QOpcUaStructureField::setDataType(const QString &dataTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField11setDataTypeERK7QString(
    QOpcUaStructureField *self,
    const QString *dataTypeId) {
  self->setDataType(*dataTypeId);
}

//  qint32 QOpcUaStructureField::valueRank() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK20QOpcUaStructureField9valueRankEv(
    const QOpcUaStructureField *self) {
  return self->valueRank();
}

//  void QOpcUaStructureField::setValueRank(qint32 valueRank)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField12setValueRankEi(
    QOpcUaStructureField *self,
    qint32 valueRank) {
  self->setValueRank(valueRank);
}

//  QList<quint32> QOpcUaStructureField::arrayDimensions() const
extern "C" Q_DECL_EXPORT
QList<quint32> *ritual_ZNK20QOpcUaStructureField15arrayDimensionsEv(
    const QOpcUaStructureField *self) {
  return new QList<quint32>(self->arrayDimensions());
}

//  void QOpcUaStructureField::setArrayDimensions(const QList<quint32>
//      &arrayDimensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField18setArrayDimensionsERK5QListIjE(
    QOpcUaStructureField *self,
    const QList<quint32> *arrayDimensions) {
  self->setArrayDimensions(*arrayDimensions);
}

//  quint32 QOpcUaStructureField::maxStringLength() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QOpcUaStructureField15maxStringLengthEv(
    const QOpcUaStructureField *self) {
  return self->maxStringLength();
}

//  void QOpcUaStructureField::setMaxStringLength(quint32 maxStringLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField18setMaxStringLengthEj(
    QOpcUaStructureField *self,
    quint32 maxStringLength) {
  self->setMaxStringLength(maxStringLength);
}

//  bool QOpcUaStructureField::isOptional() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QOpcUaStructureField10isOptionalEv(
    const QOpcUaStructureField *self) {
  return self->isOptional();
}

//  void QOpcUaStructureField::setIsOptional(bool isOptional)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaStructureField13setIsOptionalEb(
    QOpcUaStructureField *self,
    bool isOptional) {
  self->setIsOptional(isOptional);
}

//  bool operator==(const QOpcUaStructureField &lhs, const
//      QOpcUaStructureField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpcUaStructureFieldS1_(
    const QOpcUaStructureField *lhs,
    const QOpcUaStructureField *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaStructureField &lhs, const
//      QOpcUaStructureField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpcUaStructureFieldS1_(
    const QOpcUaStructureField *lhs,
    const QOpcUaStructureField *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaStructureField>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaStructureField> *ritual_list_make_QOpcUaStructureField() {
  return new QList<QOpcUaStructureField>();
}

//  void QList<QOpcUaStructureField>::append(const QOpcUaStructureField
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaStructureField(
    QList<QOpcUaStructureField> *self,
    const QOpcUaStructureField *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaStructureField>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaStructureField(
    const QList<QOpcUaStructureField> *self) {
  return self->size();
}

//  const QOpcUaStructureField &QList<QOpcUaStructureField>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QOpcUaStructureField *ritual_list_at_QOpcUaStructureField(
    const QList<QOpcUaStructureField> *self,
    long long index) {
  return new QOpcUaStructureField(self->at(index));
}

//  QList<QOpcUaStructureField>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaStructureField(
    QList<QOpcUaStructureField> *self) {
  delete self;
}

//  a QList<quint32> a ritual of QOpcUaStructureField gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaStructureField__QList_quint32(QList<quint32> *self) {
  delete self;
}
