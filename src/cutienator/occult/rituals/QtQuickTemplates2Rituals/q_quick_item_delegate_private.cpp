//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A QQuickItemDelegatePrivate that Python can take functions over in. Every QQuickItemDelegatePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPalette * (*CuteQQuickItemDelegatePrivateCall0)(const void *, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall4)(const void *, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall5)(const void *, int, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall6)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall10)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickItemDelegatePrivateCall11)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickItemDelegatePrivateCall12)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall13)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall14)(const void *, int *);
typedef void * (*CuteQQuickItemDelegatePrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickItemDelegatePrivateCall16)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickItemDelegatePrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickItemDelegatePrivateCall18)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall19)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall20)(const void *, bool, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall21)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall22)(const void *, bool, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall23)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall24)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall25)(const void *, int, int *);
typedef qreal (*CuteQQuickItemDelegatePrivateCall26)(const void *, int *);
typedef qreal (*CuteQQuickItemDelegatePrivateCall27)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickItemDelegatePrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickItemDelegatePrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickItemDelegatePrivateCall33)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall34)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickItemDelegatePrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickItemDelegatePrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickItemDelegatePrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickItemDelegatePrivateCall40)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall41)(const void *, int *);
typedef void (*CuteQQuickItemDelegatePrivateCall42)(const void *, int, int *);
class CuteQQuickItemDelegatePrivate : public QQuickItemDelegatePrivate {
public:
  using QQuickItemDelegatePrivate::QQuickItemDelegatePrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
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

  //  QPalette QQuickItemDelegatePrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall0 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall0>(taken[0]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItemDelegatePrivate::defaultPalette();
  }

  //  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point,
  //      ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall1 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
  //      ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall2 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall3 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickAbstractButtonPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall4 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::handleUngrab();
  }

  //  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
  bool acceptKeyClick(Qt::Key key) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall5 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(key), &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::acceptKeyClick(key);
  }

  //  void QQuickAbstractButtonPrivate::accessiblePressAction()
  void accessiblePressAction() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall6 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessiblePressAction();
  }

  //  void QQuickAbstractButtonPrivate::accessibleToggleAction()
  void accessibleToggleAction() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall7 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessibleToggleAction();
  }

  //  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall8 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall9 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall10 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemDestroyed(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall11 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall11>(taken[11]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall12 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall13 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall14 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall15 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall15>(taken[15]);
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
      CuteQQuickItemDelegatePrivateCall16 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall16>(taken[16]);
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
      CuteQQuickItemDelegatePrivateCall17 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall17>(taken[17]);
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
      CuteQQuickItemDelegatePrivateCall18 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall19 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall20 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall20>(taken[20]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall21 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall22 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall22>(taken[22]);
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
      CuteQQuickItemDelegatePrivateCall23 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall23>(taken[23]);
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
      CuteQQuickItemDelegatePrivateCall24 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall24>(taken[24]);
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
      CuteQQuickItemDelegatePrivateCall25 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall25>(taken[25]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall26 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall27 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall27>(taken[27]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall28 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall29 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall29>(taken[29]);
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
      CuteQQuickItemDelegatePrivateCall30 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall30>(taken[30]);
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
      CuteQQuickItemDelegatePrivateCall31 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall32 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall33 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall34 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall35 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall36 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall36>(taken[36]);
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
      CuteQQuickItemDelegatePrivateCall37 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall37>(taken[37]);
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
      CuteQQuickItemDelegatePrivateCall38 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall38>(taken[38]);
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
      CuteQQuickItemDelegatePrivateCall39 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall40 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall41 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickItemDelegatePrivateCall42 call = reinterpret_cast<CuteQQuickItemDelegatePrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickItemDelegate *QQuickItemDelegatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickItemDelegate *ritual_ZN25QQuickItemDelegatePrivate6q_funcEv(
    QQuickItemDelegatePrivate *self) {
  return self->q_func();
}

//  const QQuickItemDelegate *QQuickItemDelegatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickItemDelegate *ritual_ZNK25QQuickItemDelegatePrivate6q_funcEv(
    const QQuickItemDelegatePrivate *self) {
  return self->q_func();
}

//  QPalette QQuickItemDelegatePrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK25QQuickItemDelegatePrivate14defaultPaletteEv(
    const QQuickItemDelegatePrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  a Python function taken by a CuteQQuickItemDelegatePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemDelegatePrivate(
    QQuickItemDelegatePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemDelegatePrivate *>(self)->take(key, call);
}

//  QPalette QQuickItemDelegatePrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK25QQuickItemDelegatePrivate14defaultPaletteEv(
    const QQuickItemDelegatePrivate *self) {
  return new QPalette(self->QQuickItemDelegatePrivate::defaultPalette());
}
