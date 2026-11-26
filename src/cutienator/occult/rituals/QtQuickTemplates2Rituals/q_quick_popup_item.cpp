//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmargins.h>

//  Only a class built on QQuickPopupItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPopupItem : QQuickPopupItem {
  using QQuickPopupItem::updatePolish;
  using QQuickPopupItem::childMouseEventFilter;
  using QQuickPopupItem::focusInEvent;
  using QQuickPopupItem::focusOutEvent;
  using QQuickPopupItem::keyPressEvent;
  using QQuickPopupItem::keyReleaseEvent;
  using QQuickPopupItem::mousePressEvent;
  using QQuickPopupItem::mouseMoveEvent;
  using QQuickPopupItem::mouseReleaseEvent;
  using QQuickPopupItem::mouseDoubleClickEvent;
  using QQuickPopupItem::mouseUngrabEvent;
  using QQuickPopupItem::touchEvent;
  using QQuickPopupItem::touchUngrabEvent;
  using QQuickPopupItem::wheelEvent;
  using QQuickPopupItem::dragEnterEvent;
  using QQuickPopupItem::dragMoveEvent;
  using QQuickPopupItem::dragLeaveEvent;
  using QQuickPopupItem::dropEvent;
  using QQuickPopupItem::contentItemChange;
  using QQuickPopupItem::contentSizeChange;
  using QQuickPopupItem::fontChange;
  using QQuickPopupItem::geometryChange;
  using QQuickPopupItem::localeChange;
  using QQuickPopupItem::mirrorChange;
  using QQuickPopupItem::itemChange;
  using QQuickPopupItem::paddingChange;
  using QQuickPopupItem::insetChange;
  using QQuickPopupItem::spacingChange;
  using QQuickPopupItem::enabledChange;
  using QQuickPopupItem::defaultFont;
  using QQuickPopupItem::accessibleRole;
  using QQuickPopupItem::accessibilityActiveChanged;
};

//  const QMetaObject *QQuickPopupItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickPopupItem10metaObjectEv(
    const QQuickPopupItem *self) {
  return self->metaObject();
}

//  void *QQuickPopupItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickPopupItem11qt_metacastEPKc(
    QQuickPopupItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPopupItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickPopupItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPopupItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPopupItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickPopupItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPopupItem::tr(s, c, n));
}

//  QQuickPopupItem::QQuickPopupItem(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupItem *ritual_ZN15QQuickPopupItemC1EP11QQuickPopup(
    QQuickPopup *popup) {
  return new QQuickPopupItem(popup);
}

//  void QQuickPopupItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem12updatePolishEv(QQuickPopupItem *self) {
  self->updatePolish();
}

//  bool QQuickPopupItem::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickPopupItem21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPopupItem *self,
    QQuickItem *child,
    QEvent *event) {
  return self->childMouseEventFilter(child, event);
}

//  void QQuickPopupItem::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem12focusInEventEP11QFocusEvent(
    QQuickPopupItem *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickPopupItem::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13focusOutEventEP11QFocusEvent(
    QQuickPopupItem *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickPopupItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13keyPressEventEP9QKeyEvent(
    QQuickPopupItem *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickPopupItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem15keyReleaseEventEP9QKeyEvent(
    QQuickPopupItem *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickPopupItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem15mousePressEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickPopupItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem14mouseMoveEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickPopupItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem17mouseReleaseEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickPopupItem::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem21mouseDoubleClickEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickPopupItem::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem16mouseUngrabEventEv(QQuickPopupItem *self) {
  self->mouseUngrabEvent();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopupItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem10touchEventEP11QTouchEvent(
    QQuickPopupItem *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopupItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem16touchUngrabEventEv(QQuickPopupItem *self) {
  self->touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickPopupItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem10wheelEventEP11QWheelEvent(
    QQuickPopupItem *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem14dragEnterEventEP15QDragEnterEvent(
    QQuickPopupItem *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13dragMoveEventEP14QDragMoveEvent(
    QQuickPopupItem *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem14dragLeaveEventEP15QDragLeaveEvent(
    QQuickPopupItem *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem9dropEventEP10QDropEvent(
    QQuickPopupItem *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickPopupItem::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem17contentItemChangeEP10QQuickItemS1_(
    QQuickPopupItem *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  self->contentItemChange(newItem, oldItem);
}

//  void QQuickPopupItem::contentSizeChange(const QSizeF &newSize, const
//      QSizeF &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem17contentSizeChangeERK6QSizeFS2_(
    QQuickPopupItem *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  self->contentSizeChange(*newSize, *oldSize);
}

//  void QQuickPopupItem::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem10fontChangeERK5QFontS2_(
    QQuickPopupItem *self,
    const QFont *newFont,
    const QFont *oldFont) {
  self->fontChange(*newFont, *oldFont);
}

//  void QQuickPopupItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem14geometryChangeERK6QRectFS2_(
    QQuickPopupItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickPopupItem::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem12localeChangeERK7QLocaleS2_(
    QQuickPopupItem *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickPopupItem::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem12mirrorChangeEv(QQuickPopupItem *self) {
  self->mirrorChange();
}

//  void QQuickPopupItem::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPopupItem *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickPopupItem::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13paddingChangeERK9QMarginsFS2_(
    QQuickPopupItem *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  void QQuickPopupItem::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem11insetChangeERK9QMarginsFS2_(
    QQuickPopupItem *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  void QQuickPopupItem::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13spacingChangeEdd(
    QQuickPopupItem *self,
    qreal newSpacing,
    qreal oldSpacing) {
  self->spacingChange(newSpacing, oldSpacing);
}

//  void QQuickPopupItem::enabledChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem13enabledChangeEv(QQuickPopupItem *self) {
  self->enabledChange();
}

//  QFont QQuickPopupItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickPopupItem11defaultFontEv(
    const QQuickPopupItem *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPopupItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickPopupItem14accessibleRoleEv(
    const QQuickPopupItem *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPopupItem::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickPopupItem26accessibilityActiveChangedEb(
    QQuickPopupItem *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  QQuickPopupItemPrivate *QQuickPopupItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickPopupItemPrivate *ritual_ZN15QQuickPopupItem6d_funcEv(
    QQuickPopupItem *self) {
  return self->d_func();
}

//  const QQuickPopupItemPrivate *QQuickPopupItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopupItemPrivate *ritual_ZNK15QQuickPopupItem6d_funcEv(
    const QQuickPopupItem *self) {
  return self->d_func();
}

//  void QQuickPopupItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem12updatePolishEv(QQuickPopupItem *self) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::updatePolish();
}

//  bool QQuickPopupItem::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickPopupItem21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickPopupItem *self,
    QQuickItem *child,
    QEvent *event) {
  return static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::childMouseEventFilter(
      child,
      event);
}

//  void QQuickPopupItem::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem12focusInEventEP11QFocusEvent(
    QQuickPopupItem *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::focusInEvent(
      event);
}

//  void QQuickPopupItem::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13focusOutEventEP11QFocusEvent(
    QQuickPopupItem *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::focusOutEvent(
      event);
}

//  void QQuickPopupItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13keyPressEventEP9QKeyEvent(
    QQuickPopupItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::keyPressEvent(
      event);
}

//  void QQuickPopupItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem15keyReleaseEventEP9QKeyEvent(
    QQuickPopupItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::keyReleaseEvent(
      event);
}

//  void QQuickPopupItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem15mousePressEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mousePressEvent(
      event);
}

//  void QQuickPopupItem::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem14mouseMoveEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mouseMoveEvent(
      event);
}

//  void QQuickPopupItem::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem17mouseReleaseEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mouseReleaseEvent(
      event);
}

//  void QQuickPopupItem::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem21mouseDoubleClickEventEP11QMouseEvent(
    QQuickPopupItem *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mouseDoubleClickEvent(
      event);
}

//  void QQuickPopupItem::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem16mouseUngrabEventEv(
    QQuickPopupItem *self) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mouseUngrabEvent();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopupItem::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem10touchEventEP11QTouchEvent(
    QQuickPopupItem *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickPopupItem::touchUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem16touchUngrabEventEv(
    QQuickPopupItem *self) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::touchUngrabEvent();
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickPopupItem::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem10wheelEventEP11QWheelEvent(
    QQuickPopupItem *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem14dragEnterEventEP15QDragEnterEvent(
    QQuickPopupItem *self,
    QDragEnterEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::dragEnterEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13dragMoveEventEP14QDragMoveEvent(
    QQuickPopupItem *self,
    QDragMoveEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::dragMoveEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem14dragLeaveEventEP15QDragLeaveEvent(
    QQuickPopupItem *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::dragLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickPopupItem::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem9dropEventEP10QDropEvent(
    QQuickPopupItem *self,
    QDropEvent *event) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::dropEvent(
      event);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void QQuickPopupItem::contentItemChange(QQuickItem *newItem, QQuickItem
//      *oldItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem17contentItemChangeEP10QQuickItemS1_(
    QQuickPopupItem *self,
    QQuickItem *newItem,
    QQuickItem *oldItem) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::contentItemChange(
      newItem,
      oldItem);
}

//  void QQuickPopupItem::contentSizeChange(const QSizeF &newSize, const
//      QSizeF &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem17contentSizeChangeERK6QSizeFS2_(
    QQuickPopupItem *self,
    const QSizeF *newSize,
    const QSizeF *oldSize) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::contentSizeChange(
      *newSize,
      *oldSize);
}

//  void QQuickPopupItem::fontChange(const QFont &newFont, const QFont
//      &oldFont)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem10fontChangeERK5QFontS2_(
    QQuickPopupItem *self,
    const QFont *newFont,
    const QFont *oldFont) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::fontChange(
      *newFont,
      *oldFont);
}

//  void QQuickPopupItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem14geometryChangeERK6QRectFS2_(
    QQuickPopupItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickPopupItem::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem12localeChangeERK7QLocaleS2_(
    QQuickPopupItem *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::localeChange(
      *newLocale,
      *oldLocale);
}

//  void QQuickPopupItem::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem12mirrorChangeEv(QQuickPopupItem *self) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::mirrorChange();
}

//  void QQuickPopupItem::itemChange(ItemChange change, const ItemChangeData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickPopupItem *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::itemChange(
      change,
      *data);
}

//  void QQuickPopupItem::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13paddingChangeERK9QMarginsFS2_(
    QQuickPopupItem *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::paddingChange(
      *newPadding,
      *oldPadding);
}

//  void QQuickPopupItem::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem11insetChangeERK9QMarginsFS2_(
    QQuickPopupItem *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::insetChange(
      *newInset,
      *oldInset);
}

//  void QQuickPopupItem::spacingChange(qreal newSpacing, qreal oldSpacing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13spacingChangeEdd(
    QQuickPopupItem *self,
    qreal newSpacing,
    qreal oldSpacing) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::spacingChange(
      newSpacing,
      oldSpacing);
}

//  void QQuickPopupItem::enabledChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem13enabledChangeEv(QQuickPopupItem *self) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::enabledChange();
}

//  QFont QQuickPopupItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK15QQuickPopupItem11defaultFontEv(
    const QQuickPopupItem *self) {
  return new QFont(
      static_cast<const OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickPopupItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickPopupItem14accessibleRoleEv(
    const QQuickPopupItem *self) {
  return static_cast<const OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickPopupItem::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickPopupItem26accessibilityActiveChangedEb(
    QQuickPopupItem *self,
    bool active) {
  static_cast<OwnQQuickPopupItem *>(self)->OwnQQuickPopupItem::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)
