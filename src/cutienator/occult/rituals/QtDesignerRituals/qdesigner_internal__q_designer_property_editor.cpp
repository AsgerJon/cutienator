//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertyeditor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertyeditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/QString>

//  const QMetaObject
//      *qdesigner_internal::QDesignerPropertyEditor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal23QDesignerPropertyEditor10metaObjectEv(
    const qdesigner_internal::QDesignerPropertyEditor *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerPropertyEditor::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal23QDesignerPropertyEditor11qt_metacastEPKc(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::QDesignerPropertyEditor::qt_metacall(QMetaObject:
//      :Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal23QDesignerPropertyEditor11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::QDesignerPropertyEditor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  StringPropertyParameters qdesigner_internal::QDesignerPropertyEditor::tex
//      tPropertyValidationMode(QDesignerFormEditorInterface *core, const
//      QObject *object, const QString &propertyName, bool isMainContainer)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerPropertyEditor::StringPropertyParameters *ritual_ZN18qdesigner_internal23QDesignerPropertyEditor26textPropertyValidationModeEP28QDesignerFormEditorInterfacePK7QObjectRK7QStringb(
    QDesignerFormEditorInterface *core,
    const QObject *object,
    const QString *propertyName,
    bool isMainContainer) {
  return new qdesigner_internal::QDesignerPropertyEditor::StringPropertyParameters(
      qdesigner_internal::QDesignerPropertyEditor::textPropertyValidationMode(
          core,
          object,
          *propertyName,
          isMainContainer));
}

//  void
//      qdesigner_internal::QDesignerPropertyEditor::propertyValueChanged(con
//      st QString &name, const QVariant &value, bool
//      enableSubPropertyHandling)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor20propertyValueChangedERK7QStringRK8QVariantb(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name,
    const QVariant *value,
    bool enableSubPropertyHandling) {
  self->propertyValueChanged(*name, *value, enableSubPropertyHandling);
}

//  void qdesigner_internal::QDesignerPropertyEditor::resetProperty(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor13resetPropertyERK7QString(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name) {
  self->resetProperty(*name);
}

//  void
//      qdesigner_internal::QDesignerPropertyEditor::addDynamicProperty(const
//      QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor18addDynamicPropertyERK7QStringRK8QVariant(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name,
    const QVariant *value) {
  self->addDynamicProperty(*name, *value);
}

//  void
//      qdesigner_internal::QDesignerPropertyEditor::removeDynamicProperty(co
//      nst QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor21removeDynamicPropertyERK7QString(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name) {
  self->removeDynamicProperty(*name);
}

//  void qdesigner_internal::QDesignerPropertyEditor::editorOpened()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor12editorOpenedEv(
    qdesigner_internal::QDesignerPropertyEditor *self) {
  self->editorOpened();
}

//  void qdesigner_internal::QDesignerPropertyEditor::editorClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor12editorClosedEv(
    qdesigner_internal::QDesignerPropertyEditor *self) {
  self->editorClosed();
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

//  void
//      qdesigner_internal::QDesignerPropertyEditor::slotPropertyChanged(cons
//      t QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor19slotPropertyChangedERK7QStringRK8QVariant(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name,
    const QVariant *value) {
  self->slotPropertyChanged(*name, *value);
}

//  void qdesigner_internal::QDesignerPropertyEditor::emitPropertyValueChange
//      d(const QString &name, const QVariant &value, bool
//      enableSubPropertyHandling)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerPropertyEditor24emitPropertyValueChangedERK7QStringRK8QVariantb(
    qdesigner_internal::QDesignerPropertyEditor *self,
    const QString *name,
    const QVariant *value,
    bool enableSubPropertyHandling) {
  self->emitPropertyValueChanged(*name, *value, enableSubPropertyHandling);
}

//  a qdesigner_internal::QDesignerPropertyEditor::StringPropertyParameters a
//      ritual of qdesigner_internal::QDesignerPropertyEditor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_QDesignerPropertyEditor__qdesigner_internal_QDesignerPropertyEditor_StringPropertyParameters(
    qdesigner_internal::QDesignerPropertyEditor::StringPropertyParameters *self) {
  delete self;
}
