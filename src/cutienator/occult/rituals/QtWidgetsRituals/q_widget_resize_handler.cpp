//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetresizehandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(resizehandler)
#if QT_CONFIG(resizehandler)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetresizehandler_p.h>
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

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 22, as local:qwidgetresizehandler.cpp:RANGE
#define RANGE 4

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

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 132, as _ZN20QWidgetResizeHandler14mouseMoveEventEP11QMouseEvent
inline void QWidgetResizeHandler::mouseMoveEvent(QMouseEvent *e)
{
    QPoint pos = widget->mapFromGlobal(e->globalPosition()).toPoint();
    if (!active && !buttonDown) {
        if (pos.y() <= range && pos.x() <= range)
            mode = TopLeft;
        else if (pos.y() >= widget->height()-range && pos.x() >= widget->width()-range)
            mode = BottomRight;
        else if (pos.y() >= widget->height()-range && pos.x() <= range)
            mode = BottomLeft;
        else if (pos.y() <= range && pos.x() >= widget->width()-range)
            mode = TopRight;
        else if (pos.y() <= range)
            mode = Top;
        else if (pos.y() >= widget->height()-range)
            mode = Bottom;
        else if (pos.x() <= range)
            mode = Left;
        else if ( pos.x() >= widget->width()-range)
            mode = Right;
        else if (widget->rect().contains(pos))
            mode = Center;
        else
            mode = Nowhere;

        if (widget->isMinimized() || !isEnabled())
            mode = Center;
#ifndef QT_NO_CURSOR
        setMouseCursor(mode);
#endif
        return;
    }

    if (mode == Center)
        return;

    if (widget->testAttribute(Qt::WA_WState_ConfigPending))
        return;


    QPoint globalPos = (!widget->isWindow() && widget->parentWidget()) ?
                       widget->parentWidget()->mapFromGlobal(e->globalPosition()).toPoint() : e->globalPosition().toPoint();
    if (!widget->isWindow() && !widget->parentWidget()->rect().contains(globalPos)) {
        if (globalPos.x() < 0)
            globalPos.rx() = 0;
        if (globalPos.y() < 0)
            globalPos.ry() = 0;
        if (globalPos.x() > widget->parentWidget()->width())
            globalPos.rx() = widget->parentWidget()->width();
        if (globalPos.y() > widget->parentWidget()->height())
            globalPos.ry() = widget->parentWidget()->height();
    }

    QPoint p = globalPos + invertedMoveOffset;
    QPoint pp = globalPos - moveOffset;

    // Workaround for window managers which refuse to move a tool window partially offscreen.
    if (QGuiApplication::platformName() == "xcb"_L1) {
        const QRect desktop = QWidgetPrivate::availableScreenGeometry(widget);
        pp.rx() = qMax(pp.x(), desktop.left());
        pp.ry() = qMax(pp.y(), desktop.top());
        p.rx() = qMin(p.x(), desktop.right());
        p.ry() = qMin(p.y(), desktop.bottom());
    }

    QSize ms = qSmartMinSize(childWidget);
    int mw = ms.width();
    int mh = ms.height();
    if (childWidget != widget) {
        mw += 2 * fw;
        mh += 2 * fw + extrahei;
    }

    QSize maxsize(childWidget->maximumSize());
    if (childWidget != widget)
        maxsize += QSize(2 * fw, 2 * fw + extrahei);
    QSize mpsize(widget->geometry().right() - pp.x() + 1,
                  widget->geometry().bottom() - pp.y() + 1);
    mpsize = mpsize.expandedTo(widget->minimumSize()).expandedTo(QSize(mw, mh))
                    .boundedTo(maxsize);
    QPoint mp(widget->geometry().right() - mpsize.width() + 1,
               widget->geometry().bottom() - mpsize.height() + 1);

    QRect geom = widget->geometry();

    switch (mode) {
    case TopLeft:
        geom = QRect(mp, widget->geometry().bottomRight()) ;
        break;
    case BottomRight:
        geom = QRect(widget->geometry().topLeft(), p) ;
        break;
    case BottomLeft:
        geom = QRect(QPoint(mp.x(), widget->geometry().y()), QPoint(widget->geometry().right(), p.y())) ;
        break;
    case TopRight:
        geom = QRect(QPoint(widget->geometry().x(), mp.y()), QPoint(p.x(), widget->geometry().bottom())) ;
        break;
    case Top:
        geom = QRect(QPoint(widget->geometry().left(), mp.y()), widget->geometry().bottomRight()) ;
        break;
    case Bottom:
        geom = QRect(widget->geometry().topLeft(), QPoint(widget->geometry().right(), p.y())) ;
        break;
    case Left:
        geom = QRect(QPoint(mp.x(), widget->geometry().top()), widget->geometry().bottomRight()) ;
        break;
    case Right:
        geom = QRect(widget->geometry().topLeft(), QPoint(p.x(), widget->geometry().bottom())) ;
        break;
    default:
        break;
    }

    geom = QRect(geom.topLeft(),
                  geom.size().expandedTo(widget->minimumSize())
                             .expandedTo(QSize(mw, mh))
                             .boundedTo(maxsize));

    if (geom != widget->geometry() &&
        (widget->isWindow() || widget->parentWidget()->rect().intersects(geom))) {
        widget->setGeometry(geom);
    }
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

//  void *QWidgetResizeHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QWidgetResizeHandler11qt_metacastEPKc(
    QWidgetResizeHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWidgetResizeHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QWidgetResizeHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QWidgetResizeHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QWidgetResizeHandler::activate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler8activateEv(QWidgetResizeHandler *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWidgetResizeHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QWidgetResizeHandler::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QWidgetResizeHandler11eventFilterEP7QObjectP6QEvent(
    QWidgetResizeHandler *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  void QWidgetResizeHandler::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWidgetResizeHandler14mouseMoveEventEP11QMouseEvent(
    QWidgetResizeHandler *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
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
#endif  // QT_CONFIG(resizehandler)
