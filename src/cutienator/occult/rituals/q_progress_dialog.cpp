//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qprogressdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qprogressdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QProgressDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QProgressDialog10metaObjectEv(
    const QProgressDialog *self) {
  return self->metaObject();
}

//  QString QProgressDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QProgressDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProgressDialog::tr(s, c, n));
}

//  QProgressDialog::QProgressDialog(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QProgressDialog *ritual_ZN15QProgressDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QProgressDialog(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QProgressDialog::QProgressDialog(const QString &labelText, const QString
//      &cancelButtonText, int minimum, int maximum, QWidget *parent,
//      Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QProgressDialog *ritual_ZN15QProgressDialogC1ERK7QStringS2_iiP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *labelText,
    const QString *cancelButtonText,
    int minimum,
    int maximum,
    QWidget *parent,
    int flags) {
  return new QProgressDialog(
      *labelText,
      *cancelButtonText,
      minimum,
      maximum,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QProgressDialog::~QProgressDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialogD1Ev(QProgressDialog *self) {
  delete self;
}

//  void QProgressDialog::setLabel(QLabel *label)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setLabelEP6QLabel(
    QProgressDialog *self,
    QLabel *label) {
  self->setLabel(label);
}

//  void QProgressDialog::setCancelButton(QPushButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog15setCancelButtonEP11QPushButton(
    QProgressDialog *self,
    QPushButton *button) {
  self->setCancelButton(button);
}

//  void QProgressDialog::setBar(QProgressBar *bar)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog6setBarEP12QProgressBar(
    QProgressDialog *self,
    QProgressBar *bar) {
  self->setBar(bar);
}

//  bool QProgressDialog::wasCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog11wasCanceledEv(
    const QProgressDialog *self) {
  return self->wasCanceled();
}

//  int QProgressDialog::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog7minimumEv(const QProgressDialog *self) {
  return self->minimum();
}

//  int QProgressDialog::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog7maximumEv(const QProgressDialog *self) {
  return self->maximum();
}

//  int QProgressDialog::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog5valueEv(const QProgressDialog *self) {
  return self->value();
}

//  QSize QProgressDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QProgressDialog8sizeHintEv(const QProgressDialog *self) {
  return new QSize(self->sizeHint());
}

//  QString QProgressDialog::labelText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QProgressDialog9labelTextEv(
    const QProgressDialog *self) {
  return new QString(self->labelText());
}

//  int QProgressDialog::minimumDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QProgressDialog15minimumDurationEv(
    const QProgressDialog *self) {
  return self->minimumDuration();
}

//  void QProgressDialog::setAutoReset(bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setAutoResetEb(
    QProgressDialog *self,
    bool reset) {
  self->setAutoReset(reset);
}

//  bool QProgressDialog::autoReset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog9autoResetEv(const QProgressDialog *self) {
  return self->autoReset();
}

//  void QProgressDialog::setAutoClose(bool close)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setAutoCloseEb(
    QProgressDialog *self,
    bool close) {
  self->setAutoClose(close);
}

//  bool QProgressDialog::autoClose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QProgressDialog9autoCloseEv(const QProgressDialog *self) {
  return self->autoClose();
}

//  void QProgressDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog4openEP7QObjectPKc(
    QProgressDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QProgressDialog::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog6cancelEv(QProgressDialog *self) {
  self->cancel();
}

//  void QProgressDialog::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog5resetEv(QProgressDialog *self) {
  self->reset();
}

//  void QProgressDialog::setMaximum(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog10setMaximumEi(
    QProgressDialog *self,
    int maximum) {
  self->setMaximum(maximum);
}

//  void QProgressDialog::setMinimum(int minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog10setMinimumEi(
    QProgressDialog *self,
    int minimum) {
  self->setMinimum(minimum);
}

//  void QProgressDialog::setRange(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setRangeEii(
    QProgressDialog *self,
    int minimum,
    int maximum) {
  self->setRange(minimum, maximum);
}

//  void QProgressDialog::setValue(int progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog8setValueEi(
    QProgressDialog *self,
    int progress) {
  self->setValue(progress);
}

//  void QProgressDialog::setLabelText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog12setLabelTextERK7QString(
    QProgressDialog *self,
    const QString *text) {
  self->setLabelText(*text);
}

//  void QProgressDialog::setCancelButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog19setCancelButtonTextERK7QString(
    QProgressDialog *self,
    const QString *text) {
  self->setCancelButtonText(*text);
}

//  void QProgressDialog::setMinimumDuration(int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProgressDialog18setMinimumDurationEi(
    QProgressDialog *self,
    int ms) {
  self->setMinimumDuration(ms);
}
