//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QTabWidgetPropertySheet::QTabWidgetPropertySheet(QTabWidget *object,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QTabWidgetPropertySheet *ritual_ZN23QTabWidgetPropertySheetC1EP10QTabWidgetP7QObject(
    QTabWidget *object,
    QObject *parent) {
  return new QTabWidgetPropertySheet(object, parent);
}

//  void QTabWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QTabWidgetPropertySheet11setPropertyEiRK8QVariant(
    QTabWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->setProperty(index, *value);
}

//  QVariant QTabWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QTabWidgetPropertySheet8propertyEi(
    const QTabWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->property(index));
}

//  bool QTabWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QTabWidgetPropertySheet5resetEi(
    QTabWidgetPropertySheet *self,
    int index) {
  return self->reset(index);
}

//  bool QTabWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QTabWidgetPropertySheet9isEnabledEi(
    const QTabWidgetPropertySheet *self,
    int index) {
  return self->isEnabled(index);
}

//  bool QTabWidgetPropertySheet::checkProperty(const QString &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QTabWidgetPropertySheet13checkPropertyERK7QString(
    const QString *propertyName) {
  return QTabWidgetPropertySheet::checkProperty(*propertyName);
}

//  TabWidgetProperty
//      QTabWidgetPropertySheet::tabWidgetPropertyFromName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QTabWidgetPropertySheet::TabWidgetProperty ritual_ZN23QTabWidgetPropertySheet25tabWidgetPropertyFromNameERK7QString(
    const QString *name) {
  return QTabWidgetPropertySheet::tabWidgetPropertyFromName(*name);
}

//  void QTabWidgetPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QTabWidgetPropertySheet11setPropertyEiRK8QVariant(
    QTabWidgetPropertySheet *self,
    int index,
    const QVariant *value) {
  self->QTabWidgetPropertySheet::setProperty(index, *value);
}

//  QVariant QTabWidgetPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QTabWidgetPropertySheet8propertyEi(
    const QTabWidgetPropertySheet *self,
    int index) {
  return new QVariant(self->QTabWidgetPropertySheet::property(index));
}

//  bool QTabWidgetPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QTabWidgetPropertySheet5resetEi(
    QTabWidgetPropertySheet *self,
    int index) {
  return self->QTabWidgetPropertySheet::reset(index);
}

//  bool QTabWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QTabWidgetPropertySheet9isEnabledEi(
    const QTabWidgetPropertySheet *self,
    int index) {
  return self->QTabWidgetPropertySheet::isEnabled(index);
}
