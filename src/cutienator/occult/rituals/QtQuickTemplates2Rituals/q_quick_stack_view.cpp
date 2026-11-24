//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QQuickStackView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickStackView : QQuickStackView {
  using QQuickStackView::componentComplete;
  using QQuickStackView::geometryChange;
  using QQuickStackView::childMouseEventFilter;
  using QQuickStackView::touchEvent;
  using QQuickStackView::accessibleRole;
};

//  A QQuickStackView that Python can take functions over in. Every QQuickStackView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickStackViewCall0)(const void *, int *);
typedef void (*CuteQQuickStackViewCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef bool (*CuteQQuickStackViewCall2)(const void *, QQuickItem *, QEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickStackViewCall3)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickStackViewCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickStackViewCall5)(const void *, int *);
typedef void (*CuteQQuickStackViewCall6)(const void *, int *);
typedef void (*CuteQQuickStackViewCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickStackViewCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickStackViewCall9)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStackViewCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStackViewCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickStackViewCall16)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickStackViewCall17)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickStackViewCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickStackViewCall19)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall20)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickStackViewCall21)(const void *, int *);
typedef void (*CuteQQuickStackViewCall22)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickStackViewCall23)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickStackViewCall24)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickStackViewCall25)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickStackViewCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickStackViewCall27)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickStackViewCall28)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickStackViewCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickStackViewCall30)(const void *, int *);
typedef bool (*CuteQQuickStackViewCall31)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickStackViewCall32)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickStackViewCall33)(const void *, int *);
typedef void * (*CuteQQuickStackViewCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStackViewCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall36)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickStackViewCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickStackViewCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickStackViewCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStackViewCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStackViewCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStackViewCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickStackViewCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickStackViewCall44)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickStackViewCall45)(const void *, int *);
typedef void (*CuteQQuickStackViewCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStackViewCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStackViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStackView : public QQuickStackView {
public:
  using QQuickStackView::QQuickStackView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[37] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[39] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
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

  //  void QQuickStackView::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStackViewCall0 call = reinterpret_cast<CuteQQuickStackViewCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStackView::componentComplete();
  }

  //  void QQuickStackView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStackViewCall1 call = reinterpret_cast<CuteQQuickStackViewCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickStackView::geometryChange(newGeometry, oldGeometry);
  }

  //  bool QQuickStackView::childMouseEventFilter(QQuickItem *a0, QEvent
  //      *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStackViewCall2 call = reinterpret_cast<CuteQQuickStackViewCall2>(taken[2]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickStackView::childMouseEventFilter(a0, a1);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickStackView::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStackViewCall3 call = reinterpret_cast<CuteQQuickStackViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickStackView::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickStackView::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStackViewCall4 call = reinterpret_cast<CuteQQuickStackViewCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickStackView::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStackViewCall5 call = reinterpret_cast<CuteQQuickStackViewCall5>(taken[5]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickStackViewCall6 call = reinterpret_cast<CuteQQuickStackViewCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStackViewCall7 call = reinterpret_cast<CuteQQuickStackViewCall7>(taken[7]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStackViewCall8 call = reinterpret_cast<CuteQQuickStackViewCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStackViewCall9 call = reinterpret_cast<CuteQQuickStackViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStackViewCall10 call = reinterpret_cast<CuteQQuickStackViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickStackViewCall11 call = reinterpret_cast<CuteQQuickStackViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickStackViewCall12 call = reinterpret_cast<CuteQQuickStackViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickStackViewCall13 call = reinterpret_cast<CuteQQuickStackViewCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickStackViewCall14 call = reinterpret_cast<CuteQQuickStackViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickStackViewCall15 call = reinterpret_cast<CuteQQuickStackViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickStackViewCall16 call = reinterpret_cast<CuteQQuickStackViewCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickStackViewCall17 call = reinterpret_cast<CuteQQuickStackViewCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickStackViewCall18 call = reinterpret_cast<CuteQQuickStackViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickStackViewCall19 call = reinterpret_cast<CuteQQuickStackViewCall19>(taken[19]);
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
      CuteQQuickStackViewCall20 call = reinterpret_cast<CuteQQuickStackViewCall20>(taken[20]);
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
      CuteQQuickStackViewCall21 call = reinterpret_cast<CuteQQuickStackViewCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickStackViewCall22 call = reinterpret_cast<CuteQQuickStackViewCall22>(taken[22]);
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
      CuteQQuickStackViewCall23 call = reinterpret_cast<CuteQQuickStackViewCall23>(taken[23]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickStackViewCall24 call = reinterpret_cast<CuteQQuickStackViewCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickStackViewCall25 call = reinterpret_cast<CuteQQuickStackViewCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQuickStackViewCall26 call = reinterpret_cast<CuteQQuickStackViewCall26>(taken[26]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickStackViewCall27 call = reinterpret_cast<CuteQQuickStackViewCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickStackViewCall28 call = reinterpret_cast<CuteQQuickStackViewCall28>(taken[28]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickStackViewCall29 call = reinterpret_cast<CuteQQuickStackViewCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickStackViewCall30 call = reinterpret_cast<CuteQQuickStackViewCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickStackViewCall31 call = reinterpret_cast<CuteQQuickStackViewCall31>(taken[31]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickStackViewCall32 call = reinterpret_cast<CuteQQuickStackViewCall32>(taken[32]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickStackViewCall33 call = reinterpret_cast<CuteQQuickStackViewCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickStackViewCall34 call = reinterpret_cast<CuteQQuickStackViewCall34>(taken[34]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickStackViewCall35 call = reinterpret_cast<CuteQQuickStackViewCall35>(taken[35]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickStackViewCall36 call = reinterpret_cast<CuteQQuickStackViewCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickStackViewCall37 call = reinterpret_cast<CuteQQuickStackViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickStackViewCall38 call = reinterpret_cast<CuteQQuickStackViewCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickStackViewCall39 call = reinterpret_cast<CuteQQuickStackViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickStackViewCall40 call = reinterpret_cast<CuteQQuickStackViewCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickStackViewCall41 call = reinterpret_cast<CuteQQuickStackViewCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickStackViewCall42 call = reinterpret_cast<CuteQQuickStackViewCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickStackViewCall43 call = reinterpret_cast<CuteQQuickStackViewCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickStackViewCall44 call = reinterpret_cast<CuteQQuickStackViewCall44>(taken[44]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickStackViewCall45 call = reinterpret_cast<CuteQQuickStackViewCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickStackViewCall46 call = reinterpret_cast<CuteQQuickStackViewCall46>(taken[46]);
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
      CuteQQuickStackViewCall47 call = reinterpret_cast<CuteQQuickStackViewCall47>(taken[47]);
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
      CuteQQuickStackViewCall48 call = reinterpret_cast<CuteQQuickStackViewCall48>(taken[48]);
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
      CuteQQuickStackViewCall49 call = reinterpret_cast<CuteQQuickStackViewCall49>(taken[49]);
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
      CuteQQuickStackViewCall50 call = reinterpret_cast<CuteQQuickStackViewCall50>(taken[50]);
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
      CuteQQuickStackViewCall51 call = reinterpret_cast<CuteQQuickStackViewCall51>(taken[51]);
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
      CuteQQuickStackViewCall52 call = reinterpret_cast<CuteQQuickStackViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStackView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickStackView10metaObjectEv(
    const QQuickStackView *self) {
  return self->metaObject();
}

//  QString QQuickStackView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickStackView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStackView::tr(s, c, n));
}

//  void QQuickStackView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView21qt_qmlMarker_attachedEv(
    QQuickStackView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickStackView::QQuickStackView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickStackView *ritual_ZN15QQuickStackViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickStackView(parent);
}

//  QQuickStackView::~QQuickStackView()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackViewD1Ev(QQuickStackView *self) {
  delete self;
}

//  QQuickStackViewAttached *QQuickStackView::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickStackViewAttached *ritual_ZN15QQuickStackView21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickStackView::qmlAttachedProperties(object);
}

//  bool QQuickStackView::isBusy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickStackView6isBusyEv(const QQuickStackView *self) {
  return self->isBusy();
}

//  int QQuickStackView::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickStackView5depthEv(const QQuickStackView *self) {
  return self->depth();
}

//  QQuickItem *QQuickStackView::currentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickStackView11currentItemEv(
    const QQuickStackView *self) {
  return self->currentItem();
}

//  QJSValue QQuickStackView::initialItem() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QQuickStackView11initialItemEv(
    const QQuickStackView *self) {
  return new QJSValue(self->initialItem());
}

//  void QQuickStackView::setInitialItem(const QJSValue &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView14setInitialItemERK8QJSValue(
    QQuickStackView *self,
    const QJSValue *item) {
  self->setInitialItem(*item);
}

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::popEnter() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView8popEnterEv(
    const QQuickStackView *self) {
  return self->popEnter();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setPopEnter(QQuickTransition *enter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView11setPopEnterEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *enter) {
  self->setPopEnter(enter);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::popExit() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView7popExitEv(
    const QQuickStackView *self) {
  return self->popExit();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setPopExit(QQuickTransition *exit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView10setPopExitEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *exit) {
  self->setPopExit(exit);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::pushEnter() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView9pushEnterEv(
    const QQuickStackView *self) {
  return self->pushEnter();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setPushEnter(QQuickTransition *enter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView12setPushEnterEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *enter) {
  self->setPushEnter(enter);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::pushExit() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView8pushExitEv(
    const QQuickStackView *self) {
  return self->pushExit();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setPushExit(QQuickTransition *exit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView11setPushExitEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *exit) {
  self->setPushExit(exit);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::replaceEnter() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView12replaceEnterEv(
    const QQuickStackView *self) {
  return self->replaceEnter();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setReplaceEnter(QQuickTransition *enter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView15setReplaceEnterEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *enter) {
  self->setReplaceEnter(enter);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickStackView::replaceExit() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK15QQuickStackView11replaceExitEv(
    const QQuickStackView *self) {
  return self->replaceExit();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackView::setReplaceExit(QQuickTransition *exit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView14setReplaceExitEP16QQuickTransition(
    QQuickStackView *self,
    QQuickTransition *exit) {
  self->setReplaceExit(exit);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  QQuickItem *QQuickStackView::get(int index, QQuickStackView::LoadBehavior
//      behavior)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView3getEiNS_12LoadBehaviorE(
    QQuickStackView *self,
    int index,
    QQuickStackView::LoadBehavior behavior) {
  return self->get(index, behavior);
}

//  QQuickItem *QQuickStackView::find(const QJSValue &callback,
//      QQuickStackView::LoadBehavior behavior)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView4findERK8QJSValueNS_12LoadBehaviorE(
    QQuickStackView *self,
    const QJSValue *callback,
    QQuickStackView::LoadBehavior behavior) {
  return self->find(*callback, behavior);
}

//  void QQuickStackView::push(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView4pushEP14QQmlV4Function(
    QQuickStackView *self,
    QQmlV4FunctionPtr args) {
  self->push(args);
}

//  void QQuickStackView::pop(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView3popEP14QQmlV4Function(
    QQuickStackView *self,
    QQmlV4FunctionPtr args) {
  self->pop(args);
}

//  void QQuickStackView::replace(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView7replaceEP14QQmlV4Function(
    QQuickStackView *self,
    QQmlV4FunctionPtr args) {
  self->replace(args);
}

//  QQuickItem *QQuickStackView::pushItems(QList<QQuickStackViewArg> args,
//      Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView9pushItemsE5QListI18QQuickStackViewArgENS_9OperationE(
    QQuickStackView *self,
    const QList<QQuickStackViewArg> *args,
    QQuickStackView::Operation operation) {
  return self->pushItems(*args, operation);
}

//  QQuickItem *QQuickStackView::pushItem(QQuickItem *item, const QVariantMap
//      &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView8pushItemEP10QQuickItemRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    QQuickItem *item,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->pushItem(item, *properties, operation);
}

//  QQuickItem *QQuickStackView::pushItem(QQmlComponent *component, const
//      QVariantMap &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView8pushItemEP13QQmlComponentRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    QQmlComponent *component,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->pushItem(component, *properties, operation);
}

//  QQuickItem *QQuickStackView::pushItem(const QUrl &url, const QVariantMap
//      &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView8pushItemERK4QUrlRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    const QUrl *url,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->pushItem(*url, *properties, operation);
}

//  QQuickItem *QQuickStackView::popToItem(QQuickItem *item, Operation
//      operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView9popToItemEP10QQuickItemNS_9OperationE(
    QQuickStackView *self,
    QQuickItem *item,
    QQuickStackView::Operation operation) {
  return self->popToItem(item, operation);
}

//  QQuickItem *QQuickStackView::popToIndex(int index, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView10popToIndexEiNS_9OperationE(
    QQuickStackView *self,
    int index,
    QQuickStackView::Operation operation) {
  return self->popToIndex(index, operation);
}

//  QQuickItem *QQuickStackView::popCurrentItem(Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView14popCurrentItemENS_9OperationE(
    QQuickStackView *self,
    QQuickStackView::Operation operation) {
  return self->popCurrentItem(operation);
}

//  QQuickItem *QQuickStackView::replaceCurrentItem(const
//      QList<QQuickStackViewArg> &args, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView18replaceCurrentItemERK5QListI18QQuickStackViewArgENS_9OperationE(
    QQuickStackView *self,
    const QList<QQuickStackViewArg> *args,
    QQuickStackView::Operation operation) {
  return self->replaceCurrentItem(*args, operation);
}

//  QQuickItem *QQuickStackView::replaceCurrentItem(QQuickItem *item, const
//      QVariantMap &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView18replaceCurrentItemEP10QQuickItemRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    QQuickItem *item,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->replaceCurrentItem(item, *properties, operation);
}

//  QQuickItem *QQuickStackView::replaceCurrentItem(QQmlComponent *component,
//      const QVariantMap &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView18replaceCurrentItemEP13QQmlComponentRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    QQmlComponent *component,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->replaceCurrentItem(component, *properties, operation);
}

//  QQuickItem *QQuickStackView::replaceCurrentItem(const QUrl &url, const
//      QVariantMap &properties, Operation operation)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickStackView18replaceCurrentItemERK4QUrlRK4QMapI7QString8QVariantENS_9OperationE(
    QQuickStackView *self,
    const QUrl *url,
    const QMap<QString, QVariant> *properties,
    QQuickStackView::Operation operation) {
  return self->replaceCurrentItem(*url, *properties, operation);
}

//  bool QQuickStackView::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickStackView7isEmptyEv(const QQuickStackView *self) {
  return self->isEmpty();
}

//  void QQuickStackView::clear(Operation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView5clearENS_9OperationE(
    QQuickStackView *self,
    QQuickStackView::Operation operation) {
  self->clear(operation);
}

//  void QQuickStackView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView17componentCompleteEv(QQuickStackView *self) {
  self->componentComplete();
}

//  void QQuickStackView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView14geometryChangeERK6QRectFS2_(
    QQuickStackView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  bool QQuickStackView::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickStackView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickStackView *self,
    QQuickItem *a0,
    QEvent *a1) {
  return self->childMouseEventFilter(a0, a1);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickStackView::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStackView10touchEventEP11QTouchEvent(
    QQuickStackView *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickStackView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickStackView14accessibleRoleEv(
    const QQuickStackView *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickStackViewPrivate *QQuickStackView::d_func()
extern "C" Q_DECL_EXPORT
QQuickStackViewPrivate *ritual_ZN15QQuickStackView6d_funcEv(
    QQuickStackView *self) {
  return self->d_func();
}

//  const QQuickStackViewPrivate *QQuickStackView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickStackViewPrivate *ritual_ZNK15QQuickStackView6d_funcEv(
    const QQuickStackView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickStackView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStackView(
    QQuickStackView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStackView *>(self)->take(key, call);
}

//  void QQuickStackView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickStackView17componentCompleteEv(
    QQuickStackView *self) {
  static_cast<OwnQQuickStackView *>(self)->OwnQQuickStackView::componentComplete();
}

//  void QQuickStackView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickStackView14geometryChangeERK6QRectFS2_(
    QQuickStackView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickStackView *>(self)->OwnQQuickStackView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  bool QQuickStackView::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickStackView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickStackView *self,
    QQuickItem *a0,
    QEvent *a1) {
  return static_cast<OwnQQuickStackView *>(self)->OwnQQuickStackView::childMouseEventFilter(
      a0,
      a1);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickStackView::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickStackView10touchEventEP11QTouchEvent(
    QQuickStackView *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickStackView *>(self)->OwnQQuickStackView::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickStackView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickStackView14accessibleRoleEv(
    const QQuickStackView *self) {
  return static_cast<const OwnQQuickStackView *>(self)->OwnQQuickStackView::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
