//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(shortcut)
#include <QtGui/qkeysequence.h>
#endif
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickAbstractButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAbstractButton : QQuickAbstractButton {
  using QQuickAbstractButton::componentComplete;
  using QQuickAbstractButton::event;
  using QQuickAbstractButton::focusOutEvent;
  using QQuickAbstractButton::keyPressEvent;
  using QQuickAbstractButton::keyReleaseEvent;
  using QQuickAbstractButton::mousePressEvent;
  using QQuickAbstractButton::mouseDoubleClickEvent;
  using QQuickAbstractButton::timerEvent;
  using QQuickAbstractButton::itemChange;
  using QQuickAbstractButton::nextCheckState;
  using QQuickAbstractButton::accessibilityActiveChanged;
  using QQuickAbstractButton::accessibleRole;
};

//  A QQuickAbstractButton that Python can take functions over in. Every QQuickAbstractButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAbstractButtonCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractButtonCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall2)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall3)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall6)(const void *, QMouseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall8)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickAbstractButtonCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractButtonCall10)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickAbstractButtonCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickAbstractButtonCall12)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonCall13)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonCall14)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall15)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall17)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractButtonCall20)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractButtonCall21)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractButtonCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAbstractButtonCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAbstractButtonCall24)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickAbstractButtonCall25)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall26)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractButtonCall27)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonCall28)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickAbstractButtonCall29)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickAbstractButtonCall30)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractButtonCall31)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickAbstractButtonCall32)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickAbstractButtonCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickAbstractButtonCall34)(const void *, int *);
typedef const QRectF * (*CuteQQuickAbstractButtonCall35)(const void *, int *);
typedef bool (*CuteQQuickAbstractButtonCall36)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickAbstractButtonCall37)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickAbstractButtonCall38)(const void *, int *);
typedef void * (*CuteQQuickAbstractButtonCall39)(const void *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickAbstractButtonCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractButtonCall41)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractButtonCall42)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractButtonCall43)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractButtonCall44)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickAbstractButtonCall45)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickAbstractButtonCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickAbstractButtonCall47)(const void *, int *);
typedef void (*CuteQQuickAbstractButtonCall48)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractButtonCall49)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractButtonCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAbstractButton : public QQuickAbstractButton {
public:
  using QQuickAbstractButton::QQuickAbstractButton;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractButton14nextCheckStateEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[12] = call;
      return true;
    }
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

  //  void QQuickAbstractButton::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall0 call = reinterpret_cast<CuteQQuickAbstractButtonCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickAbstractButton::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall1 call = reinterpret_cast<CuteQQuickAbstractButtonCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButton::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickAbstractButton::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall2 call = reinterpret_cast<CuteQQuickAbstractButtonCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::focusOutEvent(event);
  }

  //  void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall3 call = reinterpret_cast<CuteQQuickAbstractButtonCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::keyPressEvent(event);
  }

  //  void QQuickAbstractButton::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall4 call = reinterpret_cast<CuteQQuickAbstractButtonCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::keyReleaseEvent(event);
  }

  //  void QQuickAbstractButton::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall5 call = reinterpret_cast<CuteQQuickAbstractButtonCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::mousePressEvent(event);
  }

  //  void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall6 call = reinterpret_cast<CuteQQuickAbstractButtonCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::mouseDoubleClickEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickAbstractButton::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall7 call = reinterpret_cast<CuteQQuickAbstractButtonCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall8 call = reinterpret_cast<CuteQQuickAbstractButtonCall8>(taken[8]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::itemChange(change, value);
  }

  //  void QQuickAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall9 call = reinterpret_cast<CuteQQuickAbstractButtonCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::nextCheckState();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickAbstractButton::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall10 call = reinterpret_cast<CuteQQuickAbstractButtonCall10>(taken[10]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickAbstractButton::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickAbstractButton::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall11 call = reinterpret_cast<CuteQQuickAbstractButtonCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickAbstractButton::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall12 call = reinterpret_cast<CuteQQuickAbstractButtonCall12>(taken[12]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall13 call = reinterpret_cast<CuteQQuickAbstractButtonCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall14 call = reinterpret_cast<CuteQQuickAbstractButtonCall14>(taken[14]);
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
      CuteQQuickAbstractButtonCall15 call = reinterpret_cast<CuteQQuickAbstractButtonCall15>(taken[15]);
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
      CuteQQuickAbstractButtonCall16 call = reinterpret_cast<CuteQQuickAbstractButtonCall16>(taken[16]);
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
      CuteQQuickAbstractButtonCall17 call = reinterpret_cast<CuteQQuickAbstractButtonCall17>(taken[17]);
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
      CuteQQuickAbstractButtonCall18 call = reinterpret_cast<CuteQQuickAbstractButtonCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall19 call = reinterpret_cast<CuteQQuickAbstractButtonCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall20 call = reinterpret_cast<CuteQQuickAbstractButtonCall20>(taken[20]);
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
      CuteQQuickAbstractButtonCall21 call = reinterpret_cast<CuteQQuickAbstractButtonCall21>(taken[21]);
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
      CuteQQuickAbstractButtonCall22 call = reinterpret_cast<CuteQQuickAbstractButtonCall22>(taken[22]);
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
      CuteQQuickAbstractButtonCall23 call = reinterpret_cast<CuteQQuickAbstractButtonCall23>(taken[23]);
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
      CuteQQuickAbstractButtonCall24 call = reinterpret_cast<CuteQQuickAbstractButtonCall24>(taken[24]);
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
      CuteQQuickAbstractButtonCall25 call = reinterpret_cast<CuteQQuickAbstractButtonCall25>(taken[25]);
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
      CuteQQuickAbstractButtonCall26 call = reinterpret_cast<CuteQQuickAbstractButtonCall26>(taken[26]);
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
      CuteQQuickAbstractButtonCall27 call = reinterpret_cast<CuteQQuickAbstractButtonCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall28 call = reinterpret_cast<CuteQQuickAbstractButtonCall28>(taken[28]);
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
      CuteQQuickAbstractButtonCall29 call = reinterpret_cast<CuteQQuickAbstractButtonCall29>(taken[29]);
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
      CuteQQuickAbstractButtonCall30 call = reinterpret_cast<CuteQQuickAbstractButtonCall30>(taken[30]);
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
      CuteQQuickAbstractButtonCall31 call = reinterpret_cast<CuteQQuickAbstractButtonCall31>(taken[31]);
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
      CuteQQuickAbstractButtonCall32 call = reinterpret_cast<CuteQQuickAbstractButtonCall32>(taken[32]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall33 call = reinterpret_cast<CuteQQuickAbstractButtonCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall34 call = reinterpret_cast<CuteQQuickAbstractButtonCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall35 call = reinterpret_cast<CuteQQuickAbstractButtonCall35>(taken[35]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall36 call = reinterpret_cast<CuteQQuickAbstractButtonCall36>(taken[36]);
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
      CuteQQuickAbstractButtonCall37 call = reinterpret_cast<CuteQQuickAbstractButtonCall37>(taken[37]);
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
      CuteQQuickAbstractButtonCall38 call = reinterpret_cast<CuteQQuickAbstractButtonCall38>(taken[38]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall39 call = reinterpret_cast<CuteQQuickAbstractButtonCall39>(taken[39]);
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
      CuteQQuickAbstractButtonCall40 call = reinterpret_cast<CuteQQuickAbstractButtonCall40>(taken[40]);
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
      CuteQQuickAbstractButtonCall41 call = reinterpret_cast<CuteQQuickAbstractButtonCall41>(taken[41]);
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
      CuteQQuickAbstractButtonCall42 call = reinterpret_cast<CuteQQuickAbstractButtonCall42>(taken[42]);
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
      CuteQQuickAbstractButtonCall43 call = reinterpret_cast<CuteQQuickAbstractButtonCall43>(taken[43]);
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
      CuteQQuickAbstractButtonCall44 call = reinterpret_cast<CuteQQuickAbstractButtonCall44>(taken[44]);
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
      CuteQQuickAbstractButtonCall45 call = reinterpret_cast<CuteQQuickAbstractButtonCall45>(taken[45]);
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
      CuteQQuickAbstractButtonCall46 call = reinterpret_cast<CuteQQuickAbstractButtonCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall47 call = reinterpret_cast<CuteQQuickAbstractButtonCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickAbstractButtonCall48 call = reinterpret_cast<CuteQQuickAbstractButtonCall48>(taken[48]);
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
      CuteQQuickAbstractButtonCall49 call = reinterpret_cast<CuteQQuickAbstractButtonCall49>(taken[49]);
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
      CuteQQuickAbstractButtonCall50 call = reinterpret_cast<CuteQQuickAbstractButtonCall50>(taken[50]);
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
      CuteQQuickAbstractButtonCall51 call = reinterpret_cast<CuteQQuickAbstractButtonCall51>(taken[51]);
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
      CuteQQuickAbstractButtonCall52 call = reinterpret_cast<CuteQQuickAbstractButtonCall52>(taken[52]);
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
      CuteQQuickAbstractButtonCall53 call = reinterpret_cast<CuteQQuickAbstractButtonCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAbstractButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickAbstractButton10metaObjectEv(
    const QQuickAbstractButton *self) {
  return self->metaObject();
}

//  void *QQuickAbstractButton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickAbstractButton11qt_metacastEPKc(
    QQuickAbstractButton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAbstractButton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickAbstractButton11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAbstractButton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAbstractButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickAbstractButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAbstractButton::tr(s, c, n));
}

//  QQuickAbstractButton::QQuickAbstractButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZN20QQuickAbstractButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickAbstractButton(parent);
}

//  QQuickAbstractButton::~QQuickAbstractButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButtonD1Ev(QQuickAbstractButton *self) {
  delete self;
}

//  QString QQuickAbstractButton::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickAbstractButton4textEv(
    const QQuickAbstractButton *self) {
  return new QString(self->text());
}

//  void QQuickAbstractButton::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7setTextERK7QString(
    QQuickAbstractButton *self,
    const QString *text) {
  self->setText(*text);
}

//  void QQuickAbstractButton::resetText()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton9resetTextEv(
    QQuickAbstractButton *self) {
  self->resetText();
}

//  bool QQuickAbstractButton::isDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton6isDownEv(
    const QQuickAbstractButton *self) {
  return self->isDown();
}

//  void QQuickAbstractButton::setDown(bool down)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7setDownEb(
    QQuickAbstractButton *self,
    bool down) {
  self->setDown(down);
}

//  void QQuickAbstractButton::resetDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton9resetDownEv(
    QQuickAbstractButton *self) {
  self->resetDown();
}

//  bool QQuickAbstractButton::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton9isPressedEv(
    const QQuickAbstractButton *self) {
  return self->isPressed();
}

//  void QQuickAbstractButton::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton10setPressedEb(
    QQuickAbstractButton *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  bool QQuickAbstractButton::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton9isCheckedEv(
    const QQuickAbstractButton *self) {
  return self->isChecked();
}

//  void QQuickAbstractButton::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton10setCheckedEb(
    QQuickAbstractButton *self,
    bool checked) {
  self->setChecked(checked);
}

//  bool QQuickAbstractButton::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton11isCheckableEv(
    const QQuickAbstractButton *self) {
  return self->isCheckable();
}

//  void QQuickAbstractButton::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton12setCheckableEb(
    QQuickAbstractButton *self,
    bool checkable) {
  self->setCheckable(checkable);
}

//  bool QQuickAbstractButton::autoExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton13autoExclusiveEv(
    const QQuickAbstractButton *self) {
  return self->autoExclusive();
}

//  void QQuickAbstractButton::setAutoExclusive(bool exclusive)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton16setAutoExclusiveEb(
    QQuickAbstractButton *self,
    bool exclusive) {
  self->setAutoExclusive(exclusive);
}

//  bool QQuickAbstractButton::autoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractButton10autoRepeatEv(
    const QQuickAbstractButton *self) {
  return self->autoRepeat();
}

//  void QQuickAbstractButton::setAutoRepeat(bool repeat)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13setAutoRepeatEb(
    QQuickAbstractButton *self,
    bool repeat) {
  self->setAutoRepeat(repeat);
}

//  QQuickItem *QQuickAbstractButton::indicator() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickAbstractButton9indicatorEv(
    const QQuickAbstractButton *self) {
  return self->indicator();
}

//  void QQuickAbstractButton::setIndicator(QQuickItem *indicator)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton12setIndicatorEP10QQuickItem(
    QQuickAbstractButton *self,
    QQuickItem *indicator) {
  self->setIndicator(indicator);
}

//  QQuickIcon QQuickAbstractButton::icon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK20QQuickAbstractButton4iconEv(
    const QQuickAbstractButton *self) {
  return new QQuickIcon(self->icon());
}

//  void QQuickAbstractButton::setIcon(const QQuickIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7setIconERK10QQuickIcon(
    QQuickAbstractButton *self,
    const QQuickIcon *icon) {
  self->setIcon(*icon);
}

//  Display QQuickAbstractButton::display() const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton::Display ritual_ZNK20QQuickAbstractButton7displayEv(
    const QQuickAbstractButton *self) {
  return self->display();
}

//  void QQuickAbstractButton::setDisplay(Display display)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton10setDisplayENS_7DisplayE(
    QQuickAbstractButton *self,
    QQuickAbstractButton::Display display) {
  self->setDisplay(display);
}

//  QQuickAction *QQuickAbstractButton::action() const
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZNK20QQuickAbstractButton6actionEv(
    const QQuickAbstractButton *self) {
  return self->action();
}

//  void QQuickAbstractButton::setAction(QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton9setActionEP12QQuickAction(
    QQuickAbstractButton *self,
    QQuickAction *action) {
  self->setAction(action);
}

#if QT_CONFIG(shortcut)
//  QKeySequence QQuickAbstractButton::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK20QQuickAbstractButton8shortcutEv(
    const QQuickAbstractButton *self) {
  return new QKeySequence(self->shortcut());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QQuickAbstractButton::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton11setShortcutERK12QKeySequence(
    QQuickAbstractButton *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

//  int QQuickAbstractButton::autoRepeatDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAbstractButton15autoRepeatDelayEv(
    const QQuickAbstractButton *self) {
  return self->autoRepeatDelay();
}

//  void QQuickAbstractButton::setAutoRepeatDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton18setAutoRepeatDelayEi(
    QQuickAbstractButton *self,
    int delay) {
  self->setAutoRepeatDelay(delay);
}

//  int QQuickAbstractButton::autoRepeatInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAbstractButton18autoRepeatIntervalEv(
    const QQuickAbstractButton *self) {
  return self->autoRepeatInterval();
}

//  void QQuickAbstractButton::setAutoRepeatInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton21setAutoRepeatIntervalEi(
    QQuickAbstractButton *self,
    int interval) {
  self->setAutoRepeatInterval(interval);
}

//  qreal QQuickAbstractButton::pressX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAbstractButton6pressXEv(
    const QQuickAbstractButton *self) {
  return self->pressX();
}

//  qreal QQuickAbstractButton::pressY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAbstractButton6pressYEv(
    const QQuickAbstractButton *self) {
  return self->pressY();
}

//  qreal QQuickAbstractButton::implicitIndicatorWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAbstractButton22implicitIndicatorWidthEv(
    const QQuickAbstractButton *self) {
  return self->implicitIndicatorWidth();
}

//  qreal QQuickAbstractButton::implicitIndicatorHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickAbstractButton23implicitIndicatorHeightEv(
    const QQuickAbstractButton *self) {
  return self->implicitIndicatorHeight();
}

//  void QQuickAbstractButton::toggle()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton6toggleEv(QQuickAbstractButton *self) {
  self->toggle();
}

//  void QQuickAbstractButton::click()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton5clickEv(QQuickAbstractButton *self) {
  self->click();
}

//  void QQuickAbstractButton::animateClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton12animateClickEv(
    QQuickAbstractButton *self) {
  self->animateClick();
}

//  void QQuickAbstractButton::pressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7pressedEv(QQuickAbstractButton *self) {
  self->pressed();
}

//  void QQuickAbstractButton::released()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton8releasedEv(QQuickAbstractButton *self) {
  self->released();
}

//  void QQuickAbstractButton::canceled()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton8canceledEv(QQuickAbstractButton *self) {
  self->canceled();
}

//  void QQuickAbstractButton::clicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7clickedEv(QQuickAbstractButton *self) {
  self->clicked();
}

//  void QQuickAbstractButton::pressAndHold()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton12pressAndHoldEv(
    QQuickAbstractButton *self) {
  self->pressAndHold();
}

//  void QQuickAbstractButton::doubleClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13doubleClickedEv(
    QQuickAbstractButton *self) {
  self->doubleClicked();
}

//  void QQuickAbstractButton::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton11textChangedEv(
    QQuickAbstractButton *self) {
  self->textChanged();
}

//  void QQuickAbstractButton::downChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton11downChangedEv(
    QQuickAbstractButton *self) {
  self->downChanged();
}

//  void QQuickAbstractButton::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton14pressedChangedEv(
    QQuickAbstractButton *self) {
  self->pressedChanged();
}

//  void QQuickAbstractButton::checkedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton14checkedChangedEv(
    QQuickAbstractButton *self) {
  self->checkedChanged();
}

//  void QQuickAbstractButton::checkableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton16checkableChangedEv(
    QQuickAbstractButton *self) {
  self->checkableChanged();
}

//  void QQuickAbstractButton::autoExclusiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton20autoExclusiveChangedEv(
    QQuickAbstractButton *self) {
  self->autoExclusiveChanged();
}

//  void QQuickAbstractButton::autoRepeatChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton17autoRepeatChangedEv(
    QQuickAbstractButton *self) {
  self->autoRepeatChanged();
}

//  void QQuickAbstractButton::indicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton16indicatorChangedEv(
    QQuickAbstractButton *self) {
  self->indicatorChanged();
}

//  void QQuickAbstractButton::toggled()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton7toggledEv(QQuickAbstractButton *self) {
  self->toggled();
}

//  void QQuickAbstractButton::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton11iconChangedEv(
    QQuickAbstractButton *self) {
  self->iconChanged();
}

//  void QQuickAbstractButton::displayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton14displayChangedEv(
    QQuickAbstractButton *self) {
  self->displayChanged();
}

//  void QQuickAbstractButton::actionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13actionChangedEv(
    QQuickAbstractButton *self) {
  self->actionChanged();
}

//  void QQuickAbstractButton::autoRepeatDelayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton22autoRepeatDelayChangedEv(
    QQuickAbstractButton *self) {
  self->autoRepeatDelayChanged();
}

//  void QQuickAbstractButton::autoRepeatIntervalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton25autoRepeatIntervalChangedEv(
    QQuickAbstractButton *self) {
  self->autoRepeatIntervalChanged();
}

//  void QQuickAbstractButton::pressXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13pressXChangedEv(
    QQuickAbstractButton *self) {
  self->pressXChanged();
}

//  void QQuickAbstractButton::pressYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13pressYChangedEv(
    QQuickAbstractButton *self) {
  self->pressYChanged();
}

//  void QQuickAbstractButton::implicitIndicatorWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton29implicitIndicatorWidthChangedEv(
    QQuickAbstractButton *self) {
  self->implicitIndicatorWidthChanged();
}

//  void QQuickAbstractButton::implicitIndicatorHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton30implicitIndicatorHeightChangedEv(
    QQuickAbstractButton *self) {
  self->implicitIndicatorHeightChanged();
}

//  QQuickAbstractButton::QQuickAbstractButton(QQuickAbstractButtonPrivate
//      &dd, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZN20QQuickAbstractButtonC1ER27QQuickAbstractButtonPrivateP10QQuickItem(
    QQuickAbstractButtonPrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickAbstractButton(*dd, parent);
}

//  void QQuickAbstractButton::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton17componentCompleteEv(
    QQuickAbstractButton *self) {
  self->componentComplete();
}

//  bool QQuickAbstractButton::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickAbstractButton5eventEP6QEvent(
    QQuickAbstractButton *self,
    QEvent *event) {
  return self->event(event);
}

//  void QQuickAbstractButton::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13focusOutEventEP11QFocusEvent(
    QQuickAbstractButton *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton13keyPressEventEP9QKeyEvent(
    QQuickAbstractButton *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickAbstractButton::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton15keyReleaseEventEP9QKeyEvent(
    QQuickAbstractButton *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickAbstractButton::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton15mousePressEventEP11QMouseEvent(
    QQuickAbstractButton *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton21mouseDoubleClickEventEP11QMouseEvent(
    QQuickAbstractButton *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickAbstractButton::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton10timerEventEP11QTimerEvent(
    QQuickAbstractButton *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQuickAbstractButton::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickAbstractButton *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickAbstractButton::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton12buttonChangeENS_12ButtonChangeE(
    QQuickAbstractButton *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  void QQuickAbstractButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton14nextCheckStateEv(
    QQuickAbstractButton *self) {
  self->nextCheckState();
}

#if QT_CONFIG(accessibility)
//  void QQuickAbstractButton::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton26accessibilityActiveChangedEb(
    QQuickAbstractButton *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickAbstractButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QQuickAbstractButton14accessibleRoleEv(
    const QQuickAbstractButton *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickAbstractButton::accessiblePressAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton21accessiblePressActionEv(
    QQuickAbstractButton *self) {
  self->accessiblePressAction();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickAbstractButton::accessibleToggleAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractButton22accessibleToggleActionEv(
    QQuickAbstractButton *self) {
  self->accessibleToggleAction();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickAbstractButtonPrivate *QQuickAbstractButton::d_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractButtonPrivate *ritual_ZN20QQuickAbstractButton6d_funcEv(
    QQuickAbstractButton *self) {
  return self->d_func();
}

//  const QQuickAbstractButtonPrivate *QQuickAbstractButton::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAbstractButtonPrivate *ritual_ZNK20QQuickAbstractButton6d_funcEv(
    const QQuickAbstractButton *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAbstractButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractButton(
    QQuickAbstractButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractButton *>(self)->take(key, call);
}

//  void QQuickAbstractButton::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton17componentCompleteEv(
    QQuickAbstractButton *self) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::componentComplete();
}

//  bool QQuickAbstractButton::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickAbstractButton5eventEP6QEvent(
    QQuickAbstractButton *self,
    QEvent *event) {
  return static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::event(
      event);
}

//  void QQuickAbstractButton::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton13focusOutEventEP11QFocusEvent(
    QQuickAbstractButton *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::focusOutEvent(
      event);
}

//  void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton13keyPressEventEP9QKeyEvent(
    QQuickAbstractButton *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::keyPressEvent(
      event);
}

//  void QQuickAbstractButton::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton15keyReleaseEventEP9QKeyEvent(
    QQuickAbstractButton *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::keyReleaseEvent(
      event);
}

//  void QQuickAbstractButton::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton15mousePressEventEP11QMouseEvent(
    QQuickAbstractButton *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::mousePressEvent(
      event);
}

//  void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton21mouseDoubleClickEventEP11QMouseEvent(
    QQuickAbstractButton *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::mouseDoubleClickEvent(
      event);
}

//  void QQuickAbstractButton::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton10timerEventEP11QTimerEvent(
    QQuickAbstractButton *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::timerEvent(
      event);
}

//  void QQuickAbstractButton::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickAbstractButton *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::itemChange(
      change,
      *value);
}

//  void QQuickAbstractButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton14nextCheckStateEv(
    QQuickAbstractButton *self) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::nextCheckState();
}

#if QT_CONFIG(accessibility)
//  void QQuickAbstractButton::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractButton26accessibilityActiveChangedEb(
    QQuickAbstractButton *self,
    bool active) {
  static_cast<OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickAbstractButton::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK20QQuickAbstractButton14accessibleRoleEv(
    const QQuickAbstractButton *self) {
  return static_cast<const OwnQQuickAbstractButton *>(self)->OwnQQuickAbstractButton::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QList<QQuickAbstractButton *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickAbstractButton *> *ritual_list_make_QQuickAbstractButton_ptr() {
  return new QList<QQuickAbstractButton *>();
}

//  void QList<QQuickAbstractButton *>::append(const QQuickAbstractButton *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickAbstractButton_ptr(
    QList<QQuickAbstractButton *> *self,
    QQuickAbstractButton *element) {
  self->append(element);
}

//  qsizetype QList<QQuickAbstractButton *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickAbstractButton_ptr(
    const QList<QQuickAbstractButton *> *self) {
  return self->size();
}

//  const QQuickAbstractButton * &QList<QQuickAbstractButton *>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_list_at_QQuickAbstractButton_ptr(
    const QList<QQuickAbstractButton *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickAbstractButton *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickAbstractButton_ptr(
    QList<QQuickAbstractButton *> *self) {
  delete self;
}
