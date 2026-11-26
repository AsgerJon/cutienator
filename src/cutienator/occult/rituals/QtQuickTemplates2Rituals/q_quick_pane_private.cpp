//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtQuick/QQuickItem>

//  A QQuickPanePrivate that Python can take functions over in. Every QQuickPanePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickPanePrivateCall0)(const void *, int *);
typedef void * (*CuteQQuickPanePrivateCall1)(const void *, int *);
typedef qreal (*CuteQQuickPanePrivateCall2)(const void *, int *);
typedef qreal (*CuteQQuickPanePrivateCall3)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPanePrivateCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPanePrivateCall6)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPanePrivateCall7)(const void *, const QPointF *, ulong, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPanePrivateCall8)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPanePrivateCall9)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPanePrivateCall10)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickPanePrivateCall11)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall12)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall13)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall14)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPanePrivateCall15)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPanePrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickPanePrivateCall17)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall18)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall19)(const void *, bool, int *);
typedef void (*CuteQQuickPanePrivateCall20)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall21)(const void *, bool, int *);
typedef void (*CuteQQuickPanePrivateCall22)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickPanePrivateCall23)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickPanePrivateCall24)(const void *, int, int *);
typedef const QPalette * (*CuteQQuickPanePrivateCall25)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPanePrivateCall27)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickPanePrivateCall28)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickPanePrivateCall29)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickPanePrivateCall30)(const void *, int *);
typedef qreal (*CuteQQuickPanePrivateCall31)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall32)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall33)(const void *, int *);
typedef bool (*CuteQQuickPanePrivateCall34)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPanePrivateCall35)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickPanePrivateCall36)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickPanePrivateCall37)(const void *, bool, int *);
typedef void * (*CuteQQuickPanePrivateCall38)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall39)(const void *, int *);
typedef void (*CuteQQuickPanePrivateCall40)(const void *, int, int *);
class CuteQQuickPanePrivate : public QQuickPanePrivate {
public:
  using QQuickPanePrivate::QQuickPanePrivate;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QQuickPanePrivate13getFirstChildEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[11] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[35] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[40] = call;
      return true;
    }
    return false;
  }

  //  QQuickItem *QQuickPanePrivate::getFirstChild() const
  QQuickItem *getFirstChild() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPanePrivateCall0 call = reinterpret_cast<CuteQQuickPanePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPanePrivate::getFirstChild();
  }

  //  QQuickItem *QQuickPanePrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPanePrivateCall1 call = reinterpret_cast<CuteQQuickPanePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPanePrivate::getContentItem();
  }

  //  qreal QQuickPanePrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPanePrivateCall2 call = reinterpret_cast<CuteQQuickPanePrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentWidth();
  }

  //  qreal QQuickPanePrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPanePrivateCall3 call = reinterpret_cast<CuteQQuickPanePrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::getContentHeight();
  }

  //  void QQuickPanePrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPanePrivateCall4 call = reinterpret_cast<CuteQQuickPanePrivateCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPanePrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickPanePrivate::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPanePrivateCall5 call = reinterpret_cast<CuteQQuickPanePrivateCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPanePrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickPanePrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPanePrivateCall6 call = reinterpret_cast<CuteQQuickPanePrivateCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPanePrivate::itemDestroyed(item);
  }

  //  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPanePrivateCall7 call = reinterpret_cast<CuteQQuickPanePrivateCall7>(taken[7]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPanePrivate::handlePress(point, timestamp);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPanePrivateCall8 call = reinterpret_cast<CuteQQuickPanePrivateCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPanePrivateCall9 call = reinterpret_cast<CuteQQuickPanePrivateCall9>(taken[9]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPanePrivateCall10 call = reinterpret_cast<CuteQQuickPanePrivateCall10>(taken[10]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPanePrivateCall11 call = reinterpret_cast<CuteQQuickPanePrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPanePrivateCall12 call = reinterpret_cast<CuteQQuickPanePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPanePrivateCall13 call = reinterpret_cast<CuteQQuickPanePrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPanePrivateCall14 call = reinterpret_cast<CuteQQuickPanePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPanePrivateCall15 call = reinterpret_cast<CuteQQuickPanePrivateCall15>(taken[15]);
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
      CuteQQuickPanePrivateCall16 call = reinterpret_cast<CuteQQuickPanePrivateCall16>(taken[16]);
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
      CuteQQuickPanePrivateCall17 call = reinterpret_cast<CuteQQuickPanePrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPanePrivateCall18 call = reinterpret_cast<CuteQQuickPanePrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPanePrivateCall19 call = reinterpret_cast<CuteQQuickPanePrivateCall19>(taken[19]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPanePrivateCall20 call = reinterpret_cast<CuteQQuickPanePrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPanePrivateCall21 call = reinterpret_cast<CuteQQuickPanePrivateCall21>(taken[21]);
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
      CuteQQuickPanePrivateCall22 call = reinterpret_cast<CuteQQuickPanePrivateCall22>(taken[22]);
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
      CuteQQuickPanePrivateCall23 call = reinterpret_cast<CuteQQuickPanePrivateCall23>(taken[23]);
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
      CuteQQuickPanePrivateCall24 call = reinterpret_cast<CuteQQuickPanePrivateCall24>(taken[24]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPanePrivateCall25 call = reinterpret_cast<CuteQQuickPanePrivateCall25>(taken[25]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPanePrivateCall26 call = reinterpret_cast<CuteQQuickPanePrivateCall26>(taken[26]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPanePrivateCall27 call = reinterpret_cast<CuteQQuickPanePrivateCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPanePrivateCall28 call = reinterpret_cast<CuteQQuickPanePrivateCall28>(taken[28]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPanePrivateCall29 call = reinterpret_cast<CuteQQuickPanePrivateCall29>(taken[29]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPanePrivateCall30 call = reinterpret_cast<CuteQQuickPanePrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPanePrivateCall31 call = reinterpret_cast<CuteQQuickPanePrivateCall31>(taken[31]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickPanePrivateCall32 call = reinterpret_cast<CuteQQuickPanePrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPanePrivateCall33 call = reinterpret_cast<CuteQQuickPanePrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPanePrivateCall34 call = reinterpret_cast<CuteQQuickPanePrivateCall34>(taken[34]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPanePrivateCall35 call = reinterpret_cast<CuteQQuickPanePrivateCall35>(taken[35]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPanePrivateCall36 call = reinterpret_cast<CuteQQuickPanePrivateCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPanePrivateCall37 call = reinterpret_cast<CuteQQuickPanePrivateCall37>(taken[37]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickPanePrivateCall38 call = reinterpret_cast<CuteQQuickPanePrivateCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickPanePrivateCall39 call = reinterpret_cast<CuteQQuickPanePrivateCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickPanePrivateCall40 call = reinterpret_cast<CuteQQuickPanePrivateCall40>(taken[40]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickPane *QQuickPanePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPane *ritual_ZN17QQuickPanePrivate6q_funcEv(QQuickPanePrivate *self) {
  return self->q_func();
}

//  const QQuickPane *QQuickPanePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPane *ritual_ZNK17QQuickPanePrivate6q_funcEv(
    const QQuickPanePrivate *self) {
  return self->q_func();
}

//  void QQuickPanePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate4initEv(QQuickPanePrivate *self) {
  self->init();
}

//  QQmlListProperty<QObject> QQuickPanePrivate::contentData()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN17QQuickPanePrivate11contentDataEv(
    QQuickPanePrivate *self) {
  return new QQmlListProperty<QObject>(self->contentData());
}

//  QQmlListProperty<QQuickItem> QQuickPanePrivate::contentChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickItem> *ritual_ZN17QQuickPanePrivate15contentChildrenEv(
    QQuickPanePrivate *self) {
  return new QQmlListProperty<QQuickItem>(self->contentChildren());
}

//  QList<QQuickItem *> QQuickPanePrivate::contentChildItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK17QQuickPanePrivate17contentChildItemsEv(
    const QQuickPanePrivate *self) {
  return new QList<QQuickItem *>(self->contentChildItems());
}

//  QQuickItem *QQuickPanePrivate::getFirstChild() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickPanePrivate13getFirstChildEv(
    const QQuickPanePrivate *self) {
  return self->getFirstChild();
}

//  QQuickItem *QQuickPanePrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickPanePrivate14getContentItemEv(
    QQuickPanePrivate *self) {
  return self->getContentItem();
}

//  qreal QQuickPanePrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickPanePrivate15getContentWidthEv(
    const QQuickPanePrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickPanePrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickPanePrivate16getContentHeightEv(
    const QQuickPanePrivate *self) {
  return self->getContentHeight();
}

//  void QQuickPanePrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickPanePrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickPanePrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate13itemDestroyedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickPanePrivate::contentChildrenChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate21contentChildrenChangeEv(
    QQuickPanePrivate *self) {
  self->contentChildrenChange();
}

//  void QQuickPanePrivate::updateContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate18updateContentWidthEv(
    QQuickPanePrivate *self) {
  self->updateContentWidth();
}

//  void QQuickPanePrivate::updateContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPanePrivate19updateContentHeightEv(
    QQuickPanePrivate *self) {
  self->updateContentHeight();
}

//  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickPanePrivate11handlePressERK7QPointFm(
    QQuickPanePrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  a Python function taken by a CuteQQuickPanePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPanePrivate(
    QQuickPanePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPanePrivate *>(self)->take(key, call);
}

//  QQuickItem *QQuickPanePrivate::getFirstChild() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZNK17QQuickPanePrivate13getFirstChildEv(
    const QQuickPanePrivate *self) {
  return self->QQuickPanePrivate::getFirstChild();
}

//  QQuickItem *QQuickPanePrivate::getContentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN17QQuickPanePrivate14getContentItemEv(
    QQuickPanePrivate *self) {
  return self->QQuickPanePrivate::getContentItem();
}

//  qreal QQuickPanePrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickPanePrivate15getContentWidthEv(
    const QQuickPanePrivate *self) {
  return self->QQuickPanePrivate::getContentWidth();
}

//  qreal QQuickPanePrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickPanePrivate16getContentHeightEv(
    const QQuickPanePrivate *self) {
  return self->QQuickPanePrivate::getContentHeight();
}

//  void QQuickPanePrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPanePrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->QQuickPanePrivate::itemImplicitWidthChanged(item);
}

//  void QQuickPanePrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPanePrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->QQuickPanePrivate::itemImplicitHeightChanged(item);
}

//  void QQuickPanePrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPanePrivate13itemDestroyedEP10QQuickItem(
    QQuickPanePrivate *self,
    QQuickItem *item) {
  self->QQuickPanePrivate::itemDestroyed(item);
}

//  bool QQuickPanePrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickPanePrivate11handlePressERK7QPointFm(
    QQuickPanePrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickPanePrivate::handlePress(*point, timestamp);
}

//  a QQmlListProperty<QObject> a ritual of QQuickPanePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPanePrivate__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<QQuickItem> a ritual of QQuickPanePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPanePrivate__QQmlListProperty_QQuickItem(
    QQmlListProperty<QQuickItem> *self) {
  delete self;
}
