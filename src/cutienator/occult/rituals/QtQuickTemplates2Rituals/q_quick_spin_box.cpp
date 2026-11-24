//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickspinbox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickspinbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qlocale.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickindicatorbutton_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickindicatorbutton_p.cpp, line 18, as _ZN28QQuickIndicatorButtonPrivate16executeIndicatorEb
inline void QQuickIndicatorButtonPrivate::executeIndicator(bool complete)
{
    Q_Q(QQuickIndicatorButton);
    if (indicator.wasExecuted())
        return;

    if (!indicator || complete)
        quickBeginDeferred(q, indicatorName(), indicator);
    if (complete)
        quickCompleteDeferred(q, indicatorName(), indicator);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickSpinBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSpinBox : QQuickSpinBox {
  using QQuickSpinBox::focusInEvent;
  using QQuickSpinBox::hoverEnterEvent;
  using QQuickSpinBox::hoverMoveEvent;
  using QQuickSpinBox::hoverLeaveEvent;
  using QQuickSpinBox::keyPressEvent;
  using QQuickSpinBox::keyReleaseEvent;
  using QQuickSpinBox::timerEvent;
  using QQuickSpinBox::wheelEvent;
  using QQuickSpinBox::classBegin;
  using QQuickSpinBox::componentComplete;
  using QQuickSpinBox::itemChange;
  using QQuickSpinBox::contentItemChange;
  using QQuickSpinBox::localeChange;
  using QQuickSpinBox::defaultFont;
  using QQuickSpinBox::accessibleRole;
  using QQuickSpinBox::accessibilityActiveChanged;
};

//  A QQuickSpinBox that Python can take functions over in. Every QQuickSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSpinBoxCall0)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall1)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall2)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall3)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall4)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall5)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall7)(const void *, QKeyEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpinBoxCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSpinBoxCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSpinBoxCall10)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall11)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall12)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickSpinBoxCall13)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSpinBoxCall14)(const void *, const QLocale *, const QLocale *, int *);
typedef const QFont * (*CuteQQuickSpinBoxCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSpinBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSpinBoxCall17)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickSpinBoxCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSpinBoxCall22)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSpinBoxCall23)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSpinBoxCall25)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickSpinBoxCall26)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSpinBoxCall28)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall29)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickSpinBoxCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSpinBoxCall31)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSpinBoxCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickSpinBoxCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickSpinBoxCall34)(const void *, int *);
typedef bool (*CuteQQuickSpinBoxCall35)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickSpinBoxCall36)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickSpinBoxCall37)(const void *, int *);
typedef void * (*CuteQQuickSpinBoxCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpinBoxCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef void (*CuteQQuickSpinBoxCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickSpinBoxCall41)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSpinBoxCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSpinBoxCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSpinBoxCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSpinBoxCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickSpinBoxCall46)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickSpinBoxCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickSpinBoxCall48)(const void *, int *);
typedef void (*CuteQQuickSpinBoxCall49)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSpinBoxCall50)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpinBoxCall51)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpinBoxCall52)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpinBoxCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSpinBoxCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSpinBox : public QQuickSpinBox {
public:
  using QQuickSpinBox::QQuickSpinBox;
  void *taken[55] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QQuickSpinBox8increaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickSpinBox8decreaseEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[38] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[41] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[49] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickSpinBox::increase()
  void increase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSpinBoxCall0 call = reinterpret_cast<CuteQQuickSpinBoxCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSpinBox::increase();
  }

  //  void QQuickSpinBox::decrease()
  void decrease() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSpinBoxCall1 call = reinterpret_cast<CuteQQuickSpinBoxCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSpinBox::decrease();
  }

  //  void QQuickSpinBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSpinBoxCall2 call = reinterpret_cast<CuteQQuickSpinBoxCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::focusInEvent(event);
  }

  //  void QQuickSpinBox::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSpinBoxCall3 call = reinterpret_cast<CuteQQuickSpinBoxCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::hoverEnterEvent(event);
  }

  //  void QQuickSpinBox::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSpinBoxCall4 call = reinterpret_cast<CuteQQuickSpinBoxCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::hoverMoveEvent(event);
  }

  //  void QQuickSpinBox::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSpinBoxCall5 call = reinterpret_cast<CuteQQuickSpinBoxCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::hoverLeaveEvent(event);
  }

  //  void QQuickSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSpinBoxCall6 call = reinterpret_cast<CuteQQuickSpinBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::keyPressEvent(event);
  }

  //  void QQuickSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSpinBoxCall7 call = reinterpret_cast<CuteQQuickSpinBoxCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::keyReleaseEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSpinBoxCall8 call = reinterpret_cast<CuteQQuickSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
  //  void QQuickSpinBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSpinBoxCall9 call = reinterpret_cast<CuteQQuickSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSpinBox::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickSpinBox::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSpinBoxCall10 call = reinterpret_cast<CuteQQuickSpinBoxCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSpinBox::classBegin();
  }

  //  void QQuickSpinBox::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSpinBoxCall11 call = reinterpret_cast<CuteQQuickSpinBoxCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSpinBox::componentComplete();
  }

  //  void QQuickSpinBox::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSpinBoxCall12 call = reinterpret_cast<CuteQQuickSpinBoxCall12>(taken[12]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickSpinBox::itemChange(change, value);
  }

  //  void QQuickSpinBox::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSpinBoxCall13 call = reinterpret_cast<CuteQQuickSpinBoxCall13>(taken[13]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickSpinBox::contentItemChange(newItem, oldItem);
  }

  //  void QQuickSpinBox::localeChange(const QLocale &newLocale, const
  //      QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSpinBoxCall14 call = reinterpret_cast<CuteQQuickSpinBoxCall14>(taken[14]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickSpinBox::localeChange(newLocale, oldLocale);
  }

  //  QFont QQuickSpinBox::defaultFont() const
  QFont defaultFont() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSpinBoxCall15 call = reinterpret_cast<CuteQQuickSpinBoxCall15>(taken[15]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickSpinBox::defaultFont();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickSpinBox::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSpinBoxCall16 call = reinterpret_cast<CuteQQuickSpinBoxCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickSpinBox::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickSpinBox::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSpinBoxCall17 call = reinterpret_cast<CuteQQuickSpinBoxCall17>(taken[17]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickSpinBox::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSpinBoxCall18 call = reinterpret_cast<CuteQQuickSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSpinBoxCall19 call = reinterpret_cast<CuteQQuickSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSpinBoxCall20 call = reinterpret_cast<CuteQQuickSpinBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickSpinBoxCall21 call = reinterpret_cast<CuteQQuickSpinBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickSpinBoxCall22 call = reinterpret_cast<CuteQQuickSpinBoxCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickSpinBoxCall23 call = reinterpret_cast<CuteQQuickSpinBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickSpinBoxCall24 call = reinterpret_cast<CuteQQuickSpinBoxCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControl::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSpinBoxCall25 call = reinterpret_cast<CuteQQuickSpinBoxCall25>(taken[25]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSpinBoxCall26 call = reinterpret_cast<CuteQQuickSpinBoxCall26>(taken[26]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSpinBoxCall27 call = reinterpret_cast<CuteQQuickSpinBoxCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSpinBoxCall28 call = reinterpret_cast<CuteQQuickSpinBoxCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSpinBoxCall29 call = reinterpret_cast<CuteQQuickSpinBoxCall29>(taken[29]);
      call(this, newSpacing, oldSpacing, &handled);
      if (handled) return;
    }
    QQuickControl::spacingChange(newSpacing, oldSpacing);
  }

  //  void QQuickControl::paddingChange(const QMarginsF &newPadding, const
  //      QMarginsF &oldPadding)
  void paddingChange(
      const QMarginsF &newPadding,
      const QMarginsF &oldPadding) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSpinBoxCall30 call = reinterpret_cast<CuteQQuickSpinBoxCall30>(taken[30]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSpinBoxCall31 call = reinterpret_cast<CuteQQuickSpinBoxCall31>(taken[31]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSpinBoxCall32 call = reinterpret_cast<CuteQQuickSpinBoxCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSpinBoxCall33 call = reinterpret_cast<CuteQQuickSpinBoxCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSpinBoxCall34 call = reinterpret_cast<CuteQQuickSpinBoxCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSpinBoxCall35 call = reinterpret_cast<CuteQQuickSpinBoxCall35>(taken[35]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickSpinBoxCall36 call = reinterpret_cast<CuteQQuickSpinBoxCall36>(taken[36]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickSpinBoxCall37 call = reinterpret_cast<CuteQQuickSpinBoxCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickSpinBoxCall38 call = reinterpret_cast<CuteQQuickSpinBoxCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickSpinBoxCall39 call = reinterpret_cast<CuteQQuickSpinBoxCall39>(taken[39]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickSpinBoxCall40 call = reinterpret_cast<CuteQQuickSpinBoxCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickSpinBoxCall41 call = reinterpret_cast<CuteQQuickSpinBoxCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickSpinBoxCall42 call = reinterpret_cast<CuteQQuickSpinBoxCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickSpinBoxCall43 call = reinterpret_cast<CuteQQuickSpinBoxCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickSpinBoxCall44 call = reinterpret_cast<CuteQQuickSpinBoxCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickSpinBoxCall45 call = reinterpret_cast<CuteQQuickSpinBoxCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickSpinBoxCall46 call = reinterpret_cast<CuteQQuickSpinBoxCall46>(taken[46]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickSpinBoxCall47 call = reinterpret_cast<CuteQQuickSpinBoxCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickSpinBoxCall48 call = reinterpret_cast<CuteQQuickSpinBoxCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickSpinBoxCall49 call = reinterpret_cast<CuteQQuickSpinBoxCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickSpinBoxCall50 call = reinterpret_cast<CuteQQuickSpinBoxCall50>(taken[50]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickSpinBoxCall51 call = reinterpret_cast<CuteQQuickSpinBoxCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickSpinBoxCall52 call = reinterpret_cast<CuteQQuickSpinBoxCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickSpinBoxCall53 call = reinterpret_cast<CuteQQuickSpinBoxCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickSpinBoxCall54 call = reinterpret_cast<CuteQQuickSpinBoxCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickSpinBox10metaObjectEv(
    const QQuickSpinBox *self) {
  return self->metaObject();
}

//  QString QQuickSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSpinBox::tr(s, c, n));
}

//  QQuickSpinBox::QQuickSpinBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSpinBox *ritual_ZN13QQuickSpinBoxC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickSpinBox(parent);
}

//  QQuickSpinBox::~QQuickSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBoxD1Ev(QQuickSpinBox *self) {
  delete self;
}

//  void QQuickSpinBox::setFrom(int from)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox7setFromEi(QQuickSpinBox *self, int from) {
  self->setFrom(from);
}

//  void QQuickSpinBox::setTo(int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox5setToEi(QQuickSpinBox *self, int to) {
  self->setTo(to);
}

//  void QQuickSpinBox::setValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox8setValueEi(QQuickSpinBox *self, int value) {
  self->setValue(value);
}

//  void QQuickSpinBox::setStepSize(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox11setStepSizeEi(QQuickSpinBox *self, int step) {
  self->setStepSize(step);
}

//  bool QQuickSpinBox::isLive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickSpinBox6isLiveEv(const QQuickSpinBox *self) {
  return self->isLive();
}

//  void QQuickSpinBox::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox7setLiveEb(QQuickSpinBox *self, bool live) {
  self->setLive(live);
}

//  QJSValue QQuickSpinBox::textFromValue() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK13QQuickSpinBox13textFromValueEv(
    const QQuickSpinBox *self) {
  return new QJSValue(self->textFromValue());
}

//  QJSValue QQuickSpinBox::valueFromText() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK13QQuickSpinBox13valueFromTextEv(
    const QQuickSpinBox *self) {
  return new QJSValue(self->valueFromText());
}

//  void QQuickSpinBox::setWrap(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox7setWrapEb(QQuickSpinBox *self, bool wrap) {
  self->setWrap(wrap);
}

//  void QQuickSpinBox::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox8increaseEv(QQuickSpinBox *self) {
  self->increase();
}

//  void QQuickSpinBox::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox8decreaseEv(QQuickSpinBox *self) {
  self->decrease();
}

//  void QQuickSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox12focusInEventEP11QFocusEvent(
    QQuickSpinBox *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickSpinBox::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox15hoverEnterEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickSpinBox::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox14hoverMoveEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickSpinBox::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox15hoverLeaveEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox13keyPressEventEP9QKeyEvent(
    QQuickSpinBox *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox15keyReleaseEventEP9QKeyEvent(
    QQuickSpinBox *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox10timerEventEP11QTimerEvent(
    QQuickSpinBox *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox10wheelEventEP11QWheelEvent(
    QQuickSpinBox *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickSpinBox::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox10classBeginEv(QQuickSpinBox *self) {
  self->classBegin();
}

//  void QQuickSpinBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox17componentCompleteEv(QQuickSpinBox *self) {
  self->componentComplete();
}

//  void QQuickSpinBox::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickSpinBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickSpinBox::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox17contentItemChangeEP10QQuickItemS1_(
    QQuickSpinBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickSpinBox::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox12localeChangeERK7QLocaleS2_(
    QQuickSpinBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  QFont QQuickSpinBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickSpinBox11defaultFontEv(const QQuickSpinBox *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSpinBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK13QQuickSpinBox14accessibleRoleEv(
    const QQuickSpinBox *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickSpinBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSpinBox26accessibilityActiveChangedEb(
    QQuickSpinBox *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickControlPrivate *QQuickSpinBox::d_base_func()
extern "C" Q_DECL_EXPORT
QQuickControlPrivate *ritual_ZN13QQuickSpinBox11d_base_funcEv(
    QQuickSpinBox *self) {
  return self->d_base_func();
}

//  const QQuickControlPrivate *QQuickSpinBox::d_base_func() const
extern "C" Q_DECL_EXPORT
const QQuickControlPrivate *ritual_ZNK13QQuickSpinBox11d_base_funcEv(
    const QQuickSpinBox *self) {
  return self->d_base_func();
}

//  a Python function taken by a CuteQQuickSpinBox, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSpinBox(
    QQuickSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSpinBox *>(self)->take(key, call);
}

//  void QQuickSpinBox::increase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox8increaseEv(QQuickSpinBox *self) {
  self->QQuickSpinBox::increase();
}

//  void QQuickSpinBox::decrease()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox8decreaseEv(QQuickSpinBox *self) {
  self->QQuickSpinBox::decrease();
}

//  void QQuickSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox12focusInEventEP11QFocusEvent(
    QQuickSpinBox *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::focusInEvent(
      event);
}

//  void QQuickSpinBox::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox15hoverEnterEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::hoverEnterEvent(
      event);
}

//  void QQuickSpinBox::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox14hoverMoveEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::hoverMoveEvent(
      event);
}

//  void QQuickSpinBox::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox15hoverLeaveEventEP11QHoverEvent(
    QQuickSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::hoverLeaveEvent(
      event);
}

//  void QQuickSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox13keyPressEventEP9QKeyEvent(
    QQuickSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::keyPressEvent(
      event);
}

//  void QQuickSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox15keyReleaseEventEP9QKeyEvent(
    QQuickSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::keyReleaseEvent(
      event);
}

//  void QQuickSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox10timerEventEP11QTimerEvent(
    QQuickSpinBox *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::timerEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox10wheelEventEP11QWheelEvent(
    QQuickSpinBox *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickSpinBox::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox10classBeginEv(QQuickSpinBox *self) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::classBegin();
}

//  void QQuickSpinBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox17componentCompleteEv(QQuickSpinBox *self) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::componentComplete();
}

//  void QQuickSpinBox::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickSpinBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::itemChange(
      change,
      *value);
}

//  void QQuickSpinBox::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox17contentItemChangeEP10QQuickItemS1_(
    QQuickSpinBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickSpinBox::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox12localeChangeERK7QLocaleS2_(
    QQuickSpinBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::localeChange(
      *newLocale,
      *oldLocale);
}

//  QFont QQuickSpinBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickSpinBox11defaultFontEv(
    const QQuickSpinBox *self) {
  return new QFont(
      static_cast<const OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSpinBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK13QQuickSpinBox14accessibleRoleEv(
    const QQuickSpinBox *self) {
  return static_cast<const OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickSpinBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSpinBox26accessibilityActiveChangedEb(
    QQuickSpinBox *self,
    bool active) {
  static_cast<OwnQQuickSpinBox *>(self)->OwnQQuickSpinBox::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
