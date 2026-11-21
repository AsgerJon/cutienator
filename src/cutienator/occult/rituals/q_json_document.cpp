//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsondocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>

//  QJsonDocument::QJsonDocument()
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1Ev() {
  return new QJsonDocument();
}

//  QJsonDocument::QJsonDocument(const QJsonObject &object)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1ERK11QJsonObject(
    const QJsonObject *object) {
  return new QJsonDocument(*object);
}

//  QJsonDocument::QJsonDocument(const QJsonArray &array)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1ERK10QJsonArray(
    const QJsonArray *array) {
  return new QJsonDocument(*array);
}

//  QJsonDocument::~QJsonDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonDocumentD1Ev(QJsonDocument *self) {
  delete self;
}

//  QJsonDocument::QJsonDocument(const QJsonDocument &other)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1ERKS_(const QJsonDocument *other) {
  return new QJsonDocument(*other);
}

//  QJsonDocument QJsonDocument::fromVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocument11fromVariantERK8QVariant(
    const QVariant *variant) {
  return new QJsonDocument(QJsonDocument::fromVariant(*variant));
}

//  QVariant QJsonDocument::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QJsonDocument9toVariantEv(const QJsonDocument *self) {
  return new QVariant(self->toVariant());
}

//  QJsonDocument QJsonDocument::fromJson(const QByteArray &json,
//      QJsonParseError *error)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocument8fromJsonERK10QByteArrayP15QJsonParseError(
    const QByteArray *json,
    QJsonParseError *error) {
  return new QJsonDocument(QJsonDocument::fromJson(*json, error));
}

//  QByteArray QJsonDocument::toJson(JsonFormat format) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QJsonDocument6toJsonENS_10JsonFormatE(
    const QJsonDocument *self,
    QJsonDocument::JsonFormat format) {
  return new QByteArray(self->toJson(format));
}

//  bool QJsonDocument::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonDocument7isEmptyEv(const QJsonDocument *self) {
  return self->isEmpty();
}

//  bool QJsonDocument::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonDocument7isArrayEv(const QJsonDocument *self) {
  return self->isArray();
}

//  bool QJsonDocument::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonDocument8isObjectEv(const QJsonDocument *self) {
  return self->isObject();
}

//  QJsonObject QJsonDocument::object() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QJsonDocument6objectEv(const QJsonDocument *self) {
  return new QJsonObject(self->object());
}

//  QJsonArray QJsonDocument::array() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK13QJsonDocument5arrayEv(const QJsonDocument *self) {
  return new QJsonArray(self->array());
}

//  void QJsonDocument::setObject(const QJsonObject &object)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonDocument9setObjectERK11QJsonObject(
    QJsonDocument *self,
    const QJsonObject *object) {
  self->setObject(*object);
}

//  void QJsonDocument::setArray(const QJsonArray &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonDocument8setArrayERK10QJsonArray(
    QJsonDocument *self,
    const QJsonArray *array) {
  self->setArray(*array);
}

//  const QJsonValue QJsonDocument::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonDocumentixERK7QString(
    const QJsonDocument *self,
    const QString *key) {
  return new QJsonValue(self->operator[](*key));
}

//  const QJsonValue QJsonDocument::operator[](QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonDocumentixE11QStringView(
    const QJsonDocument *self,
    const QString *key) {
  return new QJsonValue(self->operator[](QStringView(*key)));
}

//  const QJsonValue QJsonDocument::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonDocumentixE13QLatin1String(
    const QJsonDocument *self,
    const QLatin1String *key) {
  return new QJsonValue(self->operator[](*key));
}

//  const QJsonValue QJsonDocument::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonDocumentixEx(
    const QJsonDocument *self,
    qsizetype i) {
  return new QJsonValue(self->operator[](i));
}

//  bool QJsonDocument::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonDocument6isNullEv(const QJsonDocument *self) {
  return self->isNull();
}
