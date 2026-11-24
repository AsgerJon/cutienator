//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickControl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickControl : QQuickControl {
  using QQuickControl::defaultFont;
  using QQuickControl::classBegin;
  using QQuickControl::componentComplete;
  using QQuickControl::itemChange;
  using QQuickControl::focusInEvent;
  using QQuickControl::focusOutEvent;
  using QQuickControl::hoverEnterEvent;
  using QQuickControl::hoverMoveEvent;
  using QQuickControl::hoverLeaveEvent;
  using QQuickControl::mousePressEvent;
  using QQuickControl::mouseMoveEvent;
  using QQuickControl::mouseReleaseEvent;
  using QQuickControl::mouseUngrabEvent;
  using QQuickControl::touchEvent;
  using QQuickControl::touchUngrabEvent;
  using QQuickControl::wheelEvent;
  using QQuickControl::geometryChange;
  using QQuickControl::fontChange;
  using QQuickControl::hoverChange;
  using QQuickControl::mirrorChange;
  using QQuickControl::spacingChange;
  using QQuickControl::paddingChange;
  using QQuickControl::contentItemChange;
  using QQuickControl::localeChange;
  using QQuickControl::insetChange;
  using QQuickControl::enabledChange;
  using QQuickControl::accessibleRole;
  using QQuickControl::accessibilityActiveChanged;
};

//  A QQuickControl that Python can take functions over in. Every QQuickControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QFont * (*CuteQQuickControlCall0)(const void *, int *);
typedef void (*CuteQQuickControlCall1)(const void *, int *);
typedef void (*CuteQQuickControlCall2)(const void *, int *);
typedef void (*CuteQQuickControlCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickControlCall4)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickControlCall5)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall6)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall7)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall8)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickControlCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickControlCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickControlCall12)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickControlCall13)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickControlCall14)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickControlCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickControlCall16)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickControlCall17)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall18)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickControlCall19)(const void *, int *);
typedef void (*CuteQQuickControlCall20)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickControlCall21)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickControlCall22)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickControlCall23)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickControlCall24)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickControlCall25)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickControlCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickControlCall27)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickControlCall28)(const void *, int *);
typedef const QRectF * (*CuteQQuickControlCall29)(const void *, int *);
typedef bool (*CuteQQuickControlCall30)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickControlCall31)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickControlCall32)(const void *, int *);
typedef void * (*CuteQQuickControlCall33)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickControlCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall35)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickControlCall36)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickControlCall37)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickControlCall38)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickControlCall39)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickControlCall40)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickControlCall41)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickControlCall42)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickControlCall43)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickControlCall44)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickControlCall45)(const void *, int *);
typedef void (*CuteQQuickControlCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickControlCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickControlCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickControl : public QQuickControl {
public:
  using QQuickControl::QQuickControl;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[33] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[36] = call;
      return true;
    }
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

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickControlCall0 call = reinterpret_cast<CuteQQuickControlCall0>(taken[0]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickControlCall1 call = reinterpret_cast<CuteQQuickControlCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickControlCall2 call = reinterpret_cast<CuteQQuickControlCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::componentComplete();
  }

  //  void QQuickControl::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickControlCall3 call = reinterpret_cast<CuteQQuickControlCall3>(taken[3]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickControlCall4 call = reinterpret_cast<CuteQQuickControlCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickControlCall5 call = reinterpret_cast<CuteQQuickControlCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickControlCall6 call = reinterpret_cast<CuteQQuickControlCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickControlCall7 call = reinterpret_cast<CuteQQuickControlCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickControlCall8 call = reinterpret_cast<CuteQQuickControlCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickControlCall9 call = reinterpret_cast<CuteQQuickControlCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickControlCall10 call = reinterpret_cast<CuteQQuickControlCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickControlCall11 call = reinterpret_cast<CuteQQuickControlCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickControlCall12 call = reinterpret_cast<CuteQQuickControlCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickControlCall13 call = reinterpret_cast<CuteQQuickControlCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickControlCall14 call = reinterpret_cast<CuteQQuickControlCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickControlCall15 call = reinterpret_cast<CuteQQuickControlCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQQuickControlCall16 call = reinterpret_cast<CuteQQuickControlCall16>(taken[16]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickControlCall17 call = reinterpret_cast<CuteQQuickControlCall17>(taken[17]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickControlCall18 call = reinterpret_cast<CuteQQuickControlCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickControlCall19 call = reinterpret_cast<CuteQQuickControlCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickControlCall20 call = reinterpret_cast<CuteQQuickControlCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQQuickControlCall21 call = reinterpret_cast<CuteQQuickControlCall21>(taken[21]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickControlCall22 call = reinterpret_cast<CuteQQuickControlCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQQuickControlCall23 call = reinterpret_cast<CuteQQuickControlCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQuickControlCall24 call = reinterpret_cast<CuteQQuickControlCall24>(taken[24]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickControlCall25 call = reinterpret_cast<CuteQQuickControlCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControl::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickControlCall26 call = reinterpret_cast<CuteQQuickControlCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControl::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickControlCall27 call = reinterpret_cast<CuteQQuickControlCall27>(taken[27]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickControlCall28 call = reinterpret_cast<CuteQQuickControlCall28>(taken[28]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickControlCall29 call = reinterpret_cast<CuteQQuickControlCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickControlCall30 call = reinterpret_cast<CuteQQuickControlCall30>(taken[30]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickControlCall31 call = reinterpret_cast<CuteQQuickControlCall31>(taken[31]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickControlCall32 call = reinterpret_cast<CuteQQuickControlCall32>(taken[32]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickControlCall33 call = reinterpret_cast<CuteQQuickControlCall33>(taken[33]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickControlCall34 call = reinterpret_cast<CuteQQuickControlCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickControlCall35 call = reinterpret_cast<CuteQQuickControlCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickControlCall36 call = reinterpret_cast<CuteQQuickControlCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickControlCall37 call = reinterpret_cast<CuteQQuickControlCall37>(taken[37]);
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
      CuteQQuickControlCall38 call = reinterpret_cast<CuteQQuickControlCall38>(taken[38]);
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
      CuteQQuickControlCall39 call = reinterpret_cast<CuteQQuickControlCall39>(taken[39]);
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
      CuteQQuickControlCall40 call = reinterpret_cast<CuteQQuickControlCall40>(taken[40]);
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
      CuteQQuickControlCall41 call = reinterpret_cast<CuteQQuickControlCall41>(taken[41]);
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
      CuteQQuickControlCall42 call = reinterpret_cast<CuteQQuickControlCall42>(taken[42]);
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
      CuteQQuickControlCall43 call = reinterpret_cast<CuteQQuickControlCall43>(taken[43]);
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
      CuteQQuickControlCall44 call = reinterpret_cast<CuteQQuickControlCall44>(taken[44]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickControlCall45 call = reinterpret_cast<CuteQQuickControlCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickControlCall46 call = reinterpret_cast<CuteQQuickControlCall46>(taken[46]);
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
      CuteQQuickControlCall47 call = reinterpret_cast<CuteQQuickControlCall47>(taken[47]);
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
      CuteQQuickControlCall48 call = reinterpret_cast<CuteQQuickControlCall48>(taken[48]);
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
      CuteQQuickControlCall49 call = reinterpret_cast<CuteQQuickControlCall49>(taken[49]);
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
      CuteQQuickControlCall50 call = reinterpret_cast<CuteQQuickControlCall50>(taken[50]);
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
      CuteQQuickControlCall51 call = reinterpret_cast<CuteQQuickControlCall51>(taken[51]);
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
      CuteQQuickControlCall52 call = reinterpret_cast<CuteQQuickControlCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickControl10metaObjectEv(
    const QQuickControl *self) {
  return self->metaObject();
}

//  QString QQuickControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickControl::tr(s, c, n));
}

//  QQuickControl::QQuickControl(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickControl *ritual_ZN13QQuickControlC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickControl(parent);
}

//  QQuickControl::~QQuickControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControlD1Ev(QQuickControl *self) {
  delete self;
}

//  QFont QQuickControl::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickControl4fontEv(const QQuickControl *self) {
  return new QFont(self->font());
}

//  void QQuickControl::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl7setFontERK5QFont(
    QQuickControl *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QQuickControl::resetFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl9resetFontEv(QQuickControl *self) {
  self->resetFont();
}

//  qreal QQuickControl::availableWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl14availableWidthEv(
    const QQuickControl *self) {
  return self->availableWidth();
}

//  qreal QQuickControl::availableHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl15availableHeightEv(
    const QQuickControl *self) {
  return self->availableHeight();
}

//  qreal QQuickControl::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl7paddingEv(const QQuickControl *self) {
  return self->padding();
}

//  void QQuickControl::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10setPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QQuickControl::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12resetPaddingEv(QQuickControl *self) {
  self->resetPadding();
}

//  qreal QQuickControl::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl10topPaddingEv(const QQuickControl *self) {
  return self->topPadding();
}

//  void QQuickControl::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13setTopPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickControl::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15resetTopPaddingEv(QQuickControl *self) {
  self->resetTopPadding();
}

//  qreal QQuickControl::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl11leftPaddingEv(const QQuickControl *self) {
  return self->leftPadding();
}

//  void QQuickControl::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14setLeftPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickControl::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl16resetLeftPaddingEv(QQuickControl *self) {
  self->resetLeftPadding();
}

//  qreal QQuickControl::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl12rightPaddingEv(const QQuickControl *self) {
  return self->rightPadding();
}

//  void QQuickControl::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15setRightPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickControl::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17resetRightPaddingEv(QQuickControl *self) {
  self->resetRightPadding();
}

//  qreal QQuickControl::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl13bottomPaddingEv(const QQuickControl *self) {
  return self->bottomPadding();
}

//  void QQuickControl::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl16setBottomPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickControl::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl18resetBottomPaddingEv(QQuickControl *self) {
  self->resetBottomPadding();
}

//  qreal QQuickControl::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl7spacingEv(const QQuickControl *self) {
  return self->spacing();
}

//  void QQuickControl::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10setSpacingEd(
    QQuickControl *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  void QQuickControl::resetSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12resetSpacingEv(QQuickControl *self) {
  self->resetSpacing();
}

//  QLocale QQuickControl::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK13QQuickControl6localeEv(const QQuickControl *self) {
  return new QLocale(self->locale());
}

//  void QQuickControl::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl9setLocaleERK7QLocale(
    QQuickControl *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QQuickControl::resetLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl11resetLocaleEv(QQuickControl *self) {
  self->resetLocale();
}

//  bool QQuickControl::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickControl10isMirroredEv(const QQuickControl *self) {
  return self->isMirrored();
}

//  Qt::FocusReason QQuickControl::focusReason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK13QQuickControl11focusReasonEv(
    const QQuickControl *self) {
  return self->focusReason();
}

//  void QQuickControl::setFocusReason(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14setFocusReasonEN2Qt11FocusReasonE(
    QQuickControl *self,
    Qt::FocusReason reason) {
  self->setFocusReason(reason);
}

//  bool QQuickControl::hasVisualFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickControl14hasVisualFocusEv(const QQuickControl *self) {
  return self->hasVisualFocus();
}

//  bool QQuickControl::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickControl9isHoveredEv(const QQuickControl *self) {
  return self->isHovered();
}

//  void QQuickControl::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10setHoveredEb(
    QQuickControl *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  bool QQuickControl::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickControl14isHoverEnabledEv(const QQuickControl *self) {
  return self->isHoverEnabled();
}

//  void QQuickControl::setHoverEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15setHoverEnabledEb(
    QQuickControl *self,
    bool enabled) {
  self->setHoverEnabled(enabled);
}

//  void QQuickControl::resetHoverEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17resetHoverEnabledEv(QQuickControl *self) {
  self->resetHoverEnabled();
}

//  bool QQuickControl::isWheelEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickControl14isWheelEnabledEv(const QQuickControl *self) {
  return self->isWheelEnabled();
}

//  void QQuickControl::setWheelEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15setWheelEnabledEb(
    QQuickControl *self,
    bool enabled) {
  self->setWheelEnabled(enabled);
}

//  QQuickItem *QQuickControl::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK13QQuickControl10backgroundEv(
    const QQuickControl *self) {
  return self->background();
}

//  void QQuickControl::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13setBackgroundEP10QQuickItem(
    QQuickControl *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  QQuickItem *QQuickControl::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK13QQuickControl11contentItemEv(
    const QQuickControl *self) {
  return self->contentItem();
}

//  void QQuickControl::setContentItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14setContentItemEP10QQuickItem(
    QQuickControl *self,
    QQuickItem *item) {
  self->setContentItem(item);
}

//  qreal QQuickControl::baselineOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl14baselineOffsetEv(
    const QQuickControl *self) {
  return self->baselineOffset();
}

//  void QQuickControl::setBaselineOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17setBaselineOffsetEd(
    QQuickControl *self,
    qreal offset) {
  self->setBaselineOffset(offset);
}

//  void QQuickControl::resetBaselineOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl19resetBaselineOffsetEv(QQuickControl *self) {
  self->resetBaselineOffset();
}

//  qreal QQuickControl::horizontalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl17horizontalPaddingEv(
    const QQuickControl *self) {
  return self->horizontalPadding();
}

//  void QQuickControl::setHorizontalPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl20setHorizontalPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setHorizontalPadding(padding);
}

//  void QQuickControl::resetHorizontalPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl22resetHorizontalPaddingEv(
    QQuickControl *self) {
  self->resetHorizontalPadding();
}

//  qreal QQuickControl::verticalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl15verticalPaddingEv(
    const QQuickControl *self) {
  return self->verticalPadding();
}

//  void QQuickControl::setVerticalPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl18setVerticalPaddingEd(
    QQuickControl *self,
    qreal padding) {
  self->setVerticalPadding(padding);
}

//  void QQuickControl::resetVerticalPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl20resetVerticalPaddingEv(QQuickControl *self) {
  self->resetVerticalPadding();
}

//  qreal QQuickControl::implicitContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl20implicitContentWidthEv(
    const QQuickControl *self) {
  return self->implicitContentWidth();
}

//  qreal QQuickControl::implicitContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl21implicitContentHeightEv(
    const QQuickControl *self) {
  return self->implicitContentHeight();
}

//  qreal QQuickControl::implicitBackgroundWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl23implicitBackgroundWidthEv(
    const QQuickControl *self) {
  return self->implicitBackgroundWidth();
}

//  qreal QQuickControl::implicitBackgroundHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl24implicitBackgroundHeightEv(
    const QQuickControl *self) {
  return self->implicitBackgroundHeight();
}

//  qreal QQuickControl::topInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl8topInsetEv(const QQuickControl *self) {
  return self->topInset();
}

//  void QQuickControl::setTopInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl11setTopInsetEd(
    QQuickControl *self,
    qreal inset) {
  self->setTopInset(inset);
}

//  void QQuickControl::resetTopInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13resetTopInsetEv(QQuickControl *self) {
  self->resetTopInset();
}

//  qreal QQuickControl::leftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl9leftInsetEv(const QQuickControl *self) {
  return self->leftInset();
}

//  void QQuickControl::setLeftInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12setLeftInsetEd(
    QQuickControl *self,
    qreal inset) {
  self->setLeftInset(inset);
}

//  void QQuickControl::resetLeftInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14resetLeftInsetEv(QQuickControl *self) {
  self->resetLeftInset();
}

//  qreal QQuickControl::rightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl10rightInsetEv(const QQuickControl *self) {
  return self->rightInset();
}

//  void QQuickControl::setRightInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13setRightInsetEd(
    QQuickControl *self,
    qreal inset) {
  self->setRightInset(inset);
}

//  void QQuickControl::resetRightInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15resetRightInsetEv(QQuickControl *self) {
  self->resetRightInset();
}

//  qreal QQuickControl::bottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickControl11bottomInsetEv(const QQuickControl *self) {
  return self->bottomInset();
}

//  void QQuickControl::setBottomInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14setBottomInsetEd(
    QQuickControl *self,
    qreal inset) {
  self->setBottomInset(inset);
}

//  void QQuickControl::resetBottomInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl16resetBottomInsetEv(QQuickControl *self) {
  self->resetBottomInset();
}

//  QFont QQuickControl::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickControl11defaultFontEv(const QQuickControl *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickControl::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10classBeginEv(QQuickControl *self) {
  self->classBegin();
}

//  void QQuickControl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17componentCompleteEv(QQuickControl *self) {
  self->componentComplete();
}

//  void QQuickControl::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickControl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickControl::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12focusInEventEP11QFocusEvent(
    QQuickControl *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickControl::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13focusOutEventEP11QFocusEvent(
    QQuickControl *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15hoverEnterEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14hoverMoveEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15hoverLeaveEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickControl::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl15mousePressEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14mouseMoveEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17mouseReleaseEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickControl::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl16mouseUngrabEventEv(QQuickControl *self) {
  self->mouseUngrabEvent();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickControl::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10touchEventEP11QTouchEvent(
    QQuickControl *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickControl::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl16touchUngrabEventEv(QQuickControl *self) {
  self->touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickControl::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10wheelEventEP11QWheelEvent(
    QQuickControl *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickControl::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl14geometryChangeERK6QRectFS2_(
    QQuickControl *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickControl::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl10fontChangeERK5QFontS2_(
    QQuickControl *self,
    const QFont *newFont,
    const QFont *oldFont) {
  self->fontChange(*newFont, *oldFont);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl11hoverChangeEv(QQuickControl *self) {
  self->hoverChange();
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickControl::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12mirrorChangeEv(QQuickControl *self) {
  self->mirrorChange();
}

//  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13spacingChangeEdd(
    QQuickControl *self,
    qreal newSpacing,
    qreal oldSpacing) {
  self->spacingChange(newSpacing, oldSpacing);
}

//  void QQuickControl::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_(
    QQuickControl *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_(
    QQuickControl *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickControl::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl12localeChangeERK7QLocaleS2_(
    QQuickControl *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickControl::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl11insetChangeERK9QMarginsFS2_(
    QQuickControl *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  void QQuickControl::enabledChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl13enabledChangeEv(QQuickControl *self) {
  self->enabledChange();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickControl::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK13QQuickControl14accessibleRoleEv(
    const QQuickControl *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickControl::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl26accessibilityActiveChangedEb(
    QQuickControl *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QString QQuickControl::accessibleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQuickControl14accessibleNameEv(
    const QQuickControl *self) {
  return new QString(self->accessibleName());
}

//  void QQuickControl::maybeSetAccessibleName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickControl22maybeSetAccessibleNameERK7QString(
    QQuickControl *self,
    const QString *name) {
  self->maybeSetAccessibleName(*name);
}

//  QVariant QQuickControl::accessibleProperty(const char *propertyName)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN13QQuickControl18accessiblePropertyEPKc(
    QQuickControl *self,
    const char *propertyName) {
  return new QVariant(self->accessibleProperty(propertyName));
}

//  bool QQuickControl::setAccessibleProperty(const char *propertyName, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickControl21setAccessiblePropertyEPKcRK8QVariant(
    QQuickControl *self,
    const char *propertyName,
    const QVariant *value) {
  return self->setAccessibleProperty(propertyName, *value);
}

//  QQuickControlPrivate *QQuickControl::d_func()
extern "C" Q_DECL_EXPORT
QQuickControlPrivate *ritual_ZN13QQuickControl6d_funcEv(
    QQuickControl *self) {
  return self->d_func();
}

//  const QQuickControlPrivate *QQuickControl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickControlPrivate *ritual_ZNK13QQuickControl6d_funcEv(
    const QQuickControl *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickControl, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickControl(
    QQuickControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickControl *>(self)->take(key, call);
}

//  QFont QQuickControl::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickControl11defaultFontEv(
    const QQuickControl *self) {
  return new QFont(
      static_cast<const OwnQQuickControl *>(self)->OwnQQuickControl::defaultFont());
}

//  void QQuickControl::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl10classBeginEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::classBegin();
}

//  void QQuickControl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl17componentCompleteEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::componentComplete();
}

//  void QQuickControl::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickControl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::itemChange(
      change,
      *value);
}

//  void QQuickControl::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl12focusInEventEP11QFocusEvent(
    QQuickControl *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::focusInEvent(
      event);
}

//  void QQuickControl::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl13focusOutEventEP11QFocusEvent(
    QQuickControl *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::focusOutEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl15hoverEnterEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::hoverEnterEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl14hoverMoveEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::hoverMoveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl15hoverLeaveEventEP11QHoverEvent(
    QQuickControl *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::hoverLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickControl::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl15mousePressEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::mousePressEvent(
      event);
}

//  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl14mouseMoveEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::mouseMoveEvent(
      event);
}

//  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl17mouseReleaseEventEP11QMouseEvent(
    QQuickControl *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::mouseReleaseEvent(
      event);
}

//  void QQuickControl::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl16mouseUngrabEventEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::mouseUngrabEvent();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickControl::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl10touchEventEP11QTouchEvent(
    QQuickControl *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickControl::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl16touchUngrabEventEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickControl::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl10wheelEventEP11QWheelEvent(
    QQuickControl *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickControl::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl14geometryChangeERK6QRectFS2_(
    QQuickControl *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickControl::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl10fontChangeERK5QFontS2_(
    QQuickControl *self,
    const QFont *newFont,
    const QFont *oldFont) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::fontChange(
      *newFont,
      *oldFont);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickControl::hoverChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl11hoverChangeEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::hoverChange();
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickControl::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl12mirrorChangeEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::mirrorChange();
}

//  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl13spacingChangeEdd(
    QQuickControl *self,
    qreal newSpacing,
    qreal oldSpacing) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::spacingChange(
      newSpacing,
      oldSpacing);
}

//  void QQuickControl::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_(
    QQuickControl *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::paddingChange(
      *newPadding,
      *oldPadding);
}

//  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_(
    QQuickControl *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickControl::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl12localeChangeERK7QLocaleS2_(
    QQuickControl *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::localeChange(
      *newLocale,
      *oldLocale);
}

//  void QQuickControl::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl11insetChangeERK9QMarginsFS2_(
    QQuickControl *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::insetChange(
      *newInset,
      *oldInset);
}

//  void QQuickControl::enabledChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl13enabledChangeEv(QQuickControl *self) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::enabledChange();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickControl::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK13QQuickControl14accessibleRoleEv(
    const QQuickControl *self) {
  return static_cast<const OwnQQuickControl *>(self)->OwnQQuickControl::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickControl::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickControl26accessibilityActiveChangedEb(
    QQuickControl *self,
    bool active) {
  static_cast<OwnQQuickControl *>(self)->OwnQQuickControl::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
