//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmessagebox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>

//  const QMetaObject *QMessageBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMessageBox10metaObjectEv(
    const QMessageBox *self) {
  return self->metaObject();
}

//  QString QMessageBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QMessageBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMessageBox::tr(s, c, n));
}

//  QMessageBox::QMessageBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1EP7QWidget(QWidget *parent) {
  return new QMessageBox(parent);
}

//  QMessageBox::QMessageBox(Icon icon, const QString &title, const QString
//      &text, StandardButtons buttons, QWidget *parent, Qt::WindowFlags
//      flags)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1ENS_4IconERK7QStringS3_6QFlagsINS_14StandardButtonEEP7QWidgetS4_IN2Qt10WindowTypeEE(
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    int buttons,
    QWidget *parent,
    int flags) {
  return new QMessageBox(
      icon,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMessageBox::~QMessageBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBoxD1Ev(QMessageBox *self) {
  delete self;
}

//  void QMessageBox::addButton(QAbstractButton *button, ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox9addButtonEP15QAbstractButtonNS_10ButtonRoleE(
    QMessageBox *self,
    QAbstractButton *button,
    QMessageBox::ButtonRole role) {
  self->addButton(button, role);
}

//  QPushButton *QMessageBox::addButton(const QString &text, ButtonRole role)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QMessageBox9addButtonERK7QStringNS_10ButtonRoleE(
    QMessageBox *self,
    const QString *text,
    QMessageBox::ButtonRole role) {
  return self->addButton(*text, role);
}

//  QPushButton *QMessageBox::addButton(StandardButton button)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QMessageBox9addButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  return self->addButton(button);
}

//  void QMessageBox::removeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox12removeButtonEP15QAbstractButton(
    QMessageBox *self,
    QAbstractButton *button) {
  self->removeButton(button);
}

//  void QMessageBox::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox4openEP7QObjectPKc(
    QMessageBox *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  ButtonRole QMessageBox::buttonRole(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QMessageBox::ButtonRole ritual_ZNK11QMessageBox10buttonRoleEP15QAbstractButton(
    const QMessageBox *self,
    QAbstractButton *button) {
  return self->buttonRole(button);
}

//  void QMessageBox::setStandardButtons(StandardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox18setStandardButtonsE6QFlagsINS_14StandardButtonEE(
    QMessageBox *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QMessageBox::StandardButton>::fromInt(buttons));
}

//  StandardButtons QMessageBox::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox15standardButtonsEv(const QMessageBox *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  StandardButton QMessageBox::standardButton(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZNK11QMessageBox14standardButtonEP15QAbstractButton(
    const QMessageBox *self,
    QAbstractButton *button) {
  return self->standardButton(button);
}

//  QAbstractButton *QMessageBox::button(StandardButton which) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox6buttonENS_14StandardButtonE(
    const QMessageBox *self,
    QMessageBox::StandardButton which) {
  return self->button(which);
}

//  QPushButton *QMessageBox::defaultButton() const
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZNK11QMessageBox13defaultButtonEv(
    const QMessageBox *self) {
  return self->defaultButton();
}

//  void QMessageBox::setDefaultButton(QPushButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox16setDefaultButtonEP11QPushButton(
    QMessageBox *self,
    QPushButton *button) {
  self->setDefaultButton(button);
}

//  void QMessageBox::setDefaultButton(StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox16setDefaultButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  self->setDefaultButton(button);
}

//  QAbstractButton *QMessageBox::escapeButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox12escapeButtonEv(
    const QMessageBox *self) {
  return self->escapeButton();
}

//  void QMessageBox::setEscapeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setEscapeButtonEP15QAbstractButton(
    QMessageBox *self,
    QAbstractButton *button) {
  self->setEscapeButton(button);
}

//  void QMessageBox::setEscapeButton(StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setEscapeButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  self->setEscapeButton(button);
}

//  QAbstractButton *QMessageBox::clickedButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox13clickedButtonEv(
    const QMessageBox *self) {
  return self->clickedButton();
}

//  QString QMessageBox::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox4textEv(const QMessageBox *self) {
  return new QString(self->text());
}

//  void QMessageBox::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7setTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setText(*text);
}

//  Icon QMessageBox::icon() const
extern "C" Q_DECL_EXPORT
QMessageBox::Icon ritual_ZNK11QMessageBox4iconEv(const QMessageBox *self) {
  return self->icon();
}

//  void QMessageBox::setIcon(Icon a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7setIconENS_4IconE(
    QMessageBox *self,
    QMessageBox::Icon a0) {
  self->setIcon(a0);
}

//  QPixmap QMessageBox::iconPixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QMessageBox10iconPixmapEv(const QMessageBox *self) {
  return new QPixmap(self->iconPixmap());
}

//  void QMessageBox::setIconPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setIconPixmapERK7QPixmap(
    QMessageBox *self,
    const QPixmap *pixmap) {
  self->setIconPixmap(*pixmap);
}

//  Qt::TextFormat QMessageBox::textFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK11QMessageBox10textFormatEv(
    const QMessageBox *self) {
  return self->textFormat();
}

//  void QMessageBox::setTextFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setTextFormatEN2Qt10TextFormatE(
    QMessageBox *self,
    Qt::TextFormat format) {
  self->setTextFormat(format);
}

//  void QMessageBox::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QMessageBox *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QMessageBox::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox20textInteractionFlagsEv(
    const QMessageBox *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QMessageBox::setCheckBox(QCheckBox *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox11setCheckBoxEP9QCheckBox(
    QMessageBox *self,
    QCheckBox *cb) {
  self->setCheckBox(cb);
}

//  QCheckBox *QMessageBox::checkBox() const
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZNK11QMessageBox8checkBoxEv(const QMessageBox *self) {
  return self->checkBox();
}

//  void QMessageBox::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox9setOptionENS_6OptionEb(
    QMessageBox *self,
    QMessageBox::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMessageBox::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMessageBox10testOptionENS_6OptionE(
    const QMessageBox *self,
    QMessageBox::Option option) {
  return self->testOption(option);
}

//  void QMessageBox::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox10setOptionsE6QFlagsINS_6OptionEE(
    QMessageBox *self,
    int options) {
  self->setOptions(QFlags<QMessageBox::Option>::fromInt(options));
}

//  Options QMessageBox::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox7optionsEv(const QMessageBox *self) {
  return static_cast<int>(self->options().toInt());
}

//  StandardButton QMessageBox::information(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  StandardButton QMessageBox::information(QWidget *parent, const QString
//      &title, const QString &text, StandardButton button0, StandardButton
//      button1)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::information(parent, *title, *text, button0, button1);
}

//  StandardButton QMessageBox::question(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::question(parent, *title, *text, button0, button1);
}

//  StandardButton QMessageBox::warning(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::warning(parent, *title, *text, button0, button1);
}

//  StandardButton QMessageBox::critical(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::critical(parent, *title, *text, button0, button1);
}

//  void QMessageBox::about(QWidget *parent, const QString &title, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox5aboutEP7QWidgetRK7QStringS4_(
    QWidget *parent,
    const QString *title,
    const QString *text) {
  QMessageBox::about(parent, *title, *text);
}

//  void QMessageBox::aboutQt(QWidget *parent, const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7aboutQtEP7QWidgetRK7QString(
    QWidget *parent,
    const QString *title) {
  QMessageBox::aboutQt(parent, *title);
}

//  QMessageBox::QMessageBox(const QString &title, const QString &text, Icon
//      icon, int button0, int button1, int button2, QWidget *parent,
//      Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1ERK7QStringS2_NS_4IconEiiiP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *title,
    const QString *text,
    QMessageBox::Icon icon,
    int button0,
    int button1,
    int button2,
    QWidget *parent,
    int f) {
  return new QMessageBox(
      *title,
      *text,
      icon,
      button0,
      button1,
      button2,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  int QMessageBox::information(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}

//  int QMessageBox::information(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}

//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}

//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}

//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}

//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}

//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}

//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}

//  QString QMessageBox::buttonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox10buttonTextEi(
    const QMessageBox *self,
    int button) {
  return new QString(self->buttonText(button));
}

//  void QMessageBox::setButtonText(int button, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setButtonTextEiRK7QString(
    QMessageBox *self,
    int button,
    const QString *text) {
  self->setButtonText(button, *text);
}

//  QString QMessageBox::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox15informativeTextEv(
    const QMessageBox *self) {
  return new QString(self->informativeText());
}

//  void QMessageBox::setInformativeText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox18setInformativeTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setInformativeText(*text);
}

//  QString QMessageBox::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox12detailedTextEv(const QMessageBox *self) {
  return new QString(self->detailedText());
}

//  void QMessageBox::setDetailedText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setDetailedTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setDetailedText(*text);
}

//  void QMessageBox::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox14setWindowTitleERK7QString(
    QMessageBox *self,
    const QString *title) {
  self->setWindowTitle(*title);
}

//  void QMessageBox::setWindowModality(Qt::WindowModality windowModality)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox17setWindowModalityEN2Qt14WindowModalityE(
    QMessageBox *self,
    Qt::WindowModality windowModality) {
  self->setWindowModality(windowModality);
}

//  QPixmap QMessageBox::standardIcon(Icon icon)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QMessageBox12standardIconENS_4IconE(
    QMessageBox::Icon icon) {
  return new QPixmap(QMessageBox::standardIcon(icon));
}
