//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && (((QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))) || QT_CONFIG(wayland))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qgenericunixtheme_p.h>
#include <QtGui/private/qgnometheme_p.h>
#include <QtGui/QPalette>
#include <QtGui/QFont>
#include <QtGui/QGuiApplication>
#include <QtCore/QDir>
#include <QtCore/QFileInfo>
#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QHash>
#include <QtCore/QLoggingCategory>
#include <QtCore/QVariant>
#include <QtCore/QStandardPaths>
#include <QtCore/QStringList>
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#endif
#if QT_CONFIG(settings)
#include <QtCore/QSettings>
#if QT_CONFIG(dbus)
#include <QtGui/private/qkdetheme_p.h>
#endif
#endif
#include <QtGui/qpa/qplatformfontdatabase.h> // lcQpaFonts
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformservices.h>
#include <QtGui/qpa/qplatformdialoghelper.h>
#include <QtGui/qpa/qplatformtheme_p.h>
#if QT_CONFIG(dbus)
#include <QtCore/QJsonDocument>
#include <QtCore/QJsonArray>
#include <QtCore/QJsonObject>
#include <QtCore/QJsonValue>
#include <QtCore/QJsonParseError>
#include <QtGui/private/qdbusmenubar_p.h>
#endif
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#include <QtGui/private/qdbustrayicon_p.h>
#endif
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtCore/QStandardPaths>
#if QT_CONFIG(dbus)
#include <QtDBus/QDBusConnectionInterface>
#endif
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#include <QtCore/QMimeData>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/qgenericunixtheme.cpp, line 67, as _ZN24QGenericUnixThemePrivateC1Ev
inline QGenericUnixThemePrivate::QGenericUnixThemePrivate()
    : QPlatformThemePrivate()
    , systemFont(QLatin1StringView(QGenericUnixTheme::defaultSystemFontNameC),
                 QGenericUnixTheme::defaultSystemFontSize)
    , fixedFont(QLatin1StringView(QGenericUnixTheme::defaultFixedFontNameC),
                systemFont.pointSize())
{
    fixedFont.setStyleHint(QFont::TypeWriter);
    qCDebug(lcQpaFonts) << "default fonts: system" << systemFont << "fixed" << fixedFont;
}
//  -----------------------------------------------------------------------

//  QGenericUnixThemePrivate::QGenericUnixThemePrivate()
extern "C" Q_DECL_EXPORT
QGenericUnixThemePrivate *ritual_ZN24QGenericUnixThemePrivateC1Ev() {
  return new QGenericUnixThemePrivate();
}

//  QGenericUnixThemePrivate::~QGenericUnixThemePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGenericUnixThemePrivateD1Ev(
    QGenericUnixThemePrivate *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX) && (((QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))) || QT_CONFIG(wayland))
