//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickscrollbar_p.h"
#include "qquickscrollbar_p_p.h"
#include "qquickscrollview_p.h"
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickflickable_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 134, as _ZNK22QQuickScrollBarPrivate10visualAreaEv
inline QQuickScrollBarPrivate::VisualArea QQuickScrollBarPrivate::visualArea() const
{
    qreal visualPos = position;

    if (minimumSize > size && size != 1.0)
        visualPos = position / (1.0 - size) * (1.0 - minimumSize);

    qreal maximumSize = qMax<qreal>(0.0, 1.0 - visualPos);
    qreal visualSize =  qMax<qreal>(minimumSize,
                                    qMin<qreal>(qMax(size, minimumSize) + qMin<qreal>(0, visualPos),
                                                maximumSize));

    visualPos = qMax<qreal>(0,qMin<qreal>(visualPos,qMax<qreal>(0, 1.0 - visualSize)));

    return VisualArea(visualPos, visualSize);
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 151, as _ZNK22QQuickScrollBarPrivate15logicalPositionEd
inline qreal QQuickScrollBarPrivate::logicalPosition(qreal position) const
{
    if (minimumSize > size && minimumSize != 1.0)
        return position * (1.0 - size) / (1.0 - minimumSize);
    return position;
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 460, as _ZN22QQuickScrollBarPrivate11setPositionEdb
inline void QQuickScrollBarPrivate::setPosition(qreal newPosition, bool notifyVisualChange)
{
    Q_Q(QQuickScrollBar);
    if (!qt_is_finite(newPosition) || qFuzzyCompare(position, newPosition))
        return;

    auto oldVisualArea = visualArea();
    position = newPosition;
    if (q->isComponentComplete())
        resizeContent();
    emit q->positionChanged();
    if (notifyVisualChange)
        visualAreaChange(visualArea(), oldVisualArea);

#if QT_CONFIG(accessibility)
    if (QAccessible::isActive() && isAccessible) {
        if (QAccessibleInterface *accessible = QAccessible::queryAccessibleInterface(q)) {
            if (QAccessibleValueInterface *valueInterface = accessible->valueInterface()) {
                QAccessibleValueChangeEvent event(q, valueInterface->currentValue());
                QAccessible::updateAccessibility(&event);
            }
        }
    }
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 158, as _ZNK22QQuickScrollBarPrivate12snapPositionEd
inline qreal QQuickScrollBarPrivate::snapPosition(qreal position) const
{
    const qreal effectiveStep = stepSize * (1.0 - size);
    if (qFuzzyIsNull(effectiveStep))
        return position;

    return qRound(position / effectiveStep) * effectiveStep;
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 167, as _ZNK22QQuickScrollBarPrivate10positionAtERK7QPointF
inline qreal QQuickScrollBarPrivate::positionAt(const QPointF &point) const
{
    Q_Q(const QQuickScrollBar);
    if (orientation == Qt::Horizontal)
        return logicalPosition(point.x() - q->leftPadding()) / q->availableWidth();
    else
        return logicalPosition(point.y() - q->topPadding()) / q->availableHeight();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 176, as _ZN22QQuickScrollBarPrivate14setInteractiveEb
inline void QQuickScrollBarPrivate::setInteractive(bool enabled)
{
    Q_Q(QQuickScrollBar);
    if (interactive == enabled)
        return;

    interactive = enabled;
    if (interactive) {
        q->setAcceptedMouseButtons(Qt::LeftButton);
#if QT_CONFIG(quicktemplates2_multitouch)
        q->setAcceptTouchEvents(true);
#endif
#if QT_CONFIG(cursor)
        q->setCursor(Qt::ArrowCursor);
#endif
    } else {
        q->setAcceptedMouseButtons(Qt::NoButton);
#if QT_CONFIG(quicktemplates2_multitouch)
        q->setAcceptTouchEvents(false);
#endif
#if QT_CONFIG(cursor)
        q->unsetCursor();
#endif
        q->ungrabMouse();
    }
    emit q->interactiveChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 204, as _ZN22QQuickScrollBarPrivate12updateActiveEv
inline void QQuickScrollBarPrivate::updateActive()
{
    Q_Q(QQuickScrollBar);
#if QT_CONFIG(quicktemplates2_hover)
    bool hover = hovered;
#else
    bool hover = false;
#endif
    q->setActive(moving || (interactive && (pressed || hover)));
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 215, as _ZN22QQuickScrollBarPrivate13resizeContentEv
inline void QQuickScrollBarPrivate::resizeContent()
{
    Q_Q(QQuickScrollBar);
    if (!contentItem)
        return;

    // - negative overshoot (pos < 0): clamp the pos to 0, and deduct the overshoot from the size
    // - positive overshoot (pos + size > 1): clamp the size to 1-pos
    const VisualArea visual = visualArea();

    if (orientation == Qt::Horizontal) {
        contentItem->setPosition(QPointF(q->leftPadding() + visual.position * q->availableWidth(), q->topPadding()));
        contentItem->setSize(QSizeF(q->availableWidth() * visual.size, q->availableHeight()));
    } else {
        contentItem->setPosition(QPointF(q->leftPadding(), q->topPadding() + visual.position * q->availableHeight()));
        contentItem->setSize(QSizeF(q->availableWidth(), q->availableHeight() * visual.size));
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 234, as _ZN22QQuickScrollBarPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::itemImplicitWidthChanged(item);
    QQuickIndicatorButton *indicatorButton = q->decreaseVisual();
    if (!indicatorButton || item != indicatorButton->indicator()) {
        indicatorButton = q->increaseVisual();
        if (!indicatorButton || item != indicatorButton->indicator())
            return;
    }
    if (indicatorButton)
        emit indicatorButton->implicitIndicatorWidthChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 248, as _ZN22QQuickScrollBarPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::itemImplicitHeightChanged(item);
    QQuickIndicatorButton *indicatorButton = q->decreaseVisual();
    if (!indicatorButton || item != indicatorButton->indicator()) {
        indicatorButton = q->increaseVisual();
        if (!indicatorButton || item != indicatorButton->indicator())
            return;
    }
    if (indicatorButton)
        emit indicatorButton->implicitIndicatorHeightChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 262, as _ZN22QQuickScrollBarPrivate11handlePressERK7QPointFm
inline bool QQuickScrollBarPrivate::handlePress(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::handlePress(point, timestamp);
    if (QQuickIndicatorButton *indicatorButton = q->decreaseVisual()) {
        QQuickItem *decreaseArrow = indicatorButton->indicator();
        if (decreaseArrow && decreaseArrow->contains(q->mapToItem(decreaseArrow, point + QPointF(0.5, 0.5)))) {
            indicatorButton->setPressed(true);
            q->decrease();
            return true;
        }
    }

    if (QQuickIndicatorButton *increaseObject = q->increaseVisual()) {
        QQuickItem *increaseArrow = increaseObject->indicator();
        if (increaseArrow && increaseArrow->contains(q->mapToItem(increaseArrow, point + QPointF(0.5, 0.5)))) {
            increaseObject->setPressed(true);
            q->increase();
            return true;
        }
    }

    offset = positionAt(point) - position;
    qreal sz = qMax(size, logicalPosition(minimumSize));
    if (offset < 0 || offset > sz)
        offset = sz / 2;
    q->setPressed(true);
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 292, as _ZN22QQuickScrollBarPrivate10handleMoveERK7QPointFm
inline bool QQuickScrollBarPrivate::handleMove(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::handleMove(point, timestamp);

    /*
     * handleMove() will be called as soon as you hold the mouse button down *anywhere* on the
     * ScrollBar, including the increase/decrease button indicator areas. So without the following
     * early return, it would move the scrollbar handle to one of its extremeties. That would
     * ruin the behavior we would like when clicking e.g. the "increase button": To step the
     * scrollbar gently.
     */
    if (!pressed)
        return true;

    qreal pos = qMax<qreal>(0.0, qMin<qreal>(positionAt(point) - offset, 1.0 - size));
    if (snapMode == QQuickScrollBar::SnapAlways)
        pos = snapPosition(pos);
    q->setPosition(pos);
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 314, as _ZN22QQuickScrollBarPrivate13handleReleaseERK7QPointFm
inline bool QQuickScrollBarPrivate::handleRelease(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::handleRelease(point, timestamp);

    if (orientation == Qt::Vertical) {
        if (point.y() < q->topPadding() || point.y() >= (q->height() - q->bottomPadding()))
            return true;
    } else /* orientation == Qt::Horizontal */{
        if (point.x() < q->leftPadding() || point.x() >= (q->width() - q->rightPadding()))
            return true;
    }

    qreal pos = qMax<qreal>(0.0, qMin<qreal>(positionAt(point) - offset, 1.0 - size));
    if (snapMode != QQuickScrollBar::NoSnap)
        pos = snapPosition(pos);
    q->setPosition(pos);
    offset = 0.0;
    q->setPressed(false);
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 336, as _ZN22QQuickScrollBarPrivate12handleUngrabEv
inline void QQuickScrollBarPrivate::handleUngrab()
{
    Q_Q(QQuickScrollBar);
    QQuickControlPrivate::handleUngrab();
    offset = 0.0;
    q->setPressed(false);
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 344, as _ZN22QQuickScrollBarPrivate16visualAreaChangeERKNS_10VisualAreaES2_
inline void QQuickScrollBarPrivate::visualAreaChange(const VisualArea &newVisualArea, const VisualArea &oldVisualArea)
{
    Q_Q(QQuickScrollBar);
    if (!qFuzzyCompare(newVisualArea.size, oldVisualArea.size))
        emit q->visualSizeChanged();
    if (!qFuzzyCompare(newVisualArea.position, oldVisualArea.position))
        emit q->visualPositionChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickScrollBarPrivate that Python can take functions over in. Every QQuickScrollBarPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickScrollBarPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall2)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall4)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall5)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickScrollBarPrivateCall6)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickScrollBarPrivateCall7)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickScrollBarPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall9)(const void *, int *);
typedef void * (*CuteQQuickScrollBarPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickScrollBarPrivateCall11)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickScrollBarPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickScrollBarPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall15)(const void *, bool, int *);
typedef void (*CuteQQuickScrollBarPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall17)(const void *, bool, int *);
typedef void (*CuteQQuickScrollBarPrivateCall18)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall20)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall21)(const void *, int, int *);
typedef qreal (*CuteQQuickScrollBarPrivateCall22)(const void *, int *);
typedef qreal (*CuteQQuickScrollBarPrivateCall23)(const void *, int *);
typedef const QPalette * (*CuteQQuickScrollBarPrivateCall24)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall25)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickScrollBarPrivateCall27)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall28)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickScrollBarPrivateCall29)(const void *, int *);
typedef qreal (*CuteQQuickScrollBarPrivateCall30)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall31)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall32)(const void *, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall33)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickScrollBarPrivateCall34)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickScrollBarPrivateCall35)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickScrollBarPrivateCall36)(const void *, bool, int *);
typedef void * (*CuteQQuickScrollBarPrivateCall37)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickScrollBarPrivateCall39)(const void *, int, int *);
class CuteQQuickScrollBarPrivate : public QQuickScrollBarPrivate {
public:
  using QQuickScrollBarPrivate::QQuickScrollBarPrivate;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[34] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[39] = call;
      return true;
    }
    return false;
  }

  //  void QQuickScrollBarPrivate::resizeContent()
  void resizeContent() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall0 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickScrollBarPrivate::resizeContent();
  }

  //  void QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall1 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickScrollBarPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall2 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickScrollBarPrivate::itemImplicitHeightChanged(item);
  }

  //  bool QQuickScrollBarPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall3 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickScrollBarPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickScrollBarPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall4 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall4>(taken[4]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickScrollBarPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickScrollBarPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall5 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall5>(taken[5]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickScrollBarPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickScrollBarPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall6 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickScrollBarPrivate::handleUngrab();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall7 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall8 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall9 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall10 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall11 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall11>(taken[11]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall12 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall13 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall14 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall15 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall15>(taken[15]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall16 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall17 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall17>(taken[17]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall18 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall18>(taken[18]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall19 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall19>(taken[19]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemDestroyed(item);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall20 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall20>(taken[20]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall21 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall21>(taken[21]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall22 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall23 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall24 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall24>(taken[24]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall25 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall25>(taken[25]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall26 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall26>(taken[26]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall27 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall27>(taken[27]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall28 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall28>(taken[28]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall29 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall29>(taken[29]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall30 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall31 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall32 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall33 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall33>(taken[33]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall34 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall34>(taken[34]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall35 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall35>(taken[35]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall36 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall36>(taken[36]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall37 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall38 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickScrollBarPrivateCall39 call = reinterpret_cast<CuteQQuickScrollBarPrivateCall39>(taken[39]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickScrollBar *QQuickScrollBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickScrollBar *ritual_ZN22QQuickScrollBarPrivate6q_funcEv(
    QQuickScrollBarPrivate *self) {
  return self->q_func();
}

//  const QQuickScrollBar *QQuickScrollBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickScrollBar *ritual_ZNK22QQuickScrollBarPrivate6q_funcEv(
    const QQuickScrollBarPrivate *self) {
  return self->q_func();
}

//  QQuickScrollBarPrivate *QQuickScrollBarPrivate::get(QQuickScrollBar *bar)
extern "C" Q_DECL_EXPORT
QQuickScrollBarPrivate *ritual_ZN22QQuickScrollBarPrivate3getEP15QQuickScrollBar(
    QQuickScrollBar *bar) {
  return QQuickScrollBarPrivate::get(bar);
}

//  VisualArea QQuickScrollBarPrivate::visualArea() const
extern "C" Q_DECL_EXPORT
QQuickScrollBarPrivate::VisualArea *ritual_ZNK22QQuickScrollBarPrivate10visualAreaEv(
    const QQuickScrollBarPrivate *self) {
  return new QQuickScrollBarPrivate::VisualArea(self->visualArea());
}

//  qreal QQuickScrollBarPrivate::logicalPosition(qreal position) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickScrollBarPrivate15logicalPositionEd(
    const QQuickScrollBarPrivate *self,
    qreal position) {
  return self->logicalPosition(position);
}

//  void QQuickScrollBarPrivate::setPosition(qreal position, bool
//      notifyVisualChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate11setPositionEdb(
    QQuickScrollBarPrivate *self,
    qreal position,
    bool notifyVisualChange) {
  self->setPosition(position, notifyVisualChange);
}

//  qreal QQuickScrollBarPrivate::snapPosition(qreal position) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickScrollBarPrivate12snapPositionEd(
    const QQuickScrollBarPrivate *self,
    qreal position) {
  return self->snapPosition(position);
}

//  qreal QQuickScrollBarPrivate::positionAt(const QPointF &point) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickScrollBarPrivate10positionAtERK7QPointF(
    const QQuickScrollBarPrivate *self,
    const QPointF *point) {
  return self->positionAt(*point);
}

//  void QQuickScrollBarPrivate::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate14setInteractiveEb(
    QQuickScrollBarPrivate *self,
    bool interactive) {
  self->setInteractive(interactive);
}

//  void QQuickScrollBarPrivate::updateActive()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate12updateActiveEv(
    QQuickScrollBarPrivate *self) {
  self->updateActive();
}

//  void QQuickScrollBarPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate13resizeContentEv(
    QQuickScrollBarPrivate *self) {
  self->resizeContent();
}

//  void QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickScrollBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickScrollBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  bool QQuickScrollBarPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickScrollBarPrivate11handlePressERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  bool QQuickScrollBarPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickScrollBarPrivate10handleMoveERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(*point, timestamp);
}

//  bool QQuickScrollBarPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickScrollBarPrivate13handleReleaseERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(*point, timestamp);
}

//  void QQuickScrollBarPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate12handleUngrabEv(
    QQuickScrollBarPrivate *self) {
  self->handleUngrab();
}

//  void QQuickScrollBarPrivate::visualAreaChange(const VisualArea
//      &newVisualArea, const VisualArea &oldVisualArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickScrollBarPrivate16visualAreaChangeERKNS_10VisualAreaES2_(
    QQuickScrollBarPrivate *self,
    const QQuickScrollBarPrivate::VisualArea *newVisualArea,
    const QQuickScrollBarPrivate::VisualArea *oldVisualArea) {
  self->visualAreaChange(*newVisualArea, *oldVisualArea);
}

//  a Python function taken by a CuteQQuickScrollBarPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScrollBarPrivate(
    QQuickScrollBarPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScrollBarPrivate *>(self)->take(key, call);
}

//  void QQuickScrollBarPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickScrollBarPrivate13resizeContentEv(
    QQuickScrollBarPrivate *self) {
  self->QQuickScrollBarPrivate::resizeContent();
}

//  void QQuickScrollBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickScrollBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickScrollBarPrivate *self,
    QQuickItem *item) {
  self->QQuickScrollBarPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickScrollBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickScrollBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickScrollBarPrivate *self,
    QQuickItem *item) {
  self->QQuickScrollBarPrivate::itemImplicitHeightChanged(item);
}

//  bool QQuickScrollBarPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickScrollBarPrivate11handlePressERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickScrollBarPrivate::handlePress(*point, timestamp);
}

//  bool QQuickScrollBarPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickScrollBarPrivate10handleMoveERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickScrollBarPrivate::handleMove(*point, timestamp);
}

//  bool QQuickScrollBarPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickScrollBarPrivate13handleReleaseERK7QPointFm(
    QQuickScrollBarPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickScrollBarPrivate::handleRelease(*point, timestamp);
}

//  void QQuickScrollBarPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickScrollBarPrivate12handleUngrabEv(
    QQuickScrollBarPrivate *self) {
  self->QQuickScrollBarPrivate::handleUngrab();
}
