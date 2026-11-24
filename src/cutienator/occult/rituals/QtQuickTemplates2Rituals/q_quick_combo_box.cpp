//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcombobox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickComboBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickComboBox : QQuickComboBox {
  using QQuickComboBox::eventFilter;
  using QQuickComboBox::focusInEvent;
  using QQuickComboBox::focusOutEvent;
  using QQuickComboBox::inputMethodEvent;
  using QQuickComboBox::keyPressEvent;
  using QQuickComboBox::keyReleaseEvent;
  using QQuickComboBox::wheelEvent;
  using QQuickComboBox::event;
  using QQuickComboBox::componentComplete;
  using QQuickComboBox::itemChange;
  using QQuickComboBox::fontChange;
  using QQuickComboBox::contentItemChange;
  using QQuickComboBox::localeChange;
  using QQuickComboBox::defaultFont;
  using QQuickComboBox::accessibleRole;
  using QQuickComboBox::accessibilityActiveChanged;
};

//  A QQuickComboBox that Python can take functions over in. Every QQuickComboBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
typedef bool (*CuteQQuickComboBoxCall0)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall1)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall2)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(im)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall3)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall6)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
typedef bool (*CuteQQuickComboBoxCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall10)(const void *, const QFont *, const QFont *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall11)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall12)(const void *, const QLocale *, const QLocale *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef const QFont * (*CuteQQuickComboBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQuickComboBoxCall14)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQuickComboBoxCall15)(const void *, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickComboBoxCall16)(const void *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall17)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall18)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall19)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickComboBoxCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickComboBoxCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickComboBoxCall23)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickComboBoxCall24)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickComboBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickComboBoxCall26)(const void *, const QRectF *, const QRectF *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickComboBoxCall28)(const void *, int *);
typedef void (*CuteQQuickComboBoxCall29)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickComboBoxCall30)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickComboBoxCall31)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickComboBoxCall32)(const void *, int *);
typedef const QRectF * (*CuteQQuickComboBoxCall33)(const void *, int *);
typedef const QRectF * (*CuteQQuickComboBoxCall34)(const void *, int *);
typedef bool (*CuteQQuickComboBoxCall35)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickComboBoxCall36)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickComboBoxCall37)(const void *, int *);
typedef void * (*CuteQQuickComboBoxCall38)(const void *, int *);
typedef void (*CuteQQuickComboBoxCall39)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickComboBoxCall40)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickComboBoxCall41)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickComboBoxCall42)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickComboBoxCall43)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickComboBoxCall44)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickComboBoxCall45)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickComboBoxCall46)(const void *, int *);
typedef void (*CuteQQuickComboBoxCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickComboBoxCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickComboBoxCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickComboBoxCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickComboBoxCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickComboBoxCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickComboBox : public QQuickComboBox {
public:
  using QQuickComboBox::QQuickComboBox;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(im)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(im)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQuickControl10fontChangeERK5QFontS2_")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQuickControl12localeChangeERK7QLocaleS2_")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK13QQuickControl11defaultFontEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK13QQuickControl14accessibleRoleEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQuickControl26accessibilityActiveChangedEb")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
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
    if (!std::strcmp(key, "_ZN13QQuickControl11insetChangeERK9QMarginsFS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQuickControl13enabledChangeEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[38] = call;
      return true;
    }
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
#if QT_CONFIG(qml_delegate_model)
  //  bool QQuickComboBox::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickComboBoxCall0 call = reinterpret_cast<CuteQQuickComboBoxCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QQuickComboBox::eventFilter(object, event);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickComboBoxCall1 call = reinterpret_cast<CuteQQuickComboBoxCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::focusInEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickComboBoxCall2 call = reinterpret_cast<CuteQQuickComboBoxCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::focusOutEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(im)
#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickComboBoxCall3 call = reinterpret_cast<CuteQQuickComboBoxCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(im)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickComboBoxCall4 call = reinterpret_cast<CuteQQuickComboBoxCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::keyPressEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickComboBoxCall5 call = reinterpret_cast<CuteQQuickComboBoxCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickComboBoxCall6 call = reinterpret_cast<CuteQQuickComboBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickComboBox::wheelEvent(event);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_delegate_model)
  //  bool QQuickComboBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickComboBoxCall7 call = reinterpret_cast<CuteQQuickComboBoxCall7>(taken[7]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickComboBox::event(e);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::componentComplete()
  void componentComplete() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickComboBoxCall8 call = reinterpret_cast<CuteQQuickComboBoxCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickComboBox::componentComplete();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickComboBoxCall9 call = reinterpret_cast<CuteQQuickComboBoxCall9>(taken[9]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickComboBox::itemChange(change, value);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickComboBoxCall10 call = reinterpret_cast<CuteQQuickComboBoxCall10>(taken[10]);
      call(this, &newFont, &oldFont, &handled);
      if (handled) return;
    }
    QQuickComboBox::fontChange(newFont, oldFont);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::contentItemChange(QQuickItem *newItem,
  //      QQuickItem *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickComboBoxCall11 call = reinterpret_cast<CuteQQuickComboBoxCall11>(taken[11]);
      call(this, newItem, oldItem, &handled);
      if (handled) return;
    }
    QQuickComboBox::contentItemChange(newItem, oldItem);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::localeChange(const QLocale &newLocale, const
  //      QLocale &oldLocale)
  void localeChange(
      const QLocale &newLocale,
      const QLocale &oldLocale) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickComboBoxCall12 call = reinterpret_cast<CuteQQuickComboBoxCall12>(taken[12]);
      call(this, &newLocale, &oldLocale, &handled);
      if (handled) return;
    }
    QQuickComboBox::localeChange(newLocale, oldLocale);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  QFont QQuickComboBox::defaultFont() const
  QFont defaultFont() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickComboBoxCall13 call = reinterpret_cast<CuteQQuickComboBoxCall13>(taken[13]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickComboBox::defaultFont();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
  //  QAccessible::Role QQuickComboBox::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickComboBoxCall14 call = reinterpret_cast<CuteQQuickComboBoxCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickComboBox::accessibleRole();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(qml_delegate_model)
  //  void QQuickComboBox::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickComboBoxCall15 call = reinterpret_cast<CuteQQuickComboBoxCall15>(taken[15]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickComboBox::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControl::classBegin()
  void classBegin() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickComboBoxCall16 call = reinterpret_cast<CuteQQuickComboBoxCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::classBegin();
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickComboBoxCall17 call = reinterpret_cast<CuteQQuickComboBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickComboBoxCall18 call = reinterpret_cast<CuteQQuickComboBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickComboBoxCall19 call = reinterpret_cast<CuteQQuickComboBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickControl::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickComboBoxCall20 call = reinterpret_cast<CuteQQuickComboBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mousePressEvent(event);
  }

  //  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickComboBoxCall21 call = reinterpret_cast<CuteQQuickComboBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseMoveEvent(event);
  }

  //  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickComboBoxCall22 call = reinterpret_cast<CuteQQuickComboBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::mouseReleaseEvent(event);
  }

  //  void QQuickControl::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickComboBoxCall23 call = reinterpret_cast<CuteQQuickComboBoxCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mouseUngrabEvent();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickComboBoxCall24 call = reinterpret_cast<CuteQQuickComboBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickControl::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickControl::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickComboBoxCall25 call = reinterpret_cast<CuteQQuickComboBoxCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControl::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickComboBoxCall26 call = reinterpret_cast<CuteQQuickComboBoxCall26>(taken[26]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickControl::geometryChange(newGeometry, oldGeometry);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickControl::hoverChange()
  void hoverChange() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickComboBoxCall27 call = reinterpret_cast<CuteQQuickComboBoxCall27>(taken[27]);
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
      CuteQQuickComboBoxCall28 call = reinterpret_cast<CuteQQuickComboBoxCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::mirrorChange();
  }

  //  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickComboBoxCall29 call = reinterpret_cast<CuteQQuickComboBoxCall29>(taken[29]);
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
      CuteQQuickComboBoxCall30 call = reinterpret_cast<CuteQQuickComboBoxCall30>(taken[30]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickControl::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickControl::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickComboBoxCall31 call = reinterpret_cast<CuteQQuickComboBoxCall31>(taken[31]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickControl::insetChange(newInset, oldInset);
  }

  //  void QQuickControl::enabledChange()
  void enabledChange() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickComboBoxCall32 call = reinterpret_cast<CuteQQuickComboBoxCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControl::enabledChange();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickComboBoxCall33 call = reinterpret_cast<CuteQQuickComboBoxCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickComboBoxCall34 call = reinterpret_cast<CuteQQuickComboBoxCall34>(taken[34]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickComboBoxCall35 call = reinterpret_cast<CuteQQuickComboBoxCall35>(taken[35]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickComboBoxCall36 call = reinterpret_cast<CuteQQuickComboBoxCall36>(taken[36]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickComboBoxCall37 call = reinterpret_cast<CuteQQuickComboBoxCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickComboBoxCall38 call = reinterpret_cast<CuteQQuickComboBoxCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickComboBoxCall39 call = reinterpret_cast<CuteQQuickComboBoxCall39>(taken[39]);
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
      CuteQQuickComboBoxCall40 call = reinterpret_cast<CuteQQuickComboBoxCall40>(taken[40]);
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
      CuteQQuickComboBoxCall41 call = reinterpret_cast<CuteQQuickComboBoxCall41>(taken[41]);
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
      CuteQQuickComboBoxCall42 call = reinterpret_cast<CuteQQuickComboBoxCall42>(taken[42]);
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
      CuteQQuickComboBoxCall43 call = reinterpret_cast<CuteQQuickComboBoxCall43>(taken[43]);
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
      CuteQQuickComboBoxCall44 call = reinterpret_cast<CuteQQuickComboBoxCall44>(taken[44]);
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
      CuteQQuickComboBoxCall45 call = reinterpret_cast<CuteQQuickComboBoxCall45>(taken[45]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickComboBoxCall46 call = reinterpret_cast<CuteQQuickComboBoxCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickComboBoxCall47 call = reinterpret_cast<CuteQQuickComboBoxCall47>(taken[47]);
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
      CuteQQuickComboBoxCall48 call = reinterpret_cast<CuteQQuickComboBoxCall48>(taken[48]);
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
      CuteQQuickComboBoxCall49 call = reinterpret_cast<CuteQQuickComboBoxCall49>(taken[49]);
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
      CuteQQuickComboBoxCall50 call = reinterpret_cast<CuteQQuickComboBoxCall50>(taken[50]);
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
      CuteQQuickComboBoxCall51 call = reinterpret_cast<CuteQQuickComboBoxCall51>(taken[51]);
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
      CuteQQuickComboBoxCall52 call = reinterpret_cast<CuteQQuickComboBoxCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickComboBox10metaObjectEv(
    const QQuickComboBox *self) {
  return self->metaObject();
}

//  QString QQuickComboBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickComboBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickComboBox::tr(s, c, n));
}

//  QQuickComboBox::QQuickComboBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickComboBox *ritual_ZN14QQuickComboBoxC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickComboBox(parent);
}

//  QQuickComboBox::~QQuickComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBoxD1Ev(QQuickComboBox *self) {
  delete self;
}

//  int QQuickComboBox::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox5countEv(const QQuickComboBox *self) {
  return self->count();
}

//  QVariant QQuickComboBox::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickComboBox5modelEv(const QQuickComboBox *self) {
  return new QVariant(self->model());
}

//  void QQuickComboBox::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox8setModelERK8QVariant(
    QQuickComboBox *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  QQmlInstanceModel *QQuickComboBox::delegateModel() const
extern "C" Q_DECL_EXPORT
QQmlInstanceModel *ritual_ZNK14QQuickComboBox13delegateModelEv(
    const QQuickComboBox *self) {
  return self->delegateModel();
}

//  bool QQuickComboBox::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox9isPressedEv(const QQuickComboBox *self) {
  return self->isPressed();
}

//  void QQuickComboBox::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox10setPressedEb(
    QQuickComboBox *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  int QQuickComboBox::highlightedIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox16highlightedIndexEv(
    const QQuickComboBox *self) {
  return self->highlightedIndex();
}

//  int QQuickComboBox::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox12currentIndexEv(const QQuickComboBox *self) {
  return self->currentIndex();
}

//  void QQuickComboBox::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox15setCurrentIndexEi(
    QQuickComboBox *self,
    int index) {
  self->setCurrentIndex(index);
}

//  QString QQuickComboBox::currentText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox11currentTextEv(
    const QQuickComboBox *self) {
  return new QString(self->currentText());
}

//  QString QQuickComboBox::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox11displayTextEv(
    const QQuickComboBox *self) {
  return new QString(self->displayText());
}

//  void QQuickComboBox::setDisplayText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox14setDisplayTextERK7QString(
    QQuickComboBox *self,
    const QString *text) {
  self->setDisplayText(*text);
}

//  void QQuickComboBox::resetDisplayText()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox16resetDisplayTextEv(QQuickComboBox *self) {
  self->resetDisplayText();
}

//  QString QQuickComboBox::textRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox8textRoleEv(const QQuickComboBox *self) {
  return new QString(self->textRole());
}

//  void QQuickComboBox::setTextRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox11setTextRoleERK7QString(
    QQuickComboBox *self,
    const QString *role) {
  self->setTextRole(*role);
}

//  QString QQuickComboBox::valueRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox9valueRoleEv(const QQuickComboBox *self) {
  return new QString(self->valueRole());
}

//  void QQuickComboBox::setValueRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox12setValueRoleERK7QString(
    QQuickComboBox *self,
    const QString *role) {
  self->setValueRole(*role);
}

//  QQmlComponent *QQuickComboBox::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickComboBox8delegateEv(
    const QQuickComboBox *self) {
  return self->delegate();
}

//  void QQuickComboBox::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox11setDelegateEP13QQmlComponent(
    QQuickComboBox *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QQuickItem *QQuickComboBox::indicator() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickComboBox9indicatorEv(
    const QQuickComboBox *self) {
  return self->indicator();
}

//  void QQuickComboBox::setIndicator(QQuickItem *indicator)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox12setIndicatorEP10QQuickItem(
    QQuickComboBox *self,
    QQuickItem *indicator) {
  self->setIndicator(indicator);
}

//  QQuickPopup *QQuickComboBox::popup() const
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZNK14QQuickComboBox5popupEv(const QQuickComboBox *self) {
  return self->popup();
}

//  void QQuickComboBox::setPopup(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox8setPopupEP11QQuickPopup(
    QQuickComboBox *self,
    QQuickPopup *popup) {
  self->setPopup(popup);
}

//  QString QQuickComboBox::textAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox6textAtEi(
    const QQuickComboBox *self,
    int index) {
  return new QString(self->textAt(index));
}

//  int QQuickComboBox::find(const QString &text, Qt::MatchFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox4findERK7QString6QFlagsIN2Qt9MatchFlagEE(
    const QQuickComboBox *self,
    const QString *text,
    int flags) {
  return self->find(*text, QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  bool QQuickComboBox::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox6isFlatEv(const QQuickComboBox *self) {
  return self->isFlat();
}

//  void QQuickComboBox::setFlat(bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox7setFlatEb(QQuickComboBox *self, bool flat) {
  self->setFlat(flat);
}

//  bool QQuickComboBox::isDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox6isDownEv(const QQuickComboBox *self) {
  return self->isDown();
}

//  void QQuickComboBox::setDown(bool down)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox7setDownEb(QQuickComboBox *self, bool down) {
  self->setDown(down);
}

//  void QQuickComboBox::resetDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox9resetDownEv(QQuickComboBox *self) {
  self->resetDown();
}

//  bool QQuickComboBox::isEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox10isEditableEv(const QQuickComboBox *self) {
  return self->isEditable();
}

//  void QQuickComboBox::setEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox11setEditableEb(
    QQuickComboBox *self,
    bool editable) {
  self->setEditable(editable);
}

//  QString QQuickComboBox::editText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickComboBox8editTextEv(const QQuickComboBox *self) {
  return new QString(self->editText());
}

//  void QQuickComboBox::setEditText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox11setEditTextERK7QString(
    QQuickComboBox *self,
    const QString *text) {
  self->setEditText(*text);
}

//  void QQuickComboBox::resetEditText()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox13resetEditTextEv(QQuickComboBox *self) {
  self->resetEditText();
}

#if QT_CONFIG(validator)
//  QValidator *QQuickComboBox::validator() const
extern "C" Q_DECL_EXPORT
QValidator *ritual_ZNK14QQuickComboBox9validatorEv(
    const QQuickComboBox *self) {
  return self->validator();
}
#endif  // QT_CONFIG(validator)

#if QT_CONFIG(validator)
//  void QQuickComboBox::setValidator(QValidator *validator)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox12setValidatorEP10QValidator(
    QQuickComboBox *self,
    QValidator *validator) {
  self->setValidator(validator);
}
#endif  // QT_CONFIG(validator)

//  Qt::InputMethodHints QQuickComboBox::inputMethodHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox16inputMethodHintsEv(
    const QQuickComboBox *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QQuickComboBox::setInputMethodHints(Qt::InputMethodHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHintEE(
    QQuickComboBox *self,
    int hints) {
  self->setInputMethodHints(QFlags<Qt::InputMethodHint>::fromInt(hints));
}

//  bool QQuickComboBox::isInputMethodComposing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox22isInputMethodComposingEv(
    const QQuickComboBox *self) {
  return self->isInputMethodComposing();
}

//  bool QQuickComboBox::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox18hasAcceptableInputEv(
    const QQuickComboBox *self) {
  return self->hasAcceptableInput();
}

//  qreal QQuickComboBox::implicitIndicatorWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickComboBox22implicitIndicatorWidthEv(
    const QQuickComboBox *self) {
  return self->implicitIndicatorWidth();
}

//  qreal QQuickComboBox::implicitIndicatorHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickComboBox23implicitIndicatorHeightEv(
    const QQuickComboBox *self) {
  return self->implicitIndicatorHeight();
}

//  QVariant QQuickComboBox::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickComboBox12currentValueEv(
    const QQuickComboBox *self) {
  return new QVariant(self->currentValue());
}

//  void QQuickComboBox::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox15setCurrentValueERK8QVariant(
    QQuickComboBox *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QQuickComboBox::valueAt(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickComboBox7valueAtEi(
    const QQuickComboBox *self,
    int index) {
  return new QVariant(self->valueAt(index));
}

//  int QQuickComboBox::indexOfValue(const QVariant &value) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickComboBox12indexOfValueERK8QVariant(
    const QQuickComboBox *self,
    const QVariant *value) {
  return self->indexOfValue(*value);
}

//  bool QQuickComboBox::selectTextByMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox17selectTextByMouseEv(
    const QQuickComboBox *self) {
  return self->selectTextByMouse();
}

//  void QQuickComboBox::setSelectTextByMouse(bool canSelect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox20setSelectTextByMouseEb(
    QQuickComboBox *self,
    bool canSelect) {
  self->setSelectTextByMouse(canSelect);
}

//  ImplicitContentWidthPolicy QQuickComboBox::implicitContentWidthPolicy()
//      const
extern "C" Q_DECL_EXPORT
QQuickComboBox::ImplicitContentWidthPolicy ritual_ZNK14QQuickComboBox26implicitContentWidthPolicyEv(
    const QQuickComboBox *self) {
  return self->implicitContentWidthPolicy();
}

//  void
//      QQuickComboBox::setImplicitContentWidthPolicy(ImplicitContentWidthPol
//      icy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox29setImplicitContentWidthPolicyENS_26ImplicitContentWidthPolicyE(
    QQuickComboBox *self,
    QQuickComboBox::ImplicitContentWidthPolicy policy) {
  self->setImplicitContentWidthPolicy(policy);
}

//  bool QQuickComboBox::highlightOnHover() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickComboBox16highlightOnHoverEv(
    const QQuickComboBox *self) {
  return self->highlightOnHover();
}

//  void QQuickComboBox::setHighlightOnHover(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox19setHighlightOnHoverEb(
    QQuickComboBox *self,
    bool value) {
  self->setHighlightOnHover(value);
}

//  void QQuickComboBox::incrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox21incrementCurrentIndexEv(
    QQuickComboBox *self) {
  self->incrementCurrentIndex();
}

//  void QQuickComboBox::decrementCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox21decrementCurrentIndexEv(
    QQuickComboBox *self) {
  self->decrementCurrentIndex();
}

//  void QQuickComboBox::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox9selectAllEv(QQuickComboBox *self) {
  self->selectAll();
}

//  bool QQuickComboBox::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickComboBox11eventFilterEP7QObjectP6QEvent(
    QQuickComboBox *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QQuickComboBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox12focusInEventEP11QFocusEvent(
    QQuickComboBox *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickComboBox::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox13focusOutEventEP11QFocusEvent(
    QQuickComboBox *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(im)
//  void QQuickComboBox::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox16inputMethodEventEP17QInputMethodEvent(
    QQuickComboBox *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}
#endif  // QT_CONFIG(im)

//  void QQuickComboBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox13keyPressEventEP9QKeyEvent(
    QQuickComboBox *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickComboBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox15keyReleaseEventEP9QKeyEvent(
    QQuickComboBox *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickComboBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox10wheelEventEP11QWheelEvent(
    QQuickComboBox *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  bool QQuickComboBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickComboBox5eventEP6QEvent(
    QQuickComboBox *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickComboBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox17componentCompleteEv(QQuickComboBox *self) {
  self->componentComplete();
}

//  void QQuickComboBox::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickComboBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickComboBox::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox10fontChangeERK5QFontS2_(
    QQuickComboBox *self,
    const QFont *newFont,
    const QFont *oldFont) {
  self->fontChange(*newFont, *oldFont);
}

//  void QQuickComboBox::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox17contentItemChangeEP10QQuickItemS1_(
    QQuickComboBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickComboBox::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox12localeChangeERK7QLocaleS2_(
    QQuickComboBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  QFont QQuickComboBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickComboBox11defaultFontEv(
    const QQuickComboBox *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickComboBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK14QQuickComboBox14accessibleRoleEv(
    const QQuickComboBox *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickComboBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickComboBox26accessibilityActiveChangedEb(
    QQuickComboBox *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQQuickComboBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickComboBox(
    QQuickComboBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickComboBox *>(self)->take(key, call);
}

//  bool QQuickComboBox::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickComboBox11eventFilterEP7QObjectP6QEvent(
    QQuickComboBox *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::eventFilter(
      object,
      event);
}

//  void QQuickComboBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox12focusInEventEP11QFocusEvent(
    QQuickComboBox *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::focusInEvent(
      event);
}

//  void QQuickComboBox::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox13focusOutEventEP11QFocusEvent(
    QQuickComboBox *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::focusOutEvent(
      event);
}

#if QT_CONFIG(im)
//  void QQuickComboBox::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox16inputMethodEventEP17QInputMethodEvent(
    QQuickComboBox *self,
    QInputMethodEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::inputMethodEvent(
      event);
}
#endif  // QT_CONFIG(im)

//  void QQuickComboBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox13keyPressEventEP9QKeyEvent(
    QQuickComboBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::keyPressEvent(
      event);
}

//  void QQuickComboBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox15keyReleaseEventEP9QKeyEvent(
    QQuickComboBox *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::keyReleaseEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QQuickComboBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox10wheelEventEP11QWheelEvent(
    QQuickComboBox *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  bool QQuickComboBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickComboBox5eventEP6QEvent(
    QQuickComboBox *self,
    QEvent *e) {
  return static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::event(e);
}

//  void QQuickComboBox::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox17componentCompleteEv(
    QQuickComboBox *self) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::componentComplete();
}

//  void QQuickComboBox::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickComboBox *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::itemChange(
      change,
      *value);
}

//  void QQuickComboBox::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox10fontChangeERK5QFontS2_(
    QQuickComboBox *self,
    const QFont *newFont,
    const QFont *oldFont) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::fontChange(
      *newFont,
      *oldFont);
}

//  void QQuickComboBox::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox17contentItemChangeEP10QQuickItemS1_(
    QQuickComboBox *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickComboBox::localeChange(const QLocale &newLocale, const QLocale
//      &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox12localeChangeERK7QLocaleS2_(
    QQuickComboBox *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::localeChange(
      *newLocale,
      *oldLocale);
}

//  QFont QQuickComboBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK14QQuickComboBox11defaultFontEv(
    const QQuickComboBox *self) {
  return new QFont(
      static_cast<const OwnQQuickComboBox *>(self)->OwnQQuickComboBox::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickComboBox::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK14QQuickComboBox14accessibleRoleEv(
    const QQuickComboBox *self) {
  return static_cast<const OwnQQuickComboBox *>(self)->OwnQQuickComboBox::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickComboBox::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickComboBox26accessibilityActiveChangedEb(
    QQuickComboBox *self,
    bool active) {
  static_cast<OwnQQuickComboBox *>(self)->OwnQQuickComboBox::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
