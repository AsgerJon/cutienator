//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p.h, Qt
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
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmargins.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDialog : QQuickDialog {
  using QQuickDialog::itemChange;
  using QQuickDialog::accessibleRole;
  using QQuickDialog::accessibilityActiveChanged;
};

//  A QQuickDialog that Python can take functions over in. Every QQuickDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall0)(const void *, qreal, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall1)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall2)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall3)(const void *, int, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef int (*CuteQQuickDialogCall5)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
typedef void (*CuteQQuickDialogCall6)(const void *, bool, int *);
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickDialogCall7)(const void *, int *);
typedef void (*CuteQQuickDialogCall8)(const void *, bool, int *);
typedef void (*CuteQQuickDialogCall9)(const void *, int *);
typedef void (*CuteQQuickDialogCall10)(const void *, int *);
typedef bool (*CuteQQuickDialogCall11)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickDialogCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDialogCall13)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickDialogCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickDialogCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickDialogCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickDialogCall20)(const void *, int *);
typedef bool (*CuteQQuickDialogCall21)(const void *, QQuickItem *, QEvent *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDialogCall22)(const void *, QTouchEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickDialogCall23)(const void *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickDialogCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogCall25)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogCall26)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogCall27)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogCall28)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickDialogCall29)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickDialogCall30)(const void *, const QSizeF *, const QSizeF *, int *);
typedef void (*CuteQQuickDialogCall31)(const void *, const QFont *, const QFont *, int *);
typedef void (*CuteQQuickDialogCall32)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickDialogCall33)(const void *, const QLocale *, const QLocale *, int *);
typedef void (*CuteQQuickDialogCall34)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDialogCall35)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void (*CuteQQuickDialogCall36)(const void *, qreal, qreal, int *);
typedef void (*CuteQQuickDialogCall37)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef const QFont * (*CuteQQuickDialogCall38)(const void *, int *);
typedef void * (*CuteQQuickDialogCall39)(const void *, int *);
typedef void * (*CuteQQuickDialogCall40)(const void *, int *);
typedef void * (*CuteQQuickDialogCall41)(const void *, const QMetaObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDialogCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDialogCall43)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogCall44)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogCall45)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogCall46)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDialogCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDialog : public QQuickDialog {
public:
  using QQuickDialog::QQuickDialog;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN11QQuickPopup10setOpacityEd")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN12QQuickDialog6acceptEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN12QQuickDialog6rejectEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN12QQuickDialog4doneEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZNK11QQuickPopup14accessibleRoleEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
    if (!std::strcmp(key, "_ZN11QQuickPopup26accessibilityActiveChangedEb")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK11QQuickPopup9isVisibleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZN11QQuickPopup13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN11QQuickPopup16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN11QQuickPopup10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup9dropEventEP10QDropEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup10fontChangeERK5QFontS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup14geometryChangeERK6QRectFS2_")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup12localeChangeERK7QLocaleS2_")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup13spacingChangeEdd")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QQuickPopup11defaultFontEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickSafeAreaAttachable22safeAreaAttachmentItemEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget12attacheeItemEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QQuickAttachedPropertyPropagatorTarget14attachedParentEPK11QMetaObject")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::setOpacity(qreal opacity)
  void setOpacity(qreal opacity) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDialogCall0 call = reinterpret_cast<CuteQQuickDialogCall0>(taken[0]);
      call(this, opacity, &handled);
      if (handled) return;
    }
    QQuickDialog::setOpacity(opacity);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::accept()
  void accept() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDialogCall1 call = reinterpret_cast<CuteQQuickDialogCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialog::accept();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::reject()
  void reject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDialogCall2 call = reinterpret_cast<CuteQQuickDialogCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialog::reject();
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::done(int result)
  void done(int result) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDialogCall3 call = reinterpret_cast<CuteQQuickDialogCall3>(taken[3]);
      call(this, result, &handled);
      if (handled) return;
    }
    QQuickDialog::done(result);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::itemChange(QQuickItem::ItemChange change, const
  //      QQuickItem::ItemChangeData &data)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &data) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDialogCall4 call = reinterpret_cast<CuteQQuickDialogCall4>(taken[4]);
      call(this, static_cast<int>(change), &data, &handled);
      if (handled) return;
    }
    QQuickDialog::itemChange(change, data);
  }
#endif  // QT_CONFIG(quicktemplates2_container)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
  //  QAccessible::Role QQuickDialog::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDialogCall5 call = reinterpret_cast<CuteQQuickDialogCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickDialog::accessibleRole();
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(quicktemplates2_container)
  //  void QQuickDialog::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDialogCall6 call = reinterpret_cast<CuteQQuickDialogCall6>(taken[6]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickDialog::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickPopup::isVisible() const
  bool isVisible() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDialogCall7 call = reinterpret_cast<CuteQQuickDialogCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopup::isVisible();
  }

  //  void QQuickPopup::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDialogCall8 call = reinterpret_cast<CuteQQuickDialogCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickPopup::setVisible(visible);
  }

  //  void QQuickPopup::classBegin()
  void classBegin() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDialogCall9 call = reinterpret_cast<CuteQQuickDialogCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::classBegin();
  }

  //  void QQuickPopup::componentComplete()
  void componentComplete() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDialogCall10 call = reinterpret_cast<CuteQQuickDialogCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::componentComplete();
  }

  //  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent
  //      *event)
  bool childMouseEventFilter(QQuickItem *child, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDialogCall11 call = reinterpret_cast<CuteQQuickDialogCall11>(taken[11]);
      bool given = call(this, child, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::childMouseEventFilter(child, event);
  }

  //  void QQuickPopup::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDialogCall12 call = reinterpret_cast<CuteQQuickDialogCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusInEvent(event);
  }

  //  void QQuickPopup::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDialogCall13 call = reinterpret_cast<CuteQQuickDialogCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::focusOutEvent(event);
  }

  //  void QQuickPopup::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDialogCall14 call = reinterpret_cast<CuteQQuickDialogCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::keyPressEvent(event);
  }

  //  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDialogCall15 call = reinterpret_cast<CuteQQuickDialogCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::keyReleaseEvent(event);
  }

  //  void QQuickPopup::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDialogCall16 call = reinterpret_cast<CuteQQuickDialogCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mousePressEvent(event);
  }

  //  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDialogCall17 call = reinterpret_cast<CuteQQuickDialogCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseMoveEvent(event);
  }

  //  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDialogCall18 call = reinterpret_cast<CuteQQuickDialogCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseReleaseEvent(event);
  }

  //  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickDialogCall19 call = reinterpret_cast<CuteQQuickDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseDoubleClickEvent(event);
  }

  //  void QQuickPopup::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDialogCall20 call = reinterpret_cast<CuteQQuickDialogCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::mouseUngrabEvent();
  }

  //  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
  bool overlayEvent(QQuickItem *item, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDialogCall21 call = reinterpret_cast<CuteQQuickDialogCall21>(taken[21]);
      bool given = call(this, item, event, &handled);
      if (handled) return given;
    }
    return QQuickPopup::overlayEvent(item, event);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickDialogCall22 call = reinterpret_cast<CuteQQuickDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::touchEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  void QQuickPopup::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickDialogCall23 call = reinterpret_cast<CuteQQuickDialogCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopup::touchUngrabEvent();
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
  //  void QQuickPopup::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickDialogCall24 call = reinterpret_cast<CuteQQuickDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickDialogCall25 call = reinterpret_cast<CuteQQuickDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickDialogCall26 call = reinterpret_cast<CuteQQuickDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickDialogCall27 call = reinterpret_cast<CuteQQuickDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickPopup::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickDialogCall28 call = reinterpret_cast<CuteQQuickDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPopup::dropEvent(event);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  void QQuickPopup::contentItemChange(QQuickItem *newItem, QQuickItem
  //      *oldItem)
  void contentItemChange(QQuickItem *newItem, QQuickItem *oldItem) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickDialogCall29 call = reinterpret_cast<CuteQQuickDialogCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQQuickDialogCall30 call = reinterpret_cast<CuteQQuickDialogCall30>(taken[30]);
      call(this, &newSize, &oldSize, &handled);
      if (handled) return;
    }
    QQuickPopup::contentSizeChange(newSize, oldSize);
  }

  //  void QQuickPopup::fontChange(const QFont &newFont, const QFont
  //      &oldFont)
  void fontChange(const QFont &newFont, const QFont &oldFont) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickDialogCall31 call = reinterpret_cast<CuteQQuickDialogCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQQuickDialogCall32 call = reinterpret_cast<CuteQQuickDialogCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQQuickDialogCall33 call = reinterpret_cast<CuteQQuickDialogCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQQuickDialogCall34 call = reinterpret_cast<CuteQQuickDialogCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQQuickDialogCall35 call = reinterpret_cast<CuteQQuickDialogCall35>(taken[35]);
      call(this, &newPadding, &oldPadding, &handled);
      if (handled) return;
    }
    QQuickPopup::paddingChange(newPadding, oldPadding);
  }

  //  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
  void spacingChange(qreal newSpacing, qreal oldSpacing) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickDialogCall36 call = reinterpret_cast<CuteQQuickDialogCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQQuickDialogCall37 call = reinterpret_cast<CuteQQuickDialogCall37>(taken[37]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickPopup::insetChange(newInset, oldInset);
  }

  //  QFont QQuickPopup::defaultFont() const
  QFont defaultFont() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickDialogCall38 call = reinterpret_cast<CuteQQuickDialogCall38>(taken[38]);
      const QFont * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopup::defaultFont();
  }

  //  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
  QQuickItem *safeAreaAttachmentItem() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickDialogCall39 call = reinterpret_cast<CuteQQuickDialogCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickPopup::safeAreaAttachmentItem();
  }

  //  QQuickItem *QQuickPopup::attacheeItem() const
  QQuickItem *attacheeItem() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickDialogCall40 call = reinterpret_cast<CuteQQuickDialogCall40>(taken[40]);
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
    if (taken[41]) {
      int handled = 0;
      CuteQQuickDialogCall41 call = reinterpret_cast<CuteQQuickDialogCall41>(taken[41]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickPopup::attachedParent(attachedType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickDialogCall42 call = reinterpret_cast<CuteQQuickDialogCall42>(taken[42]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickDialogCall43 call = reinterpret_cast<CuteQQuickDialogCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickDialogCall44 call = reinterpret_cast<CuteQQuickDialogCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickDialogCall45 call = reinterpret_cast<CuteQQuickDialogCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickDialogCall46 call = reinterpret_cast<CuteQQuickDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickDialogCall47 call = reinterpret_cast<CuteQQuickDialogCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickDialogCall48 call = reinterpret_cast<CuteQQuickDialogCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickDialog10metaObjectEv(
    const QQuickDialog *self) {
  return self->metaObject();
}

//  void *QQuickDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickDialog11qt_metacastEPKc(
    QQuickDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDialog::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN12QQuickDialog20qmlExtendedNamespaceEv() {
  return QQuickDialog::qmlExtendedNamespace();
}

//  void QQuickDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickDialog::QQuickDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZN12QQuickDialogC1EP7QObject(QObject *parent) {
  return new CuteQQuickDialog(parent);
}

//  QQuickDialog::~QQuickDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialogD1Ev(QQuickDialog *self) {
  delete self;
}

//  QString QQuickDialog::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQuickDialog5titleEv(const QQuickDialog *self) {
  return new QString(self->title());
}

//  void QQuickDialog::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog8setTitleERK7QString(
    QQuickDialog *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QQuickItem *QQuickDialog::header() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickDialog6headerEv(const QQuickDialog *self) {
  return self->header();
}

//  void QQuickDialog::setHeader(QQuickItem *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog9setHeaderEP10QQuickItem(
    QQuickDialog *self,
    QQuickItem *header) {
  self->setHeader(header);
}

//  QQuickItem *QQuickDialog::footer() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK12QQuickDialog6footerEv(const QQuickDialog *self) {
  return self->footer();
}

//  void QQuickDialog::setFooter(QQuickItem *footer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog9setFooterEP10QQuickItem(
    QQuickDialog *self,
    QQuickItem *footer) {
  self->setFooter(footer);
}

//  QPlatformDialogHelper::StandardButtons QQuickDialog::standardButtons()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickDialog15standardButtonsEv(const QQuickDialog *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  void
//      QQuickDialog::setStandardButtons(QPlatformDialogHelper::StandardButto
//      ns buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog18setStandardButtonsE6QFlagsIN21QPlatformDialogHelper14StandardButtonEE(
    QQuickDialog *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QPlatformDialogHelper::StandardButton>::fromInt(buttons));
}

//  QQuickAbstractButton
//      *QQuickDialog::standardButton(QPlatformDialogHelper::StandardButton
//      button) const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZNK12QQuickDialog14standardButtonEN21QPlatformDialogHelper14StandardButtonE(
    const QQuickDialog *self,
    QPlatformDialogHelper::StandardButton button) {
  return self->standardButton(button);
}

//  int QQuickDialog::result() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickDialog6resultEv(const QQuickDialog *self) {
  return self->result();
}

//  void QQuickDialog::setResult(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog9setResultEi(QQuickDialog *self, int result) {
  self->setResult(result);
}

//  qreal QQuickDialog::implicitHeaderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDialog19implicitHeaderWidthEv(
    const QQuickDialog *self) {
  return self->implicitHeaderWidth();
}

//  qreal QQuickDialog::implicitHeaderHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDialog20implicitHeaderHeightEv(
    const QQuickDialog *self) {
  return self->implicitHeaderHeight();
}

//  qreal QQuickDialog::implicitFooterWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDialog19implicitFooterWidthEv(
    const QQuickDialog *self) {
  return self->implicitFooterWidth();
}

//  qreal QQuickDialog::implicitFooterHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickDialog20implicitFooterHeightEv(
    const QQuickDialog *self) {
  return self->implicitFooterHeight();
}

//  void QQuickDialog::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog10setOpacityEd(
    QQuickDialog *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QQuickDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog6acceptEv(QQuickDialog *self) {
  self->accept();
}

//  void QQuickDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog6rejectEv(QQuickDialog *self) {
  self->reject();
}

//  void QQuickDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog4doneEi(QQuickDialog *self, int result) {
  self->done(result);
}

//  void QQuickDialog::accepted()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog8acceptedEv(QQuickDialog *self) {
  self->accepted();
}

//  void QQuickDialog::rejected()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog8rejectedEv(QQuickDialog *self) {
  self->rejected();
}

//  void QQuickDialog::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog12titleChangedEv(QQuickDialog *self) {
  self->titleChanged();
}

//  void QQuickDialog::headerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog13headerChangedEv(QQuickDialog *self) {
  self->headerChanged();
}

//  void QQuickDialog::footerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog13footerChangedEv(QQuickDialog *self) {
  self->footerChanged();
}

//  void QQuickDialog::standardButtonsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog22standardButtonsChangedEv(QQuickDialog *self) {
  self->standardButtonsChanged();
}

//  void QQuickDialog::applied()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog7appliedEv(QQuickDialog *self) {
  self->applied();
}

//  void QQuickDialog::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog5resetEv(QQuickDialog *self) {
  self->reset();
}

//  void QQuickDialog::discarded()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog9discardedEv(QQuickDialog *self) {
  self->discarded();
}

//  void QQuickDialog::helpRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog13helpRequestedEv(QQuickDialog *self) {
  self->helpRequested();
}

//  void QQuickDialog::resultChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog13resultChangedEv(QQuickDialog *self) {
  self->resultChanged();
}

//  void QQuickDialog::implicitHeaderWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog26implicitHeaderWidthChangedEv(
    QQuickDialog *self) {
  self->implicitHeaderWidthChanged();
}

//  void QQuickDialog::implicitHeaderHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog27implicitHeaderHeightChangedEv(
    QQuickDialog *self) {
  self->implicitHeaderHeightChanged();
}

//  void QQuickDialog::implicitFooterWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog26implicitFooterWidthChangedEv(
    QQuickDialog *self) {
  self->implicitFooterWidthChanged();
}

//  void QQuickDialog::implicitFooterHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog27implicitFooterHeightChangedEv(
    QQuickDialog *self) {
  self->implicitFooterHeightChanged();
}

//  QQuickDialog::QQuickDialog(QQuickDialogPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZN12QQuickDialogC1ER19QQuickDialogPrivateP7QObject(
    QQuickDialogPrivate *dd,
    QObject *parent) {
  return new CuteQQuickDialog(*dd, parent);
}

//  void QQuickDialog::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDialog *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDialog::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK12QQuickDialog14accessibleRoleEv(
    const QQuickDialog *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickDialog::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickDialog26accessibilityActiveChangedEb(
    QQuickDialog *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickDialogPrivate *QQuickDialog::d_func()
extern "C" Q_DECL_EXPORT
QQuickDialogPrivate *ritual_ZN12QQuickDialog6d_funcEv(QQuickDialog *self) {
  return self->d_func();
}

//  const QQuickDialogPrivate *QQuickDialog::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialogPrivate *ritual_ZNK12QQuickDialog6d_funcEv(
    const QQuickDialog *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDialog(
    QQuickDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDialog *>(self)->take(key, call);
}

//  void QQuickDialog::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog10setOpacityEd(
    QQuickDialog *self,
    qreal opacity) {
  self->QQuickDialog::setOpacity(opacity);
}

//  void QQuickDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog6acceptEv(QQuickDialog *self) {
  self->QQuickDialog::accept();
}

//  void QQuickDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog6rejectEv(QQuickDialog *self) {
  self->QQuickDialog::reject();
}

//  void QQuickDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog4doneEi(QQuickDialog *self, int result) {
  self->QQuickDialog::done(result);
}

//  void QQuickDialog::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickDialog *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickDialog *>(self)->OwnQQuickDialog::itemChange(
      change,
      *data);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDialog::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK12QQuickDialog14accessibleRoleEv(
    const QQuickDialog *self) {
  return static_cast<const OwnQQuickDialog *>(self)->OwnQQuickDialog::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickDialog::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickDialog26accessibilityActiveChangedEb(
    QQuickDialog *self,
    bool active) {
  static_cast<OwnQQuickDialog *>(self)->OwnQQuickDialog::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
