//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_SYSTEMTRAYICON)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qsystemtrayicon.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qsystemtrayicon.h>
#include <QtWidgets/private/qsystemtrayicon_p.h>
#ifndef QT_NO_SYSTEMTRAYICON
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtCore/qlist.h>
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#include <QtWidgets/private/qlabel_p.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#include <QtGui/qpainterpath.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qgridlayout.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtGui/qpa/qplatformscreen.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/util/qsystemtrayicon.cpp, line 417, as _ZN22QSystemTrayIconPrivate16_q_emitActivatedEN23QPlatformSystemTrayIcon16ActivationReasonE
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QSystemTrayIconPrivate::_q_emitActivated(QPlatformSystemTrayIcon::ActivationReason reason)
{
    Q_Q(QSystemTrayIcon);
    emit q->activated(static_cast<QSystemTrayIcon::ActivationReason>(reason));
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/widgets/util/qsystemtrayicon.cpp, line 690, as _ZN22QSystemTrayIconPrivate14remove_sys_qpaEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QSystemTrayIconPrivate::remove_sys_qpa()
{
    QObject::disconnect(qpa_sys, SIGNAL(activated(QPlatformSystemTrayIcon::ActivationReason)),
                        q_func(), SLOT(_q_emitActivated(QPlatformSystemTrayIcon::ActivationReason)));
    QObject::disconnect(qpa_sys, &QPlatformSystemTrayIcon::messageClicked,
                        q_func(), &QSystemTrayIcon::messageClicked);
    qpa_sys->cleanup();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/widgets/util/qsystemtrayicon.cpp, line 699, as _ZNK22QSystemTrayIconPrivate15addPlatformMenuEP5QMenu
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QSystemTrayIconPrivate::addPlatformMenu(QMenu *menu) const
{
#if QT_CONFIG(menu)
    if (menu->platformMenu())
        return; // The platform menu already exists.

    // The recursion depth is the same as menu depth, so should not
    // be higher than 3 levels.
    const auto actions = menu->actions();
    for (QAction *action : actions) {
        if (action->menu())
            addPlatformMenu(action->menu());
    }

    // This menu should be processed *after* its children, otherwise
    // setMenu() is not called on respective QPlatformMenuItems.
    QPlatformMenu *platformMenu = qpa_sys->createMenu();
    if (platformMenu)
        menu->setPlatformMenu(platformMenu);
#else
    Q_UNUSED(menu);
#endif // QT_CONFIG(menu)
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
//  -----------------------------------------------------------------------

//  QSystemTrayIcon *QSystemTrayIconPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSystemTrayIcon *ritual_ZN22QSystemTrayIconPrivate6q_funcEv(
    QSystemTrayIconPrivate *self) {
  return self->q_func();
}

//  const QSystemTrayIcon *QSystemTrayIconPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSystemTrayIcon *ritual_ZNK22QSystemTrayIconPrivate6q_funcEv(
    const QSystemTrayIconPrivate *self) {
  return self->q_func();
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QSystemTrayIconPrivate::_q_emitActivated(QPlatformSystemTrayIcon::Ac
//      tivationReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSystemTrayIconPrivate16_q_emitActivatedEN23QPlatformSystemTrayIcon16ActivationReasonE(
    QSystemTrayIconPrivate *self,
    QPlatformSystemTrayIcon::ActivationReason reason) {
  self->_q_emitActivated(reason);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QSystemTrayIconPrivate::remove_sys_qpa()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSystemTrayIconPrivate14remove_sys_qpaEv(
    QSystemTrayIconPrivate *self) {
  self->remove_sys_qpa();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QSystemTrayIconPrivate::addPlatformMenu(QMenu *menu) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QSystemTrayIconPrivate15addPlatformMenuEP5QMenu(
    const QSystemTrayIconPrivate *self,
    QMenu *menu) {
  self->addPlatformMenu(menu);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#endif  // !defined(QT_NO_SYSTEMTRAYICON)
