//  Written by hand on 2026-11-25 from
//  QtHelp/6.12.0/QtHelp/private/qfilternamedialog_p.h, Qt 6.12.0, as the
//  Qt of macOS and of Windows install it, and that of Linux alike. Kept
//  as it is when the generator runs again. Its header includes
//  "ui_qfilternamedialog.h", which an installed Qt keeps in the folder
//  QtHelp itself. Qt's library offers nothing of this class by name:
//  only its virtual functions are called, through the object, and what
//  its header writes out. Not written: the constructor, 'tr',
//  'setFilterName' and the slot 'updateOkButton', which Qt's library
//  offers not.
#include <QtHelp/qhelp_global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/6.12.0/QtHelp/private/qfilternamedialog_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QFilterNameDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QFilterNameDialog10metaObjectEv(
    const QFilterNameDialog *self) {
  return self->metaObject();
}

//  QFilterNameDialog::~QFilterNameDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFilterNameDialogD1Ev(QFilterNameDialog *self) {
  delete self;
}

//  QString QFilterNameDialog::filterName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QFilterNameDialog10filterNameEv(
    const QFilterNameDialog *self) {
  return new QString(self->filterName());
}
