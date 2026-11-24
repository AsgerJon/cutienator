//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickswipedelegate_p.h"
#include "qquickswipedelegate_p_p.h"
#include "qquickcontrol_p_p.h"
#include "qquickitemdelegate_p_p.h"
#include "qquickvelocitycalculator_p_p.h"
#include <QtGui/qstylehints.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQuick/private/qquicktransitionmanager_p_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickswipedelegate.cpp, line 940, as _ZN26QQuickSwipeDelegatePrivate17forwardMouseEventEP11QMouseEventP10QQuickItem7QPointF
inline void QQuickSwipeDelegatePrivate::forwardMouseEvent(QMouseEvent *event, QQuickItem *destination, QPointF localPos)
{
    Q_Q(QQuickSwipeDelegate);
    QMutableSinglePointEvent localizedEvent(*event);
    QMutableEventPoint::setPosition(localizedEvent.point(0), localPos);
    QGuiApplication::sendEvent(destination, &localizedEvent);
    q->setPressed(!localizedEvent.isAccepted());
}

//  from ../qtdeclarative/src/quicktemplates/qquickswipedelegate.cpp, line 1024, as _ZNK26QQuickSwipeDelegatePrivate14getPressedItemEP10QQuickItemP11QMouseEvent
inline QQuickItem *QQuickSwipeDelegatePrivate::getPressedItem(QQuickItem *childItem, QMouseEvent *event) const
{
    if (!childItem || !event)
        return nullptr;

    QQuickItem *item = nullptr;

    if (childItem->acceptedMouseButtons() &&
            childItem->contains(childItem->mapFromScene(event->scenePosition()))) {
        item = childItem;
    } else {
        const auto &childItems = childItem->childItems();
        for (const auto &child: childItems) {
            if ((item = getPressedItem(child, event)))
                break;
        }
    }

    return item;
}

//  from ../qtdeclarative/src/quicktemplates/qquickswipedelegate.cpp, line 697, as _ZN26QQuickSwipeDelegatePrivate16resizeBackgroundEv
inline void QQuickSwipeDelegatePrivate::resizeBackground()
{
    if (!background)
        return;

    resizingBackground = true;

    QQuickItemPrivate *p = QQuickItemPrivate::get(background);
    const bool extraAllocated = extra.isAllocated();
    // Don't check for or set the x here since it will just be overwritten by reposition().
    if (((!p->widthValid() || !extraAllocated || !extra->hasBackgroundWidth))
            || (extraAllocated && (extra->hasLeftInset || extra->hasRightInset))) {
        background->setWidth(width - getLeftInset() - getRightInset());
    }
    if (((!p->heightValid() || !extraAllocated || !extra->hasBackgroundHeight) && qFuzzyIsNull(background->y()))
            || (extraAllocated && (extra->hasTopInset || extra->hasBottomInset))) {
        background->setY(getTopInset());
        background->setHeight(height - getTopInset() - getBottomInset());
    }

    resizingBackground = false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickswipedelegate.cpp, line 1013, as _ZNK26QQuickSwipeDelegatePrivate14defaultPaletteEv
inline QPalette QQuickSwipeDelegatePrivate::defaultPalette() const
{
    return QQuickTheme::palette(QQuickTheme::ListView);
}
//  -----------------------------------------------------------------------

//  A QQuickSwipeDelegatePrivate that Python can take functions over in. Every QQuickSwipeDelegatePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSwipeDelegatePrivateCall0)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall1)(const void *, int *);
typedef const QPalette * (*CuteQQuickSwipeDelegatePrivateCall2)(const void *, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall4)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall5)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall6)(const void *, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall7)(const void *, int, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall8)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall9)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall12)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickSwipeDelegatePrivateCall13)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSwipeDelegatePrivateCall14)(const void *, int *);
typedef void * (*CuteQQuickSwipeDelegatePrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSwipeDelegatePrivateCall16)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSwipeDelegatePrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickSwipeDelegatePrivateCall18)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall19)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall20)(const void *, bool, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall21)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall22)(const void *, bool, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall23)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall24)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall25)(const void *, int, int *);
typedef qreal (*CuteQQuickSwipeDelegatePrivateCall26)(const void *, int *);
typedef qreal (*CuteQQuickSwipeDelegatePrivateCall27)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickSwipeDelegatePrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickSwipeDelegatePrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickSwipeDelegatePrivateCall33)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall34)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickSwipeDelegatePrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickSwipeDelegatePrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickSwipeDelegatePrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickSwipeDelegatePrivateCall40)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall41)(const void *, int *);
typedef void (*CuteQQuickSwipeDelegatePrivateCall42)(const void *, int, int *);
class CuteQQuickSwipeDelegatePrivate : public QQuickSwipeDelegatePrivate {
public:
  using QQuickSwipeDelegatePrivate::QQuickSwipeDelegatePrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
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
    if (!std::strcmp(key, "_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[37] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[42] = call;
      return true;
    }
    return false;
  }

  //  void QQuickSwipeDelegatePrivate::resizeContent()
  void resizeContent() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall0 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSwipeDelegatePrivate::resizeContent();
  }

  //  void QQuickSwipeDelegatePrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall1 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSwipeDelegatePrivate::resizeBackground();
  }

  //  QPalette QQuickSwipeDelegatePrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall2 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall2>(taken[2]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickSwipeDelegatePrivate::defaultPalette();
  }

  //  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point,
  //      ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall3 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
  //      ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall4 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall4>(taken[4]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall5 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall5>(taken[5]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickAbstractButtonPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall6 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::handleUngrab();
  }

  //  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
  bool acceptKeyClick(Qt::Key key) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall7 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall7>(taken[7]);
      bool given = call(this, static_cast<int>(key), &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::acceptKeyClick(key);
  }

  //  void QQuickAbstractButtonPrivate::accessiblePressAction()
  void accessiblePressAction() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall8 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessiblePressAction();
  }

  //  void QQuickAbstractButtonPrivate::accessibleToggleAction()
  void accessibleToggleAction() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall9 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessibleToggleAction();
  }

  //  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall10 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall11 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall11>(taken[11]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall12 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall12>(taken[12]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemDestroyed(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall13 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall13>(taken[13]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall14 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall15 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall16 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall16>(taken[16]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall17 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall18 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall19 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall20 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall20>(taken[20]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall21 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall22 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall23 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall23>(taken[23]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall24 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall24>(taken[24]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall25 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall25>(taken[25]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall26 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall27 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall27>(taken[27]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall28 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall29 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall30 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall30>(taken[30]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall31 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall32 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall33 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall34 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall35 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall36 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall36>(taken[36]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall37 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall37>(taken[37]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall38 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall39 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall40 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall41 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickSwipeDelegatePrivateCall42 call = reinterpret_cast<CuteQQuickSwipeDelegatePrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickSwipeDelegate *QQuickSwipeDelegatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSwipeDelegate *ritual_ZN26QQuickSwipeDelegatePrivate6q_funcEv(
    QQuickSwipeDelegatePrivate *self) {
  return self->q_func();
}

//  const QQuickSwipeDelegate *QQuickSwipeDelegatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickSwipeDelegate *ritual_ZNK26QQuickSwipeDelegatePrivate6q_funcEv(
    const QQuickSwipeDelegatePrivate *self) {
  return self->q_func();
}

//  void QQuickSwipeDelegatePrivate::forwardMouseEvent(QMouseEvent *event,
//      QQuickItem *destination, QPointF localPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickSwipeDelegatePrivate17forwardMouseEventEP11QMouseEventP10QQuickItem7QPointF(
    QQuickSwipeDelegatePrivate *self,
    QMouseEvent *event,
    QQuickItem *destination,
    const QPointF *localPos) {
  self->forwardMouseEvent(event, destination, *localPos);
}

//  QQuickItem *QQuickSwipeDelegatePrivate::getPressedItem(QQuickItem
//      *childItem, QMouseEvent *event) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK26QQuickSwipeDelegatePrivate14getPressedItemEP10QQuickItemP11QMouseEvent(
    const QQuickSwipeDelegatePrivate *self,
    QQuickItem *childItem,
    QMouseEvent *event) {
  return self->getPressedItem(childItem, event);
}

//  void QQuickSwipeDelegatePrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickSwipeDelegatePrivate16resizeBackgroundEv(
    QQuickSwipeDelegatePrivate *self) {
  self->resizeBackground();
}

//  QPalette QQuickSwipeDelegatePrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK26QQuickSwipeDelegatePrivate14defaultPaletteEv(
    const QQuickSwipeDelegatePrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  a Python function taken by a CuteQQuickSwipeDelegatePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSwipeDelegatePrivate(
    QQuickSwipeDelegatePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSwipeDelegatePrivate *>(self)->take(key, call);
}

//  void QQuickSwipeDelegatePrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickSwipeDelegatePrivate16resizeBackgroundEv(
    QQuickSwipeDelegatePrivate *self) {
  self->QQuickSwipeDelegatePrivate::resizeBackground();
}

//  QPalette QQuickSwipeDelegatePrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK26QQuickSwipeDelegatePrivate14defaultPaletteEv(
    const QQuickSwipeDelegatePrivate *self) {
  return new QPalette(self->QQuickSwipeDelegatePrivate::defaultPalette());
}
