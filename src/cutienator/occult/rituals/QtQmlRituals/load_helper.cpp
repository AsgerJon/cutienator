//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlengine_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlengine_p.h"
#include "qqmlengine.h"
#include <private/qqmlcontext_p.h>
#include <private/qqmlpluginimporter_p.h>
#include <private/qqmlprofiler_p.h>
#include <private/qqmlscriptdata_p.h>
#include <private/qqmlsourcecoordinate_p.h>
#include <private/qqmltype_p.h>
#include <private/qqmltypedata_p.h>
#include <private/qqmlvmemetaobject_p.h>
#include <private/qqmlcomponent_p.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlincubator.h>
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdir.h>
#include <QtCore/qdiriterator.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmutex.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qstorageinfo.h>
#include <QtCore/qthread.h>
#include <QtCore/qtyperevision.h>
#if QT_CONFIG(qml_network)
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#endif
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#  include <shlobj.h>
#  include <QtCore/qlibrary.h>
#endif
#ifdef Q_OS_DARWIN
#  include <unistd.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlengine.cpp, line 1678, as _ZN10LoadHelper16registerCallbackEP20QQmlComponentPrivate
inline void LoadHelper::registerCallback(QQmlComponentPrivate *callback)
{
    m_callback = callback;
}

//  from ../qtdeclarative/src/qml/qml/qqmlengine.cpp, line 1683, as _ZN10LoadHelper18unregisterCallbackEP20QQmlComponentPrivate
inline void LoadHelper::unregisterCallback(QQmlComponentPrivate *callback)
{
    if (m_callback) {
        Q_ASSERT(callback == m_callback);
        m_callback = nullptr;
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlengine.cpp, line 1691, as _ZN10LoadHelper4doneEv
inline void LoadHelper::done()
{
    if (!couldFindModule()) {
        m_resolveTypeResult = ResolveTypeResult::NoSuchModule;
        return;
    }

    QQmlTypeModule *module = QQmlMetaType::typeModule(m_uri, QTypeRevision{});
    if (module) {
        m_type = module->type(m_typeName, {});
        if (m_type.isValid()) {
            m_resolveTypeResult = ResolveTypeResult::ModuleFound;
            return;
        }
    }

    // The module exists (see check above), but there is no QQmlTypeModule
    // ==> pure QML module, attempt resolveType
    QTypeRevision versionReturn;
    QList<QQmlError> errors;
    QQmlImportNamespace *ns_return = nullptr;
    m_importCache->resolveType(
            typeLoader(), m_typeName, &m_type, &versionReturn, &ns_return, &errors);
    m_resolveTypeResult = ResolveTypeResult::ModuleFound;
}

//  from ../qtdeclarative/src/qml/qml/qqmlengine.cpp, line 1717, as _ZN10LoadHelper9completedEv
inline void LoadHelper::completed()
{
    QQmlTypeLoader::Blob::completed();

    if (m_callback) {
        m_callback->completeLoadFromModule(m_uri, m_typeName);
        m_callback = nullptr;
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlengine.cpp, line 1738, as _ZNK10LoadHelper15couldFindModuleEv
inline bool LoadHelper::couldFindModule() const
{
    if (m_uri.isEmpty())
        return false;
    for (const auto &import: std::as_const(m_unresolvedImports))
        if (import->priority == 0) // compare QQmlTypeData::allDependenciesDone
            return false;
    return true;
}
//  -----------------------------------------------------------------------

//  QQmlType LoadHelper::type() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK10LoadHelper4typeEv(const LoadHelper *self) {
  return new QQmlType(self->type());
}

//  QQmlTypeLoader::Mode LoadHelper::mode() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader::Mode ritual_ZNK10LoadHelper4modeEv(const LoadHelper *self) {
  return self->mode();
}

//  ResolveTypeResult LoadHelper::resolveTypeResult() const
extern "C" Q_DECL_EXPORT
LoadHelper::ResolveTypeResult ritual_ZNK10LoadHelper17resolveTypeResultEv(
    const LoadHelper *self) {
  return self->resolveTypeResult();
}

//  void LoadHelper::registerCallback(QQmlComponentPrivate *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN10LoadHelper16registerCallbackEP20QQmlComponentPrivate(
    LoadHelper *self,
    QQmlComponentPrivate *callback) {
  self->registerCallback(callback);
}

//  void LoadHelper::unregisterCallback(QQmlComponentPrivate *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN10LoadHelper18unregisterCallbackEP20QQmlComponentPrivate(
    LoadHelper *self,
    QQmlComponentPrivate *callback) {
  self->unregisterCallback(callback);
}

//  void LoadHelper::done()
extern "C" Q_DECL_EXPORT
void ritual_ZN10LoadHelper4doneEv(LoadHelper *self) {
  self->done();
}

//  void LoadHelper::completed()
extern "C" Q_DECL_EXPORT
void ritual_ZN10LoadHelper9completedEv(LoadHelper *self) {
  self->completed();
}

//  void LoadHelper::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10LoadHelper24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    LoadHelper *self,
    const QQmlPrivate::CachedQmlUnit *a0) {
  self->initializeFromCachedUnit(a0);
}

//  bool LoadHelper::couldFindModule() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10LoadHelper15couldFindModuleEv(const LoadHelper *self) {
  return self->couldFindModule();
}
