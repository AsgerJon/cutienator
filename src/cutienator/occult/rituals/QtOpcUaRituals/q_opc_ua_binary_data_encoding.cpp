//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuabinarydataencoding.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 21. Kept
//  as it is when the generator runs again.
#include <QtOpcUa/qopcuabinarydataencoding.h>
#include <QtCore/qvariant.h>

//  QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QByteArray *buffer)
extern "C" Q_DECL_EXPORT
QOpcUaBinaryDataEncoding *ritual_ZN24QOpcUaBinaryDataEncodingC1EP10QByteArray(
    QByteArray *buffer) {
  return new QOpcUaBinaryDataEncoding(buffer);
}

//  QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QOpcUaExtensionObject
//      &object)
extern "C" Q_DECL_EXPORT
QOpcUaBinaryDataEncoding *ritual_ZN24QOpcUaBinaryDataEncodingC1ER21QOpcUaExtensionObject(
    QOpcUaExtensionObject *object) {
  return new QOpcUaBinaryDataEncoding(*object);
}

//  int QOpcUaBinaryDataEncoding::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpcUaBinaryDataEncoding6offsetEv(
    const QOpcUaBinaryDataEncoding *self) {
  return self->offset();
}

//  void QOpcUaBinaryDataEncoding::setOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncoding9setOffsetEi(
    QOpcUaBinaryDataEncoding *self,
    int offset) {
  self->setOffset(offset);
}

//  void QOpcUaBinaryDataEncoding::truncateBufferToOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncoding22truncateBufferToOffsetEv(
    QOpcUaBinaryDataEncoding *self) {
  self->truncateBufferToOffset();
}

//  bool QOpcUaBinaryDataEncoding::enoughData(int requiredSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding10enoughDataEi(
    QOpcUaBinaryDataEncoding *self,
    int requiredSize) {
  return self->enoughData(requiredSize);
}

//  QOpcUaBinaryDataEncoding::~QOpcUaBinaryDataEncoding()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncodingD1Ev(
    QOpcUaBinaryDataEncoding *self) {
  delete self;
}

//  int QOpcUaBinaryDataEncoding::decode<int>(bool &success)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QOpcUaBinaryDataEncoding6decodeIiLN6QOpcUa5TypesE4294967295EEET_Rb(QOpcUaBinaryDataEncoding *self, bool *success) {
  return self->decode<int>(*success);
}

//  double QOpcUaBinaryDataEncoding::decode<double>(bool &success)
extern "C" Q_DECL_EXPORT
double ritual_ZN24QOpcUaBinaryDataEncoding6decodeIdLN6QOpcUa5TypesE4294967295EEET_Rb(QOpcUaBinaryDataEncoding *self, bool *success) {
  return self->decode<double>(*success);
}

//  bool QOpcUaBinaryDataEncoding::decode<bool>(bool &success)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6decodeIbLN6QOpcUa5TypesE4294967295EEET_Rb(QOpcUaBinaryDataEncoding *self, bool *success) {
  return self->decode<bool>(*success);
}

//  QString QOpcUaBinaryDataEncoding::decode<QString>(bool &success)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QOpcUaBinaryDataEncoding6decodeI7QStringLN6QOpcUa5TypesE4294967295EEET_Rb(QOpcUaBinaryDataEncoding *self, bool *success) {
  return new QString(self->decode<QString>(*success));
}

//  QByteArray QOpcUaBinaryDataEncoding::decode<QByteArray>(bool &success)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QOpcUaBinaryDataEncoding6decodeI10QByteArrayLN6QOpcUa5TypesE4294967295EEET_Rb(QOpcUaBinaryDataEncoding *self, bool *success) {
  return new QByteArray(self->decode<QByteArray>(*success));
}

//  bool QOpcUaBinaryDataEncoding::encode<int>(const int &src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6encodeIiLN6QOpcUa5TypesE4294967295EEEbRKT_(QOpcUaBinaryDataEncoding *self, int src) {
  return self->encode<int>(src);
}

//  bool QOpcUaBinaryDataEncoding::encode<double>(const double &src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6encodeIdLN6QOpcUa5TypesE4294967295EEEbRKT_(QOpcUaBinaryDataEncoding *self, double src) {
  return self->encode<double>(src);
}

//  bool QOpcUaBinaryDataEncoding::encode<bool>(const bool &src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6encodeIbLN6QOpcUa5TypesE4294967295EEEbRKT_(QOpcUaBinaryDataEncoding *self, bool src) {
  return self->encode<bool>(src);
}

//  bool QOpcUaBinaryDataEncoding::encode<QString>(const QString &src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6encodeI7QStringLN6QOpcUa5TypesE4294967295EEEbRKT_(QOpcUaBinaryDataEncoding *self, const QString *src) {
  return self->encode<QString>(*src);
}

//  bool QOpcUaBinaryDataEncoding::encode<QByteArray>(const QByteArray &src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding6encodeI10QByteArrayLN6QOpcUa5TypesE4294967295EEEbRKT_(QOpcUaBinaryDataEncoding *self, const QByteArray *src) {
  return self->encode<QByteArray>(*src);
}

//  QVariant QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar<int>(
//          bool isArray, bool &success)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QOpcUaBinaryDataEncoding24decodeValueArrayOrScalarIiLN6QOpcUa5TypesE4294967295EEE8QVariantbRb(QOpcUaBinaryDataEncoding *self, bool isArray,
    bool *success) {
  return new QVariant(
      self->decodeValueArrayOrScalar<int>(isArray, *success));
}

//  QVariant QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar<double>(
//          bool isArray, bool &success)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QOpcUaBinaryDataEncoding24decodeValueArrayOrScalarIdLN6QOpcUa5TypesE4294967295EEE8QVariantbRb(QOpcUaBinaryDataEncoding *self, bool isArray,
    bool *success) {
  return new QVariant(
      self->decodeValueArrayOrScalar<double>(isArray, *success));
}

//  QVariant QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar<bool>(
//          bool isArray, bool &success)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QOpcUaBinaryDataEncoding24decodeValueArrayOrScalarIbLN6QOpcUa5TypesE4294967295EEE8QVariantbRb(QOpcUaBinaryDataEncoding *self, bool isArray,
    bool *success) {
  return new QVariant(
      self->decodeValueArrayOrScalar<bool>(isArray, *success));
}

//  QVariant QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar<QString>(
//          bool isArray, bool &success)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QOpcUaBinaryDataEncoding24decodeValueArrayOrScalarI7QStringLN6QOpcUa5TypesE4294967295EEE8QVariantbRb(QOpcUaBinaryDataEncoding *self, bool isArray,
    bool *success) {
  return new QVariant(
      self->decodeValueArrayOrScalar<QString>(isArray, *success));
}

//  bool QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar<int>(
//          const QOpcUaVariant &var)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding24encodeValueArrayOrScalarIiLN6QOpcUa5TypesE4294967295EEEbRK13QOpcUaVariant(QOpcUaBinaryDataEncoding *self, const QOpcUaVariant *var) {
  return self->encodeValueArrayOrScalar<int>(*var);
}

//  bool QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar<double>(
//          const QOpcUaVariant &var)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding24encodeValueArrayOrScalarIdLN6QOpcUa5TypesE4294967295EEEbRK13QOpcUaVariant(QOpcUaBinaryDataEncoding *self, const QOpcUaVariant *var) {
  return self->encodeValueArrayOrScalar<double>(*var);
}

//  bool QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar<bool>(
//          const QOpcUaVariant &var)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding24encodeValueArrayOrScalarIbLN6QOpcUa5TypesE4294967295EEEbRK13QOpcUaVariant(QOpcUaBinaryDataEncoding *self, const QOpcUaVariant *var) {
  return self->encodeValueArrayOrScalar<bool>(*var);
}

//  bool QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar<QString>(
//          const QOpcUaVariant &var)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding24encodeValueArrayOrScalarI7QStringLN6QOpcUa5TypesE4294967295EEEbRK13QOpcUaVariant(QOpcUaBinaryDataEncoding *self, const QOpcUaVariant *var) {
  return self->encodeValueArrayOrScalar<QString>(*var);
}

//  int QOpcUaBinaryDataEncoding::upperBound<int>()
extern "C" Q_DECL_EXPORT
int ritual_ZN24QOpcUaBinaryDataEncoding10upperBoundIiEET_v(QOpcUaBinaryDataEncoding *self) {
  return self->upperBound<int>();
}

//  unsigned int QOpcUaBinaryDataEncoding::upperBound<unsigned int>()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN24QOpcUaBinaryDataEncoding10upperBoundIjEET_v(QOpcUaBinaryDataEncoding *self) {
  return self->upperBound<unsigned int>();
}

//  long long QOpcUaBinaryDataEncoding::upperBound<long long>()
extern "C" Q_DECL_EXPORT
long long ritual_ZN24QOpcUaBinaryDataEncoding10upperBoundIxEET_v(QOpcUaBinaryDataEncoding *self) {
  return self->upperBound<long long>();
}
