//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(toolbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#if QT_CONFIG(action)
#  include <QtWidgets/qwidgetaction.h>
#endif
#include <QtGui/qclipboard.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifndef QT_NO_IM
#include <QtGui/qinputmethod.h>
#include <QtCore/qlist.h>
#endif
#include <QtGui/qpainter.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/qvalidator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::setOpacity(qreal value)
{
    if (!qFuzzyCompare(m_opacity, value)) {
        m_opacity = value;
        updateCursor();
        update();
    }
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 390, as _ZNK19QLineEditIconButton18shouldHideWithTextEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline bool QLineEditIconButton::shouldHideWithText() const
{
    return m_hideWithText;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 395, as _ZN19QLineEditIconButton15setHideWithTextEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::setHideWithText(bool hide)
{
    m_hideWithText = hide;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 362, as _ZN19QLineEditIconButton11actionEventEP12QActionEvent
#if QT_CONFIG(toolbutton)
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
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 347, as _ZN19QLineEditIconButton10paintEventEP11QPaintEvent
#if QT_CONFIG(toolbutton)
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
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 438, as _ZN19QLineEditIconButton12updateCursorEv
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::updateCursor()
{
#ifndef QT_NO_CURSOR
    setCursor(qFuzzyCompare(m_opacity, qreal(1.0)) || !parentWidget() ? QCursor(Qt::ArrowCursor) : parentWidget()->cursor());
#endif
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 400, as _ZN19QLineEditIconButton19onAnimationFinishedEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
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
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 341, as _ZNK19QLineEditIconButton15lineEditPrivateEv
#if QT_CONFIG(toolbutton)
inline QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
{
    QLineEdit *le = qobject_cast<QLineEdit *>(parentWidget());
    return le ? static_cast<QLineEditPrivate *>(qt_widget_private(le)) : nullptr;
}
#endif  // QT_CONFIG(toolbutton)
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

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::setOpacity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton10setOpacityEd(
    QLineEditIconButton *self,
    qreal value) {
  self->setOpacity(value);
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  bool QLineEditIconButton::shouldHideWithText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton18shouldHideWithTextEv(
    const QLineEditIconButton *self) {
  return self->shouldHideWithText();
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::setHideWithText(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton15setHideWithTextEb(
    QLineEditIconButton *self,
    bool hide) {
  self->setHideWithText(hide);
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  bool QLineEditIconButton::needsSpace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton10needsSpaceEv(
    const QLineEditIconButton *self) {
  return self->needsSpace();
}
#endif  // QT_CONFIG(animation)

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

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::updateCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton12updateCursorEv(
    QLineEditIconButton *self) {
  self->updateCursor();
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::onAnimationFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton19onAnimationFinishedEv(
    QLineEditIconButton *self) {
  self->onAnimationFinished();
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(toolbutton)
//  QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZNK19QLineEditIconButton15lineEditPrivateEv(
    const QLineEditIconButton *self) {
  return self->lineEditPrivate();
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::actionEvent(QActionEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton11actionEventEP12QActionEvent(
    QLineEditIconButton *self,
    QActionEvent *e) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::actionEvent(
      e);
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton10paintEventEP11QPaintEvent(
    QLineEditIconButton *self,
    QPaintEvent *event) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::paintEvent(
      event);
}
#endif  // QT_CONFIG(toolbutton)

#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
