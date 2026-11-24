//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickMenuBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenuBar : QQuickMenuBar {
  using QQuickMenuBar::eventFilter;
  using QQuickMenuBar::keyPressEvent;
  using QQuickMenuBar::keyReleaseEvent;
  using QQuickMenuBar::hoverLeaveEvent;
  using QQuickMenuBar::isContent;
  using QQuickMenuBar::itemChange;
  using QQuickMenuBar::itemAdded;
  using QQuickMenuBar::itemMoved;
  using QQuickMenuBar::itemRemoved;
  using QQuickMenuBar::componentComplete;
  using QQuickMenuBar::defaultFont;
  using QQuickMenuBar::accessibleRole;
};

//  A QQuickMenuBar that Python can take functions over in. Every QQuickMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickMenuBarCall0)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall1)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall2)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall3)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickMenuBarCall4)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall6)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall7)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall8)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall9)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef const QFont * (*CuteQQuickMenuBarCall10)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef int (*CuteQQuickMenuBarCall11)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall12)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickMenuBarCall13)(const void *, int *);
typedef void (*CuteQQuickMenuBarCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMenuBarCall15)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickMenuBarCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickMenuBarCall17)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickMenuBarCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuBarCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuBarCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuBarCall21)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickMenuBarCall22)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickMenuBarCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMenuBarCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMenuBarCall25)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickMenuBarCall26)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickMenuBarCall27)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickMenuBarCall28)(const void *, int *);
typedef void (*CuteQQuickMenuBarCall29)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickMenuBarCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickMenuBarCall31)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickMenuBarCall32)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickMenuBarCall33)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickMenuBarCall34)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickMenuBarCall35)(const void *, int *);
typedef const QRectF * (*CuteQQuickMenuBarCall36)(const void *, int *);
typedef bool (*CuteQQuickMenuBarCall37)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickMenuBarCall38)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickMenuBarCall39)(const void *, int *);
typedef void * (*CuteQQuickMenuBarCall40)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMenuBarCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef void (*CuteQQuickMenuBarCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickMenuBarCall43)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuBarCall44)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuBarCall45)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuBarCall46)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuBarCall47)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickMenuBarCall48)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickMenuBarCall49)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickMenuBarCall50)(const void *, int *);
typedef void (*CuteQQuickMenuBarCall51)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuBarCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuBarCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuBarCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuBarCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuBarCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMenuBar : public QQuickMenuBar {
public:
  using QQuickMenuBar::QQuickMenuBar;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
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
    if (!std::strcmp(key, "_ZNK15QQuickContainer9isContentEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
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
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[33] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[37] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[40] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[51] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickMenuBar::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuBarCall0 call = reinterpret_cast<CuteQQuickMenuBarCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickMenuBar::eventFilter(object, event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuBarCall1 call = reinterpret_cast<CuteQQuickMenuBarCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMenuBar::keyPressEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuBarCall2 call = reinterpret_cast<CuteQQuickMenuBarCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMenuBar::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuBarCall3 call = reinterpret_cast<CuteQQuickMenuBarCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMenuBar::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickMenuBar::isContent(QQuickItem *item) const
  bool isContent(QQuickItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuBarCall4 call = reinterpret_cast<CuteQQuickMenuBarCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickMenuBar::isContent(item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::itemChange(QQuickItem::ItemChange change, const
  //      QQuickItem::ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMenuBarCall5 call = reinterpret_cast<CuteQQuickMenuBarCall5>(taken[5]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickMenuBar::itemChange(change, value);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::itemAdded(int index, QQuickItem *item)
  void itemAdded(int index, QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMenuBarCall6 call = reinterpret_cast<CuteQQuickMenuBarCall6>(taken[6]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickMenuBar::itemAdded(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::itemMoved(int index, QQuickItem *item)
  void itemMoved(int index, QQuickItem *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuBarCall7 call = reinterpret_cast<CuteQQuickMenuBarCall7>(taken[7]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickMenuBar::itemMoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::itemRemoved(int index, QQuickItem *item)
  void itemRemoved(int index, QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMenuBarCall8 call = reinterpret_cast<CuteQQuickMenuBarCall8>(taken[8]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickMenuBar::itemRemoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickMenuBar::componentComplete()
  void componentComplete() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMenuBarCall9 call = reinterpret_cast<CuteQQuickMenuBarCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuBar::componentComplete();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  QFont QQuickMenuBar::defaultFont() const
  QFont defaultFont() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuBarCall10 call = reinterpret_cast<CuteQQuickMenuBarCall10>(taken[10]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickMenuBar::defaultFont();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
  //  QAccessible::Role QQuickMenuBar::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMenuBarCall11 call = reinterpret_cast<CuteQQuickMenuBarCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickMenuBar::accessibleRole();
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMenuBarCall12 call = reinterpret_cast<CuteQQuickMenuBarCall12>(taken[12]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickContainer::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMenuBarCall13 call = reinterpret_cast<CuteQQuickMenuBarCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMenuBarCall14 call = reinterpret_cast<CuteQQuickMenuBarCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuBarCall15 call = reinterpret_cast<CuteQQuickMenuBarCall15>(taken[15]);
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
      CuteQQuickMenuBarCall16 call = reinterpret_cast<CuteQQuickMenuBarCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMenuBarCall17 call = reinterpret_cast<CuteQQuickMenuBarCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMenuBarCall18 call = reinterpret_cast<CuteQQuickMenuBarCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuBarCall19 call = reinterpret_cast<CuteQQuickMenuBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuBarCall20 call = reinterpret_cast<CuteQQuickMenuBarCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuBarCall21 call = reinterpret_cast<CuteQQuickMenuBarCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMenuBarCall22 call = reinterpret_cast<CuteQQuickMenuBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMenuBarCall23 call = reinterpret_cast<CuteQQuickMenuBarCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickControl::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMenuBarCall24 call = reinterpret_cast<CuteQQuickMenuBarCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMenuBarCall25 call = reinterpret_cast<CuteQQuickMenuBarCall25>(taken[25]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMenuBarCall26 call = reinterpret_cast<CuteQQuickMenuBarCall26>(taken[26]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMenuBarCall27 call = reinterpret_cast<CuteQQuickMenuBarCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMenuBarCall28 call = reinterpret_cast<CuteQQuickMenuBarCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMenuBarCall29 call = reinterpret_cast<CuteQQuickMenuBarCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickMenuBarCall30 call = reinterpret_cast<CuteQQuickMenuBarCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQQuickMenuBarCall31 call = reinterpret_cast<CuteQQuickMenuBarCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQQuickMenuBarCall32 call = reinterpret_cast<CuteQQuickMenuBarCall32>(taken[32]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMenuBarCall33 call = reinterpret_cast<CuteQQuickMenuBarCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMenuBarCall34 call = reinterpret_cast<CuteQQuickMenuBarCall34>(taken[34]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickMenuBarCall35 call = reinterpret_cast<CuteQQuickMenuBarCall35>(taken[35]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickMenuBarCall36 call = reinterpret_cast<CuteQQuickMenuBarCall36>(taken[36]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickMenuBarCall37 call = reinterpret_cast<CuteQQuickMenuBarCall37>(taken[37]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickMenuBarCall38 call = reinterpret_cast<CuteQQuickMenuBarCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickMenuBarCall39 call = reinterpret_cast<CuteQQuickMenuBarCall39>(taken[39]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickMenuBarCall40 call = reinterpret_cast<CuteQQuickMenuBarCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickMenuBarCall41 call = reinterpret_cast<CuteQQuickMenuBarCall41>(taken[41]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickMenuBarCall42 call = reinterpret_cast<CuteQQuickMenuBarCall42>(taken[42]);
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
      CuteQQuickMenuBarCall43 call = reinterpret_cast<CuteQQuickMenuBarCall43>(taken[43]);
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
      CuteQQuickMenuBarCall44 call = reinterpret_cast<CuteQQuickMenuBarCall44>(taken[44]);
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
      CuteQQuickMenuBarCall45 call = reinterpret_cast<CuteQQuickMenuBarCall45>(taken[45]);
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
      CuteQQuickMenuBarCall46 call = reinterpret_cast<CuteQQuickMenuBarCall46>(taken[46]);
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
      CuteQQuickMenuBarCall47 call = reinterpret_cast<CuteQQuickMenuBarCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickMenuBarCall48 call = reinterpret_cast<CuteQQuickMenuBarCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteQQuickMenuBarCall49 call = reinterpret_cast<CuteQQuickMenuBarCall49>(taken[49]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickMenuBarCall50 call = reinterpret_cast<CuteQQuickMenuBarCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickMenuBarCall51 call = reinterpret_cast<CuteQQuickMenuBarCall51>(taken[51]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickMenuBarCall52 call = reinterpret_cast<CuteQQuickMenuBarCall52>(taken[52]);
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
      CuteQQuickMenuBarCall53 call = reinterpret_cast<CuteQQuickMenuBarCall53>(taken[53]);
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
      CuteQQuickMenuBarCall54 call = reinterpret_cast<CuteQQuickMenuBarCall54>(taken[54]);
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
      CuteQQuickMenuBarCall55 call = reinterpret_cast<CuteQQuickMenuBarCall55>(taken[55]);
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
      CuteQQuickMenuBarCall56 call = reinterpret_cast<CuteQQuickMenuBarCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickMenuBar10metaObjectEv(
    const QQuickMenuBar *self) {
  return self->metaObject();
}

//  QString QQuickMenuBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickMenuBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMenuBar::tr(s, c, n));
}

//  QQuickMenuBar::QQuickMenuBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMenuBar *ritual_ZN13QQuickMenuBarC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickMenuBar(parent);
}

//  QQuickMenuBar::~QQuickMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBarD1Ev(QQuickMenuBar *self) {
  delete self;
}

//  QQmlComponent *QQuickMenuBar::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickMenuBar8delegateEv(
    const QQuickMenuBar *self) {
  return self->delegate();
}

//  void QQuickMenuBar::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar11setDelegateEP13QQmlComponent(
    QQuickMenuBar *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QQuickMenu *QQuickMenuBar::menuAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK13QQuickMenuBar6menuAtEi(
    const QQuickMenuBar *self,
    int index) {
  return self->menuAt(index);
}

//  void QQuickMenuBar::addMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar7addMenuEP10QQuickMenu(
    QQuickMenuBar *self,
    QQuickMenu *menu) {
  self->addMenu(menu);
}

//  void QQuickMenuBar::insertMenu(int index, QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar10insertMenuEiP10QQuickMenu(
    QQuickMenuBar *self,
    int index,
    QQuickMenu *menu) {
  self->insertMenu(index, menu);
}

//  void QQuickMenuBar::removeMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar10removeMenuEP10QQuickMenu(
    QQuickMenuBar *self,
    QQuickMenu *menu) {
  self->removeMenu(menu);
}

//  QQuickMenu *QQuickMenuBar::takeMenu(int index)
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN13QQuickMenuBar8takeMenuEi(
    QQuickMenuBar *self,
    int index) {
  return self->takeMenu(index);
}

//  bool QQuickMenuBar::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQuickMenuBar11eventFilterEP7QObjectP6QEvent(
    QQuickMenuBar *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QQuickMenuBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar13keyPressEventEP9QKeyEvent(
    QQuickMenuBar *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickMenuBar::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar15keyReleaseEventEP9QKeyEvent(
    QQuickMenuBar *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickMenuBar::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar15hoverLeaveEventEP11QHoverEvent(
    QQuickMenuBar *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  bool QQuickMenuBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickMenuBar9isContentEP10QQuickItem(
    const QQuickMenuBar *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  void QQuickMenuBar::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMenuBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickMenuBar::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar9itemAddedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickMenuBar::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar9itemMovedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  self->itemMoved(index, item);
}

//  void QQuickMenuBar::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar11itemRemovedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

//  void QQuickMenuBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickMenuBar17componentCompleteEv(QQuickMenuBar *self) {
  self->componentComplete();
}

//  QFont QQuickMenuBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickMenuBar11defaultFontEv(const QQuickMenuBar *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK13QQuickMenuBar14accessibleRoleEv(
    const QQuickMenuBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickMenuBarPrivate *QQuickMenuBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickMenuBarPrivate *ritual_ZN13QQuickMenuBar6d_funcEv(
    QQuickMenuBar *self) {
  return self->d_func();
}

//  const QQuickMenuBarPrivate *QQuickMenuBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuBarPrivate *ritual_ZNK13QQuickMenuBar6d_funcEv(
    const QQuickMenuBar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMenuBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenuBar(
    QQuickMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMenuBar *>(self)->take(key, call);
}

//  bool QQuickMenuBar::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QQuickMenuBar11eventFilterEP7QObjectP6QEvent(
    QQuickMenuBar *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::eventFilter(
      object,
      event);
}

//  void QQuickMenuBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar13keyPressEventEP9QKeyEvent(
    QQuickMenuBar *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::keyPressEvent(
      event);
}

//  void QQuickMenuBar::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar15keyReleaseEventEP9QKeyEvent(
    QQuickMenuBar *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::keyReleaseEvent(
      event);
}

//  void QQuickMenuBar::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar15hoverLeaveEventEP11QHoverEvent(
    QQuickMenuBar *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::hoverLeaveEvent(
      event);
}

//  bool QQuickMenuBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QQuickMenuBar9isContentEP10QQuickItem(
    const QQuickMenuBar *self,
    QQuickItem *item) {
  return static_cast<const OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::isContent(
      item);
}

//  void QQuickMenuBar::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMenuBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::itemChange(
      change,
      *value);
}

//  void QQuickMenuBar::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar9itemAddedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::itemAdded(
      index,
      item);
}

//  void QQuickMenuBar::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar9itemMovedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::itemMoved(
      index,
      item);
}

//  void QQuickMenuBar::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar11itemRemovedEiP10QQuickItem(
    QQuickMenuBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::itemRemoved(
      index,
      item);
}

//  void QQuickMenuBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickMenuBar17componentCompleteEv(QQuickMenuBar *self) {
  static_cast<OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::componentComplete();
}

//  QFont QQuickMenuBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickMenuBar11defaultFontEv(
    const QQuickMenuBar *self) {
  return new QFont(
      static_cast<const OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK13QQuickMenuBar14accessibleRoleEv(
    const QQuickMenuBar *self) {
  return static_cast<const OwnQQuickMenuBar *>(self)->OwnQQuickMenuBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
