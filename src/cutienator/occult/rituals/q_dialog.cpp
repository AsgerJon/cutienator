//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QDialog10metaObjectEv(const QDialog *self) {
  return self->metaObject();
}

//  QString QDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QDialog2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDialog::tr(s, c, n));
}

//  QDialog::QDialog(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN7QDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QDialog(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QDialog::~QDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialogD1Ev(QDialog *self) {
  delete self;
}

//  int QDialog::result() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QDialog6resultEv(const QDialog *self) {
  return self->result();
}

//  void QDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog10setVisibleEb(QDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QSize QDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QDialog8sizeHintEv(const QDialog *self) {
  return new QSize(self->sizeHint());
}

//  QSize QDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QDialog15minimumSizeHintEv(const QDialog *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDialog::setSizeGripEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog18setSizeGripEnabledEb(QDialog *self, bool a0) {
  self->setSizeGripEnabled(a0);
}

//  bool QDialog::isSizeGripEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QDialog17isSizeGripEnabledEv(const QDialog *self) {
  return self->isSizeGripEnabled();
}

//  void QDialog::setModal(bool modal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog8setModalEb(QDialog *self, bool modal) {
  self->setModal(modal);
}

//  void QDialog::setResult(int r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog9setResultEi(QDialog *self, int r) {
  self->setResult(r);
}

//  void QDialog::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog4openEv(QDialog *self) {
  self->open();
}

//  int QDialog::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QDialog4execEv(QDialog *self) {
  return self->exec();
}

//  void QDialog::done(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog4doneEi(QDialog *self, int a0) {
  self->done(a0);
}

//  void QDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog6acceptEv(QDialog *self) {
  self->accept();
}

//  void QDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog6rejectEv(QDialog *self) {
  self->reject();
}
