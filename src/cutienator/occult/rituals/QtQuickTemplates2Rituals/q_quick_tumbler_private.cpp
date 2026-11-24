//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qpalette.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickTumblerPrivate that Python can take functions over in. Every QQuickTumblerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPalette * (*CuteQQuickTumblerPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall1)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerPrivateCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerPrivateCall3)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickTumblerPrivateCall4)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickTumblerPrivateCall5)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickTumblerPrivateCall6)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickTumblerPrivateCall7)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickTumblerPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall11)(const void *, int *);
typedef void * (*CuteQQuickTumblerPrivateCall12)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTumblerPrivateCall13)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTumblerPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTumblerPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall17)(const void *, bool, int *);
typedef void (*CuteQQuickTumblerPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall19)(const void *, bool, int *);
typedef void (*CuteQQuickTumblerPrivateCall20)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerPrivateCall21)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerPrivateCall22)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerPrivateCall23)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickTumblerPrivateCall24)(const void *, int, int *);
typedef qreal (*CuteQQuickTumblerPrivateCall25)(const void *, int *);
typedef qreal (*CuteQQuickTumblerPrivateCall26)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall27)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTumblerPrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTumblerPrivateCall29)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTumblerPrivateCall30)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickTumblerPrivateCall31)(const void *, int *);
typedef qreal (*CuteQQuickTumblerPrivateCall32)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall33)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall34)(const void *, int *);
typedef bool (*CuteQQuickTumblerPrivateCall35)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickTumblerPrivateCall36)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTumblerPrivateCall37)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickTumblerPrivateCall38)(const void *, bool, int *);
typedef void * (*CuteQQuickTumblerPrivateCall39)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall40)(const void *, int *);
typedef void (*CuteQQuickTumblerPrivateCall41)(const void *, int, int *);
class CuteQQuickTumblerPrivate : public QQuickTumblerPrivate {
public:
  using QQuickTumblerPrivate::QQuickTumblerPrivate;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickItemS1_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
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

  //  QPalette QQuickTumblerPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall0 call = reinterpret_cast<CuteQQuickTumblerPrivateCall0>(taken[0]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTumblerPrivate::defaultPalette();
  }

  //  void QQuickTumblerPrivate::itemChildAdded(QQuickItem *a0, QQuickItem
  //      *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall1 call = reinterpret_cast<CuteQQuickTumblerPrivateCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickTumblerPrivate::itemChildAdded(a0, a1);
  }

  //  void QQuickTumblerPrivate::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall2 call = reinterpret_cast<CuteQQuickTumblerPrivateCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickTumblerPrivate::itemChildRemoved(a0, a1);
  }

  //  void QQuickTumblerPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall3 call = reinterpret_cast<CuteQQuickTumblerPrivateCall3>(taken[3]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickTumblerPrivate::itemGeometryChanged(a0, a1, a2);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall4 call = reinterpret_cast<CuteQQuickTumblerPrivateCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall5 call = reinterpret_cast<CuteQQuickTumblerPrivateCall5>(taken[5]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall6 call = reinterpret_cast<CuteQQuickTumblerPrivateCall6>(taken[6]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall7 call = reinterpret_cast<CuteQQuickTumblerPrivateCall7>(taken[7]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall8 call = reinterpret_cast<CuteQQuickTumblerPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall9 call = reinterpret_cast<CuteQQuickTumblerPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall10 call = reinterpret_cast<CuteQQuickTumblerPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall11 call = reinterpret_cast<CuteQQuickTumblerPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall12 call = reinterpret_cast<CuteQQuickTumblerPrivateCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall13 call = reinterpret_cast<CuteQQuickTumblerPrivateCall13>(taken[13]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall14 call = reinterpret_cast<CuteQQuickTumblerPrivateCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall15 call = reinterpret_cast<CuteQQuickTumblerPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall16 call = reinterpret_cast<CuteQQuickTumblerPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall17 call = reinterpret_cast<CuteQQuickTumblerPrivateCall17>(taken[17]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall18 call = reinterpret_cast<CuteQQuickTumblerPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall19 call = reinterpret_cast<CuteQQuickTumblerPrivateCall19>(taken[19]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall20 call = reinterpret_cast<CuteQQuickTumblerPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall21 call = reinterpret_cast<CuteQQuickTumblerPrivateCall21>(taken[21]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall22 call = reinterpret_cast<CuteQQuickTumblerPrivateCall22>(taken[22]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemDestroyed(item);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall23 call = reinterpret_cast<CuteQQuickTumblerPrivateCall23>(taken[23]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall24 call = reinterpret_cast<CuteQQuickTumblerPrivateCall24>(taken[24]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall25 call = reinterpret_cast<CuteQQuickTumblerPrivateCall25>(taken[25]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall26 call = reinterpret_cast<CuteQQuickTumblerPrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall27 call = reinterpret_cast<CuteQQuickTumblerPrivateCall27>(taken[27]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall28 call = reinterpret_cast<CuteQQuickTumblerPrivateCall28>(taken[28]);
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
      CuteQQuickTumblerPrivateCall29 call = reinterpret_cast<CuteQQuickTumblerPrivateCall29>(taken[29]);
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
      CuteQQuickTumblerPrivateCall30 call = reinterpret_cast<CuteQQuickTumblerPrivateCall30>(taken[30]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall31 call = reinterpret_cast<CuteQQuickTumblerPrivateCall31>(taken[31]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall32 call = reinterpret_cast<CuteQQuickTumblerPrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall33 call = reinterpret_cast<CuteQQuickTumblerPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall34 call = reinterpret_cast<CuteQQuickTumblerPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall35 call = reinterpret_cast<CuteQQuickTumblerPrivateCall35>(taken[35]);
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
      CuteQQuickTumblerPrivateCall36 call = reinterpret_cast<CuteQQuickTumblerPrivateCall36>(taken[36]);
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
      CuteQQuickTumblerPrivateCall37 call = reinterpret_cast<CuteQQuickTumblerPrivateCall37>(taken[37]);
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
      CuteQQuickTumblerPrivateCall38 call = reinterpret_cast<CuteQQuickTumblerPrivateCall38>(taken[38]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall39 call = reinterpret_cast<CuteQQuickTumblerPrivateCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall40 call = reinterpret_cast<CuteQQuickTumblerPrivateCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTumblerPrivateCall41 call = reinterpret_cast<CuteQQuickTumblerPrivateCall41>(taken[41]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTumbler *QQuickTumblerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTumbler *ritual_ZN20QQuickTumblerPrivate6q_funcEv(
    QQuickTumblerPrivate *self) {
  return self->q_func();
}

//  const QQuickTumbler *QQuickTumblerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTumbler *ritual_ZNK20QQuickTumblerPrivate6q_funcEv(
    const QQuickTumblerPrivate *self) {
  return self->q_func();
}

//  QQuickItem *QQuickTumblerPrivate::determineViewType(QQuickItem
//      *contentItem)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN20QQuickTumblerPrivate17determineViewTypeEP10QQuickItem(
    QQuickTumblerPrivate *self,
    QQuickItem *contentItem) {
  return self->determineViewType(contentItem);
}

//  void QQuickTumblerPrivate::resetViewData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate13resetViewDataEv(
    QQuickTumblerPrivate *self) {
  self->resetViewData();
}

//  QList<QQuickItem *> QQuickTumblerPrivate::viewContentItemChildItems()
//      const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK20QQuickTumblerPrivate25viewContentItemChildItemsEv(
    const QQuickTumblerPrivate *self) {
  return new QList<QQuickItem *>(self->viewContentItemChildItems());
}

//  QQuickTumblerPrivate *QQuickTumblerPrivate::get(QQuickTumbler *tumbler)
extern "C" Q_DECL_EXPORT
QQuickTumblerPrivate *ritual_ZN20QQuickTumblerPrivate3getEP13QQuickTumbler(
    QQuickTumbler *tumbler) {
  return QQuickTumblerPrivate::get(tumbler);
}

//  QPalette QQuickTumblerPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK20QQuickTumblerPrivate14defaultPaletteEv(
    const QQuickTumblerPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  void QQuickTumblerPrivate::_q_updateItemHeights()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate20_q_updateItemHeightsEv(
    QQuickTumblerPrivate *self) {
  self->_q_updateItemHeights();
}

//  void QQuickTumblerPrivate::_q_updateItemWidths()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate19_q_updateItemWidthsEv(
    QQuickTumblerPrivate *self) {
  self->_q_updateItemWidths();
}

//  void QQuickTumblerPrivate::_q_onViewCurrentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate28_q_onViewCurrentIndexChangedEv(
    QQuickTumblerPrivate *self) {
  self->_q_onViewCurrentIndexChanged();
}

//  void QQuickTumblerPrivate::_q_onViewCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate21_q_onViewCountChangedEv(
    QQuickTumblerPrivate *self) {
  self->_q_onViewCountChanged();
}

//  void QQuickTumblerPrivate::_q_onViewOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate22_q_onViewOffsetChangedEv(
    QQuickTumblerPrivate *self) {
  self->_q_onViewOffsetChanged();
}

//  void QQuickTumblerPrivate::_q_onViewContentYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate24_q_onViewContentYChangedEv(
    QQuickTumblerPrivate *self) {
  self->_q_onViewContentYChanged();
}

//  void QQuickTumblerPrivate::calculateDisplacements()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate22calculateDisplacementsEv(
    QQuickTumblerPrivate *self) {
  self->calculateDisplacements();
}

//  void QQuickTumblerPrivate::disconnectFromView()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate18disconnectFromViewEv(
    QQuickTumblerPrivate *self) {
  self->disconnectFromView();
}

//  void QQuickTumblerPrivate::setupViewData(QQuickItem
//      *newControlContentItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate13setupViewDataEP10QQuickItem(
    QQuickTumblerPrivate *self,
    QQuickItem *newControlContentItem) {
  self->setupViewData(newControlContentItem);
}

//  void QQuickTumblerPrivate::warnAboutIncorrectContentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate29warnAboutIncorrectContentItemEv(
    QQuickTumblerPrivate *self) {
  self->warnAboutIncorrectContentItem();
}

//  void QQuickTumblerPrivate::syncCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate16syncCurrentIndexEv(
    QQuickTumblerPrivate *self) {
  self->syncCurrentIndex();
}

//  void QQuickTumblerPrivate::setPendingCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate22setPendingCurrentIndexEi(
    QQuickTumblerPrivate *self,
    int index) {
  self->setPendingCurrentIndex(index);
}

//  QString
//      QQuickTumblerPrivate::propertyChangeReasonToString(PropertyChangeReas
//      on changeReason)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickTumblerPrivate28propertyChangeReasonToStringENS_20PropertyChangeReasonE(
    QQuickTumblerPrivate::PropertyChangeReason changeReason) {
  return new QString(
      QQuickTumblerPrivate::propertyChangeReasonToString(
          changeReason));
}

//  void QQuickTumblerPrivate::setCurrentIndex(int newCurrentIndex,
//      PropertyChangeReason changeReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate15setCurrentIndexEiNS_20PropertyChangeReasonE(
    QQuickTumblerPrivate *self,
    int newCurrentIndex,
    QQuickTumblerPrivate::PropertyChangeReason changeReason) {
  self->setCurrentIndex(newCurrentIndex, changeReason);
}

//  void QQuickTumblerPrivate::setCount(int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate8setCountEi(
    QQuickTumblerPrivate *self,
    int newCount) {
  self->setCount(newCount);
}

//  void QQuickTumblerPrivate::setWrapBasedOnCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate19setWrapBasedOnCountEv(
    QQuickTumblerPrivate *self) {
  self->setWrapBasedOnCount();
}

//  void QQuickTumblerPrivate::setWrap(bool shouldWrap,
//      QQml::PropertyUtils::State propertyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate7setWrapEbN4QQml13PropertyUtils5StateE(
    QQuickTumblerPrivate *self,
    bool shouldWrap,
    QQml::PropertyUtils::State propertyState) {
  self->setWrap(shouldWrap, propertyState);
}

//  qreal QQuickTumblerPrivate::effectiveFlickDeceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickTumblerPrivate26effectiveFlickDecelerationEv(
    const QQuickTumblerPrivate *self) {
  return self->effectiveFlickDeceleration();
}

//  void QQuickTumblerPrivate::beginSetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate13beginSetModelEv(
    QQuickTumblerPrivate *self) {
  self->beginSetModel();
}

//  void QQuickTumblerPrivate::endSetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate11endSetModelEv(
    QQuickTumblerPrivate *self) {
  self->endSetModel();
}

//  void QQuickTumblerPrivate::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildAdded(a0, a1);
}

//  void QQuickTumblerPrivate::itemChildRemoved(QQuickItem *a0, QQuickItem
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickItemS1_(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildRemoved(a0, a1);
}

//  void QQuickTumblerPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTumblerPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  a Python function taken by a CuteQQuickTumblerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTumblerPrivate(
    QQuickTumblerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTumblerPrivate *>(self)->take(key, call);
}

//  QPalette QQuickTumblerPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK20QQuickTumblerPrivate14defaultPaletteEv(
    const QQuickTumblerPrivate *self) {
  return new QPalette(self->QQuickTumblerPrivate::defaultPalette());
}

//  void QQuickTumblerPrivate::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickTumblerPrivate::itemChildAdded(a0, a1);
}

//  void QQuickTumblerPrivate::itemChildRemoved(QQuickItem *a0, QQuickItem
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickItemS1_(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickTumblerPrivate::itemChildRemoved(a0, a1);
}

//  void QQuickTumblerPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickTumblerPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickTumblerPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickTumblerPrivate::itemGeometryChanged(a0, *a1, *a2);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
