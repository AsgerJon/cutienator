//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertyvalidator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyvalidator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertyvalidator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 657, as _ZNK21QQmlPropertyValidator9canCoerceE9QMetaTypeN17QQmlPropertyCache8ConstPtrE
inline bool QQmlPropertyValidator::canCoerce(QMetaType to, QQmlPropertyCache::ConstPtr fromMo) const
{
    if (QQmlMetaType::canConvert(fromMo, to))
        return true;

    // if we have an inline component from the current file,
    // it is not properly registered at this point, as registration
    // only occurs after the whole file has been validated
    // Therefore we need to check the ICs here
    for (const auto &icDatum : std::as_const(compilationUnit->inlineComponentData)) {
        if (icDatum.qmlType.typeId() != to)
            continue;

        const auto toMo = compilationUnit->propertyCaches.at(icDatum.objectIndex);
        for (QQmlPropertyCache::ConstPtr parent = fromMo; parent; parent = parent->parent()) {
            if (parent == toMo)
                return true;
        }
        return false;
    }

    return false;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 681, as _ZNK21QQmlPropertyValidator11recordErrorERKN3QV412CompiledData8LocationERK7QString
inline QList<QQmlError> QQmlPropertyValidator::recordError(const QV4::CompiledData::Location &location, const QString &description) const
{
    QList<QQmlError> errors;
    errors.append(qQmlCompileError(location, description));
    return errors;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 688, as _ZNK21QQmlPropertyValidator11recordErrorERK9QQmlError
inline QList<QQmlError> QQmlPropertyValidator::recordError(const QQmlError &error) const
{
    QList<QQmlError> errors;
    errors.append(error);
    return errors;
}
//  -----------------------------------------------------------------------

//  QString QQmlPropertyValidator::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlPropertyValidator2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlPropertyValidator::tr(
          sourceText,
          disambiguation,
          n));
}

//  QQmlPropertyCache::ConstPtr QQmlPropertyValidator::rootPropertyCache()
//      const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK21QQmlPropertyValidator17rootPropertyCacheEv(
    const QQmlPropertyValidator *self) {
  return new QQmlPropertyCache::ConstPtr(self->rootPropertyCache());
}

//  QUrl QQmlPropertyValidator::documentSourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQmlPropertyValidator17documentSourceUrlEv(
    const QQmlPropertyValidator *self) {
  return new QUrl(self->documentSourceUrl());
}

//  QQmlTypeLoader *QQmlPropertyValidator::typeLoader() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZNK21QQmlPropertyValidator10typeLoaderEv(
    const QQmlPropertyValidator *self) {
  return self->typeLoader();
}

//  bool QQmlPropertyValidator::canCoerce(QMetaType to,
//      QQmlPropertyCache::ConstPtr fromMo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlPropertyValidator9canCoerceE9QMetaTypeN17QQmlPropertyCache8ConstPtrE(
    const QQmlPropertyValidator *self,
    const QMetaType *to,
    const QQmlPropertyCache::ConstPtr *fromMo) {
  return self->canCoerce(*to, *fromMo);
}

//  QList<QQmlError> QQmlPropertyValidator::recordError(const
//      QV4::CompiledData::Location &location, const QString &description)
//      const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK21QQmlPropertyValidator11recordErrorERKN3QV412CompiledData8LocationERK7QString(
    const QQmlPropertyValidator *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  return new QList<QQmlError>(self->recordError(*location, *description));
}

//  QList<QQmlError> QQmlPropertyValidator::recordError(const QQmlError
//      &error) const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK21QQmlPropertyValidator11recordErrorERK9QQmlError(
    const QQmlPropertyValidator *self,
    const QQmlError *error) {
  return new QList<QQmlError>(self->recordError(*error));
}

//  QString QQmlPropertyValidator::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlPropertyValidator8stringAtEi(
    const QQmlPropertyValidator *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  QV4::ResolvedTypeReference *QQmlPropertyValidator::resolvedType(int id)
//      const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK21QQmlPropertyValidator12resolvedTypeEi(
    const QQmlPropertyValidator *self,
    int id) {
  return self->resolvedType(id);
}

//  QQmlPropertyValidator::~QQmlPropertyValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlPropertyValidatorD1Ev(QQmlPropertyValidator *self) {
  delete self;
}
