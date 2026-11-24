//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p.h>
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

//  Only a class built on QQuickPane may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPane : QQuickPane {
  using QQuickPane::componentComplete;
  using QQuickPane::contentItemChange;
  using QQuickPane::contentSizeChange;
  using QQuickPane::accessibleRole;
};

//  A QQuickPane that Python can take functions over in. Every QQuickPane
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPaneCall0)(const void *, int *);
typedef void (*CuteQQuickPaneCall1)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPaneCall2)(const void *, const QSizeF *, const QSizeF *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPaneCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QFont * (*CuteQQuickPaneCall4)(const void *, int *);
typedef void (*CuteQQuickPaneCall5)(const void *, int *);
typedef void (*CuteQQuickPaneCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPaneCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPaneCall8)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall9)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaneCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaneCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPaneCall15)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPaneCall16)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPaneCall17)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPaneCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPaneCall19)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPaneCall20)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall21)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPaneCall22)(const void *, int *);
typedef void (*CuteQQuickPaneCall23)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickPaneCall24)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPaneCall25)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickPaneCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPaneCall27)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPaneCall28)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickPaneCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickPaneCall30)(const void *, int *);
typedef bool (*CuteQQuickPaneCall31)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPaneCall32)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickPaneCall33)(const void *, int *);
typedef void * (*CuteQQuickPaneCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPaneCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall36)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPaneCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPaneCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPaneCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaneCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaneCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaneCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPaneCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPaneCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickPaneCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPaneCall46)(const void *, int *);
typedef void (*CuteQQuickPaneCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPaneCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPaneCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPane : public QQuickPane {
public:
  using QQuickPane::QQuickPane;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
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
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[47] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  void QQuickPane::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPaneCall0 call = reinterpret_cast<CuteQQuickPaneCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPane::componentComplete();
  }

  //  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPaneCall1 call = reinterpret_cast<CuteQQuickPaneCall1>(taken[1]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickPane::contentItemChange(newItem, oldItem);
  }

  //  void QQuickPane::contentSizeChange(const QSizeF &newSize, const
  //      QSizeF &oldSize)
  void contentSizeChange(
      const QSizeF &newSize,
      const QSizeF &oldSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPaneCall2 call = reinterpret_cast<CuteQQuickPaneCall2>(taken[2]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPane::contentSizeChange(newSize, oldSize);
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickPane::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPaneCall3 call = reinterpret_cast<CuteQQuickPaneCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickPane::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPaneCall4 call = reinterpret_cast<CuteQQuickPaneCall4>(taken[4]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPaneCall5 call = reinterpret_cast<CuteQQuickPaneCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPaneCall6 call = reinterpret_cast<CuteQQuickPaneCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPaneCall7 call = reinterpret_cast<CuteQQuickPaneCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPaneCall8 call = reinterpret_cast<CuteQQuickPaneCall8>(taken[8]);
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
      CuteQQuickPaneCall9 call = reinterpret_cast<CuteQQuickPaneCall9>(taken[9]);
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
      CuteQQuickPaneCall10 call = reinterpret_cast<CuteQQuickPaneCall10>(taken[10]);
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
      CuteQQuickPaneCall11 call = reinterpret_cast<CuteQQuickPaneCall11>(taken[11]);
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
      CuteQQuickPaneCall12 call = reinterpret_cast<CuteQQuickPaneCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPaneCall13 call = reinterpret_cast<CuteQQuickPaneCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPaneCall14 call = reinterpret_cast<CuteQQuickPaneCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPaneCall15 call = reinterpret_cast<CuteQQuickPaneCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPaneCall16 call = reinterpret_cast<CuteQQuickPaneCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPaneCall17 call = reinterpret_cast<CuteQQuickPaneCall17>(taken[17]);
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
      CuteQQuickPaneCall18 call = reinterpret_cast<CuteQQuickPaneCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPaneCall19 call = reinterpret_cast<CuteQQuickPaneCall19>(taken[19]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPaneCall20 call = reinterpret_cast<CuteQQuickPaneCall20>(taken[20]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPaneCall21 call = reinterpret_cast<CuteQQuickPaneCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPaneCall22 call = reinterpret_cast<CuteQQuickPaneCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPaneCall23 call = reinterpret_cast<CuteQQuickPaneCall23>(taken[23]);
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
      CuteQQuickPaneCall24 call = reinterpret_cast<CuteQQuickPaneCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPaneCall25 call = reinterpret_cast<CuteQQuickPaneCall25>(taken[25]);
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
      CuteQQuickPaneCall26 call = reinterpret_cast<CuteQQuickPaneCall26>(taken[26]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPaneCall27 call = reinterpret_cast<CuteQQuickPaneCall27>(taken[27]);
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
      CuteQQuickPaneCall28 call = reinterpret_cast<CuteQQuickPaneCall28>(taken[28]);
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
      CuteQQuickPaneCall29 call = reinterpret_cast<CuteQQuickPaneCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPaneCall30 call = reinterpret_cast<CuteQQuickPaneCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPaneCall31 call = reinterpret_cast<CuteQQuickPaneCall31>(taken[31]);
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
      CuteQQuickPaneCall32 call = reinterpret_cast<CuteQQuickPaneCall32>(taken[32]);
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
      CuteQQuickPaneCall33 call = reinterpret_cast<CuteQQuickPaneCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPaneCall34 call = reinterpret_cast<CuteQQuickPaneCall34>(taken[34]);
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
      CuteQQuickPaneCall35 call = reinterpret_cast<CuteQQuickPaneCall35>(taken[35]);
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
      CuteQQuickPaneCall36 call = reinterpret_cast<CuteQQuickPaneCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPaneCall37 call = reinterpret_cast<CuteQQuickPaneCall37>(taken[37]);
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
      CuteQQuickPaneCall38 call = reinterpret_cast<CuteQQuickPaneCall38>(taken[38]);
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
      CuteQQuickPaneCall39 call = reinterpret_cast<CuteQQuickPaneCall39>(taken[39]);
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
      CuteQQuickPaneCall40 call = reinterpret_cast<CuteQQuickPaneCall40>(taken[40]);
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
      CuteQQuickPaneCall41 call = reinterpret_cast<CuteQQuickPaneCall41>(taken[41]);
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
      CuteQQuickPaneCall42 call = reinterpret_cast<CuteQQuickPaneCall42>(taken[42]);
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
      CuteQQuickPaneCall43 call = reinterpret_cast<CuteQQuickPaneCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickPaneCall44 call = reinterpret_cast<CuteQQuickPaneCall44>(taken[44]);
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
    if (taken[45]) {
      int handled = 0;
      CuteQQuickPaneCall45 call = reinterpret_cast<CuteQQuickPaneCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickPaneCall46 call = reinterpret_cast<CuteQQuickPaneCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickPaneCall47 call = reinterpret_cast<CuteQQuickPaneCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickPaneCall48 call = reinterpret_cast<CuteQQuickPaneCall48>(taken[48]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickPaneCall49 call = reinterpret_cast<CuteQQuickPaneCall49>(taken[49]);
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
      CuteQQuickPaneCall50 call = reinterpret_cast<CuteQQuickPaneCall50>(taken[50]);
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
      CuteQQuickPaneCall51 call = reinterpret_cast<CuteQQuickPaneCall51>(taken[51]);
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
      CuteQQuickPaneCall52 call = reinterpret_cast<CuteQQuickPaneCall52>(taken[52]);
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
      CuteQQuickPaneCall53 call = reinterpret_cast<CuteQQuickPaneCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPane::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickPane10metaObjectEv(
    const QQuickPane *self) {
  return self->metaObject();
}

//  QString QQuickPane::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickPane2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPane::tr(s, c, n));
}

//  QQuickPane::QQuickPane(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPane *ritual_ZN10QQuickPaneC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickPane(parent);
}

//  QQuickPane::~QQuickPane()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPaneD1Ev(QQuickPane *self) {
  delete self;
}

//  qreal QQuickPane::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPane12contentWidthEv(const QQuickPane *self) {
  return self->contentWidth();
}

//  void QQuickPane::setContentWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane15setContentWidthEd(
    QQuickPane *self,
    qreal width) {
  self->setContentWidth(width);
}

//  void QQuickPane::resetContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane17resetContentWidthEv(QQuickPane *self) {
  self->resetContentWidth();
}

//  qreal QQuickPane::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPane13contentHeightEv(const QQuickPane *self) {
  return self->contentHeight();
}

//  void QQuickPane::setContentHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane16setContentHeightEd(
    QQuickPane *self,
    qreal height) {
  self->setContentHeight(height);
}

//  void QQuickPane::resetContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane18resetContentHeightEv(QQuickPane *self) {
  self->resetContentHeight();
}

//  void QQuickPane::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane17componentCompleteEv(QQuickPane *self) {
  self->componentComplete();
}

//  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane17contentItemChangeEP10QQuickItemS1_(
    QQuickPane *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickPane::contentSizeChange(const QSizeF &newSize, const QSizeF
//      &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_(
    QQuickPane *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  self->contentSizeChange(*newSize, *oldSize);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPane::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK10QQuickPane14accessibleRoleEv(
    const QQuickPane *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickPanePrivate *QQuickPane::d_func()
extern "C" Q_DECL_EXPORT
QQuickPanePrivate *ritual_ZN10QQuickPane6d_funcEv(QQuickPane *self) {
  return self->d_func();
}

//  const QQuickPanePrivate *QQuickPane::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPanePrivate *ritual_ZNK10QQuickPane6d_funcEv(
    const QQuickPane *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPane, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPane(QQuickPane *self, const char *key, void *call) {
  return static_cast<CuteQQuickPane *>(self)->take(key, call);
}

//  void QQuickPane::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPane17componentCompleteEv(QQuickPane *self) {
  static_cast<OwnQQuickPane *>(self)->OwnQQuickPane::componentComplete();
}

//  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPane17contentItemChangeEP10QQuickItemS1_(
    QQuickPane *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickPane *>(self)->OwnQQuickPane::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickPane::contentSizeChange(const QSizeF &newSize, const QSizeF
//      &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_(
    QQuickPane *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  static_cast<OwnQQuickPane *>(self)->OwnQQuickPane::contentSizeChange(
      *newSize,
      *oldSize);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPane::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK10QQuickPane14accessibleRoleEv(
    const QQuickPane *self) {
  return static_cast<const OwnQQuickPane *>(self)->OwnQQuickPane::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
