//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/formlayoutmenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/formlayoutmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *qdesigner_internal::FormLayoutMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14FormLayoutMenu10metaObjectEv(
    const qdesigner_internal::FormLayoutMenu *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::FormLayoutMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14FormLayoutMenu11qt_metacastEPKc(
    qdesigner_internal::FormLayoutMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::FormLayoutMenu::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14FormLayoutMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::FormLayoutMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::FormLayoutMenu::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14FormLayoutMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::FormLayoutMenu::tr(s, c, n));
}

//  qdesigner_internal::FormLayoutMenu::FormLayoutMenu(QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormLayoutMenu *ritual_ZN18qdesigner_internal14FormLayoutMenuC1EP7QObject(
    QObject *parent) {
  return new qdesigner_internal::FormLayoutMenu(parent);
}

//  void qdesigner_internal::FormLayoutMenu::populate(QWidget *w,
//      QDesignerFormWindowInterface *fw, ActionList &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormLayoutMenu8populateEP7QWidgetP28QDesignerFormWindowInterfaceR5QListIP7QActionE(
    qdesigner_internal::FormLayoutMenu *self,
    QWidget *w,
    QDesignerFormWindowInterface *fw,
    qdesigner_internal::FormLayoutMenu::ActionList *actions) {
  self->populate(w, fw, *actions);
}

//  QAction *qdesigner_internal::FormLayoutMenu::preferredEditAction(QWidget
//      *w, QDesignerFormWindowInterface *fw)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN18qdesigner_internal14FormLayoutMenu19preferredEditActionEP7QWidgetP28QDesignerFormWindowInterface(
    qdesigner_internal::FormLayoutMenu *self,
    QWidget *w,
    QDesignerFormWindowInterface *fw) {
  return self->preferredEditAction(w, fw);
}

//  void qdesigner_internal::FormLayoutMenu::slotAddRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14FormLayoutMenu10slotAddRowEv(
    qdesigner_internal::FormLayoutMenu *self) {
  self->slotAddRow();
}
