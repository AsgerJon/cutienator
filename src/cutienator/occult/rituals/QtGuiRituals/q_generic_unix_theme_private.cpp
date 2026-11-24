//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgenericunixtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgenericunixtheme_p.h"
#include "qgnometheme_p.h"
#include <QPalette>
#include <QFont>
#include <QGuiApplication>
#include <QDir>
#include <QFileInfo>
#include <QFile>
#include <QDebug>
#include <QHash>
#include <QLoggingCategory>
#include <QVariant>
#include <QStandardPaths>
#include <QStringList>
#if QT_CONFIG(mimetype)
#include <QMimeDatabase>
#endif
#if QT_CONFIG(settings)
#include <QSettings>
#if QT_CONFIG(dbus)
#include "qkdetheme_p.h"
#endif
#endif
#include <qpa/qplatformfontdatabase.h> // lcQpaFonts
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformservices.h>
#include <qpa/qplatformdialoghelper.h>
#include <qpa/qplatformtheme_p.h>
#if QT_CONFIG(dbus)
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QJsonValue>
#include <QJsonParseError>
#include <private/qdbusmenubar_p.h>
#endif
#if QT_CONFIG(dbus) && QT_CONFIG(systemtrayicon)
#include <private/qdbustrayicon_p.h>
#endif
#include <private/qguiapplication_p.h>
#include <qpa/qplatformintegration.h>
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
