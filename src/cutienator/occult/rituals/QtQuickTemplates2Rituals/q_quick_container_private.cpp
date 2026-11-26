//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickContainerPrivate that Python can take functions over in. Every QQuickContainerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickContainerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickContainerPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickContainerPrivateCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickContainerPrivateCall3)(const void *, QQuickItem *, int *);
typedef qreal (*CuteQQuickContainerPrivateCall4)(const void *, int *);
typedef qreal (*CuteQQuickContainerPrivateCall5)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickContainerPrivateCall6)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickContainerPrivateCall7)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickContainerPrivateCall8)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickContainerPrivateCall9)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickContainerPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall13)(const void *, int *);
typedef void * (*CuteQQuickContainerPrivateCall14)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickContainerPrivateCall15)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickContainerPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickContainerPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall19)(const void *, bool, int *);
typedef void (*CuteQQuickContainerPrivateCall20)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall21)(const void *, bool, int *);
typedef void (*CuteQQuickContainerPrivateCall22)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickContainerPrivateCall23)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickContainerPrivateCall24)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickContainerPrivateCall25)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickContainerPrivateCall26)(const void *, int, int *);
typedef const QPalette * (*CuteQQuickContainerPrivateCall27)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickContainerPrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickContainerPrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickContainerPrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickContainerPrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickContainerPrivateCall33)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall34)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickContainerPrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickContainerPrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickContainerPrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickContainerPrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickContainerPrivateCall40)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall41)(const void *, int *);
typedef void (*CuteQQuickContainerPrivateCall42)(const void *, int, int *);
class CuteQQuickContainerPrivate : public QQuickContainerPrivate {
public:
  using QQuickContainerPrivate::QQuickContainerPrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
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

  //  void QQuickContainerPrivate::itemChildAdded(QQuickItem *item,
  //      QQuickItem *child)
  void itemChildAdded(QQuickItem *item, QQuickItem *child) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall0 call = reinterpret_cast<CuteQQuickContainerPrivateCall0>(taken[0]);
      call(this, item, child, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemChildAdded(item, child);
  }

  //  void QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem
  //      *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall1 call = reinterpret_cast<CuteQQuickContainerPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemSiblingOrderChanged(item);
  }

  //  void QQuickContainerPrivate::itemParentChanged(QQuickItem *item,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall2 call = reinterpret_cast<CuteQQuickContainerPrivateCall2>(taken[2]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemParentChanged(item, parent);
  }

  //  void QQuickContainerPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall3 call = reinterpret_cast<CuteQQuickContainerPrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemDestroyed(item);
  }

  //  qreal QQuickContainerPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall4 call = reinterpret_cast<CuteQQuickContainerPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickContainerPrivate::getContentWidth();
  }

  //  qreal QQuickContainerPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall5 call = reinterpret_cast<CuteQQuickContainerPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickContainerPrivate::getContentHeight();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall6 call = reinterpret_cast<CuteQQuickContainerPrivateCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall7 call = reinterpret_cast<CuteQQuickContainerPrivateCall7>(taken[7]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall8 call = reinterpret_cast<CuteQQuickContainerPrivateCall8>(taken[8]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall9 call = reinterpret_cast<CuteQQuickContainerPrivateCall9>(taken[9]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall10 call = reinterpret_cast<CuteQQuickContainerPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall11 call = reinterpret_cast<CuteQQuickContainerPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall12 call = reinterpret_cast<CuteQQuickContainerPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall13 call = reinterpret_cast<CuteQQuickContainerPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall14 call = reinterpret_cast<CuteQQuickContainerPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall15 call = reinterpret_cast<CuteQQuickContainerPrivateCall15>(taken[15]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall16 call = reinterpret_cast<CuteQQuickContainerPrivateCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall17 call = reinterpret_cast<CuteQQuickContainerPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall18 call = reinterpret_cast<CuteQQuickContainerPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall19 call = reinterpret_cast<CuteQQuickContainerPrivateCall19>(taken[19]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall20 call = reinterpret_cast<CuteQQuickContainerPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall21 call = reinterpret_cast<CuteQQuickContainerPrivateCall21>(taken[21]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall22 call = reinterpret_cast<CuteQQuickContainerPrivateCall22>(taken[22]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall23 call = reinterpret_cast<CuteQQuickContainerPrivateCall23>(taken[23]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall24 call = reinterpret_cast<CuteQQuickContainerPrivateCall24>(taken[24]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall25 call = reinterpret_cast<CuteQQuickContainerPrivateCall25>(taken[25]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall26 call = reinterpret_cast<CuteQQuickContainerPrivateCall26>(taken[26]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall27 call = reinterpret_cast<CuteQQuickContainerPrivateCall27>(taken[27]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall28 call = reinterpret_cast<CuteQQuickContainerPrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall29 call = reinterpret_cast<CuteQQuickContainerPrivateCall29>(taken[29]);
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
      CuteQQuickContainerPrivateCall30 call = reinterpret_cast<CuteQQuickContainerPrivateCall30>(taken[30]);
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
      CuteQQuickContainerPrivateCall31 call = reinterpret_cast<CuteQQuickContainerPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall32 call = reinterpret_cast<CuteQQuickContainerPrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall33 call = reinterpret_cast<CuteQQuickContainerPrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall34 call = reinterpret_cast<CuteQQuickContainerPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall35 call = reinterpret_cast<CuteQQuickContainerPrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall36 call = reinterpret_cast<CuteQQuickContainerPrivateCall36>(taken[36]);
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
      CuteQQuickContainerPrivateCall37 call = reinterpret_cast<CuteQQuickContainerPrivateCall37>(taken[37]);
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
      CuteQQuickContainerPrivateCall38 call = reinterpret_cast<CuteQQuickContainerPrivateCall38>(taken[38]);
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
      CuteQQuickContainerPrivateCall39 call = reinterpret_cast<CuteQQuickContainerPrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall40 call = reinterpret_cast<CuteQQuickContainerPrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall41 call = reinterpret_cast<CuteQQuickContainerPrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickContainerPrivateCall42 call = reinterpret_cast<CuteQQuickContainerPrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickContainer *QQuickContainerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickContainer *ritual_ZN22QQuickContainerPrivate6q_funcEv(
    QQuickContainerPrivate *self) {
  return self->q_func();
}

//  const QQuickContainer *QQuickContainerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickContainer *ritual_ZNK22QQuickContainerPrivate6q_funcEv(
    const QQuickContainerPrivate *self) {
  return self->q_func();
}

//  QQuickContainerPrivate *QQuickContainerPrivate::get(QQuickContainer
//      *container)
extern "C" Q_DECL_EXPORT
QQuickContainerPrivate *ritual_ZN22QQuickContainerPrivate3getEP15QQuickContainer(
    QQuickContainer *container) {
  return QQuickContainerPrivate::get(container);
}

//  void QQuickContainerPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate4initEv(QQuickContainerPrivate *self) {
  self->init();
}

//  void QQuickContainerPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate7cleanupEv(
    QQuickContainerPrivate *self) {
  self->cleanup();
}

//  QQuickItem *QQuickContainerPrivate::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK22QQuickContainerPrivate6itemAtEi(
    const QQuickContainerPrivate *self,
    int index) {
  return self->itemAt(index);
}

//  void QQuickContainerPrivate::insertItem(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate10insertItemEiP10QQuickItem(
    QQuickContainerPrivate *self,
    int index,
    QQuickItem *item) {
  self->insertItem(index, item);
}

//  void QQuickContainerPrivate::moveItem(int from, int to, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate8moveItemEiiP10QQuickItem(
    QQuickContainerPrivate *self,
    int from,
    int to,
    QQuickItem *item) {
  self->moveItem(from, to, item);
}

//  void QQuickContainerPrivate::removeItem(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate10removeItemEiP10QQuickItem(
    QQuickContainerPrivate *self,
    int index,
    QQuickItem *item) {
  self->removeItem(index, item);
}

//  void QQuickContainerPrivate::reorderItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate12reorderItemsEv(
    QQuickContainerPrivate *self) {
  self->reorderItems();
}

//  void QQuickContainerPrivate::maybeCullItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate13maybeCullItemEP10QQuickItem(
    QQuickContainerPrivate *self,
    QQuickItem *item) {
  self->maybeCullItem(item);
}

//  void QQuickContainerPrivate::maybeCullItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate14maybeCullItemsEv(
    QQuickContainerPrivate *self) {
  self->maybeCullItems();
}

//  void QQuickContainerPrivate::_q_currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate22_q_currentIndexChangedEv(
    QQuickContainerPrivate *self) {
  self->_q_currentIndexChanged();
}

//  void QQuickContainerPrivate::itemChildAdded(QQuickItem *item, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickContainerPrivate *self,
    QQuickItem *item,
    QQuickItem *child) {
  self->itemChildAdded(item, child);
}

//  void QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickContainerPrivate *self,
    QQuickItem *item) {
  self->itemSiblingOrderChanged(item);
}

//  void QQuickContainerPrivate::itemParentChanged(QQuickItem *item,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickContainerPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->itemParentChanged(item, parent);
}

//  void QQuickContainerPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate13itemDestroyedEP10QQuickItem(
    QQuickContainerPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickContainerPrivate::contentData_append(QQmlListProperty<QObject>
//      *prop, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate18contentData_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *obj) {
  QQuickContainerPrivate::contentData_append(prop, obj);
}

//  qsizetype
//      QQuickContainerPrivate::contentData_count(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuickContainerPrivate17contentData_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  return QQuickContainerPrivate::contentData_count(prop);
}

//  QObject *QQuickContainerPrivate::contentData_at(QQmlListProperty<QObject>
//      *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQuickContainerPrivate14contentData_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *prop,
    qsizetype index) {
  return QQuickContainerPrivate::contentData_at(prop, index);
}

//  void QQuickContainerPrivate::contentData_clear(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate17contentData_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  QQuickContainerPrivate::contentData_clear(prop);
}

//  void QQuickContainerPrivate::contentChildren_append(QQmlListProperty<QQui
//      ckItem> *prop, QQuickItem *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate22contentChildren_appendEP16QQmlListPropertyI10QQuickItemEPS1_(
    QQmlListProperty<QQuickItem> *prop,
    QQuickItem *obj) {
  QQuickContainerPrivate::contentChildren_append(prop, obj);
}

//  qsizetype QQuickContainerPrivate::contentChildren_count(QQmlListProperty<
//      QQuickItem> *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuickContainerPrivate21contentChildren_countEP16QQmlListPropertyI10QQuickItemE(
    QQmlListProperty<QQuickItem> *prop) {
  return QQuickContainerPrivate::contentChildren_count(prop);
}

//  QQuickItem
//      *QQuickContainerPrivate::contentChildren_at(QQmlListProperty<QQuickIt
//      em> *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN22QQuickContainerPrivate18contentChildren_atEP16QQmlListPropertyI10QQuickItemEx(
    QQmlListProperty<QQuickItem> *prop,
    qsizetype index) {
  return QQuickContainerPrivate::contentChildren_at(prop, index);
}

//  void QQuickContainerPrivate::contentChildren_clear(QQmlListProperty<QQuic
//      kItem> *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate21contentChildren_clearEP16QQmlListPropertyI10QQuickItemE(
    QQmlListProperty<QQuickItem> *prop) {
  QQuickContainerPrivate::contentChildren_clear(prop);
}

//  void QQuickContainerPrivate::updateContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate18updateContentWidthEv(
    QQuickContainerPrivate *self) {
  self->updateContentWidth();
}

//  void QQuickContainerPrivate::updateContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContainerPrivate19updateContentHeightEv(
    QQuickContainerPrivate *self) {
  self->updateContentHeight();
}

//  qreal QQuickContainerPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickContainerPrivate15getContentWidthEv(
    const QQuickContainerPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickContainerPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickContainerPrivate16getContentHeightEv(
    const QQuickContainerPrivate *self) {
  return self->getContentHeight();
}

//  a Python function taken by a CuteQQuickContainerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContainerPrivate(
    QQuickContainerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContainerPrivate *>(self)->take(key, call);
}

//  void QQuickContainerPrivate::itemChildAdded(QQuickItem *item, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickContainerPrivate *self,
    QQuickItem *item,
    QQuickItem *child) {
  self->QQuickContainerPrivate::itemChildAdded(item, child);
}

//  void QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickContainerPrivate *self,
    QQuickItem *item) {
  self->QQuickContainerPrivate::itemSiblingOrderChanged(item);
}

//  void QQuickContainerPrivate::itemParentChanged(QQuickItem *item,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickContainerPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->QQuickContainerPrivate::itemParentChanged(item, parent);
}

//  void QQuickContainerPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickContainerPrivate13itemDestroyedEP10QQuickItem(
    QQuickContainerPrivate *self,
    QQuickItem *item) {
  self->QQuickContainerPrivate::itemDestroyed(item);
}

//  qreal QQuickContainerPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QQuickContainerPrivate15getContentWidthEv(
    const QQuickContainerPrivate *self) {
  return self->QQuickContainerPrivate::getContentWidth();
}

//  qreal QQuickContainerPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QQuickContainerPrivate16getContentHeightEv(
    const QQuickContainerPrivate *self) {
  return self->QQuickContainerPrivate::getContentHeight();
}

#endif  // QT_CONFIG(quicktemplates2_container)
