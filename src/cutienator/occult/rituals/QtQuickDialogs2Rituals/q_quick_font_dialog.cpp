//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfontdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfontdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickFontDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFontDialog : QQuickFontDialog {
  using QQuickFontDialog::useNativeDialog;
  using QQuickFontDialog::onCreate;
  using QQuickFontDialog::onShow;
};

//  const QMetaObject *QQuickFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFontDialog10metaObjectEv(
    const QQuickFontDialog *self) {
  return self->metaObject();
}

//  QString QQuickFontDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickFontDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickFontDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN16QQuickFontDialog20qmlExtendedNamespaceEv() {
  return QQuickFontDialog::qmlExtendedNamespace();
}

//  void QQuickFontDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickFontDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickFontDialog::QQuickFontDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFontDialog *ritual_ZN16QQuickFontDialogC1EP7QObject(QObject *parent) {
  return new QQuickFontDialog(parent);
}

//  void QQuickFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog14setCurrentFontERK5QFont(
    QQuickFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}

//  QFont QQuickFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QQuickFontDialog11currentFontEv(
    const QQuickFontDialog *self) {
  return new QFont(self->currentFont());
}

//  void QQuickFontDialog::setSelectedFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog15setSelectedFontERK5QFont(
    QQuickFontDialog *self,
    const QFont *font) {
  self->setSelectedFont(*font);
}

//  QFont QQuickFontDialog::selectedFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QQuickFontDialog12selectedFontEv(
    const QQuickFontDialog *self) {
  return new QFont(self->selectedFont());
}

//  QFontDialogOptions::FontDialogOptions QQuickFontDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickFontDialog7optionsEv(const QQuickFontDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QQuickFontDialog::setOptions(QFontDialogOptions::FontDialogOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog10setOptionsE6QFlagsIN18QFontDialogOptions16FontDialogOptionEE(
    QQuickFontDialog *self,
    int options) {
  self->setOptions(
      QFlags<QFontDialogOptions::FontDialogOption>::fromInt(options));
}

//  void QQuickFontDialog::resetOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog12resetOptionsEv(QQuickFontDialog *self) {
  self->resetOptions();
}

//  bool QQuickFontDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickFontDialog15useNativeDialogEv(
    const QQuickFontDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickFontDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFontDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickFontDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontDialog6onShowEP21QPlatformDialogHelper(
    QQuickFontDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  bool QQuickFontDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QQuickFontDialog15useNativeDialogEv(
    const QQuickFontDialog *self) {
  return static_cast<const OwnQQuickFontDialog *>(self)->OwnQQuickFontDialog::useNativeDialog();
}

//  void QQuickFontDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFontDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFontDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFontDialog *>(self)->OwnQQuickFontDialog::onCreate(
      dialog);
}

//  void QQuickFontDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFontDialog6onShowEP21QPlatformDialogHelper(
    QQuickFontDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFontDialog *>(self)->OwnQQuickFontDialog::onShow(
      dialog);
}
