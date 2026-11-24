//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickmessagedialog_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickmessagedialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickMessageDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMessageDialog : QQuickMessageDialog {
  using QQuickMessageDialog::onCreate;
  using QQuickMessageDialog::onShow;
  using QQuickMessageDialog::dialogCode;
};

//  const QMetaObject *QQuickMessageDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickMessageDialog10metaObjectEv(
    const QQuickMessageDialog *self) {
  return self->metaObject();
}

//  QString QQuickMessageDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickMessageDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMessageDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickMessageDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN19QQuickMessageDialog20qmlExtendedNamespaceEv() {
  return QQuickMessageDialog::qmlExtendedNamespace();
}

//  void QQuickMessageDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickMessageDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickMessageDialog::QQuickMessageDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMessageDialog *ritual_ZN19QQuickMessageDialogC1EP7QObject(
    QObject *parent) {
  return new QQuickMessageDialog(parent);
}

//  QString QQuickMessageDialog::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickMessageDialog4textEv(
    const QQuickMessageDialog *self) {
  return new QString(self->text());
}

//  void QQuickMessageDialog::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog7setTextERK7QString(
    QQuickMessageDialog *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QQuickMessageDialog::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickMessageDialog15informativeTextEv(
    const QQuickMessageDialog *self) {
  return new QString(self->informativeText());
}

//  void QQuickMessageDialog::setInformativeText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog18setInformativeTextERK7QString(
    QQuickMessageDialog *self,
    const QString *text) {
  self->setInformativeText(*text);
}

//  QString QQuickMessageDialog::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickMessageDialog12detailedTextEv(
    const QQuickMessageDialog *self) {
  return new QString(self->detailedText());
}

//  void QQuickMessageDialog::setDetailedText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog15setDetailedTextERK7QString(
    QQuickMessageDialog *self,
    const QString *text) {
  self->setDetailedText(*text);
}

//  QPlatformDialogHelper::StandardButtons QQuickMessageDialog::buttons()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMessageDialog7buttonsEv(
    const QQuickMessageDialog *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  void
//      QQuickMessageDialog::setButtons(QPlatformDialogHelper::StandardButton
//      s buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog10setButtonsE6QFlagsIN21QPlatformDialogHelper14StandardButtonEE(
    QQuickMessageDialog *self,
    int buttons) {
  self->setButtons(
      QFlags<QPlatformDialogHelper::StandardButton>::fromInt(buttons));
}

//  void
//      QQuickMessageDialog::handleClick(QPlatformDialogHelper::StandardButto
//      n button, QPlatformDialogHelper::ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog11handleClickEN21QPlatformDialogHelper14StandardButtonENS0_10ButtonRoleE(
    QQuickMessageDialog *self,
    QPlatformDialogHelper::StandardButton button,
    QPlatformDialogHelper::ButtonRole role) {
  self->handleClick(button, role);
}

//  void QQuickMessageDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog8onCreateEP21QPlatformDialogHelper(
    QQuickMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickMessageDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  int QQuickMessageDialog::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickMessageDialog10dialogCodeEv(
    const QQuickMessageDialog *self) {
  return self->dialogCode();
}

//  void QQuickMessageDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickMessageDialog8onCreateEP21QPlatformDialogHelper(
    QQuickMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickMessageDialog *>(self)->OwnQQuickMessageDialog::onCreate(
      dialog);
}

//  void QQuickMessageDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickMessageDialog *>(self)->OwnQQuickMessageDialog::onShow(
      dialog);
}

//  int QQuickMessageDialog::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickMessageDialog10dialogCodeEv(
    const QQuickMessageDialog *self) {
  return static_cast<const OwnQQuickMessageDialog *>(self)->OwnQQuickMessageDialog::dialogCode();
}
