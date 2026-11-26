//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p.h>
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

//  Only a class built on QQuickPage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPage : QQuickPage {
  using QQuickPage::componentComplete;
  using QQuickPage::spacingChange;
  using QQuickPage::accessibleRole;
  using QQuickPage::accessibilityActiveChanged;
};

//  A QQuickPage that Python can take functions over in. Every QQuickPage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPageCall0)(const void *, int *);
typedef void (*CuteQQuickPageCall1)(const void *, qreal, qreal, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPageCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPageCall3)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickPageCall4)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPageCall5)(const void *, const QSizeF *, const QSizeF *, int *);
typedef const QFont * (*CuteQQuickPageCall6)(const void *, int *);
typedef void (*CuteQQuickPageCall7)(const void *, int *);
typedef void (*CuteQQuickPageCall8)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPageCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPageCall10)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall13)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPageCall17)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPageCall18)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPageCall19)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPageCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPageCall21)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPageCall22)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickPageCall24)(const void *, int *);
typedef void (*CuteQQuickPageCall25)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPageCall26)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickPageCall27)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPageCall28)(const void *, int *);
typedef const QRectF * (*CuteQQuickPageCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickPageCall30)(const void *, int *);
typedef bool (*CuteQQuickPageCall31)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPageCall32)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickPageCall33)(const void *, int *);
typedef void * (*CuteQQuickPageCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPageCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall36)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPageCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPageCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPageCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPageCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPageCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickPageCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPageCall46)(const void *, int *);
typedef void (*CuteQQuickPageCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPageCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPageCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPage : public QQuickPage {
public:
  using QQuickPage::QQuickPage;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
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

  //  void QQuickPage::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPageCall0 call = reinterpret_cast<CuteQQuickPageCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPage::componentComplete();
  }

  //  void QQuickPage::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPageCall1 call = reinterpret_cast<CuteQQuickPageCall1>(taken[1]);
      call(this, newSpacing, oldSpacing, &handled);
      if (handled) return;
    }
    QQuickPage::spacingChange(newSpacing, oldSpacing);
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickPage::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPageCall2 call = reinterpret_cast<CuteQQuickPageCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickPage::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickPage::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPageCall3 call = reinterpret_cast<CuteQQuickPageCall3>(taken[3]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickPage::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPageCall4 call = reinterpret_cast<CuteQQuickPageCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPageCall5 call = reinterpret_cast<CuteQQuickPageCall5>(taken[5]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPane::contentSizeChange(newSize, oldSize);
  }

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPageCall6 call = reinterpret_cast<CuteQQuickPageCall6>(taken[6]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPageCall7 call = reinterpret_cast<CuteQQuickPageCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPageCall8 call = reinterpret_cast<CuteQQuickPageCall8>(taken[8]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPageCall9 call = reinterpret_cast<CuteQQuickPageCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPageCall10 call = reinterpret_cast<CuteQQuickPageCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPageCall11 call = reinterpret_cast<CuteQQuickPageCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPageCall12 call = reinterpret_cast<CuteQQuickPageCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPageCall13 call = reinterpret_cast<CuteQQuickPageCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPageCall14 call = reinterpret_cast<CuteQQuickPageCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPageCall15 call = reinterpret_cast<CuteQQuickPageCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPageCall16 call = reinterpret_cast<CuteQQuickPageCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPageCall17 call = reinterpret_cast<CuteQQuickPageCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPageCall18 call = reinterpret_cast<CuteQQuickPageCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPageCall19 call = reinterpret_cast<CuteQQuickPageCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPageCall20 call = reinterpret_cast<CuteQQuickPageCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPageCall21 call = reinterpret_cast<CuteQQuickPageCall21>(taken[21]);
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
      CuteQQuickPageCall22 call = reinterpret_cast<CuteQQuickPageCall22>(taken[22]);
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
      CuteQQuickPageCall23 call = reinterpret_cast<CuteQQuickPageCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPageCall24 call = reinterpret_cast<CuteQQuickPageCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::paddingChange(const QMarginsF &newPadding, const
  //      QMarginsF &oldPadding)
  void paddingChange(
      const QMarginsF &newPadding,
      const QMarginsF &oldPadding) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPageCall25 call = reinterpret_cast<CuteQQuickPageCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPageCall26 call = reinterpret_cast<CuteQQuickPageCall26>(taken[26]);
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
      CuteQQuickPageCall27 call = reinterpret_cast<CuteQQuickPageCall27>(taken[27]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPageCall28 call = reinterpret_cast<CuteQQuickPageCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPageCall29 call = reinterpret_cast<CuteQQuickPageCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPageCall30 call = reinterpret_cast<CuteQQuickPageCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPageCall31 call = reinterpret_cast<CuteQQuickPageCall31>(taken[31]);
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
      CuteQQuickPageCall32 call = reinterpret_cast<CuteQQuickPageCall32>(taken[32]);
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
      CuteQQuickPageCall33 call = reinterpret_cast<CuteQQuickPageCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPageCall34 call = reinterpret_cast<CuteQQuickPageCall34>(taken[34]);
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
      CuteQQuickPageCall35 call = reinterpret_cast<CuteQQuickPageCall35>(taken[35]);
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
      CuteQQuickPageCall36 call = reinterpret_cast<CuteQQuickPageCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPageCall37 call = reinterpret_cast<CuteQQuickPageCall37>(taken[37]);
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
      CuteQQuickPageCall38 call = reinterpret_cast<CuteQQuickPageCall38>(taken[38]);
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
      CuteQQuickPageCall39 call = reinterpret_cast<CuteQQuickPageCall39>(taken[39]);
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
      CuteQQuickPageCall40 call = reinterpret_cast<CuteQQuickPageCall40>(taken[40]);
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
      CuteQQuickPageCall41 call = reinterpret_cast<CuteQQuickPageCall41>(taken[41]);
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
      CuteQQuickPageCall42 call = reinterpret_cast<CuteQQuickPageCall42>(taken[42]);
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
      CuteQQuickPageCall43 call = reinterpret_cast<CuteQQuickPageCall43>(taken[43]);
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
      CuteQQuickPageCall44 call = reinterpret_cast<CuteQQuickPageCall44>(taken[44]);
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
      CuteQQuickPageCall45 call = reinterpret_cast<CuteQQuickPageCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickPageCall46 call = reinterpret_cast<CuteQQuickPageCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickPageCall47 call = reinterpret_cast<CuteQQuickPageCall47>(taken[47]);
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
      CuteQQuickPageCall48 call = reinterpret_cast<CuteQQuickPageCall48>(taken[48]);
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
      CuteQQuickPageCall49 call = reinterpret_cast<CuteQQuickPageCall49>(taken[49]);
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
      CuteQQuickPageCall50 call = reinterpret_cast<CuteQQuickPageCall50>(taken[50]);
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
      CuteQQuickPageCall51 call = reinterpret_cast<CuteQQuickPageCall51>(taken[51]);
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
      CuteQQuickPageCall52 call = reinterpret_cast<CuteQQuickPageCall52>(taken[52]);
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
      CuteQQuickPageCall53 call = reinterpret_cast<CuteQQuickPageCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickPage10metaObjectEv(
    const QQuickPage *self) {
  return self->metaObject();
}

//  void *QQuickPage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QQuickPage11qt_metacastEPKc(
    QQuickPage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPage::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QQuickPage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickPage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPage::tr(s, c, n));
}

//  QQuickPage::QQuickPage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPage *ritual_ZN10QQuickPageC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickPage(parent);
}

//  QQuickPage::~QQuickPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPageD1Ev(QQuickPage *self) {
  delete self;
}

//  QString QQuickPage::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickPage5titleEv(const QQuickPage *self) {
  return new QString(self->title());
}

//  void QQuickPage::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage8setTitleERK7QString(
    QQuickPage *self,
    const QString *title) {
  self->setTitle(*title);
}

//  void QQuickPage::resetTitle()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage10resetTitleEv(QQuickPage *self) {
  self->resetTitle();
}

//  QQuickItem *QQuickPage::header() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickPage6headerEv(const QQuickPage *self) {
  return self->header();
}

//  void QQuickPage::setHeader(QQuickItem *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage9setHeaderEP10QQuickItem(
    QQuickPage *self,
    QQuickItem *header) {
  self->setHeader(header);
}

//  QQuickItem *QQuickPage::footer() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickPage6footerEv(const QQuickPage *self) {
  return self->footer();
}

//  void QQuickPage::setFooter(QQuickItem *footer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage9setFooterEP10QQuickItem(
    QQuickPage *self,
    QQuickItem *footer) {
  self->setFooter(footer);
}

//  qreal QQuickPage::implicitHeaderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPage19implicitHeaderWidthEv(const QQuickPage *self) {
  return self->implicitHeaderWidth();
}

//  qreal QQuickPage::implicitHeaderHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPage20implicitHeaderHeightEv(
    const QQuickPage *self) {
  return self->implicitHeaderHeight();
}

//  qreal QQuickPage::implicitFooterWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPage19implicitFooterWidthEv(const QQuickPage *self) {
  return self->implicitFooterWidth();
}

//  qreal QQuickPage::implicitFooterHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPage20implicitFooterHeightEv(
    const QQuickPage *self) {
  return self->implicitFooterHeight();
}

//  void QQuickPage::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage12titleChangedEv(QQuickPage *self) {
  self->titleChanged();
}

//  void QQuickPage::headerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage13headerChangedEv(QQuickPage *self) {
  self->headerChanged();
}

//  void QQuickPage::footerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage13footerChangedEv(QQuickPage *self) {
  self->footerChanged();
}

//  void QQuickPage::implicitHeaderWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage26implicitHeaderWidthChangedEv(QQuickPage *self) {
  self->implicitHeaderWidthChanged();
}

//  void QQuickPage::implicitHeaderHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage27implicitHeaderHeightChangedEv(QQuickPage *self) {
  self->implicitHeaderHeightChanged();
}

//  void QQuickPage::implicitFooterWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage26implicitFooterWidthChangedEv(QQuickPage *self) {
  self->implicitFooterWidthChanged();
}

//  void QQuickPage::implicitFooterHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage27implicitFooterHeightChangedEv(QQuickPage *self) {
  self->implicitFooterHeightChanged();
}

//  QQuickPage::QQuickPage(QQuickPagePrivate &dd, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPage *ritual_ZN10QQuickPageC1ER17QQuickPagePrivateP10QQuickItem(
    QQuickPagePrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickPage(*dd, parent);
}

//  void QQuickPage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage17componentCompleteEv(QQuickPage *self) {
  self->componentComplete();
}

//  void QQuickPage::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage13spacingChangeEdd(
    QQuickPage *self,
    qreal newSpacing,
    qreal oldSpacing) {
  self->spacingChange(newSpacing, oldSpacing);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPage::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK10QQuickPage14accessibleRoleEv(
    const QQuickPage *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPage::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPage26accessibilityActiveChangedEb(
    QQuickPage *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickPagePrivate *QQuickPage::d_func()
extern "C" Q_DECL_EXPORT
QQuickPagePrivate *ritual_ZN10QQuickPage6d_funcEv(QQuickPage *self) {
  return self->d_func();
}

//  const QQuickPagePrivate *QQuickPage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPagePrivate *ritual_ZNK10QQuickPage6d_funcEv(
    const QQuickPage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickPage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPage(QQuickPage *self, const char *key, void *call) {
  return static_cast<CuteQQuickPage *>(self)->take(key, call);
}

//  void QQuickPage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPage17componentCompleteEv(QQuickPage *self) {
  static_cast<OwnQQuickPage *>(self)->OwnQQuickPage::componentComplete();
}

//  void QQuickPage::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPage13spacingChangeEdd(
    QQuickPage *self,
    qreal newSpacing,
    qreal oldSpacing) {
  static_cast<OwnQQuickPage *>(self)->OwnQQuickPage::spacingChange(
      newSpacing,
      oldSpacing);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPage::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK10QQuickPage14accessibleRoleEv(
    const QQuickPage *self) {
  return static_cast<const OwnQQuickPage *>(self)->OwnQQuickPage::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPage::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPage26accessibilityActiveChangedEb(
    QQuickPage *self,
    bool active) {
  static_cast<OwnQQuickPage *>(self)->OwnQQuickPage::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
