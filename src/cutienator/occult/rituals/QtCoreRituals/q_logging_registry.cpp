//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qloggingregistry_p.h"
#include <QtCore/qfile.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qstringtokenizer.h>
#include <QtCore/qdir.h>
#include <QtCore/qcoreapplication.h>
#include <qplatformdefs.h>
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qloggingregistry.cpp, line 392, as _ZN16QLoggingRegistry16registerCategoryEP16QLoggingCategory9QtMsgType
inline void QLoggingRegistry::registerCategory(QLoggingCategory *cat, QtMsgType enableForLevel)
{
    const auto locker = qt_scoped_lock(registryMutex);

    auto r = categories.tryEmplace(cat, enableForLevel);
    if (r.inserted) {
        // new entry
        (*categoryFilter)(cat);
    }
}

//  from src/corelib/io/qloggingregistry.cpp, line 407, as _ZN16QLoggingRegistry18unregisterCategoryEP16QLoggingCategory
inline void QLoggingRegistry::unregisterCategory(QLoggingCategory *cat)
{
    const auto locker = qt_scoped_lock(registryMutex);
    categories.remove(cat);
}

//  from src/corelib/io/qloggingregistry.cpp, line 453, as _ZN16QLoggingRegistry11updateRulesEv
inline void QLoggingRegistry::updateRules()
{
    for (auto it = categories.keyBegin(), end = categories.keyEnd(); it != end; ++it)
        (*categoryFilter)(*it);
}
//  -----------------------------------------------------------------------

//  void QLoggingRegistry::registerCategory(QLoggingCategory *category,
//      QtMsgType enableForLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingRegistry16registerCategoryEP16QLoggingCategory9QtMsgType(
    QLoggingRegistry *self,
    QLoggingCategory *category,
    QtMsgType enableForLevel) {
  self->registerCategory(category, enableForLevel);
}

//  void QLoggingRegistry::unregisterCategory(QLoggingCategory *category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingRegistry18unregisterCategoryEP16QLoggingCategory(
    QLoggingRegistry *self,
    QLoggingCategory *category) {
  self->unregisterCategory(category);
}

//  void QLoggingRegistry::registerEnvironmentOverrideForCategory(const char
//      *categoryName, const char *environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingRegistry38registerEnvironmentOverrideForCategoryEPKcS1_(
    QLoggingRegistry *self,
    const char *categoryName,
    const char *environment) {
  self->registerEnvironmentOverrideForCategory(categoryName, environment);
}

//  QLoggingRegistry *QLoggingRegistry::instance()
extern "C" Q_DECL_EXPORT
QLoggingRegistry *ritual_ZN16QLoggingRegistry8instanceEv() {
  return QLoggingRegistry::instance();
}

//  void QLoggingRegistry::updateRules()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingRegistry11updateRulesEv(QLoggingRegistry *self) {
  self->updateRules();
}
