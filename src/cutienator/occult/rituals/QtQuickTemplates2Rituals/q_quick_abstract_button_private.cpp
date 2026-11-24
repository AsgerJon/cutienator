//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickAbstractButtonPrivate that Python can take functions over in. Every QQuickAbstractButtonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickAbstractButtonPrivateCall0)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall3)(const void *, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall4)(const void *, int, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall9)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickAbstractButtonPrivateCall10)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractButtonPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall13)(const void *, int *);
typedef void * (*CuteQQuickAbstractButtonPrivateCall14)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractButtonPrivateCall15)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickAbstractButtonPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractButtonPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall19)(const void *, bool, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall20)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall21)(const void *, bool, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall22)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall23)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall24)(const void *, int, int *);
typedef qreal (*CuteQQuickAbstractButtonPrivateCall25)(const void *, int *);
typedef qreal (*CuteQQuickAbstractButtonPrivateCall26)(const void *, int *);
typedef const QPalette * (*CuteQQuickAbstractButtonPrivateCall27)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickAbstractButtonPrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickAbstractButtonPrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickAbstractButtonPrivateCall33)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall34)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickAbstractButtonPrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickAbstractButtonPrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickAbstractButtonPrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickAbstractButtonPrivateCall40)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall41)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonPrivateCall42)(const void *, int, int *);
class CuteQQuickAbstractButtonPrivate : public QQuickAbstractButtonPrivate {
public:
  using QQuickAbstractButtonPrivate::QQuickAbstractButtonPrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
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
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
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

  //  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point,
  //      ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall0 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall0>(taken[0]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
  //      ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall1 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall2 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickAbstractButtonPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall3 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::handleUngrab();
  }

  //  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
  bool acceptKeyClick(Qt::Key key) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall4 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(key), &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::acceptKeyClick(key);
  }

  //  void QQuickAbstractButtonPrivate::accessiblePressAction()
  void accessiblePressAction() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall5 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessiblePressAction();
  }

  //  void QQuickAbstractButtonPrivate::accessibleToggleAction()
  void accessibleToggleAction() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall6 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessibleToggleAction();
  }

  //  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall7 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall8 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall9 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemDestroyed(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall10 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall11 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall12 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall13 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall14 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall14>(taken[14]);
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
      CuteQQuickAbstractButtonPrivateCall15 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall15>(taken[15]);
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
      CuteQQuickAbstractButtonPrivateCall16 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall16>(taken[16]);
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
      CuteQQuickAbstractButtonPrivateCall17 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall18 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall19 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall19>(taken[19]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall20 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall21 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall22 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall22>(taken[22]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall23 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall23>(taken[23]);
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
      CuteQQuickAbstractButtonPrivateCall24 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall24>(taken[24]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall25 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall25>(taken[25]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall26 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall27 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall27>(taken[27]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall28 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall29 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall29>(taken[29]);
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
      CuteQQuickAbstractButtonPrivateCall30 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall30>(taken[30]);
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
      CuteQQuickAbstractButtonPrivateCall31 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall32 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall33 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall34 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall35 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall36 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall36>(taken[36]);
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
      CuteQQuickAbstractButtonPrivateCall37 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall37>(taken[37]);
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
      CuteQQuickAbstractButtonPrivateCall38 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall38>(taken[38]);
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
      CuteQQuickAbstractButtonPrivateCall39 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall40 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall41 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickAbstractButtonPrivateCall42 call = reinterpret_cast<CuteQQuickAbstractButtonPrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickAbstractButton *QQuickAbstractButtonPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZN27QQuickAbstractButtonPrivate6q_funcEv(
    QQuickAbstractButtonPrivate *self) {
  return self->q_func();
}

//  const QQuickAbstractButton *QQuickAbstractButtonPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAbstractButton *ritual_ZNK27QQuickAbstractButtonPrivate6q_funcEv(
    const QQuickAbstractButtonPrivate *self) {
  return self->q_func();
}

//  QQuickAbstractButtonPrivate
//      *QQuickAbstractButtonPrivate::get(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
QQuickAbstractButtonPrivate *ritual_ZN27QQuickAbstractButtonPrivate3getEP20QQuickAbstractButton(
    QQuickAbstractButton *button) {
  return QQuickAbstractButtonPrivate::get(button);
}

//  QPointF QQuickAbstractButtonPrivate::centerPressPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK27QQuickAbstractButtonPrivate16centerPressPointEv(
    const QQuickAbstractButtonPrivate *self) {
  return new QPointF(self->centerPressPoint());
}

//  void QQuickAbstractButtonPrivate::setPressPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate13setPressPointERK7QPointF(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point) {
  self->setPressPoint(*point);
}

//  void QQuickAbstractButtonPrivate::setMovePoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate12setMovePointERK7QPointF(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point) {
  self->setMovePoint(*point);
}

//  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickAbstractButtonPrivate11handlePressERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickAbstractButtonPrivate10handleMoveERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(*point, timestamp);
}

//  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickAbstractButtonPrivate13handleReleaseERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(*point, timestamp);
}

//  void QQuickAbstractButtonPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate12handleUngrabEv(
    QQuickAbstractButtonPrivate *self) {
  self->handleUngrab();
}

//  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE(
    const QQuickAbstractButtonPrivate *self,
    Qt::Key key) {
  return self->acceptKeyClick(key);
}

//  void QQuickAbstractButtonPrivate::accessiblePressAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv(
    QQuickAbstractButtonPrivate *self) {
  self->accessiblePressAction();
}

//  void QQuickAbstractButtonPrivate::accessibleToggleAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv(
    QQuickAbstractButtonPrivate *self) {
  self->accessibleToggleAction();
}

//  bool QQuickAbstractButtonPrivate::isPressAndHoldConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickAbstractButtonPrivate23isPressAndHoldConnectedEv(
    QQuickAbstractButtonPrivate *self) {
  return self->isPressAndHoldConnected();
}

//  bool QQuickAbstractButtonPrivate::isDoubleClickConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickAbstractButtonPrivate22isDoubleClickConnectedEv(
    QQuickAbstractButtonPrivate *self) {
  return self->isDoubleClickConnected();
}

//  void QQuickAbstractButtonPrivate::startPressAndHold()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate17startPressAndHoldEv(
    QQuickAbstractButtonPrivate *self) {
  self->startPressAndHold();
}

//  void QQuickAbstractButtonPrivate::stopPressAndHold()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate16stopPressAndHoldEv(
    QQuickAbstractButtonPrivate *self) {
  self->stopPressAndHold();
}

//  void QQuickAbstractButtonPrivate::startRepeatDelay()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate16startRepeatDelayEv(
    QQuickAbstractButtonPrivate *self) {
  self->startRepeatDelay();
}

//  void QQuickAbstractButtonPrivate::startPressRepeat()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate16startPressRepeatEv(
    QQuickAbstractButtonPrivate *self) {
  self->startPressRepeat();
}

//  void QQuickAbstractButtonPrivate::stopPressRepeat()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate15stopPressRepeatEv(
    QQuickAbstractButtonPrivate *self) {
  self->stopPressRepeat();
}

#if QT_CONFIG(shortcut)
//  void QQuickAbstractButtonPrivate::grabShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate12grabShortcutEv(
    QQuickAbstractButtonPrivate *self) {
  self->grabShortcut();
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QQuickAbstractButtonPrivate::ungrabShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate14ungrabShortcutEv(
    QQuickAbstractButtonPrivate *self) {
  self->ungrabShortcut();
}
#endif  // QT_CONFIG(shortcut)

//  QQuickAbstractButton *QQuickAbstractButtonPrivate::findCheckedButton()
//      const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZNK27QQuickAbstractButtonPrivate17findCheckedButtonEv(
    const QQuickAbstractButtonPrivate *self) {
  return self->findCheckedButton();
}

//  QList<QQuickAbstractButton *>
//      QQuickAbstractButtonPrivate::findExclusiveButtons() const
extern "C" Q_DECL_EXPORT
QList<QQuickAbstractButton *> *ritual_ZNK27QQuickAbstractButtonPrivate20findExclusiveButtonsEv(
    const QQuickAbstractButtonPrivate *self) {
  return new QList<QQuickAbstractButton *>(self->findExclusiveButtons());
}

//  void QQuickAbstractButtonPrivate::actionTextChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate16actionTextChangeEv(
    QQuickAbstractButtonPrivate *self) {
  self->actionTextChange();
}

//  void QQuickAbstractButtonPrivate::setText(const QString &text,
//      QQml::PropertyUtils::State propertyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate7setTextERK7QStringN4QQml13PropertyUtils5StateE(
    QQuickAbstractButtonPrivate *self,
    const QString *text,
    QQml::PropertyUtils::State propertyState) {
  self->setText(*text, propertyState);
}

//  void QQuickAbstractButtonPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate4initEv(
    QQuickAbstractButtonPrivate *self) {
  self->init();
}

//  void QQuickAbstractButtonPrivate::updateEffectiveIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate19updateEffectiveIconEv(
    QQuickAbstractButtonPrivate *self) {
  self->updateEffectiveIcon();
}

//  void QQuickAbstractButtonPrivate::click()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate5clickEv(
    QQuickAbstractButtonPrivate *self) {
  self->click();
}

//  void QQuickAbstractButtonPrivate::trigger(bool doubleClick)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate7triggerEb(
    QQuickAbstractButtonPrivate *self,
    bool doubleClick) {
  self->trigger(doubleClick);
}

//  void QQuickAbstractButtonPrivate::toggle(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate6toggleEb(
    QQuickAbstractButtonPrivate *self,
    bool value) {
  self->toggle(value);
}

//  void QQuickAbstractButtonPrivate::cancelIndicator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate15cancelIndicatorEv(
    QQuickAbstractButtonPrivate *self) {
  self->cancelIndicator();
}

//  void QQuickAbstractButtonPrivate::executeIndicator(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate16executeIndicatorEb(
    QQuickAbstractButtonPrivate *self,
    bool complete) {
  self->executeIndicator(complete);
}

//  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAbstractButtonPrivate13itemDestroyedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  a Python function taken by a CuteQQuickAbstractButtonPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractButtonPrivate(
    QQuickAbstractButtonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractButtonPrivate *>(self)->take(key, call);
}

//  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QQuickAbstractButtonPrivate11handlePressERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractButtonPrivate::handlePress(*point, timestamp);
}

//  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QQuickAbstractButtonPrivate10handleMoveERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractButtonPrivate::handleMove(*point, timestamp);
}

//  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QQuickAbstractButtonPrivate13handleReleaseERK7QPointFm(
    QQuickAbstractButtonPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractButtonPrivate::handleRelease(*point, timestamp);
}

//  void QQuickAbstractButtonPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate12handleUngrabEv(
    QQuickAbstractButtonPrivate *self) {
  self->QQuickAbstractButtonPrivate::handleUngrab();
}

//  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE(
    const QQuickAbstractButtonPrivate *self,
    Qt::Key key) {
  return self->QQuickAbstractButtonPrivate::acceptKeyClick(key);
}

//  void QQuickAbstractButtonPrivate::accessiblePressAction()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv(
    QQuickAbstractButtonPrivate *self) {
  self->QQuickAbstractButtonPrivate::accessiblePressAction();
}

//  void QQuickAbstractButtonPrivate::accessibleToggleAction()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv(
    QQuickAbstractButtonPrivate *self) {
  self->QQuickAbstractButtonPrivate::accessibleToggleAction();
}

//  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->QQuickAbstractButtonPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAbstractButtonPrivate13itemDestroyedEP10QQuickItem(
    QQuickAbstractButtonPrivate *self,
    QQuickItem *item) {
  self->QQuickAbstractButtonPrivate::itemDestroyed(item);
}
