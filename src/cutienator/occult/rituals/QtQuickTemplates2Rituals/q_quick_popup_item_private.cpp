//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickpage_p.h>
#include <QtQuickTemplates2/private/qquickpage_p_p.h>
#include <QtQuickTemplates2/private/qquicktoolbar_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/private/qquicktabbar_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 132, as _ZN17QQuickPagePrivate13resizeContentEv
inline void QQuickPagePrivate::resizeContent()
{
    relayout();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpage.cpp, line 183, as _ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change, const QRectF & diff)
{
    QQuickPanePrivate::itemGeometryChanged(item, change, diff);
    if (item == header || item == footer)
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
//  -----------------------------------------------------------------------

//  A QQuickPopupItemPrivate that Python can take functions over in. Every QQuickPopupItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPopupItemPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall2)(const void *, int *);
typedef void * (*CuteQQuickPopupItemPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall5)(const void *, bool, int *);
typedef void (*CuteQQuickPopupItemPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall7)(const void *, bool, int *);
typedef void * (*CuteQQuickPopupItemPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall9)(const void *, QQuickPalette *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall10)(const void *, int *);
typedef const QPalette * (*CuteQQuickPopupItemPrivateCall11)(const void *, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall12)(const void *, int *);
typedef const QPalette * (*CuteQQuickPopupItemPrivateCall13)(const void *, const QPalette *, int *);
typedef void * (*CuteQQuickPopupItemPrivateCall14)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall19)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall20)(const void *, QQuickItem *, int *);
typedef void * (*CuteQQuickPopupItemPrivateCall21)(const void *, int *);
typedef qreal (*CuteQQuickPopupItemPrivateCall22)(const void *, int *);
typedef qreal (*CuteQQuickPopupItemPrivateCall23)(const void *, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall24)(const void *, const QPointF *, ulong, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPopupItemPrivateCall25)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPopupItemPrivateCall26)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall27)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickPopupItemPrivateCall28)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall29)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall30)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPopupItemPrivateCall31)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPopupItemPrivateCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickPopupItemPrivateCall33)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall34)(const void *, int, int *);
typedef void (*CuteQQuickPopupItemPrivateCall35)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall36)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall37)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickPopupItemPrivateCall38)(const void *, int *);
typedef qreal (*CuteQQuickPopupItemPrivateCall39)(const void *, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall40)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPopupItemPrivateCall41)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickPopupItemPrivateCall42)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickPopupItemPrivateCall43)(const void *, bool, int *);
typedef void * (*CuteQQuickPopupItemPrivateCall44)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall45)(const void *, int *);
typedef void (*CuteQQuickPopupItemPrivateCall46)(const void *, int, int *);
class CuteQQuickPopupItemPrivate : public QQuickPopupItemPrivate {
public:
  using QQuickPopupItemPrivate::QQuickPopupItemPrivate;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickPopupItemPrivate7paletteEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalette")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickPopupItemPrivate12resetPaletteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickPopupItemPrivate15providesPaletteEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalette")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickPanePrivate13getFirstChildEv")) {
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
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[41] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  void QQuickPopupItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall0 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::implicitWidthChanged();
  }

  //  void QQuickPopupItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall1 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::implicitHeightChanged();
  }

  //  void QQuickPopupItemPrivate::resolveFont()
  void resolveFont() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall2 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::resolveFont();
  }

  //  QQuickItem *QQuickPopupItemPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall3 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPopupItemPrivate::getContentItem();
  }

  //  void QQuickPopupItemPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall4 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::cancelContentItem();
  }

  //  void QQuickPopupItemPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall5 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall5>(taken[5]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::executeContentItem(complete);
  }

  //  void QQuickPopupItemPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall6 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::cancelBackground();
  }

  //  void QQuickPopupItemPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall7 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall7>(taken[7]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::executeBackground(complete);
  }

  //  QQuickPalette *QQuickPopupItemPrivate::palette() const
  QQuickPalette *palette() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall8 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPalette *>(given);
    }
    return QQuickPopupItemPrivate::palette();
  }

  //  void QQuickPopupItemPrivate::setPalette(QQuickPalette *p)
  void setPalette(QQuickPalette *p) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall9 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall9>(taken[9]);
      call(this, p, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::setPalette(p);
  }

  //  void QQuickPopupItemPrivate::resetPalette()
  void resetPalette() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall10 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupItemPrivate::resetPalette();
  }

  //  QPalette QQuickPopupItemPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall11 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall11>(taken[11]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopupItemPrivate::defaultPalette();
  }

  //  bool QQuickPopupItemPrivate::providesPalette() const
  bool providesPalette() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall12 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupItemPrivate::providesPalette();
  }

  //  QPalette QQuickPopupItemPrivate::parentPalette(const QPalette
  //      &fallbackPalette) const
  QPalette parentPalette(const QPalette &fallbackPalette) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall13 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall13>(taken[13]);
      const QPalette * given = call(this, &fallbackPalette, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopupItemPrivate::parentPalette(fallbackPalette);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickPopupItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall14 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall14>(taken[14]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickPopupItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickPagePrivate::resizeContent()
  void resizeContent() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall15 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::resizeContent();
  }

  //  void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall16 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall16>(taken[16]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemVisibilityChanged(item);
  }

  //  void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall17 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall17>(taken[17]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall18 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall19 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall19>(taken[19]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall20 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPagePrivate::itemDestroyed(item);
  }

  //  QQuickItem *QQuickPanePrivate::getFirstChild() const
  QQuickItem *getFirstChild() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall21 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPanePrivate::getFirstChild();
  }

  //  qreal QQuickPanePrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall22 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentWidth();
  }

  //  qreal QQuickPanePrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall23 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentHeight();
  }

  //  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall24 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall24>(taken[24]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::handlePress(point, timestamp);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall25 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall25>(taken[25]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall26 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall26>(taken[26]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall27 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall27>(taken[27]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall28 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall29 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall30 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall31 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall31>(taken[31]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall32 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall33 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall33>(taken[33]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall34 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall34>(taken[34]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall35 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall35>(taken[35]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall36 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall36>(taken[36]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall37 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall37>(taken[37]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall38 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall38>(taken[38]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall39 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall39>(taken[39]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall40 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall40>(taken[40]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall41 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall41>(taken[41]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall42 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall42>(taken[42]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall43 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall43>(taken[43]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall44 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall44>(taken[44]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall45 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickPopupItemPrivateCall46 call = reinterpret_cast<CuteQQuickPopupItemPrivateCall46>(taken[46]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickPopupItem *QQuickPopupItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPopupItem *ritual_ZN22QQuickPopupItemPrivate6q_funcEv(
    QQuickPopupItemPrivate *self) {
  return self->q_func();
}

//  const QQuickPopupItem *QQuickPopupItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopupItem *ritual_ZNK22QQuickPopupItemPrivate6q_funcEv(
    const QQuickPopupItemPrivate *self) {
  return self->q_func();
}

//  QQuickPopupItemPrivate::QQuickPopupItemPrivate(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupItemPrivate *ritual_ZN22QQuickPopupItemPrivateC1EP11QQuickPopup(
    QQuickPopup *popup) {
  return new CuteQQuickPopupItemPrivate(popup);
}

//  QQuickPopupItemPrivate *QQuickPopupItemPrivate::get(QQuickPopupItem
//      *popupItem)
extern "C" Q_DECL_EXPORT
QQuickPopupItemPrivate *ritual_ZN22QQuickPopupItemPrivate3getEP15QQuickPopupItem(
    QQuickPopupItem *popupItem) {
  return QQuickPopupItemPrivate::get(popupItem);
}

//  void QQuickPopupItemPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate20implicitWidthChangedEv(
    QQuickPopupItemPrivate *self) {
  self->implicitWidthChanged();
}

//  void QQuickPopupItemPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate21implicitHeightChangedEv(
    QQuickPopupItemPrivate *self) {
  self->implicitHeightChanged();
}

//  void QQuickPopupItemPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate11resolveFontEv(
    QQuickPopupItemPrivate *self) {
  self->resolveFont();
}

//  QQuickItem *QQuickPopupItemPrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN22QQuickPopupItemPrivate14getContentItemEv(
    QQuickPopupItemPrivate *self) {
  return self->getContentItem();
}

//  void QQuickPopupItemPrivate::cancelContentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate17cancelContentItemEv(
    QQuickPopupItemPrivate *self) {
  self->cancelContentItem();
}

//  void QQuickPopupItemPrivate::executeContentItem(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate18executeContentItemEb(
    QQuickPopupItemPrivate *self,
    bool complete) {
  self->executeContentItem(complete);
}

//  void QQuickPopupItemPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate16cancelBackgroundEv(
    QQuickPopupItemPrivate *self) {
  self->cancelBackground();
}

//  void QQuickPopupItemPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate17executeBackgroundEb(
    QQuickPopupItemPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  QQuickPalette *QQuickPopupItemPrivate::palette() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK22QQuickPopupItemPrivate7paletteEv(
    const QQuickPopupItemPrivate *self) {
  return self->palette();
}

//  void QQuickPopupItemPrivate::setPalette(QQuickPalette *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalette(
    QQuickPopupItemPrivate *self,
    QQuickPalette *p) {
  self->setPalette(p);
}

//  void QQuickPopupItemPrivate::resetPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPopupItemPrivate12resetPaletteEv(
    QQuickPopupItemPrivate *self) {
  self->resetPalette();
}

//  QPalette QQuickPopupItemPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK22QQuickPopupItemPrivate14defaultPaletteEv(
    const QQuickPopupItemPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  bool QQuickPopupItemPrivate::providesPalette() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickPopupItemPrivate15providesPaletteEv(
    const QQuickPopupItemPrivate *self) {
  return self->providesPalette();
}

//  QPalette QQuickPopupItemPrivate::parentPalette(const QPalette
//      &fallbackPalette) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalette(
    const QQuickPopupItemPrivate *self,
    const QPalette *fallbackPalette) {
  return new QPalette(self->parentPalette(*fallbackPalette));
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickPopupItemPrivate::attachedPropertyPropagator_parent(const
//      QMetaObject *attachedType)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZN22QQuickPopupItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject(
    QQuickPopupItemPrivate *self,
    const QMetaObject *attachedType) {
  return self->attachedPropertyPropagator_parent(attachedType);
}

//  a Python function taken by a CuteQQuickPopupItemPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPopupItemPrivate(
    QQuickPopupItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPopupItemPrivate *>(self)->take(key, call);
}

//  void QQuickPopupItemPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate20implicitWidthChangedEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::implicitWidthChanged();
}

//  void QQuickPopupItemPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate21implicitHeightChangedEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::implicitHeightChanged();
}

//  void QQuickPopupItemPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate11resolveFontEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::resolveFont();
}

//  QQuickItem *QQuickPopupItemPrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN22QQuickPopupItemPrivate14getContentItemEv(
    QQuickPopupItemPrivate *self) {
  return self->QQuickPopupItemPrivate::getContentItem();
}

//  void QQuickPopupItemPrivate::cancelContentItem()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate17cancelContentItemEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::cancelContentItem();
}

//  void QQuickPopupItemPrivate::executeContentItem(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate18executeContentItemEb(
    QQuickPopupItemPrivate *self,
    bool complete) {
  self->QQuickPopupItemPrivate::executeContentItem(complete);
}

//  void QQuickPopupItemPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate16cancelBackgroundEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::cancelBackground();
}

//  void QQuickPopupItemPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate17executeBackgroundEb(
    QQuickPopupItemPrivate *self,
    bool complete) {
  self->QQuickPopupItemPrivate::executeBackground(complete);
}

//  QQuickPalette *QQuickPopupItemPrivate::palette() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_own_ZNK22QQuickPopupItemPrivate7paletteEv(
    const QQuickPopupItemPrivate *self) {
  return self->QQuickPopupItemPrivate::palette();
}

//  void QQuickPopupItemPrivate::setPalette(QQuickPalette *p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalette(
    QQuickPopupItemPrivate *self,
    QQuickPalette *p) {
  self->QQuickPopupItemPrivate::setPalette(p);
}

//  void QQuickPopupItemPrivate::resetPalette()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickPopupItemPrivate12resetPaletteEv(
    QQuickPopupItemPrivate *self) {
  self->QQuickPopupItemPrivate::resetPalette();
}

//  QPalette QQuickPopupItemPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK22QQuickPopupItemPrivate14defaultPaletteEv(
    const QQuickPopupItemPrivate *self) {
  return new QPalette(self->QQuickPopupItemPrivate::defaultPalette());
}

//  bool QQuickPopupItemPrivate::providesPalette() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QQuickPopupItemPrivate15providesPaletteEv(
    const QQuickPopupItemPrivate *self) {
  return self->QQuickPopupItemPrivate::providesPalette();
}

//  QPalette QQuickPopupItemPrivate::parentPalette(const QPalette
//      &fallbackPalette) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalette(
    const QQuickPopupItemPrivate *self,
    const QPalette *fallbackPalette) {
  return new QPalette(
      self->QQuickPopupItemPrivate::parentPalette(
          *fallbackPalette));
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickPopupItemPrivate::attachedPropertyPropagator_parent(const
//      QMetaObject *attachedType)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_own_ZN22QQuickPopupItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject(
    QQuickPopupItemPrivate *self,
    const QMetaObject *attachedType) {
  return self->QQuickPopupItemPrivate::attachedPropertyPropagator_parent(
      attachedType);
}
