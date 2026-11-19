//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QDialogButtonBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDialogButtonBox10metaObjectEv(
    const QDialogButtonBox *self) {
  return self->metaObject();
}

//  QString QDialogButtonBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDialogButtonBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDialogButtonBox::tr(s, c, n));
}

//  QDialogButtonBox::QDialogButtonBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1EP7QWidget(QWidget *parent) {
  return new QDialogButtonBox(parent);
}

//  QDialogButtonBox::QDialogButtonBox(Qt::Orientation orientation, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new QDialogButtonBox(orientation, parent);
}

//  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEP7QWidget(
    int buttons,
    QWidget *parent) {
  return new QDialogButtonBox(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons),
      parent);
}

//  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons,
//      Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEN2Qt11OrientationEP7QWidget(
    int buttons,
    Qt::Orientation orientation,
    QWidget *parent) {
  return new QDialogButtonBox(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons),
      orientation,
      parent);
}

//  QDialogButtonBox::~QDialogButtonBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBoxD1Ev(QDialogButtonBox *self) {
  delete self;
}

//  void QDialogButtonBox::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox14setOrientationEN2Qt11OrientationE(
    QDialogButtonBox *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QDialogButtonBox::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK16QDialogButtonBox11orientationEv(
    const QDialogButtonBox *self) {
  return self->orientation();
}

//  void QDialogButtonBox::addButton(QAbstractButton *button, ButtonRole
//      role)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox9addButtonEP15QAbstractButtonNS_10ButtonRoleE(
    QDialogButtonBox *self,
    QAbstractButton *button,
    QDialogButtonBox::ButtonRole role) {
  self->addButton(button, role);
}

//  QPushButton *QDialogButtonBox::addButton(const QString &text, ButtonRole
//      role)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN16QDialogButtonBox9addButtonERK7QStringNS_10ButtonRoleE(
    QDialogButtonBox *self,
    const QString *text,
    QDialogButtonBox::ButtonRole role) {
  return self->addButton(*text, role);
}

//  QPushButton *QDialogButtonBox::addButton(StandardButton button)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN16QDialogButtonBox9addButtonENS_14StandardButtonE(
    QDialogButtonBox *self,
    QDialogButtonBox::StandardButton button) {
  return self->addButton(button);
}

//  void QDialogButtonBox::removeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox12removeButtonEP15QAbstractButton(
    QDialogButtonBox *self,
    QAbstractButton *button) {
  self->removeButton(button);
}

//  void QDialogButtonBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox5clearEv(QDialogButtonBox *self) {
  self->clear();
}

//  ButtonRole QDialogButtonBox::buttonRole(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QDialogButtonBox::ButtonRole ritual_ZNK16QDialogButtonBox10buttonRoleEP15QAbstractButton(
    const QDialogButtonBox *self,
    QAbstractButton *button) {
  return self->buttonRole(button);
}

//  void QDialogButtonBox::setStandardButtons(StandardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox18setStandardButtonsE6QFlagsINS_14StandardButtonEE(
    QDialogButtonBox *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons));
}

//  StandardButtons QDialogButtonBox::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDialogButtonBox15standardButtonsEv(
    const QDialogButtonBox *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  StandardButton QDialogButtonBox::standardButton(QAbstractButton *button)
//      const
extern "C" Q_DECL_EXPORT
QDialogButtonBox::StandardButton ritual_ZNK16QDialogButtonBox14standardButtonEP15QAbstractButton(
    const QDialogButtonBox *self,
    QAbstractButton *button) {
  return self->standardButton(button);
}

//  QPushButton *QDialogButtonBox::button(StandardButton which) const
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZNK16QDialogButtonBox6buttonENS_14StandardButtonE(
    const QDialogButtonBox *self,
    QDialogButtonBox::StandardButton which) {
  return self->button(which);
}

//  void QDialogButtonBox::setCenterButtons(bool center)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox16setCenterButtonsEb(
    QDialogButtonBox *self,
    bool center) {
  self->setCenterButtons(center);
}

//  bool QDialogButtonBox::centerButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDialogButtonBox13centerButtonsEv(
    const QDialogButtonBox *self) {
  return self->centerButtons();
}

//  QString QDialogButtonBox::standardButtonText(StandardButton button)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDialogButtonBox18standardButtonTextENS_14StandardButtonE(
    QDialogButtonBox::StandardButton button) {
  return new QString(QDialogButtonBox::standardButtonText(button));
}

//  QKeySequence QDialogButtonBox::standardButtonShortcut(StandardButton
//      button)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN16QDialogButtonBox22standardButtonShortcutENS_14StandardButtonE(
    QDialogButtonBox::StandardButton button) {
  return new QKeySequence(QDialogButtonBox::standardButtonShortcut(button));
}
