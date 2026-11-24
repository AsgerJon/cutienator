//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_CONTEXTMENU)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::ContextMenuEvent::ContextMenuEvent(QWindow
//      *w, bool mouseTriggered, const QPoint &pos, const QPoint &globalPos,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ContextMenuEvent *ritual_ZN29QWindowSystemInterfacePrivate16ContextMenuEventC1EP7QWindowbRK6QPointS5_6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *w,
    bool mouseTriggered,
    const QPoint *pos,
    const QPoint *globalPos,
    int modifiers) {
  return new QWindowSystemInterfacePrivate::ContextMenuEvent(
      w,
      mouseTriggered,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QWindowSystemInterfacePrivate::ContextMenuEvent::~ContextMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate16ContextMenuEventD1Ev(
    QWindowSystemInterfacePrivate::ContextMenuEvent *self) {
  delete self;
}

#endif  // !defined(QT_NO_CONTEXTMENU)
