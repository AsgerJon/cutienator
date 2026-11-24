//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetresizehandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(resizehandler)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetresizehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwidgetresizehandler_p.h"
#include "qframe.h"
#include "qapplication.h"
#include "private/qwidget_p.h"
#include "qcursor.h"
#if QT_CONFIG(sizegrip)
#include "qsizegrip.h"
#endif
#include "qevent.h"
#include "qdebug.h"
#include "private/qlayoutengine_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 40, as _ZN20QWidgetResizeHandler10setEnabledEb
inline void QWidgetResizeHandler::setEnabled(bool b)
{
    if (b == enabled)
        return;

    enabled = b;
    if (!enabled)
        setMouseCursor(Nowhere);
}

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 50, as _ZNK20QWidgetResizeHandler9isEnabledEv
inline bool QWidgetResizeHandler::isEnabled() const
{
    return enabled;
}

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 55, as _ZN20QWidgetResizeHandler11eventFilterEP7QObjectP6QEvent
inline bool QWidgetResizeHandler::eventFilter(QObject *o, QEvent *ee)
{
    if (!isEnabled()
        || (ee->type() != QEvent::MouseButtonPress
            && ee->type() != QEvent::MouseButtonRelease
            && ee->type() != QEvent::MouseMove
            && ee->type() != QEvent::KeyPress
            && ee->type() != QEvent::ShortcutOverride)
        )
        return false;

    Q_ASSERT(o == widget);
    QWidget *w = widget;
    if (QApplication::activePopupWidget()) {
        if (buttonDown && ee->type() == QEvent::MouseButtonRelease)
            buttonDown = false;
        return false;
    }

    switch (ee->type()) {
    case QEvent::MouseButtonPress: {
        QMouseEvent *e = static_cast<QMouseEvent *>(ee);
        if (w->isMaximized())
            break;
        const QRect widgetRect = widget->rect().marginsAdded(QMargins(range, range, range, range));
        const QPoint cursorPoint = widget->mapFromGlobal(e->globalPosition()).toPoint();
        if (!widgetRect.contains(cursorPoint))
            return false;
        if (e->button() == Qt::LeftButton) {
            buttonDown = false;
            emit activate();
            mouseMoveEvent(e);
            buttonDown = true;
            moveOffset = widget->mapFromGlobal(e->globalPosition()).toPoint();
            invertedMoveOffset = widget->rect().bottomRight() - moveOffset;
            if (mode != Center)
                return true;
        }
    } break;
    case QEvent::MouseButtonRelease:
        if (w->isMaximized())
            break;
        if (static_cast<QMouseEvent *>(ee)->button() == Qt::LeftButton) {
            active = false;
            buttonDown = false;
            widget->releaseMouse();
            widget->releaseKeyboard();
            if (mode != Center)
                return true;
        }
        break;
    case QEvent::MouseMove: {
        if (w->isMaximized())
            break;
        QMouseEvent *e = static_cast<QMouseEvent *>(ee);
        buttonDown = buttonDown && (e->buttons() & Qt::LeftButton); // safety, state machine broken!
        mouseMoveEvent(e);
        if (mode != Center)
            return true;
    } break;
    case QEvent::KeyPress:
        keyPressEvent(static_cast<QKeyEvent *>(ee));
        break;
    case QEvent::ShortcutOverride:
        buttonDown &= ((QGuiApplication::mouseButtons() & Qt::LeftButton) != Qt::NoButton);
        if (buttonDown) {
            ee->accept();
            return true;
        }
        break;
    default:
        break;
    }

    return false;
}

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 257, as _ZN20QWidgetResizeHandler14setMouseCursorENS_13MousePositionE
inline void QWidgetResizeHandler::setMouseCursor(MousePosition m)
{
#ifdef QT_NO_CURSOR
    Q_UNUSED(m);
#else
    QObjectList children = widget->children();
    for (int i = 0; i < children.size(); ++i) {
        if (QWidget *w = qobject_cast<QWidget*>(children.at(i))) {
            if (!w->testAttribute(Qt::WA_SetCursor)) {
                w->setCursor(Qt::ArrowCursor);
            }
        }
    }

    switch (m) {
    case TopLeft:
    case BottomRight:
        widget->setCursor(Qt::SizeFDiagCursor);
        break;
    case BottomLeft:
    case TopRight:
        widget->setCursor(Qt::SizeBDiagCursor);
        break;
    case Top:
    case Bottom:
        widget->setCursor(Qt::SizeVerCursor);
        break;
    case Left:
    case Right:
        widget->setCursor(Qt::SizeHorCursor);
        break;
    default:
        widget->setCursor(Qt::ArrowCursor);
        break;
    }
#endif // QT_NO_CURSOR
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWidgetResizeHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWidgetResizeHandler10metaObjectEv(
    const QWidgetResizeHandler *self) {
  return self->metaObject();
}

//  void QWidgetResizeHandler::setEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler10setEnabledEb(
    QWidgetResizeHandler *self,
    bool b) {
  self->setEnabled(b);
}

//  bool QWidgetResizeHandler::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWidgetResizeHandler9isEnabledEv(
    const QWidgetResizeHandler *self) {
  return self->isEnabled();
}

//  bool QWidgetResizeHandler::isButtonDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWidgetResizeHandler12isButtonDownEv(
    const QWidgetResizeHandler *self) {
  return self->isButtonDown();
}

//  void QWidgetResizeHandler::setExtraHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler14setExtraHeightEi(
    QWidgetResizeHandler *self,
    int h) {
  self->setExtraHeight(h);
}

//  void QWidgetResizeHandler::setFrameWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler13setFrameWidthEi(
    QWidgetResizeHandler *self,
    int w) {
  self->setFrameWidth(w);
}

//  bool QWidgetResizeHandler::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QWidgetResizeHandler11eventFilterEP7QObjectP6QEvent(
    QWidgetResizeHandler *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  void QWidgetResizeHandler::setMouseCursor(MousePosition m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler14setMouseCursorENS_13MousePositionE(
    QWidgetResizeHandler *self,
    QWidgetResizeHandler::MousePosition m) {
  self->setMouseCursor(m);
}

//  bool QWidgetResizeHandler::isResizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWidgetResizeHandler10isResizingEv(
    const QWidgetResizeHandler *self) {
  return self->isResizing();
}

#endif  // QT_CONFIG(resizehandler)
