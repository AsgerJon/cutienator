//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickpage_p.h"
#include "qquickpage_p_p.h"
#include "qquicktoolbar_p.h"
#if QT_CONFIG(quicktemplates2_container)
#include "qquicktabbar_p.h"
#include "qquickdialogbuttonbox_p.h"
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 106, as _ZN17QQuickPagePrivate8relayoutEv
inline void QQuickPagePrivate::relayout()
{
    Q_Q(QQuickPage);
    const qreal hh = header && header->isVisible() ? header->height() : 0;
    const qreal fh = footer && footer->isVisible() ? footer->height() : 0;
    const qreal hsp = hh > 0 ? spacing : 0;
    const qreal fsp = fh > 0 ? spacing : 0;

    if (contentItem) {
        contentItem->setY(q->topPadding() + hh + hsp);
        contentItem->setX(q->leftPadding());
        contentItem->setWidth(q->availableWidth());
        contentItem->setHeight(q->availableHeight() - hh - fh - hsp - fsp);
    }

    if (header) {
        header->setY(0);
        header->setWidth(q->width());
    }

    if (footer) {
        footer->setY(q->height() - footer->height());
        footer->setWidth(q->width());
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 132, as _ZN17QQuickPagePrivate13resizeContentEv
inline void QQuickPagePrivate::resizeContent()
{
    relayout();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 137, as _ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem
inline void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
{
    Q_Q(QQuickPage);
    QQuickPanePrivate::itemVisibilityChanged(item);
    QScopedValueRollback signalGuard(emittingImplicitSizeChangedSignals, true);
    if (item == header) {
        emit q->implicitHeaderWidthChanged();
        emit q->implicitHeaderHeightChanged();
        relayout();
    } else if (item == footer) {
        emit q->implicitFooterWidthChanged();
        emit q->implicitFooterHeightChanged();
        relayout();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 153, as _ZN17QQuickPagePrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickPage);
    QQuickPanePrivate::itemImplicitWidthChanged(item);

    // Avoid binding loops by skipping signal emission if we're already doing it.
    if (emittingImplicitSizeChangedSignals)
        return;

    if (item == header)
        emit q->implicitHeaderWidthChanged();
    else if (item == footer)
        emit q->implicitFooterWidthChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 168, as _ZN17QQuickPagePrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickPage);
    QQuickPanePrivate::itemImplicitHeightChanged(item);

    // Avoid binding loops by skipping signal emission if we're already doing it.
    if (emittingImplicitSizeChangedSignals)
        return;

    if (item == header)
        emit q->implicitHeaderHeightChanged();
    else if (item == footer)
        emit q->implicitFooterHeightChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 183, as _ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change, const QRectF & diff)
{
    QQuickPanePrivate::itemGeometryChanged(item, change, diff);
    if (item == header || item == footer)
        relayout();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 190, as _ZN17QQuickPagePrivate13itemDestroyedEP10QQuickItem
inline void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
{
    Q_Q(QQuickPage);
    QQuickPanePrivate::itemDestroyed(item);
    if (item == header) {
        header = nullptr;
        relayout();
        emit q->implicitHeaderWidthChanged();
        emit q->implicitHeaderHeightChanged();
        emit q->headerChanged();
    } else if (item == footer) {
        footer = nullptr;
        relayout();
        emit q->implicitFooterWidthChanged();
        emit q->implicitFooterHeightChanged();
        emit q->footerChanged();
    }
}
//  -----------------------------------------------------------------------

//  A QQuickPagePrivate that Python can take functions over in. Every QQuickPagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPagePrivateCall0)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPagePrivateCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPagePrivateCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPagePrivateCall4)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickPagePrivateCall5)(const void *, QQuickItem *, int *);
typedef void * (*CuteQQuickPagePrivateCall6)(const void *, int *);
typedef void * (*CuteQQuickPagePrivateCall7)(const void *, int *);
typedef qreal (*CuteQQuickPagePrivateCall8)(const void *, int *);
typedef qreal (*CuteQQuickPagePrivateCall9)(const void *, int *);
typedef bool (*CuteQQuickPagePrivateCall10)(const void *, const QPointF *, ulong, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPagePrivateCall11)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPagePrivateCall12)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPagePrivateCall13)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickPagePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall16)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPagePrivateCall17)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPagePrivateCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickPagePrivateCall19)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall20)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall21)(const void *, bool, int *);
typedef void (*CuteQQuickPagePrivateCall22)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall23)(const void *, bool, int *);
typedef void (*CuteQQuickPagePrivateCall24)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickPagePrivateCall25)(const void *, int, int *);
typedef const QPalette * (*CuteQQuickPagePrivateCall26)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall27)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPagePrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickPagePrivateCall29)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickPagePrivateCall30)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickPagePrivateCall31)(const void *, int *);
typedef qreal (*CuteQQuickPagePrivateCall32)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall33)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall34)(const void *, int *);
typedef bool (*CuteQQuickPagePrivateCall35)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPagePrivateCall36)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickPagePrivateCall37)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickPagePrivateCall38)(const void *, bool, int *);
typedef void * (*CuteQQuickPagePrivateCall39)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall40)(const void *, int *);
typedef void (*CuteQQuickPagePrivateCall41)(const void *, int, int *);
class CuteQQuickPagePrivate : public QQuickPagePrivate {
public:
  using QQuickPagePrivate::QQuickPagePrivate;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickPanePrivate13getFirstChildEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
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
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[36] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[41] = call;
      return true;
    }
    return false;
  }

  //  void QQuickPagePrivate::resizeContent()
  void resizeContent() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPagePrivateCall0 call = reinterpret_cast<CuteQQuickPagePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::resizeContent();
  }

  //  void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPagePrivateCall1 call = reinterpret_cast<CuteQQuickPagePrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemVisibilityChanged(item);
  }

  //  void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPagePrivateCall2 call = reinterpret_cast<CuteQQuickPagePrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPagePrivateCall3 call = reinterpret_cast<CuteQQuickPagePrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPagePrivateCall4 call = reinterpret_cast<CuteQQuickPagePrivateCall4>(taken[4]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPagePrivateCall5 call = reinterpret_cast<CuteQQuickPagePrivateCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemDestroyed(item);
  }

  //  QQuickItem *QQuickPanePrivate::getFirstChild() const
  QQuickItem *getFirstChild() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPagePrivateCall6 call = reinterpret_cast<CuteQQuickPagePrivateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPanePrivate::getFirstChild();
  }

  //  QQuickItem *QQuickPanePrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPagePrivateCall7 call = reinterpret_cast<CuteQQuickPagePrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPanePrivate::getContentItem();
  }

  //  qreal QQuickPanePrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPagePrivateCall8 call = reinterpret_cast<CuteQQuickPagePrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentWidth();
  }

  //  qreal QQuickPanePrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPagePrivateCall9 call = reinterpret_cast<CuteQQuickPagePrivateCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentHeight();
  }

  //  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPagePrivateCall10 call = reinterpret_cast<CuteQQuickPagePrivateCall10>(taken[10]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::handlePress(point, timestamp);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPagePrivateCall11 call = reinterpret_cast<CuteQQuickPagePrivateCall11>(taken[11]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPagePrivateCall12 call = reinterpret_cast<CuteQQuickPagePrivateCall12>(taken[12]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPagePrivateCall13 call = reinterpret_cast<CuteQQuickPagePrivateCall13>(taken[13]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPagePrivateCall14 call = reinterpret_cast<CuteQQuickPagePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPagePrivateCall15 call = reinterpret_cast<CuteQQuickPagePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPagePrivateCall16 call = reinterpret_cast<CuteQQuickPagePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPagePrivateCall17 call = reinterpret_cast<CuteQQuickPagePrivateCall17>(taken[17]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPagePrivateCall18 call = reinterpret_cast<CuteQQuickPagePrivateCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPagePrivateCall19 call = reinterpret_cast<CuteQQuickPagePrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPagePrivateCall20 call = reinterpret_cast<CuteQQuickPagePrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPagePrivateCall21 call = reinterpret_cast<CuteQQuickPagePrivateCall21>(taken[21]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPagePrivateCall22 call = reinterpret_cast<CuteQQuickPagePrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPagePrivateCall23 call = reinterpret_cast<CuteQQuickPagePrivateCall23>(taken[23]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPagePrivateCall24 call = reinterpret_cast<CuteQQuickPagePrivateCall24>(taken[24]);
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
      CuteQQuickPagePrivateCall25 call = reinterpret_cast<CuteQQuickPagePrivateCall25>(taken[25]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPagePrivateCall26 call = reinterpret_cast<CuteQQuickPagePrivateCall26>(taken[26]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPagePrivateCall27 call = reinterpret_cast<CuteQQuickPagePrivateCall27>(taken[27]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPagePrivateCall28 call = reinterpret_cast<CuteQQuickPagePrivateCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPagePrivateCall29 call = reinterpret_cast<CuteQQuickPagePrivateCall29>(taken[29]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPagePrivateCall30 call = reinterpret_cast<CuteQQuickPagePrivateCall30>(taken[30]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPagePrivateCall31 call = reinterpret_cast<CuteQQuickPagePrivateCall31>(taken[31]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickPagePrivateCall32 call = reinterpret_cast<CuteQQuickPagePrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPagePrivateCall33 call = reinterpret_cast<CuteQQuickPagePrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPagePrivateCall34 call = reinterpret_cast<CuteQQuickPagePrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPagePrivateCall35 call = reinterpret_cast<CuteQQuickPagePrivateCall35>(taken[35]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPagePrivateCall36 call = reinterpret_cast<CuteQQuickPagePrivateCall36>(taken[36]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPagePrivateCall37 call = reinterpret_cast<CuteQQuickPagePrivateCall37>(taken[37]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickPagePrivateCall38 call = reinterpret_cast<CuteQQuickPagePrivateCall38>(taken[38]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickPagePrivateCall39 call = reinterpret_cast<CuteQQuickPagePrivateCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickPagePrivateCall40 call = reinterpret_cast<CuteQQuickPagePrivateCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickPagePrivateCall41 call = reinterpret_cast<CuteQQuickPagePrivateCall41>(taken[41]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickPage *QQuickPagePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPage *ritual_ZN17QQuickPagePrivate6q_funcEv(QQuickPagePrivate *self) {
  return self->q_func();
}

//  const QQuickPage *QQuickPagePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPage *ritual_ZNK17QQuickPagePrivate6q_funcEv(
    const QQuickPagePrivate *self) {
  return self->q_func();
}

//  void QQuickPagePrivate::relayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate8relayoutEv(QQuickPagePrivate *self) {
  self->relayout();
}

//  void QQuickPagePrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate13resizeContentEv(QQuickPagePrivate *self) {
  self->resizeContent();
}

//  void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->itemVisibilityChanged(item);
}

//  void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPagePrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPagePrivate13itemDestroyedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  a Python function taken by a CuteQQuickPagePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPagePrivate(
    QQuickPagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPagePrivate *>(self)->take(key, call);
}

//  void QQuickPagePrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate13resizeContentEv(
    QQuickPagePrivate *self) {
  self->QQuickPagePrivate::resizeContent();
}

//  void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->QQuickPagePrivate::itemVisibilityChanged(item);
}

//  void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->QQuickPagePrivate::itemImplicitWidthChanged(item);
}

//  void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->QQuickPagePrivate::itemImplicitHeightChanged(item);
}

//  void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPagePrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickPagePrivate::itemGeometryChanged(item, *change, *diff);
}

//  void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPagePrivate13itemDestroyedEP10QQuickItem(
    QQuickPagePrivate *self,
    QQuickItem *item) {
  self->QQuickPagePrivate::itemDestroyed(item);
}
