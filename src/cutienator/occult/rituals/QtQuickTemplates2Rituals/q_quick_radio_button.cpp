//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickradiobutton_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickradiobutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickRadioButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRadioButton : QQuickRadioButton {
  using QQuickRadioButton::defaultFont;
  using QQuickRadioButton::accessibleRole;
};

//  A QQuickRadioButton that Python can take functions over in. Every QQuickRadioButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QFont * (*CuteQQuickRadioButtonCall0)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickRadioButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickRadioButtonCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRadioButtonCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall4)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall5)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall8)(const void *, QMouseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall10)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickRadioButtonCall11)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickRadioButtonCall12)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickRadioButtonCall13)(const void *, int *);
typedef void (*CuteQQuickRadioButtonCall14)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall15)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall17)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRadioButtonCall20)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickRadioButtonCall21)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickRadioButtonCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRadioButtonCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRadioButtonCall24)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRadioButtonCall25)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall26)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRadioButtonCall27)(const void *, int *);
typedef void (*CuteQQuickRadioButtonCall28)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickRadioButtonCall29)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickRadioButtonCall30)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickRadioButtonCall31)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickRadioButtonCall32)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickRadioButtonCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickRadioButtonCall34)(const void *, int *);
typedef const QRectF * (*CuteQQuickRadioButtonCall35)(const void *, int *);
typedef bool (*CuteQQuickRadioButtonCall36)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRadioButtonCall37)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRadioButtonCall38)(const void *, int *);
typedef void * (*CuteQQuickRadioButtonCall39)(const void *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRadioButtonCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRadioButtonCall41)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRadioButtonCall42)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRadioButtonCall43)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRadioButtonCall44)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRadioButtonCall45)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickRadioButtonCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRadioButtonCall47)(const void *, int *);
typedef void (*CuteQQuickRadioButtonCall48)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRadioButtonCall49)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRadioButtonCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRadioButton : public QQuickRadioButton {
public:
  using QQuickRadioButton::QQuickRadioButton;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractButton14nextCheckStateEv")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[36] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[39] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[48] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QFont QQuickRadioButton::defaultFont() const
  QFont defaultFont() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRadioButtonCall0 call = reinterpret_cast<CuteQQuickRadioButtonCall0>(taken[0]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickRadioButton::defaultFont();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickRadioButton::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRadioButtonCall1 call = reinterpret_cast<CuteQQuickRadioButtonCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickRadioButton::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickAbstractButton::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRadioButtonCall2 call = reinterpret_cast<CuteQQuickRadioButtonCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickAbstractButton::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRadioButtonCall3 call = reinterpret_cast<CuteQQuickRadioButtonCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButton::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickAbstractButton::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRadioButtonCall4 call = reinterpret_cast<CuteQQuickRadioButtonCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::focusOutEvent(event);
  }

  //  void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRadioButtonCall5 call = reinterpret_cast<CuteQQuickRadioButtonCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::keyPressEvent(event);
  }

  //  void QQuickAbstractButton::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRadioButtonCall6 call = reinterpret_cast<CuteQQuickRadioButtonCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::keyReleaseEvent(event);
  }

  //  void QQuickAbstractButton::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRadioButtonCall7 call = reinterpret_cast<CuteQQuickRadioButtonCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::mousePressEvent(event);
  }

  //  void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRadioButtonCall8 call = reinterpret_cast<CuteQQuickRadioButtonCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::mouseDoubleClickEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickAbstractButton::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRadioButtonCall9 call = reinterpret_cast<CuteQQuickRadioButtonCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickAbstractButton::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRadioButtonCall10 call = reinterpret_cast<CuteQQuickRadioButtonCall10>(taken[10]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::itemChange(change, value);
  }

  //  void QQuickAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRadioButtonCall11 call = reinterpret_cast<CuteQQuickRadioButtonCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::nextCheckState();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickAbstractButton::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRadioButtonCall12 call = reinterpret_cast<CuteQQuickRadioButtonCall12>(taken[12]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRadioButtonCall13 call = reinterpret_cast<CuteQQuickRadioButtonCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRadioButtonCall14 call = reinterpret_cast<CuteQQuickRadioButtonCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRadioButtonCall15 call = reinterpret_cast<CuteQQuickRadioButtonCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRadioButtonCall16 call = reinterpret_cast<CuteQQuickRadioButtonCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRadioButtonCall17 call = reinterpret_cast<CuteQQuickRadioButtonCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRadioButtonCall18 call = reinterpret_cast<CuteQQuickRadioButtonCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRadioButtonCall19 call = reinterpret_cast<CuteQQuickRadioButtonCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRadioButtonCall20 call = reinterpret_cast<CuteQQuickRadioButtonCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRadioButtonCall21 call = reinterpret_cast<CuteQQuickRadioButtonCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRadioButtonCall22 call = reinterpret_cast<CuteQQuickRadioButtonCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRadioButtonCall23 call = reinterpret_cast<CuteQQuickRadioButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickControl::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickRadioButtonCall24 call = reinterpret_cast<CuteQQuickRadioButtonCall24>(taken[24]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickRadioButtonCall25 call = reinterpret_cast<CuteQQuickRadioButtonCall25>(taken[25]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRadioButtonCall26 call = reinterpret_cast<CuteQQuickRadioButtonCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRadioButtonCall27 call = reinterpret_cast<CuteQQuickRadioButtonCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRadioButtonCall28 call = reinterpret_cast<CuteQQuickRadioButtonCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQuickRadioButtonCall29 call = reinterpret_cast<CuteQQuickRadioButtonCall29>(taken[29]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickRadioButtonCall30 call = reinterpret_cast<CuteQQuickRadioButtonCall30>(taken[30]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickControl::contentItemChange(newItem, oldItem);
  }

  //  void QQuickControl::localeChange(const QLocale &newLocale, const
  //      QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickRadioButtonCall31 call = reinterpret_cast<CuteQQuickRadioButtonCall31>(taken[31]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickControl::localeChange(newLocale, oldLocale);
  }

  //  void QQuickControl::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickRadioButtonCall32 call = reinterpret_cast<CuteQQuickRadioButtonCall32>(taken[32]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickRadioButtonCall33 call = reinterpret_cast<CuteQQuickRadioButtonCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickRadioButtonCall34 call = reinterpret_cast<CuteQQuickRadioButtonCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickRadioButtonCall35 call = reinterpret_cast<CuteQQuickRadioButtonCall35>(taken[35]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickRadioButtonCall36 call = reinterpret_cast<CuteQQuickRadioButtonCall36>(taken[36]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickRadioButtonCall37 call = reinterpret_cast<CuteQQuickRadioButtonCall37>(taken[37]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickRadioButtonCall38 call = reinterpret_cast<CuteQQuickRadioButtonCall38>(taken[38]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickRadioButtonCall39 call = reinterpret_cast<CuteQQuickRadioButtonCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickRadioButtonCall40 call = reinterpret_cast<CuteQQuickRadioButtonCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickRadioButtonCall41 call = reinterpret_cast<CuteQQuickRadioButtonCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickRadioButtonCall42 call = reinterpret_cast<CuteQQuickRadioButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickRadioButtonCall43 call = reinterpret_cast<CuteQQuickRadioButtonCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickRadioButtonCall44 call = reinterpret_cast<CuteQQuickRadioButtonCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickRadioButtonCall45 call = reinterpret_cast<CuteQQuickRadioButtonCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQQuickRadioButtonCall46 call = reinterpret_cast<CuteQQuickRadioButtonCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickRadioButtonCall47 call = reinterpret_cast<CuteQQuickRadioButtonCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickRadioButtonCall48 call = reinterpret_cast<CuteQQuickRadioButtonCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickRadioButtonCall49 call = reinterpret_cast<CuteQQuickRadioButtonCall49>(taken[49]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickRadioButtonCall50 call = reinterpret_cast<CuteQQuickRadioButtonCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickRadioButtonCall51 call = reinterpret_cast<CuteQQuickRadioButtonCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickRadioButtonCall52 call = reinterpret_cast<CuteQQuickRadioButtonCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickRadioButtonCall53 call = reinterpret_cast<CuteQQuickRadioButtonCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRadioButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickRadioButton10metaObjectEv(
    const QQuickRadioButton *self) {
  return self->metaObject();
}

//  QString QQuickRadioButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickRadioButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRadioButton::tr(s, c, n));
}

//  QQuickRadioButton::QQuickRadioButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRadioButton *ritual_ZN17QQuickRadioButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRadioButton(parent);
}

//  QFont QQuickRadioButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickRadioButton11defaultFontEv(
    const QQuickRadioButton *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRadioButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickRadioButton14accessibleRoleEv(
    const QQuickRadioButton *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQQuickRadioButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRadioButton(
    QQuickRadioButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRadioButton *>(self)->take(key, call);
}

//  QFont QQuickRadioButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK17QQuickRadioButton11defaultFontEv(
    const QQuickRadioButton *self) {
  return new QFont(
      static_cast<const OwnQQuickRadioButton *>(self)->OwnQQuickRadioButton::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRadioButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QQuickRadioButton14accessibleRoleEv(
    const QQuickRadioButton *self) {
  return static_cast<const OwnQQuickRadioButton *>(self)->OwnQQuickRadioButton::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
