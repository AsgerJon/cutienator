//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QToolBoxHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QToolBoxHelper10metaObjectEv(
    const QToolBoxHelper *self) {
  return self->metaObject();
}

//  QString QToolBoxHelper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QToolBoxHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QToolBoxHelper::tr(s, c, n));
}

//  QToolBoxHelper::QToolBoxHelper(QToolBox *toolbox)
extern "C" Q_DECL_EXPORT
QToolBoxHelper *ritual_ZN14QToolBoxHelperC1EP8QToolBox(QToolBox *toolbox) {
  return new QToolBoxHelper(toolbox);
}

//  void QToolBoxHelper::install(QToolBox *toolbox)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper7installEP8QToolBox(QToolBox *toolbox) {
  QToolBoxHelper::install(toolbox);
}

//  QToolBoxHelper *QToolBoxHelper::helperOf(const QToolBox *toolbox)
extern "C" Q_DECL_EXPORT
QToolBoxHelper *ritual_ZN14QToolBoxHelper8helperOfEPK8QToolBox(
    const QToolBox *toolbox) {
  return QToolBoxHelper::helperOf(toolbox);
}

//  QMenu *QToolBoxHelper::addToolBoxContextMenuActions(const QToolBox
//      *toolbox, QMenu *popup)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QToolBoxHelper28addToolBoxContextMenuActionsEPK8QToolBoxP5QMenu(
    const QToolBox *toolbox,
    QMenu *popup) {
  return QToolBoxHelper::addToolBoxContextMenuActions(toolbox, popup);
}

//  QPalette::ColorRole QToolBoxHelper::currentItemBackgroundRole() const
extern "C" Q_DECL_EXPORT
QPalette::ColorRole ritual_ZNK14QToolBoxHelper25currentItemBackgroundRoleEv(
    const QToolBoxHelper *self) {
  return self->currentItemBackgroundRole();
}

//  void QToolBoxHelper::setCurrentItemBackgroundRole(QPalette::ColorRole
//      role)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper28setCurrentItemBackgroundRoleEN8QPalette9ColorRoleE(
    QToolBoxHelper *self,
    QPalette::ColorRole role) {
  self->setCurrentItemBackgroundRole(role);
}

//  bool QToolBoxHelper::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QToolBoxHelper11eventFilterEP7QObjectP6QEvent(
    QToolBoxHelper *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  QMenu *QToolBoxHelper::addContextMenuActions(QMenu *popup) const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK14QToolBoxHelper21addContextMenuActionsEP5QMenu(
    const QToolBoxHelper *self,
    QMenu *popup) {
  return self->addContextMenuActions(popup);
}

//  void QToolBoxHelper::removeCurrentPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper17removeCurrentPageEv(QToolBoxHelper *self) {
  self->removeCurrentPage();
}

//  void QToolBoxHelper::addPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper7addPageEv(QToolBoxHelper *self) {
  self->addPage();
}

//  void QToolBoxHelper::addPageAfter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper12addPageAfterEv(QToolBoxHelper *self) {
  self->addPageAfter();
}

//  void QToolBoxHelper::changeOrder()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBoxHelper11changeOrderEv(QToolBoxHelper *self) {
  self->changeOrder();
}

//  bool QToolBoxHelper::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QToolBoxHelper11eventFilterEP7QObjectP6QEvent(
    QToolBoxHelper *self,
    QObject *watched,
    QEvent *event) {
  return self->QToolBoxHelper::eventFilter(watched, event);
}
