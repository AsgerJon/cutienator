//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qloggingregistry_p.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qloggingregistry.cpp, line 24, as local:qloggingregistry.cpp:debugMsg
#define debugMsg QMessageLogger(QT_MESSAGELOG_FILE, QT_MESSAGELOG_LINE, QT_MESSAGELOG_FUNC, "qt.core.logging").debug

//  from src/corelib/io/qloggingregistry.cpp, line 26, as local:qloggingregistry.cpp:registryMsg
#define registryMsg QMessageLogger(QT_MESSAGELOG_FILE, QT_MESSAGELOG_LINE, QT_MESSAGELOG_FUNC, "_logging_categories").debug

//  from src/corelib/io/qloggingregistry.cpp, line 282, as local:qloggingregistry.cpp:qtLoggingDebug
static bool qtLoggingDebug()
{
    static const bool debugEnv = [] {
        bool debug = qEnvironmentVariableIsSet("QT_LOGGING_DEBUG");
        if (debug)
            debugMsg("QT_LOGGING_DEBUG environment variable is set.");
        return debug;
    }();
    return Q_UNLIKELY(debugEnv);
}

//  from src/corelib/io/qloggingregistry.cpp, line 57, as _ZNK12QLoggingRule4passE13QLatin1String9QtMsgType
inline int QLoggingRule::pass(QLatin1StringView cat, QtMsgType msgType) const
{
    // check message type
    if (messageType > -1 && messageType != msgType)
        return 0;

    if (flags == FullText) {
        // full match
        if (category == cat)
            return (enabled ? 1 : -1);
        else
            return 0;
    }

    const qsizetype idx = cat.indexOf(category);
    if (idx >= 0) {
        if (flags == MidFilter) {
            // matches somewhere
            return (enabled ? 1 : -1);
        } else if (flags == LeftFilter) {
            // matches left
            if (idx == 0)
                return (enabled ? 1 : -1);
        } else if (flags == RightFilter) {
            // matches right
            if (idx == (cat.size() - category.size()))
                return (enabled ? 1 : -1);
        }
    }
    return 0;
}

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

//  from src/corelib/io/qloggingregistry.cpp, line 463, as _ZN16QLoggingRegistry13installFilterEPFvP16QLoggingCategoryE
inline QLoggingCategory::CategoryFilter
QLoggingRegistry::installFilter(QLoggingCategory::CategoryFilter filter)
{
    const auto locker = qt_scoped_lock(registryMutex);

    if (!filter)
        filter = defaultCategoryFilter;

    QLoggingCategory::CategoryFilter old = categoryFilter;
    categoryFilter = filter;

    updateRules();

    return old;
}

//  from src/corelib/io/qloggingregistry.cpp, line 453, as _ZN16QLoggingRegistry11updateRulesEv
inline void QLoggingRegistry::updateRules()
{
    for (auto it = categories.keyBegin(), end = categories.keyEnd(); it != end; ++it)
        (*categoryFilter)(*it);
}

//  from src/corelib/io/qloggingregistry.cpp, line 506, as _ZN16QLoggingRegistry21defaultCategoryFilterEP16QLoggingCategory
inline void QLoggingRegistry::defaultCategoryFilter(QLoggingCategory *cat)
{
    const QLoggingRegistry *reg = self;
    Q_ASSERT(reg->categories.contains(cat));
    QtMsgType enableForLevel = reg->categories.value(cat);

    // NB: note that the numeric values of the Qt*Msg constants are
    //     not in severity order.
    bool debug = (enableForLevel == QtDebugMsg);
    bool info = debug || (enableForLevel == QtInfoMsg);
    bool warning = info || (enableForLevel == QtWarningMsg);
    bool critical = warning || (enableForLevel == QtCriticalMsg);

    // hard-wired implementation of
    //   qt.*.debug=false
    //   qt.debug=false
    if (const char *categoryName = cat->categoryName()) {
        // == "qt" or startsWith("qt.")
        if (strcmp(categoryName, "qt") == 0) {
            debug = false;
        } else if (strncmp(categoryName, "qt.", 3) == 0) {
            // may be overridden
            auto it = reg->qtCategoryEnvironmentOverrides.find(categoryName);
            if (it == reg->qtCategoryEnvironmentOverrides.end())
                debug = false;
            else
                debug = qEnvironmentVariableIntValue(it->second);
        }
    }

    const auto categoryName = QLatin1StringView(cat->categoryName());

    for (const auto &ruleSet : reg->ruleSets) {
        for (const auto &rule : ruleSet) {
            int filterpass = rule.pass(categoryName, QtDebugMsg);
            if (filterpass != 0)
                debug = (filterpass > 0);
            filterpass = rule.pass(categoryName, QtInfoMsg);
            if (filterpass != 0)
                info = (filterpass > 0);
            filterpass = rule.pass(categoryName, QtWarningMsg);
            if (filterpass != 0)
                warning = (filterpass > 0);
            filterpass = rule.pass(categoryName, QtCriticalMsg);
            if (filterpass != 0)
                critical = (filterpass > 0);
        }
    }

    cat->setEnabled(QtDebugMsg, debug);
    cat->setEnabled(QtInfoMsg, info);
    cat->setEnabled(QtWarningMsg, warning);
    cat->setEnabled(QtCriticalMsg, critical);

    for (const auto &ruleSet : reg->ruleSets) {
        for (const auto &rule : ruleSet) {
            // this must be an exact match
            if (rule.messageType != QtDebugMsg && rule.flags != QLoggingRule::FullText)
                continue;
            if (rule.category != "_logging_categories"_L1)
                continue;
            if (rule.enabled) {
                registryMsg("CATEGORY:%s %d %d %d %d",
                    cat->categoryName(),
                    cat->isDebugEnabled(),
                    cat->isWarningEnabled(),
                    cat->isCriticalEnabled(),
                    cat->isInfoEnabled()
                );
            }
            break;
        }
    }
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

//  QLoggingCategory::CategoryFilter
//      QLoggingRegistry::installFilter(QLoggingCategory::CategoryFilter
//      filter)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QLoggingRegistry13installFilterEPFvP16QLoggingCategoryE(
    QLoggingRegistry *self,
    void *filter) {
  return reinterpret_cast<void *>(
      self->installFilter(
          reinterpret_cast<QLoggingCategory::CategoryFilter>(filter)));
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

//  void QLoggingRegistry::defaultCategoryFilter(QLoggingCategory *category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingRegistry21defaultCategoryFilterEP16QLoggingCategory(
    QLoggingCategory *category) {
  QLoggingRegistry::defaultCategoryFilter(category);
}
