//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlocale.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickPopup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPopup : QQuickPopup {
  using QQuickPopup::classBegin;
  using QQuickPopup::componentComplete;
  using QQuickPopup::childMouseEventFilter;
  using QQuickPopup::focusInEvent;
  using QQuickPopup::focusOutEvent;
  using QQuickPopup::keyPressEvent;
  using QQuickPopup::keyReleaseEvent;
  using QQuickPopup::mousePressEvent;
  using QQuickPopup::mouseMoveEvent;
  using QQuickPopup::mouseReleaseEvent;
  using QQuickPopup::mouseDoubleClickEvent;
  using QQuickPopup::mouseUngrabEvent;
  using QQuickPopup::overlayEvent;
  using QQuickPopup::touchEvent;
  using QQuickPopup::touchUngrabEvent;
  using QQuickPopup::wheelEvent;
  using QQuickPopup::dragEnterEvent;
  using QQuickPopup::dragMoveEvent;
  using QQuickPopup::dragLeaveEvent;
  using QQuickPopup::dropEvent;
  using QQuickPopup::contentItemChange;
  using QQuickPopup::contentSizeChange;
  using QQuickPopup::fontChange;
  using QQuickPopup::geometryChange;
  using QQuickPopup::localeChange;
  using QQuickPopup::itemChange;
  using QQuickPopup::marginsChange;
  using QQuickPopup::paddingChange;
  using QQuickPopup::spacingChange;
  using QQuickPopup::insetChange;
  using QQuickPopup::defaultFont;
  using QQuickPopup::accessibilityActiveChanged;
};

//  A QQuickPopup that Python can take functions over in. Every QQuickPopup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPopupCall0)(const void *, int *);
typedef void (*CuteQQuickPopupCall1)(const void *, bool, int *);
typedef void (*CuteQQuickPopupCall2)(const void *, qreal, int *);
typedef void (*CuteQQuickPopupCall3)(const void *, int *);
typedef void (*CuteQQuickPopupCall4)(const void *, int *);
typedef bool (*CuteQQuickPopupCall5)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickPopupCall6)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPopupCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPopupCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPopupCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPopupCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPopupCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPopupCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPopupCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPopupCall14)(const void *, int *);
typedef bool (*CuteQQuickPopupCall15)(const void *, QQuickItem *, QEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPopupCall16)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickPopupCall17)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPopupCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPopupCall19)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPopupCall20)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPopupCall21)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPopupCall22)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPopupCall23)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupCall24)(const void *, const QSizeF *, const QSizeF *, int *);
typedef void (*CuteQQuickPopupCall25)(const void *, const QFont *, const QFont *, int *);
typedef void (*CuteQQuickPopupCall26)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPopupCall27)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickPopupCall28)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPopupCall29)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPopupCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickPopupCall31)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickPopupCall32)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef const QFont * (*CuteQQuickPopupCall33)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPopupCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickPopupCall35)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void * (*CuteQQuickPopupCall36)(const void *, int *);
typedef void * (*CuteQQuickPopupCall37)(const void *, int *);
typedef void * (*CuteQQuickPopupCall38)(const void *, const QMetaObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPopupCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPopupCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPopup : public QQuickPopup {
public:
  using QQuickPopup::QQuickPopup;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QQuickPopup9isVisibleEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10setOpacityEd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12focusInEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13focusOutEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup16mouseUngrabEventEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup10touchEventEP11QTouchEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup16touchUngrabEventEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN11QQuickPopup10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup9dropEventEP10QDropEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10fontChangeERK5QFontS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14geometryChangeERK6QRectFS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12localeChangeERK7QLocaleS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13spacingChangeEdd")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QQuickPopup11defaultFontEv")) {
      taken[33] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK11QQuickPopup14accessibleRoleEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QQuickPopup26accessibilityActiveChangedEb")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QQuickSafeAreaAttachable22safeAreaAttachmentItemEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK11QMetaObject")) {
      taken[38] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickPopup::isVisible() const
  bool isVisible() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPopupCall0 call = reinterpret_cast<CuteQQuickPopupCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopup::isVisible();
  }

  //  void QQuickPopup::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPopupCall1 call = reinterpret_cast<CuteQQuickPopupCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickPopup::setVisible(visible);
  }

  //  void QQuickPopup::setOpacity(qreal opacity)
  void setOpacity(qreal opacity) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPopupCall2 call = reinterpret_cast<CuteQQuickPopupCall2>(taken[2]);
      call(this, opacity, &handled);
      if (handled) return;
    }
    QQuickPopup::setOpacity(opacity);
  }

  //  void QQuickPopup::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPopupCall3 call = reinterpret_cast<CuteQQuickPopupCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::classBegin();
  }

  //  void QQuickPopup::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPopupCall4 call = reinterpret_cast<CuteQQuickPopupCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::componentComplete();
  }

  //  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *child, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPopupCall5 call = reinterpret_cast<CuteQQuickPopupCall5>(taken[5]);
      bool given = call(this, child, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::childMouseEventFilter(child, event);
  }

  //  void QQuickPopup::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPopupCall6 call = reinterpret_cast<CuteQQuickPopupCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusInEvent(event);
  }

  //  void QQuickPopup::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPopupCall7 call = reinterpret_cast<CuteQQuickPopupCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusOutEvent(event);
  }

  //  void QQuickPopup::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPopupCall8 call = reinterpret_cast<CuteQQuickPopupCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::keyPressEvent(event);
  }

  //  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPopupCall9 call = reinterpret_cast<CuteQQuickPopupCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::keyReleaseEvent(event);
  }

  //  void QQuickPopup::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPopupCall10 call = reinterpret_cast<CuteQQuickPopupCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mousePressEvent(event);
  }

  //  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPopupCall11 call = reinterpret_cast<CuteQQuickPopupCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseMoveEvent(event);
  }

  //  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPopupCall12 call = reinterpret_cast<CuteQQuickPopupCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseReleaseEvent(event);
  }

  //  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPopupCall13 call = reinterpret_cast<CuteQQuickPopupCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseDoubleClickEvent(event);
  }

  //  void QQuickPopup::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPopupCall14 call = reinterpret_cast<CuteQQuickPopupCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseUngrabEvent();
  }

  //  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
  bool overlayEvent(QQuickItem *item, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPopupCall15 call = reinterpret_cast<CuteQQuickPopupCall15>(taken[15]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::overlayEvent(item, event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPopupCall16 call = reinterpret_cast<CuteQQuickPopupCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPopupCall17 call = reinterpret_cast<CuteQQuickPopupCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickPopup::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPopupCall18 call = reinterpret_cast<CuteQQuickPopupCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPopupCall19 call = reinterpret_cast<CuteQQuickPopupCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPopupCall20 call = reinterpret_cast<CuteQQuickPopupCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPopupCall21 call = reinterpret_cast<CuteQQuickPopupCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPopupCall22 call = reinterpret_cast<CuteQQuickPopupCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dropEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  void QQuickPopup::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPopupCall23 call = reinterpret_cast<CuteQQuickPopupCall23>(taken[23]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickPopup::contentItemChange(newItem, oldItem);
  }

  //  void QQuickPopup::contentSizeChange(const QSizeF &newSize, const
  //      QSizeF &oldSize)
  void contentSizeChange(
      const QSizeF &newSize,
      const QSizeF &oldSize) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPopupCall24 call = reinterpret_cast<CuteQQuickPopupCall24>(taken[24]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPopup::contentSizeChange(newSize, oldSize);
  }

  //  void QQuickPopup::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPopupCall25 call = reinterpret_cast<CuteQQuickPopupCall25>(taken[25]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickPopup::fontChange(newFont, oldFont);
  }

  //  void QQuickPopup::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPopupCall26 call = reinterpret_cast<CuteQQuickPopupCall26>(taken[26]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickPopup::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickPopup::localeChange(const QLocale &newLocale, const
  //      QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPopupCall27 call = reinterpret_cast<CuteQQuickPopupCall27>(taken[27]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickPopup::localeChange(newLocale, oldLocale);
  }

  //  void QQuickPopup::itemChange(QQuickItem::ItemChange change, const
  //      QQuickItem::ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPopupCall28 call = reinterpret_cast<CuteQQuickPopupCall28>(taken[28]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickPopup::itemChange(change, data);
  }

  //  void QQuickPopup::marginsChange(const QMarginsF &newMargins, const
  //      QMarginsF &oldMargins)
  void marginsChange(
      const QMarginsF &newMargins,
      const QMarginsF &oldMargins) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPopupCall29 call = reinterpret_cast<CuteQQuickPopupCall29>(taken[29]);
      call(this, &newMargins, &oldMargins, &handled);
      if (handled) return;
    }
    QQuickPopup::marginsChange(newMargins, oldMargins);
  }

  //  void QQuickPopup::paddingChange(const QMarginsF &newPadding, const
  //      QMarginsF &oldPadding)
  void paddingChange(
      const QMarginsF &newPadding,
      const QMarginsF &oldPadding) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPopupCall30 call = reinterpret_cast<CuteQQuickPopupCall30>(taken[30]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickPopup::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickPopupCall31 call = reinterpret_cast<CuteQQuickPopupCall31>(taken[31]);
      call(this, newSpacing, oldSpacing, &handled);
      if (handled) return;
    }
    QQuickPopup::spacingChange(newSpacing, oldSpacing);
  }

  //  void QQuickPopup::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickPopupCall32 call = reinterpret_cast<CuteQQuickPopupCall32>(taken[32]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickPopup::insetChange(newInset, oldInset);
  }

  //  QFont QQuickPopup::defaultFont() const
  QFont defaultFont() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickPopupCall33 call = reinterpret_cast<CuteQQuickPopupCall33>(taken[33]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopup::defaultFont();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickPopup::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickPopupCall34 call = reinterpret_cast<CuteQQuickPopupCall34>(taken[34]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickPopup::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QQuickPopup::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPopupCall35 call = reinterpret_cast<CuteQQuickPopupCall35>(taken[35]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickPopup::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
  QQuickItem *safeAreaAttachmentItem() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPopupCall36 call = reinterpret_cast<CuteQQuickPopupCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPopup::safeAreaAttachmentItem();
  }

  //  QQuickItem *QQuickPopup::attacheeItem() const
  QQuickItem *attacheeItem() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickPopupCall37 call = reinterpret_cast<CuteQQuickPopupCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPopup::attacheeItem();
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickPopup::attachedParent(const QMetaObject *attachedType)
  //      const
  QtPrivate::QQuickAttachedPropertyPropagator *attachedParent(
      const QMetaObject *attachedType) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickPopupCall38 call = reinterpret_cast<CuteQQuickPopupCall38>(taken[38]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickPopup::attachedParent(attachedType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickPopupCall39 call = reinterpret_cast<CuteQQuickPopupCall39>(taken[39]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickPopupCall40 call = reinterpret_cast<CuteQQuickPopupCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickPopupCall41 call = reinterpret_cast<CuteQQuickPopupCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickPopupCall42 call = reinterpret_cast<CuteQQuickPopupCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickPopupCall43 call = reinterpret_cast<CuteQQuickPopupCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickPopupCall44 call = reinterpret_cast<CuteQQuickPopupCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickPopupCall45 call = reinterpret_cast<CuteQQuickPopupCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPopup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickPopup10metaObjectEv(
    const QQuickPopup *self) {
  return self->metaObject();
}

//  QString QQuickPopup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickPopup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPopup::tr(s, c, n));
}

//  QQuickPopup::QQuickPopup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZN11QQuickPopupC1EP7QObject(QObject *parent) {
  return new CuteQQuickPopup(parent);
}

//  QQuickPopup::~QQuickPopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopupD1Ev(QQuickPopup *self) {
  delete self;
}

//  qreal QQuickPopup::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup1xEv(const QQuickPopup *self) {
  return self->x();
}

//  void QQuickPopup::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup4setXEd(QQuickPopup *self, qreal x) {
  self->setX(x);
}

//  qreal QQuickPopup::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup1yEv(const QQuickPopup *self) {
  return self->y();
}

//  void QQuickPopup::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup4setYEd(QQuickPopup *self, qreal y) {
  self->setY(y);
}

//  QPointF QQuickPopup::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QQuickPopup8positionEv(const QQuickPopup *self) {
  return new QPointF(self->position());
}

//  void QQuickPopup::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup11setPositionERK7QPointF(
    QQuickPopup *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  qreal QQuickPopup::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup1zEv(const QQuickPopup *self) {
  return self->z();
}

//  void QQuickPopup::setZ(qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup4setZEd(QQuickPopup *self, qreal z) {
  self->setZ(z);
}

//  void QQuickPopup::resetZ()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup6resetZEv(QQuickPopup *self) {
  self->resetZ();
}

//  qreal QQuickPopup::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup5widthEv(const QQuickPopup *self) {
  return self->width();
}

//  void QQuickPopup::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8setWidthEd(QQuickPopup *self, qreal width) {
  self->setWidth(width);
}

//  void QQuickPopup::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10resetWidthEv(QQuickPopup *self) {
  self->resetWidth();
}

//  qreal QQuickPopup::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup6heightEv(const QQuickPopup *self) {
  return self->height();
}

//  void QQuickPopup::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup9setHeightEd(QQuickPopup *self, qreal height) {
  self->setHeight(height);
}

//  void QQuickPopup::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup11resetHeightEv(QQuickPopup *self) {
  self->resetHeight();
}

//  qreal QQuickPopup::implicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup13implicitWidthEv(const QQuickPopup *self) {
  return self->implicitWidth();
}

//  void QQuickPopup::setImplicitWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16setImplicitWidthEd(
    QQuickPopup *self,
    qreal width) {
  self->setImplicitWidth(width);
}

//  qreal QQuickPopup::implicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup14implicitHeightEv(const QQuickPopup *self) {
  return self->implicitHeight();
}

//  void QQuickPopup::setImplicitHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17setImplicitHeightEd(
    QQuickPopup *self,
    qreal height) {
  self->setImplicitHeight(height);
}

//  qreal QQuickPopup::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup12contentWidthEv(const QQuickPopup *self) {
  return self->contentWidth();
}

//  void QQuickPopup::setContentWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15setContentWidthEd(
    QQuickPopup *self,
    qreal width) {
  self->setContentWidth(width);
}

//  qreal QQuickPopup::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup13contentHeightEv(const QQuickPopup *self) {
  return self->contentHeight();
}

//  void QQuickPopup::setContentHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16setContentHeightEd(
    QQuickPopup *self,
    qreal height) {
  self->setContentHeight(height);
}

//  qreal QQuickPopup::availableWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup14availableWidthEv(const QQuickPopup *self) {
  return self->availableWidth();
}

//  qreal QQuickPopup::availableHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup15availableHeightEv(const QQuickPopup *self) {
  return self->availableHeight();
}

//  qreal QQuickPopup::margins() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup7marginsEv(const QQuickPopup *self) {
  return self->margins();
}

//  void QQuickPopup::setMargins(qreal margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setMarginsEd(QQuickPopup *self, qreal margins) {
  self->setMargins(margins);
}

//  void QQuickPopup::resetMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12resetMarginsEv(QQuickPopup *self) {
  self->resetMargins();
}

//  qreal QQuickPopup::topMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup9topMarginEv(const QQuickPopup *self) {
  return self->topMargin();
}

//  void QQuickPopup::setTopMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12setTopMarginEd(
    QQuickPopup *self,
    qreal margin) {
  self->setTopMargin(margin);
}

//  void QQuickPopup::resetTopMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14resetTopMarginEv(QQuickPopup *self) {
  self->resetTopMargin();
}

//  qreal QQuickPopup::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup10leftMarginEv(const QQuickPopup *self) {
  return self->leftMargin();
}

//  void QQuickPopup::setLeftMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13setLeftMarginEd(
    QQuickPopup *self,
    qreal margin) {
  self->setLeftMargin(margin);
}

//  void QQuickPopup::resetLeftMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15resetLeftMarginEv(QQuickPopup *self) {
  self->resetLeftMargin();
}

//  qreal QQuickPopup::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup11rightMarginEv(const QQuickPopup *self) {
  return self->rightMargin();
}

//  void QQuickPopup::setRightMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14setRightMarginEd(
    QQuickPopup *self,
    qreal margin) {
  self->setRightMargin(margin);
}

//  void QQuickPopup::resetRightMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16resetRightMarginEv(QQuickPopup *self) {
  self->resetRightMargin();
}

//  qreal QQuickPopup::bottomMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup12bottomMarginEv(const QQuickPopup *self) {
  return self->bottomMargin();
}

//  void QQuickPopup::setBottomMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15setBottomMarginEd(
    QQuickPopup *self,
    qreal margin) {
  self->setBottomMargin(margin);
}

//  void QQuickPopup::resetBottomMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17resetBottomMarginEv(QQuickPopup *self) {
  self->resetBottomMargin();
}

//  qreal QQuickPopup::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup7paddingEv(const QQuickPopup *self) {
  return self->padding();
}

//  void QQuickPopup::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setPaddingEd(QQuickPopup *self, qreal padding) {
  self->setPadding(padding);
}

//  void QQuickPopup::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12resetPaddingEv(QQuickPopup *self) {
  self->resetPadding();
}

//  qreal QQuickPopup::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup10topPaddingEv(const QQuickPopup *self) {
  return self->topPadding();
}

//  void QQuickPopup::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13setTopPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickPopup::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15resetTopPaddingEv(QQuickPopup *self) {
  self->resetTopPadding();
}

//  qreal QQuickPopup::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup11leftPaddingEv(const QQuickPopup *self) {
  return self->leftPadding();
}

//  void QQuickPopup::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14setLeftPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickPopup::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16resetLeftPaddingEv(QQuickPopup *self) {
  self->resetLeftPadding();
}

//  qreal QQuickPopup::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup12rightPaddingEv(const QQuickPopup *self) {
  return self->rightPadding();
}

//  void QQuickPopup::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15setRightPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickPopup::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17resetRightPaddingEv(QQuickPopup *self) {
  self->resetRightPadding();
}

//  qreal QQuickPopup::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup13bottomPaddingEv(const QQuickPopup *self) {
  return self->bottomPadding();
}

//  void QQuickPopup::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16setBottomPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickPopup::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup18resetBottomPaddingEv(QQuickPopup *self) {
  self->resetBottomPadding();
}

//  QLocale QQuickPopup::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK11QQuickPopup6localeEv(const QQuickPopup *self) {
  return new QLocale(self->locale());
}

//  void QQuickPopup::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup9setLocaleERK7QLocale(
    QQuickPopup *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QQuickPopup::resetLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup11resetLocaleEv(QQuickPopup *self) {
  self->resetLocale();
}

//  QFont QQuickPopup::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QQuickPopup4fontEv(const QQuickPopup *self) {
  return new QFont(self->font());
}

//  void QQuickPopup::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup7setFontERK5QFont(
    QQuickPopup *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QQuickPopup::resetFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup9resetFontEv(QQuickPopup *self) {
  self->resetFont();
}

//  QQuickWindow *QQuickPopup::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK11QQuickPopup6windowEv(const QQuickPopup *self) {
  return self->window();
}

//  QQuickItem *QQuickPopup::popupItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup9popupItemEv(const QQuickPopup *self) {
  return self->popupItem();
}

//  QQuickItem *QQuickPopup::parentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup10parentItemEv(const QQuickPopup *self) {
  return self->parentItem();
}

//  void QQuickPopup::setParentItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13setParentItemEP10QQuickItem(
    QQuickPopup *self,
    QQuickItem *parent) {
  self->setParentItem(parent);
}

//  void QQuickPopup::resetParentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15resetParentItemEv(QQuickPopup *self) {
  self->resetParentItem();
}

//  QQuickItem *QQuickPopup::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup10backgroundEv(const QQuickPopup *self) {
  return self->background();
}

//  void QQuickPopup::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13setBackgroundEP10QQuickItem(
    QQuickPopup *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  QQuickItem *QQuickPopup::contentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup11contentItemEv(const QQuickPopup *self) {
  return self->contentItem();
}

//  void QQuickPopup::setContentItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14setContentItemEP10QQuickItem(
    QQuickPopup *self,
    QQuickItem *item) {
  self->setContentItem(item);
}

//  bool QQuickPopup::clip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup4clipEv(const QQuickPopup *self) {
  return self->clip();
}

//  void QQuickPopup::setClip(bool clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup7setClipEb(QQuickPopup *self, bool clip) {
  self->setClip(clip);
}

//  bool QQuickPopup::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup8hasFocusEv(const QQuickPopup *self) {
  return self->hasFocus();
}

//  void QQuickPopup::setFocus(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8setFocusEb(QQuickPopup *self, bool focus) {
  self->setFocus(focus);
}

//  bool QQuickPopup::hasActiveFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup14hasActiveFocusEv(const QQuickPopup *self) {
  return self->hasActiveFocus();
}

//  bool QQuickPopup::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup7isModalEv(const QQuickPopup *self) {
  return self->isModal();
}

//  void QQuickPopup::setModal(bool modal)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8setModalEb(QQuickPopup *self, bool modal) {
  self->setModal(modal);
}

//  bool QQuickPopup::dim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup3dimEv(const QQuickPopup *self) {
  return self->dim();
}

//  void QQuickPopup::setDim(bool dim)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup6setDimEb(QQuickPopup *self, bool dim) {
  self->setDim(dim);
}

//  void QQuickPopup::resetDim()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8resetDimEv(QQuickPopup *self) {
  self->resetDim();
}

//  bool QQuickPopup::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup9isVisibleEv(const QQuickPopup *self) {
  return self->isVisible();
}

//  void QQuickPopup::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setVisibleEb(QQuickPopup *self, bool visible) {
  self->setVisible(visible);
}

//  qreal QQuickPopup::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup7opacityEv(const QQuickPopup *self) {
  return self->opacity();
}

//  void QQuickPopup::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setOpacityEd(QQuickPopup *self, qreal opacity) {
  self->setOpacity(opacity);
}

//  qreal QQuickPopup::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup5scaleEv(const QQuickPopup *self) {
  return self->scale();
}

//  void QQuickPopup::setScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8setScaleEd(QQuickPopup *self, qreal scale) {
  self->setScale(scale);
}

//  ClosePolicy QQuickPopup::closePolicy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QQuickPopup11closePolicyEv(const QQuickPopup *self) {
  return static_cast<int>(self->closePolicy().toInt());
}

//  void QQuickPopup::setClosePolicy(ClosePolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14setClosePolicyE6QFlagsINS_15ClosePolicyFlagEE(
    QQuickPopup *self,
    int policy) {
  self->setClosePolicy(
      QFlags<QQuickPopup::ClosePolicyFlag>::fromInt(policy));
}

//  void QQuickPopup::resetClosePolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16resetClosePolicyEv(QQuickPopup *self) {
  self->resetClosePolicy();
}

//  TransformOrigin QQuickPopup::transformOrigin() const
extern "C" Q_DECL_EXPORT
QQuickPopup::TransformOrigin ritual_ZNK11QQuickPopup15transformOriginEv(
    const QQuickPopup *self) {
  return self->transformOrigin();
}

//  void QQuickPopup::setTransformOrigin(TransformOrigin a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup18setTransformOriginENS_15TransformOriginE(
    QQuickPopup *self,
    QQuickPopup::TransformOrigin a0) {
  self->setTransformOrigin(a0);
}

//  QQuickTransition *QQuickPopup::enter() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK11QQuickPopup5enterEv(const QQuickPopup *self) {
  return self->enter();
}

//  void QQuickPopup::setEnter(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup8setEnterEP16QQuickTransition(
    QQuickPopup *self,
    QQuickTransition *transition) {
  self->setEnter(transition);
}

//  QQuickTransition *QQuickPopup::exit() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK11QQuickPopup4exitEv(const QQuickPopup *self) {
  return self->exit();
}

//  void QQuickPopup::setExit(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup7setExitEP16QQuickTransition(
    QQuickPopup *self,
    QQuickTransition *transition) {
  self->setExit(transition);
}

//  bool QQuickPopup::filtersChildMouseEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup23filtersChildMouseEventsEv(
    const QQuickPopup *self) {
  return self->filtersChildMouseEvents();
}

//  void QQuickPopup::setFiltersChildMouseEvents(bool filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup26setFiltersChildMouseEventsEb(
    QQuickPopup *self,
    bool filter) {
  self->setFiltersChildMouseEvents(filter);
}

//  void QQuickPopup::forceActiveFocus(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16forceActiveFocusEN2Qt11FocusReasonE(
    QQuickPopup *self,
    Qt::FocusReason reason) {
  self->forceActiveFocus(reason);
}

//  qreal QQuickPopup::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup7spacingEv(const QQuickPopup *self) {
  return self->spacing();
}

//  void QQuickPopup::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setSpacingEd(QQuickPopup *self, qreal spacing) {
  self->setSpacing(spacing);
}

//  void QQuickPopup::resetSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12resetSpacingEv(QQuickPopup *self) {
  self->resetSpacing();
}

//  bool QQuickPopup::isOpened() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup8isOpenedEv(const QQuickPopup *self) {
  return self->isOpened();
}

//  bool QQuickPopup::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup10isMirroredEv(const QQuickPopup *self) {
  return self->isMirrored();
}

//  bool QQuickPopup::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup9isEnabledEv(const QQuickPopup *self) {
  return self->isEnabled();
}

//  void QQuickPopup::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10setEnabledEb(QQuickPopup *self, bool enabled) {
  self->setEnabled(enabled);
}

//  qreal QQuickPopup::horizontalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup17horizontalPaddingEv(const QQuickPopup *self) {
  return self->horizontalPadding();
}

//  void QQuickPopup::setHorizontalPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup20setHorizontalPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setHorizontalPadding(padding);
}

//  void QQuickPopup::resetHorizontalPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup22resetHorizontalPaddingEv(QQuickPopup *self) {
  self->resetHorizontalPadding();
}

//  qreal QQuickPopup::verticalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup15verticalPaddingEv(const QQuickPopup *self) {
  return self->verticalPadding();
}

//  void QQuickPopup::setVerticalPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup18setVerticalPaddingEd(
    QQuickPopup *self,
    qreal padding) {
  self->setVerticalPadding(padding);
}

//  void QQuickPopup::resetVerticalPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup20resetVerticalPaddingEv(QQuickPopup *self) {
  self->resetVerticalPadding();
}

//  qreal QQuickPopup::implicitContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup20implicitContentWidthEv(
    const QQuickPopup *self) {
  return self->implicitContentWidth();
}

//  qreal QQuickPopup::implicitContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup21implicitContentHeightEv(
    const QQuickPopup *self) {
  return self->implicitContentHeight();
}

//  qreal QQuickPopup::implicitBackgroundWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup23implicitBackgroundWidthEv(
    const QQuickPopup *self) {
  return self->implicitBackgroundWidth();
}

//  qreal QQuickPopup::implicitBackgroundHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup24implicitBackgroundHeightEv(
    const QQuickPopup *self) {
  return self->implicitBackgroundHeight();
}

//  qreal QQuickPopup::topInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup8topInsetEv(const QQuickPopup *self) {
  return self->topInset();
}

//  void QQuickPopup::setTopInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup11setTopInsetEd(QQuickPopup *self, qreal inset) {
  self->setTopInset(inset);
}

//  void QQuickPopup::resetTopInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13resetTopInsetEv(QQuickPopup *self) {
  self->resetTopInset();
}

//  qreal QQuickPopup::leftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup9leftInsetEv(const QQuickPopup *self) {
  return self->leftInset();
}

//  void QQuickPopup::setLeftInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12setLeftInsetEd(QQuickPopup *self, qreal inset) {
  self->setLeftInset(inset);
}

//  void QQuickPopup::resetLeftInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14resetLeftInsetEv(QQuickPopup *self) {
  self->resetLeftInset();
}

//  qreal QQuickPopup::rightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup10rightInsetEv(const QQuickPopup *self) {
  return self->rightInset();
}

//  void QQuickPopup::setRightInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13setRightInsetEd(
    QQuickPopup *self,
    qreal inset) {
  self->setRightInset(inset);
}

//  void QQuickPopup::resetRightInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15resetRightInsetEv(QQuickPopup *self) {
  self->resetRightInset();
}

//  qreal QQuickPopup::bottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickPopup11bottomInsetEv(const QQuickPopup *self) {
  return self->bottomInset();
}

//  void QQuickPopup::setBottomInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14setBottomInsetEd(
    QQuickPopup *self,
    qreal inset) {
  self->setBottomInset(inset);
}

//  void QQuickPopup::resetBottomInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16resetBottomInsetEv(QQuickPopup *self) {
  self->resetBottomInset();
}

//  PopupType QQuickPopup::popupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_ZNK11QQuickPopup9popupTypeEv(
    const QQuickPopup *self) {
  return self->popupType();
}

//  void QQuickPopup::setPopupType(PopupType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12setPopupTypeENS_9PopupTypeE(
    QQuickPopup *self,
    QQuickPopup::PopupType a0) {
  self->setPopupType(a0);
}

//  void QQuickPopup::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup4openEv(QQuickPopup *self) {
  self->open();
}

//  void QQuickPopup::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup5closeEv(QQuickPopup *self) {
  self->close();
}

//  void QQuickPopup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10classBeginEv(QQuickPopup *self) {
  self->classBegin();
}

//  void QQuickPopup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17componentCompleteEv(QQuickPopup *self) {
  self->componentComplete();
}

//  bool QQuickPopup::isComponentComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickPopup19isComponentCompleteEv(
    const QQuickPopup *self) {
  return self->isComponentComplete();
}

//  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPopup *self,
    QQuickItem *child,
    QEvent *event) {
  return self->childMouseEventFilter(child, event);
}

//  void QQuickPopup::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12focusInEventEP11QFocusEvent(
    QQuickPopup *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickPopup::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13focusOutEventEP11QFocusEvent(
    QQuickPopup *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickPopup::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13keyPressEventEP9QKeyEvent(
    QQuickPopup *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent(
    QQuickPopup *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickPopup::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup15mousePressEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickPopup::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16mouseUngrabEventEv(QQuickPopup *self) {
  self->mouseUngrabEvent();
}

//  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent(
    QQuickPopup *self,
    QQuickItem *item,
    QEvent *event) {
  return self->overlayEvent(item, event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopup::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10touchEventEP11QTouchEvent(
    QQuickPopup *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopup::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup16touchUngrabEventEv(QQuickPopup *self) {
  self->touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickPopup::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10wheelEventEP11QWheelEvent(
    QQuickPopup *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent(
    QQuickPopup *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent(
    QQuickPopup *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent(
    QQuickPopup *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup9dropEventEP10QDropEvent(
    QQuickPopup *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickPopup::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_(
    QQuickPopup *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickPopup::contentSizeChange(const QSizeF &newSize, const QSizeF
//      &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_(
    QQuickPopup *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  self->contentSizeChange(*newSize, *oldSize);
}

//  void QQuickPopup::fontChange(const QFont &newFont, const QFont &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10fontChangeERK5QFontS2_(
    QQuickPopup *self,
    const QFont *newFont,
    const QFont *oldFont) {
  self->fontChange(*newFont, *oldFont);
}

//  void QQuickPopup::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup14geometryChangeERK6QRectFS2_(
    QQuickPopup *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickPopup::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup12localeChangeERK7QLocaleS2_(
    QQuickPopup *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickPopup::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPopup *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickPopup::marginsChange(const QMarginsF &newMargins, const
//      QMarginsF &oldMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newMargins,
    const QMarginsF *oldMargins) {
  self->marginsChange(*newMargins, *oldMargins);
}

//  void QQuickPopup::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup13spacingChangeEdd(
    QQuickPopup *self,
    qreal newSpacing,
    qreal oldSpacing) {
  self->spacingChange(newSpacing, oldSpacing);
}

//  void QQuickPopup::insetChange(const QMarginsF &newInset, const QMarginsF
//      &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  QFont QQuickPopup::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QQuickPopup11defaultFontEv(const QQuickPopup *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPopup::effectiveAccessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK11QQuickPopup23effectiveAccessibleRoleEv(
    const QQuickPopup *self) {
  return self->effectiveAccessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPopup::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK11QQuickPopup14accessibleRoleEv(
    const QQuickPopup *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPopup::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup26accessibilityActiveChangedEb(
    QQuickPopup *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QString QQuickPopup::accessibleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQuickPopup14accessibleNameEv(const QQuickPopup *self) {
  return new QString(self->accessibleName());
}

//  void QQuickPopup::maybeSetAccessibleName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickPopup22maybeSetAccessibleNameERK7QString(
    QQuickPopup *self,
    const QString *name) {
  self->maybeSetAccessibleName(*name);
}

//  QVariant QQuickPopup::accessibleProperty(const char *propertyName)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN11QQuickPopup18accessiblePropertyEPKc(
    QQuickPopup *self,
    const char *propertyName) {
  return new QVariant(self->accessibleProperty(propertyName));
}

//  bool QQuickPopup::setAccessibleProperty(const char *propertyName, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickPopup21setAccessiblePropertyEPKcRK8QVariant(
    QQuickPopup *self,
    const char *propertyName,
    const QVariant *value) {
  return self->setAccessibleProperty(propertyName, *value);
}

//  QQuickItem *QQuickPopup::findParentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup14findParentItemEv(
    const QQuickPopup *self) {
  return self->findParentItem();
}

//  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN11QQuickPopup22safeAreaAttachmentItemEv(
    QQuickPopup *self) {
  return self->safeAreaAttachmentItem();
}

//  QQuickItem *QQuickPopup::attacheeItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickPopup12attacheeItemEv(
    const QQuickPopup *self) {
  return self->attacheeItem();
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickPopup::attachedParent(const QMetaObject *attachedType) const
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZNK11QQuickPopup14attachedParentEPK11QMetaObject(
    const QQuickPopup *self,
    const QMetaObject *attachedType) {
  return self->attachedParent(attachedType);
}

//  QQuickPopupPrivate *QQuickPopup::d_func()
extern "C" Q_DECL_EXPORT
QQuickPopupPrivate *ritual_ZN11QQuickPopup6d_funcEv(QQuickPopup *self) {
  return self->d_func();
}

//  const QQuickPopupPrivate *QQuickPopup::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopupPrivate *ritual_ZNK11QQuickPopup6d_funcEv(
    const QQuickPopup *self) {
  return self->d_func();
}

//  QQuickPopup as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickPopup_QQmlParserStatus(
    QQuickPopup *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  QQuickPopup as the QQuickSafeAreaAttachable it is built on
extern "C" Q_DECL_EXPORT
QQuickSafeAreaAttachable *ritual_cast_QQuickPopup_QQuickSafeAreaAttachable(
    QQuickPopup *self) {
  return static_cast<QQuickSafeAreaAttachable *>(self);
}

//  QQuickPopup as the QQuickAttachedPropertyPropagatorTarget it is built on
extern "C" Q_DECL_EXPORT
QQuickAttachedPropertyPropagatorTarget *ritual_cast_QQuickPopup_QQuickAttachedPropertyPropagatorTarget(
    QQuickPopup *self) {
  return static_cast<QQuickAttachedPropertyPropagatorTarget *>(self);
}

//  a Python function taken by a CuteQQuickPopup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPopup(
    QQuickPopup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPopup *>(self)->take(key, call);
}

//  bool QQuickPopup::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QQuickPopup9isVisibleEv(const QQuickPopup *self) {
  return self->QQuickPopup::isVisible();
}

//  void QQuickPopup::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10setVisibleEb(
    QQuickPopup *self,
    bool visible) {
  self->QQuickPopup::setVisible(visible);
}

//  void QQuickPopup::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10setOpacityEd(
    QQuickPopup *self,
    qreal opacity) {
  self->QQuickPopup::setOpacity(opacity);
}

//  void QQuickPopup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10classBeginEv(QQuickPopup *self) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::classBegin();
}

//  void QQuickPopup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup17componentCompleteEv(QQuickPopup *self) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::componentComplete();
}

//  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPopup *self,
    QQuickItem *child,
    QEvent *event) {
  return static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::childMouseEventFilter(
      child,
      event);
}

//  void QQuickPopup::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup12focusInEventEP11QFocusEvent(
    QQuickPopup *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::focusInEvent(event);
}

//  void QQuickPopup::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13focusOutEventEP11QFocusEvent(
    QQuickPopup *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::focusOutEvent(event);
}

//  void QQuickPopup::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13keyPressEventEP9QKeyEvent(
    QQuickPopup *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::keyPressEvent(event);
}

//  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent(
    QQuickPopup *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::keyReleaseEvent(
      event);
}

//  void QQuickPopup::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup15mousePressEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::mousePressEvent(
      event);
}

//  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::mouseMoveEvent(event);
}

//  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::mouseReleaseEvent(
      event);
}

//  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent(
    QQuickPopup *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::mouseDoubleClickEvent(
      event);
}

//  void QQuickPopup::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup16mouseUngrabEventEv(QQuickPopup *self) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::mouseUngrabEvent();
}

//  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent(
    QQuickPopup *self,
    QQuickItem *item,
    QEvent *event) {
  return static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::overlayEvent(
      item,
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopup::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10touchEventEP11QTouchEvent(
    QQuickPopup *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopup::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup16touchUngrabEventEv(QQuickPopup *self) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickPopup::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10wheelEventEP11QWheelEvent(
    QQuickPopup *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent(
    QQuickPopup *self,
    QDragEnterEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::dragEnterEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent(
    QQuickPopup *self,
    QDragMoveEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::dragMoveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent(
    QQuickPopup *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::dragLeaveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopup::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup9dropEventEP10QDropEvent(
    QQuickPopup *self,
    QDropEvent *event) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::dropEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickPopup::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_(
    QQuickPopup *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickPopup::contentSizeChange(const QSizeF &newSize, const QSizeF
//      &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_(
    QQuickPopup *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::contentSizeChange(
      *newSize,
      *oldSize);
}

//  void QQuickPopup::fontChange(const QFont &newFont, const QFont &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10fontChangeERK5QFontS2_(
    QQuickPopup *self,
    const QFont *newFont,
    const QFont *oldFont) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::fontChange(
      *newFont,
      *oldFont);
}

//  void QQuickPopup::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup14geometryChangeERK6QRectFS2_(
    QQuickPopup *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickPopup::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup12localeChangeERK7QLocaleS2_(
    QQuickPopup *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::localeChange(
      *newLocale,
      *oldLocale);
}

//  void QQuickPopup::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPopup *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::itemChange(
      change,
      *data);
}

//  void QQuickPopup::marginsChange(const QMarginsF &newMargins, const
//      QMarginsF &oldMargins)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newMargins,
    const QMarginsF *oldMargins) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::marginsChange(
      *newMargins,
      *oldMargins);
}

//  void QQuickPopup::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::paddingChange(
      *newPadding,
      *oldPadding);
}

//  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup13spacingChangeEdd(
    QQuickPopup *self,
    qreal newSpacing,
    qreal oldSpacing) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::spacingChange(
      newSpacing,
      oldSpacing);
}

//  void QQuickPopup::insetChange(const QMarginsF &newInset, const QMarginsF
//      &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_(
    QQuickPopup *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::insetChange(
      *newInset,
      *oldInset);
}

//  QFont QQuickPopup::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK11QQuickPopup11defaultFontEv(const QQuickPopup *self) {
  return new QFont(
      static_cast<const OwnQQuickPopup *>(self)->OwnQQuickPopup::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPopup::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK11QQuickPopup14accessibleRoleEv(
    const QQuickPopup *self) {
  return self->QQuickPopup::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPopup::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickPopup26accessibilityActiveChangedEb(
    QQuickPopup *self,
    bool active) {
  static_cast<OwnQQuickPopup *>(self)->OwnQQuickPopup::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN11QQuickPopup22safeAreaAttachmentItemEv(
    QQuickPopup *self) {
  return self->QQuickPopup::safeAreaAttachmentItem();
}

//  QQuickItem *QQuickPopup::attacheeItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZNK11QQuickPopup12attacheeItemEv(
    const QQuickPopup *self) {
  return self->QQuickPopup::attacheeItem();
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickPopup::attachedParent(const QMetaObject *attachedType) const
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_own_ZNK11QQuickPopup14attachedParentEPK11QMetaObject(
    const QQuickPopup *self,
    const QMetaObject *attachedType) {
  return self->QQuickPopup::attachedParent(attachedType);
}

//  QList<QQuickPopup *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickPopup *> *ritual_list_make_QQuickPopup_ptr() {
  return new QList<QQuickPopup *>();
}

//  void QList<QQuickPopup *>::append(const QQuickPopup * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickPopup_ptr(
    QList<QQuickPopup *> *self,
    QQuickPopup *element) {
  self->append(element);
}

//  qsizetype QList<QQuickPopup *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickPopup_ptr(
    const QList<QQuickPopup *> *self) {
  return self->size();
}

//  const QQuickPopup * &QList<QQuickPopup *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_list_at_QQuickPopup_ptr(
    const QList<QQuickPopup *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickPopup *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickPopup_ptr(QList<QQuickPopup *> *self) {
  delete self;
}
