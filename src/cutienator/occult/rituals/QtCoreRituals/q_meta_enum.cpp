//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaobject.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qbytearray.h>
#include <optional>
#include <QtCore/qnamespace.h>

//  QMetaEnum::QMetaEnum()
extern "C" Q_DECL_EXPORT
QMetaEnum *ritual_ZN9QMetaEnumC1Ev() {
  return new QMetaEnum();
}

//  const char *QMetaEnum::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaEnum4nameEv(const QMetaEnum *self) {
  return self->name();
}

//  const char *QMetaEnum::enumName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaEnum8enumNameEv(const QMetaEnum *self) {
  return self->enumName();
}

//  QMetaType QMetaEnum::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK9QMetaEnum8metaTypeEv(const QMetaEnum *self) {
  return new QMetaType(self->metaType());
}

//  bool QMetaEnum::isFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaEnum6isFlagEv(const QMetaEnum *self) {
  return self->isFlag();
}

//  bool QMetaEnum::isScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaEnum8isScopedEv(const QMetaEnum *self) {
  return self->isScoped();
}

//  bool QMetaEnum::is64Bit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaEnum7is64BitEv(const QMetaEnum *self) {
  return self->is64Bit();
}

//  int QMetaEnum::keyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaEnum8keyCountEv(const QMetaEnum *self) {
  return self->keyCount();
}

//  const char *QMetaEnum::key(int index) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaEnum3keyEi(const QMetaEnum *self, int index) {
  return self->key(index);
}

//  int QMetaEnum::value(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaEnum5valueEi(const QMetaEnum *self, int index) {
  return self->value(index);
}

//  std::optional<quint64> QMetaEnum::value64(int index) const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK9QMetaEnum7value64Ei(
    const QMetaEnum *self,
    int index) {
  return new std::optional<quint64>(self->value64(index));
}

//  const char *QMetaEnum::scope() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaEnum5scopeEv(const QMetaEnum *self) {
  return self->scope();
}

//  int QMetaEnum::keyToValue(const char *key, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaEnum10keyToValueEPKcPb(
    const QMetaEnum *self,
    const char *key,
    bool *ok) {
  return self->keyToValue(key, ok);
}

//  int QMetaEnum::keysToValue(const char *keys, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaEnum11keysToValueEPKcPb(
    const QMetaEnum *self,
    const char *keys,
    bool *ok) {
  return self->keysToValue(keys, ok);
}

//  std::optional<quint64> QMetaEnum::keyToValue64(const char *key) const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK9QMetaEnum12keyToValue64EPKc(
    const QMetaEnum *self,
    const char *key) {
  return new std::optional<quint64>(self->keyToValue64(key));
}

//  std::optional<quint64> QMetaEnum::keysToValue64(const char *keys) const
extern "C" Q_DECL_EXPORT
std::optional<quint64> *ritual_ZNK9QMetaEnum13keysToValue64EPKc(
    const QMetaEnum *self,
    const char *keys) {
  return new std::optional<quint64>(self->keysToValue64(keys));
}

//  const char *QMetaEnum::valueToKey(quint64 value) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaEnum10valueToKeyEy(
    const QMetaEnum *self,
    quint64 value) {
  return self->valueToKey(value);
}

//  QByteArray QMetaEnum::valueToKeys(quint64 value) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QMetaEnum11valueToKeysEy(
    const QMetaEnum *self,
    quint64 value) {
  return new QByteArray(self->valueToKeys(value));
}

//  const QMetaObject *QMetaEnum::enclosingMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QMetaEnum19enclosingMetaObjectEv(
    const QMetaEnum *self) {
  return self->enclosingMetaObject();
}

//  bool QMetaEnum::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaEnum7isValidEv(const QMetaEnum *self) {
  return self->isValid();
}

//  QMetaEnum::QMetaEnum(const QMetaObject *mobj, int index)
extern "C" Q_DECL_EXPORT
QMetaEnum *ritual_ZN9QMetaEnumC1EPK11QMetaObjecti(
    const QMetaObject *mobj,
    int index) {
  return new QMetaEnum(mobj, index);
}

//  QMetaEnum::~QMetaEnum()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaEnumD1Ev(QMetaEnum *self) {
  delete self;
}

//  a std::optional<quint64> a ritual of QMetaEnum gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMetaEnum__std_optional_quint64(
    std::optional<quint64> *self) {
  delete self;
}

//  static QMetaEnum QMetaEnum::fromType<Qt::Orientation>()
extern "C" Q_DECL_EXPORT
QMetaEnum * ritual_ZN9QMetaEnum8fromTypeIN2Qt11OrientationEEES_v() {
  return new QMetaEnum(QMetaEnum::fromType<Qt::Orientation>());
}

//  static QMetaEnum QMetaEnum::fromType<Qt::DayOfWeek>()
extern "C" Q_DECL_EXPORT
QMetaEnum * ritual_ZN9QMetaEnum8fromTypeIN2Qt9DayOfWeekEEES_v() {
  return new QMetaEnum(QMetaEnum::fromType<Qt::DayOfWeek>());
}

//  static QMetaEnum QMetaEnum::fromType<Qt::CheckState>()
extern "C" Q_DECL_EXPORT
QMetaEnum * ritual_ZN9QMetaEnum8fromTypeIN2Qt10CheckStateEEES_v() {
  return new QMetaEnum(QMetaEnum::fromType<Qt::CheckState>());
}

//  static QMetaEnum QMetaEnum::fromType<Qt::CaseSensitivity>()
extern "C" Q_DECL_EXPORT
QMetaEnum * ritual_ZN9QMetaEnum8fromTypeIN2Qt15CaseSensitivityEEES_v() {
  return new QMetaEnum(QMetaEnum::fromType<Qt::CaseSensitivity>());
}

//  static QMetaEnum QMetaEnum::fromType<Qt::ConnectionType>()
extern "C" Q_DECL_EXPORT
QMetaEnum * ritual_ZN9QMetaEnum8fromTypeIN2Qt14ConnectionTypeEEES_v() {
  return new QMetaEnum(QMetaEnum::fromType<Qt::ConnectionType>());
}
