//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p.h,
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
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontainer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtQuick/QQuickItem>

//  Only a class built on QQuickContainer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickContainer : QQuickContainer {
  using QQuickContainer::componentComplete;
  using QQuickContainer::itemChange;
  using QQuickContainer::contentItemChange;
  using QQuickContainer::isContent;
  using QQuickContainer::itemAdded;
  using QQuickContainer::itemMoved;
  using QQuickContainer::itemRemoved;
};

//  A QQuickContainer that Python can take functions over in. Every QQuickContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall0)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall2)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickContainerCall3)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall4)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall5)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickContainerCall6)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
typedef const QFont * (*CuteQQuickContainerCall7)(const void *, int *);
typedef void (*CuteQQuickContainerCall8)(const void *, int *);
typedef void (*CuteQQuickContainerCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickContainerCall10)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall11)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall12)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall13)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickContainerCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickContainerCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickContainerCall17)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickContainerCall18)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickContainerCall19)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickContainerCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickContainerCall21)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickContainerCall22)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickContainerCall24)(const void *, int *);
typedef void (*CuteQQuickContainerCall25)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickContainerCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickContainerCall27)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickContainerCall28)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickContainerCall29)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickContainerCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickContainerCall31)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickContainerCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickContainerCall33)(const void *, int *);
typedef bool (*CuteQQuickContainerCall34)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickContainerCall35)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickContainerCall36)(const void *, int *);
typedef void * (*CuteQQuickContainerCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContainerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall39)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickContainerCall40)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickContainerCall41)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickContainerCall42)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickContainerCall43)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickContainerCall44)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickContainerCall45)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickContainerCall46)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickContainerCall47)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickContainerCall48)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickContainerCall49)(const void *, int *);
typedef void (*CuteQQuickContainerCall50)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContainerCall51)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContainerCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickContainer : public QQuickContainer {
public:
  using QQuickContainer::QQuickContainer;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
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

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContainerCall0 call = reinterpret_cast<CuteQQuickContainerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContainer::componentComplete();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemChange(ItemChange change, const
  //      ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContainerCall1 call = reinterpret_cast<CuteQQuickContainerCall1>(taken[1]);
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
      CuteQQuickContainerCall2 call = reinterpret_cast<CuteQQuickContainerCall2>(taken[2]);
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
      CuteQQuickContainerCall3 call = reinterpret_cast<CuteQQuickContainerCall3>(taken[3]);
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
      CuteQQuickContainerCall4 call = reinterpret_cast<CuteQQuickContainerCall4>(taken[4]);
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
      CuteQQuickContainerCall5 call = reinterpret_cast<CuteQQuickContainerCall5>(taken[5]);
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
      CuteQQuickContainerCall6 call = reinterpret_cast<CuteQQuickContainerCall6>(taken[6]);
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
      CuteQQuickContainerCall7 call = reinterpret_cast<CuteQQuickContainerCall7>(taken[7]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickContainerCall8 call = reinterpret_cast<CuteQQuickContainerCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickContainerCall9 call = reinterpret_cast<CuteQQuickContainerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickContainerCall10 call = reinterpret_cast<CuteQQuickContainerCall10>(taken[10]);
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
      CuteQQuickContainerCall11 call = reinterpret_cast<CuteQQuickContainerCall11>(taken[11]);
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
      CuteQQuickContainerCall12 call = reinterpret_cast<CuteQQuickContainerCall12>(taken[12]);
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
      CuteQQuickContainerCall13 call = reinterpret_cast<CuteQQuickContainerCall13>(taken[13]);
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
      CuteQQuickContainerCall14 call = reinterpret_cast<CuteQQuickContainerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickContainerCall15 call = reinterpret_cast<CuteQQuickContainerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickContainerCall16 call = reinterpret_cast<CuteQQuickContainerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickContainerCall17 call = reinterpret_cast<CuteQQuickContainerCall17>(taken[17]);
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
      CuteQQuickContainerCall18 call = reinterpret_cast<CuteQQuickContainerCall18>(taken[18]);
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
      CuteQQuickContainerCall19 call = reinterpret_cast<CuteQQuickContainerCall19>(taken[19]);
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
      CuteQQuickContainerCall20 call = reinterpret_cast<CuteQQuickContainerCall20>(taken[20]);
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
      CuteQQuickContainerCall21 call = reinterpret_cast<CuteQQuickContainerCall21>(taken[21]);
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
      CuteQQuickContainerCall22 call = reinterpret_cast<CuteQQuickContainerCall22>(taken[22]);
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
      CuteQQuickContainerCall23 call = reinterpret_cast<CuteQQuickContainerCall23>(taken[23]);
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
      CuteQQuickContainerCall24 call = reinterpret_cast<CuteQQuickContainerCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickContainerCall25 call = reinterpret_cast<CuteQQuickContainerCall25>(taken[25]);
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
      CuteQQuickContainerCall26 call = reinterpret_cast<CuteQQuickContainerCall26>(taken[26]);
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
      CuteQQuickContainerCall27 call = reinterpret_cast<CuteQQuickContainerCall27>(taken[27]);
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
      CuteQQuickContainerCall28 call = reinterpret_cast<CuteQQuickContainerCall28>(taken[28]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickContainerCall29 call = reinterpret_cast<CuteQQuickContainerCall29>(taken[29]);
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
      CuteQQuickContainerCall30 call = reinterpret_cast<CuteQQuickContainerCall30>(taken[30]);
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
      CuteQQuickContainerCall31 call = reinterpret_cast<CuteQQuickContainerCall31>(taken[31]);
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
      CuteQQuickContainerCall32 call = reinterpret_cast<CuteQQuickContainerCall32>(taken[32]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickContainerCall33 call = reinterpret_cast<CuteQQuickContainerCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickContainerCall34 call = reinterpret_cast<CuteQQuickContainerCall34>(taken[34]);
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
      CuteQQuickContainerCall35 call = reinterpret_cast<CuteQQuickContainerCall35>(taken[35]);
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
      CuteQQuickContainerCall36 call = reinterpret_cast<CuteQQuickContainerCall36>(taken[36]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickContainerCall37 call = reinterpret_cast<CuteQQuickContainerCall37>(taken[37]);
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
      CuteQQuickContainerCall38 call = reinterpret_cast<CuteQQuickContainerCall38>(taken[38]);
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
      CuteQQuickContainerCall39 call = reinterpret_cast<CuteQQuickContainerCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickContainerCall40 call = reinterpret_cast<CuteQQuickContainerCall40>(taken[40]);
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
      CuteQQuickContainerCall41 call = reinterpret_cast<CuteQQuickContainerCall41>(taken[41]);
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
      CuteQQuickContainerCall42 call = reinterpret_cast<CuteQQuickContainerCall42>(taken[42]);
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
      CuteQQuickContainerCall43 call = reinterpret_cast<CuteQQuickContainerCall43>(taken[43]);
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
      CuteQQuickContainerCall44 call = reinterpret_cast<CuteQQuickContainerCall44>(taken[44]);
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
      CuteQQuickContainerCall45 call = reinterpret_cast<CuteQQuickContainerCall45>(taken[45]);
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
      CuteQQuickContainerCall46 call = reinterpret_cast<CuteQQuickContainerCall46>(taken[46]);
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
      CuteQQuickContainerCall47 call = reinterpret_cast<CuteQQuickContainerCall47>(taken[47]);
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
      CuteQQuickContainerCall48 call = reinterpret_cast<CuteQQuickContainerCall48>(taken[48]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickContainerCall49 call = reinterpret_cast<CuteQQuickContainerCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickContainerCall50 call = reinterpret_cast<CuteQQuickContainerCall50>(taken[50]);
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
      CuteQQuickContainerCall51 call = reinterpret_cast<CuteQQuickContainerCall51>(taken[51]);
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
      CuteQQuickContainerCall52 call = reinterpret_cast<CuteQQuickContainerCall52>(taken[52]);
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
      CuteQQuickContainerCall53 call = reinterpret_cast<CuteQQuickContainerCall53>(taken[53]);
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
      CuteQQuickContainerCall54 call = reinterpret_cast<CuteQQuickContainerCall54>(taken[54]);
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
      CuteQQuickContainerCall55 call = reinterpret_cast<CuteQQuickContainerCall55>(taken[55]);
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
      CuteQQuickContainerCall56 call = reinterpret_cast<CuteQQuickContainerCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickContainer10metaObjectEv(
    const QQuickContainer *self) {
  return self->metaObject();
}

//  void *QQuickContainer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickContainer11qt_metacastEPKc(
    QQuickContainer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickContainer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickContainer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickContainer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickContainer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickContainer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickContainer::tr(s, c, n));
}

//  QQuickContainer::QQuickContainer(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickContainer *ritual_ZN15QQuickContainerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickContainer(parent);
}

//  QQuickContainer::~QQuickContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainerD1Ev(QQuickContainer *self) {
  delete self;
}

//  int QQuickContainer::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickContainer5countEv(const QQuickContainer *self) {
  return self->count();
}

//  QQuickItem *QQuickContainer::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickContainer6itemAtEi(
    const QQuickContainer *self,
    int index) {
  return self->itemAt(index);
}

//  void QQuickContainer::addItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer7addItemEP10QQuickItem(
    QQuickContainer *self,
    QQuickItem *item) {
  self->addItem(item);
}

//  void QQuickContainer::insertItem(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer10insertItemEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  self->insertItem(index, item);
}

//  void QQuickContainer::moveItem(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer8moveItemEii(
    QQuickContainer *self,
    int from,
    int to) {
  self->moveItem(from, to);
}

//  void QQuickContainer::removeItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer10removeItemEP10QQuickItem(
    QQuickContainer *self,
    QQuickItem *item) {
  self->removeItem(item);
}

//  QQuickItem *QQuickContainer::takeItem(int index)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN15QQuickContainer8takeItemEi(
    QQuickContainer *self,
    int index) {
  return self->takeItem(index);
}

//  QVariant QQuickContainer::contentModel() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQuickContainer12contentModelEv(
    const QQuickContainer *self) {
  return new QVariant(self->contentModel());
}

//  QQmlListProperty<QObject> QQuickContainer::contentData()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN15QQuickContainer11contentDataEv(
    QQuickContainer *self) {
  return new QQmlListProperty<QObject>(self->contentData());
}

//  QQmlListProperty<QQuickItem> QQuickContainer::contentChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickItem> *ritual_ZN15QQuickContainer15contentChildrenEv(
    QQuickContainer *self) {
  return new QQmlListProperty<QQuickItem>(self->contentChildren());
}

//  int QQuickContainer::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickContainer12currentIndexEv(
    const QQuickContainer *self) {
  return self->currentIndex();
}

//  QQuickItem *QQuickContainer::currentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickContainer11currentItemEv(
    const QQuickContainer *self) {
  return self->currentItem();
}

//  qreal QQuickContainer::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickContainer12contentWidthEv(
    const QQuickContainer *self) {
  return self->contentWidth();
}

//  void QQuickContainer::setContentWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer15setContentWidthEd(
    QQuickContainer *self,
    qreal width) {
  self->setContentWidth(width);
}

//  void QQuickContainer::resetContentWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer17resetContentWidthEv(QQuickContainer *self) {
  self->resetContentWidth();
}

//  qreal QQuickContainer::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickContainer13contentHeightEv(
    const QQuickContainer *self) {
  return self->contentHeight();
}

//  void QQuickContainer::setContentHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer16setContentHeightEd(
    QQuickContainer *self,
    qreal height) {
  self->setContentHeight(height);
}

//  void QQuickContainer::resetContentHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer18resetContentHeightEv(
    QQuickContainer *self) {
  self->resetContentHeight();
}

//  void QQuickContainer::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer15setCurrentIndexEi(
    QQuickContainer *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QQuickContainer::incrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer21incrementCurrentIndexEv(
    QQuickContainer *self) {
  self->incrementCurrentIndex();
}

//  void QQuickContainer::decrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer21decrementCurrentIndexEv(
    QQuickContainer *self) {
  self->decrementCurrentIndex();
}

//  void QQuickContainer::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer12countChangedEv(QQuickContainer *self) {
  self->countChanged();
}

//  void QQuickContainer::contentChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer22contentChildrenChangedEv(
    QQuickContainer *self) {
  self->contentChildrenChanged();
}

//  void QQuickContainer::currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer19currentIndexChangedEv(
    QQuickContainer *self) {
  self->currentIndexChanged();
}

//  void QQuickContainer::currentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer18currentItemChangedEv(
    QQuickContainer *self) {
  self->currentItemChanged();
}

//  void QQuickContainer::contentWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer19contentWidthChangedEv(
    QQuickContainer *self) {
  self->contentWidthChanged();
}

//  void QQuickContainer::contentHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer20contentHeightChangedEv(
    QQuickContainer *self) {
  self->contentHeightChanged();
}

//  QQuickContainer::QQuickContainer(QQuickContainerPrivate &dd, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickContainer *ritual_ZN15QQuickContainerC1ER22QQuickContainerPrivateP10QQuickItem(
    QQuickContainerPrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickContainer(*dd, parent);
}

//  void QQuickContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer17componentCompleteEv(QQuickContainer *self) {
  self->componentComplete();
}

//  void QQuickContainer::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickContainer *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickContainer::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer17contentItemChangeEP10QQuickItemS1_(
    QQuickContainer *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  bool QQuickContainer::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickContainer9isContentEP10QQuickItem(
    const QQuickContainer *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  void QQuickContainer::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer9itemAddedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickContainer::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer9itemMovedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  self->itemMoved(index, item);
}

//  void QQuickContainer::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContainer11itemRemovedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

//  QQuickContainerPrivate *QQuickContainer::d_func()
extern "C" Q_DECL_EXPORT
QQuickContainerPrivate *ritual_ZN15QQuickContainer6d_funcEv(
    QQuickContainer *self) {
  return self->d_func();
}

//  const QQuickContainerPrivate *QQuickContainer::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickContainerPrivate *ritual_ZNK15QQuickContainer6d_funcEv(
    const QQuickContainer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickContainer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContainer(
    QQuickContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContainer *>(self)->take(key, call);
}

//  void QQuickContainer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer17componentCompleteEv(
    QQuickContainer *self) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::componentComplete();
}

//  void QQuickContainer::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickContainer *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::itemChange(
      change,
      *data);
}

//  void QQuickContainer::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer17contentItemChangeEP10QQuickItemS1_(
    QQuickContainer *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::contentItemChange(
      newItem,
      oldItem);
}

//  bool QQuickContainer::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QQuickContainer9isContentEP10QQuickItem(
    const QQuickContainer *self,
    QQuickItem *item) {
  return static_cast<const OwnQQuickContainer *>(self)->OwnQQuickContainer::isContent(
      item);
}

//  void QQuickContainer::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer9itemAddedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::itemAdded(
      index,
      item);
}

//  void QQuickContainer::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer9itemMovedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::itemMoved(
      index,
      item);
}

//  void QQuickContainer::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickContainer11itemRemovedEiP10QQuickItem(
    QQuickContainer *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickContainer *>(self)->OwnQQuickContainer::itemRemoved(
      index,
      item);
}

//  a QQmlListProperty<QObject> a ritual of QQuickContainer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickContainer__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<QQuickItem> a ritual of QQuickContainer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickContainer__QQmlListProperty_QQuickItem(
    QQmlListProperty<QQuickItem> *self) {
  delete self;
}

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
