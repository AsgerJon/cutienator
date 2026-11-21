//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qaccessiblewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
//      QAccessible::Role role)
extern "C" Q_DECL_EXPORT
QAccessibleWidgetV2 *ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleE(
    QWidget *object,
    QAccessible::Role role) {
  return new QAccessibleWidgetV2(object, role);
}

//  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
//      QAccessible::Role role, const QString &name)
extern "C" Q_DECL_EXPORT
QAccessibleWidgetV2 *ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleERK7QString(
    QWidget *object,
    QAccessible::Role role,
    const QString *name) {
  return new QAccessibleWidgetV2(object, role, *name);
}

//  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessible9AttributeE(
    const QAccessibleWidgetV2 *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}
