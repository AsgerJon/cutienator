//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::PropertySheetPixmapValue::PropertySheetPixmapValue(co
//      nst QString &path)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue *ritual_ZN18qdesigner_internal24PropertySheetPixmapValueC1ERK7QString(
    const QString *path) {
  return new qdesigner_internal::PropertySheetPixmapValue(*path);
}

//  qdesigner_internal::PropertySheetPixmapValue::PropertySheetPixmapValue()
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue *ritual_ZN18qdesigner_internal24PropertySheetPixmapValueC1Ev() {
  return new qdesigner_internal::PropertySheetPixmapValue();
}

//  PixmapSource qdesigner_internal::PropertySheetPixmapValue::getPixmapSourc
//      e(QDesignerFormEditorInterface *core, const QString &path)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue::PixmapSource ritual_ZN18qdesigner_internal24PropertySheetPixmapValue15getPixmapSourceEP28QDesignerFormEditorInterfaceRK7QString(
    QDesignerFormEditorInterface *core,
    const QString *path) {
  return qdesigner_internal::PropertySheetPixmapValue::getPixmapSource(
      core,
      *path);
}

//  PixmapSource qdesigner_internal::PropertySheetPixmapValue::pixmapSource(Q
//      DesignerFormEditorInterface *core) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue::PixmapSource ritual_ZNK18qdesigner_internal24PropertySheetPixmapValue12pixmapSourceEP28QDesignerFormEditorInterface(
    const qdesigner_internal::PropertySheetPixmapValue *self,
    QDesignerFormEditorInterface *core) {
  return self->pixmapSource(core);
}

//  QString qdesigner_internal::PropertySheetPixmapValue::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal24PropertySheetPixmapValue4pathEv(
    const qdesigner_internal::PropertySheetPixmapValue *self) {
  return new QString(self->path());
}

//  void qdesigner_internal::PropertySheetPixmapValue::setPath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24PropertySheetPixmapValue7setPathERK7QString(
    qdesigner_internal::PropertySheetPixmapValue *self,
    const QString *path) {
  self->setPath(*path);
}

//  bool operator==(const PropertySheetPixmapValue &lhs, const
//      PropertySheetPixmapValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_24PropertySheetPixmapValueES2_(
    const qdesigner_internal::PropertySheetPixmapValue *lhs,
    const qdesigner_internal::PropertySheetPixmapValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetPixmapValue &lhs, const
//      PropertySheetPixmapValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_24PropertySheetPixmapValueES2_(
    const qdesigner_internal::PropertySheetPixmapValue *lhs,
    const qdesigner_internal::PropertySheetPixmapValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetPixmapValue::~PropertySheetPixmapValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24PropertySheetPixmapValueD1Ev(
    qdesigner_internal::PropertySheetPixmapValue *self) {
  delete self;
}
