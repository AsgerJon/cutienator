//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p_p.h>
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
#include <QtQuickTemplates2/private/qquickmenubaritem_p.h>
#include <QtQuickTemplates2/private/qquickmenubaritem_p_p.h>
#include <QtQuickTemplates2/private/qquickmenubar_p.h>
#include <QtQuickTemplates2/private/qquickmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickmenubaritem.cpp, line 41, as _ZN24QQuickMenuBarItemPrivate10setMenuBarEP13QQuickMenuBar
inline void QQuickMenuBarItemPrivate::setMenuBar(QQuickMenuBar *newMenuBar)
{
    Q_Q(QQuickMenuBarItem);
    if (menuBar == newMenuBar)
        return;

    menuBar = newMenuBar;
    emit q->menuBarChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickmenubaritem.cpp, line 63, as _ZN24QQuickMenuBarItemPrivate11handlePressERK7QPointFm
inline bool QQuickMenuBarItemPrivate::handlePress(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickMenuBarItem);
    const bool handled = QQuickAbstractButtonPrivate::handlePress(point, timestamp);
    if (!handled)
        return false;

    const bool wasTouchPress = touchId != -1;
    if (!wasTouchPress) {
        // Open the menu when it's a mouse press.
        emit q->triggered();
    }

    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmenubaritem.cpp, line 79, as _ZN24QQuickMenuBarItemPrivate13handleReleaseERK7QPointFm
inline bool QQuickMenuBarItemPrivate::handleRelease(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickMenuBarItem);
    const bool wasTouchPress = touchId != -1;
    const bool handled = QQuickAbstractButtonPrivate::handleRelease(point, timestamp);
    if (!handled)
        return false;

    if (wasDoubleClick || !wasTouchPress) {
        // Don't open the menu on mouse release, as it should be done on press.
        return handled;
    }

    if (wasTouchPress) {
        // Open the menu.
        emit q->triggered();
    }

    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmenubaritem.cpp, line 100, as _ZNK24QQuickMenuBarItemPrivate14defaultPaletteEv
inline QPalette QQuickMenuBarItemPrivate::defaultPalette() const
{
    return QQuickTheme::palette(QQuickTheme::MenuBar);
}

//  from ../qtdeclarative/src/quicktemplates/qquickmenubaritem.cpp, line 51, as _ZN24QQuickMenuBarItemPrivate21accessiblePressActionEv
inline void QQuickMenuBarItemPrivate::accessiblePressAction()
{
    // This is inspired by the code in keyReleaseEvent

    Q_Q(QQuickMenuBarItem);

    // We override these event functions so that we can emit triggered here.
    // We can't just connect clicked to triggered, because that would cause mouse clicks
    // to open the menu, when only presses should.
    emit q->triggered();
}
//  -----------------------------------------------------------------------

//  A QQuickMenuBarItemPrivate that Python can take functions over in. Every QQuickMenuBarItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickMenuBarItemPrivateCall0)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef const QPalette * (*CuteQQuickMenuBarItemPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall3)(const void *, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall4)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall5)(const void *, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall10)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickMenuBarItemPrivateCall11)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickMenuBarItemPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall14)(const void *, int *);
typedef void * (*CuteQQuickMenuBarItemPrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickMenuBarItemPrivateCall16)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickMenuBarItemPrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickMenuBarItemPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall20)(const void *, bool, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall22)(const void *, bool, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall23)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall24)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall25)(const void *, int, int *);
typedef qreal (*CuteQQuickMenuBarItemPrivateCall26)(const void *, int *);
typedef qreal (*CuteQQuickMenuBarItemPrivateCall27)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickMenuBarItemPrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickMenuBarItemPrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickMenuBarItemPrivateCall33)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall34)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickMenuBarItemPrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickMenuBarItemPrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickMenuBarItemPrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickMenuBarItemPrivateCall40)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall41)(const void *, int *);
typedef void (*CuteQQuickMenuBarItemPrivateCall42)(const void *, int, int *);
class CuteQQuickMenuBarItemPrivate : public QQuickMenuBarItemPrivate {
public:
  using QQuickMenuBarItemPrivate::QQuickMenuBarItemPrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE")) {
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

  //  bool QQuickMenuBarItemPrivate::handlePress(const QPointF &point,
  //      ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall0 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall0>(taken[0]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickMenuBarItemPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickMenuBarItemPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall1 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickMenuBarItemPrivate::handleRelease(point, timestamp);
  }

  //  QPalette QQuickMenuBarItemPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall2 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall2>(taken[2]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickMenuBarItemPrivate::defaultPalette();
  }

  //  void QQuickMenuBarItemPrivate::accessiblePressAction()
  void accessiblePressAction() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall3 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuBarItemPrivate::accessiblePressAction();
  }

  //  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
  //      ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall4 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall4>(taken[4]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleMove(point, timestamp);
  }

  //  void QQuickAbstractButtonPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall5 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::handleUngrab();
  }

  //  bool QQuickAbstractButtonPrivate::acceptKeyClick(Qt::Key key) const
  bool acceptKeyClick(Qt::Key key) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall6 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(key), &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::acceptKeyClick(key);
  }

  //  void QQuickAbstractButtonPrivate::accessibleToggleAction()
  void accessibleToggleAction() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall7 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall7>(taken[7]);
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
      CuteQQuickMenuBarItemPrivateCall8 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall8>(taken[8]);
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
      CuteQQuickMenuBarItemPrivateCall9 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall10 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall10>(taken[10]);
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
      CuteQQuickMenuBarItemPrivateCall11 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall11>(taken[11]);
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
      CuteQQuickMenuBarItemPrivateCall12 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall13 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall14 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall15 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall15>(taken[15]);
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
      CuteQQuickMenuBarItemPrivateCall16 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall16>(taken[16]);
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
      CuteQQuickMenuBarItemPrivateCall17 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall17>(taken[17]);
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
      CuteQQuickMenuBarItemPrivateCall18 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall19 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall20 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall20>(taken[20]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall21 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall22 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall22>(taken[22]);
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
      CuteQQuickMenuBarItemPrivateCall23 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall23>(taken[23]);
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
      CuteQQuickMenuBarItemPrivateCall24 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall24>(taken[24]);
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
      CuteQQuickMenuBarItemPrivateCall25 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall25>(taken[25]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall26 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall27 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall27>(taken[27]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall28 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall29 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall29>(taken[29]);
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
      CuteQQuickMenuBarItemPrivateCall30 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall30>(taken[30]);
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
      CuteQQuickMenuBarItemPrivateCall31 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall32 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall33 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall34 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall35 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall36 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall36>(taken[36]);
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
      CuteQQuickMenuBarItemPrivateCall37 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall37>(taken[37]);
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
      CuteQQuickMenuBarItemPrivateCall38 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall38>(taken[38]);
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
      CuteQQuickMenuBarItemPrivateCall39 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall40 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall41 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickMenuBarItemPrivateCall42 call = reinterpret_cast<CuteQQuickMenuBarItemPrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickMenuBarItem *QQuickMenuBarItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMenuBarItem *ritual_ZN24QQuickMenuBarItemPrivate6q_funcEv(
    QQuickMenuBarItemPrivate *self) {
  return self->q_func();
}

//  const QQuickMenuBarItem *QQuickMenuBarItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuBarItem *ritual_ZNK24QQuickMenuBarItemPrivate6q_funcEv(
    const QQuickMenuBarItemPrivate *self) {
  return self->q_func();
}

//  QQuickMenuBarItemPrivate *QQuickMenuBarItemPrivate::get(QQuickMenuBarItem
//      *item)
extern "C" Q_DECL_EXPORT
QQuickMenuBarItemPrivate *ritual_ZN24QQuickMenuBarItemPrivate3getEP17QQuickMenuBarItem(
    QQuickMenuBarItem *item) {
  return QQuickMenuBarItemPrivate::get(item);
}

//  void QQuickMenuBarItemPrivate::setMenuBar(QQuickMenuBar *menuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMenuBarItemPrivate10setMenuBarEP13QQuickMenuBar(
    QQuickMenuBarItemPrivate *self,
    QQuickMenuBar *menuBar) {
  self->setMenuBar(menuBar);
}

//  bool QQuickMenuBarItemPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickMenuBarItemPrivate11handlePressERK7QPointFm(
    QQuickMenuBarItemPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  bool QQuickMenuBarItemPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickMenuBarItemPrivate13handleReleaseERK7QPointFm(
    QQuickMenuBarItemPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(*point, timestamp);
}

//  QPalette QQuickMenuBarItemPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK24QQuickMenuBarItemPrivate14defaultPaletteEv(
    const QQuickMenuBarItemPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  void QQuickMenuBarItemPrivate::accessiblePressAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMenuBarItemPrivate21accessiblePressActionEv(
    QQuickMenuBarItemPrivate *self) {
  self->accessiblePressAction();
}

//  a Python function taken by a CuteQQuickMenuBarItemPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenuBarItemPrivate(
    QQuickMenuBarItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMenuBarItemPrivate *>(self)->take(key, call);
}

//  bool QQuickMenuBarItemPrivate::handlePress(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickMenuBarItemPrivate11handlePressERK7QPointFm(
    QQuickMenuBarItemPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickMenuBarItemPrivate::handlePress(*point, timestamp);
}

//  bool QQuickMenuBarItemPrivate::handleRelease(const QPointF &point, ulong
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickMenuBarItemPrivate13handleReleaseERK7QPointFm(
    QQuickMenuBarItemPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickMenuBarItemPrivate::handleRelease(*point, timestamp);
}

//  QPalette QQuickMenuBarItemPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK24QQuickMenuBarItemPrivate14defaultPaletteEv(
    const QQuickMenuBarItemPrivate *self) {
  return new QPalette(self->QQuickMenuBarItemPrivate::defaultPalette());
}

//  void QQuickMenuBarItemPrivate::accessiblePressAction()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickMenuBarItemPrivate21accessiblePressActionEv(
    QQuickMenuBarItemPrivate *self) {
  self->QQuickMenuBarItemPrivate::accessiblePressAction();
}

#endif  // QT_CONFIG(quicktemplates2_container)
