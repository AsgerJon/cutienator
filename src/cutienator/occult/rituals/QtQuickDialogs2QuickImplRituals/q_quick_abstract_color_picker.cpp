//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpic
//  ker_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAbstractColorPicker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAbstractColorPicker : QQuickAbstractColorPicker {
  using QQuickAbstractColorPicker::componentComplete;
};

//  A QQuickAbstractColorPicker that Python can take functions over in. Every QQuickAbstractColorPicker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QColor * (*CuteQQuickAbstractColorPickerCall0)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall1)(const void *, int *);
typedef const QFont * (*CuteQQuickAbstractColorPickerCall2)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall3)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall5)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall6)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall7)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall8)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall9)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall13)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractColorPickerCall14)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickAbstractColorPickerCall15)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAbstractColorPickerCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickAbstractColorPickerCall17)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall18)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall19)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickAbstractColorPickerCall20)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall21)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickAbstractColorPickerCall22)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall23)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall24)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall25)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall26)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickAbstractColorPickerCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickAbstractColorPickerCall28)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickAbstractColorPickerCall29)(const void *, int *);
typedef const QRectF * (*CuteQQuickAbstractColorPickerCall30)(const void *, int *);
typedef bool (*CuteQQuickAbstractColorPickerCall31)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickAbstractColorPickerCall32)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickAbstractColorPickerCall33)(const void *, int *);
typedef void * (*CuteQQuickAbstractColorPickerCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractColorPickerCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall36)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickAbstractColorPickerCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickAbstractColorPickerCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractColorPickerCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractColorPickerCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractColorPickerCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickAbstractColorPickerCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickAbstractColorPickerCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickAbstractColorPickerCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall46)(const void *, int *);
typedef void (*CuteQQuickAbstractColorPickerCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractColorPickerCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractColorPickerCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAbstractColorPicker : public QQuickAbstractColorPicker {
public:
  using QQuickAbstractColorPicker::QQuickAbstractColorPicker;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QQuickAbstractColorPicker7colorAtERK7QPointF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
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
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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

  //  QColor QQuickAbstractColorPicker::colorAt(const QPointF &pos)
  QColor colorAt(const QPointF &pos) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall0 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall0>(taken[0]);
      const QColor * given = call(this, &pos, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QQuickAbstractColorPicker::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall1 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractColorPicker::componentComplete();
  }

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall2 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall2>(taken[2]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall3 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall4 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall4>(taken[4]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickControl::itemChange(change, value);
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall5 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall6 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall7 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall8 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall9 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall10 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall11 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall12 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall13 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall14 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall15 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall16 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall17 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall17>(taken[17]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall18 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall18>(taken[18]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall19 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall20 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall21 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall22 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall22>(taken[22]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall23 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall24 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall24>(taken[24]);
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
      CuteQQuickAbstractColorPickerCall25 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall25>(taken[25]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall26 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControl::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall27 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControl::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall28 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall28>(taken[28]);
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
      CuteQQuickAbstractColorPickerCall29 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall29>(taken[29]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall30 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall31 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall31>(taken[31]);
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
      CuteQQuickAbstractColorPickerCall32 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall32>(taken[32]);
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
      CuteQQuickAbstractColorPickerCall33 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall34 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall34>(taken[34]);
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
      CuteQQuickAbstractColorPickerCall35 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall35>(taken[35]);
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
      CuteQQuickAbstractColorPickerCall36 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall37 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall37>(taken[37]);
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
      CuteQQuickAbstractColorPickerCall38 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall38>(taken[38]);
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
      CuteQQuickAbstractColorPickerCall39 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall39>(taken[39]);
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
      CuteQQuickAbstractColorPickerCall40 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall40>(taken[40]);
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
      CuteQQuickAbstractColorPickerCall41 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall41>(taken[41]);
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
      CuteQQuickAbstractColorPickerCall42 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall42>(taken[42]);
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
      CuteQQuickAbstractColorPickerCall43 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall43>(taken[43]);
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
      CuteQQuickAbstractColorPickerCall44 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall44>(taken[44]);
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
      CuteQQuickAbstractColorPickerCall45 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall46 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickAbstractColorPickerCall47 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall47>(taken[47]);
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
      CuteQQuickAbstractColorPickerCall48 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall48>(taken[48]);
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
      CuteQQuickAbstractColorPickerCall49 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall49>(taken[49]);
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
      CuteQQuickAbstractColorPickerCall50 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall50>(taken[50]);
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
      CuteQQuickAbstractColorPickerCall51 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall51>(taken[51]);
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
      CuteQQuickAbstractColorPickerCall52 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall52>(taken[52]);
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
      CuteQQuickAbstractColorPickerCall53 call = reinterpret_cast<CuteQQuickAbstractColorPickerCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAbstractColorPicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickAbstractColorPicker10metaObjectEv(
    const QQuickAbstractColorPicker *self) {
  return self->metaObject();
}

//  QString QQuickAbstractColorPicker::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickAbstractColorPicker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAbstractColorPicker::tr(s, c, n));
}

//  void QQuickAbstractColorPicker::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker24qt_qmlMarker_uncreatableEv(
    QQuickAbstractColorPicker *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickAbstractColorPicker::~QQuickAbstractColorPicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPickerD1Ev(
    QQuickAbstractColorPicker *self) {
  delete self;
}

//  QColor QQuickAbstractColorPicker::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickAbstractColorPicker5colorEv(
    const QQuickAbstractColorPicker *self) {
  return new QColor(self->color());
}

//  void QQuickAbstractColorPicker::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker8setColorERK6QColor(
    QQuickAbstractColorPicker *self,
    const QColor *c) {
  self->setColor(*c);
}

//  qreal QQuickAbstractColorPicker::hue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker3hueEv(
    const QQuickAbstractColorPicker *self) {
  return self->hue();
}

//  void QQuickAbstractColorPicker::setHue(qreal hue)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker6setHueEd(
    QQuickAbstractColorPicker *self,
    qreal hue) {
  self->setHue(hue);
}

//  qreal QQuickAbstractColorPicker::saturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker10saturationEv(
    const QQuickAbstractColorPicker *self) {
  return self->saturation();
}

//  void QQuickAbstractColorPicker::setSaturation(qreal saturation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker13setSaturationEd(
    QQuickAbstractColorPicker *self,
    qreal saturation) {
  self->setSaturation(saturation);
}

//  qreal QQuickAbstractColorPicker::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker5valueEv(
    const QQuickAbstractColorPicker *self) {
  return self->value();
}

//  void QQuickAbstractColorPicker::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker8setValueEd(
    QQuickAbstractColorPicker *self,
    qreal value) {
  self->setValue(value);
}

//  qreal QQuickAbstractColorPicker::lightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker9lightnessEv(
    const QQuickAbstractColorPicker *self) {
  return self->lightness();
}

//  void QQuickAbstractColorPicker::setLightness(qreal lightness)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker12setLightnessEd(
    QQuickAbstractColorPicker *self,
    qreal lightness) {
  self->setLightness(lightness);
}

//  qreal QQuickAbstractColorPicker::alpha() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker5alphaEv(
    const QQuickAbstractColorPicker *self) {
  return self->alpha();
}

//  void QQuickAbstractColorPicker::setAlpha(qreal alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker8setAlphaEd(
    QQuickAbstractColorPicker *self,
    qreal alpha) {
  self->setAlpha(alpha);
}

//  bool QQuickAbstractColorPicker::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickAbstractColorPicker9isPressedEv(
    const QQuickAbstractColorPicker *self) {
  return self->isPressed();
}

//  void QQuickAbstractColorPicker::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker10setPressedEb(
    QQuickAbstractColorPicker *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  QQuickItem *QQuickAbstractColorPicker::handle() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK25QQuickAbstractColorPicker6handleEv(
    const QQuickAbstractColorPicker *self) {
  return self->handle();
}

//  void QQuickAbstractColorPicker::setHandle(QQuickItem *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker9setHandleEP10QQuickItem(
    QQuickAbstractColorPicker *self,
    QQuickItem *handle) {
  self->setHandle(handle);
}

//  qreal QQuickAbstractColorPicker::implicitHandleWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker19implicitHandleWidthEv(
    const QQuickAbstractColorPicker *self) {
  return self->implicitHandleWidth();
}

//  qreal QQuickAbstractColorPicker::implicitHandleHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAbstractColorPicker20implicitHandleHeightEv(
    const QQuickAbstractColorPicker *self) {
  return self->implicitHandleHeight();
}

//  QColor QQuickAbstractColorPicker::colorAt(const QPointF &pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN25QQuickAbstractColorPicker7colorAtERK7QPointF(
    QQuickAbstractColorPicker *self,
    const QPointF *pos) {
  return new QColor(self->colorAt(*pos));
}

//  void QQuickAbstractColorPicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker17componentCompleteEv(
    QQuickAbstractColorPicker *self) {
  self->componentComplete();
}

//  void QQuickAbstractColorPicker::updateColor(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAbstractColorPicker11updateColorERK7QPointF(
    QQuickAbstractColorPicker *self,
    const QPointF *pos) {
  self->updateColor(*pos);
}

//  QQuickAbstractColorPickerPrivate *QQuickAbstractColorPicker::d_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractColorPickerPrivate *ritual_ZN25QQuickAbstractColorPicker6d_funcEv(
    QQuickAbstractColorPicker *self) {
  return self->d_func();
}

//  const QQuickAbstractColorPickerPrivate
//      *QQuickAbstractColorPicker::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAbstractColorPickerPrivate *ritual_ZNK25QQuickAbstractColorPicker6d_funcEv(
    const QQuickAbstractColorPicker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAbstractColorPicker, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractColorPicker(
    QQuickAbstractColorPicker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractColorPicker *>(self)->take(key, call);
}

//  void QQuickAbstractColorPicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickAbstractColorPicker17componentCompleteEv(
    QQuickAbstractColorPicker *self) {
  static_cast<OwnQQuickAbstractColorPicker *>(self)->OwnQQuickAbstractColorPicker::componentComplete();
}
