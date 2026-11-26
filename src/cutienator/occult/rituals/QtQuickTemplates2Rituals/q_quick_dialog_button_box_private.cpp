//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickDialogButtonBoxPrivate that Python can take functions over in. Every QQuickDialogButtonBoxPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickDialogButtonBoxPrivateCall0)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall2)(const void *, int *);
typedef qreal (*CuteQQuickDialogButtonBoxPrivateCall3)(const void *, int *);
typedef qreal (*CuteQQuickDialogButtonBoxPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall5)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall7)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall8)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall9)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall10)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall11)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall12)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall15)(const void *, int *);
typedef void * (*CuteQQuickDialogButtonBoxPrivateCall16)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickDialogButtonBoxPrivateCall17)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickDialogButtonBoxPrivateCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickDialogButtonBoxPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall20)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall21)(const void *, bool, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall23)(const void *, bool, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall24)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall25)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall26)(const void *, int, int *);
typedef const QPalette * (*CuteQQuickDialogButtonBoxPrivateCall27)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickDialogButtonBoxPrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickDialogButtonBoxPrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickDialogButtonBoxPrivateCall33)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall34)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickDialogButtonBoxPrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickDialogButtonBoxPrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickDialogButtonBoxPrivateCall40)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall41)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxPrivateCall42)(const void *, int, int *);
class CuteQQuickDialogButtonBoxPrivate : public QQuickDialogButtonBoxPrivate {
public:
  using QQuickDialogButtonBoxPrivate::QQuickDialogButtonBoxPrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate14itemChildAddedEP10QQuickItemS1_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickContainerPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
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

  //  void
  //      QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall0 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(QQuickIte
  //      m *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall1 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickDialogButtonBoxPrivate::resizeContent()
  void resizeContent() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall2 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBoxPrivate::resizeContent();
  }

  //  qreal QQuickDialogButtonBoxPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall3 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickDialogButtonBoxPrivate::getContentWidth();
  }

  //  qreal QQuickDialogButtonBoxPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall4 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickDialogButtonBoxPrivate::getContentHeight();
  }

  //  void QQuickContainerPrivate::itemChildAdded(QQuickItem *item,
  //      QQuickItem *child)
  void itemChildAdded(QQuickItem *item, QQuickItem *child) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall5 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall5>(taken[5]);
      call(this, item, child, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemChildAdded(item, child);
  }

  //  void QQuickContainerPrivate::itemSiblingOrderChanged(QQuickItem
  //      *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall6 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemSiblingOrderChanged(item);
  }

  //  void QQuickContainerPrivate::itemParentChanged(QQuickItem *item,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall7 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall7>(taken[7]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemParentChanged(item, parent);
  }

  //  void QQuickContainerPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall8 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickContainerPrivate::itemDestroyed(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall9 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall10 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall10>(taken[10]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall11 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall11>(taken[11]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall12 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall12>(taken[12]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall13 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall14 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall15 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall16 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall17 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall17>(taken[17]);
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
      CuteQQuickDialogButtonBoxPrivateCall18 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall18>(taken[18]);
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
      CuteQQuickDialogButtonBoxPrivateCall19 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall20 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall21 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall21>(taken[21]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall22 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall23 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall24 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall24>(taken[24]);
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
      CuteQQuickDialogButtonBoxPrivateCall25 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall25>(taken[25]);
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
      CuteQQuickDialogButtonBoxPrivateCall26 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall26>(taken[26]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall27 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall27>(taken[27]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall28 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall29 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall29>(taken[29]);
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
      CuteQQuickDialogButtonBoxPrivateCall30 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall30>(taken[30]);
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
      CuteQQuickDialogButtonBoxPrivateCall31 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall32 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall33 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall34 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall35 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall36 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall36>(taken[36]);
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
      CuteQQuickDialogButtonBoxPrivateCall37 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall37>(taken[37]);
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
      CuteQQuickDialogButtonBoxPrivateCall38 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall38>(taken[38]);
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
      CuteQQuickDialogButtonBoxPrivateCall39 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall40 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall41 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxPrivateCall42 call = reinterpret_cast<CuteQQuickDialogButtonBoxPrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickDialogButtonBox *QQuickDialogButtonBoxPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZN28QQuickDialogButtonBoxPrivate6q_funcEv(
    QQuickDialogButtonBoxPrivate *self) {
  return self->q_func();
}

//  const QQuickDialogButtonBox *QQuickDialogButtonBoxPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialogButtonBox *ritual_ZNK28QQuickDialogButtonBoxPrivate6q_funcEv(
    const QQuickDialogButtonBoxPrivate *self) {
  return self->q_func();
}

//  QQuickDialogButtonBoxPrivate
//      *QQuickDialogButtonBoxPrivate::get(QQuickDialogButtonBox *box)
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxPrivate *ritual_ZN28QQuickDialogButtonBoxPrivate3getEP21QQuickDialogButtonBox(
    QQuickDialogButtonBox *box) {
  return QQuickDialogButtonBoxPrivate::get(box);
}

//  void QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickDialogButtonBoxPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickDialogButtonBoxPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickDialogButtonBoxPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate13resizeContentEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->resizeContent();
}

//  void QQuickDialogButtonBoxPrivate::updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate12updateLayoutEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->updateLayout();
}

//  void QQuickDialogButtonBoxPrivate::updateFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate11updateFocusEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->updateFocus();
}

//  qreal QQuickDialogButtonBoxPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QQuickDialogButtonBoxPrivate15getContentWidthEv(
    const QQuickDialogButtonBoxPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickDialogButtonBoxPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QQuickDialogButtonBoxPrivate16getContentHeightEv(
    const QQuickDialogButtonBoxPrivate *self) {
  return self->getContentHeight();
}

//  void QQuickDialogButtonBoxPrivate::handleClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate11handleClickEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->handleClick();
}

//  QString QQuickDialogButtonBoxPrivate::buttonText(QPlatformDialogHelper::S
//      tandardButton standardButton)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickDialogButtonBoxPrivate10buttonTextEN21QPlatformDialogHelper14StandardButtonE(
    QPlatformDialogHelper::StandardButton standardButton) {
  return new QString(
      QQuickDialogButtonBoxPrivate::buttonText(
          standardButton));
}

//  QQuickAbstractButton *QQuickDialogButtonBoxPrivate::createStandardButton(
//      QPlatformDialogHelper::StandardButton button)
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZN28QQuickDialogButtonBoxPrivate20createStandardButtonEN21QPlatformDialogHelper14StandardButtonE(
    QQuickDialogButtonBoxPrivate *self,
    QPlatformDialogHelper::StandardButton button) {
  return self->createStandardButton(button);
}

//  void QQuickDialogButtonBoxPrivate::removeStandardButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate21removeStandardButtonsEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->removeStandardButtons();
}

//  void QQuickDialogButtonBoxPrivate::updateLanguage()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickDialogButtonBoxPrivate14updateLanguageEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->updateLanguage();
}

//  QPlatformDialogHelper::StandardButton
//      QQuickDialogButtonBoxPrivate::standardButton(QQuickAbstractButton
//      *button) const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::StandardButton ritual_ZNK28QQuickDialogButtonBoxPrivate14standardButtonEP20QQuickAbstractButton(
    const QQuickDialogButtonBoxPrivate *self,
    QQuickAbstractButton *button) {
  return self->standardButton(button);
}

//  a Python function taken by a CuteQQuickDialogButtonBoxPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDialogButtonBoxPrivate(
    QQuickDialogButtonBoxPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDialogButtonBoxPrivate *>(self)->take(key, call);
}

//  void QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickDialogButtonBoxPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickDialogButtonBoxPrivate *self,
    QQuickItem *item) {
  self->QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickDialogButtonBoxPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickDialogButtonBoxPrivate *self,
    QQuickItem *item) {
  self->QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickDialogButtonBoxPrivate::resizeContent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickDialogButtonBoxPrivate13resizeContentEv(
    QQuickDialogButtonBoxPrivate *self) {
  self->QQuickDialogButtonBoxPrivate::resizeContent();
}

//  qreal QQuickDialogButtonBoxPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK28QQuickDialogButtonBoxPrivate15getContentWidthEv(
    const QQuickDialogButtonBoxPrivate *self) {
  return self->QQuickDialogButtonBoxPrivate::getContentWidth();
}

//  qreal QQuickDialogButtonBoxPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK28QQuickDialogButtonBoxPrivate16getContentHeightEv(
    const QQuickDialogButtonBoxPrivate *self) {
  return self->QQuickDialogButtonBoxPrivate::getContentHeight();
}

#endif  // QT_CONFIG(quicktemplates2_container)
