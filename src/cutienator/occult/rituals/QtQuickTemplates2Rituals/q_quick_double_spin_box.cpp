//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdoublespinbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdoublespinbox_p.h>
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

//  Only a class built on QQuickDoubleSpinBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDoubleSpinBox : QQuickDoubleSpinBox {
  using QQuickDoubleSpinBox::focusInEvent;
  using QQuickDoubleSpinBox::hoverEnterEvent;
  using QQuickDoubleSpinBox::hoverMoveEvent;
  using QQuickDoubleSpinBox::hoverLeaveEvent;
  using QQuickDoubleSpinBox::keyPressEvent;
  using QQuickDoubleSpinBox::keyReleaseEvent;
  using QQuickDoubleSpinBox::timerEvent;
  using QQuickDoubleSpinBox::wheelEvent;
  using QQuickDoubleSpinBox::classBegin;
  using QQuickDoubleSpinBox::componentComplete;
  using QQuickDoubleSpinBox::itemChange;
  using QQuickDoubleSpinBox::contentItemChange;
  using QQuickDoubleSpinBox::localeChange;
  using QQuickDoubleSpinBox::defaultFont;
  using QQuickDoubleSpinBox::accessibleRole;
  using QQuickDoubleSpinBox::accessibilityActiveChanged;
};

//  A QQuickDoubleSpinBox that Python can take functions over in. Every QQuickDoubleSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickDoubleSpinBoxCall0)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall1)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall2)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall3)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall4)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall5)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall7)(const void *, QKeyEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDoubleSpinBoxCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDoubleSpinBoxCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDoubleSpinBoxCall10)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall11)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall12)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall13)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall14)(const void *, const QLocale *, const QLocale *, int *);
typedef const QFont * (*CuteQQuickDoubleSpinBoxCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickDoubleSpinBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickDoubleSpinBoxCall17)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickDoubleSpinBoxCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall22)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDoubleSpinBoxCall23)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDoubleSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDoubleSpinBoxCall25)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall26)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDoubleSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDoubleSpinBoxCall28)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall29)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall31)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickDoubleSpinBoxCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickDoubleSpinBoxCall34)(const void *, int *);
typedef bool (*CuteQQuickDoubleSpinBoxCall35)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickDoubleSpinBoxCall36)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickDoubleSpinBoxCall37)(const void *, int *);
typedef void * (*CuteQQuickDoubleSpinBoxCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDoubleSpinBoxCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef void (*CuteQQuickDoubleSpinBoxCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickDoubleSpinBoxCall41)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDoubleSpinBoxCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDoubleSpinBoxCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDoubleSpinBoxCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDoubleSpinBoxCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickDoubleSpinBoxCall46)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickDoubleSpinBoxCall47)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall48)(const void *, int *);
typedef void (*CuteQQuickDoubleSpinBoxCall49)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDoubleSpinBoxCall50)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDoubleSpinBoxCall51)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDoubleSpinBoxCall52)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDoubleSpinBoxCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDoubleSpinBoxCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDoubleSpinBox : public QQuickDoubleSpinBox {
public:
  using QQuickDoubleSpinBox::QQuickDoubleSpinBox;
  void *taken[55] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDoubleSpinBox8increaseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDoubleSpinBox8decreaseEv")) {
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

  //  void QQuickDoubleSpinBox::increase()
  void increase() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall0 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::increase();
  }

  //  void QQuickDoubleSpinBox::decrease()
  void decrease() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall1 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::decrease();
  }

  //  void QQuickDoubleSpinBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall2 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::focusInEvent(event);
  }

  //  void QQuickDoubleSpinBox::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall3 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::hoverEnterEvent(event);
  }

  //  void QQuickDoubleSpinBox::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall4 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::hoverMoveEvent(event);
  }

  //  void QQuickDoubleSpinBox::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall5 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::hoverLeaveEvent(event);
  }

  //  void QQuickDoubleSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall6 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::keyPressEvent(event);
  }

  //  void QQuickDoubleSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall7 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::keyReleaseEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickDoubleSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall8 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
  //  void QQuickDoubleSpinBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall9 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickDoubleSpinBox::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall10 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::classBegin();
  }

  //  void QQuickDoubleSpinBox::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall11 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::componentComplete();
  }

  //  void QQuickDoubleSpinBox::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall12 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall12>(taken[12]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::itemChange(change, value);
  }

  //  void QQuickDoubleSpinBox::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall13 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall13>(taken[13]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::contentItemChange(newItem, oldItem);
  }

  //  void QQuickDoubleSpinBox::localeChange(const QLocale &newLocale,
  //      const QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall14 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall14>(taken[14]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::localeChange(newLocale, oldLocale);
  }

  //  QFont QQuickDoubleSpinBox::defaultFont() const
  QFont defaultFont() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall15 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall15>(taken[15]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickDoubleSpinBox::defaultFont();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickDoubleSpinBox::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall16 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickDoubleSpinBox::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickDoubleSpinBox::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall17 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall17>(taken[17]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickDoubleSpinBox::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall18 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall19 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall20 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall21 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall22 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall22>(taken[22]);
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
      CuteQQuickDoubleSpinBoxCall23 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall23>(taken[23]);
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
      CuteQQuickDoubleSpinBoxCall24 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall24>(taken[24]);
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
      CuteQQuickDoubleSpinBoxCall25 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall25>(taken[25]);
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
      CuteQQuickDoubleSpinBoxCall26 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall26>(taken[26]);
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
      CuteQQuickDoubleSpinBoxCall27 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall27>(taken[27]);
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
      CuteQQuickDoubleSpinBoxCall28 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall29 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall29>(taken[29]);
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
      CuteQQuickDoubleSpinBoxCall30 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall30>(taken[30]);
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
      CuteQQuickDoubleSpinBoxCall31 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall31>(taken[31]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall32 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall33 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall34 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall35 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall35>(taken[35]);
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
      CuteQQuickDoubleSpinBoxCall36 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall36>(taken[36]);
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
      CuteQQuickDoubleSpinBoxCall37 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall38 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall38>(taken[38]);
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
      CuteQQuickDoubleSpinBoxCall39 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall39>(taken[39]);
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
      CuteQQuickDoubleSpinBoxCall40 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall40>(taken[40]);
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
      CuteQQuickDoubleSpinBoxCall41 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall41>(taken[41]);
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
      CuteQQuickDoubleSpinBoxCall42 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall42>(taken[42]);
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
      CuteQQuickDoubleSpinBoxCall43 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall43>(taken[43]);
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
      CuteQQuickDoubleSpinBoxCall44 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall44>(taken[44]);
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
      CuteQQuickDoubleSpinBoxCall45 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall45>(taken[45]);
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
      CuteQQuickDoubleSpinBoxCall46 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall46>(taken[46]);
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
      CuteQQuickDoubleSpinBoxCall47 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall47>(taken[47]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall48 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickDoubleSpinBoxCall49 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall49>(taken[49]);
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
      CuteQQuickDoubleSpinBoxCall50 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall50>(taken[50]);
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
      CuteQQuickDoubleSpinBoxCall51 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall51>(taken[51]);
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
      CuteQQuickDoubleSpinBoxCall52 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall52>(taken[52]);
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
      CuteQQuickDoubleSpinBoxCall53 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall53>(taken[53]);
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
      CuteQQuickDoubleSpinBoxCall54 call = reinterpret_cast<CuteQQuickDoubleSpinBoxCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDoubleSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickDoubleSpinBox10metaObjectEv(
    const QQuickDoubleSpinBox *self) {
  return self->metaObject();
}

//  void *QQuickDoubleSpinBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickDoubleSpinBox11qt_metacastEPKc(
    QQuickDoubleSpinBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDoubleSpinBox::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickDoubleSpinBox11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDoubleSpinBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDoubleSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickDoubleSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDoubleSpinBox::tr(s, c, n));
}

//  QQuickDoubleSpinBox::QQuickDoubleSpinBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDoubleSpinBox *ritual_ZN19QQuickDoubleSpinBoxC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickDoubleSpinBox(parent);
}

//  QQuickDoubleSpinBox::~QQuickDoubleSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBoxD1Ev(QQuickDoubleSpinBox *self) {
  delete self;
}

//  void QQuickDoubleSpinBox::setFrom(double from)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox7setFromEd(
    QQuickDoubleSpinBox *self,
    double from) {
  self->setFrom(from);
}

//  void QQuickDoubleSpinBox::setTo(double to)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox5setToEd(
    QQuickDoubleSpinBox *self,
    double to) {
  self->setTo(to);
}

//  void QQuickDoubleSpinBox::setValue(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox8setValueEd(
    QQuickDoubleSpinBox *self,
    double value) {
  self->setValue(value);
}

//  void QQuickDoubleSpinBox::setStepSize(double step)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox11setStepSizeEd(
    QQuickDoubleSpinBox *self,
    double step) {
  self->setStepSize(step);
}

//  int QQuickDoubleSpinBox::decimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickDoubleSpinBox8decimalsEv(
    const QQuickDoubleSpinBox *self) {
  return self->decimals();
}

//  void QQuickDoubleSpinBox::setDecimals(int prec)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox11setDecimalsEi(
    QQuickDoubleSpinBox *self,
    int prec) {
  self->setDecimals(prec);
}

//  QJSValue QQuickDoubleSpinBox::textFromValue() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK19QQuickDoubleSpinBox13textFromValueEv(
    const QQuickDoubleSpinBox *self) {
  return new QJSValue(self->textFromValue());
}

//  QJSValue QQuickDoubleSpinBox::valueFromText() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK19QQuickDoubleSpinBox13valueFromTextEv(
    const QQuickDoubleSpinBox *self) {
  return new QJSValue(self->valueFromText());
}

//  void QQuickDoubleSpinBox::setWrap(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox7setWrapEb(
    QQuickDoubleSpinBox *self,
    bool wrap) {
  self->setWrap(wrap);
}

//  void QQuickDoubleSpinBox::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox8increaseEv(QQuickDoubleSpinBox *self) {
  self->increase();
}

//  void QQuickDoubleSpinBox::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox8decreaseEv(QQuickDoubleSpinBox *self) {
  self->decrease();
}

//  void QQuickDoubleSpinBox::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox11fromChangedEv(
    QQuickDoubleSpinBox *self) {
  self->fromChanged();
}

//  void QQuickDoubleSpinBox::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox9toChangedEv(QQuickDoubleSpinBox *self) {
  self->toChanged();
}

//  void QQuickDoubleSpinBox::valueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox12valueChangedEv(
    QQuickDoubleSpinBox *self) {
  self->valueChanged();
}

//  void QQuickDoubleSpinBox::stepSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15stepSizeChangedEv(
    QQuickDoubleSpinBox *self) {
  self->stepSizeChanged();
}

//  void QQuickDoubleSpinBox::decimalsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15decimalsChangedEv(
    QQuickDoubleSpinBox *self) {
  self->decimalsChanged();
}

//  void QQuickDoubleSpinBox::editableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15editableChangedEv(
    QQuickDoubleSpinBox *self) {
  self->editableChanged();
}

#if QT_CONFIG(validator)
//  void QQuickDoubleSpinBox::validatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox16validatorChangedEv(
    QQuickDoubleSpinBox *self) {
  self->validatorChanged();
}
#endif  // QT_CONFIG(validator)

//  void QQuickDoubleSpinBox::textFromValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox20textFromValueChangedEv(
    QQuickDoubleSpinBox *self) {
  self->textFromValueChanged();
}

//  void QQuickDoubleSpinBox::valueFromTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox20valueFromTextChangedEv(
    QQuickDoubleSpinBox *self) {
  self->valueFromTextChanged();
}

//  void QQuickDoubleSpinBox::valueModified()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox13valueModifiedEv(
    QQuickDoubleSpinBox *self) {
  self->valueModified();
}

//  void QQuickDoubleSpinBox::inputMethodHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox23inputMethodHintsChangedEv(
    QQuickDoubleSpinBox *self) {
  self->inputMethodHintsChanged();
}

//  void QQuickDoubleSpinBox::inputMethodComposingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox27inputMethodComposingChangedEv(
    QQuickDoubleSpinBox *self) {
  self->inputMethodComposingChanged();
}

//  void QQuickDoubleSpinBox::wrapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox11wrapChangedEv(
    QQuickDoubleSpinBox *self) {
  self->wrapChanged();
}

//  void QQuickDoubleSpinBox::displayTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox18displayTextChangedEv(
    QQuickDoubleSpinBox *self) {
  self->displayTextChanged();
}

//  void QQuickDoubleSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox12focusInEventEP11QFocusEvent(
    QQuickDoubleSpinBox *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickDoubleSpinBox::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15hoverEnterEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickDoubleSpinBox::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox14hoverMoveEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickDoubleSpinBox::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15hoverLeaveEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickDoubleSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox13keyPressEventEP9QKeyEvent(
    QQuickDoubleSpinBox *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickDoubleSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox15keyReleaseEventEP9QKeyEvent(
    QQuickDoubleSpinBox *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickDoubleSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox10timerEventEP11QTimerEvent(
    QQuickDoubleSpinBox *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickDoubleSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox10wheelEventEP11QWheelEvent(
    QQuickDoubleSpinBox *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickDoubleSpinBox::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox10classBeginEv(
    QQuickDoubleSpinBox *self) {
  self->classBegin();
}

//  void QQuickDoubleSpinBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox17componentCompleteEv(
    QQuickDoubleSpinBox *self) {
  self->componentComplete();
}

//  void QQuickDoubleSpinBox::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDoubleSpinBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickDoubleSpinBox::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox17contentItemChangeEP10QQuickItemS1_(
    QQuickDoubleSpinBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickDoubleSpinBox::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox12localeChangeERK7QLocaleS2_(
    QQuickDoubleSpinBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  QFont QQuickDoubleSpinBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickDoubleSpinBox11defaultFontEv(
    const QQuickDoubleSpinBox *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDoubleSpinBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickDoubleSpinBox14accessibleRoleEv(
    const QQuickDoubleSpinBox *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickDoubleSpinBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDoubleSpinBox26accessibilityActiveChangedEb(
    QQuickDoubleSpinBox *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickDoubleSpinBoxPrivate *QQuickDoubleSpinBox::d_func()
extern "C" Q_DECL_EXPORT
QQuickDoubleSpinBoxPrivate *ritual_ZN19QQuickDoubleSpinBox6d_funcEv(
    QQuickDoubleSpinBox *self) {
  return self->d_func();
}

//  const QQuickDoubleSpinBoxPrivate *QQuickDoubleSpinBox::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDoubleSpinBoxPrivate *ritual_ZNK19QQuickDoubleSpinBox6d_funcEv(
    const QQuickDoubleSpinBox *self) {
  return self->d_func();
}

//  QQuickControlPrivate *QQuickDoubleSpinBox::d_base_func()
extern "C" Q_DECL_EXPORT
QQuickControlPrivate *ritual_ZN19QQuickDoubleSpinBox11d_base_funcEv(
    QQuickDoubleSpinBox *self) {
  return self->d_base_func();
}

//  const QQuickControlPrivate *QQuickDoubleSpinBox::d_base_func() const
extern "C" Q_DECL_EXPORT
const QQuickControlPrivate *ritual_ZNK19QQuickDoubleSpinBox11d_base_funcEv(
    const QQuickDoubleSpinBox *self) {
  return self->d_base_func();
}

//  a Python function taken by a CuteQQuickDoubleSpinBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDoubleSpinBox(
    QQuickDoubleSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDoubleSpinBox *>(self)->take(key, call);
}

//  void QQuickDoubleSpinBox::increase()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox8increaseEv(
    QQuickDoubleSpinBox *self) {
  self->QQuickDoubleSpinBox::increase();
}

//  void QQuickDoubleSpinBox::decrease()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox8decreaseEv(
    QQuickDoubleSpinBox *self) {
  self->QQuickDoubleSpinBox::decrease();
}

//  void QQuickDoubleSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox12focusInEventEP11QFocusEvent(
    QQuickDoubleSpinBox *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::focusInEvent(
      event);
}

//  void QQuickDoubleSpinBox::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox15hoverEnterEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::hoverEnterEvent(
      event);
}

//  void QQuickDoubleSpinBox::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox14hoverMoveEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::hoverMoveEvent(
      event);
}

//  void QQuickDoubleSpinBox::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox15hoverLeaveEventEP11QHoverEvent(
    QQuickDoubleSpinBox *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::hoverLeaveEvent(
      event);
}

//  void QQuickDoubleSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox13keyPressEventEP9QKeyEvent(
    QQuickDoubleSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::keyPressEvent(
      event);
}

//  void QQuickDoubleSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox15keyReleaseEventEP9QKeyEvent(
    QQuickDoubleSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::keyReleaseEvent(
      event);
}

//  void QQuickDoubleSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox10timerEventEP11QTimerEvent(
    QQuickDoubleSpinBox *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::timerEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickDoubleSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox10wheelEventEP11QWheelEvent(
    QQuickDoubleSpinBox *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickDoubleSpinBox::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox10classBeginEv(
    QQuickDoubleSpinBox *self) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::classBegin();
}

//  void QQuickDoubleSpinBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox17componentCompleteEv(
    QQuickDoubleSpinBox *self) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::componentComplete();
}

//  void QQuickDoubleSpinBox::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDoubleSpinBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::itemChange(
      change,
      *value);
}

//  void QQuickDoubleSpinBox::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox17contentItemChangeEP10QQuickItemS1_(
    QQuickDoubleSpinBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickDoubleSpinBox::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox12localeChangeERK7QLocaleS2_(
    QQuickDoubleSpinBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::localeChange(
      *newLocale,
      *oldLocale);
}

//  QFont QQuickDoubleSpinBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickDoubleSpinBox11defaultFontEv(
    const QQuickDoubleSpinBox *self) {
  return new QFont(
      static_cast<const OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDoubleSpinBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickDoubleSpinBox14accessibleRoleEv(
    const QQuickDoubleSpinBox *self) {
  return static_cast<const OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickDoubleSpinBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDoubleSpinBox26accessibilityActiveChangedEb(
    QQuickDoubleSpinBox *self,
    bool active) {
  static_cast<OwnQQuickDoubleSpinBox *>(self)->OwnQQuickDoubleSpinBox::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
