//  Edited by hand on 2026-11-25: the includes of
//  QtCore/private/qcoffpeparser_p.h and qmachparser_p.h are taken out:
//  Qt installs the first for Windows only and the second for Apple
//  systems only (file not found on Linux), and no ritual here uses
//  them. Kept as it is when the generator runs again.
//  Edited by hand again on 2026-11-26: the include of
//  QtCore/private/qelfparser_p.h is taken out too: Qt installs it for
//  Linux and the other systems of ELF only (file not found on macOS and
//  Windows), and no ritual here uses it. Kept as it is when the
//  generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlibrary_p.h, Qt 6.12.0.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(library)
#if QT_CONFIG(library)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlibrary_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlibrary.h>
#include <QtCore/private/qlibrary_p.h>
#include <QtCore/q20algorithm.h>
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qmutex.h>
#include <QtCore/qoperatingsystemversion.h>
#include <QtCore/qstringlist.h>
#ifdef Q_OS_DARWIN
#  include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtCore/private/qsystemerror_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtCore/q20map.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/plugin/qlibrary.cpp, line 583, as _ZN15QLibraryPrivate10loadPluginEv
inline QtPluginInstanceFunction QLibraryPrivate::loadPlugin()
{
    if (auto ptr = instanceFactory.loadAcquire()) {
        libraryUnloadCount.ref();
        return ptr;
    }
    if (pluginState == IsNotAPlugin)
        return nullptr;
    if (load()) {
        auto ptr = reinterpret_cast<QtPluginInstanceFunction>(resolve("qt_plugin_instance"));
        instanceFactory.storeRelease(ptr); // two threads may store the same value
        if (Q_LIKELY(ptr))
            return ptr;
        errorString = QLibrary::tr("Could not resolve 'qt_plugin_instance' function");
    }
    qCDebug(qt_lcDebugPlugins) << "QLibraryPrivate::loadPlugin failed on" << fileName << ":" << errorString;
    pluginState = IsNotAPlugin;
    return nullptr;
}

//  from src/corelib/plugin/qlibrary.cpp, line 453, as _ZN15QLibraryPrivateC1ERK7QStringS2_6QFlagsIN8QLibrary8LoadHintEE
inline QLibraryPrivate::QLibraryPrivate(const QString &canonicalFileName, const QString &version, QLibrary::LoadHints loadHints)
    : fileName(canonicalFileName), fullVersion(version), pluginState(MightBeAPlugin)
{
    loadHintsInt.storeRelaxed(loadHints.toInt());
    if (canonicalFileName.isEmpty())
        errorString = QLibrary::tr("The shared library was not found.");
}

//  from src/corelib/plugin/qlibrary.cpp, line 467, as _ZN15QLibraryPrivateD1Ev
inline QLibraryPrivate::~QLibraryPrivate()
{
}

//  from src/corelib/plugin/qlibrary.cpp, line 471, as _ZN15QLibraryPrivate14mergeLoadHintsE6QFlagsIN8QLibrary8LoadHintEE
inline void QLibraryPrivate::mergeLoadHints(QLibrary::LoadHints lh)
{
    // if the library is already loaded, we can't change the load hints
    if (pHnd.loadRelaxed())
        return;

    loadHintsInt.fetchAndOrRelaxed(lh.toInt());
}
//  -----------------------------------------------------------------------

//  QLibrary::LoadHints QLibraryPrivate::loadHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QLibraryPrivate9loadHintsEv(const QLibraryPrivate *self) {
  return static_cast<int>(self->loadHints().toInt());
}

//  QStringView QLibraryPrivate::prefix_sys()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QLibraryPrivate10prefix_sysEv() {
  return new QString(QLibraryPrivate::prefix_sys().toString());
}

//  QLibraryPrivate *QLibraryPrivate::get(QLibrary *lib)
extern "C" Q_DECL_EXPORT
QLibraryPrivate *ritual_ZN15QLibraryPrivate3getEP8QLibrary(QLibrary *lib) {
  return QLibraryPrivate::get(lib);
}

//  QLibraryPrivate::QLibraryPrivate(const QString &canonicalFileName, const
//      QString &version, QLibrary::LoadHints loadHints)
extern "C" Q_DECL_EXPORT
QLibraryPrivate *ritual_ZN15QLibraryPrivateC1ERK7QStringS2_6QFlagsIN8QLibrary8LoadHintEE(
    const QString *canonicalFileName,
    const QString *version,
    int loadHints) {
  return new QLibraryPrivate(
      *canonicalFileName,
      *version,
      QFlags<QLibrary::LoadHint>::fromInt(loadHints));
}

//  QLibraryPrivate::~QLibraryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLibraryPrivateD1Ev(QLibraryPrivate *self) {
  delete self;
}

//  void QLibraryPrivate::mergeLoadHints(QLibrary::LoadHints loadHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLibraryPrivate14mergeLoadHintsE6QFlagsIN8QLibrary8LoadHintEE(
    QLibraryPrivate *self,
    int loadHints) {
  self->mergeLoadHints(QFlags<QLibrary::LoadHint>::fromInt(loadHints));
}

#endif  // QT_CONFIG(library)
#endif  // QT_CONFIG(library)
