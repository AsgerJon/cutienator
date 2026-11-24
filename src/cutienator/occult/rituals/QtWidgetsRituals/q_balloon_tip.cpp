//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_SYSTEMTRAYICON)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpainter.h"
#include "qevent.h"
#include "qpixmapcache.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qlabel_p.h"
#include "private/qhexstring_p.h"
#include <qmath.h>
#if QT_CONFIG(style_stylesheet)
#include "private/qstylesheetstyle_p.h"
#endif
#if QT_CONFIG(abstractbutton)
#include "qabstractbutton.h"
#endif
#if QT_CONFIG(accessibility)
#include <qaccessible.h>
#endif
#include "qsystemtrayicon.h"
#include "qsystemtrayicon_p.h"
#ifndef QT_NO_SYSTEMTRAYICON
#if QT_CONFIG(menu)
#include "qmenu.h"
#endif
#include "qlist.h"
#include "qevent.h"
#include "qpoint.h"
#if QT_CONFIG(label)
#include "qlabel.h"
#include "private/qlabel_p.h"
#endif
#if QT_CONFIG(pushbutton)
#include "qpushbutton.h"
#endif
#include "qpainterpath.h"
#include "qpainter.h"
#include "qstyle.h"
#include "qgridlayout.h"
#include "qapplication.h"
#include "qbitmap.h"
#include <private/qhighdpiscaling_p.h>
#include <qpa/qplatformscreen.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qlabel.cpp, line 1562, as _ZNK13QLabelPrivate17ensureTextControlEv
inline void QLabelPrivate::ensureTextControl() const
{
    Q_Q(const QLabel);
    if (!isTextLabel)
        return;
    if (!control) {
        control = new QWidgetTextControl(const_cast<QLabel *>(q));
        control->document()->setUndoRedoEnabled(false);
        control->document()->setDefaultFont(q->font());
        if (resourceProvider != nullptr)
            control->document()->setResourceProvider(resourceProvider);
        control->setTextInteractionFlags(textInteractionFlags);
        control->setOpenExternalLinks(openExternalLinks);
        control->setPalette(q->palette());
        control->setFocus(q->hasFocus());
        QObject::connect(control, &QWidgetTextControl::updateRequest,
                         q, qOverload<>(&QLabel::update));
        QObject::connect(control, &QWidgetTextControl::linkActivated,
                         q, &QLabel::linkActivated);
        QObjectPrivate::connect(control, &QWidgetTextControl::linkHovered,
                                this, &QLabelPrivate::linkHovered);
        textLayoutDirty = true;
        textDirty = true;
    }
}

//  from src/widgets/util/qsystemtrayicon.cpp, line 556, as _ZN11QBalloonTip10paintEventEP11QPaintEvent
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QBalloonTip::paintEvent(QPaintEvent *)
{
    QPainter painter(this);
    painter.drawPixmap(rect(), pixmap);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/widgets/util/qsystemtrayicon.cpp, line 562, as _ZN11QBalloonTip11resizeEventEP12QResizeEvent
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QBalloonTip::resizeEvent(QResizeEvent *ev)
{
    QWidget::resizeEvent(ev);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/widgets/util/qsystemtrayicon.cpp, line 659, as _ZN11QBalloonTip15mousePressEventEP11QMouseEvent
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QBalloonTip::mousePressEvent(QMouseEvent *e)
{
    close();
    if (e->button() == Qt::LeftButton)
        emit trayIcon->messageClicked();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/widgets/util/qsystemtrayicon.cpp, line 666, as _ZN11QBalloonTip10timerEventEP11QTimerEvent
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QBalloonTip::timerEvent(QTimerEvent *e)
{
    if (e->id() == timer.id()) {
        timer.stop();
        if (!underMouse())
            close();
        return;
    }
    QWidget::timerEvent(e);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
//  -----------------------------------------------------------------------

//  Only a class built on QBalloonTip may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQBalloonTip : QBalloonTip {
  using QBalloonTip::paintEvent;
  using QBalloonTip::resizeEvent;
  using QBalloonTip::mousePressEvent;
  using QBalloonTip::timerEvent;
};

//  const QMetaObject *QBalloonTip::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QBalloonTip10metaObjectEv(
    const QBalloonTip *self) {
  return self->metaObject();
}

//  void QBalloonTip::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBalloonTip10paintEventEP11QPaintEvent(
    QBalloonTip *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QBalloonTip::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBalloonTip11resizeEventEP12QResizeEvent(
    QBalloonTip *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QBalloonTip::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBalloonTip15mousePressEventEP11QMouseEvent(
    QBalloonTip *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QBalloonTip::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBalloonTip10timerEventEP11QTimerEvent(
    QBalloonTip *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QBalloonTip::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QBalloonTip10paintEventEP11QPaintEvent(
    QBalloonTip *self,
    QPaintEvent *a0) {
  static_cast<OwnQBalloonTip *>(self)->OwnQBalloonTip::paintEvent(a0);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QBalloonTip::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QBalloonTip11resizeEventEP12QResizeEvent(
    QBalloonTip *self,
    QResizeEvent *a0) {
  static_cast<OwnQBalloonTip *>(self)->OwnQBalloonTip::resizeEvent(a0);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QBalloonTip::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QBalloonTip15mousePressEventEP11QMouseEvent(
    QBalloonTip *self,
    QMouseEvent *e) {
  static_cast<OwnQBalloonTip *>(self)->OwnQBalloonTip::mousePressEvent(e);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QBalloonTip::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QBalloonTip10timerEventEP11QTimerEvent(
    QBalloonTip *self,
    QTimerEvent *e) {
  static_cast<OwnQBalloonTip *>(self)->OwnQBalloonTip::timerEvent(e);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#endif  // !defined(QT_NO_SYSTEMTRAYICON)
