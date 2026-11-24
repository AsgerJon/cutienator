//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfileiconprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qfileiconprovider.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfileiconprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfileiconprovider.h"
#include "qfileiconprovider_p.h"
#include <qapplication.h>
#include <qdir.h>
#include <qpixmapcache.h>
#include <private/qfunctions_p.h>
#include <private/qguiapplication_p.h>
#include <private/qicon_p.h>
#include <private/qfilesystementry_p.h>
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformservices.h>
#include <qpa/qplatformtheme.h>
#if defined(Q_OS_WIN)
#  include <qt_windows.h>
#  include <commctrl.h>
#  include <objbase.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qfileiconprovider.cpp, line 35, as _ZN24QFileIconProviderPrivateC1EP17QFileIconProvider
inline QFileIconProviderPrivate::QFileIconProviderPrivate(QFileIconProvider *q)
    : QAbstractFileIconProviderPrivate(q), homePath(QDir::home().absolutePath())
{
}

//  from src/widgets/itemviews/qfileiconprovider.cpp, line 40, as _ZNK24QFileIconProviderPrivate7getIconEN6QStyle14StandardPixmapE
inline QIcon QFileIconProviderPrivate::getIcon(QStyle::StandardPixmap name) const
{
    switch (name) {
    case QStyle::SP_FileIcon:
        if (file.isNull())
            file = QApplication::style()->standardIcon(name);
        return file;
    case QStyle::SP_FileLinkIcon:
        if (fileLink.isNull())
            fileLink = QApplication::style()->standardIcon(name);
        return fileLink;
    case QStyle::SP_DirIcon:
        if (directory.isNull())
            directory = QApplication::style()->standardIcon(name);
        return directory;
    case QStyle::SP_DirLinkIcon:
        if (directoryLink.isNull())
            directoryLink = QApplication::style()->standardIcon(name);
        return directoryLink;
    case QStyle::SP_DriveHDIcon:
        if (harddisk.isNull())
            harddisk = QApplication::style()->standardIcon(name);
        return harddisk;
    case QStyle::SP_DriveFDIcon:
        if (floppy.isNull())
            floppy = QApplication::style()->standardIcon(name);
        return floppy;
    case QStyle::SP_DriveCDIcon:
        if (cdrom.isNull())
            cdrom = QApplication::style()->standardIcon(name);
        return cdrom;
    case QStyle::SP_DriveNetIcon:
        if (network.isNull())
            network = QApplication::style()->standardIcon(name);
        return network;
    case QStyle::SP_ComputerIcon:
        if (computer.isNull())
            computer = QApplication::style()->standardIcon(name);
        return computer;
    case QStyle::SP_DesktopIcon:
        if (desktop.isNull())
            desktop = QApplication::style()->standardIcon(name);
        return desktop;
    case QStyle::SP_TrashIcon:
        if (trashcan.isNull())
            trashcan = QApplication::style()->standardIcon(name);
        return trashcan;
    case QStyle::SP_DirHomeIcon:
        if (home.isNull())
            home = QApplication::style()->standardIcon(name);
        return home;
    default:
        return QIcon();
    }
    return QIcon();
}

//  from src/widgets/itemviews/qfileiconprovider.cpp, line 140, as _ZNK24QFileIconProviderPrivate7getIconERK9QFileInfo
inline QIcon QFileIconProviderPrivate::getIcon(const QFileInfo &fi) const
{
    return getPlatformThemeIcon(fi);
}
//  -----------------------------------------------------------------------

//  QFileIconProvider *QFileIconProviderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileIconProvider *ritual_ZN24QFileIconProviderPrivate6q_funcEv(
    QFileIconProviderPrivate *self) {
  return self->q_func();
}

//  const QFileIconProvider *QFileIconProviderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileIconProvider *ritual_ZNK24QFileIconProviderPrivate6q_funcEv(
    const QFileIconProviderPrivate *self) {
  return self->q_func();
}

//  QFileIconProviderPrivate::QFileIconProviderPrivate(QFileIconProvider *q)
extern "C" Q_DECL_EXPORT
QFileIconProviderPrivate *ritual_ZN24QFileIconProviderPrivateC1EP17QFileIconProvider(
    QFileIconProvider *q) {
  return new QFileIconProviderPrivate(q);
}

//  QIcon QFileIconProviderPrivate::getIcon(QStyle::StandardPixmap name)
//      const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK24QFileIconProviderPrivate7getIconEN6QStyle14StandardPixmapE(
    const QFileIconProviderPrivate *self,
    QStyle::StandardPixmap name) {
  return new QIcon(self->getIcon(name));
}

//  QIcon QFileIconProviderPrivate::getIcon(const QFileInfo &fi) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK24QFileIconProviderPrivate7getIconERK9QFileInfo(
    const QFileIconProviderPrivate *self,
    const QFileInfo *fi) {
  return new QIcon(self->getIcon(*fi));
}
