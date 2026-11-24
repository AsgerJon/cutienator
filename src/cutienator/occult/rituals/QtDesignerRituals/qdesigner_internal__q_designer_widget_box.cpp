//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *qdesigner_internal::QDesignerWidgetBox::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal18QDesignerWidgetBox10metaObjectEv(
    const qdesigner_internal::QDesignerWidgetBox *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::QDesignerWidgetBox::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal18QDesignerWidgetBox2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerWidgetBox::tr(s, c, n));
}

//  bool qdesigner_internal::QDesignerWidgetBox::loadContents(const QString
//      &contents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18QDesignerWidgetBox12loadContentsERK7QString(
    qdesigner_internal::QDesignerWidgetBox *self,
    const QString *contents) {
  return self->loadContents(*contents);
}

//  QIcon qdesigner_internal::QDesignerWidgetBox::iconForWidget(const QString
//      &className, const QString &category) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK18qdesigner_internal18QDesignerWidgetBox13iconForWidgetERK7QStringS3_(
    const qdesigner_internal::QDesignerWidgetBox *self,
    const QString *className,
    const QString *category) {
  return new QIcon(self->iconForWidget(*className, *category));
}
