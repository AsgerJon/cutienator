//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickSideBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSideBar : QQuickSideBar {
  using QQuickSideBar::componentComplete;
};

//  A QQuickSideBar that Python can take functions over in. Every QQuickSideBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSideBarCall0)(const void *, int *);
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSideBarCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSideBarCall2)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickSideBarCall3)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSideBarCall4)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSideBarCall5)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickSideBarCall6)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
typedef const QFont * (*CuteQQuickSideBarCall7)(const void *, int *);
typedef void (*CuteQQuickSideBarCall8)(const void *, int *);
typedef void (*CuteQQuickSideBarCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSideBarCall10)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall13)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSideBarCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSideBarCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSideBarCall17)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSideBarCall18)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSideBarCall19)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSideBarCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSideBarCall21)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickSideBarCall22)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSideBarCall24)(const void *, int *);
typedef void (*CuteQQuickSideBarCall25)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickSideBarCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSideBarCall27)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickSideBarCall28)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSideBarCall29)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSideBarCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSideBarCall31)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickSideBarCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickSideBarCall33)(const void *, int *);
typedef bool (*CuteQQuickSideBarCall34)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickSideBarCall35)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickSideBarCall36)(const void *, int *);
typedef void * (*CuteQQuickSideBarCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSideBarCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall39)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSideBarCall40)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickSideBarCall41)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickSideBarCall42)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSideBarCall43)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSideBarCall44)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSideBarCall45)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSideBarCall46)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickSideBarCall47)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickSideBarCall48)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickSideBarCall49)(const void *, int *);
typedef void (*CuteQQuickSideBarCall50)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSideBarCall51)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSideBarCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSideBar : public QQuickSideBar {
public:
  using QQuickSideBar::QQuickSideBar;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK15QQuickContainer9isContentEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemAddedEiP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemMovedEiP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer11itemRemovedEiP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[40] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[42] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
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

  //  void QQuickSideBar::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSideBarCall0 call = reinterpret_cast<CuteQQuickSideBarCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSideBar::componentComplete();
  }

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSideBarCall1 call = reinterpret_cast<CuteQQuickSideBarCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSideBarCall2 call = reinterpret_cast<CuteQQuickSideBarCall2>(taken[2]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickContainer::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickContainer::isContent(QQuickItem *item) const
  bool isContent(QQuickItem *item) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSideBarCall3 call = reinterpret_cast<CuteQQuickSideBarCall3>(taken[3]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickContainer::isContent(item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemAdded(int index, QQuickItem *item)
  void itemAdded(int index, QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSideBarCall4 call = reinterpret_cast<CuteQQuickSideBarCall4>(taken[4]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickContainer::itemAdded(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemMoved(int index, QQuickItem *item)
  void itemMoved(int index, QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSideBarCall5 call = reinterpret_cast<CuteQQuickSideBarCall5>(taken[5]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickContainer::itemMoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemRemoved(int index, QQuickItem *item)
  void itemRemoved(int index, QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSideBarCall6 call = reinterpret_cast<CuteQQuickSideBarCall6>(taken[6]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickContainer::itemRemoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSideBarCall7 call = reinterpret_cast<CuteQQuickSideBarCall7>(taken[7]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSideBarCall8 call = reinterpret_cast<CuteQQuickSideBarCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSideBarCall9 call = reinterpret_cast<CuteQQuickSideBarCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSideBarCall10 call = reinterpret_cast<CuteQQuickSideBarCall10>(taken[10]);
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
      CuteQQuickSideBarCall11 call = reinterpret_cast<CuteQQuickSideBarCall11>(taken[11]);
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
      CuteQQuickSideBarCall12 call = reinterpret_cast<CuteQQuickSideBarCall12>(taken[12]);
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
      CuteQQuickSideBarCall13 call = reinterpret_cast<CuteQQuickSideBarCall13>(taken[13]);
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
      CuteQQuickSideBarCall14 call = reinterpret_cast<CuteQQuickSideBarCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSideBarCall15 call = reinterpret_cast<CuteQQuickSideBarCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSideBarCall16 call = reinterpret_cast<CuteQQuickSideBarCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSideBarCall17 call = reinterpret_cast<CuteQQuickSideBarCall17>(taken[17]);
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
      CuteQQuickSideBarCall18 call = reinterpret_cast<CuteQQuickSideBarCall18>(taken[18]);
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
      CuteQQuickSideBarCall19 call = reinterpret_cast<CuteQQuickSideBarCall19>(taken[19]);
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
      CuteQQuickSideBarCall20 call = reinterpret_cast<CuteQQuickSideBarCall20>(taken[20]);
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
      CuteQQuickSideBarCall21 call = reinterpret_cast<CuteQQuickSideBarCall21>(taken[21]);
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
      CuteQQuickSideBarCall22 call = reinterpret_cast<CuteQQuickSideBarCall22>(taken[22]);
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
      CuteQQuickSideBarCall23 call = reinterpret_cast<CuteQQuickSideBarCall23>(taken[23]);
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
      CuteQQuickSideBarCall24 call = reinterpret_cast<CuteQQuickSideBarCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSideBarCall25 call = reinterpret_cast<CuteQQuickSideBarCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSideBarCall26 call = reinterpret_cast<CuteQQuickSideBarCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSideBarCall27 call = reinterpret_cast<CuteQQuickSideBarCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSideBarCall28 call = reinterpret_cast<CuteQQuickSideBarCall28>(taken[28]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSideBarCall29 call = reinterpret_cast<CuteQQuickSideBarCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControl::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSideBarCall30 call = reinterpret_cast<CuteQQuickSideBarCall30>(taken[30]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControl::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSideBarCall31 call = reinterpret_cast<CuteQQuickSideBarCall31>(taken[31]);
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
      CuteQQuickSideBarCall32 call = reinterpret_cast<CuteQQuickSideBarCall32>(taken[32]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSideBarCall33 call = reinterpret_cast<CuteQQuickSideBarCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSideBarCall34 call = reinterpret_cast<CuteQQuickSideBarCall34>(taken[34]);
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
      CuteQQuickSideBarCall35 call = reinterpret_cast<CuteQQuickSideBarCall35>(taken[35]);
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
      CuteQQuickSideBarCall36 call = reinterpret_cast<CuteQQuickSideBarCall36>(taken[36]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickSideBarCall37 call = reinterpret_cast<CuteQQuickSideBarCall37>(taken[37]);
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
      CuteQQuickSideBarCall38 call = reinterpret_cast<CuteQQuickSideBarCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickSideBarCall39 call = reinterpret_cast<CuteQQuickSideBarCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickSideBarCall40 call = reinterpret_cast<CuteQQuickSideBarCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickSideBarCall41 call = reinterpret_cast<CuteQQuickSideBarCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickSideBarCall42 call = reinterpret_cast<CuteQQuickSideBarCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickSideBarCall43 call = reinterpret_cast<CuteQQuickSideBarCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickSideBarCall44 call = reinterpret_cast<CuteQQuickSideBarCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickSideBarCall45 call = reinterpret_cast<CuteQQuickSideBarCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickSideBarCall46 call = reinterpret_cast<CuteQQuickSideBarCall46>(taken[46]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickSideBarCall47 call = reinterpret_cast<CuteQQuickSideBarCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQQuickSideBarCall48 call = reinterpret_cast<CuteQQuickSideBarCall48>(taken[48]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickSideBarCall49 call = reinterpret_cast<CuteQQuickSideBarCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickSideBarCall50 call = reinterpret_cast<CuteQQuickSideBarCall50>(taken[50]);
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
      CuteQQuickSideBarCall51 call = reinterpret_cast<CuteQQuickSideBarCall51>(taken[51]);
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
      CuteQQuickSideBarCall52 call = reinterpret_cast<CuteQQuickSideBarCall52>(taken[52]);
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
      CuteQQuickSideBarCall53 call = reinterpret_cast<CuteQQuickSideBarCall53>(taken[53]);
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
      CuteQQuickSideBarCall54 call = reinterpret_cast<CuteQQuickSideBarCall54>(taken[54]);
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
      CuteQQuickSideBarCall55 call = reinterpret_cast<CuteQQuickSideBarCall55>(taken[55]);
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
      CuteQQuickSideBarCall56 call = reinterpret_cast<CuteQQuickSideBarCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSideBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickSideBar10metaObjectEv(
    const QQuickSideBar *self) {
  return self->metaObject();
}

//  QString QQuickSideBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickSideBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSideBar::tr(s, c, n));
}

//  QQuickSideBar::QQuickSideBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSideBar *ritual_ZN13QQuickSideBarC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickSideBar(parent);
}

//  QQuickSideBar::~QQuickSideBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBarD1Ev(QQuickSideBar *self) {
  delete self;
}

//  QQuickDialog *QQuickSideBar::dialog() const
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZNK13QQuickSideBar6dialogEv(const QQuickSideBar *self) {
  return self->dialog();
}

//  void QQuickSideBar::setDialog(QQuickDialog *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar9setDialogEP12QQuickDialog(
    QQuickSideBar *self,
    QQuickDialog *dialog) {
  self->setDialog(dialog);
}

//  QList<QUrl> QQuickSideBar::favoritePaths() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK13QQuickSideBar13favoritePathsEv(
    const QQuickSideBar *self) {
  return new QList<QUrl>(self->favoritePaths());
}

//  QQmlComponent *QQuickSideBar::buttonDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickSideBar14buttonDelegateEv(
    const QQuickSideBar *self) {
  return self->buttonDelegate();
}

//  void QQuickSideBar::setButtonDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar17setButtonDelegateEP13QQmlComponent(
    QQuickSideBar *self,
    QQmlComponent *delegate) {
  self->setButtonDelegate(delegate);
}

//  QQmlComponent *QQuickSideBar::separatorDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickSideBar17separatorDelegateEv(
    const QQuickSideBar *self) {
  return self->separatorDelegate();
}

//  void QQuickSideBar::setSeparatorDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar20setSeparatorDelegateEP13QQmlComponent(
    QQuickSideBar *self,
    QQmlComponent *delegate) {
  self->setSeparatorDelegate(delegate);
}

//  QQmlComponent *QQuickSideBar::addFavoriteDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QQuickSideBar19addFavoriteDelegateEv(
    const QQuickSideBar *self) {
  return self->addFavoriteDelegate();
}

//  void QQuickSideBar::setAddFavoriteDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar22setAddFavoriteDelegateEP13QQmlComponent(
    QQuickSideBar *self,
    QQmlComponent *delegate) {
  self->setAddFavoriteDelegate(delegate);
}

//  void QQuickSideBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar17componentCompleteEv(QQuickSideBar *self) {
  self->componentComplete();
}

//  void QQuickSideBar::setFavoritePaths(const QList<QUrl> &favoritePaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickSideBar16setFavoritePathsERK5QListI4QUrlE(
    QQuickSideBar *self,
    const QList<QUrl> *favoritePaths) {
  self->setFavoritePaths(*favoritePaths);
}

//  QQuickSideBarPrivate *QQuickSideBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickSideBarPrivate *ritual_ZN13QQuickSideBar6d_funcEv(
    QQuickSideBar *self) {
  return self->d_func();
}

//  const QQuickSideBarPrivate *QQuickSideBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSideBarPrivate *ritual_ZNK13QQuickSideBar6d_funcEv(
    const QQuickSideBar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickSideBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSideBar(
    QQuickSideBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSideBar *>(self)->take(key, call);
}

//  void QQuickSideBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickSideBar17componentCompleteEv(QQuickSideBar *self) {
  static_cast<OwnQQuickSideBar *>(self)->OwnQQuickSideBar::componentComplete();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
