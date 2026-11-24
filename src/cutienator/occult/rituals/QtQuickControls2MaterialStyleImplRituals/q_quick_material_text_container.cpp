//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialtextcontainer_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialtextcontainer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickmaterialtextcontainer_p.h"
#include <QtCore/qpropertyanimation.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 38, as _ZNK27QQuickMaterialTextContainer8isFilledEv
inline bool QQuickMaterialTextContainer::isFilled() const
{
    return m_filled;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 43, as _ZN27QQuickMaterialTextContainer9setFilledEb
inline void QQuickMaterialTextContainer::setFilled(bool filled)
{
    if (filled == m_filled)
        return;

    m_filled = filled;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 52, as _ZNK27QQuickMaterialTextContainer9fillColorEv
inline QColor QQuickMaterialTextContainer::fillColor() const
{
    return m_fillColor;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 57, as _ZN27QQuickMaterialTextContainer12setFillColorERK6QColor
inline void QQuickMaterialTextContainer::setFillColor(const QColor &fillColor)
{
    if (fillColor == m_fillColor)
        return;

    m_fillColor = fillColor;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 66, as _ZNK27QQuickMaterialTextContainer12outlineColorEv
inline QColor QQuickMaterialTextContainer::outlineColor() const
{
    return m_outlineColor;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 71, as _ZN27QQuickMaterialTextContainer15setOutlineColorERK6QColor
inline void QQuickMaterialTextContainer::setOutlineColor(const QColor &outlineColor)
{
    if (outlineColor == m_outlineColor)
        return;

    m_outlineColor = outlineColor;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 80, as _ZNK27QQuickMaterialTextContainer19focusedOutlineColorEv
inline QColor QQuickMaterialTextContainer::focusedOutlineColor() const
{
    return m_outlineColor;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 85, as _ZN27QQuickMaterialTextContainer22setFocusedOutlineColorERK6QColor
inline void QQuickMaterialTextContainer::setFocusedOutlineColor(const QColor &focusedOutlineColor)
{
    if (focusedOutlineColor == m_focusedOutlineColor)
        return;

    m_focusedOutlineColor = focusedOutlineColor;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 94, as _ZNK27QQuickMaterialTextContainer22focusAnimationProgressEv
inline qreal QQuickMaterialTextContainer::focusAnimationProgress() const
{
    return m_focusAnimationProgress;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 99, as _ZN27QQuickMaterialTextContainer25setFocusAnimationProgressEd
inline void QQuickMaterialTextContainer::setFocusAnimationProgress(qreal progress)
{
    if (qFuzzyCompare(progress, m_focusAnimationProgress))
        return;

    m_focusAnimationProgress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 108, as _ZNK27QQuickMaterialTextContainer20placeholderTextWidthEv
inline qreal QQuickMaterialTextContainer::placeholderTextWidth() const
{
    return m_placeholderTextWidth;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 113, as _ZN27QQuickMaterialTextContainer23setPlaceholderTextWidthEd
inline void QQuickMaterialTextContainer::setPlaceholderTextWidth(qreal placeholderTextWidth)
{
    if (qFuzzyCompare(placeholderTextWidth, m_placeholderTextWidth))
        return;

    m_placeholderTextWidth = placeholderTextWidth;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 136, as _ZNK27QQuickMaterialTextContainer21controlHasActiveFocusEv
inline bool QQuickMaterialTextContainer::controlHasActiveFocus() const
{
    return m_controlHasActiveFocus;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 154, as _ZNK27QQuickMaterialTextContainer14controlHasTextEv
inline bool QQuickMaterialTextContainer::controlHasText() const
{
    return m_controlHasText;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 172, as _ZNK27QQuickMaterialTextContainer18placeholderHasTextEv
inline bool QQuickMaterialTextContainer::placeholderHasText() const
{
    return m_placeholderHasText;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 188, as _ZNK27QQuickMaterialTextContainer17horizontalPaddingEv
inline int QQuickMaterialTextContainer::horizontalPadding() const
{
    return m_horizontalPadding;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 210, as _ZN27QQuickMaterialTextContainer5paintEP8QPainter
inline void QQuickMaterialTextContainer::paint(QPainter *painter)
{
    qreal w = width();
    qreal h = height();
    if (w <= 0 || h <= 0)
        return;

    // Account for pen width.
    const qreal penWidth = m_filled ? 1 : (m_controlHasActiveFocus ? 2 : 1);
    w -= penWidth;
    h -= penWidth;

    const qreal cornerRadius = 4;
    // This is coincidentally the same as cornerRadius, but use different variable names
    // to keep the code understandable.
    const qreal gapPadding = 4;
    // When animating focus on outlined containers, we need to make a gap
    // at the top left for the placeholder text.
    // If the text is too wide for the container, it will be elided, so
    // we shouldn't need to clamp its width here. TODO: check that this is the case for TextArea.
    const qreal halfPlaceholderWidth = m_placeholderTextWidth / 2;
    // Take care of different Alignment cases for the placeholder text.
    qreal gapCenterX;
    switch (m_placeholderTextHAlign) {
    case PlaceHolderHAlignment::AlignHCenter:
        gapCenterX = width() / 2;
        break;
    case PlaceHolderHAlignment::AlignRight:
        gapCenterX = width()  - halfPlaceholderWidth - m_horizontalPadding;
        break;
    default:
        gapCenterX = m_horizontalPadding + halfPlaceholderWidth;
        break;
    }

    QPainterPath path;

    QPointF startPos;

    // Top-left rounded corner.
    if (m_filled || m_focusAnimationProgress == 0) {
        startPos = QPointF(cornerRadius, 0);
    } else {
        // Start at the center of the gap and animate outwards towards the left-hand side.
        // Subtract gapPadding to account for the gap between the line and the placeholder text.
        // Also subtract the pen width because otherwise it extends by that distance too much to the right.
        // Changing the cap style to Qt::FlatCap would only fix this by half the pen width,
        // but it has no effect anyway (perhaps it literally only affects end points and not "start" points?).
        startPos = QPointF(gapCenterX - (m_focusAnimationProgress * halfPlaceholderWidth) - gapPadding - penWidth, 0);
    }
    path.moveTo(startPos);
    path.arcTo(0, 0, cornerRadius * 2, cornerRadius * 2, 90, 90);

    // Bottom-left corner.
    if (m_filled) {
        path.lineTo(0, h);
    } else {
        path.lineTo(0, h - cornerRadius * 2);
        path.arcTo(0, h - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 180, 90);
    }

    // Bottom-right corner.
    if (m_filled) {
        path.lineTo(w, h);
    } else {
        path.lineTo(w - cornerRadius * 2, h);
        path.arcTo(w - cornerRadius * 2, h - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 270, 90);
    }

    // Top-right rounded corner.
    path.lineTo(w, cornerRadius);
    path.arcTo(w - (cornerRadius * 2), 0, cornerRadius * 2, cornerRadius * 2, 0, 90);

    if (m_filled || qFuzzyIsNull(m_focusAnimationProgress)) {
        // Back to the start.
        path.lineTo(startPos.x(), startPos.y());
    } else {
        path.lineTo(gapCenterX + (m_focusAnimationProgress * halfPlaceholderWidth) + gapPadding, startPos.y());
    }

    // Account for pen width.
    painter->translate(penWidth / 2, penWidth / 2);

    painter->setRenderHint(QPainter::Antialiasing, true);

    auto control = textControl();
    const bool focused = control && control->hasActiveFocus();
    // We still want to draw the stroke when it's filled, otherwise it will be a pixel
    // (the pen width) too narrow on either side.
    QPen pen;
    pen.setColor(m_filled ? m_fillColor : (focused ? m_focusedOutlineColor : m_outlineColor));
    pen.setWidthF(penWidth);
    painter->setPen(pen);
    if (m_filled)
        painter->setBrush(m_fillColor);

    // Fill or stroke the container's shape.
    // If not filling, the default brush will be used, which is Qt::NoBrush.
    painter->drawPath(path);

    // Draw the focus line at the bottom for filled containers.
    if (m_filled) {
        if (!qFuzzyCompare(m_focusAnimationProgress, qreal(1.0))) {
            // Draw the enabled active indicator line (#10) that's at the bottom when it's not focused:
            // https://m3.material.io/components/text-fields/specs#6d654d1d-262e-4697-858c-9a75e8e7c81d
            // Don't bother drawing it when the animation has finished, as the focused active indicator
            // line below will obscure it.
            pen.setColor(m_outlineColor);
            painter->setPen(pen);
            painter->drawLine(0, h, w, h);
        }

        if (!qFuzzyIsNull(m_focusAnimationProgress)) {
            // Draw the focused active indicator line (#6) that's at the bottom when it's focused.
            // Start at the center and expand outwards.
            const int lineLength = m_focusAnimationProgress * w;
            const int horizontalCenter = w / 2;
            pen.setColor(m_focusedOutlineColor);
            pen.setWidth(2);
            painter->setPen(pen);
            painter->drawLine(horizontalCenter - (lineLength / 2), h,
                horizontalCenter + (lineLength / 2) + pen.width() / 2, h);
        }
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 122, as _ZNK27QQuickMaterialTextContainer21placeholderTextHAlignEv
inline QQuickMaterialTextContainer::PlaceHolderHAlignment QQuickMaterialTextContainer::placeholderTextHAlign() const
{
    return m_placeholderTextHAlign;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 127, as _ZN27QQuickMaterialTextContainer24setPlaceholderTextHAlignENS_21PlaceHolderHAlignmentE
inline void QQuickMaterialTextContainer::setPlaceholderTextHAlign(PlaceHolderHAlignment placeholderTextHAlign)
{
    if (m_placeholderTextHAlign == placeholderTextHAlign)
        return;

    m_placeholderTextHAlign = placeholderTextHAlign;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 336, as _ZNK27QQuickMaterialTextContainer20shouldAnimateOutlineEv
inline bool QQuickMaterialTextContainer::shouldAnimateOutline() const
{
    return !m_controlHasText && m_placeholderHasText;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 346, as _ZNK27QQuickMaterialTextContainer11textControlEv
inline QQuickItem *QQuickMaterialTextContainer::textControl() const
{
    return qobject_cast<QQuickItem *>(parent());
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 351, as _ZN27QQuickMaterialTextContainer21controlGotActiveFocusEv
inline void QQuickMaterialTextContainer::controlGotActiveFocus()
{
    if (m_focusAnimation) {
        m_focusAnimation->stop();
        m_focusAnimation.clear();
    }
    const bool shouldAnimate = m_filled ? !m_controlHasText : shouldAnimateOutline();
    if (!shouldAnimate) {
        // It does have focus, but sometimes we don't need to animate anything, just change colors.
        if (m_filled && m_controlHasText) {
            // When a filled container has text already entered, we should just immediately change
            // the color and thickness of the indicator line.
            m_focusAnimationProgress = 1;
        }
        update();
        return;
    }

    updateFocusAnimation(true);
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 372, as _ZN27QQuickMaterialTextContainer22controlLostActiveFocusEv
inline void QQuickMaterialTextContainer::controlLostActiveFocus()
{
    if (m_focusAnimation) {
        m_focusAnimation->stop();
        m_focusAnimation.clear();
    }
    // We don't want to animate the active indicator line (at the bottom) of filled containers
    // when the control loses focus, only when it gets it.
    if (m_filled || !shouldAnimateOutline()) {
        // Ensure that we set this so that filled containers go back to a non-accent-colored
        // active indicator line when losing focus.
        if (m_filled)
            m_focusAnimationProgress = 0;
        update();
        return;
    }

    updateFocusAnimation(true);
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 392, as _ZN27QQuickMaterialTextContainer20updateFocusAnimationEb
inline void QQuickMaterialTextContainer::updateFocusAnimation(bool createIfNeeded)
{
    if (m_filled) {
        if (m_focusAnimation) {
            m_focusAnimation->stop();
            m_focusAnimation.clear();
        }
        return;
    }

    int focusAnimationProgressValue = 0;
    if (m_controlHasText && m_placeholderHasText) {
        // Show the interrupted outline when there is text.
        focusAnimationProgressValue = 1;
    } else if (!m_controlHasText) {
        if (m_controlHasActiveFocus && m_placeholderHasText)
            focusAnimationProgressValue = 1;
        else
            focusAnimationProgressValue = 0;
    }

    if (m_focusAnimation || createIfNeeded) {
        int duration = 300;
        if (m_focusAnimation) {
            duration = m_focusAnimation->totalDuration() - m_focusAnimation->currentTime();
            m_focusAnimation->stop();
        }
        m_focusAnimation = new QPropertyAnimation(this, "focusAnimationProgress", this);
        m_focusAnimation->setDuration(duration);
        m_focusAnimation->setStartValue(focusAnimationProgress());
        m_focusAnimation->setEndValue(focusAnimationProgressValue);
        m_focusAnimation->start(QAbstractAnimation::DeleteWhenStopped);
    } else {
        setFocusAnimationProgress(focusAnimationProgressValue);
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialtextcontainer.cpp, line 429, as _ZN27QQuickMaterialTextContainer17componentCompleteEv
inline void QQuickMaterialTextContainer::componentComplete()
{
    QQuickPaintedItem::componentComplete();

    if (!parentItem())
        qmlWarning(this) << "Expected parent item by component completion!";

    updateFocusAnimation();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickMaterialTextContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickMaterialTextContainer10metaObjectEv(
    const QQuickMaterialTextContainer *self) {
  return self->metaObject();
}

//  bool QQuickMaterialTextContainer::isFilled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialTextContainer8isFilledEv(
    const QQuickMaterialTextContainer *self) {
  return self->isFilled();
}

//  void QQuickMaterialTextContainer::setFilled(bool filled)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer9setFilledEb(
    QQuickMaterialTextContainer *self,
    bool filled) {
  self->setFilled(filled);
}

//  QColor QQuickMaterialTextContainer::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK27QQuickMaterialTextContainer9fillColorEv(
    const QQuickMaterialTextContainer *self) {
  return new QColor(self->fillColor());
}

//  void QQuickMaterialTextContainer::setFillColor(const QColor &fillColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer12setFillColorERK6QColor(
    QQuickMaterialTextContainer *self,
    const QColor *fillColor) {
  self->setFillColor(*fillColor);
}

//  QColor QQuickMaterialTextContainer::outlineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK27QQuickMaterialTextContainer12outlineColorEv(
    const QQuickMaterialTextContainer *self) {
  return new QColor(self->outlineColor());
}

//  void QQuickMaterialTextContainer::setOutlineColor(const QColor
//      &outlineColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer15setOutlineColorERK6QColor(
    QQuickMaterialTextContainer *self,
    const QColor *outlineColor) {
  self->setOutlineColor(*outlineColor);
}

//  QColor QQuickMaterialTextContainer::focusedOutlineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK27QQuickMaterialTextContainer19focusedOutlineColorEv(
    const QQuickMaterialTextContainer *self) {
  return new QColor(self->focusedOutlineColor());
}

//  void QQuickMaterialTextContainer::setFocusedOutlineColor(const QColor
//      &focusedOutlineColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer22setFocusedOutlineColorERK6QColor(
    QQuickMaterialTextContainer *self,
    const QColor *focusedOutlineColor) {
  self->setFocusedOutlineColor(*focusedOutlineColor);
}

//  qreal QQuickMaterialTextContainer::focusAnimationProgress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQuickMaterialTextContainer22focusAnimationProgressEv(
    const QQuickMaterialTextContainer *self) {
  return self->focusAnimationProgress();
}

//  void QQuickMaterialTextContainer::setFocusAnimationProgress(qreal
//      progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer25setFocusAnimationProgressEd(
    QQuickMaterialTextContainer *self,
    qreal progress) {
  self->setFocusAnimationProgress(progress);
}

//  qreal QQuickMaterialTextContainer::placeholderTextWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQuickMaterialTextContainer20placeholderTextWidthEv(
    const QQuickMaterialTextContainer *self) {
  return self->placeholderTextWidth();
}

//  void QQuickMaterialTextContainer::setPlaceholderTextWidth(qreal
//      placeholderTextWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer23setPlaceholderTextWidthEd(
    QQuickMaterialTextContainer *self,
    qreal placeholderTextWidth) {
  self->setPlaceholderTextWidth(placeholderTextWidth);
}

//  bool QQuickMaterialTextContainer::controlHasActiveFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialTextContainer21controlHasActiveFocusEv(
    const QQuickMaterialTextContainer *self) {
  return self->controlHasActiveFocus();
}

//  bool QQuickMaterialTextContainer::controlHasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialTextContainer14controlHasTextEv(
    const QQuickMaterialTextContainer *self) {
  return self->controlHasText();
}

//  bool QQuickMaterialTextContainer::placeholderHasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialTextContainer18placeholderHasTextEv(
    const QQuickMaterialTextContainer *self) {
  return self->placeholderHasText();
}

//  int QQuickMaterialTextContainer::horizontalPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuickMaterialTextContainer17horizontalPaddingEv(
    const QQuickMaterialTextContainer *self) {
  return self->horizontalPadding();
}

//  void QQuickMaterialTextContainer::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer5paintEP8QPainter(
    QQuickMaterialTextContainer *self,
    QPainter *painter) {
  self->paint(painter);
}

//  PlaceHolderHAlignment
//      QQuickMaterialTextContainer::placeholderTextHAlign() const
extern "C" Q_DECL_EXPORT
QQuickMaterialTextContainer::PlaceHolderHAlignment ritual_ZNK27QQuickMaterialTextContainer21placeholderTextHAlignEv(
    const QQuickMaterialTextContainer *self) {
  return self->placeholderTextHAlign();
}

//  void QQuickMaterialTextContainer::setPlaceholderTextHAlign(PlaceHolderHAl
//      ignment placeHolderTextHAlign)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer24setPlaceholderTextHAlignENS_21PlaceHolderHAlignmentE(
    QQuickMaterialTextContainer *self,
    QQuickMaterialTextContainer::PlaceHolderHAlignment placeHolderTextHAlign) {
  self->setPlaceholderTextHAlign(placeHolderTextHAlign);
}

//  bool QQuickMaterialTextContainer::shouldAnimateOutline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialTextContainer20shouldAnimateOutlineEv(
    const QQuickMaterialTextContainer *self) {
  return self->shouldAnimateOutline();
}

//  QQuickItem *QQuickMaterialTextContainer::textControl() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK27QQuickMaterialTextContainer11textControlEv(
    const QQuickMaterialTextContainer *self) {
  return self->textControl();
}

//  void QQuickMaterialTextContainer::controlGotActiveFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer21controlGotActiveFocusEv(
    QQuickMaterialTextContainer *self) {
  self->controlGotActiveFocus();
}

//  void QQuickMaterialTextContainer::controlLostActiveFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer22controlLostActiveFocusEv(
    QQuickMaterialTextContainer *self) {
  self->controlLostActiveFocus();
}

//  void QQuickMaterialTextContainer::updateFocusAnimation(bool
//      createIfNeeded)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer20updateFocusAnimationEb(
    QQuickMaterialTextContainer *self,
    bool createIfNeeded) {
  self->updateFocusAnimation(createIfNeeded);
}

//  void QQuickMaterialTextContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialTextContainer17componentCompleteEv(
    QQuickMaterialTextContainer *self) {
  self->componentComplete();
}

//  void QQuickMaterialTextContainer::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickMaterialTextContainer5paintEP8QPainter(
    QQuickMaterialTextContainer *self,
    QPainter *painter) {
  self->QQuickMaterialTextContainer::paint(painter);
}

//  void QQuickMaterialTextContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickMaterialTextContainer17componentCompleteEv(
    QQuickMaterialTextContainer *self) {
  self->QQuickMaterialTextContainer::componentComplete();
}
