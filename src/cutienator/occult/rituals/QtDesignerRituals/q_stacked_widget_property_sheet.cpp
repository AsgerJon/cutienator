//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QStackedWidgetPropertySheet::QStackedWidgetPropertySheet(QStackedWidget
//      *object, QObject *parent)
extern "C" Q_DECL_EXPORT
QStackedWidgetPropertySheet *ritual_ZN27QStackedWidgetPropertySheetC1EP14QStackedWidgetP7QObject(
    QStackedWidget *object,
    QObject *parent) {
  return new QStackedWidgetPropertySheet(object, parent);
}

//  void QStackedWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QStackedWidgetPropertySheet11setPropertyEiRK8QVariant(
    QStackedWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->setProperty(index, *value);
}

//  QVariant QStackedWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QStackedWidgetPropertySheet8propertyEi(
    const QStackedWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->property(index));
}

//  bool QStackedWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QStackedWidgetPropertySheet5resetEi(
    QStackedWidgetPropertySheet *self,
    int index) {
  return self->reset(index);
}

//  bool QStackedWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QStackedWidgetPropertySheet9isEnabledEi(
    const QStackedWidgetPropertySheet *self,
    int index) {
  return self->isEnabled(index);
}

//  bool QStackedWidgetPropertySheet::checkProperty(const QString
//      &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QStackedWidgetPropertySheet13checkPropertyERK7QString(
    const QString *propertyName) {
  return QStackedWidgetPropertySheet::checkProperty(*propertyName);
}

//  void QStackedWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QStackedWidgetPropertySheet11setPropertyEiRK8QVariant(
    QStackedWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->QStackedWidgetPropertySheet::setProperty(index, *value);
}

//  QVariant QStackedWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK27QStackedWidgetPropertySheet8propertyEi(
    const QStackedWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->QStackedWidgetPropertySheet::property(index));
}

//  bool QStackedWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QStackedWidgetPropertySheet5resetEi(
    QStackedWidgetPropertySheet *self,
    int index) {
  return self->QStackedWidgetPropertySheet::reset(index);
}

//  bool QStackedWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QStackedWidgetPropertySheet9isEnabledEi(
    const QStackedWidgetPropertySheet *self,
    int index) {
  return self->QStackedWidgetPropertySheet::isEnabled(index);
}
