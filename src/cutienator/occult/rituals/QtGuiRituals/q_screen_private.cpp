//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qscreen_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qscreen.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qscreen.h>
#include <QtGui/private/qscreen_p.h>
#include <QtGui/qpixmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformscreen.h>
#include <QtGui/qpa/qplatformscreen_p.h>
#include <QtCore/QDebug>
#include <QtCore/private/qobject_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qscreen.cpp, line 66, as _ZN14QScreenPrivate14updateGeometryEv
inline void QScreenPrivate::updateGeometry()
{
    geometry = QHighDpi::fromNativeGlobalPosition(platformScreen->geometry(), platformScreen);
    availableGeometry = QHighDpi::fromNativeGlobalPosition(platformScreen->availableGeometry(), platformScreen);
}

//  from src/gui/kernel/qscreen.cpp, line 625, as _ZN14QScreenPrivate24updatePrimaryOrientationEv
inline void QScreenPrivate::updatePrimaryOrientation()
{
    primaryOrientation = geometry.width() >= geometry.height() ? Qt::LandscapeOrientation : Qt::PortraitOrientation;
}
//  -----------------------------------------------------------------------

//  QScreen *QScreenPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN14QScreenPrivate6q_funcEv(QScreenPrivate *self) {
  return self->q_func();
}

//  const QScreen *QScreenPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScreen *ritual_ZNK14QScreenPrivate6q_funcEv(
    const QScreenPrivate *self) {
  return self->q_func();
}

//  void QScreenPrivate::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenPrivate14updateGeometryEv(QScreenPrivate *self) {
  self->updateGeometry();
}

//  void QScreenPrivate::updatePrimaryOrientation()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenPrivate24updatePrimaryOrientationEv(
    QScreenPrivate *self) {
  self->updatePrimaryOrientation();
}

//  QScreenPrivate as the QScreenData it is built on
extern "C" Q_DECL_EXPORT
QScreenData *ritual_cast_QScreenPrivate_QScreenData(QScreenPrivate *self) {
  return static_cast<QScreenData *>(self);
}
