//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h>
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

//  Only a class built on QQuickRangeSlider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRangeSlider : QQuickRangeSlider {
  using QQuickRangeSlider::focusInEvent;
  using QQuickRangeSlider::hoverEnterEvent;
  using QQuickRangeSlider::hoverMoveEvent;
  using QQuickRangeSlider::hoverLeaveEvent;
  using QQuickRangeSlider::keyPressEvent;
  using QQuickRangeSlider::keyReleaseEvent;
  using QQuickRangeSlider::mousePressEvent;
  using QQuickRangeSlider::touchEvent;
  using QQuickRangeSlider::mirrorChange;
  using QQuickRangeSlider::classBegin;
  using QQuickRangeSlider::componentComplete;
  using QQuickRangeSlider::accessibleRole;
};

//  A QQuickRangeSlider that Python can take functions over in. Every QQuickRangeSlider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRangeSliderCall0)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall1)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall2)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall3)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall5)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall6)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickRangeSliderCall7)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickRangeSliderCall8)(const void *, int *);
typedef void (*CuteQQuickRangeSliderCall9)(const void *, int *);
typedef void (*CuteQQuickRangeSliderCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickRangeSliderCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickRangeSliderCall12)(const void *, int *);
typedef void (*CuteQQuickRangeSliderCall13)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickRangeSliderCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRangeSliderCall17)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickRangeSliderCall18)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRangeSliderCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRangeSliderCall20)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRangeSliderCall21)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRangeSliderCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickRangeSliderCall23)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickRangeSliderCall24)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickRangeSliderCall25)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickRangeSliderCall26)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickRangeSliderCall27)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickRangeSliderCall28)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickRangeSliderCall29)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickRangeSliderCall30)(const void *, int *);
typedef const QRectF * (*CuteQQuickRangeSliderCall31)(const void *, int *);
typedef bool (*CuteQQuickRangeSliderCall32)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRangeSliderCall33)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRangeSliderCall34)(const void *, int *);
typedef void * (*CuteQQuickRangeSliderCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRangeSliderCall36)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef void (*CuteQQuickRangeSliderCall37)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRangeSliderCall38)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRangeSliderCall39)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRangeSliderCall40)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRangeSliderCall41)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRangeSliderCall42)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRangeSliderCall43)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickRangeSliderCall44)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRangeSliderCall45)(const void *, int *);
typedef void (*CuteQQuickRangeSliderCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRangeSliderCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRangeSliderCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRangeSlider : public QQuickRangeSlider {
public:
  using QQuickRangeSlider::QQuickRangeSlider;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[10] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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

  //  void QQuickRangeSlider::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRangeSliderCall0 call = reinterpret_cast<CuteQQuickRangeSliderCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::focusInEvent(event);
  }

  //  void QQuickRangeSlider::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRangeSliderCall1 call = reinterpret_cast<CuteQQuickRangeSliderCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::hoverEnterEvent(event);
  }

  //  void QQuickRangeSlider::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRangeSliderCall2 call = reinterpret_cast<CuteQQuickRangeSliderCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::hoverMoveEvent(event);
  }

  //  void QQuickRangeSlider::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRangeSliderCall3 call = reinterpret_cast<CuteQQuickRangeSliderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::hoverLeaveEvent(event);
  }

  //  void QQuickRangeSlider::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRangeSliderCall4 call = reinterpret_cast<CuteQQuickRangeSliderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::keyPressEvent(event);
  }

  //  void QQuickRangeSlider::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRangeSliderCall5 call = reinterpret_cast<CuteQQuickRangeSliderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::keyReleaseEvent(event);
  }

  //  void QQuickRangeSlider::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRangeSliderCall6 call = reinterpret_cast<CuteQQuickRangeSliderCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::mousePressEvent(event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickRangeSlider::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRangeSliderCall7 call = reinterpret_cast<CuteQQuickRangeSliderCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickRangeSlider::mirrorChange()
  void mirrorChange() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRangeSliderCall8 call = reinterpret_cast<CuteQQuickRangeSliderCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::mirrorChange();
  }

  //  void QQuickRangeSlider::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRangeSliderCall9 call = reinterpret_cast<CuteQQuickRangeSliderCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::classBegin();
  }

  //  void QQuickRangeSlider::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRangeSliderCall10 call = reinterpret_cast<CuteQQuickRangeSliderCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRangeSlider::componentComplete();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickRangeSlider::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRangeSliderCall11 call = reinterpret_cast<CuteQQuickRangeSliderCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickRangeSlider::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRangeSliderCall12 call = reinterpret_cast<CuteQQuickRangeSliderCall12>(taken[12]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRangeSliderCall13 call = reinterpret_cast<CuteQQuickRangeSliderCall13>(taken[13]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRangeSliderCall14 call = reinterpret_cast<CuteQQuickRangeSliderCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRangeSliderCall15 call = reinterpret_cast<CuteQQuickRangeSliderCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRangeSliderCall16 call = reinterpret_cast<CuteQQuickRangeSliderCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRangeSliderCall17 call = reinterpret_cast<CuteQQuickRangeSliderCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRangeSliderCall18 call = reinterpret_cast<CuteQQuickRangeSliderCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRangeSliderCall19 call = reinterpret_cast<CuteQQuickRangeSliderCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRangeSliderCall20 call = reinterpret_cast<CuteQQuickRangeSliderCall20>(taken[20]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRangeSliderCall21 call = reinterpret_cast<CuteQQuickRangeSliderCall21>(taken[21]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRangeSliderCall22 call = reinterpret_cast<CuteQQuickRangeSliderCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRangeSliderCall23 call = reinterpret_cast<CuteQQuickRangeSliderCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQuickRangeSliderCall24 call = reinterpret_cast<CuteQQuickRangeSliderCall24>(taken[24]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickRangeSliderCall25 call = reinterpret_cast<CuteQQuickRangeSliderCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRangeSliderCall26 call = reinterpret_cast<CuteQQuickRangeSliderCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRangeSliderCall27 call = reinterpret_cast<CuteQQuickRangeSliderCall27>(taken[27]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRangeSliderCall28 call = reinterpret_cast<CuteQQuickRangeSliderCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickRangeSliderCall29 call = reinterpret_cast<CuteQQuickRangeSliderCall29>(taken[29]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickRangeSliderCall30 call = reinterpret_cast<CuteQQuickRangeSliderCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickRangeSliderCall31 call = reinterpret_cast<CuteQQuickRangeSliderCall31>(taken[31]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickRangeSliderCall32 call = reinterpret_cast<CuteQQuickRangeSliderCall32>(taken[32]);
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
      CuteQQuickRangeSliderCall33 call = reinterpret_cast<CuteQQuickRangeSliderCall33>(taken[33]);
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
      CuteQQuickRangeSliderCall34 call = reinterpret_cast<CuteQQuickRangeSliderCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickRangeSliderCall35 call = reinterpret_cast<CuteQQuickRangeSliderCall35>(taken[35]);
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
      CuteQQuickRangeSliderCall36 call = reinterpret_cast<CuteQQuickRangeSliderCall36>(taken[36]);
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
      CuteQQuickRangeSliderCall37 call = reinterpret_cast<CuteQQuickRangeSliderCall37>(taken[37]);
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
      CuteQQuickRangeSliderCall38 call = reinterpret_cast<CuteQQuickRangeSliderCall38>(taken[38]);
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
      CuteQQuickRangeSliderCall39 call = reinterpret_cast<CuteQQuickRangeSliderCall39>(taken[39]);
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
      CuteQQuickRangeSliderCall40 call = reinterpret_cast<CuteQQuickRangeSliderCall40>(taken[40]);
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
      CuteQQuickRangeSliderCall41 call = reinterpret_cast<CuteQQuickRangeSliderCall41>(taken[41]);
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
      CuteQQuickRangeSliderCall42 call = reinterpret_cast<CuteQQuickRangeSliderCall42>(taken[42]);
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
      CuteQQuickRangeSliderCall43 call = reinterpret_cast<CuteQQuickRangeSliderCall43>(taken[43]);
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
      CuteQQuickRangeSliderCall44 call = reinterpret_cast<CuteQQuickRangeSliderCall44>(taken[44]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickRangeSliderCall45 call = reinterpret_cast<CuteQQuickRangeSliderCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickRangeSliderCall46 call = reinterpret_cast<CuteQQuickRangeSliderCall46>(taken[46]);
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
      CuteQQuickRangeSliderCall47 call = reinterpret_cast<CuteQQuickRangeSliderCall47>(taken[47]);
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
      CuteQQuickRangeSliderCall48 call = reinterpret_cast<CuteQQuickRangeSliderCall48>(taken[48]);
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
      CuteQQuickRangeSliderCall49 call = reinterpret_cast<CuteQQuickRangeSliderCall49>(taken[49]);
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
      CuteQQuickRangeSliderCall50 call = reinterpret_cast<CuteQQuickRangeSliderCall50>(taken[50]);
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
      CuteQQuickRangeSliderCall51 call = reinterpret_cast<CuteQQuickRangeSliderCall51>(taken[51]);
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
      CuteQQuickRangeSliderCall52 call = reinterpret_cast<CuteQQuickRangeSliderCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRangeSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickRangeSlider10metaObjectEv(
    const QQuickRangeSlider *self) {
  return self->metaObject();
}

//  void *QQuickRangeSlider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickRangeSlider11qt_metacastEPKc(
    QQuickRangeSlider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRangeSlider::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickRangeSlider11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRangeSlider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRangeSlider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickRangeSlider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRangeSlider::tr(s, c, n));
}

//  QQuickRangeSlider::QQuickRangeSlider(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRangeSlider *ritual_ZN17QQuickRangeSliderC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRangeSlider(parent);
}

//  QQuickRangeSlider::~QQuickRangeSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSliderD1Ev(QQuickRangeSlider *self) {
  delete self;
}

//  qreal QQuickRangeSlider::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider4fromEv(const QQuickRangeSlider *self) {
  return self->from();
}

//  void QQuickRangeSlider::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider7setFromEd(
    QQuickRangeSlider *self,
    qreal from) {
  self->setFrom(from);
}

//  qreal QQuickRangeSlider::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider2toEv(const QQuickRangeSlider *self) {
  return self->to();
}

//  void QQuickRangeSlider::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider5setToEd(
    QQuickRangeSlider *self,
    qreal to) {
  self->setTo(to);
}

//  QQuickRangeSliderNode *QQuickRangeSlider::first() const
extern "C" Q_DECL_EXPORT
QQuickRangeSliderNode *ritual_ZNK17QQuickRangeSlider5firstEv(
    const QQuickRangeSlider *self) {
  return self->first();
}

//  QQuickRangeSliderNode *QQuickRangeSlider::second() const
extern "C" Q_DECL_EXPORT
QQuickRangeSliderNode *ritual_ZNK17QQuickRangeSlider6secondEv(
    const QQuickRangeSlider *self) {
  return self->second();
}

//  qreal QQuickRangeSlider::stepSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider8stepSizeEv(
    const QQuickRangeSlider *self) {
  return self->stepSize();
}

//  void QQuickRangeSlider::setStepSize(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider11setStepSizeEd(
    QQuickRangeSlider *self,
    qreal step) {
  self->setStepSize(step);
}

//  SnapMode QQuickRangeSlider::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickRangeSlider::SnapMode ritual_ZNK17QQuickRangeSlider8snapModeEv(
    const QQuickRangeSlider *self) {
  return self->snapMode();
}

//  void QQuickRangeSlider::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider11setSnapModeENS_8SnapModeE(
    QQuickRangeSlider *self,
    QQuickRangeSlider::SnapMode mode) {
  self->setSnapMode(mode);
}

//  Qt::Orientation QQuickRangeSlider::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK17QQuickRangeSlider11orientationEv(
    const QQuickRangeSlider *self) {
  return self->orientation();
}

//  void QQuickRangeSlider::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider14setOrientationEN2Qt11OrientationE(
    QQuickRangeSlider *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  void QQuickRangeSlider::setValues(qreal firstValue, qreal secondValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider9setValuesEdd(
    QQuickRangeSlider *self,
    qreal firstValue,
    qreal secondValue) {
  self->setValues(firstValue, secondValue);
}

//  bool QQuickRangeSlider::live() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRangeSlider4liveEv(const QQuickRangeSlider *self) {
  return self->live();
}

//  void QQuickRangeSlider::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider7setLiveEb(
    QQuickRangeSlider *self,
    bool live) {
  self->setLive(live);
}

//  bool QQuickRangeSlider::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRangeSlider12isHorizontalEv(
    const QQuickRangeSlider *self) {
  return self->isHorizontal();
}

//  bool QQuickRangeSlider::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRangeSlider10isVerticalEv(
    const QQuickRangeSlider *self) {
  return self->isVertical();
}

//  qreal QQuickRangeSlider::touchDragThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider18touchDragThresholdEv(
    const QQuickRangeSlider *self) {
  return self->touchDragThreshold();
}

//  void QQuickRangeSlider::setTouchDragThreshold(qreal touchDragThreshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider21setTouchDragThresholdEd(
    QQuickRangeSlider *self,
    qreal touchDragThreshold) {
  self->setTouchDragThreshold(touchDragThreshold);
}

//  void QQuickRangeSlider::resetTouchDragThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider23resetTouchDragThresholdEv(
    QQuickRangeSlider *self) {
  self->resetTouchDragThreshold();
}

//  qreal QQuickRangeSlider::valueAt(qreal position) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider7valueAtEd(
    const QQuickRangeSlider *self,
    qreal position) {
  return self->valueAt(position);
}

//  bool QQuickRangeSlider::isCrossingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRangeSlider17isCrossingEnabledEv(
    const QQuickRangeSlider *self) {
  return self->isCrossingEnabled();
}

//  void QQuickRangeSlider::setCrossingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider18setCrossingEnabledEb(
    QQuickRangeSlider *self,
    bool enabled) {
  self->setCrossingEnabled(enabled);
}

//  bool QQuickRangeSlider::handlesCrossed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickRangeSlider14handlesCrossedEv(
    const QQuickRangeSlider *self) {
  return self->handlesCrossed();
}

//  qreal QQuickRangeSlider::effectiveFirstValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider19effectiveFirstValueEv(
    const QQuickRangeSlider *self) {
  return self->effectiveFirstValue();
}

//  qreal QQuickRangeSlider::effectiveSecondValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRangeSlider20effectiveSecondValueEv(
    const QQuickRangeSlider *self) {
  return self->effectiveSecondValue();
}

//  void QQuickRangeSlider::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider11fromChangedEv(QQuickRangeSlider *self) {
  self->fromChanged();
}

//  void QQuickRangeSlider::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider9toChangedEv(QQuickRangeSlider *self) {
  self->toChanged();
}

//  void QQuickRangeSlider::stepSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15stepSizeChangedEv(
    QQuickRangeSlider *self) {
  self->stepSizeChanged();
}

//  void QQuickRangeSlider::snapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15snapModeChangedEv(
    QQuickRangeSlider *self) {
  self->snapModeChanged();
}

//  void QQuickRangeSlider::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider18orientationChangedEv(
    QQuickRangeSlider *self) {
  self->orientationChanged();
}

//  void QQuickRangeSlider::liveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider11liveChangedEv(QQuickRangeSlider *self) {
  self->liveChanged();
}

//  void QQuickRangeSlider::touchDragThresholdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider25touchDragThresholdChangedEv(
    QQuickRangeSlider *self) {
  self->touchDragThresholdChanged();
}

//  void QQuickRangeSlider::crossingEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider22crossingEnabledChangedEv(
    QQuickRangeSlider *self) {
  self->crossingEnabledChanged();
}

//  void QQuickRangeSlider::handlesCrossedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider21handlesCrossedChangedEv(
    QQuickRangeSlider *self) {
  self->handlesCrossedChanged();
}

//  void QQuickRangeSlider::effectiveFirstValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider26effectiveFirstValueChangedEv(
    QQuickRangeSlider *self) {
  self->effectiveFirstValueChanged();
}

//  void QQuickRangeSlider::effectiveSecondValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider27effectiveSecondValueChangedEv(
    QQuickRangeSlider *self) {
  self->effectiveSecondValueChanged();
}

//  void QQuickRangeSlider::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider12focusInEventEP11QFocusEvent(
    QQuickRangeSlider *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickRangeSlider::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15hoverEnterEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickRangeSlider::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider14hoverMoveEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickRangeSlider::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15hoverLeaveEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickRangeSlider::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider13keyPressEventEP9QKeyEvent(
    QQuickRangeSlider *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickRangeSlider::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15keyReleaseEventEP9QKeyEvent(
    QQuickRangeSlider *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickRangeSlider::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider15mousePressEventEP11QMouseEvent(
    QQuickRangeSlider *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickRangeSlider::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider10touchEventEP11QTouchEvent(
    QQuickRangeSlider *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickRangeSlider::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider12mirrorChangeEv(QQuickRangeSlider *self) {
  self->mirrorChange();
}

//  void QQuickRangeSlider::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider10classBeginEv(QQuickRangeSlider *self) {
  self->classBegin();
}

//  void QQuickRangeSlider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider17componentCompleteEv(
    QQuickRangeSlider *self) {
  self->componentComplete();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRangeSlider::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickRangeSlider14accessibleRoleEv(
    const QQuickRangeSlider *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickRangeSlider::updateHandleCrossing()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider20updateHandleCrossingEv(
    QQuickRangeSlider *self) {
  self->updateHandleCrossing();
}

//  void QQuickRangeSlider::effectiveValueChange(QQuickRangeSliderNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider20effectiveValueChangeEP21QQuickRangeSliderNode(
    QQuickRangeSlider *self,
    QQuickRangeSliderNode *node) {
  self->effectiveValueChange(node);
}

//  void QQuickRangeSlider::updateFocusOrder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRangeSlider16updateFocusOrderEv(
    QQuickRangeSlider *self) {
  self->updateFocusOrder();
}

//  QQuickRangeSliderPrivate *QQuickRangeSlider::d_func()
extern "C" Q_DECL_EXPORT
QQuickRangeSliderPrivate *ritual_ZN17QQuickRangeSlider6d_funcEv(
    QQuickRangeSlider *self) {
  return self->d_func();
}

//  const QQuickRangeSliderPrivate *QQuickRangeSlider::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRangeSliderPrivate *ritual_ZNK17QQuickRangeSlider6d_funcEv(
    const QQuickRangeSlider *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickRangeSlider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRangeSlider(
    QQuickRangeSlider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRangeSlider *>(self)->take(key, call);
}

//  void QQuickRangeSlider::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider12focusInEventEP11QFocusEvent(
    QQuickRangeSlider *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::focusInEvent(
      event);
}

//  void QQuickRangeSlider::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider15hoverEnterEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::hoverEnterEvent(
      event);
}

//  void QQuickRangeSlider::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider14hoverMoveEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::hoverMoveEvent(
      event);
}

//  void QQuickRangeSlider::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider15hoverLeaveEventEP11QHoverEvent(
    QQuickRangeSlider *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::hoverLeaveEvent(
      event);
}

//  void QQuickRangeSlider::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider13keyPressEventEP9QKeyEvent(
    QQuickRangeSlider *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::keyPressEvent(
      event);
}

//  void QQuickRangeSlider::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider15keyReleaseEventEP9QKeyEvent(
    QQuickRangeSlider *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::keyReleaseEvent(
      event);
}

//  void QQuickRangeSlider::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider15mousePressEventEP11QMouseEvent(
    QQuickRangeSlider *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::mousePressEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickRangeSlider::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider10touchEventEP11QTouchEvent(
    QQuickRangeSlider *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickRangeSlider::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider12mirrorChangeEv(
    QQuickRangeSlider *self) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::mirrorChange();
}

//  void QQuickRangeSlider::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider10classBeginEv(
    QQuickRangeSlider *self) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::classBegin();
}

//  void QQuickRangeSlider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRangeSlider17componentCompleteEv(
    QQuickRangeSlider *self) {
  static_cast<OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::componentComplete();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickRangeSlider::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QQuickRangeSlider14accessibleRoleEv(
    const QQuickRangeSlider *self) {
  return static_cast<const OwnQQuickRangeSlider *>(self)->OwnQQuickRangeSlider::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
