//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmargins.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickMenu may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenu : QQuickMenu {
  using QQuickMenu::componentComplete;
  using QQuickMenu::contentItemChange;
  using QQuickMenu::itemChange;
  using QQuickMenu::keyPressEvent;
  using QQuickMenu::timerEvent;
  using QQuickMenu::defaultFont;
  using QQuickMenu::accessibleRole;
};

//  A QQuickMenu that Python can take functions over in. Every QQuickMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_object_model)
typedef bool (*CuteQQuickMenuCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall2)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall3)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQuickMenuCall6)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(qml_object_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
typedef const QFont * (*CuteQQuickMenuCall7)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQuickMenuCall8)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickMenuCall9)(const void *, qreal, int *);
typedef void (*CuteQQuickMenuCall10)(const void *, int *);
typedef bool (*CuteQQuickMenuCall11)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickMenuCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMenuCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMenuCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickMenuCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuCall19)(const void *, int *);
typedef bool (*CuteQQuickMenuCall20)(const void *, QQuickItem *, QEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickMenuCall21)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickMenuCall22)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMenuCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuCall24)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuCall25)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuCall26)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuCall27)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuCall28)(const void *, const QSizeF *, const QSizeF *, int *);
typedef void (*CuteQQuickMenuCall29)(const void *, const QFont *, const QFont *, int *);
typedef void (*CuteQQuickMenuCall30)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickMenuCall31)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickMenuCall32)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickMenuCall33)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickMenuCall34)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickMenuCall35)(const void *, const QMarginsF *, const QMarginsF *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickMenuCall36)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
typedef void * (*CuteQQuickMenuCall37)(const void *, int *);
typedef void * (*CuteQQuickMenuCall38)(const void *, int *);
typedef void * (*CuteQQuickMenuCall39)(const void *, const QMetaObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMenuCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMenuCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMenu : public QQuickMenu {
public:
  using QQuickMenu::QQuickMenu;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK11QQuickPopup9isVisibleEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN11QQuickPopup10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN11QQuickPopup13keyPressEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK11QQuickPopup11defaultFontEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK11QQuickPopup14accessibleRoleEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QQuickPopup10setOpacityEd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12focusInEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13focusOutEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup16mouseUngrabEventEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup10touchEventEP11QTouchEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN11QQuickPopup10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup9dropEventEP10QDropEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10fontChangeERK5QFontS2_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14geometryChangeERK6QRectFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12localeChangeERK7QLocaleS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13spacingChangeEdd")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QQuickPopup26accessibilityActiveChangedEb")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QQuickSafeAreaAttachable22safeAreaAttachmentItemEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK11QMetaObject")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

#if QT_CONFIG(qml_object_model)
  //  bool QQuickMenu::isVisible() const
  bool isVisible() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuCall0 call = reinterpret_cast<CuteQQuickMenuCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickMenu::isVisible();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuCall1 call = reinterpret_cast<CuteQQuickMenuCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickMenu::setVisible(visible);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuCall2 call = reinterpret_cast<CuteQQuickMenuCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenu::componentComplete();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuCall3 call = reinterpret_cast<CuteQQuickMenuCall3>(taken[3]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickMenu::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::itemChange(QQuickItem::ItemChange change, const
  //      QQuickItem::ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuCall4 call = reinterpret_cast<CuteQQuickMenuCall4>(taken[4]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickMenu::itemChange(change, data);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMenuCall5 call = reinterpret_cast<CuteQQuickMenuCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMenu::keyPressEvent(event);
  }
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_object_model)
  //  void QQuickMenu::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMenuCall6 call = reinterpret_cast<CuteQQuickMenuCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMenu::timerEvent(event);
  }
#endif  // QT_CONFIG(qml_object_model)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(qml_object_model)
  //  QFont QQuickMenu::defaultFont() const
  QFont defaultFont() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuCall7 call = reinterpret_cast<CuteQQuickMenuCall7>(taken[7]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickMenu::defaultFont();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_object_model)
  //  QAccessible::Role QQuickMenu::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMenuCall8 call = reinterpret_cast<CuteQQuickMenuCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickMenu::accessibleRole();
  }
#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(accessibility)

  //  void QQuickPopup::setOpacity(qreal opacity)
  void setOpacity(qreal opacity) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMenuCall9 call = reinterpret_cast<CuteQQuickMenuCall9>(taken[9]);
      call(this, opacity, &handled);
      if (handled) return;
    }
    QQuickPopup::setOpacity(opacity);
  }

  //  void QQuickPopup::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuCall10 call = reinterpret_cast<CuteQQuickMenuCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::classBegin();
  }

  //  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *child, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMenuCall11 call = reinterpret_cast<CuteQQuickMenuCall11>(taken[11]);
      bool given = call(this, child, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::childMouseEventFilter(child, event);
  }

  //  void QQuickPopup::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMenuCall12 call = reinterpret_cast<CuteQQuickMenuCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusInEvent(event);
  }

  //  void QQuickPopup::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMenuCall13 call = reinterpret_cast<CuteQQuickMenuCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusOutEvent(event);
  }

  //  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMenuCall14 call = reinterpret_cast<CuteQQuickMenuCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::keyReleaseEvent(event);
  }

  //  void QQuickPopup::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuCall15 call = reinterpret_cast<CuteQQuickMenuCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mousePressEvent(event);
  }

  //  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMenuCall16 call = reinterpret_cast<CuteQQuickMenuCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseMoveEvent(event);
  }

  //  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMenuCall17 call = reinterpret_cast<CuteQQuickMenuCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseReleaseEvent(event);
  }

  //  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMenuCall18 call = reinterpret_cast<CuteQQuickMenuCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseDoubleClickEvent(event);
  }

  //  void QQuickPopup::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuCall19 call = reinterpret_cast<CuteQQuickMenuCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseUngrabEvent();
  }

  //  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
  bool overlayEvent(QQuickItem *item, QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuCall20 call = reinterpret_cast<CuteQQuickMenuCall20>(taken[20]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::overlayEvent(item, event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuCall21 call = reinterpret_cast<CuteQQuickMenuCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMenuCall22 call = reinterpret_cast<CuteQQuickMenuCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickPopup::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMenuCall23 call = reinterpret_cast<CuteQQuickMenuCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMenuCall24 call = reinterpret_cast<CuteQQuickMenuCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMenuCall25 call = reinterpret_cast<CuteQQuickMenuCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMenuCall26 call = reinterpret_cast<CuteQQuickMenuCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickMenuCall27 call = reinterpret_cast<CuteQQuickMenuCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dropEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  void QQuickPopup::contentSizeChange(const QSizeF &newSize, const
  //      QSizeF &oldSize)
  void contentSizeChange(
      const QSizeF &newSize,
      const QSizeF &oldSize) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickMenuCall28 call = reinterpret_cast<CuteQQuickMenuCall28>(taken[28]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPopup::contentSizeChange(newSize, oldSize);
  }

  //  void QQuickPopup::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickMenuCall29 call = reinterpret_cast<CuteQQuickMenuCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickMenuCall30 call = reinterpret_cast<CuteQQuickMenuCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQQuickMenuCall31 call = reinterpret_cast<CuteQQuickMenuCall31>(taken[31]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickPopup::localeChange(newLocale, oldLocale);
  }

  //  void QQuickPopup::marginsChange(const QMarginsF &newMargins, const
  //      QMarginsF &oldMargins)
  void marginsChange(
      const QMarginsF &newMargins,
      const QMarginsF &oldMargins) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickMenuCall32 call = reinterpret_cast<CuteQQuickMenuCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMenuCall33 call = reinterpret_cast<CuteQQuickMenuCall33>(taken[33]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickPopup::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMenuCall34 call = reinterpret_cast<CuteQQuickMenuCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQQuickMenuCall35 call = reinterpret_cast<CuteQQuickMenuCall35>(taken[35]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickPopup::insetChange(newInset, oldInset);
  }

#if QT_CONFIG(accessibility)
  //  void QQuickPopup::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickMenuCall36 call = reinterpret_cast<CuteQQuickMenuCall36>(taken[36]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickPopup::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

  //  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
  QQuickItem *safeAreaAttachmentItem() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickMenuCall37 call = reinterpret_cast<CuteQQuickMenuCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPopup::safeAreaAttachmentItem();
  }

  //  QQuickItem *QQuickPopup::attacheeItem() const
  QQuickItem *attacheeItem() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickMenuCall38 call = reinterpret_cast<CuteQQuickMenuCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteQQuickMenuCall39 call = reinterpret_cast<CuteQQuickMenuCall39>(taken[39]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickPopup::attachedParent(attachedType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickMenuCall40 call = reinterpret_cast<CuteQQuickMenuCall40>(taken[40]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickMenuCall41 call = reinterpret_cast<CuteQQuickMenuCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickMenuCall42 call = reinterpret_cast<CuteQQuickMenuCall42>(taken[42]);
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
      CuteQQuickMenuCall43 call = reinterpret_cast<CuteQQuickMenuCall43>(taken[43]);
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
      CuteQQuickMenuCall44 call = reinterpret_cast<CuteQQuickMenuCall44>(taken[44]);
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
      CuteQQuickMenuCall45 call = reinterpret_cast<CuteQQuickMenuCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickMenu10metaObjectEv(
    const QQuickMenu *self) {
  return self->metaObject();
}

//  QString QQuickMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickMenu2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMenu::tr(s, c, n));
}

//  QQuickMenu::QQuickMenu(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN10QQuickMenuC1EP7QObject(QObject *parent) {
  return new CuteQQuickMenu(parent);
}

//  QQuickMenu::~QQuickMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenuD1Ev(QQuickMenu *self) {
  delete self;
}

//  QQuickItem *QQuickMenu::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickMenu6itemAtEi(
    const QQuickMenu *self,
    int index) {
  return self->itemAt(index);
}

//  void QQuickMenu::addItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu7addItemEP10QQuickItem(
    QQuickMenu *self,
    QQuickItem *item) {
  self->addItem(item);
}

//  void QQuickMenu::insertItem(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10insertItemEiP10QQuickItem(
    QQuickMenu *self,
    int index,
    QQuickItem *item) {
  self->insertItem(index, item);
}

//  void QQuickMenu::moveItem(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu8moveItemEii(QQuickMenu *self, int from, int to) {
  self->moveItem(from, to);
}

//  void QQuickMenu::removeItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10removeItemEP10QQuickItem(
    QQuickMenu *self,
    QQuickItem *item) {
  self->removeItem(item);
}

//  QVariant QQuickMenu::contentModel() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QQuickMenu12contentModelEv(const QQuickMenu *self) {
  return new QVariant(self->contentModel());
}

//  QString QQuickMenu::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickMenu5titleEv(const QQuickMenu *self) {
  return new QString(self->title());
}

//  void QQuickMenu::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu8setTitleERK7QString(
    QQuickMenu *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QQuickIcon QQuickMenu::icon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK10QQuickMenu4iconEv(const QQuickMenu *self) {
  return new QQuickIcon(self->icon());
}

//  void QQuickMenu::setIcon(const QQuickIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu7setIconERK10QQuickIcon(
    QQuickMenu *self,
    const QQuickIcon *icon) {
  self->setIcon(*icon);
}

//  bool QQuickMenu::separatorsCollapsible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickMenu21separatorsCollapsibleEv(
    const QQuickMenu *self) {
  return self->separatorsCollapsible();
}

//  void QQuickMenu::setSeparatorsCollapsible(bool collapsible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu24setSeparatorsCollapsibleEb(
    QQuickMenu *self,
    bool collapsible) {
  self->setSeparatorsCollapsible(collapsible);
}

//  bool QQuickMenu::cascade() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickMenu7cascadeEv(const QQuickMenu *self) {
  return self->cascade();
}

//  void QQuickMenu::setCascade(bool cascade)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10setCascadeEb(QQuickMenu *self, bool cascade) {
  self->setCascade(cascade);
}

//  void QQuickMenu::resetCascade()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu12resetCascadeEv(QQuickMenu *self) {
  self->resetCascade();
}

//  qreal QQuickMenu::overlap() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickMenu7overlapEv(const QQuickMenu *self) {
  return self->overlap();
}

//  void QQuickMenu::setOverlap(qreal overlap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10setOverlapEd(QQuickMenu *self, qreal overlap) {
  self->setOverlap(overlap);
}

//  QQmlComponent *QQuickMenu::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK10QQuickMenu8delegateEv(const QQuickMenu *self) {
  return self->delegate();
}

//  void QQuickMenu::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu11setDelegateEP13QQmlComponent(
    QQuickMenu *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  int QQuickMenu::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickMenu12currentIndexEv(const QQuickMenu *self) {
  return self->currentIndex();
}

//  void QQuickMenu::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu15setCurrentIndexEi(QQuickMenu *self, int index) {
  self->setCurrentIndex(index);
}

//  int QQuickMenu::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickMenu5countEv(const QQuickMenu *self) {
  return self->count();
}

//  QQuickItem *QQuickMenu::takeItem(int index)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN10QQuickMenu8takeItemEi(QQuickMenu *self, int index) {
  return self->takeItem(index);
}

//  QQuickMenu *QQuickMenu::menuAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK10QQuickMenu6menuAtEi(
    const QQuickMenu *self,
    int index) {
  return self->menuAt(index);
}

//  void QQuickMenu::addMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu7addMenuEPS_(QQuickMenu *self, QQuickMenu *menu) {
  self->addMenu(menu);
}

//  void QQuickMenu::insertMenu(int index, QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10insertMenuEiPS_(
    QQuickMenu *self,
    int index,
    QQuickMenu *menu) {
  self->insertMenu(index, menu);
}

//  void QQuickMenu::removeMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10removeMenuEPS_(
    QQuickMenu *self,
    QQuickMenu *menu) {
  self->removeMenu(menu);
}

//  QQuickMenu *QQuickMenu::takeMenu(int index)
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN10QQuickMenu8takeMenuEi(QQuickMenu *self, int index) {
  return self->takeMenu(index);
}

//  QQuickAction *QQuickMenu::actionAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZNK10QQuickMenu8actionAtEi(
    const QQuickMenu *self,
    int index) {
  return self->actionAt(index);
}

//  void QQuickMenu::addAction(QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu9addActionEP12QQuickAction(
    QQuickMenu *self,
    QQuickAction *action) {
  self->addAction(action);
}

//  void QQuickMenu::insertAction(int index, QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu12insertActionEiP12QQuickAction(
    QQuickMenu *self,
    int index,
    QQuickAction *action) {
  self->insertAction(index, action);
}

//  void QQuickMenu::removeAction(QQuickAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu12removeActionEP12QQuickAction(
    QQuickMenu *self,
    QQuickAction *action) {
  self->removeAction(action);
}

//  QQuickAction *QQuickMenu::takeAction(int index)
extern "C" Q_DECL_EXPORT
QQuickAction *ritual_ZN10QQuickMenu10takeActionEi(
    QQuickMenu *self,
    int index) {
  return self->takeAction(index);
}

//  bool QQuickMenu::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickMenu9isVisibleEv(const QQuickMenu *self) {
  return self->isVisible();
}

//  void QQuickMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10setVisibleEb(QQuickMenu *self, bool visible) {
  self->setVisible(visible);
}

//  void QQuickMenu::popup(QQuickItem *parent, qreal x, qreal y, QQuickItem
//      *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupEP10QQuickItemddS1_(
    QQuickMenu *self,
    QQuickItem *parent,
    qreal x,
    qreal y,
    QQuickItem *menuItem) {
  self->popup(parent, x, y, menuItem);
}

//  void QQuickMenu::popup(QQuickItem *parent, const QPointF &position,
//      QQuickItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupEP10QQuickItemRK7QPointFS1_(
    QQuickMenu *self,
    QQuickItem *parent,
    const QPointF *position,
    QQuickItem *menuItem) {
  self->popup(parent, *position, menuItem);
}

//  void QQuickMenu::popup(QQuickItem *parent, QQuickItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupEP10QQuickItemS1_(
    QQuickMenu *self,
    QQuickItem *parent,
    QQuickItem *menuItem) {
  self->popup(parent, menuItem);
}

//  void QQuickMenu::popup(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupEP10QQuickItem(
    QQuickMenu *self,
    QQuickItem *parent) {
  self->popup(parent);
}

//  void QQuickMenu::popup(qreal x, qreal y, QQuickItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupEddP10QQuickItem(
    QQuickMenu *self,
    qreal x,
    qreal y,
    QQuickItem *menuItem) {
  self->popup(x, y, menuItem);
}

//  void QQuickMenu::popup(const QPointF &position, QQuickItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu5popupERK7QPointFP10QQuickItem(
    QQuickMenu *self,
    const QPointF *position,
    QQuickItem *menuItem) {
  self->popup(*position, menuItem);
}

//  void QQuickMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu7dismissEv(QQuickMenu *self) {
  self->dismiss();
}

//  void QQuickMenu::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu17componentCompleteEv(QQuickMenu *self) {
  self->componentComplete();
}

//  void QQuickMenu::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu17contentItemChangeEP10QQuickItemS1_(
    QQuickMenu *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickMenu::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMenu *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickMenu::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu13keyPressEventEP9QKeyEvent(
    QQuickMenu *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickMenu::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickMenu10timerEventEP11QTimerEvent(
    QQuickMenu *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QFont QQuickMenu::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10QQuickMenu11defaultFontEv(const QQuickMenu *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenu::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK10QQuickMenu14accessibleRoleEv(
    const QQuickMenu *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickMenuPrivate *QQuickMenu::d_func()
extern "C" Q_DECL_EXPORT
QQuickMenuPrivate *ritual_ZN10QQuickMenu6d_funcEv(QQuickMenu *self) {
  return self->d_func();
}

//  const QQuickMenuPrivate *QQuickMenu::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuPrivate *ritual_ZNK10QQuickMenu6d_funcEv(
    const QQuickMenu *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMenu, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenu(QQuickMenu *self, const char *key, void *call) {
  return static_cast<CuteQQuickMenu *>(self)->take(key, call);
}

//  bool QQuickMenu::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QQuickMenu9isVisibleEv(const QQuickMenu *self) {
  return self->QQuickMenu::isVisible();
}

//  void QQuickMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu10setVisibleEb(
    QQuickMenu *self,
    bool visible) {
  self->QQuickMenu::setVisible(visible);
}

//  void QQuickMenu::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu17componentCompleteEv(QQuickMenu *self) {
  static_cast<OwnQQuickMenu *>(self)->OwnQQuickMenu::componentComplete();
}

//  void QQuickMenu::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu17contentItemChangeEP10QQuickItemS1_(
    QQuickMenu *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickMenu *>(self)->OwnQQuickMenu::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickMenu::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMenu *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickMenu *>(self)->OwnQQuickMenu::itemChange(
      change,
      *data);
}

//  void QQuickMenu::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu13keyPressEventEP9QKeyEvent(
    QQuickMenu *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickMenu *>(self)->OwnQQuickMenu::keyPressEvent(event);
}

//  void QQuickMenu::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickMenu10timerEventEP11QTimerEvent(
    QQuickMenu *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickMenu *>(self)->OwnQQuickMenu::timerEvent(event);
}

//  QFont QQuickMenu::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK10QQuickMenu11defaultFontEv(const QQuickMenu *self) {
  return new QFont(
      static_cast<const OwnQQuickMenu *>(self)->OwnQQuickMenu::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenu::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK10QQuickMenu14accessibleRoleEv(
    const QQuickMenu *self) {
  return static_cast<const OwnQQuickMenu *>(self)->OwnQQuickMenu::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(qml_object_model)
