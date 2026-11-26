//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h, Qt
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
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickDialogButtonBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDialogButtonBox : QQuickDialogButtonBox {
  using QQuickDialogButtonBox::updatePolish;
  using QQuickDialogButtonBox::componentComplete;
  using QQuickDialogButtonBox::geometryChange;
  using QQuickDialogButtonBox::contentItemChange;
  using QQuickDialogButtonBox::isContent;
  using QQuickDialogButtonBox::itemAdded;
  using QQuickDialogButtonBox::itemRemoved;
  using QQuickDialogButtonBox::accessibleRole;
  using QQuickDialogButtonBox::event;
};

//  A QQuickDialogButtonBox that Python can take functions over in. Every QQuickDialogButtonBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall1)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall2)(const void *, const QRectF *, const QRectF *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall3)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickDialogButtonBoxCall4)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall5)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall6)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef int (*CuteQQuickDialogButtonBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
typedef bool (*CuteQQuickDialogButtonBoxCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogButtonBoxCall10)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
typedef const QFont * (*CuteQQuickDialogButtonBoxCall11)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall12)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall14)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall15)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall16)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall17)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall21)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDialogButtonBoxCall22)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDialogButtonBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDialogButtonBoxCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDialogButtonBoxCall25)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall26)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickDialogButtonBoxCall27)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall28)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickDialogButtonBoxCall29)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall30)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall31)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall32)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickDialogButtonBoxCall33)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickDialogButtonBoxCall34)(const void *, int *);
typedef const QRectF * (*CuteQQuickDialogButtonBoxCall35)(const void *, int *);
typedef bool (*CuteQQuickDialogButtonBoxCall36)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickDialogButtonBoxCall37)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickDialogButtonBoxCall38)(const void *, int *);
typedef void * (*CuteQQuickDialogButtonBoxCall39)(const void *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall40)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall41)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickDialogButtonBoxCall42)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickDialogButtonBoxCall43)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogButtonBoxCall44)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogButtonBoxCall45)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogButtonBoxCall46)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogButtonBoxCall47)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickDialogButtonBoxCall48)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickDialogButtonBoxCall49)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickDialogButtonBoxCall50)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDialogButtonBoxCall51)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogButtonBoxCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogButtonBoxCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogButtonBoxCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogButtonBoxCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogButtonBoxCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDialogButtonBox : public QQuickDialogButtonBox {
public:
  using QQuickDialogButtonBox::QQuickDialogButtonBox;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
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
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemAddedEiP10QQuickItem")) {
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
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN15QQuickContainer9itemMovedEiP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
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
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl11hoverChangeEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN13QQuickControl12mirrorChangeEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13spacingChangeEdd")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[32] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[36] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[39] = call;
      return true;
    }
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
  //  void QQuickDialogButtonBox::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall0 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::updatePolish();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall1 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::componentComplete();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall2 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall2>(taken[2]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::geometryChange(newGeometry, oldGeometry);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall3 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall3>(taken[3]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickDialogButtonBox::isContent(QQuickItem *item) const
  bool isContent(QQuickItem *item) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall4 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall4>(taken[4]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickDialogButtonBox::isContent(item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::itemAdded(int index, QQuickItem *item)
  void itemAdded(int index, QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall5 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall5>(taken[5]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::itemAdded(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::itemRemoved(int index, QQuickItem *item)
  void itemRemoved(int index, QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall6 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall6>(taken[6]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::itemRemoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
  //  QAccessible::Role QQuickDialogButtonBox::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall7 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickDialogButtonBox::accessibleRole();
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quicktemplates2_container)
  //  bool QQuickDialogButtonBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall8 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall8>(taken[8]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickDialogButtonBox::event(e);
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialogButtonBox::itemChange(QQuickItem::ItemChange change,
  //      const QQuickItem::ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall9 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall9>(taken[9]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickDialogButtonBox::itemChange(change, data);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickContainer::itemMoved(int index, QQuickItem *item)
  void itemMoved(int index, QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall10 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall10>(taken[10]);
      call(this, index, item, &handled);
      if (handled) return;
    }
    QQuickContainer::itemMoved(index, item);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall11 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall11>(taken[11]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall12 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

  //  void QQuickControl::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall13 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusInEvent(event);
  }

  //  void QQuickControl::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall14 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall15 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall16 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall17 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall18 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall19 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall20 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall21 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall21>(taken[21]);
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
      CuteQQuickDialogButtonBoxCall22 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall22>(taken[22]);
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
      CuteQQuickDialogButtonBoxCall23 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall23>(taken[23]);
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
      CuteQQuickDialogButtonBoxCall24 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickControl::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall25 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall25>(taken[25]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickControl::fontChange(newFont, oldFont);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall26 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::hoverChange();
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mirrorChange()
  void mirrorChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall27 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall28 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall29 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall30 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall31 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall31>(taken[31]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall32 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControl::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall33 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall33>(taken[33]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControl::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall34 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall35 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall35>(taken[35]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall36 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall36>(taken[36]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall37 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall37>(taken[37]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall38 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall38>(taken[38]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall39 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall40 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall41 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall41>(taken[41]);
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
      CuteQQuickDialogButtonBoxCall42 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall42>(taken[42]);
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
      CuteQQuickDialogButtonBoxCall43 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall43>(taken[43]);
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
      CuteQQuickDialogButtonBoxCall44 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall44>(taken[44]);
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
      CuteQQuickDialogButtonBoxCall45 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall45>(taken[45]);
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
      CuteQQuickDialogButtonBoxCall46 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall46>(taken[46]);
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
      CuteQQuickDialogButtonBoxCall47 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall47>(taken[47]);
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
      CuteQQuickDialogButtonBoxCall48 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall48>(taken[48]);
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
      CuteQQuickDialogButtonBoxCall49 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall49>(taken[49]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall50 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickDialogButtonBoxCall51 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall51>(taken[51]);
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
      CuteQQuickDialogButtonBoxCall52 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall52>(taken[52]);
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
      CuteQQuickDialogButtonBoxCall53 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall53>(taken[53]);
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
      CuteQQuickDialogButtonBoxCall54 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall54>(taken[54]);
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
      CuteQQuickDialogButtonBoxCall55 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall55>(taken[55]);
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
      CuteQQuickDialogButtonBoxCall56 call = reinterpret_cast<CuteQQuickDialogButtonBoxCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDialogButtonBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickDialogButtonBox10metaObjectEv(
    const QQuickDialogButtonBox *self) {
  return self->metaObject();
}

//  void *QQuickDialogButtonBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickDialogButtonBox11qt_metacastEPKc(
    QQuickDialogButtonBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDialogButtonBox::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickDialogButtonBox11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDialogButtonBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDialogButtonBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickDialogButtonBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDialogButtonBox::tr(s, c, n));
}

//  void QQuickDialogButtonBox::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox21qt_qmlMarker_attachedEv(
    QQuickDialogButtonBox *self) {
  self->qt_qmlMarker_attached();
}

//  const QMetaObject *QQuickDialogButtonBox::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN21QQuickDialogButtonBox20qmlExtendedNamespaceEv() {
  return QQuickDialogButtonBox::qmlExtendedNamespace();
}

//  void QQuickDialogButtonBox::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox30qt_qmlMarker_extendedNamespaceEv(
    QQuickDialogButtonBox *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickDialogButtonBox::QQuickDialogButtonBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZN21QQuickDialogButtonBoxC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickDialogButtonBox(parent);
}

//  QQuickDialogButtonBox::~QQuickDialogButtonBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBoxD1Ev(QQuickDialogButtonBox *self) {
  delete self;
}

//  Position QQuickDialogButtonBox::position() const
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox::Position ritual_ZNK21QQuickDialogButtonBox8positionEv(
    const QQuickDialogButtonBox *self) {
  return self->position();
}

//  void QQuickDialogButtonBox::setPosition(Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox11setPositionENS_8PositionE(
    QQuickDialogButtonBox *self,
    QQuickDialogButtonBox::Position position) {
  self->setPosition(position);
}

//  Qt::Alignment QQuickDialogButtonBox::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickDialogButtonBox9alignmentEv(
    const QQuickDialogButtonBox *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QQuickDialogButtonBox::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickDialogButtonBox *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QQuickDialogButtonBox::resetAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox14resetAlignmentEv(
    QQuickDialogButtonBox *self) {
  self->resetAlignment();
}

//  QPlatformDialogHelper::StandardButtons
//      QQuickDialogButtonBox::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickDialogButtonBox15standardButtonsEv(
    const QQuickDialogButtonBox *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  void QQuickDialogButtonBox::setStandardButtons(QPlatformDialogHelper::Sta
//      ndardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox18setStandardButtonsE6QFlagsIN21QPlatformDialogHelper14StandardButtonEE(
    QQuickDialogButtonBox *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QPlatformDialogHelper::StandardButton>::fromInt(buttons));
}

//  QQuickAbstractButton *QQuickDialogButtonBox::standardButton(QPlatformDial
//      ogHelper::StandardButton button) const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZNK21QQuickDialogButtonBox14standardButtonEN21QPlatformDialogHelper14StandardButtonE(
    const QQuickDialogButtonBox *self,
    QPlatformDialogHelper::StandardButton button) {
  return self->standardButton(button);
}

//  QPlatformDialogHelper::StandardButton
//      QQuickDialogButtonBox::defaultStandardButton() const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::StandardButton ritual_ZNK21QQuickDialogButtonBox21defaultStandardButtonEv(
    const QQuickDialogButtonBox *self) {
  return self->defaultStandardButton();
}

//  void QQuickDialogButtonBox::setDefaultStandardButton(QPlatformDialogHelpe
//      r::StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox24setDefaultStandardButtonEN21QPlatformDialogHelper14StandardButtonE(
    QQuickDialogButtonBox *self,
    QPlatformDialogHelper::StandardButton button) {
  self->setDefaultStandardButton(button);
}

//  QQuickAbstractButton *QQuickDialogButtonBox::defaultButton() const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZNK21QQuickDialogButtonBox13defaultButtonEv(
    const QQuickDialogButtonBox *self) {
  return self->defaultButton();
}

//  void QQuickDialogButtonBox::setDefaultButton(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox16setDefaultButtonEP20QQuickAbstractButton(
    QQuickDialogButtonBox *self,
    QQuickAbstractButton *button) {
  self->setDefaultButton(button);
}

//  QQmlComponent *QQuickDialogButtonBox::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQuickDialogButtonBox8delegateEv(
    const QQuickDialogButtonBox *self) {
  return self->delegate();
}

//  void QQuickDialogButtonBox::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox11setDelegateEP13QQmlComponent(
    QQuickDialogButtonBox *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QQuickDialogButtonBoxAttached
//      *QQuickDialogButtonBox::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxAttached *ritual_ZN21QQuickDialogButtonBox21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickDialogButtonBox::qmlAttachedProperties(object);
}

//  QPlatformDialogHelper::ButtonLayout QQuickDialogButtonBox::buttonLayout()
//      const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::ButtonLayout ritual_ZNK21QQuickDialogButtonBox12buttonLayoutEv(
    const QQuickDialogButtonBox *self) {
  return self->buttonLayout();
}

//  void QQuickDialogButtonBox::setButtonLayout(QPlatformDialogHelper::Button
//      Layout layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox15setButtonLayoutEN21QPlatformDialogHelper12ButtonLayoutE(
    QQuickDialogButtonBox *self,
    QPlatformDialogHelper::ButtonLayout layout) {
  self->setButtonLayout(layout);
}

//  void QQuickDialogButtonBox::resetButtonLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox17resetButtonLayoutEv(
    QQuickDialogButtonBox *self) {
  self->resetButtonLayout();
}

//  void QQuickDialogButtonBox::accepted()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox8acceptedEv(
    QQuickDialogButtonBox *self) {
  self->accepted();
}

//  void QQuickDialogButtonBox::rejected()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox8rejectedEv(
    QQuickDialogButtonBox *self) {
  self->rejected();
}

//  void QQuickDialogButtonBox::helpRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox13helpRequestedEv(
    QQuickDialogButtonBox *self) {
  self->helpRequested();
}

//  void QQuickDialogButtonBox::clicked(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox7clickedEP20QQuickAbstractButton(
    QQuickDialogButtonBox *self,
    QQuickAbstractButton *button) {
  self->clicked(button);
}

//  void QQuickDialogButtonBox::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox15positionChangedEv(
    QQuickDialogButtonBox *self) {
  self->positionChanged();
}

//  void QQuickDialogButtonBox::alignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox16alignmentChangedEv(
    QQuickDialogButtonBox *self) {
  self->alignmentChanged();
}

//  void QQuickDialogButtonBox::standardButtonsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox22standardButtonsChangedEv(
    QQuickDialogButtonBox *self) {
  self->standardButtonsChanged();
}

//  void QQuickDialogButtonBox::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox15delegateChangedEv(
    QQuickDialogButtonBox *self) {
  self->delegateChanged();
}

//  void QQuickDialogButtonBox::applied()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox7appliedEv(
    QQuickDialogButtonBox *self) {
  self->applied();
}

//  void QQuickDialogButtonBox::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox5resetEv(QQuickDialogButtonBox *self) {
  self->reset();
}

//  void QQuickDialogButtonBox::discarded()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox9discardedEv(
    QQuickDialogButtonBox *self) {
  self->discarded();
}

//  void QQuickDialogButtonBox::buttonLayoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox19buttonLayoutChangedEv(
    QQuickDialogButtonBox *self) {
  self->buttonLayoutChanged();
}

//  void QQuickDialogButtonBox::defaultStandardButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox28defaultStandardButtonChangedEv(
    QQuickDialogButtonBox *self) {
  self->defaultStandardButtonChanged();
}

//  void QQuickDialogButtonBox::defaultButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox20defaultButtonChangedEv(
    QQuickDialogButtonBox *self) {
  self->defaultButtonChanged();
}

//  void QQuickDialogButtonBox::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox12updatePolishEv(
    QQuickDialogButtonBox *self) {
  self->updatePolish();
}

//  void QQuickDialogButtonBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox17componentCompleteEv(
    QQuickDialogButtonBox *self) {
  self->componentComplete();
}

//  void QQuickDialogButtonBox::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox14geometryChangeERK6QRectFS2_(
    QQuickDialogButtonBox *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickDialogButtonBox::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox17contentItemChangeEP10QQuickItemS1_(
    QQuickDialogButtonBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  bool QQuickDialogButtonBox::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickDialogButtonBox9isContentEP10QQuickItem(
    const QQuickDialogButtonBox *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  void QQuickDialogButtonBox::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox9itemAddedEiP10QQuickItem(
    QQuickDialogButtonBox *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickDialogButtonBox::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox11itemRemovedEiP10QQuickItem(
    QQuickDialogButtonBox *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDialogButtonBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK21QQuickDialogButtonBox14accessibleRoleEv(
    const QQuickDialogButtonBox *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  bool QQuickDialogButtonBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDialogButtonBox5eventEP6QEvent(
    QQuickDialogButtonBox *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickDialogButtonBox::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDialogButtonBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDialogButtonBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickDialogButtonBoxPrivate *QQuickDialogButtonBox::d_func()
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxPrivate *ritual_ZN21QQuickDialogButtonBox6d_funcEv(
    QQuickDialogButtonBox *self) {
  return self->d_func();
}

//  const QQuickDialogButtonBoxPrivate *QQuickDialogButtonBox::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialogButtonBoxPrivate *ritual_ZNK21QQuickDialogButtonBox6d_funcEv(
    const QQuickDialogButtonBox *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickDialogButtonBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDialogButtonBox(
    QQuickDialogButtonBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDialogButtonBox *>(self)->take(key, call);
}

//  void QQuickDialogButtonBox::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox12updatePolishEv(
    QQuickDialogButtonBox *self) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::updatePolish();
}

//  void QQuickDialogButtonBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox17componentCompleteEv(
    QQuickDialogButtonBox *self) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::componentComplete();
}

//  void QQuickDialogButtonBox::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox14geometryChangeERK6QRectFS2_(
    QQuickDialogButtonBox *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickDialogButtonBox::contentItemChange(QQuickItem *newItem,
//      QQuickItem *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox17contentItemChangeEP10QQuickItemS1_(
    QQuickDialogButtonBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::contentItemChange(
      newItem,
      oldItem);
}

//  bool QQuickDialogButtonBox::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QQuickDialogButtonBox9isContentEP10QQuickItem(
    const QQuickDialogButtonBox *self,
    QQuickItem *item) {
  return static_cast<const OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::isContent(
      item);
}

//  void QQuickDialogButtonBox::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox9itemAddedEiP10QQuickItem(
    QQuickDialogButtonBox *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::itemAdded(
      index,
      item);
}

//  void QQuickDialogButtonBox::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox11itemRemovedEiP10QQuickItem(
    QQuickDialogButtonBox *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::itemRemoved(
      index,
      item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDialogButtonBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK21QQuickDialogButtonBox14accessibleRoleEv(
    const QQuickDialogButtonBox *self) {
  return static_cast<const OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  bool QQuickDialogButtonBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickDialogButtonBox5eventEP6QEvent(
    QQuickDialogButtonBox *self,
    QEvent *e) {
  return static_cast<OwnQQuickDialogButtonBox *>(self)->OwnQQuickDialogButtonBox::event(
      e);
}

//  void QQuickDialogButtonBox::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickDialogButtonBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDialogButtonBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickDialogButtonBox::itemChange(change, *data);
}

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
