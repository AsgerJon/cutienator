//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/stylesheeteditor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/stylesheeteditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *qdesigner_internal::StyleSheetPropertyEditorDialog::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal30StyleSheetPropertyEditorDialog10metaObjectEv(
    const qdesigner_internal::StyleSheetPropertyEditorDialog *self) {
  return self->metaObject();
}

//  void
//      *qdesigner_internal::StyleSheetPropertyEditorDialog::qt_metacast(cons
//      t char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal30StyleSheetPropertyEditorDialog11qt_metacastEPKc(
    qdesigner_internal::StyleSheetPropertyEditorDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::StyleSheetPropertyEditorDialog::qt_metacall(QMeta
//      Object::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal30StyleSheetPropertyEditorDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::StyleSheetPropertyEditorDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::StyleSheetPropertyEditorDialog::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal30StyleSheetPropertyEditorDialog2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      qdesigner_internal::StyleSheetPropertyEditorDialog::tr(
          s,
          c,
          n));
}

//  qdesigner_internal::StyleSheetPropertyEditorDialog::StyleSheetPropertyEdi
//      torDialog(QWidget *parent, QDesignerFormWindowInterface *fw, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
qdesigner_internal::StyleSheetPropertyEditorDialog *ritual_ZN18qdesigner_internal30StyleSheetPropertyEditorDialogC1EP7QWidgetP28QDesignerFormWindowInterfaceS2_(
    QWidget *parent,
    QDesignerFormWindowInterface *fw,
    QWidget *widget) {
  return new qdesigner_internal::StyleSheetPropertyEditorDialog(
      parent,
      fw,
      widget);
}

//  void
//      qdesigner_internal::StyleSheetPropertyEditorDialog::applyStyleSheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal30StyleSheetPropertyEditorDialog15applyStyleSheetEv(
    qdesigner_internal::StyleSheetPropertyEditorDialog *self) {
  self->applyStyleSheet();
}
