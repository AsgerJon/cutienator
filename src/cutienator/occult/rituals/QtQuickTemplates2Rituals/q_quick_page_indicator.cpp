//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickpageindicator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpageindicator_p.h>
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

//  Only a class built on QQuickPageIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPageIndicator : QQuickPageIndicator {
  using QQuickPageIndicator::contentItemChange;
  using QQuickPageIndicator::touchEvent;
  using QQuickPageIndicator::accessibleRole;
};

//  A QQuickPageIndicator that Python can take functions over in. Every QQuickPageIndicator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPageIndicatorCall0)(const void *, QQuickItem *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPageIndicatorCall1)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPageIndicatorCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickPageIndicatorCall3)(const void *, int *);
typedef void (*CuteQQuickPageIndicatorCall4)(const void *, int *);
typedef void (*CuteQQuickPageIndicatorCall5)(const void *, int *);
typedef void (*CuteQQuickPageIndicatorCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPageIndicatorCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPageIndicatorCall8)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall9)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageIndicatorCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageIndicatorCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageIndicatorCall15)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPageIndicatorCall16)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPageIndicatorCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPageIndicatorCall18)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPageIndicatorCall19)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall20)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageIndicatorCall21)(const void *, int *);
typedef void (*CuteQQuickPageIndicatorCall22)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickPageIndicatorCall23)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPageIndicatorCall24)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickPageIndicatorCall25)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPageIndicatorCall26)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPageIndicatorCall27)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickPageIndicatorCall28)(const void *, int *);
typedef const QRectF * (*CuteQQuickPageIndicatorCall29)(const void *, int *);
typedef bool (*CuteQQuickPageIndicatorCall30)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPageIndicatorCall31)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickPageIndicatorCall32)(const void *, int *);
typedef void * (*CuteQQuickPageIndicatorCall33)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPageIndicatorCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall35)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPageIndicatorCall36)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPageIndicatorCall37)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPageIndicatorCall38)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageIndicatorCall39)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageIndicatorCall40)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageIndicatorCall41)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageIndicatorCall42)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPageIndicatorCall43)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickPageIndicatorCall44)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPageIndicatorCall45)(const void *, int *);
typedef void (*CuteQQuickPageIndicatorCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPageIndicatorCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageIndicatorCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPageIndicator : public QQuickPageIndicator {
public:
  using QQuickPageIndicator::QQuickPageIndicator;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[26] = call;
      return true;
    }
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

  //  void QQuickPageIndicator::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall0 call = reinterpret_cast<CuteQQuickPageIndicatorCall0>(taken[0]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickPageIndicator::contentItemChange(newItem, oldItem);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPageIndicator::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall1 call = reinterpret_cast<CuteQQuickPageIndicatorCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPageIndicator::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickPageIndicator::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall2 call = reinterpret_cast<CuteQQuickPageIndicatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickPageIndicator::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall3 call = reinterpret_cast<CuteQQuickPageIndicatorCall3>(taken[3]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall4 call = reinterpret_cast<CuteQQuickPageIndicatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall5 call = reinterpret_cast<CuteQQuickPageIndicatorCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall6 call = reinterpret_cast<CuteQQuickPageIndicatorCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall7 call = reinterpret_cast<CuteQQuickPageIndicatorCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall8 call = reinterpret_cast<CuteQQuickPageIndicatorCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall9 call = reinterpret_cast<CuteQQuickPageIndicatorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall10 call = reinterpret_cast<CuteQQuickPageIndicatorCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall11 call = reinterpret_cast<CuteQQuickPageIndicatorCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall12 call = reinterpret_cast<CuteQQuickPageIndicatorCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall13 call = reinterpret_cast<CuteQQuickPageIndicatorCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall14 call = reinterpret_cast<CuteQQuickPageIndicatorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall15 call = reinterpret_cast<CuteQQuickPageIndicatorCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall16 call = reinterpret_cast<CuteQQuickPageIndicatorCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall17 call = reinterpret_cast<CuteQQuickPageIndicatorCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall18 call = reinterpret_cast<CuteQQuickPageIndicatorCall18>(taken[18]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall19 call = reinterpret_cast<CuteQQuickPageIndicatorCall19>(taken[19]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall20 call = reinterpret_cast<CuteQQuickPageIndicatorCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall21 call = reinterpret_cast<CuteQQuickPageIndicatorCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall22 call = reinterpret_cast<CuteQQuickPageIndicatorCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall23 call = reinterpret_cast<CuteQQuickPageIndicatorCall23>(taken[23]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::localeChange(const QLocale &newLocale, const
  //      QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall24 call = reinterpret_cast<CuteQQuickPageIndicatorCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall25 call = reinterpret_cast<CuteQQuickPageIndicatorCall25>(taken[25]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall26 call = reinterpret_cast<CuteQQuickPageIndicatorCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall27 call = reinterpret_cast<CuteQQuickPageIndicatorCall27>(taken[27]);
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
      CuteQQuickPageIndicatorCall28 call = reinterpret_cast<CuteQQuickPageIndicatorCall28>(taken[28]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall29 call = reinterpret_cast<CuteQQuickPageIndicatorCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall30 call = reinterpret_cast<CuteQQuickPageIndicatorCall30>(taken[30]);
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
      CuteQQuickPageIndicatorCall31 call = reinterpret_cast<CuteQQuickPageIndicatorCall31>(taken[31]);
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
      CuteQQuickPageIndicatorCall32 call = reinterpret_cast<CuteQQuickPageIndicatorCall32>(taken[32]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall33 call = reinterpret_cast<CuteQQuickPageIndicatorCall33>(taken[33]);
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
      CuteQQuickPageIndicatorCall34 call = reinterpret_cast<CuteQQuickPageIndicatorCall34>(taken[34]);
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
      CuteQQuickPageIndicatorCall35 call = reinterpret_cast<CuteQQuickPageIndicatorCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall36 call = reinterpret_cast<CuteQQuickPageIndicatorCall36>(taken[36]);
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
      CuteQQuickPageIndicatorCall37 call = reinterpret_cast<CuteQQuickPageIndicatorCall37>(taken[37]);
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
      CuteQQuickPageIndicatorCall38 call = reinterpret_cast<CuteQQuickPageIndicatorCall38>(taken[38]);
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
      CuteQQuickPageIndicatorCall39 call = reinterpret_cast<CuteQQuickPageIndicatorCall39>(taken[39]);
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
      CuteQQuickPageIndicatorCall40 call = reinterpret_cast<CuteQQuickPageIndicatorCall40>(taken[40]);
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
      CuteQQuickPageIndicatorCall41 call = reinterpret_cast<CuteQQuickPageIndicatorCall41>(taken[41]);
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
      CuteQQuickPageIndicatorCall42 call = reinterpret_cast<CuteQQuickPageIndicatorCall42>(taken[42]);
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
      CuteQQuickPageIndicatorCall43 call = reinterpret_cast<CuteQQuickPageIndicatorCall43>(taken[43]);
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
      CuteQQuickPageIndicatorCall44 call = reinterpret_cast<CuteQQuickPageIndicatorCall44>(taken[44]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall45 call = reinterpret_cast<CuteQQuickPageIndicatorCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickPageIndicatorCall46 call = reinterpret_cast<CuteQQuickPageIndicatorCall46>(taken[46]);
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
      CuteQQuickPageIndicatorCall47 call = reinterpret_cast<CuteQQuickPageIndicatorCall47>(taken[47]);
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
      CuteQQuickPageIndicatorCall48 call = reinterpret_cast<CuteQQuickPageIndicatorCall48>(taken[48]);
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
      CuteQQuickPageIndicatorCall49 call = reinterpret_cast<CuteQQuickPageIndicatorCall49>(taken[49]);
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
      CuteQQuickPageIndicatorCall50 call = reinterpret_cast<CuteQQuickPageIndicatorCall50>(taken[50]);
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
      CuteQQuickPageIndicatorCall51 call = reinterpret_cast<CuteQQuickPageIndicatorCall51>(taken[51]);
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
      CuteQQuickPageIndicatorCall52 call = reinterpret_cast<CuteQQuickPageIndicatorCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPageIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPageIndicator10metaObjectEv(
    const QQuickPageIndicator *self) {
  return self->metaObject();
}

//  QString QQuickPageIndicator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickPageIndicator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPageIndicator::tr(s, c, n));
}

//  QQuickPageIndicator::QQuickPageIndicator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPageIndicator *ritual_ZN19QQuickPageIndicatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPageIndicator(parent);
}

//  QQuickPageIndicator::~QQuickPageIndicator()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicatorD1Ev(QQuickPageIndicator *self) {
  delete self;
}

//  int QQuickPageIndicator::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickPageIndicator5countEv(
    const QQuickPageIndicator *self) {
  return self->count();
}

//  void QQuickPageIndicator::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator8setCountEi(
    QQuickPageIndicator *self,
    int count) {
  self->setCount(count);
}

//  int QQuickPageIndicator::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickPageIndicator12currentIndexEv(
    const QQuickPageIndicator *self) {
  return self->currentIndex();
}

//  void QQuickPageIndicator::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator15setCurrentIndexEi(
    QQuickPageIndicator *self,
    int index) {
  self->setCurrentIndex(index);
}

//  bool QQuickPageIndicator::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickPageIndicator13isInteractiveEv(
    const QQuickPageIndicator *self) {
  return self->isInteractive();
}

//  void QQuickPageIndicator::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator14setInteractiveEb(
    QQuickPageIndicator *self,
    bool interactive) {
  self->setInteractive(interactive);
}

//  QQmlComponent *QQuickPageIndicator::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK19QQuickPageIndicator8delegateEv(
    const QQuickPageIndicator *self) {
  return self->delegate();
}

//  void QQuickPageIndicator::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator11setDelegateEP13QQmlComponent(
    QQuickPageIndicator *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  void QQuickPageIndicator::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator17contentItemChangeEP10QQuickItemS1_(
    QQuickPageIndicator *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPageIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPageIndicator10touchEventEP11QTouchEvent(
    QQuickPageIndicator *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPageIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickPageIndicator14accessibleRoleEv(
    const QQuickPageIndicator *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQQuickPageIndicator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPageIndicator(
    QQuickPageIndicator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPageIndicator *>(self)->take(key, call);
}

//  void QQuickPageIndicator::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickPageIndicator17contentItemChangeEP10QQuickItemS1_(
    QQuickPageIndicator *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickPageIndicator *>(self)->OwnQQuickPageIndicator::contentItemChange(
      newItem,
      oldItem);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPageIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickPageIndicator10touchEventEP11QTouchEvent(
    QQuickPageIndicator *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickPageIndicator *>(self)->OwnQQuickPageIndicator::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPageIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickPageIndicator14accessibleRoleEv(
    const QQuickPageIndicator *self) {
  return static_cast<const OwnQQuickPageIndicator *>(self)->OwnQQuickPageIndicator::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
