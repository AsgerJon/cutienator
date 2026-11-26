//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypemodule_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypemodule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypemodule_p.h>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtCore/qmutex.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypemodule.cpp, line 26, as _ZN14QQmlTypeModule3addEP15QQmlTypePrivate
inline void QQmlTypeModule::add(QQmlTypePrivate *type)
{
    QMutexLocker lock(&m_mutex);

    if (type->version.hasMinorVersion())
        addMinorVersion(type->version.minorVersion());

    QList<QQmlTypePrivate *> &list = m_typeHash[type->elementName];
    for (int ii = 0; ii < list.size(); ++ii) {
        QQmlTypePrivate *in_list = list.at(ii);
        Q_ASSERT(in_list);
        if (in_list->version.minorVersion() < type->version.minorVersion()) {
            list.insert(ii, type);
            return;
        } else if (in_list->version.minorVersion() == type->version.minorVersion()) {
            list[ii] = type;
            return;
        }
    }
    list.append(type);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemodule.cpp, line 48, as _ZN14QQmlTypeModule6removeEPK15QQmlTypePrivate
inline void QQmlTypeModule::remove(const QQmlTypePrivate *type)
{
    QMutexLocker lock(&m_mutex);
    for (auto elementIt = m_typeHash.begin(); elementIt != m_typeHash.end(); ++elementIt)
        QQmlMetaType::removeQQmlTypePrivate(elementIt.value(), type);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemodule.cpp, line 13, as _ZN14QQmlTypeModule15addMinorVersionEh
inline void QQmlTypeModule::addMinorVersion(quint8 version)
{
    for (int oldVersion = m_minMinorVersion.loadRelaxed();
         oldVersion > version && !m_minMinorVersion.testAndSetOrdered(oldVersion, version);
         oldVersion = m_minMinorVersion.loadRelaxed()) {
    }

    for (int oldVersion = m_maxMinorVersion.loadRelaxed();
         oldVersion < version && !m_maxMinorVersion.testAndSetOrdered(oldVersion, version);
         oldVersion = m_maxMinorVersion.loadRelaxed()) {
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmltypemodule.cpp, line 66, as _ZNK14QQmlTypeModule23walkCompositeSingletonsERKSt8functionIFvRK8QQmlTypeEE
inline void QQmlTypeModule::walkCompositeSingletons(const std::function<void(const QQmlType &)> &callback) const
{
    QMutexLocker lock(&m_mutex);
    for (auto typeCandidates = m_typeHash.begin(), end = m_typeHash.end();
         typeCandidates != end; ++typeCandidates) {
        for (auto type: typeCandidates.value()) {
            if (type->regType == QQmlType::CompositeSingletonType)
                callback(QQmlType(type));
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlTypeModule::QQmlTypeModule()
extern "C" Q_DECL_EXPORT
QQmlTypeModule *ritual_ZN14QQmlTypeModuleC1Ev() {
  return new QQmlTypeModule();
}

//  QQmlTypeModule::QQmlTypeModule(const QString &uri, quint8 majorVersion)
extern "C" Q_DECL_EXPORT
QQmlTypeModule *ritual_ZN14QQmlTypeModuleC1ERK7QStringh(
    const QString *uri,
    quint8 majorVersion) {
  return new QQmlTypeModule(*uri, majorVersion);
}

//  void QQmlTypeModule::add(QQmlTypePrivate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeModule3addEP15QQmlTypePrivate(
    QQmlTypeModule *self,
    QQmlTypePrivate *a0) {
  self->add(a0);
}

//  void QQmlTypeModule::remove(const QQmlTypePrivate *type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeModule6removeEPK15QQmlTypePrivate(
    QQmlTypeModule *self,
    const QQmlTypePrivate *type) {
  self->remove(type);
}

//  LockLevel QQmlTypeModule::lockLevel() const
extern "C" Q_DECL_EXPORT
QQmlTypeModule::LockLevel ritual_ZNK14QQmlTypeModule9lockLevelEv(
    const QQmlTypeModule *self) {
  return self->lockLevel();
}

//  bool QQmlTypeModule::setLockLevel(LockLevel mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlTypeModule12setLockLevelENS_9LockLevelE(
    QQmlTypeModule *self,
    QQmlTypeModule::LockLevel mode) {
  return self->setLockLevel(mode);
}

//  QString QQmlTypeModule::module() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlTypeModule6moduleEv(const QQmlTypeModule *self) {
  return new QString(self->module());
}

//  quint8 QQmlTypeModule::majorVersion() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK14QQmlTypeModule12majorVersionEv(
    const QQmlTypeModule *self) {
  return self->majorVersion();
}

//  void QQmlTypeModule::addMinorVersion(quint8 minorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeModule15addMinorVersionEh(
    QQmlTypeModule *self,
    quint8 minorVersion) {
  self->addMinorVersion(minorVersion);
}

//  quint8 QQmlTypeModule::minimumMinorVersion() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK14QQmlTypeModule19minimumMinorVersionEv(
    const QQmlTypeModule *self) {
  return self->minimumMinorVersion();
}

//  quint8 QQmlTypeModule::maximumMinorVersion() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK14QQmlTypeModule19maximumMinorVersionEv(
    const QQmlTypeModule *self) {
  return self->maximumMinorVersion();
}

//  QQmlType QQmlTypeModule::type(const QHashedStringRef &name, QTypeRevision
//      version) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK14QQmlTypeModule4typeERK16QHashedStringRef13QTypeRevision(
    const QQmlTypeModule *self,
    const QHashedStringRef *name,
    const QTypeRevision *version) {
  return new QQmlType(self->type(*name, *version));
}

//  QQmlType QQmlTypeModule::type(const QV4::String *name, QTypeRevision
//      version) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK14QQmlTypeModule4typeEPKN3QV46StringE13QTypeRevision(
    const QQmlTypeModule *self,
    const QV4::String *name,
    const QTypeRevision *version) {
  return new QQmlType(self->type(name, *version));
}

//  void QQmlTypeModule::walkCompositeSingletons(const std::function<void
//      (const QQmlType &)> &callback) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQmlTypeModule23walkCompositeSingletonsERKSt8functionIFvRK8QQmlTypeEE(
    const QQmlTypeModule *self,
    const std::function<void (const QQmlType &)> *callback) {
  self->walkCompositeSingletons(*callback);
}

//  QQmlType QQmlTypeModule::findType(const QList<QQmlTypePrivate *> *types,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN14QQmlTypeModule8findTypeEPK5QListIP15QQmlTypePrivateE13QTypeRevision(
    const QList<QQmlTypePrivate *> *types,
    const QTypeRevision *version) {
  return new QQmlType(QQmlTypeModule::findType(types, *version));
}
