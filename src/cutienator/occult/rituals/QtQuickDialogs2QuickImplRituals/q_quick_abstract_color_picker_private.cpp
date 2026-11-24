//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpic
//  ker_p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogutils_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 17, as _ZN32QQuickAbstractColorPickerPrivate11handlePressERK7QPointFm
inline bool QQuickAbstractColorPickerPrivate::handlePress(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::handlePress(point, timestamp);
    m_pressPoint = point;
    q->setPressed(true);
    q->updateColor(point);
    return true;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 27, as _ZN32QQuickAbstractColorPickerPrivate10handleMoveERK7QPointFm
inline bool QQuickAbstractColorPickerPrivate::handleMove(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::handleMove(point, timestamp);
    if (point != m_pressPoint)
        q->updateColor(point);
    return true;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 36, as _ZN32QQuickAbstractColorPickerPrivate13handleReleaseERK7QPointFm
inline bool QQuickAbstractColorPickerPrivate::handleRelease(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::handleRelease(point, timestamp);
    m_pressPoint = QPointF();
    q->setKeepMouseGrab(false);
    q->setKeepTouchGrab(false);
    q->setPressed(false);
    q->updateColor(point);
    return true;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 48, as _ZN32QQuickAbstractColorPickerPrivate12handleUngrabEv
inline void QQuickAbstractColorPickerPrivate::handleUngrab()
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::handleUngrab();
    m_pressPoint = QPointF();
    q->setPressed(false);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 56, as _ZN32QQuickAbstractColorPickerPrivate12cancelHandleEv
inline void QQuickAbstractColorPickerPrivate::cancelHandle()
{
    Q_Q(QQuickAbstractColorPicker);
    quickCancelDeferred(q, handleName());
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 62, as _ZN32QQuickAbstractColorPickerPrivate13executeHandleEb
inline void QQuickAbstractColorPickerPrivate::executeHandle(bool complete)
{
    Q_Q(QQuickAbstractColorPicker);
    if (m_handle.wasExecuted())
        return;

    if (!m_handle || complete)
        quickBeginDeferred(q, handleName(), m_handle);
    if (complete)
        quickCompleteDeferred(q, handleName(), m_handle);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 74, as _ZN32QQuickAbstractColorPickerPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::itemImplicitWidthChanged(item);
    if (item == m_handle)
        emit q->implicitHandleWidthChanged();
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickabstractcolorpicker.cpp, line 82, as _ZN32QQuickAbstractColorPickerPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickAbstractColorPicker);
    QQuickControlPrivate::itemImplicitHeightChanged(item);
    if (item == m_handle)
        emit q->implicitHandleHeightChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickAbstractColorPickerPrivate that Python can take functions over in. Every QQuickAbstractColorPickerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall0)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall5)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall6)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractColorPickerPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall9)(const void *, int *);
typedef void * (*CuteQQuickAbstractColorPickerPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractColorPickerPrivateCall11)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickAbstractColorPickerPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractColorPickerPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall15)(const void *, bool, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall17)(const void *, bool, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall18)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall20)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall21)(const void *, int, int *);
typedef qreal (*CuteQQuickAbstractColorPickerPrivateCall22)(const void *, int *);
typedef qreal (*CuteQQuickAbstractColorPickerPrivateCall23)(const void *, int *);
typedef const QPalette * (*CuteQQuickAbstractColorPickerPrivateCall24)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall25)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickAbstractColorPickerPrivateCall27)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall28)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickAbstractColorPickerPrivateCall29)(const void *, int *);
typedef qreal (*CuteQQuickAbstractColorPickerPrivateCall30)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall31)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall32)(const void *, int *);
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall33)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall34)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickAbstractColorPickerPrivateCall35)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickAbstractColorPickerPrivateCall36)(const void *, bool, int *);
typedef void * (*CuteQQuickAbstractColorPickerPrivateCall37)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerPrivateCall39)(const void *, int, int *);
class CuteQQuickAbstractColorPickerPrivate : public QQuickAbstractColorPickerPrivate {
public:
  using QQuickAbstractColorPickerPrivate::QQuickAbstractColorPickerPrivate;
  void *taken[40] = {};

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
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
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

  //  bool QQuickAbstractColorPickerPrivate::handlePress(const QPointF
  //      &point, ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall0 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall0>(taken[0]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractColorPickerPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickAbstractColorPickerPrivate::handleMove(const QPointF
  //      &point, ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall1 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractColorPickerPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickAbstractColorPickerPrivate::handleRelease(const QPointF
  //      &point, ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall2 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractColorPickerPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickAbstractColorPickerPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall3 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractColorPickerPrivate::handleUngrab();
  }

  //  void
  //      QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(QQuick
  //      Item *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall4 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(QQui
  //      ckItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall5 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall6 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall7 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall8 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall9 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall10 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall11 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall11>(taken[11]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall12 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall13 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall14 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall15 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall15>(taken[15]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall16 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall17 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall18 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall18>(taken[18]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall19 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall19>(taken[19]);
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
      CuteQQuickAbstractColorPickerPrivateCall20 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall20>(taken[20]);
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
      CuteQQuickAbstractColorPickerPrivateCall21 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall21>(taken[21]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall22 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall23 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall24 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall24>(taken[24]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall25 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall25>(taken[25]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall26 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall26>(taken[26]);
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
      CuteQQuickAbstractColorPickerPrivateCall27 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall27>(taken[27]);
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
      CuteQQuickAbstractColorPickerPrivateCall28 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall28>(taken[28]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall29 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall29>(taken[29]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall30 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall31 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall32 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall33 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall33>(taken[33]);
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
      CuteQQuickAbstractColorPickerPrivateCall34 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall34>(taken[34]);
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
      CuteQQuickAbstractColorPickerPrivateCall35 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall35>(taken[35]);
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
      CuteQQuickAbstractColorPickerPrivateCall36 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall36>(taken[36]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall37 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall38 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerPrivateCall39 call = reinterpret_cast<CuteQQuickAbstractColorPickerPrivateCall39>(taken[39]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickAbstractColorPicker *QQuickAbstractColorPickerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractColorPicker *ritual_ZN32QQuickAbstractColorPickerPrivate6q_funcEv(
    QQuickAbstractColorPickerPrivate *self) {
  return self->q_func();
}

//  const QQuickAbstractColorPicker
//      *QQuickAbstractColorPickerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAbstractColorPicker *ritual_ZNK32QQuickAbstractColorPickerPrivate6q_funcEv(
    const QQuickAbstractColorPickerPrivate *self) {
  return self->q_func();
}

//  QQuickAbstractColorPickerPrivate
//      *QQuickAbstractColorPickerPrivate::get(QQuickAbstractColorPicker
//      *colorPicker)
extern "C" Q_DECL_EXPORT
QQuickAbstractColorPickerPrivate *ritual_ZN32QQuickAbstractColorPickerPrivate3getEP25QQuickAbstractColorPicker(
    QQuickAbstractColorPicker *colorPicker) {
  return QQuickAbstractColorPickerPrivate::get(colorPicker);
}

//  bool QQuickAbstractColorPickerPrivate::handlePress(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QQuickAbstractColorPickerPrivate11handlePressERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(*point, timestamp);
}

//  bool QQuickAbstractColorPickerPrivate::handleMove(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QQuickAbstractColorPickerPrivate10handleMoveERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(*point, timestamp);
}

//  bool QQuickAbstractColorPickerPrivate::handleRelease(const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QQuickAbstractColorPickerPrivate13handleReleaseERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(*point, timestamp);
}

//  void QQuickAbstractColorPickerPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAbstractColorPickerPrivate12handleUngrabEv(
    QQuickAbstractColorPickerPrivate *self) {
  self->handleUngrab();
}

//  void QQuickAbstractColorPickerPrivate::cancelHandle()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAbstractColorPickerPrivate12cancelHandleEv(
    QQuickAbstractColorPickerPrivate *self) {
  self->cancelHandle();
}

//  void QQuickAbstractColorPickerPrivate::executeHandle(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAbstractColorPickerPrivate13executeHandleEb(
    QQuickAbstractColorPickerPrivate *self,
    bool complete) {
  self->executeHandle(complete);
}

//  void
//      QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAbstractColorPickerPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickAbstractColorPickerPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void
//      QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(QQuickIte
//      m *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickAbstractColorPickerPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickAbstractColorPickerPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  a Python function taken by a CuteQQuickAbstractColorPickerPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractColorPickerPrivate(
    QQuickAbstractColorPickerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractColorPickerPrivate *>(self)->take(key, call);
}

//  bool QQuickAbstractColorPickerPrivate::handlePress(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN32QQuickAbstractColorPickerPrivate11handlePressERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractColorPickerPrivate::handlePress(
      *point,
      timestamp);
}

//  bool QQuickAbstractColorPickerPrivate::handleMove(const QPointF &point,
//      ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN32QQuickAbstractColorPickerPrivate10handleMoveERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractColorPickerPrivate::handleMove(
      *point,
      timestamp);
}

//  bool QQuickAbstractColorPickerPrivate::handleRelease(const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN32QQuickAbstractColorPickerPrivate13handleReleaseERK7QPointFm(
    QQuickAbstractColorPickerPrivate *self,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickAbstractColorPickerPrivate::handleRelease(
      *point,
      timestamp);
}

//  void QQuickAbstractColorPickerPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickAbstractColorPickerPrivate12handleUngrabEv(
    QQuickAbstractColorPickerPrivate *self) {
  self->QQuickAbstractColorPickerPrivate::handleUngrab();
}

//  void
//      QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickAbstractColorPickerPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickAbstractColorPickerPrivate *self,
    QQuickItem *item) {
  self->QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(item);
}

//  void
//      QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(QQuickIte
//      m *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickAbstractColorPickerPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickAbstractColorPickerPrivate *self,
    QQuickItem *item) {
  self->QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(item);
}
