//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickslider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickslider_p.h>
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

//  Only a class built on QQuickSlider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSlider : QQuickSlider {
  using QQuickSlider::keyPressEvent;
  using QQuickSlider::keyReleaseEvent;
  using QQuickSlider::mousePressEvent;
  using QQuickSlider::touchEvent;
  using QQuickSlider::wheelEvent;
  using QQuickSlider::mirrorChange;
  using QQuickSlider::componentComplete;
  using QQuickSlider::accessibilityActiveChanged;
  using QQuickSlider::accessibleRole;
};

//  A QQuickSlider that Python can take functions over in. Every QQuickSlider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSliderCall0)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSliderCall1)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSliderCall2)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSliderCall3)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSliderCall4)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSliderCall5)(const void *, int *);
typedef void (*CuteQQuickSliderCall6)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSliderCall7)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSliderCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickSliderCall9)(const void *, int *);
typedef void (*CuteQQuickSliderCall10)(const void *, int *);
typedef void (*CuteQQuickSliderCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickSliderCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSliderCall13)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall14)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall15)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSliderCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSliderCall19)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSliderCall20)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSliderCall21)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickSliderCall22)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSliderCall24)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickSliderCall25)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSliderCall26)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSliderCall27)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickSliderCall28)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSliderCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickSliderCall30)(const void *, int *);
typedef const QRectF * (*CuteQQuickSliderCall31)(const void *, int *);
typedef bool (*CuteQQuickSliderCall32)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickSliderCall33)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickSliderCall34)(const void *, int *);
typedef void * (*CuteQQuickSliderCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSliderCall36)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef void (*CuteQQuickSliderCall37)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickSliderCall38)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSliderCall39)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSliderCall40)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSliderCall41)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSliderCall42)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickSliderCall43)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickSliderCall44)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickSliderCall45)(const void *, int *);
typedef void (*CuteQQuickSliderCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSliderCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSliderCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSliderCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSliderCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSliderCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSliderCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSlider : public QQuickSlider {
public:
  using QQuickSlider::QQuickSlider;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[32] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[38] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickSlider::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSliderCall0 call = reinterpret_cast<CuteQQuickSliderCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSlider::keyPressEvent(event);
  }

  //  void QQuickSlider::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSliderCall1 call = reinterpret_cast<CuteQQuickSliderCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSlider::keyReleaseEvent(event);
  }

  //  void QQuickSlider::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSliderCall2 call = reinterpret_cast<CuteQQuickSliderCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSlider::mousePressEvent(event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickSlider::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSliderCall3 call = reinterpret_cast<CuteQQuickSliderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSlider::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickSlider::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSliderCall4 call = reinterpret_cast<CuteQQuickSliderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSlider::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickSlider::mirrorChange()
  void mirrorChange() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSliderCall5 call = reinterpret_cast<CuteQQuickSliderCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSlider::mirrorChange();
  }

  //  void QQuickSlider::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSliderCall6 call = reinterpret_cast<CuteQQuickSliderCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSlider::componentComplete();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickSlider::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSliderCall7 call = reinterpret_cast<CuteQQuickSliderCall7>(taken[7]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickSlider::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickSlider::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSliderCall8 call = reinterpret_cast<CuteQQuickSliderCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickSlider::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSliderCall9 call = reinterpret_cast<CuteQQuickSliderCall9>(taken[9]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSliderCall10 call = reinterpret_cast<CuteQQuickSliderCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSliderCall11 call = reinterpret_cast<CuteQQuickSliderCall11>(taken[11]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSliderCall12 call = reinterpret_cast<CuteQQuickSliderCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSliderCall13 call = reinterpret_cast<CuteQQuickSliderCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSliderCall14 call = reinterpret_cast<CuteQQuickSliderCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSliderCall15 call = reinterpret_cast<CuteQQuickSliderCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSliderCall16 call = reinterpret_cast<CuteQQuickSliderCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSliderCall17 call = reinterpret_cast<CuteQQuickSliderCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSliderCall18 call = reinterpret_cast<CuteQQuickSliderCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSliderCall19 call = reinterpret_cast<CuteQQuickSliderCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSliderCall20 call = reinterpret_cast<CuteQQuickSliderCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQQuickSliderCall21 call = reinterpret_cast<CuteQQuickSliderCall21>(taken[21]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickSliderCall22 call = reinterpret_cast<CuteQQuickSliderCall22>(taken[22]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickSliderCall23 call = reinterpret_cast<CuteQQuickSliderCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickSliderCall24 call = reinterpret_cast<CuteQQuickSliderCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSliderCall25 call = reinterpret_cast<CuteQQuickSliderCall25>(taken[25]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSliderCall26 call = reinterpret_cast<CuteQQuickSliderCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSliderCall27 call = reinterpret_cast<CuteQQuickSliderCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSliderCall28 call = reinterpret_cast<CuteQQuickSliderCall28>(taken[28]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSliderCall29 call = reinterpret_cast<CuteQQuickSliderCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSliderCall30 call = reinterpret_cast<CuteQQuickSliderCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSliderCall31 call = reinterpret_cast<CuteQQuickSliderCall31>(taken[31]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSliderCall32 call = reinterpret_cast<CuteQQuickSliderCall32>(taken[32]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSliderCall33 call = reinterpret_cast<CuteQQuickSliderCall33>(taken[33]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSliderCall34 call = reinterpret_cast<CuteQQuickSliderCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSliderCall35 call = reinterpret_cast<CuteQQuickSliderCall35>(taken[35]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickSliderCall36 call = reinterpret_cast<CuteQQuickSliderCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickSliderCall37 call = reinterpret_cast<CuteQQuickSliderCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickSliderCall38 call = reinterpret_cast<CuteQQuickSliderCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickSliderCall39 call = reinterpret_cast<CuteQQuickSliderCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickSliderCall40 call = reinterpret_cast<CuteQQuickSliderCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickSliderCall41 call = reinterpret_cast<CuteQQuickSliderCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickSliderCall42 call = reinterpret_cast<CuteQQuickSliderCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickSliderCall43 call = reinterpret_cast<CuteQQuickSliderCall43>(taken[43]);
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
    if (taken[44]) {
      int handled = 0;
      CuteQQuickSliderCall44 call = reinterpret_cast<CuteQQuickSliderCall44>(taken[44]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickSliderCall45 call = reinterpret_cast<CuteQQuickSliderCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickSliderCall46 call = reinterpret_cast<CuteQQuickSliderCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickSliderCall47 call = reinterpret_cast<CuteQQuickSliderCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickSliderCall48 call = reinterpret_cast<CuteQQuickSliderCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickSliderCall49 call = reinterpret_cast<CuteQQuickSliderCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickSliderCall50 call = reinterpret_cast<CuteQQuickSliderCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickSliderCall51 call = reinterpret_cast<CuteQQuickSliderCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickSliderCall52 call = reinterpret_cast<CuteQQuickSliderCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickSlider10metaObjectEv(
    const QQuickSlider *self) {
  return self->metaObject();
}

//  QString QQuickSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickSlider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSlider::tr(s, c, n));
}

//  QQuickSlider::QQuickSlider(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSlider *ritual_ZN12QQuickSliderC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickSlider(parent);
}

//  QQuickSlider::~QQuickSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSliderD1Ev(QQuickSlider *self) {
  delete self;
}

//  qreal QQuickSlider::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider4fromEv(const QQuickSlider *self) {
  return self->from();
}

//  void QQuickSlider::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider7setFromEd(QQuickSlider *self, qreal from) {
  self->setFrom(from);
}

//  qreal QQuickSlider::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider2toEv(const QQuickSlider *self) {
  return self->to();
}

//  void QQuickSlider::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider5setToEd(QQuickSlider *self, qreal to) {
  self->setTo(to);
}

//  qreal QQuickSlider::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider5valueEv(const QQuickSlider *self) {
  return self->value();
}

//  void QQuickSlider::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider8setValueEd(QQuickSlider *self, qreal value) {
  self->setValue(value);
}

//  qreal QQuickSlider::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider8positionEv(const QQuickSlider *self) {
  return self->position();
}

//  qreal QQuickSlider::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider14visualPositionEv(const QQuickSlider *self) {
  return self->visualPosition();
}

//  qreal QQuickSlider::stepSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider8stepSizeEv(const QQuickSlider *self) {
  return self->stepSize();
}

//  void QQuickSlider::setStepSize(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider11setStepSizeEd(QQuickSlider *self, qreal step) {
  self->setStepSize(step);
}

//  SnapMode QQuickSlider::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickSlider::SnapMode ritual_ZNK12QQuickSlider8snapModeEv(
    const QQuickSlider *self) {
  return self->snapMode();
}

//  void QQuickSlider::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider11setSnapModeENS_8SnapModeE(
    QQuickSlider *self,
    QQuickSlider::SnapMode mode) {
  self->setSnapMode(mode);
}

//  bool QQuickSlider::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSlider9isPressedEv(const QQuickSlider *self) {
  return self->isPressed();
}

//  void QQuickSlider::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider10setPressedEb(
    QQuickSlider *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  Qt::Orientation QQuickSlider::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK12QQuickSlider11orientationEv(
    const QQuickSlider *self) {
  return self->orientation();
}

//  void QQuickSlider::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider14setOrientationEN2Qt11OrientationE(
    QQuickSlider *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  QQuickItem *QQuickSlider::handle() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickSlider6handleEv(const QQuickSlider *self) {
  return self->handle();
}

//  void QQuickSlider::setHandle(QQuickItem *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider9setHandleEP10QQuickItem(
    QQuickSlider *self,
    QQuickItem *handle) {
  self->setHandle(handle);
}

//  qreal QQuickSlider::valueAt(qreal position) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider7valueAtEd(
    const QQuickSlider *self,
    qreal position) {
  return self->valueAt(position);
}

//  bool QQuickSlider::live() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSlider4liveEv(const QQuickSlider *self) {
  return self->live();
}

//  void QQuickSlider::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider7setLiveEb(QQuickSlider *self, bool live) {
  self->setLive(live);
}

//  bool QQuickSlider::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSlider12isHorizontalEv(const QQuickSlider *self) {
  return self->isHorizontal();
}

//  bool QQuickSlider::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickSlider10isVerticalEv(const QQuickSlider *self) {
  return self->isVertical();
}

//  qreal QQuickSlider::touchDragThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider18touchDragThresholdEv(
    const QQuickSlider *self) {
  return self->touchDragThreshold();
}

//  void QQuickSlider::setTouchDragThreshold(qreal touchDragThreshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider21setTouchDragThresholdEd(
    QQuickSlider *self,
    qreal touchDragThreshold) {
  self->setTouchDragThreshold(touchDragThreshold);
}

//  void QQuickSlider::resetTouchDragThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider23resetTouchDragThresholdEv(QQuickSlider *self) {
  self->resetTouchDragThreshold();
}

//  qreal QQuickSlider::implicitHandleWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider19implicitHandleWidthEv(
    const QQuickSlider *self) {
  return self->implicitHandleWidth();
}

//  qreal QQuickSlider::implicitHandleHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSlider20implicitHandleHeightEv(
    const QQuickSlider *self) {
  return self->implicitHandleHeight();
}

//  void QQuickSlider::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider8increaseEv(QQuickSlider *self) {
  self->increase();
}

//  void QQuickSlider::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider8decreaseEv(QQuickSlider *self) {
  self->decrease();
}

//  void QQuickSlider::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider13keyPressEventEP9QKeyEvent(
    QQuickSlider *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickSlider::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider15keyReleaseEventEP9QKeyEvent(
    QQuickSlider *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickSlider::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider15mousePressEventEP11QMouseEvent(
    QQuickSlider *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSlider::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider10touchEventEP11QTouchEvent(
    QQuickSlider *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickSlider::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider10wheelEventEP11QWheelEvent(
    QQuickSlider *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickSlider::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider12mirrorChangeEv(QQuickSlider *self) {
  self->mirrorChange();
}

//  void QQuickSlider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider17componentCompleteEv(QQuickSlider *self) {
  self->componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickSlider::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSlider26accessibilityActiveChangedEb(
    QQuickSlider *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSlider::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK12QQuickSlider14accessibleRoleEv(
    const QQuickSlider *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQQuickSlider, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSlider(
    QQuickSlider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSlider *>(self)->take(key, call);
}

//  void QQuickSlider::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider13keyPressEventEP9QKeyEvent(
    QQuickSlider *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::keyPressEvent(
      event);
}

//  void QQuickSlider::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider15keyReleaseEventEP9QKeyEvent(
    QQuickSlider *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::keyReleaseEvent(
      event);
}

//  void QQuickSlider::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider15mousePressEventEP11QMouseEvent(
    QQuickSlider *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::mousePressEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSlider::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider10touchEventEP11QTouchEvent(
    QQuickSlider *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickSlider::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider10wheelEventEP11QWheelEvent(
    QQuickSlider *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickSlider::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider12mirrorChangeEv(QQuickSlider *self) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::mirrorChange();
}

//  void QQuickSlider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider17componentCompleteEv(QQuickSlider *self) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickSlider::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSlider26accessibilityActiveChangedEb(
    QQuickSlider *self,
    bool active) {
  static_cast<OwnQQuickSlider *>(self)->OwnQQuickSlider::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSlider::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK12QQuickSlider14accessibleRoleEv(
    const QQuickSlider *self) {
  return static_cast<const OwnQQuickSlider *>(self)->OwnQQuickSlider::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
