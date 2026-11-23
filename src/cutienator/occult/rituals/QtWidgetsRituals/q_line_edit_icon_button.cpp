//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#include "qlineedit.h"
#include "qlineedit_p.h"
#include "qvariant.h"
#if QT_CONFIG(itemviews)
#include "qabstractitemview.h"
#endif
#if QT_CONFIG(draganddrop)
#include "qdrag.h"
#endif
#if QT_CONFIG(action)
#  include "qwidgetaction.h"
#endif
#include "qclipboard.h"
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#endif
#ifndef QT_NO_IM
#include "qinputmethod.h"
#include "qlist.h"
#endif
#include <qpainter.h>
#if QT_CONFIG(animation)
#include <qpropertyanimation.h>
#endif
#include <qstylehints.h>
#include <qvalidator.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qlineedit_p.cpp, line 341, as _ZNK19QLineEditIconButton15lineEditPrivateEv
inline QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
{
    QLineEdit *le = qobject_cast<QLineEdit *>(parentWidget());
    return le ? static_cast<QLineEditPrivate *>(qt_widget_private(le)) : nullptr;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 521, as _ZN16QLineEditPrivate19positionSideWidgetsEv
inline void QLineEditPrivate::positionSideWidgets()
{
    Q_Q(QLineEdit);
    if (hasSideWidgets()) {
        const QRect contentRect = q->rect();
        const SideWidgetParameters p = sideWidgetParameters();
        const int delta = p.margin + p.widgetWidth;
        QRect widgetGeometry(QPoint(p.margin, (contentRect.height() - p.widgetHeight) / 2),
                             QSize(p.widgetWidth, p.widgetHeight));
        for (const SideWidgetEntry &e : leftSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() + delta);
#else
            Q_UNUSED(delta);
#endif
        }
        widgetGeometry.moveLeft(contentRect.width() - p.widgetWidth - p.margin);
        for (const SideWidgetEntry &e : rightSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() - delta);
#endif
        }
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 488, as _ZNK16QLineEditPrivate20sideWidgetParametersEv
inline QLineEditPrivate::SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
{
    Q_Q(const QLineEdit);
    SideWidgetParameters result;
    result.iconSize = q->style()->pixelMetric(QStyle::PM_LineEditIconSize, nullptr, q);
    result.margin = q->style()->pixelMetric(QStyle::PM_LineEditIconMargin, nullptr, q);
    result.widgetWidth = result.iconSize + 6;
    result.widgetHeight = result.iconSize + 2;
    return result;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 380, as _ZN19QLineEditIconButton10setOpacityEd
inline void QLineEditIconButton::setOpacity(qreal value)
{
    if (!qFuzzyCompare(m_opacity, value)) {
        m_opacity = value;
        updateCursor();
        update();
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 390, as _ZNK19QLineEditIconButton18shouldHideWithTextEv
inline bool QLineEditIconButton::shouldHideWithText() const
{
    return m_hideWithText;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 395, as _ZN19QLineEditIconButton15setHideWithTextEb
inline void QLineEditIconButton::setHideWithText(bool hide)
{
    m_hideWithText = hide;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 362, as _ZN19QLineEditIconButton11actionEventEP12QActionEvent
inline void QLineEditIconButton::actionEvent(QActionEvent *e)
{
    switch (e->type()) {
    case QEvent::ActionChanged: {
        const auto *action = e->action();
        if (isVisibleTo(parentWidget()) != action->isVisible()) {
            setVisible(action->isVisible());
            if (QLineEditPrivate *lep = lineEditPrivate())
                lep->positionSideWidgets();
        }
    }
        break;
    default:
        break;
    }
    QToolButton::actionEvent(e);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 347, as _ZN19QLineEditIconButton10paintEventEP11QPaintEvent
inline void QLineEditIconButton::paintEvent(QPaintEvent *)
{
    QPainter painter(this);
    QIcon::Mode mode = QIcon::Disabled;
    if (isEnabled())
        mode = isDown() ? QIcon::Active : QIcon::Normal;
    const QLineEditPrivate *lep = lineEditPrivate();
    const int iconWidth = lep ? lep->sideWidgetParameters().iconSize : 16;
    const QSize iconSize(iconWidth, iconWidth);
    QRect pixmapRect = QRect(QPoint(0, 0), iconSize);
    pixmapRect.moveCenter(rect().center());
    painter.setOpacity(m_opacity);
    icon().paint(&painter, pixmapRect, Qt::AlignCenter, mode, QIcon::Off);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 438, as _ZN19QLineEditIconButton12updateCursorEv
inline void QLineEditIconButton::updateCursor()
{
#ifndef QT_NO_CURSOR
    setCursor(qFuzzyCompare(m_opacity, qreal(1.0)) || !parentWidget() ? QCursor(Qt::ArrowCursor) : parentWidget()->cursor());
#endif
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 400, as _ZN19QLineEditIconButton19onAnimationFinishedEv
inline void QLineEditIconButton::onAnimationFinished()
{
    if (shouldHideWithText() && isVisible() && m_fadingOut) {
        hide();
        m_fadingOut = false;

        // Invalidate previous geometry to take into account new size of side widgets
        if (auto le = lineEditPrivate())
            le->updateGeometry_helper(true);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QLineEditIconButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLineEditIconButton : QLineEditIconButton {
  using QLineEditIconButton::actionEvent;
  using QLineEditIconButton::paintEvent;
};

//  const QMetaObject *QLineEditIconButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QLineEditIconButton10metaObjectEv(
    const QLineEditIconButton *self) {
  return self->metaObject();
}

//  qreal QLineEditIconButton::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QLineEditIconButton7opacityEv(
    const QLineEditIconButton *self) {
  return self->opacity();
}

//  void QLineEditIconButton::setOpacity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton10setOpacityEd(
    QLineEditIconButton *self,
    qreal value) {
  self->setOpacity(value);
}

//  bool QLineEditIconButton::shouldHideWithText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton18shouldHideWithTextEv(
    const QLineEditIconButton *self) {
  return self->shouldHideWithText();
}

//  void QLineEditIconButton::setHideWithText(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton15setHideWithTextEb(
    QLineEditIconButton *self,
    bool hide) {
  self->setHideWithText(hide);
}

//  bool QLineEditIconButton::needsSpace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton10needsSpaceEv(
    const QLineEditIconButton *self) {
  return self->needsSpace();
}

//  void QLineEditIconButton::actionEvent(QActionEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton11actionEventEP12QActionEvent(
    QLineEditIconButton *self,
    QActionEvent *e) {
  self->actionEvent(e);
}

//  void QLineEditIconButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton10paintEventEP11QPaintEvent(
    QLineEditIconButton *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QLineEditIconButton::updateCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton12updateCursorEv(
    QLineEditIconButton *self) {
  self->updateCursor();
}

//  void QLineEditIconButton::onAnimationFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton19onAnimationFinishedEv(
    QLineEditIconButton *self) {
  self->onAnimationFinished();
}

//  void QLineEditIconButton::actionEvent(QActionEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton11actionEventEP12QActionEvent(
    QLineEditIconButton *self,
    QActionEvent *e) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::actionEvent(
      e);
}

//  void QLineEditIconButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton10paintEventEP11QPaintEvent(
    QLineEditIconButton *self,
    QPaintEvent *event) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::paintEvent(
      event);
}
