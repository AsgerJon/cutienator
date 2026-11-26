//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QMessageDialogOptions::CustomButton::CustomButton(int id, const QString
//      &label, QPlatformDialogHelper::ButtonRole role, void *button)
extern "C" Q_DECL_EXPORT
QMessageDialogOptions::CustomButton *ritual_ZN21QMessageDialogOptions12CustomButtonC1EiRK7QStringN21QPlatformDialogHelper10ButtonRoleEPv(
    int id,
    const QString *label,
    QPlatformDialogHelper::ButtonRole role,
    void *button) {
  return new QMessageDialogOptions::CustomButton(id, *label, role, button);
}

//  QMessageDialogOptions::CustomButton::~CustomButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions12CustomButtonD1Ev(
    QMessageDialogOptions::CustomButton *self) {
  delete self;
}
