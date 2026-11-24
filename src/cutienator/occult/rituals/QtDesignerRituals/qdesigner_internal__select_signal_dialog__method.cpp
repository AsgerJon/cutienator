//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/selectsignaldialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/selectsignaldialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  qdesigner_internal::SelectSignalDialog::Method::Method()
extern "C" Q_DECL_EXPORT
qdesigner_internal::SelectSignalDialog::Method *ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodC1Ev() {
  return new qdesigner_internal::SelectSignalDialog::Method();
}

//  qdesigner_internal::SelectSignalDialog::Method::Method(const QString &c,
//      const QString &s, const QStringList &p)
extern "C" Q_DECL_EXPORT
qdesigner_internal::SelectSignalDialog::Method *ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodC1ERK7QStringS4_RK5QListIS2_E(
    const QString *c,
    const QString *s,
    const QList<QString> *p) {
  return new qdesigner_internal::SelectSignalDialog::Method(*c, *s, *p);
}

//  bool qdesigner_internal::SelectSignalDialog::Method::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal18SelectSignalDialog6Method7isValidEv(
    const qdesigner_internal::SelectSignalDialog::Method *self) {
  return self->isValid();
}

//  qdesigner_internal::SelectSignalDialog::Method::~Method()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodD1Ev(
    qdesigner_internal::SelectSignalDialog::Method *self) {
  delete self;
}
