//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/morphmenu_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/morphmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *qdesigner_internal::MorphMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal9MorphMenu10metaObjectEv(
    const qdesigner_internal::MorphMenu *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::MorphMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal9MorphMenu11qt_metacastEPKc(
    qdesigner_internal::MorphMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::MorphMenu::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal9MorphMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::MorphMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::MorphMenu::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal9MorphMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::MorphMenu::tr(s, c, n));
}

//  qdesigner_internal::MorphMenu::MorphMenu(QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::MorphMenu *ritual_ZN18qdesigner_internal9MorphMenuC1EP7QObject(
    QObject *parent) {
  return new qdesigner_internal::MorphMenu(parent);
}

//  void qdesigner_internal::MorphMenu::populate(QWidget *w,
//      QDesignerFormWindowInterface *fw, ActionList &al)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal9MorphMenu8populateEP7QWidgetP28QDesignerFormWindowInterfaceR5QListIP7QActionE(
    qdesigner_internal::MorphMenu *self,
    QWidget *w,
    QDesignerFormWindowInterface *fw,
    qdesigner_internal::MorphMenu::ActionList *al) {
  self->populate(w, fw, *al);
}

//  void qdesigner_internal::MorphMenu::populate(QWidget *w,
//      QDesignerFormWindowInterface *fw, QMenu &m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal9MorphMenu8populateEP7QWidgetP28QDesignerFormWindowInterfaceR5QMenu(
    qdesigner_internal::MorphMenu *self,
    QWidget *w,
    QDesignerFormWindowInterface *fw,
    QMenu *m) {
  self->populate(w, fw, *m);
}

//  void qdesigner_internal::MorphMenu::slotMorph(const QString
//      &newClassName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal9MorphMenu9slotMorphERK7QString(
    qdesigner_internal::MorphMenu *self,
    const QString *newClassName) {
  self->slotMorph(*newClassName);
}

//  bool qdesigner_internal::MorphMenu::populateMenu(QWidget *w,
//      QDesignerFormWindowInterface *fw)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal9MorphMenu12populateMenuEP7QWidgetP28QDesignerFormWindowInterface(
    qdesigner_internal::MorphMenu *self,
    QWidget *w,
    QDesignerFormWindowInterface *fw) {
  return self->populateMenu(w, fw);
}
