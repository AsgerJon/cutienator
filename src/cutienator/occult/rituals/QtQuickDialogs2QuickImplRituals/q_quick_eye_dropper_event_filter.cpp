//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_
//  p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogutils_p.h>
#include <QtQuickTemplates2/private/qquickslider_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformservices.h>
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickcolordialogimpl.cpp, line 30, as _ZN27QQuickEyeDropperEventFilter11eventFilterEP7QObjectP6QEvent
inline bool QQuickEyeDropperEventFilter::eventFilter(QObject *obj, QEvent *event)
{
    switch (event->type()) {
    case QEvent::MouseMove: {
        m_lastPosition = static_cast<QMouseEvent *>(event)->globalPosition().toPoint();
        m_update(m_lastPosition);
        return true;
    }
    case QEvent::MouseButtonRelease: {
        m_lastPosition = static_cast<QMouseEvent *>(event)->globalPosition().toPoint();
        m_leave(m_lastPosition, QQuickEyeDropperEventFilter::LeaveReason::Default);
        return true;
    }
    case QEvent::MouseButtonPress:
        return true;
    case QEvent::KeyPress: {
        auto keyEvent = static_cast<QKeyEvent *>(event);
#if QT_CONFIG(shortcut)
        if (keyEvent->matches(QKeySequence::Cancel))
            m_leave(m_lastPosition, QQuickEyeDropperEventFilter::LeaveReason::Cancel);
        else
#endif
        if (keyEvent->key() == Qt::Key_Return || keyEvent->key() == Qt::Key_Enter) {
            m_leave(m_lastPosition, QQuickEyeDropperEventFilter::LeaveReason::Default);
        } else if (keyEvent->key() == Qt::Key_Escape) {
            m_leave(m_lastPosition, QQuickEyeDropperEventFilter::LeaveReason::Cancel);
        }
        keyEvent->accept();
        return true;
    }
    default:
        return QObject::eventFilter(obj, event);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickEyeDropperEventFilter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickEyeDropperEventFilter : QQuickEyeDropperEventFilter {
  using QQuickEyeDropperEventFilter::eventFilter;
};

//  bool QQuickEyeDropperEventFilter::eventFilter(QObject *obj, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickEyeDropperEventFilter11eventFilterEP7QObjectP6QEvent(
    QQuickEyeDropperEventFilter *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

//  bool QQuickEyeDropperEventFilter::eventFilter(QObject *obj, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QQuickEyeDropperEventFilter11eventFilterEP7QObjectP6QEvent(
    QQuickEyeDropperEventFilter *self,
    QObject *obj,
    QEvent *event) {
  return static_cast<OwnQQuickEyeDropperEventFilter *>(self)->OwnQQuickEyeDropperEventFilter::eventFilter(
      obj,
      event);
}
