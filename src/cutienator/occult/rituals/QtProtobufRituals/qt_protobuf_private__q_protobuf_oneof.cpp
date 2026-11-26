//  Written by hand on 2026-11-25 from QtProtobuf/qprotobufoneof.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Not written: 'operator=', the templates ('setValue', 'value', 'message',
//  'isEqual'), and the private pointer of the class,
//  'QProtobufOneofPrivate', which no function names. Also added by hand on
//  2026-11-25, instances of templates of the class: 15.
#include <QtProtobuf/qtprotobufglobal.h>
#include <QtProtobuf/qprotobufoneof.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QtProtobufPrivate::QProtobufOneof::QProtobufOneof()
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufOneof *ritual_ZN17QtProtobufPrivate14QProtobufOneofC1Ev() {
  return new QtProtobufPrivate::QProtobufOneof();
}

//  QtProtobufPrivate::QProtobufOneof::~QProtobufOneof()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneofD1Ev(
    QtProtobufPrivate::QProtobufOneof *self) {
  delete self;
}

//  QtProtobufPrivate::QProtobufOneof::QProtobufOneof(const QProtobufOneof
//      &other)
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufOneof *ritual_ZN17QtProtobufPrivate14QProtobufOneofC1ERKS0_(
    const QtProtobufPrivate::QProtobufOneof *other) {
  return new QtProtobufPrivate::QProtobufOneof(*other);
}

//  QtProtobufPrivate::QProtobufOneof::QProtobufOneof(QProtobufOneof &&other)
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufOneof *ritual_ZN17QtProtobufPrivate14QProtobufOneofC1EOS0_(
    QtProtobufPrivate::QProtobufOneof *other) {
  return new QtProtobufPrivate::QProtobufOneof(std::move(*other));
}

//  void QtProtobufPrivate::QProtobufOneof::swap(QProtobufOneof &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof4swapERS0_(
    QtProtobufPrivate::QProtobufOneof *self,
    QtProtobufPrivate::QProtobufOneof *other) {
  self->swap(*other);
}

//  int QtProtobufPrivate::QProtobufOneof::fieldNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate14QProtobufOneof11fieldNumberEv(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return self->fieldNumber();
}

//  bool QtProtobufPrivate::QProtobufOneof::holdsField(int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof10holdsFieldEi(
    const QtProtobufPrivate::QProtobufOneof *self,
    int fieldNumber) {
  return self->holdsField(fieldNumber);
}

//  void QtProtobufPrivate::QProtobufOneof::ensureMetaType(QMetaType lhs,
//      QMetaType rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof14ensureMetaTypeE9QMetaTypeS1_(
    const QMetaType *lhs,
    const QMetaType *rhs) {
  QtProtobufPrivate::QProtobufOneof::ensureMetaType(*lhs, *rhs);
}

//  void QtProtobufPrivate::QProtobufOneof::ensureRawValue(QMetaType
//      metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof14ensureRawValueE9QMetaType(
    QtProtobufPrivate::QProtobufOneof *self,
    const QMetaType *metaType) {
  self->ensureRawValue(*metaType);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue(const QVariant &value,
//      int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueERK8QVarianti(
    QtProtobufPrivate::QProtobufOneof *self,
    const QVariant *value,
    int fieldNumber) {
  self->setValue(*value, fieldNumber);
}

//  const QVariant &QtProtobufPrivate::QProtobufOneof::rawValue() const
extern "C" Q_DECL_EXPORT
const QVariant *ritual_ZNK17QtProtobufPrivate14QProtobufOneof8rawValueEv(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return &(self->rawValue());
}

//  QVariant &QtProtobufPrivate::QProtobufOneof::rawValue()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QtProtobufPrivate14QProtobufOneof8rawValueEv(
    QtProtobufPrivate::QProtobufOneof *self) {
  return &(self->rawValue());
}

//  bool QtProtobufPrivate::comparesEqual(const QProtobufOneof &lhs, const
//      QProtobufOneof &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtProtobufPrivate13comparesEqualERKNS_14QProtobufOneofES2_(
    const QtProtobufPrivate::QProtobufOneof *lhs,
    const QtProtobufPrivate::QProtobufOneof *rhs) {
  return comparesEqual(*lhs, *rhs);
}

//  bool operator==(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtProtobufPrivateeqERKNS_14QProtobufOneofES2_(
    const QtProtobufPrivate::QProtobufOneof *lhs,
    const QtProtobufPrivate::QProtobufOneof *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtProtobufPrivateneERKNS_14QProtobufOneofES2_(
    const QtProtobufPrivate::QProtobufOneof *lhs,
    const QtProtobufPrivate::QProtobufOneof *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue<int>(const int &value,
//      int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueIiLb1EEEvRKT_i(
    QtProtobufPrivate::QProtobufOneof *self,
    int value,
    int fieldNumber) {
  self->setValue<int>(value, fieldNumber);
}

//  int QtProtobufPrivate::QProtobufOneof::value<int>() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate14QProtobufOneof5valueIiLb1EEET_v(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return self->value<int>();
}

//  bool QtProtobufPrivate::QProtobufOneof::isEqual<int>(const int
//      &otherValue, int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof7isEqualIiLb1EEEbRKT_i(
    const QtProtobufPrivate::QProtobufOneof *self,
    int otherValue,
    int fieldNumber) {
  return self->isEqual<int>(otherValue, fieldNumber);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue<double>(const double
//      &value, int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueIdLb1EEEvRKT_i(
    QtProtobufPrivate::QProtobufOneof *self,
    double value,
    int fieldNumber) {
  self->setValue<double>(value, fieldNumber);
}

//  double QtProtobufPrivate::QProtobufOneof::value<double>() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QtProtobufPrivate14QProtobufOneof5valueIdLb1EEET_v(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return self->value<double>();
}

//  bool QtProtobufPrivate::QProtobufOneof::isEqual<double>(const double
//      &otherValue, int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof7isEqualIdLb1EEEbRKT_i(
    const QtProtobufPrivate::QProtobufOneof *self,
    double otherValue,
    int fieldNumber) {
  return self->isEqual<double>(otherValue, fieldNumber);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue<bool>(const bool &value,
//      int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueIbLb1EEEvRKT_i(
    QtProtobufPrivate::QProtobufOneof *self,
    bool value,
    int fieldNumber) {
  self->setValue<bool>(value, fieldNumber);
}

//  bool QtProtobufPrivate::QProtobufOneof::value<bool>() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof5valueIbLb1EEET_v(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return self->value<bool>();
}

//  bool QtProtobufPrivate::QProtobufOneof::isEqual<bool>(const bool
//      &otherValue, int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof7isEqualIbLb1EEEbRKT_i(
    const QtProtobufPrivate::QProtobufOneof *self,
    bool otherValue,
    int fieldNumber) {
  return self->isEqual<bool>(otherValue, fieldNumber);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue<QString>(const QString
//      &value, int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueI7QStringLb1EEEvRKT_i(
    QtProtobufPrivate::QProtobufOneof *self,
    const QString *value,
    int fieldNumber) {
  self->setValue<QString>(*value, fieldNumber);
}

//  QString QtProtobufPrivate::QProtobufOneof::value<QString>() const
extern "C" Q_DECL_EXPORT
QString * ritual_ZNK17QtProtobufPrivate14QProtobufOneof5valueI7QStringLb1EEET_v(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return new QString(self->value<QString>());
}

//  bool QtProtobufPrivate::QProtobufOneof::isEqual<QString>(const QString
//      &otherValue, int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof7isEqualI7QStringLb1EEEbRKT_i(
    const QtProtobufPrivate::QProtobufOneof *self,
    const QString *otherValue,
    int fieldNumber) {
  return self->isEqual<QString>(*otherValue, fieldNumber);
}

//  void QtProtobufPrivate::QProtobufOneof::setValue<QByteArray>(const
//      QByteArray &value, int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueI10QByteArrayLb1EEEvRKT_i(
    QtProtobufPrivate::QProtobufOneof *self,
    const QByteArray *value,
    int fieldNumber) {
  self->setValue<QByteArray>(*value, fieldNumber);
}

//  QByteArray QtProtobufPrivate::QProtobufOneof::value<QByteArray>() const
extern "C" Q_DECL_EXPORT
QByteArray * ritual_ZNK17QtProtobufPrivate14QProtobufOneof5valueI10QByteArrayLb1EEET_v(
    const QtProtobufPrivate::QProtobufOneof *self) {
  return new QByteArray(self->value<QByteArray>());
}

//  bool QtProtobufPrivate::QProtobufOneof::isEqual<QByteArray>(const
//      QByteArray &otherValue, int fieldNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate14QProtobufOneof7isEqualI10QByteArrayLb1EEEbRKT_i(
    const QtProtobufPrivate::QProtobufOneof *self,
    const QByteArray *otherValue,
    int fieldNumber) {
  return self->isEqual<QByteArray>(*otherValue, fieldNumber);
}
