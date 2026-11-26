//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsondocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qdebug.h>
#include <QtCore/qcborvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <QtCore/qdebug.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qcborarray.h>
#include <QtCore/private/qjsonparser_p.h>
#include <QtCore/private/qjson_p.h>
#include <QtCore/qdatastream.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qjsondocument.cpp, line 52, as local:qjsondocument.cpp:QJsonDocumentPrivate
class QJsonDocumentPrivate
{
    Q_DISABLE_COPY_MOVE(QJsonDocumentPrivate);
public:
    QJsonDocumentPrivate() = default;
    QJsonDocumentPrivate(QCborValue data) : value(std::move(data)) {}

    QCborValue value;
};

//  from src/corelib/serialization/qjsondocument.cpp, line 110, as _ZN13QJsonDocumentC1E10QCborValue
inline QJsonDocument::QJsonDocument(QCborValue data)
    : d(new QJsonDocumentPrivate(std::move(data)))
{
}
//  -----------------------------------------------------------------------

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

//  QJsonDocument::QJsonDocument(QJsonObject &&object)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1EO11QJsonObject(
    QJsonObject *object) {
  return new QJsonDocument(std::move(*object));
}

//  QJsonDocument::QJsonDocument(const QJsonArray &array)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1ERK10QJsonArray(
    const QJsonArray *array) {
  return new QJsonDocument(*array);
}

//  QJsonDocument::QJsonDocument(QJsonArray &&array)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1EO10QJsonArray(QJsonArray *array) {
  return new QJsonDocument(std::move(*array));
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

//  QJsonDocument &QJsonDocument::operator=(const QJsonDocument &other)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentaSERKS_(
    QJsonDocument *self,
    const QJsonDocument *other) {
  return &(self->operator=(*other));
}

//  QJsonDocument::QJsonDocument(QJsonDocument &&other)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1EOS_(QJsonDocument *other) {
  return new QJsonDocument(std::move(*other));
}

//  QJsonDocument &QJsonDocument::operator=(QJsonDocument &&other)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentaSEOS_(
    QJsonDocument *self,
    QJsonDocument *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QJsonDocument::swap(QJsonDocument &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonDocument4swapERS_(
    QJsonDocument *self,
    QJsonDocument *other) {
  self->swap(*other);
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

//  QDebug operator<<(QDebug a0, const QJsonDocument &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK13QJsonDocument(
    const QDebug *a0,
    const QJsonDocument *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  bool operator==(const QJsonDocument &lhs, const QJsonDocument &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QJsonDocumentS1_(
    const QJsonDocument *lhs,
    const QJsonDocument *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonDocument &lhs, const QJsonDocument &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QJsonDocumentS1_(
    const QJsonDocument *lhs,
    const QJsonDocument *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QJsonDocument::QJsonDocument(QCborValue data)
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN13QJsonDocumentC1E10QCborValue(
    const QCborValue *data) {
  return new QJsonDocument(*data);
}
