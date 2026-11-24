//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtWidgets/qframe.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/qcursor.h>
#if QT_CONFIG(sizegrip)
#include <QtWidgets/qsizegrip.h>
#endif
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qproxystyle.h>
#include <QtGui/qwindow.h>
#include <QtGui/qscreen.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
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

//  from src/widgets/widgets/qdockwidget.cpp, line 667, as _ZN18QDockWidgetPrivate10toggleViewEb
inline void QDockWidgetPrivate::toggleView(bool b)
{
    Q_Q(QDockWidget);
    if (b == q->isHidden()) {
        if (b)
            q->show();
        else
            q->close();
    }
}

//  from src/widgets/widgets/qdockwidget.cpp, line 715, as _ZN18QDockWidgetPrivate14toggleTopLevelEv
inline void QDockWidgetPrivate::toggleTopLevel()
{
    Q_Q(QDockWidget);
    q->setFloating(!q->isFloating());
}

//  from src/widgets/widgets/qdockwidget.cpp, line 875, as _ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockPositionE
inline Qt::DockWidgetArea QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
{
    switch (pos) {
    case QInternal::LeftDock:   return Qt::LeftDockWidgetArea;
    case QInternal::RightDock:  return Qt::RightDockWidgetArea;
    case QInternal::TopDock:    return Qt::TopDockWidgetArea;
    case QInternal::BottomDock: return Qt::BottomDockWidgetArea;
    default: break;
    }
    return Qt::NoDockWidgetArea;
}

//  from src/widgets/widgets/qdockwidget.cpp, line 1139, as _ZN18QDockWidgetPrivate19recalculatePressPosEP12QResizeEvent
inline void QDockWidgetPrivate::recalculatePressPos(QResizeEvent *event)
{
    qreal ratio = event->oldSize().width() / (1.0 * event->size().width());
    state->pressPos.setX(state->pressPos.x() / ratio);
}
//  -----------------------------------------------------------------------

//  QDockWidget *QDockWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN18QDockWidgetPrivate6q_funcEv(
    QDockWidgetPrivate *self) {
  return self->q_func();
}

//  const QDockWidget *QDockWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDockWidget *ritual_ZNK18QDockWidgetPrivate6q_funcEv(
    const QDockWidgetPrivate *self) {
  return self->q_func();
}

//  void QDockWidgetPrivate::toggleView(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate10toggleViewEb(
    QDockWidgetPrivate *self,
    bool a0) {
  self->toggleView(a0);
}

//  void QDockWidgetPrivate::toggleTopLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate14toggleTopLevelEv(
    QDockWidgetPrivate *self) {
  self->toggleTopLevel();
}

//  Qt::DockWidgetArea
//      QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockPositionE(
    QInternal::DockPosition pos) {
  return QDockWidgetPrivate::toDockWidgetArea(pos);
}

//  void QDockWidgetPrivate::recalculatePressPos(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate19recalculatePressPosEP12QResizeEvent(
    QDockWidgetPrivate *self,
    QResizeEvent *event) {
  self->recalculatePressPos(event);
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
