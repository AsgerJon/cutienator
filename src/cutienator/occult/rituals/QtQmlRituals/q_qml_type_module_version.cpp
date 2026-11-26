//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypemoduleversion_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, instances of templates of the
//  class: 2. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypemoduleversion_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypemoduleversion_p.h>
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypemoduleversion.cpp, line 9, as _ZN21QQmlTypeModuleVersionC1Ev
inline QQmlTypeModuleVersion::QQmlTypeModuleVersion()
    : m_module(nullptr), m_minor(0)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemoduleversion.cpp, line 14, as _ZN21QQmlTypeModuleVersionC1EP14QQmlTypeModule13QTypeRevision
inline QQmlTypeModuleVersion::QQmlTypeModuleVersion(QQmlTypeModule *module, QTypeRevision version)
    : m_module(module), m_minor(version.minorVersion())
{
    Q_ASSERT(m_module);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemoduleversion.cpp, line 20, as _ZN21QQmlTypeModuleVersionC1ERKS_
inline QQmlTypeModuleVersion::QQmlTypeModuleVersion(const QQmlTypeModuleVersion &o)
    : m_module(o.m_module), m_minor(o.m_minor)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemoduleversion.cpp, line 25, as _ZN21QQmlTypeModuleVersionaSERKS_
inline QQmlTypeModuleVersion &QQmlTypeModuleVersion::operator=(const QQmlTypeModuleVersion &o)
{
    m_module = o.m_module;
    m_minor = o.m_minor;
    return *this;
}
//  -----------------------------------------------------------------------

//  QQmlTypeModuleVersion::QQmlTypeModuleVersion()
extern "C" Q_DECL_EXPORT
QQmlTypeModuleVersion *ritual_ZN21QQmlTypeModuleVersionC1Ev() {
  return new QQmlTypeModuleVersion();
}

//  QQmlTypeModuleVersion::QQmlTypeModuleVersion(QQmlTypeModule *a0,
//      QTypeRevision a1)
extern "C" Q_DECL_EXPORT
QQmlTypeModuleVersion *ritual_ZN21QQmlTypeModuleVersionC1EP14QQmlTypeModule13QTypeRevision(
    QQmlTypeModule *a0,
    const QTypeRevision *a1) {
  return new QQmlTypeModuleVersion(a0, *a1);
}

//  QQmlTypeModuleVersion::QQmlTypeModuleVersion(const QQmlTypeModuleVersion
//      &a0)
extern "C" Q_DECL_EXPORT
QQmlTypeModuleVersion *ritual_ZN21QQmlTypeModuleVersionC1ERKS_(
    const QQmlTypeModuleVersion *a0) {
  return new QQmlTypeModuleVersion(*a0);
}

//  QQmlTypeModuleVersion &QQmlTypeModuleVersion::operator=(const
//      QQmlTypeModuleVersion &a0)
extern "C" Q_DECL_EXPORT
QQmlTypeModuleVersion *ritual_ZN21QQmlTypeModuleVersionaSERKS_(
    QQmlTypeModuleVersion *self,
    const QQmlTypeModuleVersion *a0) {
  return &(self->operator=(*a0));
}

//  QQmlTypeModuleVersion::~QQmlTypeModuleVersion()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlTypeModuleVersionD1Ev(QQmlTypeModuleVersion *self) {
  delete self;
}

//  QQmlType QQmlTypeModuleVersion::type<QHashedStringRef>(
//      QHashedStringRef name) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK21QQmlTypeModuleVersion4typeI16QHashedStringRefEE8QQmlTypeT_(
    const QQmlTypeModuleVersion *self,
    const QHashedStringRef *name) {
  return new QQmlType(self->type<QHashedStringRef>(*name));
}

//  QQmlType QQmlTypeModuleVersion::type<const QV4::String *>(
//      const QV4::String *name) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK21QQmlTypeModuleVersion4typeIPKN3QV46StringEEE8QQmlTypeT_(
    const QQmlTypeModuleVersion *self,
    const QV4::String *name) {
  return new QQmlType(self->type<const QV4::String *>(name));
}
