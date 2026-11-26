//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickgroupbox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickgroupbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickGroupBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGroupBox : QQuickGroupBox {
  using QQuickGroupBox::componentComplete;
  using QQuickGroupBox::defaultFont;
  using QQuickGroupBox::accessibleRole;
  using QQuickGroupBox::accessibilityActiveChanged;
};

//  A QQuickGroupBox that Python can take functions over in. Every QQuickGroupBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGroupBoxCall0)(const void *, int *);
typedef const QFont * (*CuteQQuickGroupBoxCall1)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickGroupBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickGroupBoxCall3)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickGroupBoxCall4)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickGroupBoxCall5)(const void *, const QSizeF *, const QSizeF *, int *);
typedef void (*CuteQQuickGroupBoxCall6)(const void *, int *);
typedef void (*CuteQQuickGroupBoxCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGroupBoxCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGroupBoxCall9)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGroupBoxCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGroupBoxCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGroupBoxCall16)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickGroupBoxCall17)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickGroupBoxCall18)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGroupBoxCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGroupBoxCall20)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickGroupBoxCall21)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickGroupBoxCall23)(const void *, int *);
typedef void (*CuteQQuickGroupBoxCall24)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickGroupBoxCall25)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickGroupBoxCall26)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickGroupBoxCall27)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickGroupBoxCall28)(const void *, int *);
typedef const QRectF * (*CuteQQuickGroupBoxCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickGroupBoxCall30)(const void *, int *);
typedef bool (*CuteQQuickGroupBoxCall31)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGroupBoxCall32)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickGroupBoxCall33)(const void *, int *);
typedef void * (*CuteQQuickGroupBoxCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGroupBoxCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall36)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickGroupBoxCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGroupBoxCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGroupBoxCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGroupBoxCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGroupBoxCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGroupBoxCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGroupBoxCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickGroupBoxCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickGroupBoxCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickGroupBoxCall46)(const void *, int *);
typedef void (*CuteQQuickGroupBoxCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGroupBoxCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGroupBoxCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGroupBox : public QQuickGroupBox {
public:
  using QQuickGroupBox::QQuickGroupBox;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
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
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
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

  //  void QQuickGroupBox::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGroupBoxCall0 call = reinterpret_cast<CuteQQuickGroupBoxCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGroupBox::componentComplete();
  }

  //  QFont QQuickGroupBox::defaultFont() const
  QFont defaultFont() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGroupBoxCall1 call = reinterpret_cast<CuteQQuickGroupBoxCall1>(taken[1]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickGroupBox::defaultFont();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickGroupBox::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGroupBoxCall2 call = reinterpret_cast<CuteQQuickGroupBoxCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickGroupBox::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickGroupBox::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGroupBoxCall3 call = reinterpret_cast<CuteQQuickGroupBoxCall3>(taken[3]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickGroupBox::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGroupBoxCall4 call = reinterpret_cast<CuteQQuickGroupBoxCall4>(taken[4]);
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
      CuteQQuickGroupBoxCall5 call = reinterpret_cast<CuteQQuickGroupBoxCall5>(taken[5]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPane::contentSizeChange(newSize, oldSize);
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGroupBoxCall6 call = reinterpret_cast<CuteQQuickGroupBoxCall6>(taken[6]);
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
      CuteQQuickGroupBoxCall7 call = reinterpret_cast<CuteQQuickGroupBoxCall7>(taken[7]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGroupBoxCall8 call = reinterpret_cast<CuteQQuickGroupBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGroupBoxCall9 call = reinterpret_cast<CuteQQuickGroupBoxCall9>(taken[9]);
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
      CuteQQuickGroupBoxCall10 call = reinterpret_cast<CuteQQuickGroupBoxCall10>(taken[10]);
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
      CuteQQuickGroupBoxCall11 call = reinterpret_cast<CuteQQuickGroupBoxCall11>(taken[11]);
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
      CuteQQuickGroupBoxCall12 call = reinterpret_cast<CuteQQuickGroupBoxCall12>(taken[12]);
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
      CuteQQuickGroupBoxCall13 call = reinterpret_cast<CuteQQuickGroupBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGroupBoxCall14 call = reinterpret_cast<CuteQQuickGroupBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGroupBoxCall15 call = reinterpret_cast<CuteQQuickGroupBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGroupBoxCall16 call = reinterpret_cast<CuteQQuickGroupBoxCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGroupBoxCall17 call = reinterpret_cast<CuteQQuickGroupBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGroupBoxCall18 call = reinterpret_cast<CuteQQuickGroupBoxCall18>(taken[18]);
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
      CuteQQuickGroupBoxCall19 call = reinterpret_cast<CuteQQuickGroupBoxCall19>(taken[19]);
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
      CuteQQuickGroupBoxCall20 call = reinterpret_cast<CuteQQuickGroupBoxCall20>(taken[20]);
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
      CuteQQuickGroupBoxCall21 call = reinterpret_cast<CuteQQuickGroupBoxCall21>(taken[21]);
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
      CuteQQuickGroupBoxCall22 call = reinterpret_cast<CuteQQuickGroupBoxCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGroupBoxCall23 call = reinterpret_cast<CuteQQuickGroupBoxCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGroupBoxCall24 call = reinterpret_cast<CuteQQuickGroupBoxCall24>(taken[24]);
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
      CuteQQuickGroupBoxCall25 call = reinterpret_cast<CuteQQuickGroupBoxCall25>(taken[25]);
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
      CuteQQuickGroupBoxCall26 call = reinterpret_cast<CuteQQuickGroupBoxCall26>(taken[26]);
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
      CuteQQuickGroupBoxCall27 call = reinterpret_cast<CuteQQuickGroupBoxCall27>(taken[27]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGroupBoxCall28 call = reinterpret_cast<CuteQQuickGroupBoxCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGroupBoxCall29 call = reinterpret_cast<CuteQQuickGroupBoxCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGroupBoxCall30 call = reinterpret_cast<CuteQQuickGroupBoxCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGroupBoxCall31 call = reinterpret_cast<CuteQQuickGroupBoxCall31>(taken[31]);
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
      CuteQQuickGroupBoxCall32 call = reinterpret_cast<CuteQQuickGroupBoxCall32>(taken[32]);
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
      CuteQQuickGroupBoxCall33 call = reinterpret_cast<CuteQQuickGroupBoxCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickGroupBoxCall34 call = reinterpret_cast<CuteQQuickGroupBoxCall34>(taken[34]);
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
      CuteQQuickGroupBoxCall35 call = reinterpret_cast<CuteQQuickGroupBoxCall35>(taken[35]);
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
      CuteQQuickGroupBoxCall36 call = reinterpret_cast<CuteQQuickGroupBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGroupBoxCall37 call = reinterpret_cast<CuteQQuickGroupBoxCall37>(taken[37]);
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
      CuteQQuickGroupBoxCall38 call = reinterpret_cast<CuteQQuickGroupBoxCall38>(taken[38]);
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
      CuteQQuickGroupBoxCall39 call = reinterpret_cast<CuteQQuickGroupBoxCall39>(taken[39]);
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
      CuteQQuickGroupBoxCall40 call = reinterpret_cast<CuteQQuickGroupBoxCall40>(taken[40]);
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
      CuteQQuickGroupBoxCall41 call = reinterpret_cast<CuteQQuickGroupBoxCall41>(taken[41]);
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
      CuteQQuickGroupBoxCall42 call = reinterpret_cast<CuteQQuickGroupBoxCall42>(taken[42]);
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
      CuteQQuickGroupBoxCall43 call = reinterpret_cast<CuteQQuickGroupBoxCall43>(taken[43]);
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
      CuteQQuickGroupBoxCall44 call = reinterpret_cast<CuteQQuickGroupBoxCall44>(taken[44]);
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
      CuteQQuickGroupBoxCall45 call = reinterpret_cast<CuteQQuickGroupBoxCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickGroupBoxCall46 call = reinterpret_cast<CuteQQuickGroupBoxCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGroupBoxCall47 call = reinterpret_cast<CuteQQuickGroupBoxCall47>(taken[47]);
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
      CuteQQuickGroupBoxCall48 call = reinterpret_cast<CuteQQuickGroupBoxCall48>(taken[48]);
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
      CuteQQuickGroupBoxCall49 call = reinterpret_cast<CuteQQuickGroupBoxCall49>(taken[49]);
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
      CuteQQuickGroupBoxCall50 call = reinterpret_cast<CuteQQuickGroupBoxCall50>(taken[50]);
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
      CuteQQuickGroupBoxCall51 call = reinterpret_cast<CuteQQuickGroupBoxCall51>(taken[51]);
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
      CuteQQuickGroupBoxCall52 call = reinterpret_cast<CuteQQuickGroupBoxCall52>(taken[52]);
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
      CuteQQuickGroupBoxCall53 call = reinterpret_cast<CuteQQuickGroupBoxCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGroupBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickGroupBox10metaObjectEv(
    const QQuickGroupBox *self) {
  return self->metaObject();
}

//  void *QQuickGroupBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickGroupBox11qt_metacastEPKc(
    QQuickGroupBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGroupBox::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickGroupBox11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGroupBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGroupBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickGroupBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGroupBox::tr(s, c, n));
}

//  QQuickGroupBox::QQuickGroupBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGroupBox *ritual_ZN14QQuickGroupBoxC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickGroupBox(parent);
}

//  QQuickGroupBox::~QQuickGroupBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBoxD1Ev(QQuickGroupBox *self) {
  delete self;
}

//  QString QQuickGroupBox::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickGroupBox5titleEv(const QQuickGroupBox *self) {
  return new QString(self->title());
}

//  void QQuickGroupBox::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox8setTitleERK7QString(
    QQuickGroupBox *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QQuickItem *QQuickGroupBox::label() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickGroupBox5labelEv(const QQuickGroupBox *self) {
  return self->label();
}

//  void QQuickGroupBox::setLabel(QQuickItem *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox8setLabelEP10QQuickItem(
    QQuickGroupBox *self,
    QQuickItem *label) {
  self->setLabel(label);
}

//  qreal QQuickGroupBox::implicitLabelWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickGroupBox18implicitLabelWidthEv(
    const QQuickGroupBox *self) {
  return self->implicitLabelWidth();
}

//  qreal QQuickGroupBox::implicitLabelHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickGroupBox19implicitLabelHeightEv(
    const QQuickGroupBox *self) {
  return self->implicitLabelHeight();
}

//  void QQuickGroupBox::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox12titleChangedEv(QQuickGroupBox *self) {
  self->titleChanged();
}

//  void QQuickGroupBox::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox12labelChangedEv(QQuickGroupBox *self) {
  self->labelChanged();
}

//  void QQuickGroupBox::implicitLabelWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox25implicitLabelWidthChangedEv(
    QQuickGroupBox *self) {
  self->implicitLabelWidthChanged();
}

//  void QQuickGroupBox::implicitLabelHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox26implicitLabelHeightChangedEv(
    QQuickGroupBox *self) {
  self->implicitLabelHeightChanged();
}

//  void QQuickGroupBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox17componentCompleteEv(QQuickGroupBox *self) {
  self->componentComplete();
}

//  QFont QQuickGroupBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickGroupBox11defaultFontEv(
    const QQuickGroupBox *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickGroupBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK14QQuickGroupBox14accessibleRoleEv(
    const QQuickGroupBox *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickGroupBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickGroupBox26accessibilityActiveChangedEb(
    QQuickGroupBox *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickGroupBoxPrivate *QQuickGroupBox::d_func()
extern "C" Q_DECL_EXPORT
QQuickGroupBoxPrivate *ritual_ZN14QQuickGroupBox6d_funcEv(
    QQuickGroupBox *self) {
  return self->d_func();
}

//  const QQuickGroupBoxPrivate *QQuickGroupBox::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickGroupBoxPrivate *ritual_ZNK14QQuickGroupBox6d_funcEv(
    const QQuickGroupBox *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickGroupBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGroupBox(
    QQuickGroupBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGroupBox *>(self)->take(key, call);
}

//  void QQuickGroupBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGroupBox17componentCompleteEv(
    QQuickGroupBox *self) {
  static_cast<OwnQQuickGroupBox *>(self)->OwnQQuickGroupBox::componentComplete();
}

//  QFont QQuickGroupBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK14QQuickGroupBox11defaultFontEv(
    const QQuickGroupBox *self) {
  return new QFont(
      static_cast<const OwnQQuickGroupBox *>(self)->OwnQQuickGroupBox::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickGroupBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK14QQuickGroupBox14accessibleRoleEv(
    const QQuickGroupBox *self) {
  return static_cast<const OwnQQuickGroupBox *>(self)->OwnQQuickGroupBox::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickGroupBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickGroupBox26accessibilityActiveChangedEb(
    QQuickGroupBox *self,
    bool active) {
  static_cast<OwnQQuickGroupBox *>(self)->OwnQQuickGroupBox::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
