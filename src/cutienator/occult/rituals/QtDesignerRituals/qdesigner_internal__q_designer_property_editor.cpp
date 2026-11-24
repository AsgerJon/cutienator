//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertyeditor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertyeditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *qdesigner_internal::QDesignerPropertyEditor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal23QDesignerPropertyEditor10metaObjectEv(
    const qdesigner_internal::QDesignerPropertyEditor *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::QDesignerPropertyEditor::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal23QDesignerPropertyEditor2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      qdesigner_internal::QDesignerPropertyEditor::tr(
          s,
          c,
          n));
}

//  void qdesigner_internal::QDesignerPropertyEditor::updatePropertySheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor19updatePropertySheetEv(
    qdesigner_internal::QDesignerPropertyEditor *self) {
  self->updatePropertySheet();
}

//  void
//      qdesigner_internal::QDesignerPropertyEditor::reloadResourceProperties
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor24reloadResourcePropertiesEv(
    qdesigner_internal::QDesignerPropertyEditor *self) {
  self->reloadResourceProperties();
}
