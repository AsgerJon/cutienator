//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborstreamreader.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborstreamreader.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qcborcommon.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>

//  QCborStreamReader::QCborStreamReader()
extern "C" Q_DECL_EXPORT
QCborStreamReader *ritual_ZN17QCborStreamReaderC1Ev() {
  return new QCborStreamReader();
}

//  QCborStreamReader::QCborStreamReader(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
QCborStreamReader *ritual_ZN17QCborStreamReaderC1EPKcx(
    const char *data,
    qsizetype len) {
  return new QCborStreamReader(data, len);
}

//  QCborStreamReader::QCborStreamReader(const QByteArray &data)
extern "C" Q_DECL_EXPORT
QCborStreamReader *ritual_ZN17QCborStreamReaderC1ERK10QByteArray(
    const QByteArray *data) {
  return new QCborStreamReader(*data);
}

//  QCborStreamReader::QCborStreamReader(QIODevice *device)
extern "C" Q_DECL_EXPORT
QCborStreamReader *ritual_ZN17QCborStreamReaderC1EP9QIODevice(
    QIODevice *device) {
  return new QCborStreamReader(device);
}

//  QCborStreamReader::~QCborStreamReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReaderD1Ev(QCborStreamReader *self) {
  delete self;
}

//  void QCborStreamReader::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader9setDeviceEP9QIODevice(
    QCborStreamReader *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QCborStreamReader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK17QCborStreamReader6deviceEv(
    const QCborStreamReader *self) {
  return self->device();
}

//  void QCborStreamReader::addData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader7addDataERK10QByteArray(
    QCborStreamReader *self,
    const QByteArray *data) {
  self->addData(*data);
}

//  void QCborStreamReader::addData(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader7addDataEPKcx(
    QCborStreamReader *self,
    const char *data,
    qsizetype len) {
  self->addData(data, len);
}

//  void QCborStreamReader::reparse()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader7reparseEv(QCborStreamReader *self) {
  self->reparse();
}

//  void QCborStreamReader::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader5clearEv(QCborStreamReader *self) {
  self->clear();
}

//  void QCborStreamReader::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCborStreamReader5resetEv(QCborStreamReader *self) {
  self->reset();
}

//  QCborError QCborStreamReader::lastError() const
extern "C" Q_DECL_EXPORT
QCborError *ritual_ZNK17QCborStreamReader9lastErrorEv(
    const QCborStreamReader *self) {
  return new QCborError(self->lastError());
}

//  qint64 QCborStreamReader::currentOffset() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QCborStreamReader13currentOffsetEv(
    const QCborStreamReader *self) {
  return self->currentOffset();
}

//  bool QCborStreamReader::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader7isValidEv(const QCborStreamReader *self) {
  return self->isValid();
}

//  int QCborStreamReader::containerDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QCborStreamReader14containerDepthEv(
    const QCborStreamReader *self) {
  return self->containerDepth();
}

//  QCborStreamReader::Type QCborStreamReader::parentContainerType() const
extern "C" Q_DECL_EXPORT
QCborStreamReader::Type ritual_ZNK17QCborStreamReader19parentContainerTypeEv(
    const QCborStreamReader *self) {
  return self->parentContainerType();
}

//  bool QCborStreamReader::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader7hasNextEv(const QCborStreamReader *self) {
  return self->hasNext();
}

//  bool QCborStreamReader::next(int maxRecursion)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCborStreamReader4nextEi(
    QCborStreamReader *self,
    int maxRecursion) {
  return self->next(maxRecursion);
}

//  Type QCborStreamReader::type() const
extern "C" Q_DECL_EXPORT
QCborStreamReader::Type ritual_ZNK17QCborStreamReader4typeEv(
    const QCborStreamReader *self) {
  return self->type();
}

//  bool QCborStreamReader::isUnsignedInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader17isUnsignedIntegerEv(
    const QCborStreamReader *self) {
  return self->isUnsignedInteger();
}

//  bool QCborStreamReader::isNegativeInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader17isNegativeIntegerEv(
    const QCborStreamReader *self) {
  return self->isNegativeInteger();
}

//  bool QCborStreamReader::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader9isIntegerEv(
    const QCborStreamReader *self) {
  return self->isInteger();
}

//  bool QCborStreamReader::isByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader11isByteArrayEv(
    const QCborStreamReader *self) {
  return self->isByteArray();
}

//  bool QCborStreamReader::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader8isStringEv(
    const QCborStreamReader *self) {
  return self->isString();
}

//  bool QCborStreamReader::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader7isArrayEv(const QCborStreamReader *self) {
  return self->isArray();
}

//  bool QCborStreamReader::isMap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader5isMapEv(const QCborStreamReader *self) {
  return self->isMap();
}

//  bool QCborStreamReader::isTag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader5isTagEv(const QCborStreamReader *self) {
  return self->isTag();
}

//  bool QCborStreamReader::isSimpleType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader12isSimpleTypeEv(
    const QCborStreamReader *self) {
  return self->isSimpleType();
}

//  bool QCborStreamReader::isFloat16() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader9isFloat16Ev(
    const QCborStreamReader *self) {
  return self->isFloat16();
}

//  bool QCborStreamReader::isFloat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader7isFloatEv(const QCborStreamReader *self) {
  return self->isFloat();
}

//  bool QCborStreamReader::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader8isDoubleEv(
    const QCborStreamReader *self) {
  return self->isDouble();
}

//  bool QCborStreamReader::isInvalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader9isInvalidEv(
    const QCborStreamReader *self) {
  return self->isInvalid();
}

//  bool QCborStreamReader::isSimpleType(QCborSimpleType st) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader12isSimpleTypeE15QCborSimpleType(
    const QCborStreamReader *self,
    QCborSimpleType st) {
  return self->isSimpleType(st);
}

//  bool QCborStreamReader::isFalse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader7isFalseEv(const QCborStreamReader *self) {
  return self->isFalse();
}

//  bool QCborStreamReader::isTrue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader6isTrueEv(const QCborStreamReader *self) {
  return self->isTrue();
}

//  bool QCborStreamReader::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader6isBoolEv(const QCborStreamReader *self) {
  return self->isBool();
}

//  bool QCborStreamReader::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader6isNullEv(const QCborStreamReader *self) {
  return self->isNull();
}

//  bool QCborStreamReader::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader11isUndefinedEv(
    const QCborStreamReader *self) {
  return self->isUndefined();
}

//  bool QCborStreamReader::isLengthKnown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader13isLengthKnownEv(
    const QCborStreamReader *self) {
  return self->isLengthKnown();
}

//  quint64 QCborStreamReader::length() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QCborStreamReader6lengthEv(
    const QCborStreamReader *self) {
  return self->length();
}

//  bool QCborStreamReader::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader11isContainerEv(
    const QCborStreamReader *self) {
  return self->isContainer();
}

//  bool QCborStreamReader::enterContainer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCborStreamReader14enterContainerEv(
    QCborStreamReader *self) {
  return self->enterContainer();
}

//  bool QCborStreamReader::leaveContainer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QCborStreamReader14leaveContainerEv(
    QCborStreamReader *self) {
  return self->leaveContainer();
}

//  qsizetype QCborStreamReader::currentStringChunkSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QCborStreamReader22currentStringChunkSizeEv(
    const QCborStreamReader *self) {
  return self->currentStringChunkSize();
}

//  bool QCborStreamReader::toBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCborStreamReader6toBoolEv(const QCborStreamReader *self) {
  return self->toBool();
}

//  QCborTag QCborStreamReader::toTag() const
extern "C" Q_DECL_EXPORT
QCborTag ritual_ZNK17QCborStreamReader5toTagEv(
    const QCborStreamReader *self) {
  return self->toTag();
}

//  quint64 QCborStreamReader::toUnsignedInteger() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QCborStreamReader17toUnsignedIntegerEv(
    const QCborStreamReader *self) {
  return self->toUnsignedInteger();
}

//  QCborNegativeInteger QCborStreamReader::toNegativeInteger() const
extern "C" Q_DECL_EXPORT
QCborNegativeInteger ritual_ZNK17QCborStreamReader17toNegativeIntegerEv(
    const QCborStreamReader *self) {
  return self->toNegativeInteger();
}

//  QCborSimpleType QCborStreamReader::toSimpleType() const
extern "C" Q_DECL_EXPORT
QCborSimpleType ritual_ZNK17QCborStreamReader12toSimpleTypeEv(
    const QCborStreamReader *self) {
  return self->toSimpleType();
}

//  qfloat16 QCborStreamReader::toFloat16() const
extern "C" Q_DECL_EXPORT
qfloat16 *ritual_ZNK17QCborStreamReader9toFloat16Ev(
    const QCborStreamReader *self) {
  return new qfloat16(self->toFloat16());
}

//  float QCborStreamReader::toFloat() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QCborStreamReader7toFloatEv(
    const QCborStreamReader *self) {
  return self->toFloat();
}

//  double QCborStreamReader::toDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QCborStreamReader8toDoubleEv(
    const QCborStreamReader *self) {
  return self->toDouble();
}

//  qint64 QCborStreamReader::toInteger() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QCborStreamReader9toIntegerEv(
    const QCborStreamReader *self) {
  return self->toInteger();
}

//  QString QCborStreamReader::readAllString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QCborStreamReader13readAllStringEv(
    QCborStreamReader *self) {
  return new QString(self->readAllString());
}

//  QByteArray QCborStreamReader::readAllUtf8String()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QCborStreamReader17readAllUtf8StringEv(
    QCborStreamReader *self) {
  return new QByteArray(self->readAllUtf8String());
}

//  QByteArray QCborStreamReader::readAllByteArray()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QCborStreamReader16readAllByteArrayEv(
    QCborStreamReader *self) {
  return new QByteArray(self->readAllByteArray());
}
