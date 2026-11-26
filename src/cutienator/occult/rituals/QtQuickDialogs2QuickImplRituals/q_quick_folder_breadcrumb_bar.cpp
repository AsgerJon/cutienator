//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumb
//  bar_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickFolderBreadcrumbBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFolderBreadcrumbBar : QQuickFolderBreadcrumbBar {
  using QQuickFolderBreadcrumbBar::event;
  using QQuickFolderBreadcrumbBar::keyPressEvent;
  using QQuickFolderBreadcrumbBar::componentComplete;
  using QQuickFolderBreadcrumbBar::itemChange;
  using QQuickFolderBreadcrumbBar::isContent;
  using QQuickFolderBreadcrumbBar::defaultFont;
  using QQuickFolderBreadcrumbBar::accessibleRole;
};

//  const QMetaObject *QQuickFolderBreadcrumbBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickFolderBreadcrumbBar10metaObjectEv(
    const QQuickFolderBreadcrumbBar *self) {
  return self->metaObject();
}

//  void *QQuickFolderBreadcrumbBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickFolderBreadcrumbBar11qt_metacastEPKc(
    QQuickFolderBreadcrumbBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFolderBreadcrumbBar::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickFolderBreadcrumbBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFolderBreadcrumbBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFolderBreadcrumbBar::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickFolderBreadcrumbBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFolderBreadcrumbBar::tr(s, c, n));
}

//  QQuickFolderBreadcrumbBar::QQuickFolderBreadcrumbBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFolderBreadcrumbBar *ritual_ZN25QQuickFolderBreadcrumbBarC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFolderBreadcrumbBar(parent);
}

//  QQuickDialog *QQuickFolderBreadcrumbBar::dialog() const
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZNK25QQuickFolderBreadcrumbBar6dialogEv(
    const QQuickFolderBreadcrumbBar *self) {
  return self->dialog();
}

//  void QQuickFolderBreadcrumbBar::setDialog(QQuickDialog *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar9setDialogEP12QQuickDialog(
    QQuickFolderBreadcrumbBar *self,
    QQuickDialog *dialog) {
  self->setDialog(dialog);
}

//  QQmlComponent *QQuickFolderBreadcrumbBar::buttonDelegate()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN25QQuickFolderBreadcrumbBar14buttonDelegateEv(
    QQuickFolderBreadcrumbBar *self) {
  return self->buttonDelegate();
}

//  void QQuickFolderBreadcrumbBar::setButtonDelegate(QQmlComponent
//      *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar17setButtonDelegateEP13QQmlComponent(
    QQuickFolderBreadcrumbBar *self,
    QQmlComponent *delegate) {
  self->setButtonDelegate(delegate);
}

//  QQmlComponent *QQuickFolderBreadcrumbBar::separatorDelegate()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN25QQuickFolderBreadcrumbBar17separatorDelegateEv(
    QQuickFolderBreadcrumbBar *self) {
  return self->separatorDelegate();
}

//  void QQuickFolderBreadcrumbBar::setSeparatorDelegate(QQmlComponent
//      *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar20setSeparatorDelegateEP13QQmlComponent(
    QQuickFolderBreadcrumbBar *self,
    QQmlComponent *delegate) {
  self->setSeparatorDelegate(delegate);
}

//  QQuickAbstractButton *QQuickFolderBreadcrumbBar::upButton()
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZN25QQuickFolderBreadcrumbBar8upButtonEv(
    QQuickFolderBreadcrumbBar *self) {
  return self->upButton();
}

//  void QQuickFolderBreadcrumbBar::setUpButton(QQuickAbstractButton
//      *upButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar11setUpButtonEP20QQuickAbstractButton(
    QQuickFolderBreadcrumbBar *self,
    QQuickAbstractButton *upButton) {
  self->setUpButton(upButton);
}

//  int QQuickFolderBreadcrumbBar::upButtonSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuickFolderBreadcrumbBar15upButtonSpacingEv(
    const QQuickFolderBreadcrumbBar *self) {
  return self->upButtonSpacing();
}

//  void QQuickFolderBreadcrumbBar::setUpButtonSpacing(int upButtonSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar18setUpButtonSpacingEi(
    QQuickFolderBreadcrumbBar *self,
    int upButtonSpacing) {
  self->setUpButtonSpacing(upButtonSpacing);
}

//  QQuickTextField *QQuickFolderBreadcrumbBar::textField()
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZN25QQuickFolderBreadcrumbBar9textFieldEv(
    QQuickFolderBreadcrumbBar *self) {
  return self->textField();
}

//  void QQuickFolderBreadcrumbBar::setTextField(QQuickTextField *textField)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar12setTextFieldEP15QQuickTextField(
    QQuickFolderBreadcrumbBar *self,
    QQuickTextField *textField) {
  self->setTextField(textField);
}

//  void QQuickFolderBreadcrumbBar::dialogChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar13dialogChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->dialogChanged();
}

//  void QQuickFolderBreadcrumbBar::buttonDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar21buttonDelegateChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->buttonDelegateChanged();
}

//  void QQuickFolderBreadcrumbBar::separatorDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar24separatorDelegateChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->separatorDelegateChanged();
}

//  void QQuickFolderBreadcrumbBar::upButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar15upButtonChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->upButtonChanged();
}

//  void QQuickFolderBreadcrumbBar::upButtonSpacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar22upButtonSpacingChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->upButtonSpacingChanged();
}

//  void QQuickFolderBreadcrumbBar::textFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar16textFieldChangedEv(
    QQuickFolderBreadcrumbBar *self) {
  self->textFieldChanged();
}

//  bool QQuickFolderBreadcrumbBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickFolderBreadcrumbBar5eventEP6QEvent(
    QQuickFolderBreadcrumbBar *self,
    QEvent *event) {
  return self->event(event);
}

//  void QQuickFolderBreadcrumbBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar13keyPressEventEP9QKeyEvent(
    QQuickFolderBreadcrumbBar *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickFolderBreadcrumbBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar17componentCompleteEv(
    QQuickFolderBreadcrumbBar *self) {
  self->componentComplete();
}

//  void QQuickFolderBreadcrumbBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFolderBreadcrumbBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFolderBreadcrumbBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  bool QQuickFolderBreadcrumbBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickFolderBreadcrumbBar9isContentEP10QQuickItem(
    const QQuickFolderBreadcrumbBar *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  QFont QQuickFolderBreadcrumbBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK25QQuickFolderBreadcrumbBar11defaultFontEv(
    const QQuickFolderBreadcrumbBar *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickFolderBreadcrumbBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK25QQuickFolderBreadcrumbBar14accessibleRoleEv(
    const QQuickFolderBreadcrumbBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickFolderBreadcrumbBarPrivate *QQuickFolderBreadcrumbBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickFolderBreadcrumbBarPrivate *ritual_ZN25QQuickFolderBreadcrumbBar6d_funcEv(
    QQuickFolderBreadcrumbBar *self) {
  return self->d_func();
}

//  const QQuickFolderBreadcrumbBarPrivate
//      *QQuickFolderBreadcrumbBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFolderBreadcrumbBarPrivate *ritual_ZNK25QQuickFolderBreadcrumbBar6d_funcEv(
    const QQuickFolderBreadcrumbBar *self) {
  return self->d_func();
}

//  bool QQuickFolderBreadcrumbBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QQuickFolderBreadcrumbBar5eventEP6QEvent(
    QQuickFolderBreadcrumbBar *self,
    QEvent *event) {
  return static_cast<OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::event(
      event);
}

//  void QQuickFolderBreadcrumbBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFolderBreadcrumbBar13keyPressEventEP9QKeyEvent(
    QQuickFolderBreadcrumbBar *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::keyPressEvent(
      event);
}

//  void QQuickFolderBreadcrumbBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFolderBreadcrumbBar17componentCompleteEv(
    QQuickFolderBreadcrumbBar *self) {
  static_cast<OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::componentComplete();
}

//  void QQuickFolderBreadcrumbBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFolderBreadcrumbBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFolderBreadcrumbBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::itemChange(
      change,
      *data);
}

//  bool QQuickFolderBreadcrumbBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QQuickFolderBreadcrumbBar9isContentEP10QQuickItem(
    const QQuickFolderBreadcrumbBar *self,
    QQuickItem *item) {
  return static_cast<const OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::isContent(
      item);
}

//  QFont QQuickFolderBreadcrumbBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK25QQuickFolderBreadcrumbBar11defaultFontEv(
    const QQuickFolderBreadcrumbBar *self) {
  return new QFont(
      static_cast<const OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickFolderBreadcrumbBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK25QQuickFolderBreadcrumbBar14accessibleRoleEv(
    const QQuickFolderBreadcrumbBar *self) {
  return static_cast<const OwnQQuickFolderBreadcrumbBar *>(self)->OwnQQuickFolderBreadcrumbBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
