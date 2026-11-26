//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/QSharedPointer>

//  QMessageDialogOptions::QMessageDialogOptions(QMessageDialogOptionsPrivate
//      *dd)
extern "C" Q_DECL_EXPORT
QMessageDialogOptions *ritual_ZN21QMessageDialogOptionsC1EP28QMessageDialogOptionsPrivate(
    QMessageDialogOptionsPrivate *dd) {
  return new QMessageDialogOptions(dd);
}

//  QMessageDialogOptions::~QMessageDialogOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptionsD1Ev(QMessageDialogOptions *self) {
  delete self;
}

//  QSharedPointer<QMessageDialogOptions> QMessageDialogOptions::create()
extern "C" Q_DECL_EXPORT
QSharedPointer<QMessageDialogOptions> *ritual_ZN21QMessageDialogOptions6createEv() {
  return new QSharedPointer<QMessageDialogOptions>(
      QMessageDialogOptions::create());
}

//  QSharedPointer<QMessageDialogOptions> QMessageDialogOptions::clone()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<QMessageDialogOptions> *ritual_ZNK21QMessageDialogOptions5cloneEv(
    const QMessageDialogOptions *self) {
  return new QSharedPointer<QMessageDialogOptions>(self->clone());
}

//  QString QMessageDialogOptions::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMessageDialogOptions11windowTitleEv(
    const QMessageDialogOptions *self) {
  return new QString(self->windowTitle());
}

//  void QMessageDialogOptions::setWindowTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions14setWindowTitleERK7QString(
    QMessageDialogOptions *self,
    const QString *a0) {
  self->setWindowTitle(*a0);
}

//  void QMessageDialogOptions::setStandardIcon(StandardIcon icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions15setStandardIconENS_12StandardIconE(
    QMessageDialogOptions *self,
    QMessageDialogOptions::StandardIcon icon) {
  self->setStandardIcon(icon);
}

//  StandardIcon QMessageDialogOptions::standardIcon() const
extern "C" Q_DECL_EXPORT
QMessageDialogOptions::StandardIcon ritual_ZNK21QMessageDialogOptions12standardIconEv(
    const QMessageDialogOptions *self) {
  return self->standardIcon();
}

//  void QMessageDialogOptions::setIconPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions13setIconPixmapERK7QPixmap(
    QMessageDialogOptions *self,
    const QPixmap *pixmap) {
  self->setIconPixmap(*pixmap);
}

//  QPixmap QMessageDialogOptions::iconPixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK21QMessageDialogOptions10iconPixmapEv(
    const QMessageDialogOptions *self) {
  return new QPixmap(self->iconPixmap());
}

//  void QMessageDialogOptions::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions7setTextERK7QString(
    QMessageDialogOptions *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QMessageDialogOptions::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMessageDialogOptions4textEv(
    const QMessageDialogOptions *self) {
  return new QString(self->text());
}

//  void QMessageDialogOptions::setInformativeText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions18setInformativeTextERK7QString(
    QMessageDialogOptions *self,
    const QString *text) {
  self->setInformativeText(*text);
}

//  QString QMessageDialogOptions::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMessageDialogOptions15informativeTextEv(
    const QMessageDialogOptions *self) {
  return new QString(self->informativeText());
}

//  void QMessageDialogOptions::setDetailedText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions15setDetailedTextERK7QString(
    QMessageDialogOptions *self,
    const QString *text) {
  self->setDetailedText(*text);
}

//  QString QMessageDialogOptions::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMessageDialogOptions12detailedTextEv(
    const QMessageDialogOptions *self) {
  return new QString(self->detailedText());
}

//  void QMessageDialogOptions::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions9setOptionENS_6OptionEb(
    QMessageDialogOptions *self,
    QMessageDialogOptions::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMessageDialogOptions::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QMessageDialogOptions10testOptionENS_6OptionE(
    const QMessageDialogOptions *self,
    QMessageDialogOptions::Option option) {
  return self->testOption(option);
}

//  void QMessageDialogOptions::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions10setOptionsE6QFlagsINS_6OptionEE(
    QMessageDialogOptions *self,
    int options) {
  self->setOptions(QFlags<QMessageDialogOptions::Option>::fromInt(options));
}

//  Options QMessageDialogOptions::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMessageDialogOptions7optionsEv(
    const QMessageDialogOptions *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QMessageDialogOptions::setStandardButtons(QPlatformDialogHelper::Sta
//      ndardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions18setStandardButtonsE6QFlagsIN21QPlatformDialogHelper14StandardButtonEE(
    QMessageDialogOptions *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QPlatformDialogHelper::StandardButton>::fromInt(buttons));
}

//  QPlatformDialogHelper::StandardButtons
//      QMessageDialogOptions::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMessageDialogOptions15standardButtonsEv(
    const QMessageDialogOptions *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  int QMessageDialogOptions::addButton(const QString &label,
//      QPlatformDialogHelper::ButtonRole role, void *buttonImpl, int
//      buttonId)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QMessageDialogOptions9addButtonERK7QStringN21QPlatformDialogHelper10ButtonRoleEPvi(
    QMessageDialogOptions *self,
    const QString *label,
    QPlatformDialogHelper::ButtonRole role,
    void *buttonImpl,
    int buttonId) {
  return self->addButton(*label, role, buttonImpl, buttonId);
}

//  void QMessageDialogOptions::removeButton(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions12removeButtonEi(
    QMessageDialogOptions *self,
    int id) {
  self->removeButton(id);
}

//  const QList<CustomButton> &QMessageDialogOptions::customButtons()
extern "C" Q_DECL_EXPORT
const QList<QMessageDialogOptions::CustomButton> *ritual_ZN21QMessageDialogOptions13customButtonsEv(
    QMessageDialogOptions *self) {
  return &(self->customButtons());
}

//  const CustomButton *QMessageDialogOptions::customButton(int id)
extern "C" Q_DECL_EXPORT
const QMessageDialogOptions::CustomButton *ritual_ZN21QMessageDialogOptions12customButtonEi(
    QMessageDialogOptions *self,
    int id) {
  return self->customButton(id);
}

//  void QMessageDialogOptions::clearCustomButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions18clearCustomButtonsEv(
    QMessageDialogOptions *self) {
  self->clearCustomButtons();
}

//  void QMessageDialogOptions::setCheckBox(const QString &label,
//      Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions11setCheckBoxERK7QStringN2Qt10CheckStateE(
    QMessageDialogOptions *self,
    const QString *label,
    Qt::CheckState state) {
  self->setCheckBox(*label, state);
}

//  QString QMessageDialogOptions::checkBoxLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMessageDialogOptions13checkBoxLabelEv(
    const QMessageDialogOptions *self) {
  return new QString(self->checkBoxLabel());
}

//  Qt::CheckState QMessageDialogOptions::checkBoxState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK21QMessageDialogOptions13checkBoxStateEv(
    const QMessageDialogOptions *self) {
  return self->checkBoxState();
}

//  void QMessageDialogOptions::setEscapeButton(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions15setEscapeButtonEi(
    QMessageDialogOptions *self,
    int id) {
  self->setEscapeButton(id);
}

//  int QMessageDialogOptions::escapeButton() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMessageDialogOptions12escapeButtonEv(
    const QMessageDialogOptions *self) {
  return self->escapeButton();
}

//  void QMessageDialogOptions::setDefaultButton(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMessageDialogOptions16setDefaultButtonEi(
    QMessageDialogOptions *self,
    int id) {
  self->setDefaultButton(id);
}

//  int QMessageDialogOptions::defaultButton() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QMessageDialogOptions13defaultButtonEv(
    const QMessageDialogOptions *self) {
  return self->defaultButton();
}

//  a QSharedPointer<QMessageDialogOptions> a ritual of QMessageDialogOptions
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMessageDialogOptions__QSharedPointer_QMessageDialogOptions(
    QSharedPointer<QMessageDialogOptions> *self) {
  delete self;
}
