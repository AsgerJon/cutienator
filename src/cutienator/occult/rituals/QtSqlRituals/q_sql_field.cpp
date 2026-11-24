//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlfield.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlfield.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>

//  QSqlField::QSqlField(const QString &fieldName, QMetaType type, const
//      QString &tableName)
extern "C" Q_DECL_EXPORT
QSqlField *ritual_ZN9QSqlFieldC1ERK7QString9QMetaTypeS2_(
    const QString *fieldName,
    const QMetaType *type,
    const QString *tableName) {
  return new QSqlField(*fieldName, *type, *tableName);
}

//  QSqlField::QSqlField(const QSqlField &other)
extern "C" Q_DECL_EXPORT
QSqlField *ritual_ZN9QSqlFieldC1ERKS_(const QSqlField *other) {
  return new QSqlField(*other);
}

//  QSqlField::~QSqlField()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlFieldD1Ev(QSqlField *self) {
  delete self;
}

//  bool QSqlField::operator==(const QSqlField &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlFieldeqERKS_(
    const QSqlField *self,
    const QSqlField *other) {
  return self->operator==(*other);
}

//  bool QSqlField::operator!=(const QSqlField &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlFieldneERKS_(
    const QSqlField *self,
    const QSqlField *other) {
  return self->operator!=(*other);
}

//  void QSqlField::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField8setValueERK8QVariant(
    QSqlField *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QVariant QSqlField::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlField5valueEv(const QSqlField *self) {
  return new QVariant(self->value());
}

//  void QSqlField::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField7setNameERK7QString(
    QSqlField *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QSqlField::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlField4nameEv(const QSqlField *self) {
  return new QString(self->name());
}

//  void QSqlField::setTableName(const QString &tableName)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField12setTableNameERK7QString(
    QSqlField *self,
    const QString *tableName) {
  self->setTableName(*tableName);
}

//  QString QSqlField::tableName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlField9tableNameEv(const QSqlField *self) {
  return new QString(self->tableName());
}

//  bool QSqlField::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlField6isNullEv(const QSqlField *self) {
  return self->isNull();
}

//  void QSqlField::setReadOnly(bool readOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField11setReadOnlyEb(QSqlField *self, bool readOnly) {
  self->setReadOnly(readOnly);
}

//  bool QSqlField::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlField10isReadOnlyEv(const QSqlField *self) {
  return self->isReadOnly();
}

//  void QSqlField::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField5clearEv(QSqlField *self) {
  self->clear();
}

//  bool QSqlField::isAutoValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlField11isAutoValueEv(const QSqlField *self) {
  return self->isAutoValue();
}

//  QMetaType QSqlField::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK9QSqlField8metaTypeEv(const QSqlField *self) {
  return new QMetaType(self->metaType());
}

//  void QSqlField::setMetaType(QMetaType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField11setMetaTypeE9QMetaType(
    QSqlField *self,
    const QMetaType *type) {
  self->setMetaType(*type);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QSqlField::QSqlField(const QString &fieldName, QVariant::Type type, const
//      QString &tableName)
extern "C" Q_DECL_EXPORT
QSqlField *ritual_ZN9QSqlFieldC1ERK7QStringN8QVariant4TypeES2_(
    const QString *fieldName,
    QVariant::Type type,
    const QString *tableName) {
  return new QSqlField(*fieldName, type, *tableName);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QVariant::Type QSqlField::type() const
extern "C" Q_DECL_EXPORT
QVariant::Type ritual_ZNK9QSqlField4typeEv(const QSqlField *self) {
  return self->type();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QSqlField::setType(QVariant::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField7setTypeEN8QVariant4TypeE(
    QSqlField *self,
    QVariant::Type type) {
  self->setType(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  void QSqlField::setRequiredStatus(RequiredStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField17setRequiredStatusENS_14RequiredStatusE(
    QSqlField *self,
    QSqlField::RequiredStatus status) {
  self->setRequiredStatus(status);
}

//  void QSqlField::setRequired(bool required)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField11setRequiredEb(QSqlField *self, bool required) {
  self->setRequired(required);
}

//  void QSqlField::setLength(int fieldLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField9setLengthEi(QSqlField *self, int fieldLength) {
  self->setLength(fieldLength);
}

//  void QSqlField::setPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField12setPrecisionEi(QSqlField *self, int precision) {
  self->setPrecision(precision);
}

//  void QSqlField::setDefaultValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField15setDefaultValueERK8QVariant(
    QSqlField *self,
    const QVariant *value) {
  self->setDefaultValue(*value);
}

#if QT_DEPRECATED_SINCE(6, 8)
//  void QSqlField::setSqlType(int type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField10setSqlTypeEi(QSqlField *self, int type) {
  self->setSqlType(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  void QSqlField::setGenerated(bool gen)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField12setGeneratedEb(QSqlField *self, bool gen) {
  self->setGenerated(gen);
}

//  void QSqlField::setAutoValue(bool autoVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField12setAutoValueEb(QSqlField *self, bool autoVal) {
  self->setAutoValue(autoVal);
}

//  RequiredStatus QSqlField::requiredStatus() const
extern "C" Q_DECL_EXPORT
QSqlField::RequiredStatus ritual_ZNK9QSqlField14requiredStatusEv(
    const QSqlField *self) {
  return self->requiredStatus();
}

//  int QSqlField::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlField6lengthEv(const QSqlField *self) {
  return self->length();
}

//  int QSqlField::precision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlField9precisionEv(const QSqlField *self) {
  return self->precision();
}

//  QVariant QSqlField::defaultValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlField12defaultValueEv(const QSqlField *self) {
  return new QVariant(self->defaultValue());
}

#if QT_DEPRECATED_SINCE(6, 8)
//  int QSqlField::typeID() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlField6typeIDEv(const QSqlField *self) {
  return self->typeID();
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  bool QSqlField::isGenerated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlField11isGeneratedEv(const QSqlField *self) {
  return self->isGenerated();
}

//  bool QSqlField::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlField7isValidEv(const QSqlField *self) {
  return self->isValid();
}

//  void QSqlField::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlField6detachEv(QSqlField *self) {
  self->detach();
}
