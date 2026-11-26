//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
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

//  Only a class built on QQuickScrollView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickScrollView : QQuickScrollView {
  using QQuickScrollView::childMouseEventFilter;
  using QQuickScrollView::eventFilter;
  using QQuickScrollView::keyPressEvent;
  using QQuickScrollView::componentComplete;
  using QQuickScrollView::contentItemChange;
  using QQuickScrollView::contentSizeChange;
  using QQuickScrollView::accessibleRole;
};

//  A QQuickScrollView that Python can take functions over in. Every QQuickScrollView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickScrollViewCall0)(const void *, QQuickItem *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall2)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickScrollViewCall3)(const void *, int *);
typedef void (*CuteQQuickScrollViewCall4)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickScrollViewCall5)(const void *, const QSizeF *, const QSizeF *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickScrollViewCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickScrollViewCall7)(const void *, int *);
typedef void (*CuteQQuickScrollViewCall8)(const void *, int *);
typedef void (*CuteQQuickScrollViewCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickScrollViewCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickScrollViewCall11)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall13)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall14)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickScrollViewCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickScrollViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickScrollViewCall18)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickScrollViewCall19)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickScrollViewCall20)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickScrollViewCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickScrollViewCall22)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickScrollViewCall23)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall24)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickScrollViewCall25)(const void *, int *);
typedef void (*CuteQQuickScrollViewCall26)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickScrollViewCall27)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickScrollViewCall28)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickScrollViewCall29)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickScrollViewCall30)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickScrollViewCall31)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickScrollViewCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickScrollViewCall33)(const void *, int *);
typedef bool (*CuteQQuickScrollViewCall34)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickScrollViewCall35)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickScrollViewCall36)(const void *, int *);
typedef void * (*CuteQQuickScrollViewCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollViewCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall39)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickScrollViewCall40)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickScrollViewCall41)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickScrollViewCall42)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickScrollViewCall43)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickScrollViewCall44)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickScrollViewCall45)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void * (*CuteQQuickScrollViewCall46)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickScrollViewCall47)(const void *, int *);
typedef void (*CuteQQuickScrollViewCall48)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollViewCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScrollView : public QQuickScrollView {
public:
  using QQuickScrollView::QQuickScrollView;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[37] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[39] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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

  //  bool QQuickScrollView::childMouseEventFilter(QQuickItem *item, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *item, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScrollViewCall0 call = reinterpret_cast<CuteQQuickScrollViewCall0>(taken[0]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickScrollView::childMouseEventFilter(item, event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickScrollView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScrollViewCall1 call = reinterpret_cast<CuteQQuickScrollViewCall1>(taken[1]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickScrollView::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickScrollView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScrollViewCall2 call = reinterpret_cast<CuteQQuickScrollViewCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickScrollView::keyPressEvent(event);
  }

  //  void QQuickScrollView::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScrollViewCall3 call = reinterpret_cast<CuteQQuickScrollViewCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickScrollView::componentComplete();
  }

  //  void QQuickScrollView::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickScrollViewCall4 call = reinterpret_cast<CuteQQuickScrollViewCall4>(taken[4]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickScrollView::contentItemChange(newItem, oldItem);
  }

  //  void QQuickScrollView::contentSizeChange(const QSizeF &newSize, const
  //      QSizeF &oldSize)
  void contentSizeChange(
      const QSizeF &newSize,
      const QSizeF &oldSize) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickScrollViewCall5 call = reinterpret_cast<CuteQQuickScrollViewCall5>(taken[5]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickScrollView::contentSizeChange(newSize, oldSize);
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickScrollView::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickScrollViewCall6 call = reinterpret_cast<CuteQQuickScrollViewCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickScrollView::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickScrollViewCall7 call = reinterpret_cast<CuteQQuickScrollViewCall7>(taken[7]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickScrollViewCall8 call = reinterpret_cast<CuteQQuickScrollViewCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQQuickScrollViewCall9 call = reinterpret_cast<CuteQQuickScrollViewCall9>(taken[9]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickScrollViewCall10 call = reinterpret_cast<CuteQQuickScrollViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickScrollViewCall11 call = reinterpret_cast<CuteQQuickScrollViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickScrollViewCall12 call = reinterpret_cast<CuteQQuickScrollViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickScrollViewCall13 call = reinterpret_cast<CuteQQuickScrollViewCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickScrollViewCall14 call = reinterpret_cast<CuteQQuickScrollViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickScrollViewCall15 call = reinterpret_cast<CuteQQuickScrollViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickScrollViewCall16 call = reinterpret_cast<CuteQQuickScrollViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickScrollViewCall17 call = reinterpret_cast<CuteQQuickScrollViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickScrollViewCall18 call = reinterpret_cast<CuteQQuickScrollViewCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickScrollViewCall19 call = reinterpret_cast<CuteQQuickScrollViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickScrollViewCall20 call = reinterpret_cast<CuteQQuickScrollViewCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickScrollViewCall21 call = reinterpret_cast<CuteQQuickScrollViewCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQQuickScrollViewCall22 call = reinterpret_cast<CuteQQuickScrollViewCall22>(taken[22]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickScrollViewCall23 call = reinterpret_cast<CuteQQuickScrollViewCall23>(taken[23]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickScrollViewCall24 call = reinterpret_cast<CuteQQuickScrollViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickScrollViewCall25 call = reinterpret_cast<CuteQQuickScrollViewCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickScrollViewCall26 call = reinterpret_cast<CuteQQuickScrollViewCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQuickScrollViewCall27 call = reinterpret_cast<CuteQQuickScrollViewCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickScrollViewCall28 call = reinterpret_cast<CuteQQuickScrollViewCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQuickScrollViewCall29 call = reinterpret_cast<CuteQQuickScrollViewCall29>(taken[29]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickScrollViewCall30 call = reinterpret_cast<CuteQQuickScrollViewCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickScrollViewCall31 call = reinterpret_cast<CuteQQuickScrollViewCall31>(taken[31]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickScrollViewCall32 call = reinterpret_cast<CuteQQuickScrollViewCall32>(taken[32]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickScrollViewCall33 call = reinterpret_cast<CuteQQuickScrollViewCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickScrollViewCall34 call = reinterpret_cast<CuteQQuickScrollViewCall34>(taken[34]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickScrollViewCall35 call = reinterpret_cast<CuteQQuickScrollViewCall35>(taken[35]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickScrollViewCall36 call = reinterpret_cast<CuteQQuickScrollViewCall36>(taken[36]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickScrollViewCall37 call = reinterpret_cast<CuteQQuickScrollViewCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickScrollViewCall38 call = reinterpret_cast<CuteQQuickScrollViewCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickScrollViewCall39 call = reinterpret_cast<CuteQQuickScrollViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickScrollViewCall40 call = reinterpret_cast<CuteQQuickScrollViewCall40>(taken[40]);
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
      CuteQQuickScrollViewCall41 call = reinterpret_cast<CuteQQuickScrollViewCall41>(taken[41]);
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
      CuteQQuickScrollViewCall42 call = reinterpret_cast<CuteQQuickScrollViewCall42>(taken[42]);
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
      CuteQQuickScrollViewCall43 call = reinterpret_cast<CuteQQuickScrollViewCall43>(taken[43]);
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
      CuteQQuickScrollViewCall44 call = reinterpret_cast<CuteQQuickScrollViewCall44>(taken[44]);
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
      CuteQQuickScrollViewCall45 call = reinterpret_cast<CuteQQuickScrollViewCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQQuickScrollViewCall46 call = reinterpret_cast<CuteQQuickScrollViewCall46>(taken[46]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickScrollViewCall47 call = reinterpret_cast<CuteQQuickScrollViewCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickScrollViewCall48 call = reinterpret_cast<CuteQQuickScrollViewCall48>(taken[48]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickScrollViewCall49 call = reinterpret_cast<CuteQQuickScrollViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickScrollViewCall50 call = reinterpret_cast<CuteQQuickScrollViewCall50>(taken[50]);
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
      CuteQQuickScrollViewCall51 call = reinterpret_cast<CuteQQuickScrollViewCall51>(taken[51]);
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
      CuteQQuickScrollViewCall52 call = reinterpret_cast<CuteQQuickScrollViewCall52>(taken[52]);
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
      CuteQQuickScrollViewCall53 call = reinterpret_cast<CuteQQuickScrollViewCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScrollView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickScrollView10metaObjectEv(
    const QQuickScrollView *self) {
  return self->metaObject();
}

//  void *QQuickScrollView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickScrollView11qt_metacastEPKc(
    QQuickScrollView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickScrollView::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickScrollView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickScrollView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickScrollView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickScrollView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScrollView::tr(s, c, n));
}

//  QQuickScrollView::QQuickScrollView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickScrollView *ritual_ZN16QQuickScrollViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickScrollView(parent);
}

//  QQuickScrollView::~QQuickScrollView()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollViewD1Ev(QQuickScrollView *self) {
  delete self;
}

//  qreal QQuickScrollView::effectiveScrollBarWidth()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN16QQuickScrollView23effectiveScrollBarWidthEv(
    QQuickScrollView *self) {
  return self->effectiveScrollBarWidth();
}

//  qreal QQuickScrollView::effectiveScrollBarHeight()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN16QQuickScrollView24effectiveScrollBarHeightEv(
    QQuickScrollView *self) {
  return self->effectiveScrollBarHeight();
}

//  bool QQuickScrollView::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickScrollView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickScrollView *self,
    QQuickItem *item,
    QEvent *event) {
  return self->childMouseEventFilter(item, event);
}

//  bool QQuickScrollView::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickScrollView11eventFilterEP7QObjectP6QEvent(
    QQuickScrollView *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QQuickScrollView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView13keyPressEventEP9QKeyEvent(
    QQuickScrollView *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickScrollView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView17componentCompleteEv(
    QQuickScrollView *self) {
  self->componentComplete();
}

//  void QQuickScrollView::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView17contentItemChangeEP10QQuickItemS1_(
    QQuickScrollView *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickScrollView::contentSizeChange(const QSizeF &newSize, const
//      QSizeF &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView17contentSizeChangeERK6QSizeFS2_(
    QQuickScrollView *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  self->contentSizeChange(*newSize, *oldSize);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK16QQuickScrollView14accessibleRoleEv(
    const QQuickScrollView *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickScrollView::effectiveScrollBarWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView30effectiveScrollBarWidthChangedEv(
    QQuickScrollView *self) {
  self->effectiveScrollBarWidthChanged();
}

//  void QQuickScrollView::effectiveScrollBarHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScrollView31effectiveScrollBarHeightChangedEv(
    QQuickScrollView *self) {
  self->effectiveScrollBarHeightChanged();
}

//  QQuickScrollViewPrivate *QQuickScrollView::d_func()
extern "C" Q_DECL_EXPORT
QQuickScrollViewPrivate *ritual_ZN16QQuickScrollView6d_funcEv(
    QQuickScrollView *self) {
  return self->d_func();
}

//  const QQuickScrollViewPrivate *QQuickScrollView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickScrollViewPrivate *ritual_ZNK16QQuickScrollView6d_funcEv(
    const QQuickScrollView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickScrollView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScrollView(
    QQuickScrollView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScrollView *>(self)->take(key, call);
}

//  bool QQuickScrollView::childMouseEventFilter(QQuickItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickScrollView21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickScrollView *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::childMouseEventFilter(
      item,
      event);
}

//  bool QQuickScrollView::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickScrollView11eventFilterEP7QObjectP6QEvent(
    QQuickScrollView *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::eventFilter(
      object,
      event);
}

//  void QQuickScrollView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickScrollView13keyPressEventEP9QKeyEvent(
    QQuickScrollView *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::keyPressEvent(
      event);
}

//  void QQuickScrollView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickScrollView17componentCompleteEv(
    QQuickScrollView *self) {
  static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::componentComplete();
}

//  void QQuickScrollView::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickScrollView17contentItemChangeEP10QQuickItemS1_(
    QQuickScrollView *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickScrollView::contentSizeChange(const QSizeF &newSize, const
//      QSizeF &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickScrollView17contentSizeChangeERK6QSizeFS2_(
    QQuickScrollView *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  static_cast<OwnQQuickScrollView *>(self)->OwnQQuickScrollView::contentSizeChange(
      *newSize,
      *oldSize);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK16QQuickScrollView14accessibleRoleEv(
    const QQuickScrollView *self) {
  return static_cast<const OwnQQuickScrollView *>(self)->OwnQQuickScrollView::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
