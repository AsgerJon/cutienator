//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksplitview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksplitview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickSplitView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSplitView : QQuickSplitView {
  using QQuickSplitView::componentComplete;
  using QQuickSplitView::hoverMoveEvent;
  using QQuickSplitView::hoverLeaveEvent;
  using QQuickSplitView::childMouseEventFilter;
  using QQuickSplitView::geometryChange;
  using QQuickSplitView::itemAdded;
  using QQuickSplitView::itemMoved;
  using QQuickSplitView::itemRemoved;
  using QQuickSplitView::accessibleRole;
};

//  A QQuickSplitView that Python can take functions over in. Every QQuickSplitView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickSplitViewCall0)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall1)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall2)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall3)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickSplitViewCall4)(const void *, QQuickItem *, QEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall5)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall6)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall7)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall8)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef int (*CuteQQuickSplitViewCall9)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall10)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSplitViewCall11)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
typedef const QFont * (*CuteQQuickSplitViewCall12)(const void *, int *);
typedef void (*CuteQQuickSplitViewCall13)(const void *, int *);
typedef void (*CuteQQuickSplitViewCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSplitViewCall15)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSplitViewCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSplitViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSplitViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSplitViewCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSplitViewCall20)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSplitViewCall21)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSplitViewCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSplitViewCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSplitViewCall24)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSplitViewCall25)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSplitViewCall26)(const void *, int *);
typedef void (*CuteQQuickSplitViewCall27)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickSplitViewCall28)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSplitViewCall29)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickSplitViewCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSplitViewCall31)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSplitViewCall32)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickSplitViewCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickSplitViewCall34)(const void *, int *);
typedef bool (*CuteQQuickSplitViewCall35)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickSplitViewCall36)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickSplitViewCall37)(const void *, int *);
typedef void * (*CuteQQuickSplitViewCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSplitViewCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall40)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSplitViewCall41)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickSplitViewCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickSplitViewCall43)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSplitViewCall44)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSplitViewCall45)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSplitViewCall46)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSplitViewCall47)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickSplitViewCall48)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickSplitViewCall49)(const void *, int *);
typedef void (*CuteQQuickSplitViewCall50)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSplitViewCall51)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSplitViewCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSplitView : public QQuickSplitView {
public:
  using QQuickSplitView::QQuickSplitView;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK15QQuickContainer9isContentEP10QQuickItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemAddedEiP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemMovedEiP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer11itemRemovedEiP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
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
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[41] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[43] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[50] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickSplitView::isContent(QQuickItem *item) const
  bool isContent(QQuickItem *item) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSplitViewCall0 call = reinterpret_cast<CuteQQuickSplitViewCall0>(taken[0]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickSplitView::isContent(item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSplitViewCall1 call = reinterpret_cast<CuteQQuickSplitViewCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSplitView::componentComplete();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSplitViewCall2 call = reinterpret_cast<CuteQQuickSplitViewCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSplitView::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSplitViewCall3 call = reinterpret_cast<CuteQQuickSplitViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSplitView::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickSplitView::childMouseEventFilter(QQuickItem *item, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *item, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSplitViewCall4 call = reinterpret_cast<CuteQQuickSplitViewCall4>(taken[4]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickSplitView::childMouseEventFilter(item, event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSplitViewCall5 call = reinterpret_cast<CuteQQuickSplitViewCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickSplitView::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::itemAdded(int index, QQuickItem *item)
  void itemAdded(int index, QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSplitViewCall6 call = reinterpret_cast<CuteQQuickSplitViewCall6>(taken[6]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickSplitView::itemAdded(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::itemMoved(int index, QQuickItem *item)
  void itemMoved(int index, QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSplitViewCall7 call = reinterpret_cast<CuteQQuickSplitViewCall7>(taken[7]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickSplitView::itemMoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickSplitView::itemRemoved(int index, QQuickItem *item)
  void itemRemoved(int index, QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSplitViewCall8 call = reinterpret_cast<CuteQQuickSplitViewCall8>(taken[8]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickSplitView::itemRemoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
  //  QAccessible::Role QQuickSplitView::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSplitViewCall9 call = reinterpret_cast<CuteQQuickSplitViewCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickSplitView::accessibleRole();
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSplitViewCall10 call = reinterpret_cast<CuteQQuickSplitViewCall10>(taken[10]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickContainer::itemChange(change, data);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSplitViewCall11 call = reinterpret_cast<CuteQQuickSplitViewCall11>(taken[11]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickContainer::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSplitViewCall12 call = reinterpret_cast<CuteQQuickSplitViewCall12>(taken[12]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSplitViewCall13 call = reinterpret_cast<CuteQQuickSplitViewCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSplitViewCall14 call = reinterpret_cast<CuteQQuickSplitViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSplitViewCall15 call = reinterpret_cast<CuteQQuickSplitViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSplitViewCall16 call = reinterpret_cast<CuteQQuickSplitViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSplitViewCall17 call = reinterpret_cast<CuteQQuickSplitViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSplitViewCall18 call = reinterpret_cast<CuteQQuickSplitViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSplitViewCall19 call = reinterpret_cast<CuteQQuickSplitViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSplitViewCall20 call = reinterpret_cast<CuteQQuickSplitViewCall20>(taken[20]);
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
      CuteQQuickSplitViewCall21 call = reinterpret_cast<CuteQQuickSplitViewCall21>(taken[21]);
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
      CuteQQuickSplitViewCall22 call = reinterpret_cast<CuteQQuickSplitViewCall22>(taken[22]);
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
      CuteQQuickSplitViewCall23 call = reinterpret_cast<CuteQQuickSplitViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickSplitViewCall24 call = reinterpret_cast<CuteQQuickSplitViewCall24>(taken[24]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSplitViewCall25 call = reinterpret_cast<CuteQQuickSplitViewCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSplitViewCall26 call = reinterpret_cast<CuteQQuickSplitViewCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSplitViewCall27 call = reinterpret_cast<CuteQQuickSplitViewCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSplitViewCall28 call = reinterpret_cast<CuteQQuickSplitViewCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSplitViewCall29 call = reinterpret_cast<CuteQQuickSplitViewCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSplitViewCall30 call = reinterpret_cast<CuteQQuickSplitViewCall30>(taken[30]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSplitViewCall31 call = reinterpret_cast<CuteQQuickSplitViewCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSplitViewCall32 call = reinterpret_cast<CuteQQuickSplitViewCall32>(taken[32]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSplitViewCall33 call = reinterpret_cast<CuteQQuickSplitViewCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSplitViewCall34 call = reinterpret_cast<CuteQQuickSplitViewCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSplitViewCall35 call = reinterpret_cast<CuteQQuickSplitViewCall35>(taken[35]);
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
      CuteQQuickSplitViewCall36 call = reinterpret_cast<CuteQQuickSplitViewCall36>(taken[36]);
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
      CuteQQuickSplitViewCall37 call = reinterpret_cast<CuteQQuickSplitViewCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickSplitViewCall38 call = reinterpret_cast<CuteQQuickSplitViewCall38>(taken[38]);
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
      CuteQQuickSplitViewCall39 call = reinterpret_cast<CuteQQuickSplitViewCall39>(taken[39]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickSplitViewCall40 call = reinterpret_cast<CuteQQuickSplitViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickSplitViewCall41 call = reinterpret_cast<CuteQQuickSplitViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickSplitViewCall42 call = reinterpret_cast<CuteQQuickSplitViewCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickSplitViewCall43 call = reinterpret_cast<CuteQQuickSplitViewCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickSplitViewCall44 call = reinterpret_cast<CuteQQuickSplitViewCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickSplitViewCall45 call = reinterpret_cast<CuteQQuickSplitViewCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickSplitViewCall46 call = reinterpret_cast<CuteQQuickSplitViewCall46>(taken[46]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickSplitViewCall47 call = reinterpret_cast<CuteQQuickSplitViewCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQQuickSplitViewCall48 call = reinterpret_cast<CuteQQuickSplitViewCall48>(taken[48]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickSplitViewCall49 call = reinterpret_cast<CuteQQuickSplitViewCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickSplitViewCall50 call = reinterpret_cast<CuteQQuickSplitViewCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickSplitViewCall51 call = reinterpret_cast<CuteQQuickSplitViewCall51>(taken[51]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickSplitViewCall52 call = reinterpret_cast<CuteQQuickSplitViewCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickSplitViewCall53 call = reinterpret_cast<CuteQQuickSplitViewCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickSplitViewCall54 call = reinterpret_cast<CuteQQuickSplitViewCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickSplitViewCall55 call = reinterpret_cast<CuteQQuickSplitViewCall55>(taken[55]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickSplitViewCall56 call = reinterpret_cast<CuteQQuickSplitViewCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSplitView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickSplitView10metaObjectEv(
    const QQuickSplitView *self) {
  return self->metaObject();
}

//  QString QQuickSplitView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickSplitView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSplitView::tr(s, c, n));
}

//  void QQuickSplitView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView21qt_qmlMarker_attachedEv(
    QQuickSplitView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickSplitView::QQuickSplitView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSplitView *ritual_ZN15QQuickSplitViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickSplitView(parent);
}

//  QQuickSplitView::~QQuickSplitView()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitViewD1Ev(QQuickSplitView *self) {
  delete self;
}

//  Qt::Orientation QQuickSplitView::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QQuickSplitView11orientationEv(
    const QQuickSplitView *self) {
  return self->orientation();
}

//  void QQuickSplitView::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView14setOrientationEN2Qt11OrientationE(
    QQuickSplitView *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  bool QQuickSplitView::isResizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickSplitView10isResizingEv(const QQuickSplitView *self) {
  return self->isResizing();
}

//  QQmlComponent *QQuickSplitView::handle()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN15QQuickSplitView6handleEv(QQuickSplitView *self) {
  return self->handle();
}

//  void QQuickSplitView::setHandle(QQmlComponent *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView9setHandleEP13QQmlComponent(
    QQuickSplitView *self,
    QQmlComponent *handle) {
  self->setHandle(handle);
}

//  bool QQuickSplitView::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickSplitView9isContentEP10QQuickItem(
    const QQuickSplitView *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  QQuickSplitViewAttached *QQuickSplitView::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickSplitViewAttached *ritual_ZN15QQuickSplitView21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickSplitView::qmlAttachedProperties(object);
}

//  QVariant QQuickSplitView::saveState()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QQuickSplitView9saveStateEv(QQuickSplitView *self) {
  return new QVariant(self->saveState());
}

//  bool QQuickSplitView::restoreState(const QVariant &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickSplitView12restoreStateERK8QVariant(
    QQuickSplitView *self,
    const QVariant *state) {
  return self->restoreState(*state);
}

//  void QQuickSplitView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView17componentCompleteEv(QQuickSplitView *self) {
  self->componentComplete();
}

//  void QQuickSplitView::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView14hoverMoveEventEP11QHoverEvent(
    QQuickSplitView *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickSplitView::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView15hoverLeaveEventEP11QHoverEvent(
    QQuickSplitView *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  bool QQuickSplitView::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickSplitView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickSplitView *self,
    QQuickItem *item,
    QEvent *event) {
  return self->childMouseEventFilter(item, event);
}

//  void QQuickSplitView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView14geometryChangeERK6QRectFS2_(
    QQuickSplitView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickSplitView::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView9itemAddedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickSplitView::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView9itemMovedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  self->itemMoved(index, item);
}

//  void QQuickSplitView::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSplitView11itemRemovedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSplitView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickSplitView14accessibleRoleEv(
    const QQuickSplitView *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQQuickSplitView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSplitView(
    QQuickSplitView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSplitView *>(self)->take(key, call);
}

//  bool QQuickSplitView::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQuickSplitView9isContentEP10QQuickItem(
    const QQuickSplitView *self,
    QQuickItem *item) {
  return self->QQuickSplitView::isContent(item);
}

//  void QQuickSplitView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView17componentCompleteEv(
    QQuickSplitView *self) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::componentComplete();
}

//  void QQuickSplitView::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView14hoverMoveEventEP11QHoverEvent(
    QQuickSplitView *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::hoverMoveEvent(
      event);
}

//  void QQuickSplitView::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView15hoverLeaveEventEP11QHoverEvent(
    QQuickSplitView *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::hoverLeaveEvent(
      event);
}

//  bool QQuickSplitView::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickSplitView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickSplitView *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::childMouseEventFilter(
      item,
      event);
}

//  void QQuickSplitView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView14geometryChangeERK6QRectFS2_(
    QQuickSplitView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickSplitView::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView9itemAddedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::itemAdded(
      index,
      item);
}

//  void QQuickSplitView::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView9itemMovedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::itemMoved(
      index,
      item);
}

//  void QQuickSplitView::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSplitView11itemRemovedEiP10QQuickItem(
    QQuickSplitView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSplitView *>(self)->OwnQQuickSplitView::itemRemoved(
      index,
      item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSplitView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickSplitView14accessibleRoleEv(
    const QQuickSplitView *self) {
  return static_cast<const OwnQQuickSplitView *>(self)->OwnQQuickSplitView::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
