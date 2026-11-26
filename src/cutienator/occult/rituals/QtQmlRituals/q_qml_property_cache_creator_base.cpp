//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qurl.h>
#include <optional>
#include <QtCore/QMetaType>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 16, as local:qqmlpropertycachecreator.cpp:processUrlForClassName
inline template<typename BaseNameHandler, typename FailHandler>
auto processUrlForClassName(
    const QUrl &url, BaseNameHandler &&baseNameHandler, FailHandler &&failHandler)
{
    const QString path = url.path();

    // Not a reusable type if we don't have an absolute Url
    const qsizetype lastSlash = path.lastIndexOf(QLatin1Char('/'));
    if (lastSlash <= -1)
        return failHandler();

    // ### this might not be correct for .ui.qml files
    const QStringView baseName = QStringView{path}.mid(lastSlash + 1, path.size() - lastSlash - 5);

    // Not a reusable type if it doesn't start with a upper case letter.
    return (!baseName.isEmpty() && baseName.at(0).isUpper())
        ? baseNameHandler(baseName)
        : failHandler();
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 36, as _ZN28QQmlPropertyCacheCreatorBase27canCreateClassNameTypeByUrlERK4QUrl
inline bool QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(const QUrl &url)
{
    return processUrlForClassName(url, [](QStringView) {
        return true;
    }, []() {
        return false;
    });
}
//  -----------------------------------------------------------------------

//  QString QQmlPropertyCacheCreatorBase::tr(const char *sourceText, const
//      char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQmlPropertyCacheCreatorBase2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlPropertyCacheCreatorBase::tr(
          sourceText,
          disambiguation,
          n));
}

//  std::optional<QMetaType> QQmlPropertyCacheCreatorBase::metaTypeForPropert
//      yType(QV4::CompiledData::CommonType type)
extern "C" Q_DECL_EXPORT
std::optional<QMetaType> *ritual_ZN28QQmlPropertyCacheCreatorBase23metaTypeForPropertyTypeEN3QV412CompiledData10CommonTypeE(
    QV4::CompiledData::CommonType type) {
  return new std::optional<QMetaType>(
      QQmlPropertyCacheCreatorBase::metaTypeForPropertyType(
          type));
}

//  std::optional<QMetaType> QQmlPropertyCacheCreatorBase::listTypeForPropert
//      yType(QV4::CompiledData::CommonType type)
extern "C" Q_DECL_EXPORT
std::optional<QMetaType> *ritual_ZN28QQmlPropertyCacheCreatorBase23listTypeForPropertyTypeEN3QV412CompiledData10CommonTypeE(
    QV4::CompiledData::CommonType type) {
  return new std::optional<QMetaType>(
      QQmlPropertyCacheCreatorBase::listTypeForPropertyType(
          type));
}

//  QV4::CompiledData::CommonType
//      QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(QMetaType
//      metaType)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CommonType ritual_ZN28QQmlPropertyCacheCreatorBase23propertyTypeForMetaTypeE9QMetaType(
    const QMetaType *metaType) {
  return QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(*metaType);
}

//  bool QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QQmlPropertyCacheCreatorBase27canCreateClassNameTypeByUrlERK4QUrl(
    const QUrl *url) {
  return QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(*url);
}

//  QString QQmlPropertyCacheCreatorBase::explain(OverrideSemantics::Status
//      reason)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQmlPropertyCacheCreatorBase7explainEN17OverrideSemantics6StatusE(
    OverrideSemantics::Status reason) {
  return new QString(QQmlPropertyCacheCreatorBase::explain(reason));
}

//  QQmlPropertyCacheCreatorBase::~QQmlPropertyCacheCreatorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlPropertyCacheCreatorBaseD1Ev(
    QQmlPropertyCacheCreatorBase *self) {
  delete self;
}

//  a std::optional<QMetaType> a ritual of QQmlPropertyCacheCreatorBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlPropertyCacheCreatorBase__std_optional_QMetaType(
    std::optional<QMetaType> *self) {
  delete self;
}
