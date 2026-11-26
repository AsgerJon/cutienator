//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/private/qscreen_p.h>
#include <QtCore/QAbstractEventDispatcher>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/private/qlocking_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qpa/qplatformdrag.h>
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

//  from src/gui/kernel/qwindowsysteminterface.cpp, line 315, as _ZN29QWindowSystemInterfacePrivate11ExposeEventC1EP7QWindowRK7QRegion
inline QWindowSystemInterfacePrivate::ExposeEvent::ExposeEvent(QWindow *window, const QRegion &region)
    : WindowSystemEvent(Expose)
    , window(window)
    , isExposed(window && window->handle() ? window->handle()->isExposed() : false)
    , region(region)
{
}
//  -----------------------------------------------------------------------

//  QWindowSystemInterfacePrivate::ExposeEvent::ExposeEvent(QWindow *window,
//      const QRegion &region)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ExposeEvent *ritual_ZN29QWindowSystemInterfacePrivate11ExposeEventC1EP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return new QWindowSystemInterfacePrivate::ExposeEvent(window, *region);
}

//  QWindowSystemInterfacePrivate::ExposeEvent::~ExposeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate11ExposeEventD1Ev(
    QWindowSystemInterfacePrivate::ExposeEvent *self) {
  delete self;
}
