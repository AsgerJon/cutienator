//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebengineextensioninfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#if QT_CONFIG(webengine_extensions)
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineextensioninfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <string>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/qwebengineextensioninfo.h>
#include <QtWebEngineCore/private/qwebengineextensioninfo_p.h>
#if QT_CONFIG(webengine_extensions)
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
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

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 42, as _ZN30QWebEngineExtensionInfoPrivateC1ERKNS_13ExtensionDataEPN15QtWebEngineCore16ExtensionManagerE
#if QT_CONFIG(webengine_extensions)
inline QWebEngineExtensionInfoPrivate::QWebEngineExtensionInfoPrivate(
        const ExtensionData &data, QtWebEngineCore::ExtensionManager *manager)
    : QSharedData(), m_data(data), m_manager(manager)
{
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 48, as _ZN30QWebEngineExtensionInfoPrivateD1Ev
#if QT_CONFIG(webengine_extensions)
inline QWebEngineExtensionInfoPrivate::~QWebEngineExtensionInfoPrivate() = default;
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 55, as _ZNK30QWebEngineExtensionInfoPrivate2idB5cxx11Ev
#if QT_CONFIG(webengine_extensions)
inline std::string QWebEngineExtensionInfoPrivate::id() const
{
    return m_data.id;
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 50, as _ZNK30QWebEngineExtensionInfoPrivate4nameEv
#if QT_CONFIG(webengine_extensions)
inline QString QWebEngineExtensionInfoPrivate::name() const
{
    return m_data.name;
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 60, as _ZNK30QWebEngineExtensionInfoPrivate11descriptionEv
#if QT_CONFIG(webengine_extensions)
inline QString QWebEngineExtensionInfoPrivate::description() const
{
    return m_data.description;
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 65, as _ZNK30QWebEngineExtensionInfoPrivate4pathEv
#if QT_CONFIG(webengine_extensions)
inline QString QWebEngineExtensionInfoPrivate::path() const
{
    return m_data.path;
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 70, as _ZNK30QWebEngineExtensionInfoPrivate5errorEv
#if QT_CONFIG(webengine_extensions)
inline QString QWebEngineExtensionInfoPrivate::error() const
{
    return m_data.error;
}
#endif  // QT_CONFIG(webengine_extensions)

//  from ../qtwebengine/src/core/api/qwebengineextensioninfo.cpp, line 75, as _ZNK30QWebEngineExtensionInfoPrivate14actionPopupUrlEv
#if QT_CONFIG(webengine_extensions)
inline QUrl QWebEngineExtensionInfoPrivate::actionPopupUrl() const
{
    return m_data.actionPopupUrl;
}
#endif  // QT_CONFIG(webengine_extensions)
//  -----------------------------------------------------------------------

//  QWebEngineExtensionInfoPrivate::QWebEngineExtensionInfoPrivate(const
//      ExtensionData &data, QtWebEngineCore::ExtensionManager *manager)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfoPrivate *ritual_ZN30QWebEngineExtensionInfoPrivateC1ERKNS_13ExtensionDataEPN15QtWebEngineCore16ExtensionManagerE(
    const QWebEngineExtensionInfoPrivate::ExtensionData *data,
    QtWebEngineCore::ExtensionManager *manager) {
  return new QWebEngineExtensionInfoPrivate(*data, manager);
}

//  QWebEngineExtensionInfoPrivate::~QWebEngineExtensionInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWebEngineExtensionInfoPrivateD1Ev(
    QWebEngineExtensionInfoPrivate *self) {
  delete self;
}

#if QT_CONFIG(webengine_extensions)
//  std::string QWebEngineExtensionInfoPrivate::id() const
extern "C" Q_DECL_EXPORT
std::string *ritual_ZNK30QWebEngineExtensionInfoPrivate2idB5cxx11Ev(
    const QWebEngineExtensionInfoPrivate *self) {
  return new std::string(self->id());
}
#endif  // QT_CONFIG(webengine_extensions)

#if QT_CONFIG(webengine_extensions)
//  QString QWebEngineExtensionInfoPrivate::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QWebEngineExtensionInfoPrivate4nameEv(
    const QWebEngineExtensionInfoPrivate *self) {
  return new QString(self->name());
}
#endif  // QT_CONFIG(webengine_extensions)

#if QT_CONFIG(webengine_extensions)
//  QString QWebEngineExtensionInfoPrivate::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QWebEngineExtensionInfoPrivate11descriptionEv(
    const QWebEngineExtensionInfoPrivate *self) {
  return new QString(self->description());
}
#endif  // QT_CONFIG(webengine_extensions)

#if QT_CONFIG(webengine_extensions)
//  QString QWebEngineExtensionInfoPrivate::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QWebEngineExtensionInfoPrivate4pathEv(
    const QWebEngineExtensionInfoPrivate *self) {
  return new QString(self->path());
}
#endif  // QT_CONFIG(webengine_extensions)

#if QT_CONFIG(webengine_extensions)
//  QString QWebEngineExtensionInfoPrivate::error() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QWebEngineExtensionInfoPrivate5errorEv(
    const QWebEngineExtensionInfoPrivate *self) {
  return new QString(self->error());
}
#endif  // QT_CONFIG(webengine_extensions)

#if QT_CONFIG(webengine_extensions)
//  QUrl QWebEngineExtensionInfoPrivate::actionPopupUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK30QWebEngineExtensionInfoPrivate14actionPopupUrlEv(
    const QWebEngineExtensionInfoPrivate *self) {
  return new QUrl(self->actionPopupUrl());
}
#endif  // QT_CONFIG(webengine_extensions)

//  a std::string a ritual of QWebEngineExtensionInfoPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEngineExtensionInfoPrivate__std_string(
    std::string *self) {
  delete self;
}

#endif  // QT_CONFIG(webengine_extensions)
