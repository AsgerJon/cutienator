//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qinputdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qinputdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QInputDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QInputDialog10metaObjectEv(
    const QInputDialog *self) {
  return self->metaObject();
}

//  QString QInputDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputDialog::tr(s, c, n));
}

//  QInputDialog::QInputDialog(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QInputDialog *ritual_ZN12QInputDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QInputDialog(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QInputDialog::~QInputDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialogD1Ev(QInputDialog *self) {
  delete self;
}

//  void QInputDialog::setInputMode(InputMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setInputModeENS_9InputModeE(
    QInputDialog *self,
    QInputDialog::InputMode mode) {
  self->setInputMode(mode);
}

//  InputMode QInputDialog::inputMode() const
extern "C" Q_DECL_EXPORT
QInputDialog::InputMode ritual_ZNK12QInputDialog9inputModeEv(
    const QInputDialog *self) {
  return self->inputMode();
}

//  void QInputDialog::setLabelText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setLabelTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setLabelText(*text);
}

//  QString QInputDialog::labelText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog9labelTextEv(const QInputDialog *self) {
  return new QString(self->labelText());
}

//  void QInputDialog::setOption(InputDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog9setOptionENS_17InputDialogOptionEb(
    QInputDialog *self,
    QInputDialog::InputDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QInputDialog::testOption(InputDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDialog10testOptionENS_17InputDialogOptionE(
    const QInputDialog *self,
    QInputDialog::InputDialogOption option) {
  return self->testOption(option);
}

//  void QInputDialog::setOptions(InputDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setOptionsE6QFlagsINS_17InputDialogOptionEE(
    QInputDialog *self,
    int options) {
  self->setOptions(
      QFlags<QInputDialog::InputDialogOption>::fromInt(options));
}

//  InputDialogOptions QInputDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog7optionsEv(const QInputDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QInputDialog::setTextValue(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setTextValueERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setTextValue(*text);
}

//  QString QInputDialog::textValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog9textValueEv(const QInputDialog *self) {
  return new QString(self->textValue());
}

//  void QInputDialog::setTextEchoMode(QLineEdit::EchoMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog15setTextEchoModeEN9QLineEdit8EchoModeE(
    QInputDialog *self,
    QLineEdit::EchoMode mode) {
  self->setTextEchoMode(mode);
}

//  QLineEdit::EchoMode QInputDialog::textEchoMode() const
extern "C" Q_DECL_EXPORT
QLineEdit::EchoMode ritual_ZNK12QInputDialog12textEchoModeEv(
    const QInputDialog *self) {
  return self->textEchoMode();
}

//  void QInputDialog::setComboBoxEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog19setComboBoxEditableEb(
    QInputDialog *self,
    bool editable) {
  self->setComboBoxEditable(editable);
}

//  bool QInputDialog::isComboBoxEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDialog18isComboBoxEditableEv(
    const QInputDialog *self) {
  return self->isComboBoxEditable();
}

//  void QInputDialog::setIntValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog11setIntValueEi(QInputDialog *self, int value) {
  self->setIntValue(value);
}

//  int QInputDialog::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog8intValueEv(const QInputDialog *self) {
  return self->intValue();
}

//  void QInputDialog::setIntMinimum(int min)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setIntMinimumEi(QInputDialog *self, int min) {
  self->setIntMinimum(min);
}

//  int QInputDialog::intMinimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog10intMinimumEv(const QInputDialog *self) {
  return self->intMinimum();
}

//  void QInputDialog::setIntMaximum(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setIntMaximumEi(QInputDialog *self, int max) {
  self->setIntMaximum(max);
}

//  int QInputDialog::intMaximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog10intMaximumEv(const QInputDialog *self) {
  return self->intMaximum();
}

//  void QInputDialog::setIntRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog11setIntRangeEii(
    QInputDialog *self,
    int min,
    int max) {
  self->setIntRange(min, max);
}

//  void QInputDialog::setIntStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setIntStepEi(QInputDialog *self, int step) {
  self->setIntStep(step);
}

//  int QInputDialog::intStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog7intStepEv(const QInputDialog *self) {
  return self->intStep();
}

//  void QInputDialog::setDoubleValue(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog14setDoubleValueEd(
    QInputDialog *self,
    double value) {
  self->setDoubleValue(value);
}

//  double QInputDialog::doubleValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog11doubleValueEv(const QInputDialog *self) {
  return self->doubleValue();
}

//  void QInputDialog::setDoubleMinimum(double min)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog16setDoubleMinimumEd(
    QInputDialog *self,
    double min) {
  self->setDoubleMinimum(min);
}

//  double QInputDialog::doubleMinimum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog13doubleMinimumEv(const QInputDialog *self) {
  return self->doubleMinimum();
}

//  void QInputDialog::setDoubleMaximum(double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog16setDoubleMaximumEd(
    QInputDialog *self,
    double max) {
  self->setDoubleMaximum(max);
}

//  double QInputDialog::doubleMaximum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog13doubleMaximumEv(const QInputDialog *self) {
  return self->doubleMaximum();
}

//  void QInputDialog::setDoubleRange(double min, double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog14setDoubleRangeEdd(
    QInputDialog *self,
    double min,
    double max) {
  self->setDoubleRange(min, max);
}

//  void QInputDialog::setDoubleDecimals(int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog17setDoubleDecimalsEi(
    QInputDialog *self,
    int decimals) {
  self->setDoubleDecimals(decimals);
}

//  int QInputDialog::doubleDecimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog14doubleDecimalsEv(const QInputDialog *self) {
  return self->doubleDecimals();
}

//  void QInputDialog::setOkButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog15setOkButtonTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setOkButtonText(*text);
}

//  QString QInputDialog::okButtonText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog12okButtonTextEv(const QInputDialog *self) {
  return new QString(self->okButtonText());
}

//  void QInputDialog::setCancelButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog19setCancelButtonTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setCancelButtonText(*text);
}

//  QString QInputDialog::cancelButtonText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog16cancelButtonTextEv(
    const QInputDialog *self) {
  return new QString(self->cancelButtonText());
}

//  void QInputDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog4openEP7QObjectPKc(
    QInputDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  QSize QInputDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QInputDialog15minimumSizeHintEv(
    const QInputDialog *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSize QInputDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QInputDialog8sizeHintEv(const QInputDialog *self) {
  return new QSize(self->sizeHint());
}

//  void QInputDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setVisibleEb(
    QInputDialog *self,
    bool visible) {
  self->setVisible(visible);
}

//  QString QInputDialog::getText(QWidget *parent, const QString &title,
//      const QString &label, QLineEdit::EchoMode echo, const QString &text,
//      bool *ok, Qt::WindowFlags flags, Qt::InputMethodHints
//      inputMethodHints)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog7getTextEP7QWidgetRK7QStringS4_N9QLineEdit8EchoModeES4_Pb6QFlagsIN2Qt10WindowTypeEES8_INS9_15InputMethodHintEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    QLineEdit::EchoMode echo,
    const QString *text,
    bool *ok,
    int flags,
    int inputMethodHints) {
  return new QString(
      QInputDialog::getText(
          parent,
          *title,
          *label,
          echo,
          *text,
          ok,
          QFlags<Qt::WindowType>::fromInt(flags),
          QFlags<Qt::InputMethodHint>::fromInt(inputMethodHints)));
}

//  QString QInputDialog::getMultiLineText(QWidget *parent, const QString
//      &title, const QString &label, const QString &text, bool *ok,
//      Qt::WindowFlags flags, Qt::InputMethodHints inputMethodHints)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog16getMultiLineTextEP7QWidgetRK7QStringS4_S4_Pb6QFlagsIN2Qt10WindowTypeEES6_INS7_15InputMethodHintEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    const QString *text,
    bool *ok,
    int flags,
    int inputMethodHints) {
  return new QString(
      QInputDialog::getMultiLineText(
          parent,
          *title,
          *label,
          *text,
          ok,
          QFlags<Qt::WindowType>::fromInt(flags),
          QFlags<Qt::InputMethodHint>::fromInt(inputMethodHints)));
}

//  int QInputDialog::getInt(QWidget *parent, const QString &title, const
//      QString &label, int value, int minValue, int maxValue, int step, bool
//      *ok, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QInputDialog6getIntEP7QWidgetRK7QStringS4_iiiiPb6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    int value,
    int minValue,
    int maxValue,
    int step,
    bool *ok,
    int flags) {
  return QInputDialog::getInt(
      parent,
      *title,
      *label,
      value,
      minValue,
      maxValue,
      step,
      ok,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  double QInputDialog::getDouble(QWidget *parent, const QString &title,
//      const QString &label, double value, double minValue, double maxValue,
//      int decimals, bool *ok, Qt::WindowFlags flags, double step)
extern "C" Q_DECL_EXPORT
double ritual_ZN12QInputDialog9getDoubleEP7QWidgetRK7QStringS4_dddiPb6QFlagsIN2Qt10WindowTypeEEd(
    QWidget *parent,
    const QString *title,
    const QString *label,
    double value,
    double minValue,
    double maxValue,
    int decimals,
    bool *ok,
    int flags,
    double step) {
  return QInputDialog::getDouble(
      parent,
      *title,
      *label,
      value,
      minValue,
      maxValue,
      decimals,
      ok,
      QFlags<Qt::WindowType>::fromInt(flags),
      step);
}

//  void QInputDialog::setDoubleStep(double step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setDoubleStepEd(
    QInputDialog *self,
    double step) {
  self->setDoubleStep(step);
}

//  double QInputDialog::doubleStep() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog10doubleStepEv(const QInputDialog *self) {
  return self->doubleStep();
}

//  void QInputDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog4doneEi(QInputDialog *self, int result) {
  self->done(result);
}
