//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickControlPrivate that Python can take functions over in. Every QQuickControlPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickControlPrivateCall0)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickControlPrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickControlPrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickControlPrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickControlPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall7)(const void *, int *);
typedef void * (*CuteQQuickControlPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickControlPrivateCall9)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickControlPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickControlPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall13)(const void *, bool, int *);
typedef void (*CuteQQuickControlPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall15)(const void *, bool, int *);
typedef void (*CuteQQuickControlPrivateCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickControlPrivateCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickControlPrivateCall18)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickControlPrivateCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickControlPrivateCall20)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickControlPrivateCall21)(const void *, int, int *);
typedef qreal (*CuteQQuickControlPrivateCall22)(const void *, int *);
typedef qreal (*CuteQQuickControlPrivateCall23)(const void *, int *);
typedef const QPalette * (*CuteQQuickControlPrivateCall24)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall25)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickControlPrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickControlPrivateCall27)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickControlPrivateCall28)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickControlPrivateCall29)(const void *, int *);
typedef qreal (*CuteQQuickControlPrivateCall30)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall31)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall32)(const void *, int *);
typedef bool (*CuteQQuickControlPrivateCall33)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickControlPrivateCall34)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickControlPrivateCall35)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickControlPrivateCall36)(const void *, bool, int *);
typedef void * (*CuteQQuickControlPrivateCall37)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickControlPrivateCall39)(const void *, int, int *);
class CuteQQuickControlPrivate : public QQuickControlPrivate {
public:
  using QQuickControlPrivate::QQuickControlPrivate;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
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
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
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

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickControlPrivateCall0 call = reinterpret_cast<CuteQQuickControlPrivateCall0>(taken[0]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickControlPrivateCall1 call = reinterpret_cast<CuteQQuickControlPrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickControlPrivateCall2 call = reinterpret_cast<CuteQQuickControlPrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickControlPrivateCall3 call = reinterpret_cast<CuteQQuickControlPrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickControlPrivateCall4 call = reinterpret_cast<CuteQQuickControlPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickControlPrivateCall5 call = reinterpret_cast<CuteQQuickControlPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickControlPrivateCall6 call = reinterpret_cast<CuteQQuickControlPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickControlPrivateCall7 call = reinterpret_cast<CuteQQuickControlPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickControlPrivateCall8 call = reinterpret_cast<CuteQQuickControlPrivateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickControlPrivateCall9 call = reinterpret_cast<CuteQQuickControlPrivateCall9>(taken[9]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickControlPrivateCall10 call = reinterpret_cast<CuteQQuickControlPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickControlPrivateCall11 call = reinterpret_cast<CuteQQuickControlPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickControlPrivateCall12 call = reinterpret_cast<CuteQQuickControlPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickControlPrivateCall13 call = reinterpret_cast<CuteQQuickControlPrivateCall13>(taken[13]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickControlPrivateCall14 call = reinterpret_cast<CuteQQuickControlPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickControlPrivateCall15 call = reinterpret_cast<CuteQQuickControlPrivateCall15>(taken[15]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickControlPrivateCall16 call = reinterpret_cast<CuteQQuickControlPrivateCall16>(taken[16]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickControlPrivateCall17 call = reinterpret_cast<CuteQQuickControlPrivateCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQQuickControlPrivateCall18 call = reinterpret_cast<CuteQQuickControlPrivateCall18>(taken[18]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickControlPrivateCall19 call = reinterpret_cast<CuteQQuickControlPrivateCall19>(taken[19]);
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
      CuteQQuickControlPrivateCall20 call = reinterpret_cast<CuteQQuickControlPrivateCall20>(taken[20]);
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
      CuteQQuickControlPrivateCall21 call = reinterpret_cast<CuteQQuickControlPrivateCall21>(taken[21]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickControlPrivateCall22 call = reinterpret_cast<CuteQQuickControlPrivateCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickControlPrivateCall23 call = reinterpret_cast<CuteQQuickControlPrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickControlPrivateCall24 call = reinterpret_cast<CuteQQuickControlPrivateCall24>(taken[24]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickControlPrivateCall25 call = reinterpret_cast<CuteQQuickControlPrivateCall25>(taken[25]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickControlPrivateCall26 call = reinterpret_cast<CuteQQuickControlPrivateCall26>(taken[26]);
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
      CuteQQuickControlPrivateCall27 call = reinterpret_cast<CuteQQuickControlPrivateCall27>(taken[27]);
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
      CuteQQuickControlPrivateCall28 call = reinterpret_cast<CuteQQuickControlPrivateCall28>(taken[28]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickControlPrivateCall29 call = reinterpret_cast<CuteQQuickControlPrivateCall29>(taken[29]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickControlPrivateCall30 call = reinterpret_cast<CuteQQuickControlPrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickControlPrivateCall31 call = reinterpret_cast<CuteQQuickControlPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickControlPrivateCall32 call = reinterpret_cast<CuteQQuickControlPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickControlPrivateCall33 call = reinterpret_cast<CuteQQuickControlPrivateCall33>(taken[33]);
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
      CuteQQuickControlPrivateCall34 call = reinterpret_cast<CuteQQuickControlPrivateCall34>(taken[34]);
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
      CuteQQuickControlPrivateCall35 call = reinterpret_cast<CuteQQuickControlPrivateCall35>(taken[35]);
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
      CuteQQuickControlPrivateCall36 call = reinterpret_cast<CuteQQuickControlPrivateCall36>(taken[36]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickControlPrivateCall37 call = reinterpret_cast<CuteQQuickControlPrivateCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickControlPrivateCall38 call = reinterpret_cast<CuteQQuickControlPrivateCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickControlPrivateCall39 call = reinterpret_cast<CuteQQuickControlPrivateCall39>(taken[39]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickControl *QQuickControlPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickControl *ritual_ZN20QQuickControlPrivate6q_funcEv(
    QQuickControlPrivate *self) {
  return self->q_func();
}

//  const QQuickControl *QQuickControlPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickControl *ritual_ZNK20QQuickControlPrivate6q_funcEv(
    const QQuickControlPrivate *self) {
  return self->q_func();
}

//  QQuickControlPrivate::QQuickControlPrivate()
extern "C" Q_DECL_EXPORT
QQuickControlPrivate *ritual_ZN20QQuickControlPrivateC1Ev() {
  return new CuteQQuickControlPrivate();
}

//  QQuickControlPrivate::~QQuickControlPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivateD1Ev(QQuickControlPrivate *self) {
  delete self;
}

//  QQuickControlPrivate *QQuickControlPrivate::get(QQuickControl *control)
extern "C" Q_DECL_EXPORT
QQuickControlPrivate *ritual_ZN20QQuickControlPrivate3getEP13QQuickControl(
    QQuickControl *control) {
  return QQuickControlPrivate::get(control);
}

//  void QQuickControlPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate4initEv(QQuickControlPrivate *self) {
  self->init();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint(
    QQuickControlPrivate *self,
    const QEventPoint *point) {
  return self->acceptTouch(*point);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate11handlePressERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate10handleMoveERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(*point, timestamp);
}

//  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(*point, timestamp);
}

//  void QQuickControlPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate12handleUngrabEv(
    QQuickControlPrivate *self) {
  self->handleUngrab();
}

//  void QQuickControlPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate12mirrorChangeEv(
    QQuickControlPrivate *self) {
  self->mirrorChange();
}

//  QMarginsF QQuickControlPrivate::getPadding() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QQuickControlPrivate10getPaddingEv(
    const QQuickControlPrivate *self) {
  return new QMarginsF(self->getPadding());
}

//  qreal QQuickControlPrivate::getTopPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate13getTopPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getTopPadding();
}

//  qreal QQuickControlPrivate::getLeftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate14getLeftPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getLeftPadding();
}

//  qreal QQuickControlPrivate::getRightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate15getRightPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getRightPadding();
}

//  qreal QQuickControlPrivate::getBottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate16getBottomPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getBottomPadding();
}

//  qreal QQuickControlPrivate::getHorizontalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate20getHorizontalPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getHorizontalPadding();
}

//  qreal QQuickControlPrivate::getVerticalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate18getVerticalPaddingEv(
    const QQuickControlPrivate *self) {
  return self->getVerticalPadding();
}

//  void QQuickControlPrivate::setTopPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate13setTopPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setTopPadding(value, reset);
}

//  void QQuickControlPrivate::setLeftPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate14setLeftPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftPadding(value, reset);
}

//  void QQuickControlPrivate::setRightPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate15setRightPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setRightPadding(value, reset);
}

//  void QQuickControlPrivate::setBottomPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate16setBottomPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomPadding(value, reset);
}

//  void QQuickControlPrivate::setHorizontalPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate20setHorizontalPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setHorizontalPadding(value, reset);
}

//  void QQuickControlPrivate::setVerticalPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate18setVerticalPaddingEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setVerticalPadding(value, reset);
}

//  QMarginsF QQuickControlPrivate::getInset() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QQuickControlPrivate8getInsetEv(
    const QQuickControlPrivate *self) {
  return new QMarginsF(self->getInset());
}

//  qreal QQuickControlPrivate::getTopInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate11getTopInsetEv(
    const QQuickControlPrivate *self) {
  return self->getTopInset();
}

//  qreal QQuickControlPrivate::getLeftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate12getLeftInsetEv(
    const QQuickControlPrivate *self) {
  return self->getLeftInset();
}

//  qreal QQuickControlPrivate::getRightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate13getRightInsetEv(
    const QQuickControlPrivate *self) {
  return self->getRightInset();
}

//  qreal QQuickControlPrivate::getBottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate14getBottomInsetEv(
    const QQuickControlPrivate *self) {
  return self->getBottomInset();
}

//  void QQuickControlPrivate::setTopInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate11setTopInsetEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setTopInset(value, reset);
}

//  void QQuickControlPrivate::setLeftInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate12setLeftInsetEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftInset(value, reset);
}

//  void QQuickControlPrivate::setRightInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate13setRightInsetEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setRightInset(value, reset);
}

//  void QQuickControlPrivate::setBottomInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate14setBottomInsetEdb(
    QQuickControlPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomInset(value, reset);
}

//  void QQuickControlPrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate16resizeBackgroundEv(
    QQuickControlPrivate *self) {
  self->resizeBackground();
}

//  void QQuickControlPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate13resizeContentEv(
    QQuickControlPrivate *self) {
  self->resizeContent();
}

//  QQuickItem *QQuickControlPrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN20QQuickControlPrivate14getContentItemEv(
    QQuickControlPrivate *self) {
  return self->getContentItem();
}

//  void QQuickControlPrivate::setContentItem_helper(QQuickItem *item, bool
//      notify)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate21setContentItem_helperEP10QQuickItemb(
    QQuickControlPrivate *self,
    QQuickItem *item,
    bool notify) {
  self->setContentItem_helper(item, notify);
}

#if QT_CONFIG(accessibility)
//  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate26accessibilityActiveChangedEb(
    QQuickControlPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickControlPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QQuickControlPrivate14accessibleRoleEv(
    const QQuickControlPrivate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QQuickAccessibleAttached *QQuickControlPrivate::accessibleAttached(const
//      QObject *object)
extern "C" Q_DECL_EXPORT
QQuickAccessibleAttached *ritual_ZN20QQuickControlPrivate18accessibleAttachedEPK7QObject(
    const QObject *object) {
  return QQuickControlPrivate::accessibleAttached(object);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickControlPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate11resolveFontEv(
    QQuickControlPrivate *self) {
  self->resolveFont();
}

//  void QQuickControlPrivate::inheritFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate11inheritFontERK5QFont(
    QQuickControlPrivate *self,
    const QFont *font) {
  self->inheritFont(*font);
}

//  void QQuickControlPrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate10updateFontERK5QFont(
    QQuickControlPrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  void QQuickControlPrivate::updateFontRecur(QQuickItem *item, const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate15updateFontRecurEP10QQuickItemRK5QFont(
    QQuickItem *item,
    const QFont *font) {
  QQuickControlPrivate::updateFontRecur(item, *font);
}

//  void QQuickControlPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate14setFont_helperERK5QFont(
    QQuickControlPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

//  QFont QQuickControlPrivate::parentFont(const QQuickItem *item)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN20QQuickControlPrivate10parentFontEPK10QQuickItem(
    const QQuickItem *item) {
  return new QFont(QQuickControlPrivate::parentFont(item));
}

//  void QQuickControlPrivate::updateLocale(const QLocale &l, bool e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate12updateLocaleERK7QLocaleb(
    QQuickControlPrivate *self,
    const QLocale *l,
    bool e) {
  self->updateLocale(*l, e);
}

//  void QQuickControlPrivate::updateLocaleRecur(QQuickItem *item, const
//      QLocale &l)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate17updateLocaleRecurEP10QQuickItemRK7QLocale(
    QQuickItem *item,
    const QLocale *l) {
  QQuickControlPrivate::updateLocaleRecur(item, *l);
}

//  QLocale QQuickControlPrivate::calcLocale(const QQuickItem *item)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN20QQuickControlPrivate10calcLocaleEPK10QQuickItem(
    const QQuickItem *item) {
  return new QLocale(QQuickControlPrivate::calcLocale(item));
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControlPrivate::updateHoverEnabled(bool enabled, bool xplicit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate18updateHoverEnabledEbb(
    QQuickControlPrivate *self,
    bool enabled,
    bool xplicit) {
  self->updateHoverEnabled(enabled, xplicit);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControlPrivate::updateHoverEnabledRecur(QQuickItem *item, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate23updateHoverEnabledRecurEP10QQuickItemb(
    QQuickItem *item,
    bool enabled) {
  QQuickControlPrivate::updateHoverEnabledRecur(item, enabled);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  bool QQuickControlPrivate::calcHoverEnabled(const QQuickItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate16calcHoverEnabledEPK10QQuickItem(
    const QQuickItem *item) {
  return QQuickControlPrivate::calcHoverEnabled(item);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickControlPrivate::warnIfCustomizationNotSupported(QObject
//      *control, QQuickItem *item, const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate31warnIfCustomizationNotSupportedEP7QObjectP10QQuickItemRK7QString(
    QObject *control,
    QQuickItem *item,
    const QString *propertyName) {
  QQuickControlPrivate::warnIfCustomizationNotSupported(
      control,
      item,
      *propertyName);
}

//  void QQuickControlPrivate::cancelContentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate17cancelContentItemEv(
    QQuickControlPrivate *self) {
  self->cancelContentItem();
}

//  void QQuickControlPrivate::executeContentItem(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate18executeContentItemEb(
    QQuickControlPrivate *self,
    bool complete) {
  self->executeContentItem(complete);
}

//  void QQuickControlPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate16cancelBackgroundEv(
    QQuickControlPrivate *self) {
  self->cancelBackground();
}

//  void QQuickControlPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate17executeBackgroundEb(
    QQuickControlPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  void QQuickControlPrivate::hideOldItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate11hideOldItemEP10QQuickItem(
    QQuickItem *item) {
  QQuickControlPrivate::hideOldItem(item);
}

//  void QQuickControlPrivate::unhideOldItem(QQuickControl *control,
//      QQuickItem *item, UnhideVisibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate13unhideOldItemEP13QQuickControlP10QQuickItemNS_16UnhideVisibilityE(
    QQuickControl *control,
    QQuickItem *item,
    QQuickControlPrivate::UnhideVisibility visibility) {
  QQuickControlPrivate::unhideOldItem(control, item, visibility);
}

//  void QQuickControlPrivate::updateBaselineOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate20updateBaselineOffsetEv(
    QQuickControlPrivate *self) {
  self->updateBaselineOffset();
}

//  void QQuickControlPrivate::addImplicitSizeListener(QQuickItem *item,
//      ChangeTypes changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate23addImplicitSizeListenerEP10QQuickItem6QFlagsIN17QQuickItemPrivate10ChangeTypeEE(
    QQuickControlPrivate *self,
    QQuickItem *item,
    int changes) {
  self->addImplicitSizeListener(
      item,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(changes));
}

//  void QQuickControlPrivate::removeImplicitSizeListener(QQuickItem *item,
//      ChangeTypes changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate26removeImplicitSizeListenerEP10QQuickItem6QFlagsIN17QQuickItemPrivate10ChangeTypeEE(
    QQuickControlPrivate *self,
    QQuickItem *item,
    int changes) {
  self->removeImplicitSizeListener(
      item,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(changes));
}

//  void QQuickControlPrivate::addImplicitSizeListener(QQuickItem *item,
//      QQuickItemChangeListener *listener, ChangeTypes changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate23addImplicitSizeListenerEP10QQuickItemP24QQuickItemChangeListener6QFlagsIN17QQuickItemPrivate10ChangeTypeEE(
    QQuickItem *item,
    QQuickItemChangeListener *listener,
    int changes) {
  QQuickControlPrivate::addImplicitSizeListener(
      item,
      listener,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(changes));
}

//  void QQuickControlPrivate::removeImplicitSizeListener(QQuickItem *item,
//      QQuickItemChangeListener *listener, ChangeTypes changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate26removeImplicitSizeListenerEP10QQuickItemP24QQuickItemChangeListener6QFlagsIN17QQuickItemPrivate10ChangeTypeEE(
    QQuickItem *item,
    QQuickItemChangeListener *listener,
    int changes) {
  QQuickControlPrivate::removeImplicitSizeListener(
      item,
      listener,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(changes));
}

//  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickControlPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
//      Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE(
    QQuickControlPrivate *self,
    QQuickItem *item,
    Qt::FocusReason reason) {
  self->itemFocusChanged(item, reason);
}

//  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickControlPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickControlPrivate *self,
    Qt::FocusReason a0) {
  return self->setLastFocusChangeReason(a0);
}

//  qreal QQuickControlPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate15getContentWidthEv(
    const QQuickControlPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickControlPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickControlPrivate16getContentHeightEv(
    const QQuickControlPrivate *self) {
  return self->getContentHeight();
}

//  void QQuickControlPrivate::updateImplicitContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate26updateImplicitContentWidthEv(
    QQuickControlPrivate *self) {
  self->updateImplicitContentWidth();
}

//  void QQuickControlPrivate::updateImplicitContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate27updateImplicitContentHeightEv(
    QQuickControlPrivate *self) {
  self->updateImplicitContentHeight();
}

//  void QQuickControlPrivate::updateImplicitContentSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickControlPrivate25updateImplicitContentSizeEv(
    QQuickControlPrivate *self) {
  self->updateImplicitContentSize();
}

//  QPalette QQuickControlPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK20QQuickControlPrivate14defaultPaletteEv(
    const QQuickControlPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  QQuickControlPrivate as the QAccessible::ActivationObserver it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessible::ActivationObserver *ritual_cast_QQuickControlPrivate_QAccessible_ActivationObserver(
    QQuickControlPrivate *self) {
  return static_cast<QAccessible::ActivationObserver *>(self);
}

//  a Python function taken by a CuteQQuickControlPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickControlPrivate(
    QQuickControlPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickControlPrivate *>(self)->take(key, call);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint(
    QQuickControlPrivate *self,
    const QEventPoint *point) {
  return self->QQuickControlPrivate::acceptTouch(*point);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickControlPrivate11handlePressERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickControlPrivate::handlePress(*point, timestamp);
}

//  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickControlPrivate10handleMoveERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickControlPrivate::handleMove(*point, timestamp);
}

//  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm(
    QQuickControlPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickControlPrivate::handleRelease(*point, timestamp);
}

//  void QQuickControlPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate12handleUngrabEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::handleUngrab();
}

//  void QQuickControlPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate12mirrorChangeEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::mirrorChange();
}

//  void QQuickControlPrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate16resizeBackgroundEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::resizeBackground();
}

//  void QQuickControlPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate13resizeContentEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::resizeContent();
}

//  QQuickItem *QQuickControlPrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN20QQuickControlPrivate14getContentItemEv(
    QQuickControlPrivate *self) {
  return self->QQuickControlPrivate::getContentItem();
}

#if QT_CONFIG(accessibility)
//  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate26accessibilityActiveChangedEb(
    QQuickControlPrivate *self,
    bool active) {
  self->QQuickControlPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickControlPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK20QQuickControlPrivate14accessibleRoleEv(
    const QQuickControlPrivate *self) {
  return self->QQuickControlPrivate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickControlPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate11resolveFontEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::resolveFont();
}

//  void QQuickControlPrivate::cancelContentItem()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate17cancelContentItemEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::cancelContentItem();
}

//  void QQuickControlPrivate::executeContentItem(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate18executeContentItemEb(
    QQuickControlPrivate *self,
    bool complete) {
  self->QQuickControlPrivate::executeContentItem(complete);
}

//  void QQuickControlPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate16cancelBackgroundEv(
    QQuickControlPrivate *self) {
  self->QQuickControlPrivate::cancelBackground();
}

//  void QQuickControlPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate17executeBackgroundEb(
    QQuickControlPrivate *self,
    bool complete) {
  self->QQuickControlPrivate::executeBackground(complete);
}

//  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->QQuickControlPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->QQuickControlPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickControlPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickControlPrivate::itemGeometryChanged(item, *change, *diff);
}

//  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem(
    QQuickControlPrivate *self,
    QQuickItem *item) {
  self->QQuickControlPrivate::itemDestroyed(item);
}

//  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
//      Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE(
    QQuickControlPrivate *self,
    QQuickItem *item,
    Qt::FocusReason reason) {
  self->QQuickControlPrivate::itemFocusChanged(item, reason);
}

//  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickControlPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickControlPrivate *self,
    Qt::FocusReason a0) {
  return self->QQuickControlPrivate::setLastFocusChangeReason(a0);
}

//  qreal QQuickControlPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickControlPrivate15getContentWidthEv(
    const QQuickControlPrivate *self) {
  return self->QQuickControlPrivate::getContentWidth();
}

//  qreal QQuickControlPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickControlPrivate16getContentHeightEv(
    const QQuickControlPrivate *self) {
  return self->QQuickControlPrivate::getContentHeight();
}

//  QPalette QQuickControlPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK20QQuickControlPrivate14defaultPaletteEv(
    const QQuickControlPrivate *self) {
  return new QPalette(self->QQuickControlPrivate::defaultPalette());
}
