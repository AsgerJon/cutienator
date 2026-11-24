//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QToolBoxWidgetPropertySheet::QToolBoxWidgetPropertySheet(QToolBox
//      *object, QObject *parent)
extern "C" Q_DECL_EXPORT
QToolBoxWidgetPropertySheet *ritual_ZN27QToolBoxWidgetPropertySheetC1EP8QToolBoxP7QObject(
    QToolBox *object,
    QObject *parent) {
  return new QToolBoxWidgetPropertySheet(object, parent);
}

//  void QToolBoxWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QToolBoxWidgetPropertySheet11setPropertyEiRK8QVariant(
    QToolBoxWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->setProperty(index, *value);
}

//  QVariant QToolBoxWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QToolBoxWidgetPropertySheet8propertyEi(
    const QToolBoxWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->property(index));
}

//  bool QToolBoxWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QToolBoxWidgetPropertySheet5resetEi(
    QToolBoxWidgetPropertySheet *self,
    int index) {
  return self->reset(index);
}

//  bool QToolBoxWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QToolBoxWidgetPropertySheet9isEnabledEi(
    const QToolBoxWidgetPropertySheet *self,
    int index) {
  return self->isEnabled(index);
}

//  bool QToolBoxWidgetPropertySheet::checkProperty(const QString
//      &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QToolBoxWidgetPropertySheet13checkPropertyERK7QString(
    const QString *propertyName) {
  return QToolBoxWidgetPropertySheet::checkProperty(*propertyName);
}

//  ToolBoxProperty
//      QToolBoxWidgetPropertySheet::toolBoxPropertyFromName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QToolBoxWidgetPropertySheet::ToolBoxProperty ritual_ZN27QToolBoxWidgetPropertySheet23toolBoxPropertyFromNameERK7QString(
    const QString *name) {
  return QToolBoxWidgetPropertySheet::toolBoxPropertyFromName(*name);
}

//  void QToolBoxWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QToolBoxWidgetPropertySheet11setPropertyEiRK8QVariant(
    QToolBoxWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->QToolBoxWidgetPropertySheet::setProperty(index, *value);
}

//  QVariant QToolBoxWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK27QToolBoxWidgetPropertySheet8propertyEi(
    const QToolBoxWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->QToolBoxWidgetPropertySheet::property(index));
}

//  bool QToolBoxWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QToolBoxWidgetPropertySheet5resetEi(
    QToolBoxWidgetPropertySheet *self,
    int index) {
  return self->QToolBoxWidgetPropertySheet::reset(index);
}

//  bool QToolBoxWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QToolBoxWidgetPropertySheet9isEnabledEi(
    const QToolBoxWidgetPropertySheet *self,
    int index) {
  return self->QToolBoxWidgetPropertySheet::isEnabled(index);
}
