//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksearchfield_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksearchfield_p.h>
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

//  Only a class built on QQuickSearchField may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSearchField : QQuickSearchField {
  using QQuickSearchField::eventFilter;
  using QQuickSearchField::focusInEvent;
  using QQuickSearchField::focusOutEvent;
  using QQuickSearchField::hoverEnterEvent;
  using QQuickSearchField::hoverMoveEvent;
  using QQuickSearchField::hoverLeaveEvent;
  using QQuickSearchField::keyPressEvent;
  using QQuickSearchField::classBegin;
  using QQuickSearchField::componentComplete;
  using QQuickSearchField::contentItemChange;
  using QQuickSearchField::itemChange;
};

//  A QQuickSearchField that Python can take functions over in. Every QQuickSearchField
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSearchFieldCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall1)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall2)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall3)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall4)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall5)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall7)(const void *, int *);
typedef void (*CuteQQuickSearchFieldCall8)(const void *, int *);
typedef void (*CuteQQuickSearchFieldCall9)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSearchFieldCall10)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QFont * (*CuteQQuickSearchFieldCall11)(const void *, int *);
typedef void (*CuteQQuickSearchFieldCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickSearchFieldCall15)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSearchFieldCall16)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickSearchFieldCall17)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSearchFieldCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickSearchFieldCall19)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickSearchFieldCall20)(const void *, const QFont *, const QFont *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSearchFieldCall21)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickSearchFieldCall22)(const void *, int *);
typedef void (*CuteQQuickSearchFieldCall23)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickSearchFieldCall24)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSearchFieldCall25)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickSearchFieldCall26)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickSearchFieldCall27)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSearchFieldCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSearchFieldCall29)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef const QRectF * (*CuteQQuickSearchFieldCall30)(const void *, int *);
typedef const QRectF * (*CuteQQuickSearchFieldCall31)(const void *, int *);
typedef bool (*CuteQQuickSearchFieldCall32)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickSearchFieldCall33)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickSearchFieldCall34)(const void *, int *);
typedef void * (*CuteQQuickSearchFieldCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSearchFieldCall36)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall37)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickSearchFieldCall38)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickSearchFieldCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSearchFieldCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSearchFieldCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSearchFieldCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickSearchFieldCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickSearchFieldCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickSearchFieldCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickSearchFieldCall46)(const void *, int *);
typedef void (*CuteQQuickSearchFieldCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSearchFieldCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSearchField : public QQuickSearchField {
public:
  using QQuickSearchField::QQuickSearchField;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[11] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[47] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickSearchField::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSearchFieldCall0 call = reinterpret_cast<CuteQQuickSearchFieldCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickSearchField::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickSearchField::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSearchFieldCall1 call = reinterpret_cast<CuteQQuickSearchFieldCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::focusInEvent(event);
  }

  //  void QQuickSearchField::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSearchFieldCall2 call = reinterpret_cast<CuteQQuickSearchFieldCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::focusOutEvent(event);
  }

  //  void QQuickSearchField::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSearchFieldCall3 call = reinterpret_cast<CuteQQuickSearchFieldCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::hoverEnterEvent(event);
  }

  //  void QQuickSearchField::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSearchFieldCall4 call = reinterpret_cast<CuteQQuickSearchFieldCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::hoverMoveEvent(event);
  }

  //  void QQuickSearchField::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSearchFieldCall5 call = reinterpret_cast<CuteQQuickSearchFieldCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::hoverLeaveEvent(event);
  }

  //  void QQuickSearchField::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSearchFieldCall6 call = reinterpret_cast<CuteQQuickSearchFieldCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSearchField::keyPressEvent(event);
  }

  //  void QQuickSearchField::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSearchFieldCall7 call = reinterpret_cast<CuteQQuickSearchFieldCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSearchField::classBegin();
  }

  //  void QQuickSearchField::componentComplete()
  void componentComplete() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSearchFieldCall8 call = reinterpret_cast<CuteQQuickSearchFieldCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickSearchField::componentComplete();
  }

  //  void QQuickSearchField::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSearchFieldCall9 call = reinterpret_cast<CuteQQuickSearchFieldCall9>(taken[9]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickSearchField::contentItemChange(newItem, oldItem);
  }

  //  void QQuickSearchField::itemChange(QQuickItem::ItemChange change,
  //      const QQuickItem::ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSearchFieldCall10 call = reinterpret_cast<CuteQQuickSearchFieldCall10>(taken[10]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickSearchField::itemChange(change, data);
  }

  //  QFont QQuickControl::defaultFont() const
  QFont defaultFont() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSearchFieldCall11 call = reinterpret_cast<CuteQQuickSearchFieldCall11>(taken[11]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControl::defaultFont();
  }

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSearchFieldCall12 call = reinterpret_cast<CuteQQuickSearchFieldCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSearchFieldCall13 call = reinterpret_cast<CuteQQuickSearchFieldCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSearchFieldCall14 call = reinterpret_cast<CuteQQuickSearchFieldCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSearchFieldCall15 call = reinterpret_cast<CuteQQuickSearchFieldCall15>(taken[15]);
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
      CuteQQuickSearchFieldCall16 call = reinterpret_cast<CuteQQuickSearchFieldCall16>(taken[16]);
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
      CuteQQuickSearchFieldCall17 call = reinterpret_cast<CuteQQuickSearchFieldCall17>(taken[17]);
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
      CuteQQuickSearchFieldCall18 call = reinterpret_cast<CuteQQuickSearchFieldCall18>(taken[18]);
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
      CuteQQuickSearchFieldCall19 call = reinterpret_cast<CuteQQuickSearchFieldCall19>(taken[19]);
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
      CuteQQuickSearchFieldCall20 call = reinterpret_cast<CuteQQuickSearchFieldCall20>(taken[20]);
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
      CuteQQuickSearchFieldCall21 call = reinterpret_cast<CuteQQuickSearchFieldCall21>(taken[21]);
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
      CuteQQuickSearchFieldCall22 call = reinterpret_cast<CuteQQuickSearchFieldCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickSearchFieldCall23 call = reinterpret_cast<CuteQQuickSearchFieldCall23>(taken[23]);
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
      CuteQQuickSearchFieldCall24 call = reinterpret_cast<CuteQQuickSearchFieldCall24>(taken[24]);
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
      CuteQQuickSearchFieldCall25 call = reinterpret_cast<CuteQQuickSearchFieldCall25>(taken[25]);
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
      CuteQQuickSearchFieldCall26 call = reinterpret_cast<CuteQQuickSearchFieldCall26>(taken[26]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSearchFieldCall27 call = reinterpret_cast<CuteQQuickSearchFieldCall27>(taken[27]);
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
      CuteQQuickSearchFieldCall28 call = reinterpret_cast<CuteQQuickSearchFieldCall28>(taken[28]);
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
      CuteQQuickSearchFieldCall29 call = reinterpret_cast<CuteQQuickSearchFieldCall29>(taken[29]);
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
      CuteQQuickSearchFieldCall30 call = reinterpret_cast<CuteQQuickSearchFieldCall30>(taken[30]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSearchFieldCall31 call = reinterpret_cast<CuteQQuickSearchFieldCall31>(taken[31]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSearchFieldCall32 call = reinterpret_cast<CuteQQuickSearchFieldCall32>(taken[32]);
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
      CuteQQuickSearchFieldCall33 call = reinterpret_cast<CuteQQuickSearchFieldCall33>(taken[33]);
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
      CuteQQuickSearchFieldCall34 call = reinterpret_cast<CuteQQuickSearchFieldCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSearchFieldCall35 call = reinterpret_cast<CuteQQuickSearchFieldCall35>(taken[35]);
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
      CuteQQuickSearchFieldCall36 call = reinterpret_cast<CuteQQuickSearchFieldCall36>(taken[36]);
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
      CuteQQuickSearchFieldCall37 call = reinterpret_cast<CuteQQuickSearchFieldCall37>(taken[37]);
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
      CuteQQuickSearchFieldCall38 call = reinterpret_cast<CuteQQuickSearchFieldCall38>(taken[38]);
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
      CuteQQuickSearchFieldCall39 call = reinterpret_cast<CuteQQuickSearchFieldCall39>(taken[39]);
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
      CuteQQuickSearchFieldCall40 call = reinterpret_cast<CuteQQuickSearchFieldCall40>(taken[40]);
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
      CuteQQuickSearchFieldCall41 call = reinterpret_cast<CuteQQuickSearchFieldCall41>(taken[41]);
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
      CuteQQuickSearchFieldCall42 call = reinterpret_cast<CuteQQuickSearchFieldCall42>(taken[42]);
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
      CuteQQuickSearchFieldCall43 call = reinterpret_cast<CuteQQuickSearchFieldCall43>(taken[43]);
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
      CuteQQuickSearchFieldCall44 call = reinterpret_cast<CuteQQuickSearchFieldCall44>(taken[44]);
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
      CuteQQuickSearchFieldCall45 call = reinterpret_cast<CuteQQuickSearchFieldCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickSearchFieldCall46 call = reinterpret_cast<CuteQQuickSearchFieldCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickSearchFieldCall47 call = reinterpret_cast<CuteQQuickSearchFieldCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickSearchFieldCall48 call = reinterpret_cast<CuteQQuickSearchFieldCall48>(taken[48]);
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
      CuteQQuickSearchFieldCall49 call = reinterpret_cast<CuteQQuickSearchFieldCall49>(taken[49]);
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
      CuteQQuickSearchFieldCall50 call = reinterpret_cast<CuteQQuickSearchFieldCall50>(taken[50]);
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
      CuteQQuickSearchFieldCall51 call = reinterpret_cast<CuteQQuickSearchFieldCall51>(taken[51]);
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
      CuteQQuickSearchFieldCall52 call = reinterpret_cast<CuteQQuickSearchFieldCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSearchField::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickSearchField10metaObjectEv(
    const QQuickSearchField *self) {
  return self->metaObject();
}

//  void *QQuickSearchField::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickSearchField11qt_metacastEPKc(
    QQuickSearchField *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSearchField::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickSearchField11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSearchField *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSearchField::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickSearchField2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSearchField::tr(s, c, n));
}

//  QQuickSearchField::QQuickSearchField(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSearchField *ritual_ZN17QQuickSearchFieldC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickSearchField(parent);
}

//  QQuickSearchField::~QQuickSearchField()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchFieldD1Ev(QQuickSearchField *self) {
  delete self;
}

//  QVariant QQuickSearchField::suggestionModel() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQuickSearchField15suggestionModelEv(
    const QQuickSearchField *self) {
  return new QVariant(self->suggestionModel());
}

//  void QQuickSearchField::setSuggestionModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField18setSuggestionModelERK8QVariant(
    QQuickSearchField *self,
    const QVariant *model) {
  self->setSuggestionModel(*model);
}

//  QQmlInstanceModel *QQuickSearchField::delegateModel() const
extern "C" Q_DECL_EXPORT
QQmlInstanceModel *ritual_ZNK17QQuickSearchField13delegateModelEv(
    const QQuickSearchField *self) {
  return self->delegateModel();
}

//  int QQuickSearchField::suggestionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField15suggestionCountEv(
    const QQuickSearchField *self) {
  return self->suggestionCount();
}

//  int QQuickSearchField::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField12currentIndexEv(
    const QQuickSearchField *self) {
  return self->currentIndex();
}

//  void QQuickSearchField::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15setCurrentIndexEi(
    QQuickSearchField *self,
    int index) {
  self->setCurrentIndex(index);
}

//  int QQuickSearchField::highlightedIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField16highlightedIndexEv(
    const QQuickSearchField *self) {
  return self->highlightedIndex();
}

//  QString QQuickSearchField::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickSearchField4textEv(
    const QQuickSearchField *self) {
  return new QString(self->text());
}

//  void QQuickSearchField::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField7setTextERK7QString(
    QQuickSearchField *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QQuickSearchField::textRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickSearchField8textRoleEv(
    const QQuickSearchField *self) {
  return new QString(self->textRole());
}

//  void QQuickSearchField::setTextRole(const QString &textRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField11setTextRoleERK7QString(
    QQuickSearchField *self,
    const QString *textRole) {
  self->setTextRole(*textRole);
}

//  bool QQuickSearchField::isLive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickSearchField6isLiveEv(const QQuickSearchField *self) {
  return self->isLive();
}

//  void QQuickSearchField::setLive(const bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField7setLiveEb(
    QQuickSearchField *self,
    bool live) {
  self->setLive(live);
}

//  QQuickIndicatorButton *QQuickSearchField::searchIndicator() const
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZNK17QQuickSearchField15searchIndicatorEv(
    const QQuickSearchField *self) {
  return self->searchIndicator();
}

//  QQuickIndicatorButton *QQuickSearchField::clearIndicator() const
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZNK17QQuickSearchField14clearIndicatorEv(
    const QQuickSearchField *self) {
  return self->clearIndicator();
}

//  QQuickPopup *QQuickSearchField::popup() const
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZNK17QQuickSearchField5popupEv(
    const QQuickSearchField *self) {
  return self->popup();
}

//  void QQuickSearchField::setPopup(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField8setPopupEP11QQuickPopup(
    QQuickSearchField *self,
    QQuickPopup *popup) {
  self->setPopup(popup);
}

//  QQmlComponent *QQuickSearchField::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK17QQuickSearchField8delegateEv(
    const QQuickSearchField *self) {
  return self->delegate();
}

//  void QQuickSearchField::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField11setDelegateEP13QQmlComponent(
    QQuickSearchField *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QString QQuickSearchField::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickSearchField15placeholderTextEv(
    const QQuickSearchField *self) {
  return new QString(self->placeholderText());
}

//  void QQuickSearchField::setPlaceholderText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField18setPlaceholderTextERK7QString(
    QQuickSearchField *self,
    const QString *text) {
  self->setPlaceholderText(*text);
}

//  bool QQuickSearchField::selectTextByMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickSearchField17selectTextByMouseEv(
    const QQuickSearchField *self) {
  return self->selectTextByMouse();
}

//  void QQuickSearchField::setSelectTextByMouse(const bool selectable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField20setSelectTextByMouseEb(
    QQuickSearchField *self,
    bool selectable) {
  self->setSelectTextByMouse(selectable);
}

//  QString QQuickSearchField::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickSearchField12selectedTextEv(
    const QQuickSearchField *self) {
  return new QString(self->selectedText());
}

//  int QQuickSearchField::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField14selectionStartEv(
    const QQuickSearchField *self) {
  return self->selectionStart();
}

//  int QQuickSearchField::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField12selectionEndEv(
    const QQuickSearchField *self) {
  return self->selectionEnd();
}

//  int QQuickSearchField::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickSearchField14cursorPositionEv(
    const QQuickSearchField *self) {
  return self->cursorPosition();
}

//  void QQuickSearchField::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField17setCursorPositionEi(
    QQuickSearchField *self,
    int position) {
  self->setCursorPosition(position);
}

//  void QQuickSearchField::select(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField6selectEii(
    QQuickSearchField *self,
    int start,
    int end) {
  self->select(start, end);
}

//  void QQuickSearchField::selectWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField10selectWordEv(QQuickSearchField *self) {
  self->selectWord();
}

//  void QQuickSearchField::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField9selectAllEv(QQuickSearchField *self) {
  self->selectAll();
}

//  void QQuickSearchField::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField8deselectEv(QQuickSearchField *self) {
  self->deselect();
}

//  void QQuickSearchField::activated(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField9activatedEi(
    QQuickSearchField *self,
    int index) {
  self->activated(index);
}

//  void QQuickSearchField::highlighted(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField11highlightedEi(
    QQuickSearchField *self,
    int index) {
  self->highlighted(index);
}

//  void QQuickSearchField::accepted()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField8acceptedEv(QQuickSearchField *self) {
  self->accepted();
}

//  void QQuickSearchField::searchTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15searchTriggeredEv(
    QQuickSearchField *self) {
  self->searchTriggered();
}

//  void QQuickSearchField::textEdited()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField10textEditedEv(QQuickSearchField *self) {
  self->textEdited();
}

//  void QQuickSearchField::suggestionModelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField22suggestionModelChangedEv(
    QQuickSearchField *self) {
  self->suggestionModelChanged();
}

//  void QQuickSearchField::delegateModelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField20delegateModelChangedEv(
    QQuickSearchField *self) {
  self->delegateModelChanged();
}

//  void QQuickSearchField::suggestionCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField22suggestionCountChangedEv(
    QQuickSearchField *self) {
  self->suggestionCountChanged();
}

//  void QQuickSearchField::currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField19currentIndexChangedEv(
    QQuickSearchField *self) {
  self->currentIndexChanged();
}

//  void QQuickSearchField::highlightedIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField23highlightedIndexChangedEv(
    QQuickSearchField *self) {
  self->highlightedIndexChanged();
}

//  void QQuickSearchField::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField11textChangedEv(QQuickSearchField *self) {
  self->textChanged();
}

//  void QQuickSearchField::textRoleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15textRoleChangedEv(
    QQuickSearchField *self) {
  self->textRoleChanged();
}

//  void QQuickSearchField::liveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField11liveChangedEv(QQuickSearchField *self) {
  self->liveChanged();
}

//  void QQuickSearchField::popupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField12popupChangedEv(QQuickSearchField *self) {
  self->popupChanged();
}

//  void QQuickSearchField::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15delegateChangedEv(
    QQuickSearchField *self) {
  self->delegateChanged();
}

//  void QQuickSearchField::placeholderTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField22placeholderTextChangedEv(
    QQuickSearchField *self) {
  self->placeholderTextChanged();
}

//  void QQuickSearchField::selectTextByMouseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField24selectTextByMouseChangedEv(
    QQuickSearchField *self) {
  self->selectTextByMouseChanged();
}

//  void QQuickSearchField::selectedTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField19selectedTextChangedEv(
    QQuickSearchField *self) {
  self->selectedTextChanged();
}

//  void QQuickSearchField::selectionStartChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField21selectionStartChangedEv(
    QQuickSearchField *self) {
  self->selectionStartChanged();
}

//  void QQuickSearchField::selectionEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField19selectionEndChangedEv(
    QQuickSearchField *self) {
  self->selectionEndChanged();
}

//  void QQuickSearchField::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField21cursorPositionChangedEv(
    QQuickSearchField *self) {
  self->cursorPositionChanged();
}

//  void QQuickSearchField::searchButtonPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField19searchButtonPressedEv(
    QQuickSearchField *self) {
  self->searchButtonPressed();
}

//  void QQuickSearchField::clearButtonPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField18clearButtonPressedEv(
    QQuickSearchField *self) {
  self->clearButtonPressed();
}

//  bool QQuickSearchField::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickSearchField11eventFilterEP7QObjectP6QEvent(
    QQuickSearchField *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QQuickSearchField::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField12focusInEventEP11QFocusEvent(
    QQuickSearchField *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickSearchField::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField13focusOutEventEP11QFocusEvent(
    QQuickSearchField *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickSearchField::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15hoverEnterEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickSearchField::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField14hoverMoveEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickSearchField::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField15hoverLeaveEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickSearchField::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField13keyPressEventEP9QKeyEvent(
    QQuickSearchField *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickSearchField::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField10classBeginEv(QQuickSearchField *self) {
  self->classBegin();
}

//  void QQuickSearchField::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField17componentCompleteEv(
    QQuickSearchField *self) {
  self->componentComplete();
}

//  void QQuickSearchField::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField17contentItemChangeEP10QQuickItemS1_(
    QQuickSearchField *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickSearchField::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickSearchField10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickSearchField *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickSearchFieldPrivate *QQuickSearchField::d_func()
extern "C" Q_DECL_EXPORT
QQuickSearchFieldPrivate *ritual_ZN17QQuickSearchField6d_funcEv(
    QQuickSearchField *self) {
  return self->d_func();
}

//  const QQuickSearchFieldPrivate *QQuickSearchField::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSearchFieldPrivate *ritual_ZNK17QQuickSearchField6d_funcEv(
    const QQuickSearchField *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickSearchField, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSearchField(
    QQuickSearchField *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSearchField *>(self)->take(key, call);
}

//  bool QQuickSearchField::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickSearchField11eventFilterEP7QObjectP6QEvent(
    QQuickSearchField *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::eventFilter(
      object,
      event);
}

//  void QQuickSearchField::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField12focusInEventEP11QFocusEvent(
    QQuickSearchField *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::focusInEvent(
      event);
}

//  void QQuickSearchField::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField13focusOutEventEP11QFocusEvent(
    QQuickSearchField *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::focusOutEvent(
      event);
}

//  void QQuickSearchField::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField15hoverEnterEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::hoverEnterEvent(
      event);
}

//  void QQuickSearchField::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField14hoverMoveEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::hoverMoveEvent(
      event);
}

//  void QQuickSearchField::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField15hoverLeaveEventEP11QHoverEvent(
    QQuickSearchField *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::hoverLeaveEvent(
      event);
}

//  void QQuickSearchField::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField13keyPressEventEP9QKeyEvent(
    QQuickSearchField *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::keyPressEvent(
      event);
}

//  void QQuickSearchField::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField10classBeginEv(
    QQuickSearchField *self) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::classBegin();
}

//  void QQuickSearchField::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField17componentCompleteEv(
    QQuickSearchField *self) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::componentComplete();
}

//  void QQuickSearchField::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField17contentItemChangeEP10QQuickItemS1_(
    QQuickSearchField *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickSearchField::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickSearchField10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickSearchField *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickSearchField *>(self)->OwnQQuickSearchField::itemChange(
      change,
      *data);
}
