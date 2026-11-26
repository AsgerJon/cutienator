//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/promotiontaskmenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/promotiontaskmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *qdesigner_internal::PromotionTaskMenu::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17PromotionTaskMenu10metaObjectEv(
    const qdesigner_internal::PromotionTaskMenu *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::PromotionTaskMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal17PromotionTaskMenu11qt_metacastEPKc(
    qdesigner_internal::PromotionTaskMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::PromotionTaskMenu::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal17PromotionTaskMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::PromotionTaskMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::PromotionTaskMenu::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17PromotionTaskMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::PromotionTaskMenu::tr(s, c, n));
}

//  qdesigner_internal::PromotionTaskMenu::PromotionTaskMenu(QWidget *widget,
//      Mode mode, QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionTaskMenu *ritual_ZN18qdesigner_internal17PromotionTaskMenuC1EP7QWidgetNS0_4ModeEP7QObject(
    QWidget *widget,
    qdesigner_internal::PromotionTaskMenu::Mode mode,
    QObject *parent) {
  return new qdesigner_internal::PromotionTaskMenu(widget, mode, parent);
}

//  Mode qdesigner_internal::PromotionTaskMenu::mode() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionTaskMenu::Mode ritual_ZNK18qdesigner_internal17PromotionTaskMenu4modeEv(
    const qdesigner_internal::PromotionTaskMenu *self) {
  return self->mode();
}

//  void qdesigner_internal::PromotionTaskMenu::setMode(Mode m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu7setModeENS0_4ModeE(
    qdesigner_internal::PromotionTaskMenu *self,
    qdesigner_internal::PromotionTaskMenu::Mode m) {
  self->setMode(m);
}

//  void qdesigner_internal::PromotionTaskMenu::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu9setWidgetEP7QWidget(
    qdesigner_internal::PromotionTaskMenu *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  void qdesigner_internal::PromotionTaskMenu::setPromoteLabel(const QString
//      &promoteLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu15setPromoteLabelERK7QString(
    qdesigner_internal::PromotionTaskMenu *self,
    const QString *promoteLabel) {
  self->setPromoteLabel(*promoteLabel);
}

//  void qdesigner_internal::PromotionTaskMenu::setEditPromoteToLabel(const
//      QString &promoteEditLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu21setEditPromoteToLabelERK7QString(
    qdesigner_internal::PromotionTaskMenu *self,
    const QString *promoteEditLabel) {
  self->setEditPromoteToLabel(*promoteEditLabel);
}

//  void qdesigner_internal::PromotionTaskMenu::setDemoteLabel(const QString
//      &demoteLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu14setDemoteLabelERK7QString(
    qdesigner_internal::PromotionTaskMenu *self,
    const QString *demoteLabel) {
  self->setDemoteLabel(*demoteLabel);
}

//  void qdesigner_internal::PromotionTaskMenu::addActions(QDesignerFormWindo
//      wInterface *fw, unsigned int flags, ActionList &actionList)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEP28QDesignerFormWindowInterfacejR5QListIP7QActionE(
    qdesigner_internal::PromotionTaskMenu *self,
    QDesignerFormWindowInterface *fw,
    unsigned int flags,
    qdesigner_internal::PromotionTaskMenu::ActionList *actionList) {
  self->addActions(fw, flags, *actionList);
}

//  void qdesigner_internal::PromotionTaskMenu::addActions(unsigned int
//      flags, ActionList &actionList)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEjR5QListIP7QActionE(
    qdesigner_internal::PromotionTaskMenu *self,
    unsigned int flags,
    qdesigner_internal::PromotionTaskMenu::ActionList *actionList) {
  self->addActions(flags, *actionList);
}

//  void qdesigner_internal::PromotionTaskMenu::addActions(QDesignerFormWindo
//      wInterface *fw, unsigned int flags, QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEP28QDesignerFormWindowInterfacejP5QMenu(
    qdesigner_internal::PromotionTaskMenu *self,
    QDesignerFormWindowInterface *fw,
    unsigned int flags,
    QMenu *menu) {
  self->addActions(fw, flags, menu);
}

//  void qdesigner_internal::PromotionTaskMenu::addActions(unsigned int
//      flags, QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEjP5QMenu(
    qdesigner_internal::PromotionTaskMenu *self,
    unsigned int flags,
    QMenu *menu) {
  self->addActions(flags, menu);
}

//  void qdesigner_internal::PromotionTaskMenu::editPromotedWidgets(QDesigner
//      FormEditorInterface *core, QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu19editPromotedWidgetsEP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerFormEditorInterface *core,
    QWidget *parent) {
  qdesigner_internal::PromotionTaskMenu::editPromotedWidgets(core, parent);
}

//  void
//      qdesigner_internal::PromotionTaskMenu::slotPromoteToCustomWidget(cons
//      t QString &customClassName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu25slotPromoteToCustomWidgetERK7QString(
    qdesigner_internal::PromotionTaskMenu *self,
    const QString *customClassName) {
  self->slotPromoteToCustomWidget(*customClassName);
}

//  void qdesigner_internal::PromotionTaskMenu::slotDemoteFromCustomWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu26slotDemoteFromCustomWidgetEv(
    qdesigner_internal::PromotionTaskMenu *self) {
  self->slotDemoteFromCustomWidget();
}

//  void qdesigner_internal::PromotionTaskMenu::slotEditPromotedWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu23slotEditPromotedWidgetsEv(
    qdesigner_internal::PromotionTaskMenu *self) {
  self->slotEditPromotedWidgets();
}

//  void qdesigner_internal::PromotionTaskMenu::slotEditPromoteTo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu17slotEditPromoteToEv(
    qdesigner_internal::PromotionTaskMenu *self) {
  self->slotEditPromoteTo();
}

//  void qdesigner_internal::PromotionTaskMenu::slotEditSignalsSlots()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu20slotEditSignalsSlotsEv(
    qdesigner_internal::PromotionTaskMenu *self) {
  self->slotEditSignalsSlots();
}

//  void qdesigner_internal::PromotionTaskMenu::promoteTo(QDesignerFormWindow
//      Interface *fw, const QString &customClassName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17PromotionTaskMenu9promoteToEP28QDesignerFormWindowInterfaceRK7QString(
    qdesigner_internal::PromotionTaskMenu *self,
    QDesignerFormWindowInterface *fw,
    const QString *customClassName) {
  self->promoteTo(fw, *customClassName);
}

//  PromotionState qdesigner_internal::PromotionTaskMenu::createPromotionActi
//      ons(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionTaskMenu::PromotionState ritual_ZN18qdesigner_internal17PromotionTaskMenu22createPromotionActionsEP28QDesignerFormWindowInterface(
    qdesigner_internal::PromotionTaskMenu *self,
    QDesignerFormWindowInterface *formWindow) {
  return self->createPromotionActions(formWindow);
}

//  QDesignerFormWindowInterface
//      *qdesigner_internal::PromotionTaskMenu::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK18qdesigner_internal17PromotionTaskMenu10formWindowEv(
    const qdesigner_internal::PromotionTaskMenu *self) {
  return self->formWindow();
}

//  PromotionSelectionList qdesigner_internal::PromotionTaskMenu::promotionSe
//      lectionList(QDesignerFormWindowInterface *formWindow) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionTaskMenu::PromotionSelectionList *ritual_ZNK18qdesigner_internal17PromotionTaskMenu22promotionSelectionListEP28QDesignerFormWindowInterface(
    const qdesigner_internal::PromotionTaskMenu *self,
    QDesignerFormWindowInterface *formWindow) {
  return new qdesigner_internal::PromotionTaskMenu::PromotionSelectionList(
      self->promotionSelectionList(
          formWindow));
}

//  a qdesigner_internal::PromotionTaskMenu::PromotionSelectionList a ritual
//      of qdesigner_internal::PromotionTaskMenu gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_PromotionTaskMenu__qdesigner_internal_PromotionTaskMenu_PromotionSelectionList(
    qdesigner_internal::PromotionTaskMenu::PromotionSelectionList *self) {
  delete self;
}
