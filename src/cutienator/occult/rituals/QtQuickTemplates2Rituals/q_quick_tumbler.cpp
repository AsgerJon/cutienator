//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTumbler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTumbler : QQuickTumbler {
  using QQuickTumbler::geometryChange;
  using QQuickTumbler::componentComplete;
  using QQuickTumbler::contentItemChange;
  using QQuickTumbler::keyPressEvent;
  using QQuickTumbler::updatePolish;
  using QQuickTumbler::defaultFont;
};

//  A QQuickTumbler that Python can take functions over in. Every QQuickTumbler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTumblerCall0)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTumblerCall1)(const void *, int *);
typedef void (*CuteQQuickTumblerCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickTumblerCall3)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTumblerCall4)(const void *, int *);
typedef const QFont * (*CuteQQuickTumblerCall5)(const void *, int *);
typedef void (*CuteQQuickTumblerCall6)(const void *, int *);
typedef void (*CuteQQuickTumblerCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTumblerCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTumblerCall9)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTumblerCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTumblerCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTumblerCall16)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickTumblerCall17)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickTumblerCall18)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTumblerCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTumblerCall20)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall21)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTumblerCall22)(const void *, int *);
typedef void (*CuteQQuickTumblerCall23)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickTumblerCall24)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickTumblerCall25)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickTumblerCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickTumblerCall27)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTumblerCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTumblerCall29)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickTumblerCall30)(const void *, int *);
typedef const QRectF * (*CuteQQuickTumblerCall31)(const void *, int *);
typedef bool (*CuteQQuickTumblerCall32)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTumblerCall33)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickTumblerCall34)(const void *, int *);
typedef void * (*CuteQQuickTumblerCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTumblerCall36)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTumblerCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTumblerCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTumblerCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTumblerCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTumblerCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTumblerCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTumblerCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickTumblerCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTumblerCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTumblerCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTumblerCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTumbler : public QQuickTumbler {
public:
  using QQuickTumbler::QQuickTumbler;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[4] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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

  //  void QQuickTumbler::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTumblerCall0 call = reinterpret_cast<CuteQQuickTumblerCall0>(taken[0]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTumbler::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickTumbler::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTumblerCall1 call = reinterpret_cast<CuteQQuickTumblerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTumbler::componentComplete();
  }

  //  void QQuickTumbler::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTumblerCall2 call = reinterpret_cast<CuteQQuickTumblerCall2>(taken[2]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickTumbler::contentItemChange(newItem, oldItem);
  }

  //  void QQuickTumbler::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTumblerCall3 call = reinterpret_cast<CuteQQuickTumblerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTumbler::keyPressEvent(event);
  }

  //  void QQuickTumbler::updatePolish()
  void updatePolish() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTumblerCall4 call = reinterpret_cast<CuteQQuickTumblerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTumbler::updatePolish();
  }

  //  QFont QQuickTumbler::defaultFont() const
  QFont defaultFont() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTumblerCall5 call = reinterpret_cast<CuteQQuickTumblerCall5>(taken[5]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTumbler::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTumblerCall6 call = reinterpret_cast<CuteQQuickTumblerCall6>(taken[6]);
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
      CuteQQuickTumblerCall7 call = reinterpret_cast<CuteQQuickTumblerCall7>(taken[7]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTumblerCall8 call = reinterpret_cast<CuteQQuickTumblerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTumblerCall9 call = reinterpret_cast<CuteQQuickTumblerCall9>(taken[9]);
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
      CuteQQuickTumblerCall10 call = reinterpret_cast<CuteQQuickTumblerCall10>(taken[10]);
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
      CuteQQuickTumblerCall11 call = reinterpret_cast<CuteQQuickTumblerCall11>(taken[11]);
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
      CuteQQuickTumblerCall12 call = reinterpret_cast<CuteQQuickTumblerCall12>(taken[12]);
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
      CuteQQuickTumblerCall13 call = reinterpret_cast<CuteQQuickTumblerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTumblerCall14 call = reinterpret_cast<CuteQQuickTumblerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTumblerCall15 call = reinterpret_cast<CuteQQuickTumblerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTumblerCall16 call = reinterpret_cast<CuteQQuickTumblerCall16>(taken[16]);
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
      CuteQQuickTumblerCall17 call = reinterpret_cast<CuteQQuickTumblerCall17>(taken[17]);
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
      CuteQQuickTumblerCall18 call = reinterpret_cast<CuteQQuickTumblerCall18>(taken[18]);
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
      CuteQQuickTumblerCall19 call = reinterpret_cast<CuteQQuickTumblerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTumblerCall20 call = reinterpret_cast<CuteQQuickTumblerCall20>(taken[20]);
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
      CuteQQuickTumblerCall21 call = reinterpret_cast<CuteQQuickTumblerCall21>(taken[21]);
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
      CuteQQuickTumblerCall22 call = reinterpret_cast<CuteQQuickTumblerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTumblerCall23 call = reinterpret_cast<CuteQQuickTumblerCall23>(taken[23]);
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
      CuteQQuickTumblerCall24 call = reinterpret_cast<CuteQQuickTumblerCall24>(taken[24]);
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
      CuteQQuickTumblerCall25 call = reinterpret_cast<CuteQQuickTumblerCall25>(taken[25]);
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
      CuteQQuickTumblerCall26 call = reinterpret_cast<CuteQQuickTumblerCall26>(taken[26]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTumblerCall27 call = reinterpret_cast<CuteQQuickTumblerCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControl::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTumblerCall28 call = reinterpret_cast<CuteQQuickTumblerCall28>(taken[28]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControl::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTumblerCall29 call = reinterpret_cast<CuteQQuickTumblerCall29>(taken[29]);
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
      CuteQQuickTumblerCall30 call = reinterpret_cast<CuteQQuickTumblerCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTumblerCall31 call = reinterpret_cast<CuteQQuickTumblerCall31>(taken[31]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTumblerCall32 call = reinterpret_cast<CuteQQuickTumblerCall32>(taken[32]);
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
      CuteQQuickTumblerCall33 call = reinterpret_cast<CuteQQuickTumblerCall33>(taken[33]);
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
      CuteQQuickTumblerCall34 call = reinterpret_cast<CuteQQuickTumblerCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTumblerCall35 call = reinterpret_cast<CuteQQuickTumblerCall35>(taken[35]);
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
      CuteQQuickTumblerCall36 call = reinterpret_cast<CuteQQuickTumblerCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTumblerCall37 call = reinterpret_cast<CuteQQuickTumblerCall37>(taken[37]);
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
      CuteQQuickTumblerCall38 call = reinterpret_cast<CuteQQuickTumblerCall38>(taken[38]);
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
      CuteQQuickTumblerCall39 call = reinterpret_cast<CuteQQuickTumblerCall39>(taken[39]);
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
      CuteQQuickTumblerCall40 call = reinterpret_cast<CuteQQuickTumblerCall40>(taken[40]);
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
      CuteQQuickTumblerCall41 call = reinterpret_cast<CuteQQuickTumblerCall41>(taken[41]);
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
      CuteQQuickTumblerCall42 call = reinterpret_cast<CuteQQuickTumblerCall42>(taken[42]);
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
      CuteQQuickTumblerCall43 call = reinterpret_cast<CuteQQuickTumblerCall43>(taken[43]);
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
      CuteQQuickTumblerCall44 call = reinterpret_cast<CuteQQuickTumblerCall44>(taken[44]);
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
      CuteQQuickTumblerCall45 call = reinterpret_cast<CuteQQuickTumblerCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickTumblerCall46 call = reinterpret_cast<CuteQQuickTumblerCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickTumblerCall47 call = reinterpret_cast<CuteQQuickTumblerCall47>(taken[47]);
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
      CuteQQuickTumblerCall48 call = reinterpret_cast<CuteQQuickTumblerCall48>(taken[48]);
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
      CuteQQuickTumblerCall49 call = reinterpret_cast<CuteQQuickTumblerCall49>(taken[49]);
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
      CuteQQuickTumblerCall50 call = reinterpret_cast<CuteQQuickTumblerCall50>(taken[50]);
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
      CuteQQuickTumblerCall51 call = reinterpret_cast<CuteQQuickTumblerCall51>(taken[51]);
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
      CuteQQuickTumblerCall52 call = reinterpret_cast<CuteQQuickTumblerCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTumbler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickTumbler10metaObjectEv(
    const QQuickTumbler *self) {
  return self->metaObject();
}

//  void *QQuickTumbler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuickTumbler11qt_metacastEPKc(
    QQuickTumbler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTumbler::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuickTumbler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTumbler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTumbler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickTumbler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTumbler::tr(s, c, n));
}

//  void QQuickTumbler::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler21qt_qmlMarker_attachedEv(QQuickTumbler *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickTumbler::QQuickTumbler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTumbler *ritual_ZN13QQuickTumblerC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickTumbler(parent);
}

//  QQuickTumbler::~QQuickTumbler()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumblerD1Ev(QQuickTumbler *self) {
  delete self;
}

//  QVariant QQuickTumbler::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QQuickTumbler5modelEv(const QQuickTumbler *self) {
  return new QVariant(self->model());
}

//  void QQuickTumbler::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler8setModelERK8QVariant(
    QQuickTumbler *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  int QQuickTumbler::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickTumbler5countEv(const QQuickTumbler *self) {
  return self->count();
}

//  int QQuickTumbler::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickTumbler12currentIndexEv(const QQuickTumbler *self) {
  return self->currentIndex();
}

//  void QQuickTumbler::setCurrentIndex(int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler15setCurrentIndexEi(
    QQuickTumbler *self,
    int currentIndex) {
  self->setCurrentIndex(currentIndex);
}

//  QQuickItem *QQuickTumbler::currentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK13QQuickTumbler11currentItemEv(
    const QQuickTumbler *self) {
  return self->currentItem();
}

//  QQmlComponent *QQuickTumbler::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickTumbler8delegateEv(
    const QQuickTumbler *self) {
  return self->delegate();
}

//  void QQuickTumbler::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler11setDelegateEP13QQmlComponent(
    QQuickTumbler *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  int QQuickTumbler::visibleItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickTumbler16visibleItemCountEv(
    const QQuickTumbler *self) {
  return self->visibleItemCount();
}

//  void QQuickTumbler::setVisibleItemCount(int visibleItemCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler19setVisibleItemCountEi(
    QQuickTumbler *self,
    int visibleItemCount) {
  self->setVisibleItemCount(visibleItemCount);
}

//  QQuickTumblerAttached *QQuickTumbler::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickTumblerAttached *ritual_ZN13QQuickTumbler21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickTumbler::qmlAttachedProperties(object);
}

//  bool QQuickTumbler::wrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickTumbler4wrapEv(const QQuickTumbler *self) {
  return self->wrap();
}

//  void QQuickTumbler::setWrap(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler7setWrapEb(QQuickTumbler *self, bool wrap) {
  self->setWrap(wrap);
}

//  void QQuickTumbler::resetWrap()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler9resetWrapEv(QQuickTumbler *self) {
  self->resetWrap();
}

//  bool QQuickTumbler::isMoving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickTumbler8isMovingEv(const QQuickTumbler *self) {
  return self->isMoving();
}

//  void QQuickTumbler::positionViewAtIndex(int index, PositionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler19positionViewAtIndexEiNS_12PositionModeE(
    QQuickTumbler *self,
    int index,
    QQuickTumbler::PositionMode mode) {
  self->positionViewAtIndex(index, mode);
}

//  qreal QQuickTumbler::flickDeceleration() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickTumbler17flickDecelerationEv(
    const QQuickTumbler *self) {
  return self->flickDeceleration();
}

//  void QQuickTumbler::setFlickDeceleration(qreal newFlickDeceleration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler20setFlickDecelerationEd(
    QQuickTumbler *self,
    qreal newFlickDeceleration) {
  self->setFlickDeceleration(newFlickDeceleration);
}

//  void QQuickTumbler::resetFlickDeceleration()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler22resetFlickDecelerationEv(
    QQuickTumbler *self) {
  self->resetFlickDeceleration();
}

//  void QQuickTumbler::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler12modelChangedEv(QQuickTumbler *self) {
  self->modelChanged();
}

//  void QQuickTumbler::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler12countChangedEv(QQuickTumbler *self) {
  self->countChanged();
}

//  void QQuickTumbler::currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler19currentIndexChangedEv(QQuickTumbler *self) {
  self->currentIndexChanged();
}

//  void QQuickTumbler::currentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler18currentItemChangedEv(QQuickTumbler *self) {
  self->currentItemChanged();
}

//  void QQuickTumbler::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler15delegateChangedEv(QQuickTumbler *self) {
  self->delegateChanged();
}

//  void QQuickTumbler::visibleItemCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler23visibleItemCountChangedEv(
    QQuickTumbler *self) {
  self->visibleItemCountChanged();
}

//  void QQuickTumbler::wrapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler11wrapChangedEv(QQuickTumbler *self) {
  self->wrapChanged();
}

//  void QQuickTumbler::movingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler13movingChangedEv(QQuickTumbler *self) {
  self->movingChanged();
}

//  void QQuickTumbler::flickDecelerationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler24flickDecelerationChangedEv(
    QQuickTumbler *self) {
  self->flickDecelerationChanged();
}

//  void QQuickTumbler::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler14geometryChangeERK6QRectFS2_(
    QQuickTumbler *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTumbler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler17componentCompleteEv(QQuickTumbler *self) {
  self->componentComplete();
}

//  void QQuickTumbler::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler17contentItemChangeEP10QQuickItemS1_(
    QQuickTumbler *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickTumbler::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler13keyPressEventEP9QKeyEvent(
    QQuickTumbler *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickTumbler::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickTumbler12updatePolishEv(QQuickTumbler *self) {
  self->updatePolish();
}

//  QFont QQuickTumbler::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickTumbler11defaultFontEv(const QQuickTumbler *self) {
  return new QFont(self->defaultFont());
}

//  QQuickTumblerPrivate *QQuickTumbler::d_func()
extern "C" Q_DECL_EXPORT
QQuickTumblerPrivate *ritual_ZN13QQuickTumbler6d_funcEv(
    QQuickTumbler *self) {
  return self->d_func();
}

//  const QQuickTumblerPrivate *QQuickTumbler::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTumblerPrivate *ritual_ZNK13QQuickTumbler6d_funcEv(
    const QQuickTumbler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickTumbler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTumbler(
    QQuickTumbler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTumbler *>(self)->take(key, call);
}

//  void QQuickTumbler::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickTumbler14geometryChangeERK6QRectFS2_(
    QQuickTumbler *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTumbler *>(self)->OwnQQuickTumbler::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTumbler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickTumbler17componentCompleteEv(QQuickTumbler *self) {
  static_cast<OwnQQuickTumbler *>(self)->OwnQQuickTumbler::componentComplete();
}

//  void QQuickTumbler::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickTumbler17contentItemChangeEP10QQuickItemS1_(
    QQuickTumbler *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickTumbler *>(self)->OwnQQuickTumbler::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickTumbler::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickTumbler13keyPressEventEP9QKeyEvent(
    QQuickTumbler *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickTumbler *>(self)->OwnQQuickTumbler::keyPressEvent(
      event);
}

//  void QQuickTumbler::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickTumbler12updatePolishEv(QQuickTumbler *self) {
  static_cast<OwnQQuickTumbler *>(self)->OwnQQuickTumbler::updatePolish();
}

//  QFont QQuickTumbler::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickTumbler11defaultFontEv(
    const QQuickTumbler *self) {
  return new QFont(
      static_cast<const OwnQQuickTumbler *>(self)->OwnQQuickTumbler::defaultFont());
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
